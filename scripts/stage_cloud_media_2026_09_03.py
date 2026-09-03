#!/usr/bin/env python3
"""Stage the 2026-09-03 slate media into cloud-media/ and write media-stamp.json.

Slugs are derived from the FILESYSTEM, never sed-copied from a previous dated
script — a previous run invented empty folders that way.
"""
from __future__ import annotations
import hashlib, json, shutil
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
D = "2026-09-03"
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
POSTS = ROOT / "data" / "posts"
CLOUD = ROOT / "cloud-media" / D

SLOTS = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]


def main() -> int:
    slugs = sorted(p.name for p in POSTS.glob(f"{D}-*") if p.is_dir())
    if not slugs:
        print("no slugs found")
        return 1
    rc = 0
    for slug in slugs:
        src = IMG_ROOT / slug
        dst = CLOUD / slug
        dst.mkdir(parents=True, exist_ok=True)
        entries = []
        for slot in SLOTS:
            f = src / slot
            if not f.exists():
                print(f"  MISSING {slug}/{slot}")
                rc = 1
                continue
            shutil.copy2(f, dst / slot)
            data = f.read_bytes()
            entries.append({
                "file": slot,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest()[:16],
            })
        meta = POSTS / slug / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "media-stamp.json").write_text(
            json.dumps({"slug": slug, "date": D,
                        "images": sorted(entries, key=lambda e: e["file"])},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  staged {slug}  ({len(entries)}/4)")
    print(f"\n{len(slugs)} slugs staged into cloud-media/{D}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
