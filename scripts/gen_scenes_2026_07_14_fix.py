#!/usr/bin/env python3
"""Regen the one 2026-07-14 image flagged sensitive: graft-gold-375kg/broll_2.
Softer, evidence-exhibit framing (no 'stuffed'/'broken wall' cues)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

HARD = "absolutely no readable text, no numbers, no letters, no user interface, no app screen, no news graphics, no watermark, no logos, no weapons"

JOBS = [
    ("2026-07-14-graft-gold-375kg", "broll_2.jpg",
     f"A police evidence table displaying neat bundles of US hundred-dollar banknotes beside several clear empty plastic water bottles arranged as exhibits under clean forensic lighting, an anti-corruption cash seizure where money was hidden in ordinary containers, blank bottles with no readable labels, {HARD}, {NEG}"),
]

def main():
    jobs = []
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        tid = submit(prompt)
        jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
        print(f"  + {slug}/{fname} tid={tid}", flush=True)
    pending = list(jobs)
    deadline = time.time() + 12 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception as e:
                if "402" in str(e):
                    print("  !! KIE 402", file=sys.stderr, flush=True); return 2
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if url:
                    print("  OK", j["slug"], j["file"], download(url, j["out"]), flush=True)
                    j["ok"] = True
            elif st == "fail":
                print(f"  X {j['file']}: {data.get('failMsg','?')}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    return 0 if all(j["ok"] for j in jobs) else 1

if __name__ == "__main__":
    sys.exit(main())
