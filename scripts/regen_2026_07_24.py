#!/usr/bin/env python3
"""Regenerate 2 rejected images from the 2026-07-24 slate.
  money-printing-25tn/broll_2 — prior output legibly said "FEDERAL RESERVE
    AUTHORITY" (wrong institution for an Iraq central-bank story) → no-signage central bank.
  water-heat-crisis/broll_3 — prior output was 90°-rotated (KIE quirk) → force upright portrait.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-24"
JOBS = [
    (f"{D}-money-printing-25tn", "broll_2.jpg",
     f"Exterior of an imposing modern Middle Eastern central-bank headquarters building with tall plain stone columns and a large unmarked stone facade under an overcast grey sky, monetary-authority theme, wide editorial architectural photography, absolutely no English or Latin text, no signage, no readable words or letters anywhere on the building, {NEG}"),
    (f"{D}-water-heat-crisis", "broll_3.jpg",
     f"Vertical portrait orientation, upright framing with the sky at the top and the cracked ground at the bottom: an old abandoned wooden fishing boat stranded on the sun-scorched cracked dry earth of a dried-up southern Iraqi marshland at midday, climate and drought disaster, tall 9:16 vertical composition, wide cinematic documentary shot, {NEG}"),
]


def main() -> int:
    jobs = []
    print(f"== Submitting {len(JOBS)} regen jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        tid = submit(prompt)
        jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
        print(f"  + {slug}/{fname} tid={tid}", flush=True)
        time.sleep(0.5)
    pending = list(jobs)
    deadline = time.time() + 20 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = (r.get("data") or {})
            url = first_image_url(data)
            state = str(data.get("state") or data.get("status") or "").lower()
            if url:
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    still.append(j)
            elif state in ("fail", "failed", "error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(jobs)} ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
