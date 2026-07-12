#!/usr/bin/env python3
"""Regenerate 2 rejected images for the 2026-07-12 slate:
  - zaidi-washington-fund/hero.jpg  (first pass rendered the Syrian 3-star flag
    instead of the Iraqi takbir flag → avoid the flag entirely: US flag + motorcade)
  - gene-cure-thalassemia/broll_1.jpg (first pass came out 90°-rotated → force upright)
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-12"
JOBS = [
    (f"{D}-zaidi-washington-fund", "hero.jpg", f"The White House South Portico at golden hour, a high-level state-visit arrival, a black armored motorcade of SUVs and a line of press photographers with cameras on the curved driveway, only a single American flag on the building, dramatic cinematic editorial wide shot, no other flags, no readable text, {NEG}"),
    (f"{D}-gene-cure-thalassemia", "broll_1.jpg", f"A bright modern gene-therapy laboratory, a scientist standing fully upright in white PPE coveralls and blue nitrile gloves, holding a small vial of edited cells up to the light, straight upright vertical portrait orientation, head at top and feet at bottom, blue lab lighting, advanced biotechnology, cinematic editorial, no readable text, {NEG}"),
]


def main():
    jobs = []
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.5)
    pending = [j for j in jobs if j.get("tid")]
    deadline = time.time() + 15 * 60
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
                    print(f"  OK {j['slug']}/{j['file']}  {download(url, j['out'])}", flush=True)
                    j["ok"] = True
                else:
                    print(f"  ? {j['slug']}/{j['file']}: no url", flush=True)
            elif st == "fail":
                print(f"  X {j['slug']}/{j['file']}: {data.get('failMsg','?')}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"== fix done: {ok}/{len(JOBS)} ==", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
