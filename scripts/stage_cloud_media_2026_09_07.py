#!/usr/bin/env python3
"""Stage 2026-09-07 slate images into cloud-media/ and write .meta/media-stamp.json.

Slugs are derived from the filesystem (never sed-copied from a prior dated script).
"""
import hashlib, json, shutil, sys
from pathlib import Path

DATE = "2026-09-07"
ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "my-video" / "public" / "images" / "news"
DEST = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]

slugs = sorted(p.name for p in POSTS.iterdir() if p.name.startswith(DATE + "-") and p.is_dir())
if not slugs:
    sys.exit(f"no slugs found for {DATE}")

rc = 0
for slug in slugs:
    sdir, ddir = SRC / slug, DEST / slug
    if not sdir.is_dir():
        print(f"MISSING image dir: {slug}"); rc = 1; continue
    ddir.mkdir(parents=True, exist_ok=True)
    entries = []
    for f in FILES:
        s = sdir / f
        if not s.exists():
            print(f"MISSING {slug}/{f}"); rc = 1; continue
        shutil.copy2(s, ddir / f)
        b = s.read_bytes()
        entries.append({"file": f, "bytes": len(b),
                        "sha256": hashlib.sha256(b).hexdigest()[:16]})
    stamp = {"slug": slug, "date": DATE, "images": sorted(entries, key=lambda e: e["file"])}
    (POSTS / slug / ".meta" / "media-stamp.json").write_text(
        json.dumps(stamp, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{slug}: staged {len(entries)}/4")
sys.exit(rc)
