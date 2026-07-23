#!/usr/bin/env python3
"""Regenerate 2 flagged scenes for 2026-07-23:
  - salaries-run-late/broll_2  (previous output came back rotated 90°)
  - graft-saladin-airways/broll_1 (previous output had prominent garbled Arabic)
Explicit upright-portrait wording to fight KIE rotation; plain/no-text wording
to avoid garbled Arabic. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-23"
UPRIGHT = "vertical 9:16 upright portrait photograph, camera held perfectly upright, level horizon, correct vertical orientation"
NOTEXT = "plain surfaces, no readable text, no lettering, no labels, no signage"

JOBS = [
    (f"{D}-salaries-run-late", "broll_2.jpg", f"{UPRIGHT}. Interior of an Iraqi finance ministry electronic-payments operations room, employees seated at computer terminals handling bank transfers, cool blue overhead lighting, calm documentary tone, no readable screens, {NOTEXT}, {NEG}"),
    (f"{D}-graft-saladin-airways", "broll_1.jpg", f"{UPRIGHT}. A neat stack of closed confidential government case-file folders tied with string on a dark wooden investigator's desk beside a small Iraqi flag, dramatic side light, shallow depth of field, plain unmarked folders, {NOTEXT}, {NEG}"),
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
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 12 * 60
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
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True); still.append(j)
            elif state in ("fail", "failed", "error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"    … {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(jobs)} ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
