#!/usr/bin/env python3
"""Regenerate two flagged 2026-07-02 scenes:
  worldcup/broll_1 (came back as a BASKETBALL — needs a real soccer ball)
  michael/broll_1  (garbled marquee lettering — needs blank signage)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage, no lettering, no digits")

WC = "2026-07-02-worldcup-r32-drama"
MJ = "2026-07-02-michael-biopic-record"

JOBS = [
    (WC, "broll_1.jpg", f"A dynamic cinematic action shot of two football (soccer) players in unmarked dark kits battling for a classic round black-and-white spotted association-football soccer ball mid-sprint on a pristine green grass pitch under bright stadium floodlights, the round soccer ball clearly in motion low on the grass, motion blur, intense competitive energy, {NEG}, {X}"),
    (MJ, "broll_1.jpg", f"A glamorous cinematic night red-carpet film premiere outside a grand classic theater, an elegant couple in formal black-tie wear walking a long red carpet past velvet ropes and brass stanchions, a crowd of formally dressed guests applauding, paparazzi flashbulbs firing brightly, warm golden theater bulb lights framing a completely blank unlit empty marquee with no lettering of any kind, Hollywood blockbuster event mood, {NEG}, {X}"),
]


def submit_retry(p, tries=5):
    last = None
    for i in range(tries):
        try: return submit(p)
        except Exception as e: last = e; time.sleep(3*(i+1))
    raise last


def main():
    jobs = []
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists():
            out.unlink()
        tid = submit_retry(prompt)
        jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
        print(f"  + {slug}/{fname} {tid}", flush=True)
        time.sleep(0.8)
    pending = list(jobs)
    deadline = time.time() + 12*60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try: r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception: still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url: still.append(j); continue
                try: download(url, j["out"]); j["ok"] = True; print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                except Exception as e: print(f"  ! dl: {e}", file=sys.stderr); still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr)
            else: still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== REGEN DONE {ok}/{len(JOBS)} ==", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
