#!/usr/bin/env python3
"""Generate the 4 scenes for the 2026-07-20 hormuz-reopening slug (replaces baniyas)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-20"
NEG = (
    "ultra-realistic editorial photojournalism, cinematic lighting, "
    "upright vertical 9:16 portrait orientation, correctly oriented, not rotated, not sideways, "
    "no on-screen text, no captions, no subtitles, no watermark, no logos, no signage text, "
    "no user interface, no app interface, no phone screenshot, no social media UI, "
    "no news ticker, no chyron, no lower third, no browser window, no arabic text, no garbled text"
)

JOBS = [
    (f"{D}-hormuz-reopening", "hero.jpg", f"A large crude oil tanker sailing through a narrow blue sea strait at dawn, rugged coastlines on both sides, hopeful golden light breaking through, epic aerial cinematic wide shot, {NEG}"),
    (f"{D}-hormuz-reopening", "broll_1.jpg", f"A convoy of oil tankers moving in a line through open sea at sunrise, calm water, distant coastal mountains, wide aerial documentary, {NEG}"),
    (f"{D}-hormuz-reopening", "broll_2.jpg", f"A busy oil export terminal at a Gulf port at dusk with loading arms connected to a docked tanker and rows of storage tanks, industrial cinematic wide shot, {NEG}"),
    (f"{D}-hormuz-reopening", "broll_3.jpg", f"A ship's officer standing on a tanker bridge looking out over the sea at dawn, hands on the railing, seen from behind, quiet anticipation, cinematic, {NEG}"),
]


def main():
    jobs = []
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        try:
            tid = submit(prompt); jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.5)
    pending = [j for j in jobs if j.get("tid")]
    deadline = time.time() + 15 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL); still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = r.get("data") or {}; st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    print(f"  ✗ {j['slug']}/{j['file']} no url", file=sys.stderr, flush=True); continue
                try:
                    info = download(url, j["out"]); j["ok"] = True; print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:160]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(JOBS)} ==", flush=True)
    for j in jobs:
        if not j.get("ok"): print(f"  MISSING {j['slug']}/{j['file']}", flush=True)


if __name__ == "__main__":
    main()
