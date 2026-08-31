#!/usr/bin/env python3
"""Stage the 2026-08-31 slate frames into cloud-media/ and write media-stamp.json.

Slug list is derived from data/posts/2026-08-28-* so it can never drift from the
authored slate (a hardcoded list is how a stale date-copy of this script invents
folders that do not exist).
"""
from __future__ import annotations
import hashlib, json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = "2026-08-31"
POSTS = ROOT / "data" / "posts"
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / D


def used_frames(slug: str) -> list[str]:
    """Every frame the reel actually references, hero first, de-duplicated."""
    meta = POSTS / slug / ".meta"
    names: list[str] = []
    props = json.loads((meta / "props.json").read_text(encoding="utf-8"))
    paths = [props["breaking"]["heroMedia"]] + [b["broll"] for b in props["beats"]]
    brief = meta / "v11-brief.json"
    if brief.exists():
        paths += json.loads(brief.read_text(encoding="utf-8"))["images"]
    for p in paths:
        n = p.rsplit("/", 1)[-1]
        if n not in names:
            names.append(n)
    return names


def main() -> int:
    slugs = sorted(p.name for p in POSTS.glob(f"{D}-*") if p.is_dir())
    missing: list[str] = []
    for slug in slugs:
        dest = CLOUD / slug
        dest.mkdir(parents=True, exist_ok=True)
        stamp = []
        for name in used_frames(slug):
            src = IMG_ROOT / slug / name
            if not src.exists():
                missing.append(f"{slug}/{name}")
                continue
            shutil.copy2(src, dest / name)
            raw = src.read_bytes()
            stamp.append({
                "file": name,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest()[:16],
            })
        stamp.sort(key=lambda e: e["file"])
        (POSTS / slug / ".meta" / "media-stamp.json").write_text(
            json.dumps({"slug": slug, "date": D, "images": stamp},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  ok  {slug}  {len(stamp)} frames staged + media-stamp.json")
    if missing:
        print("\nMISSING:")
        for m in missing:
            print("  " + m)
        return 1
    print(f"\n{len(slugs)} slugs staged, 0 missing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
