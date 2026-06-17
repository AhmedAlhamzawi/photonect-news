#!/usr/bin/env python3
"""Fetch a real Commons portrait for the 2026-06-17 slate's one centrally-named person:
  - Lionel Messi -> worldcup-messi-hattrick broll_1 (the story is his record WC hat-trick)
Tries several title variants; if none resolve, the generated celebration fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Lionel_Messi", "Lionel_Messi_2018", "Lionel_Messi_20180626", "Leo_Messi"],
     "2026-06-17-worldcup-messi-hattrick/broll_1.jpg"),
]


def main():
    ok = 0
    for titles, rel in CANDIDATES:
        url = None; used = None
        for t in titles:
            url = get_image_url(t)
            if url:
                used = t; break
        if not url:
            print(f"  ✗ {rel}: no Commons portrait for any of {titles}", file=sys.stderr)
            continue
        try:
            size, kb = download(url, IMG / rel)
            print(f"  ✓ {used} -> {rel}  {size} {kb}KB")
            ok += 1
        except Exception as e:
            print(f"  ✗ {used}: {e}", file=sys.stderr)
    print(f"\n{ok}/{len(CANDIDATES)} faces fetched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
