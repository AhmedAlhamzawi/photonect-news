#!/usr/bin/env python3
"""Regenerate the single KIE image that hit an internal error in the 2026-07-13 batch:
graft-oil-two-trillion/broll_3.jpg (oil refinery at dusk, wealth shadowed by graft)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

HARD = "absolutely no readable text, no numbers, no letters, no user interface, no app screen, no news graphics, no maps with labels, no watermark, no logos"

JOBS = [
    ("2026-07-13-graft-oil-two-trillion", "broll_3.jpg",
     f"A large oil refinery with distillation towers and a bright gas flare at dusk under a somber sky, national oil wealth shadowed by graft, industrial editorial wide shot, {HARD}, {NEG}"),
]


def main():
    jobs = []
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        tid = submit(prompt)
        jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
        print(f"  + {slug}/{fname} tid={tid}", flush=True)
    pending = list(jobs)
    deadline = time.time() + 15 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception as e:
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if url:
                    print(f"  OK {j['slug']}/{j['file']}  {download(url, j['out'])}", flush=True)
                    j["ok"] = True
            elif st == "fail":
                print(f"  X {j['slug']}/{j['file']}: {data.get('failMsg','?')} — resubmitting", file=sys.stderr, flush=True)
                j["tid"] = submit(JOBS[0][2]); still.append(j)
            else:
                still.append(j)
        pending = still
    return 0 if all(j["ok"] for j in jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
