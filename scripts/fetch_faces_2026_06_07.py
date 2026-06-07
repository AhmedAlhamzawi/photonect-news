#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for the 2026-06-07 slate.
Andreeva -> french-open hero (she IS the champion); Chwalinska -> french-open broll_2
(the runner-up); al-Zaidi -> iraq anti-corruption hero (the PM driving the purge)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

FACES = [
    ("Mirra_Andreeva", "2026-06-07-french-open-andreeva/hero.jpg"),
    ("Maja_Chwalińska", "2026-06-07-french-open-andreeva/broll_2.jpg"),
    ("Ali_al-Zaidi", "2026-06-07-iraq-zaidi-anticorruption/hero.jpg"),
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
