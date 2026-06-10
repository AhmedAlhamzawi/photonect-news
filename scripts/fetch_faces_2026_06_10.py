#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for 2026-06-10.
Randy Bresnik -> Artemis III commander (beat-1, the face of the crew);
Luca Parmitano -> Artemis III ESA pilot (beat-3, the international partnership)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

FACES = [
    ("Randy_Bresnik", "2026-06-10-artemis-3-moon-crew/broll_1.jpg"),
    ("Luca_Parmitano", "2026-06-10-artemis-3-moon-crew/broll_3.jpg"),
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
