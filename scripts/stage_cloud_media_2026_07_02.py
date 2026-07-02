#!/usr/bin/env python3
"""Stage the 2026-07-02 slate media into cloud-media/<date>/<slug>/ (what the render
workflow consumes) and write .meta/media-stamp.json per slug."""
from __future__ import annotations
import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-02"
IMG = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"

SLUGS = [
    "iraq-us-chevron-pivot",
    "worldcup-r32-drama",
    "centcom-bahrain-summit",
    "michael-biopic-record",
    "tianwen2-quasimoon",
    "skorea-chip-megaplan",
]
SLOTS = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]

STAMP = {
    "manual": True,
    "source": "kie-nano-banana-pro + wikimedia-faces",
    "date": DATE,
    "note": "hand-verified faces (al-Zaidi/Brad Cooper/Michael Jackson/Lee Jae-myung) + 20 bespoke cinematic scenes; every image Read-verified; worldcup/broll_1 + michael/broll_1 regenerated after QA",
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
