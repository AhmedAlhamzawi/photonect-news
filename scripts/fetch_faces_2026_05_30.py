#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for 2026-05-30.
Each goes into broll_1.jpg of its slug (the person-focused beat 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

FACES = [
    ("Benjamin_Netanyahu", "2026-05-30-gaza-seizure-70/broll_1.jpg"),
    ("Mohammed_bin_Salman", "2026-05-30-neom-line-halt/broll_1.jpg"),
    ("Ahmed_al-Sharaa", "2026-05-30-syria-energy-deal/broll_1.jpg"),
    ("Jared_Isaacman", "2026-05-30-nasa-moonbase/broll_1.jpg"),
]


def main():
    ok = 0
    for title, rel in FACES:
        url = get_image_url(title)
        if not url:
            print(f"  ✗ {title}: no image url", file=sys.stderr); continue
        try:
            size, kb = download(url, IMG / rel)
            print(f"  ✓ {title} -> {rel}  {size} {kb}KB")
            ok += 1
        except Exception as e:
            print(f"  ✗ {title}: {e}", file=sys.stderr)
    print(f"\n{ok}/{len(FACES)} faces fetched")
    return 0 if ok == len(FACES) else 1


if __name__ == "__main__":
    sys.exit(main())
