#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for 2026-06-09.
Ayman Hussein -> Iraq World Cup beat-2 (the goalscorer);
Abbas Araghchi -> Iran nuclear hero (the FM driving the talks)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

FACES = [
    ("Ayman_Hussein", "2026-06-09-iraq-worldcup-2026/broll_2.jpg"),
    ("Abbas_Araghchi", "2026-06-09-iran-nuclear-deadlock/hero.jpg"),
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
