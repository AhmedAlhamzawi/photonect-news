#!/usr/bin/env python3
"""2026-09-19: AI image credits exhausted -> every slot is a hand-vetted REAL photo (Pexels /
Wikimedia Commons), chosen from search results and Read-verified after crop.
Crop to 9:16 around a (cx, cy) centre fraction (default centre), resize 1536x2730, JPEG q92.
Writes my-video/public/images/news/2026-09-19-<slug>/ and scripts/_image_credits_2026_09_19.json.
Usage: place_images_2026_09_19.py [slug | slug/file]"""
import io, json, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"}
D = "2026-09-19"
W, H = 1536, 2730

# (file, source, id, cx, cy)  source: "commons" -> File: title, "pexels" -> photo id
PLAN = {
 "a-najaf-electricity-graft": [
  ("hero.jpg",    "pexels", 13992359, 0.50, 0.45),
  ("broll_1.jpg", "pexels", 28697750, 0.50, 0.45),
  ("broll_2.jpg", "pexels",  6801148, 0.50, 0.50),
  ("broll_3.jpg", "pexels", 20288664, 0.50, 0.40),
 ],
 "b-dollar-160250-baghdad": [
  ("hero.jpg",    "pexels",  7680565, 0.50, 0.50),
  ("broll_1.jpg", "pexels",  6266447, 0.50, 0.45),
  ("broll_2.jpg", "pexels", 27593509, 0.50, 0.45),
  ("broll_3.jpg", "pexels", 19582434, 0.50, 0.45),
 ],
 "c-aqari-platform-kirkuk": [
  ("hero.jpg",    "pexels", 31221014, 0.50, 0.50),
  ("broll_1.jpg", "pexels",  8962684, 0.50, 0.45),
  ("broll_2.jpg", "pexels", 13660674, 0.50, 0.45),
  ("broll_3.jpg", "pexels", 12048264, 0.50, 0.50),
 ],
 "d-cbi-reserves-speculation": [
  ("hero.jpg",    "pexels", 25913209, 0.50, 0.45),
  ("broll_1.jpg", "pexels",  6266282, 0.50, 0.50),
  ("broll_2.jpg", "pexels",  7567223, 0.50, 0.45),
  ("broll_3.jpg", "pexels",  6672308, 0.50, 0.45),
 ],
 "e-anbar-petrol-queues-end": [
  ("hero.jpg",    "pexels", 28001555, 0.50, 0.45),
  ("broll_1.jpg", "pexels",  9216589, 0.50, 0.45),
  ("broll_2.jpg", "pexels", 39114829, 0.50, 0.45),
  ("broll_3.jpg", "pexels", 16975390, 0.50, 0.45),
 ],
}


def pexels_key():
    for fn in (".env.local", ".env"):
        p = ROOT / fn
        if p.exists():
            for l in p.read_text().splitlines():
                if l.startswith("PEXELS_API_KEY="):
                    return l.split("=", 1)[1].strip().strip('"').strip("'")


def get(url, headers=UA):
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120).read()


def resolve(src, ident):
    if src == "pexels":
        ph = json.loads(get(f"https://api.pexels.com/v1/photos/{ident}", {**UA, "Authorization": pexels_key()}))
        url = ph["src"]["original"]
        meta = {"src": "pexels", "title": ph.get("alt", ""), "page": ph["url"], "artist": ph["photographer"], "license": "Pexels License"}
    else:
        q = urllib.parse.urlencode({"action": "query", "format": "json", "titles": ident, "prop": "imageinfo", "iiprop": "url|size|extmetadata"})
        pg = next(iter(json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))["query"]["pages"].values()))
        ii = pg["imageinfo"][0]; md = ii.get("extmetadata", {})
        url = ii["url"]
        meta = {"src": "commons", "title": ident, "page": ii["descriptionurl"],
                "artist": md.get("Artist", {}).get("value", "")[:200], "license": md.get("LicenseShortName", {}).get("value", "")}
    return url, meta


def crop(im, cx, cy):
    r = W / H
    if im.width / im.height > r:
        nw = int(im.height * r); x = int(min(max(cx * im.width - nw / 2, 0), im.width - nw))
        im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / r); y = int(min(max(cy * im.height - nh / 2, 0), im.height - nh))
        im = im.crop((0, y, im.width, y + nh))
    return im.resize((W, H), Image.LANCZOS)


cp = ROOT / f"scripts/_image_credits_{D.replace('-', '_')}.json"
credits = json.load(open(cp)) if cp.exists() else {}
for slug, jobs in PLAN.items():
    out = IMG / f"{D}-{slug}"; out.mkdir(parents=True, exist_ok=True)
    for f, src, ident, cx, cy in jobs:
        key = f"{slug}/{f}"
        if ONLY and ONLY not in (key, slug):
            continue
        url, meta = resolve(src, ident)
        im = ImageOps.exif_transpose(Image.open(io.BytesIO(get(url)))).convert("RGB")
        crop(im, cx, cy).save(out / f, "JPEG", quality=92)
        credits[key] = meta
        print(f"{key} <- {src} {str(ident)[:70]} ({im.width}x{im.height})")
json.dump(credits, open(cp, "w"), ensure_ascii=False, indent=1)
