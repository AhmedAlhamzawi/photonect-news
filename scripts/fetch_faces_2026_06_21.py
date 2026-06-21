#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-21 slate's centrally-named people:
  - Wyndham Clark   -> us-open-golf broll_1 (beat 1: he leads the U.S. Open)
  - Scottie Scheffler -> us-open-golf broll_2 (beat 2: his Grand Slam bid)
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Wyndham_Clark", "Wyndham_Clark_2023", "Wyndham_Clark_(golfer)"],
     "2026-06-21-us-open-golf/broll_1.jpg"),
    (["Scottie_Scheffler", "Scottie_Scheffler_2022", "Scottie_Scheffler_(golfer)", "Scott_Scheffler"],
     "2026-06-21-us-open-golf/broll_2.jpg"),
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
