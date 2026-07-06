#!/usr/bin/env python3
"""Stage the 2026-07-06 slate media into cloud-media/<date>/<slug>/ (what the render
workflow consumes) and write .meta/media-stamp.json per slug."""
from __future__ import annotations
import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-06"
IMG = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"

SLUGS = [
    "baghdad-graft-2trillion",
    "crude-price-slide",
    "iraq-cyber-law",
    "karbala-arbaeen-economy",
    "kurdistan-salary-oil",
]
SLOTS = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]

STAMP = {
    "manual": True,
    "source": "kie-nano-banana-pro",
    "date": DATE,
    "note": "20 bespoke cinematic KIE nano-banana-pro 9:16 2K scenes (all scene-based, no named-person portraits); every image Read-verified before accept; 3 regenerated on QA — graft/broll_3 (dropped a wrong US flag), crude/hero (90°-rotation fix), kurdistan/broll_1 (wrong-region crowd → authentic Iraqi summer queue)",
}


def main():
    total = 0
    for slug in SLUGS:
        full = f"{DATE}-{slug}"
        src = IMG / full
        dst = CLOUD / full
        dst.mkdir(parents=True, exist_ok=True)
        for slot in SLOTS:
            s = src / slot
            if not s.is_file() or s.stat().st_size < 50_000:
                raise SystemExit(f"MISSING/too-small: {s}")
            shutil.copy2(s, dst / slot)
            total += 1
        meta = POSTS / full / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "media-stamp.json").write_text(json.dumps(STAMP, ensure_ascii=False), encoding="utf-8")
        print(f"  ✓ {full}: 4 images → cloud-media + stamp")
    print(f"\nstaged {total} images across {len(SLUGS)} slugs")


if __name__ == "__main__":
    main()
