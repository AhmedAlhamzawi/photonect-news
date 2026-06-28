#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-28 slate's centrally-named people:
  - Rafael Fiziev (UFC Baku headliner KO) -> ufc-baku-fiziev broll_1
  - Abdel Fattah al-Burhan (Sudan army chief) -> sudan-burhan-deadlock broll_1
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Rafael_Fiziev", "Rafael_Fiziev_2023", "Rafael_Fiziev_(fighter)"],
     "2026-06-28-ufc-baku-fiziev/broll_1.jpg"),
    (["Abdel_Fattah_al-Burhan", "Abdel_Fattah_Abdelrahman_al-Burhan", "Abdel_Fattah_Burhan"],
     "2026-06-28-sudan-burhan-deadlock/broll_1.jpg"),
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
