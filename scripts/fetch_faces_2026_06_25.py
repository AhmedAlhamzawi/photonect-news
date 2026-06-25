#!/usr/bin/env python3
"""Fetch a real Commons portrait for the 2026-06-25 slate's centrally-named person:
  - Giannis Antetokounmpo -> giannis-heat-trade broll_1 (beat 1: he is traded to Miami)
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Giannis_Antetokounmpo", "Giannis_Antetokounmpo_2019", "Giannis_Antetokounmpo_(51959533045)", "Giannis_Antetokounmpo_Bucks"],
     "2026-06-25-giannis-heat-trade/broll_1.jpg"),
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
