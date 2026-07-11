#!/usr/bin/env python3
"""Regen graft-second-wave/broll_2 — first pass rendered the UK House of Commons
(green benches / Westminster Gothic), wrong for an Iraq story. Replace with a
neutral Iraqi official press-podium scene (evokes the PM's public vow), no
Westminster, no readable text."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

SLUG = "2026-07-11-graft-second-wave"
FNAME = "broll_2.jpg"
PROMPT = (f"An empty formal government press-conference podium with a cluster of microphones "
          f"in a stately official hall, a plain Iraqi flag on a pole beside it, soft directional "
          f"light, a sense of an official anti-corruption announcement, editorial documentary, "
          f"no readable text, {NEG}")


def main():
    out = IMG_ROOT / SLUG / FNAME
    tid = submit(PROMPT)
    print(f"submitted {SLUG}/{FNAME} tid={tid}", flush=True)
    deadline = time.time() + 8 * 60
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        try:
            r = http_get(f"{STATUS_URL}?taskId={tid}")
        except Exception:
            continue
        data = r.get("data") or {}
        st = data.get("state")
        if st == "success":
            url = first_image_url(data)
            if url:
                print("downloaded:", download(url, out), flush=True)
                return 0
            print("no image url", file=sys.stderr); return 1
        if st == "fail":
            print("FAIL", str(data)[:160], file=sys.stderr); return 1
        print("  ... generating", flush=True)
    print("timeout", file=sys.stderr); return 1


if __name__ == "__main__":
    raise SystemExit(main())
