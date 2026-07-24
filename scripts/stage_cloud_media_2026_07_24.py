#!/usr/bin/env python3
"""Stage the 2026-07-24 slate media into cloud-media/ (CI source of truth) and write
each slug's .meta/media-stamp.json. Copies the 4 verified KIE images per slug from
my-video/public/images/news/<slug>/ → cloud-media/2026-07-24/<slug>/.
"""
from __future__ import annotations
import json, shutil
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
DATE = "2026-07-24"
SLUGS = [
    "graft-return-or-jail", "iran-gas-oil-barter", "money-printing-25tn",
    "gulf-swf-trillions", "water-heat-crisis",
]
IMG_SRC = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
STAMP = {
    "manual": True, "source": "kie-nano-banana-pro", "date": DATE,
    "note": "5 slugs x 4 bespoke KIE nano-banana-pro 9:16 2K scenes (all scene-based, no named-person portraits); one still per beat matched to that beat text; every image Read-verified before accept; 2 regenerated (money-printing broll_2 wrong-signage, water broll_3 rotation).",
}


def main():
    missing = []
    for slug in SLUGS:
        full = f"{DATE}-{slug}"
        src = IMG_SRC / full
        dst = CLOUD / full
        dst.mkdir(parents=True, exist_ok=True)
        for f in FILES:
            sp = src / f
            if not sp.is_file():
                missing.append(f"{full}/{f}"); continue
            shutil.copy2(sp, dst / f)
        meta = POSTS / full / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "media-stamp.json").write_text(json.dumps(STAMP, ensure_ascii=False), encoding="utf-8")
        print(f"  ✓ staged {full} ({len(FILES)} imgs)")
    if missing:
        print("  ! MISSING:", *missing, sep="\n    ")
        raise SystemExit(1)
    print(f"\nStaged {len(SLUGS)} slugs into {CLOUD}")


if __name__ == "__main__":
    main()
