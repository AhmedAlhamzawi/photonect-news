#!/usr/bin/env python3
"""One-shot migration: flatten every post folder to `video.mp4` + `caption.txt`.

Before:
    data/posts/2026-04-22-lebanon-bekaa/
        caption.txt
        media-stamp.json
        newsreel_v3.mp4
        props.json
        thumbnail.jpg

After:
    data/posts/2026-04-22-lebanon-bekaa/
        video.mp4          # renamed from newsreel_v3.mp4
        caption.txt
        .meta/
            props.json
            media-stamp.json
            thumbnail.jpg
            old-renders/
                newsreel.mp4       (if existed)
                newsreel_v2.mp4    (if existed)

Idempotent — rerunning after completion is a no-op.

Usage:
    python3 automation/scripts/flatten-posts.py            # dry run, print plan
    python3 automation/scripts/flatten-posts.py --apply    # actually do it
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"

# Files that go into .meta/ (metadata + preview artifacts)
META_FILES = {
    "props.json",
    "media-stamp.json",
    "thumbnail.jpg",
    "story.json",
}

# Directories that also go into .meta/ (legacy QA/asset dirs from Apr 17 workshop)
META_DIRS = {
    "assets",
    "qa",
    "qa_v2",
}

# Old render files go into .meta/old-renders/
OLD_RENDERS = {
    "newsreel.mp4",
    "newsreel_v2.mp4",
}


def plan_folder(post_dir: Path) -> list[tuple[str, Path, Path]]:
    """Return a list of (action, src, dst) tuples describing the migration.

    action is one of: 'rename', 'move-to-meta', 'move-to-old-renders'.
    """
    actions: list[tuple[str, Path, Path]] = []

    # 1. Rename newsreel_v3.mp4 → video.mp4 (the main event)
    v3 = post_dir / "newsreel_v3.mp4"
    video = post_dir / "video.mp4"
    if v3.exists() and not video.exists():
        actions.append(("rename", v3, video))

    # 2. Move metadata files into .meta/
    meta = post_dir / ".meta"
    for name in META_FILES:
        src = post_dir / name
        if src.exists() and src.is_file():
            actions.append(("move-to-meta", src, meta / name))

    # 3. Move metadata dirs into .meta/
    for name in META_DIRS:
        src = post_dir / name
        if src.exists() and src.is_dir():
            actions.append(("move-to-meta", src, meta / name))

    # 4. Move old renders into .meta/old-renders/
    old_renders = meta / "old-renders"
    for name in OLD_RENDERS:
        src = post_dir / name
        if src.exists() and src.is_file():
            actions.append(("move-to-old-renders", src, old_renders / name))

    return actions


def apply_actions(actions: list[tuple[str, Path, Path]]) -> None:
    for action, src, dst in actions:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))


def main() -> int:
    dry_run = "--apply" not in sys.argv

    post_dirs = sorted(d for d in POSTS.glob("2026-*-*") if d.is_dir())
    if not post_dirs:
        print("No post folders found under data/posts/")
        return 1

    total_actions = 0
    post_action_count = 0
    header = "DRY RUN — pass --apply to execute" if dry_run else "APPLYING"
    print(f"=== flatten-posts.py — {header} ===")
    print(f"Scanning {len(post_dirs)} post folders under {POSTS.relative_to(ROOT)}/")
    print()

    for post in post_dirs:
        actions = plan_folder(post)
        if not actions:
            continue
        post_action_count += 1
        total_actions += len(actions)
        print(f"  {post.name}  ({len(actions)} actions)")
        for act, src, dst in actions:
            print(f"     {act:20s}  {src.name}  →  {dst.relative_to(post)}")
        if not dry_run:
            apply_actions(actions)

    print()
    print(f"Touched {post_action_count}/{len(post_dirs)} folders, {total_actions} total actions")
    if dry_run:
        print("Dry run only. Rerun with --apply to perform the migration.")
    else:
        print("✓ migration complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
