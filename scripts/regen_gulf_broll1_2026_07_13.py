#!/usr/bin/env python3
"""Regenerate gulf-energy-fund-iraq/broll_1.jpg — the first pass came back 90°-rotated
with random wrong flags (Brazil/UK/Australia). Reprompt: upright portrait, single flag,
clean signing scene. (See feedback_daily_render_gotchas: KIE 90°-rotation + upright reprompt.)"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

HARD = "absolutely no readable text, no numbers, no letters, no user interface, no app screen, no news graphics, no maps with labels, no watermark, no logos"

PROMPT = ("An upright vertical portrait photograph, camera held perfectly level, of a formal "
          "high-level investment signing meeting: two business delegations in dark suits seated "
          "and shaking hands across a long polished table in a bright modern conference room, one "
          "plain flag on a stand blurred in the background, sovereign-fund and energy investment "
          "diplomacy, faces turned away or indistinct, cinematic editorial photojournalism, "
          f"clearly upright vertical 9:16 composition, {HARD}, {NEG}")

JOBS = [("2026-07-13-gulf-energy-fund-iraq", "broll_1.jpg", PROMPT)]


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
            except Exception:
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if url:
                    print(f"  OK {j['slug']}/{j['file']}  {download(url, j['out'])}", flush=True)
                    j["ok"] = True
            elif st == "fail":
                print(f"  X fail — resubmitting", file=sys.stderr, flush=True)
                j["tid"] = submit(PROMPT); still.append(j)
            else:
                still.append(j)
        pending = still
    return 0 if all(j["ok"] for j in jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
