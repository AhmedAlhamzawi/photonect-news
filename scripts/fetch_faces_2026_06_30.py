#!/usr/bin/env python3
"""Fetch real Commons/Wikipedia portraits for the named people in the 2026-06-30 slate.
→ my-video/public/images/news/<slug>/<slot>.jpg  (only the face slots; scenes handled separately)."""
from __future__ import annotations
import json, sys, urllib.parse, urllib.request, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video" / "public" / "images" / "news"
UA = "Mozilla/5.0 (PhotonectNews/1.0; ahmed@photonect.net)"

# (wikipedia title, slug, slot)
FACES = [
    ("Robert Lewandowski", "2026-06-30-lewandowski-mls-chicago", "hero.jpg"),
    ("Umm Kulthum",        "2026-06-30-umm-kulthum-biopic-us",   "hero.jpg"),
    ("Mona Zaki",          "2026-06-30-umm-kulthum-biopic-us",   "broll_2.jpg"),
    ("Steve Witkoff",      "2026-06-30-iran-doha-frozen-assets", "broll_1.jpg"),
]


def pageimage(title: str) -> str | None:
    q = urllib.parse.urlencode({
        "action": "query", "titles": title, "prop": "pageimages",
        "piprop": "thumbnail", "pithumbsize": "1200", "format": "json", "redirects": "1",
    })
    url = f"https://en.wikipedia.org/w/api.php?{q}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
    pages = data.get("query", {}).get("pages", {})
    for _, p in pages.items():
        th = p.get("thumbnail", {}).get("source")
        if th:
            return th
    return None


def main():
    ok, miss = [], []
    for title, slug, slot in FACES:
        dest = IMG / slug / slot
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            src = pageimage(title)
            if not src:
                print(f"  ✗ {title}: no Commons portrait"); miss.append((title, slug, slot)); continue
            subprocess.run(["curl", "-sL", "--retry", "3", "--max-time", "60", "-A", UA, src, "-o", str(dest)], check=False)
            sz = dest.stat().st_size if dest.is_file() else 0
            if sz > 25_000:
                print(f"  ✓ {title} → {slug}/{slot} ({sz//1024} KB)  [{src.split('/')[-1][:40]}]")
                ok.append((title, slug, slot))
            else:
                print(f"  ✗ {title}: download too small ({sz}b)"); miss.append((title, slug, slot))
        except Exception as e:
            print(f"  ✗ {title}: {e}"); miss.append((title, slug, slot))
    print(f"\nfaces: {len(ok)} ok, {len(miss)} missing")
    if miss:
        print("MISSING (will fall back to scene):", [f"{s}/{sl}" for _, s, sl in miss])
    # write a manifest of missing slots so the scene-gen can fill them
    (IMG / "_faces_missing_0630.json").write_text(json.dumps([[s, sl] for _, s, sl in miss]))


if __name__ == "__main__":
    main()
