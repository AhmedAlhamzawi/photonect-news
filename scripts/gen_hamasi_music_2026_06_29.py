#!/usr/bin/env python3
"""Generate one energetic (حماسي) instrumental bed for the Iraq special reels via KIE/Suno.
Downloads → my-video/public/audio/mood_hamasi.mp3 (take 1)."""
from __future__ import annotations
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

KIE = "https://api.kie.ai"
GEN = f"{KIE}/api/v1/generate"
INFO = f"{KIE}/api/v1/generate/record-info"
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
POLL, MAX_MIN = 12, 12
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "my-video" / "public" / "audio" / "mood_hamasi.mp3"
STYLE = ("epic energetic Middle Eastern Iraqi anthem, driving taut percussion, powerful brass and "
         "strings, urgent heroic momentum, breaking-news intensity, motivational حماسي, cinematic, instrumental")
PROMPT = ("A rousing, energetic, epic Arabic/Iraqi instrumental for a breaking-news investigative report: "
          "driving percussion, bold brass stabs, soaring strings, urgent heroic momentum, no vocals.")


def key():
    for envf in (ROOT/".env", ROOT/".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_AI_API_KEY\s*=\s*(.+)\s*$", line)
                if m: return m.group(1).strip().strip('"').strip("'")
    return os.environ.get("KIE_AI_API_KEY")


def post(u, b, k):
    r = urllib.request.Request(u, data=json.dumps(b).encode(), method="POST",
        headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(r, timeout=30).read().decode())


def get(u, k):
    r = urllib.request.Request(u, headers={"Authorization": f"Bearer {k}", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(r, timeout=30).read().decode())


def main():
    k = key()
    if not k: sys.exit("no KIE key")
    body = {"prompt": PROMPT, "model": "V5", "customMode": True, "instrumental": True,
            "style": STYLE[:200], "title": "Photonect Hamasi Bed", "callBackUrl": CALLBACK}
    r = post(GEN, body, k)
    if r.get("code") != 200: sys.exit(f"submit failed: {r}")
    tid = (r.get("data") or {}).get("taskId")
    print(f"taskId {tid}", flush=True)
    deadline = time.time() + MAX_MIN*60
    while time.time() < deadline:
        time.sleep(POLL)
        try: d = (get(f"{INFO}?taskId={tid}", k).get("data") or {})
        except Exception as e: print("poll err", e); continue
        st = d.get("status");
        if st == "SUCCESS":
            clips = (d.get("response") or {}).get("sunoData") or []
            url = clips[0].get("audioUrl") if clips else None
            if not url: continue
            OUT.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["curl","-sL","--retry","3","--max-time","240","-A","Mozilla/5.0",url,"-o",str(OUT)], check=False)
            print(f"saved {OUT} ({OUT.stat().st_size//1024} KB, {clips[0].get('duration')}s)")
            return 0
        if st in {"CREATE_TASK_FAILED","GENERATE_AUDIO_FAILED","SENSITIVE_WORD_ERROR","CALLBACK_EXCEPTION"}:
            sys.exit(f"failed: {st}")
        print(f"  {st}", flush=True)
    sys.exit("timeout")


if __name__ == "__main__":
    sys.exit(main())
