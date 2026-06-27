#!/usr/bin/env python3
"""Generate the MSA-rap VO track for the Development Road essay via Suno (KIE).

Concatenates all 7 beats' arabic_vo into one custom-lyric vocal track. Returns
~2 clips; downloads both to data/essay-faw-road/audio/. The exact words are
carried by the on-screen captions regardless of Suno's phrasing, so the track
is the energy/voice; timing is fit per-beat in the Remotion engine.
"""
from __future__ import annotations
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

KIE = "https://api.kie.ai"
GEN = f"{KIE}/api/v1/generate"
INFO = f"{KIE}/api/v1/generate/record-info"
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
POLL, MAX_MIN = 12, 12
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "data" / "essay-faw-road" / "script.json"
OUT = ROOT / "data" / "essay-faw-road" / "audio"
STYLE = ("Arabic hip hop, Modern Standard Arabic, confident clear male rap vocal, "
         "serious analytical documentary tone, cinematic news beat, steady 90 bpm, "
         "minimal melodic, intelligible diction")


def load_key():
    for envf in (ROOT/".env", ROOT/".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_AI_API_KEY\s*=\s*(.+)\s*$", line)
                if m: return m.group(1).strip().strip('"').strip("'")
    return os.environ.get("KIE_AI_API_KEY")


def build_lyrics():
    segs = json.loads(SCRIPT.read_text())["segments"]
    parts = ["[Intro]\nفوتونكت... تحليل"]
    for s in segs:
        lines = s["arabic_vo"].replace(" / ", "\n")
        parts.append("[Verse]\n" + lines)
    return "\n\n".join(parts)


def post(url, body, key):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def get(url, key):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def curl_dl(url, dest, tries=4):
    dest.parent.mkdir(parents=True, exist_ok=True)
    for t in range(tries):
        subprocess.run(["curl", "-sL", "--retry", "3", "--max-time", "240", "-A", "Mozilla/5.0", url, "-o", str(dest)], check=False)
        if dest.is_file() and dest.stat().st_size > 200_000:
            return True
        time.sleep(3)
    return False


def main():
    key = load_key()
    if not key: sys.exit("no KIE key")
    OUT.mkdir(parents=True, exist_ok=True)
    lyrics = build_lyrics()
    # Persian-char guard
    bad = [c for c in lyrics if c in "یکپچژگ"]
    if bad: sys.exit(f"persian chars: {set(bad)}")
    print(f"━━━ Essay MSA-rap VO — {len(lyrics.splitlines())} lines ━━━")
    body = {"prompt": lyrics, "model": "V5", "customMode": True, "instrumental": False,
            "style": STYLE[:200], "title": "Photonect Essay - Tariq al-Tanmiya", "callBackUrl": CALLBACK}
    resp = post(GEN, body, key)
    if resp.get("code") != 200:
        sys.exit(f"submit failed: {resp}")
    tid = (resp.get("data") or {}).get("taskId")
    print(f"  taskId: {tid}")

    deadline = time.time() + MAX_MIN * 60
    last = None
    while time.time() < deadline:
        try:
            d = (get(f"{INFO}?taskId={tid}", key).get("data") or {})
        except Exception as e:
            print(f"      poll err: {e}"); time.sleep(POLL); continue
        st = d.get("status")
        if st != last:
            print(f"      status: {st}", flush=True); last = st
        if st == "SUCCESS":
            clips = (d.get("response") or {}).get("sunoData") or []
            man = []
            for i, c in enumerate(clips, 1):
                dest = OUT / f"rap_{i}.mp3"
                if c.get("audioUrl") and curl_dl(c["audioUrl"], dest):
                    print(f"      ✓ {dest.name} ({c.get('duration')}s)")
                    man.append({"file": dest.name, "duration": c.get("duration"), "url": c["audioUrl"]})
            (OUT / "_manifest.json").write_text(json.dumps(man, indent=2, ensure_ascii=False))
            print(f"\n✅ audio: {len(man)} take(s) → {OUT}")
            return 0
        if st in {"CREATE_TASK_FAILED", "GENERATE_AUDIO_FAILED", "SENSITIVE_WORD_ERROR", "CALLBACK_EXCEPTION"}:
            sys.exit(f"failed: {st}")
        time.sleep(POLL)
    sys.exit("timeout")


if __name__ == "__main__":
    sys.exit(main())
