#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for 2026-05-29 (Ahmed:
"when you talk about Elon Musk you MUST show his picture"). Uses Wikipedia REST
summary API -> originalimage (Commons-hosted, free license for living people).
"""
import io, json, sys, urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG = ROOT / "my-video" / "public" / "images" / "news"

# (wikipedia_title, output_path_rel)
FACES = [
    ("Elon_Musk", "2026-05-29-musk-spacex-ipo/hero.jpg"),
    ("Lionel_Messi", "2026-05-29-worldcup-messi-ronaldo/hero.jpg"),
    ("Cristiano_Ronaldo", "2026-05-29-worldcup-messi-ronaldo/broll_1.jpg"),
    ("Achraf_Hakimi", "2026-05-29-worldcup-messi-ronaldo/broll_3.jpg"),
    ("Ahmed_al-Sharaa", "2026-05-29-lebanon-ceasefire-brink/broll_2.jpg"),
]

UA = "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def get_image_url(title):
    # Try REST summary first
    try:
        d = get_json(f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}")
        for k in ("originalimage", "thumbnail"):
            if d.get(k, {}).get("source"):
                return d[k]["source"]
    except Exception as e:
        print(f"  summary err {title}: {e}", file=sys.stderr)
    # Fallback: pageimages query (original)
    try:
        d = get_json(f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&piprop=original&format=json")
        pages = d.get("query", {}).get("pages", {})
        for p in pages.values():
            if p.get("original", {}).get("source"):
                return p["original"]["source"]
    except Exception as e:
        print(f"  pageimages err {title}: {e}", file=sys.stderr)
    return None


def download(url, out: Path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    im = Image.open(io.BytesIO(data)).convert("RGB")
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=92)
    return im.size, len(data) // 1024


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
