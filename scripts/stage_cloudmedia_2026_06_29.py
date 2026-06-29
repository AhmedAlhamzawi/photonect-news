#!/usr/bin/env python3
"""Stage the 2026-06-29 slate media into cloud-media/<date>/<date>-<slug>/ (what CI
reads) and drop media-stamp.json beside each props.json so the CI auto-hunter
never overwrites these hand-vetted images. Verifies all 4 images per slug first.

This slate's media: KIE Nano Banana Pro bespoke scenes (KIE funded again, ~9.3k
credits) + 2 Wikimedia Commons portraits (George Russell -> f1 broll_1,
Alphonso Davies -> worldcup broll_2). Every image hand-verified with the Read
tool before staging."""
import json, shutil, sys
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG = ROOT / "my-video" / "public" / "images" / "news"
DATE = "2026-06-29"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"
SLUGS = [
    "iraq-drought-tombs", "f1-austria-russell", "hormuz-record-flow",
    "asteroid-flyby-1997nc1", "aramco-rastanura-crash", "worldcup-canada-r16",
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
            "source": "kie-nano-banana-pro + wikimedia-commons",
            "date": DATE,
            "note": "KIE bespoke scenes (funded) + 2 Commons portraits (Russell, Davies); all hand-verified with Read",
        }), encoding="utf-8")
        print(f"  ✓ {DATE}-{slug}: 4 images -> cloud-media + stamp")
    print(f"\nstaged {len(SLUGS)} slugs into {CLOUD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
