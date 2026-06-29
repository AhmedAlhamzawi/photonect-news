#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-29 slate's centrally-named people:
  - George Russell (F1 Austrian GP winner) -> f1-austria-russell broll_1
  - Alphonso Davies (Canada World Cup debut)  -> worldcup-canada-r16 broll_2
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["George_Russell_2023", "George_Russell_(racing_driver)", "George_Russell"],
     "2026-06-29-f1-austria-russell/broll_1.jpg"),
    (["Alphonso_Davies", "Alphonso_Davies_2019", "Alphonso_Davies_2018"],
     "2026-06-29-worldcup-canada-r16/broll_2.jpg"),
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
