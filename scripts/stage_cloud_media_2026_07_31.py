#!/usr/bin/env python3
"""Stage the 2026-07-31 slate media into cloud-media/ (the CI source of truth).

Copies the 4 Read-verified Higgsfield images per slug from
my-video/public/images/news/<slug>/ -> cloud-media/2026-07-31/<slug>/.
media-stamp.json is written by scripts/author_2026_07_31.py, not here.
"""
from __future__ import annotations
import shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-31"
SLUGS = ["banks-open-for-salaries", "dollar-friday-shops",
         "foreign-strikes-sovereignty", "power-2tn-unused", "starlink-live-iraq"]
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
SRC = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / DATE


def main() -> int:
    missing = []
    for s in SLUGS:
        full = f"{DATE}-{s}"
        dst = CLOUD / full
        dst.mkdir(parents=True, exist_ok=True)
        for f in FILES:
            sp = SRC / full / f
            if not sp.is_file():
                missing.append(f"{full}/{f}"); continue
            shutil.copy2(sp, dst / f)
        print(f"  ✓ {full}  ({len(FILES)} images)")
    if missing:
        print(f"\n❌ MISSING: {missing}", file=sys.stderr)
        return 1
    print(f"\n== {len(SLUGS)} slugs staged into cloud-media/{DATE} ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
