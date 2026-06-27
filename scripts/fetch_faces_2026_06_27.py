#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-27 slate's centrally-named people:
  - Ahmed al-Sharaa (Syrian interim president) -> syria-minority-cabinet broll_1
  - Serena Williams (Wimbledon wild-card return) -> wimbledon-serena-return broll_1
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Ahmed_al-Sharaa", "Ahmad_al-Sharaa", "Ahmed_al-Shara", "Ahmed_Hussein_al-Sharaa", "Abu_Mohammad_al-Julani"],
     "2026-06-27-syria-minority-cabinet/broll_1.jpg"),
    (["Serena_Williams", "Serena_Williams_2013", "Serena_Williams_at_2013_US_Open", "Serena_Williams_2022"],
     "2026-06-27-wimbledon-serena-return/broll_1.jpg"),
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
            print(f"  ✗ {rel}: no Commons portrait for any of {titles} — keeping generated scene", file=sys.stderr)
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
