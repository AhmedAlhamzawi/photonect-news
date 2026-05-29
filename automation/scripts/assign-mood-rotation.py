#!/usr/bin/env python3
"""
Assign one of the 4 V7 mood beds to each post of a given date in rotation.

Rotation is deterministic by alphabetical slug order within the date, so the
same date always gets the same mood assignment — idempotent, safe to rerun.

Moods cycle in this order:
  0. cinematic    (slow piano + sub-bass + sparse strings)
  1. newsroom     (synth arps + light percussion)
  2. orchestral   (low strings + soft brass + piano)
  3. mideast      (oud + qanun + drum + cinematic pad)

Usage:
  python3 automation/scripts/assign-mood-rotation.py 2026-04-24
  python3 automation/scripts/assign-mood-rotation.py 2026-04-24 2026-04-25
"""
import json
import sys
from pathlib import Path

# V10 (2026-05-29) — expanded 11-track rotation: 4 original V7 moods + 7 new
# Suno-generated beds (loudnorm'd to -16 LUFS), interleaved so each slate mixes
# new and proven tracks. Ahmed: "new music, generate 10 more, loop with current."
MOODS = [
    "audio/music_01.mp3",        # cinematic dawn (new)
    "audio/mood_cinematic.mp3",
    "audio/music_03.mp3",        # orchestral weight (new)
    "audio/mood_newsroom.mp3",
    "audio/music_05.mp3",        # markets voltage (new)
    "audio/mood_orchestral.mp3",
    "audio/music_04.mp3",        # mideast cinematic (new)
    "audio/mood_mideast.mp3",
    "audio/music_06.mp3",        # ambient tide (new)
    "audio/music_08.mp3",        # hopeful strings (new)
    "audio/music_10.mp3",        # tech glass (new)
]

ROOT = Path(__file__).resolve().parents[2]
POSTS = ROOT / "data" / "posts"


def assign_for_date(date_str: str) -> int:
    slugs = sorted(p for p in POSTS.glob(f"{date_str}-*") if p.is_dir())
    if not slugs:
        print(f"  {date_str}: no slugs found — skipping")
        return 0
    for i, slug_dir in enumerate(slugs):
        props = slug_dir / ".meta" / "props.json"
        if not props.exists():
            print(f"  {slug_dir.name}: no props.json — skipping")
            continue
        with props.open() as f:
            data = json.load(f)
        mood = MOODS[i % len(MOODS)]
        before = data.get("audioBed", "<unset>")
        data["audioBed"] = mood
        with props.open("w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"  [{i % len(MOODS)}] {slug_dir.name}: {before} → {mood}")
    return len(slugs)


def main():
    if len(sys.argv) < 2:
        print("error: pass at least one date (YYYY-MM-DD)", file=sys.stderr)
        sys.exit(2)
    total = 0
    for date_str in sys.argv[1:]:
        print(f"━━━ {date_str} ━━━")
        total += assign_for_date(date_str)
    print(f"\n{total} slug(s) updated across {len(sys.argv) - 1} date(s)")


if __name__ == "__main__":
    main()
