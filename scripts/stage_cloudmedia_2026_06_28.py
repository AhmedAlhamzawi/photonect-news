#!/usr/bin/env python3
"""Stage the 2026-06-28 slate media into cloud-media/<date>/<date>-<slug>/ (what CI
reads) and drop media-stamp.json beside each props.json so the CI auto-hunter
never overwrites these hand-vetted images. Verifies all 4 images per slug first.

NOTE: this slate's scenes are licensed Pexels stock + 2 Wikimedia Commons
portraits (Fiziev, Burhan) + 1 Commons Baghdad establishing shot — KIE Nano
Banana Pro was out of credits (HTTP 402) on 2026-06-28, so the engine's
documented fallback tiers (Commons -> Pexels) were used. Every image was
hand-verified with the Read tool before staging."""
import json, shutil, sys
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG = ROOT / "my-video" / "public" / "images" / "news"
DATE = "2026-06-28"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"
SLUGS = [
    "iraq-greenzone-arrests", "ufc-baku-fiziev", "sudan-burhan-deadlock",
    "exoplanets-superpuff", "uae-etihad-rail", "toystory5-record",
]
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]


def main():
    missing = []
    for slug in SLUGS:
        for f in FILES:
            p = IMG / f"{DATE}-{slug}" / f
            if not p.exists() or p.stat().st_size < 20_000:
                missing.append(f"{DATE}-{slug}/{f}")
    if missing:
        print("MISSING / too-small IMAGES:", file=sys.stderr)
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
        stamp.write_text(json.dumps({
            "manual": True,
            "source": "pexels+wikimedia-commons",
            "date": DATE,
            "note": "KIE 402 out-of-credits; Commons/Pexels fallback; all hand-verified",
        }), encoding="utf-8")
        print(f"  ✓ {DATE}-{slug}: 4 images -> cloud-media + stamp")
    print(f"\nstaged {len(SLUGS)} slugs into {CLOUD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
