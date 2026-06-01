#!/usr/bin/env python3
"""Stage the 2026-06-01 slate media into cloud-media/<date>/<slug>/ (what CI reads)
and drop a media-stamp.json beside each props.json so the auto-hunter never
overwrites these hand-picked images. Verifies all 4 images per slug exist first.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG = ROOT / "my-video" / "public" / "images" / "news"
DATE = "2026-06-01"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"
SLUGS = [
    "iraq-oil-gas-law", "redsea-reopens", "ai-price-war",
    "qatar-lng-expansion", "ecb-rate-hike", "white-hydrogen",
]
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]


def main():
    missing = []
    for slug in SLUGS:
        for f in FILES:
            if not (IMG / f"{DATE}-{slug}" / f).exists():
                missing.append(f"{DATE}-{slug}/{f}")
    if missing:
        print("MISSING IMAGES:", file=sys.stderr)
        for m in missing:
            print("  -", m, file=sys.stderr)
        return 1

    for slug in SLUGS:
        src = IMG / f"{DATE}-{slug}"
        dst = CLOUD / f"{DATE}-{slug}"
        dst.mkdir(parents=True, exist_ok=True)
        for f in FILES:
            shutil.copy2(src / f, dst / f)
        stamp = POSTS / f"{DATE}-{slug}" / ".meta" / "media-stamp.json"
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text(json.dumps({"manual": True, "source": "nano-banana-pro+real"}), encoding="utf-8")
        print(f"  ✓ {DATE}-{slug}: 4 images -> cloud-media + stamp")
    print(f"\nstaged {len(SLUGS)} slugs into {CLOUD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
