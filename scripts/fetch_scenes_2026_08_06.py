#!/usr/bin/env python3
"""Download the 2026-08-06 slate frames from Higgsfield result URLs into
my-video/public/images/news/<full-slug>/, converting PNG -> JPEG.

Reads a JSON map {"<index>": "<result_url>"} from scripts/_scene_urls_2026_08_06.json
(written by the orchestrating session as each batch completes) and places each
index at its beat-matched destination.
"""
from __future__ import annotations
import json
import sys
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
URLS = Path(__file__).resolve().parent / "_scene_urls_2026_08_06.json"
D = "2026-08-06"

# index -> (slug, filename) — each frame matched to the beat it illustrates
DEST = {
    0:  ("basra-1300-megawatt", "hero.jpg"),
    1:  ("basra-1300-megawatt", "broll_1.jpg"),
    2:  ("basra-1300-megawatt", "broll_2.jpg"),
    3:  ("basra-1300-megawatt", "broll_3.jpg"),
    4:  ("dollar-gold-jump", "hero.jpg"),
    5:  ("dollar-gold-jump", "broll_1.jpg"),
    6:  ("dollar-gold-jump", "broll_2.jpg"),
    7:  ("dollar-gold-jump", "broll_3.jpg"),
    8:  ("no-salary-37-days", "hero.jpg"),
    9:  ("no-salary-37-days", "broll_1.jpg"),
    10: ("no-salary-37-days", "broll_2.jpg"),
    11: ("no-salary-37-days", "broll_3.jpg"),
    12: ("petrol-mosul-queues", "hero.jpg"),
    13: ("petrol-mosul-queues", "broll_1.jpg"),
    14: ("petrol-mosul-queues", "broll_2.jpg"),
    15: ("petrol-mosul-queues", "broll_3.jpg"),
    16: ("sour-basrah-crude", "hero.jpg"),
    17: ("sour-basrah-crude", "broll_1.jpg"),
    18: ("sour-basrah-crude", "broll_2.jpg"),
    19: ("sour-basrah-crude", "broll_3.jpg"),
}


def main() -> int:
    urls = {int(k): v for k, v in json.loads(URLS.read_text()).items()}
    rc = 0
    for idx in sorted(urls):
        slug, fname = DEST[idx]
        out = IMG_ROOT / f"{D}-{slug}" / fname
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            raw = urllib.request.urlopen(urls[idx], timeout=120).read()
            im = Image.open(BytesIO(raw)).convert("RGB")
            im.save(out, "JPEG", quality=92, optimize=True)
            print(f"  ✓ [{idx:2d}] {D}-{slug}/{fname}  {im.width}x{im.height}  "
                  f"{out.stat().st_size // 1024}KB", flush=True)
        except Exception as e:
            print(f"  ! [{idx:2d}] {slug}/{fname}: {e}", file=sys.stderr, flush=True)
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
