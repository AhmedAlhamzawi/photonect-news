#!/usr/bin/env python3
"""Per-beat MSA-rap clips for the Development Road essay (intelligibility fix).

The single 42-line Suno gen slurred. Short clips enunciate (the test takes
proved it), and per-beat audio gives exact beat boundaries to sync captions to.
For each of the 7 beats: one Suno custom-lyric vocal clip, slow + clearly
enunciated. Downloads both takes → data/essay-faw-road/rap/beat_{i}_{role}_{take}.mp3
"""
from __future__ import annotations
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

KIE = "https://api.kie.ai"
GEN = f"{KIE}/api/v1/generate"
INFO = f"{KIE}/api/v1/generate/record-info"
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
POLL, MAX_MIN = 12, 13
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "data" / "essay-faw-road" / "script.json"
OUT = ROOT / "data" / "essay-faw-road" / "rap"
# Slow + clearly enunciated → maximises intelligibility (the cram was the failure).
STYLE = ("Arabic spoken-word rap, Modern Standard Arabic, slow deliberate delivery, "
         "very clear enunciation, every word distinct and intelligible, calm confident "
         "male voice, minimal melody, sparse cinematic boom-bap beat, 72 bpm, documentary tone")


def load_key():
    for envf in (ROOT/".env", ROOT/".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_AI_API_KEY\s*=\s*(.+)\s*$", line)
                if m: return m.group(1).strip().strip('"').strip("'")
    return os.environ.get("KIE_AI_API_KEY")


def post(url, body, key):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def get(url, key):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def curl_dl(url, dest, tries=4):
    dest.parent.mkdir(parents=True, exist_ok=True)
    for _ in range(tries):
        subprocess.run(["curl", "-sL", "--retry", "3", "--max-time", "240", "-A", "Mozilla/5.0", url, "-o", str(dest)], check=False)
        if dest.is_file() and dest.stat().st_size > 150_000:
            return True
        time.sleep(3)
    return False


def submit(lyrics, title, key):
    bad = [c for c in lyrics if c in "یکپچژگ"]
    if bad: raise SystemExit(f"persian chars in {title}: {set(bad)}")
    body = {"prompt": lyrics, "model": "V5", "customMode": True, "instrumental": False,
            "style": STYLE[:200], "title": title[:80], "callBackUrl": CALLBACK}
    r = post(GEN, body, key)
    if r.get("code") != 200:
        raise RuntimeError(f"submit failed: {r}")
    return (r.get("data") or {}).get("taskId")


def main():
    key = load_key()
    if not key: sys.exit("no KIE key")
    segs = json.loads(SCRIPT.read_text())["segments"]
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"━━━ per-beat MSA rap — {len(segs)} beats ━━━")

    tasks = []
    for i, s in enumerate(segs, 1):
        role = s["beat_role"]
        lyrics = "[Verse]\n" + s["arabic_vo"].replace(" / ", "\n")
        try:
            tid = submit(lyrics, f"Essay beat {i} {role}", key)
            print(f"  [{i}] {role} → {tid}")
            tasks.append((i, role, tid))
        except Exception as e:
            print(f"  [{i}] {role} SUBMIT FAIL: {e}")
        time.sleep(2)

    man = []
    for i, role, tid in tasks:
        print(f"\n  polling [{i}] {role} ({tid[:8]})")
        deadline = time.time() + MAX_MIN * 60
        done = False
        while time.time() < deadline:
            try:
                d = (get(f"{INFO}?taskId={tid}", key).get("data") or {})
            except Exception as e:
                print(f"      poll err: {e}"); time.sleep(POLL); continue
            st = d.get("status")
            if st == "SUCCESS":
                clips = (d.get("response") or {}).get("sunoData") or []
                for t, c in enumerate(clips, 1):
                    if c.get("audioUrl"):
                        dest = OUT / f"beat_{i}_{role}_{t}.mp3"
                        if curl_dl(c["audioUrl"], dest):
                            print(f"      ✓ {dest.name} ({c.get('duration')}s)")
                            man.append({"beat": i, "role": role, "take": t, "file": dest.name, "duration": c.get("duration")})
                done = True; break
            if st in {"CREATE_TASK_FAILED", "GENERATE_AUDIO_FAILED", "SENSITIVE_WORD_ERROR", "CALLBACK_EXCEPTION"}:
                print(f"      FAILED: {st}"); break
            time.sleep(POLL)
        if not done:
            print(f"      ✗ beat {i} no clip")

    (OUT / "_manifest.json").write_text(json.dumps(man, indent=2, ensure_ascii=False))
    print(f"\n✅ per-beat rap: {len(man)} clips → {OUT}")


if __name__ == "__main__":
    main()
