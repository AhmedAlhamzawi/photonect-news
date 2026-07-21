#!/usr/bin/env python3
"""Finalize 2026-07-21 slate after mood rotation:
  1. sync each V11 brief's audioBed to its props.audioBed (music bed match)
  2. copy the 4 images per slug into cloud-media/<date>/<slug>/
  3. write .meta/media-stamp.json per slug
Run AFTER assign-mood-rotation.py.
"""
from __future__ import annotations
import json, shutil
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
D = "2026-07-21"
POSTS = ROOT / "data" / "posts"
IMG = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / D
STAMP_TIME = "2026-07-21T11:15:00+00:00"

slugs = sorted(p for p in POSTS.glob(f"{D}-*") if p.is_dir())
for d in slugs:
    slug = d.name
    props = json.loads((d / ".meta" / "props.json").read_text())
    bucket = props.get("topicBucket", "iraq_domestic")
    bed = props.get("audioBed", "audio/music_01.mp3")

    # 1. sync brief audioBed
    brief_p = d / ".meta" / "v11-brief.json"
    if brief_p.exists():
        b = json.loads(brief_p.read_text())
        b["audioBed"] = bed
        brief_p.write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n")

    # 2. copy images to cloud-media
    src = IMG / slug
    dst = CLOUD / slug
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for name in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"):
        s = src / name
        if s.exists():
            shutil.copy2(s, dst / name)
            n += 1

    # 3. media-stamp
    (d / ".meta" / "media-stamp.json").write_text(
        json.dumps({"hunted_at": STAMP_TIME, "bucket": bucket}, ensure_ascii=False, indent=2)
    )
    print(f"  ✓ {slug}: bed={bed}, {n} imgs -> cloud-media")

print("finalize done")
