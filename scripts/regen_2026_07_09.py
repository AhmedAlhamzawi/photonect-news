#!/usr/bin/env python3
"""Regenerate 2 rejected scenes for 2026-07-09:
  - american-hospital/broll_2 : first pass had garbled 'United States of Passport' text
  - american-hospital/broll_3 : first pass rendered rotated 90 degrees (sideways)
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-09"
JOBS = [
    (f"{D}-american-hospital", "broll_2.jpg", f"A clean editorial still life on a dark slate surface, upright vertical composition — a stethoscope, a fan of US hundred-dollar bills beside a neat bundle of Iraqi dinar banknotes, and a chest X-ray film, symbolizing the high cost of seeking medical treatment abroad, dramatic warm side light, absolutely no passport and no documents with lettering, {NEG}"),
    (f"{D}-american-hospital", "broll_3.jpg", f"Upright vertical portrait photo of doctors and nurses in scrubs and white coats walking toward the camera down a bright modern hospital corridor with tall windows and advanced medical equipment, a newly built advanced facility, hopeful professional atmosphere, correct upright orientation, {NEG}"),
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
    deadline = time.time() + 12 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Regen done {ok}/{len(JOBS)} ==", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
