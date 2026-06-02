#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for 2026-06-02.
Hakimi -> hero (he IS the story); Hadi & Sisi -> person beat broll_1."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

FACES = [
    ("Achraf_Hakimi", "2026-06-02-hakimi-ucl-record/hero.jpg"),
    ("Abdrabbuh_Mansur_Hadi", "2026-06-02-hadi-yemen-legacy/broll_1.jpg"),
    ("Abdel_Fattah_el-Sisi", "2026-06-02-egypt-imf-saudi/broll_1.jpg"),
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
