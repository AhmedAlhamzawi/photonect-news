#!/usr/bin/env python3
"""2026-09-17: AI image credits exhausted -> every slot is a hand-vetted REAL photo (Pexels /
Wikimedia Commons), chosen from search results and Read-verified after crop.
Crop to 9:16 around a (cx, cy) centre fraction (default centre), resize 1536x2730, JPEG q92.
Writes my-video/public/images/news/2026-09-17-<slug>/ and scripts/_image_credits_2026_09_17.json.
Usage: place_images_2026_09_17.py [slug | slug/file]"""
import io, json, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net)"}
D = "2026-09-17"
W, H = 1536, 2730

# (file, source, id, cx, cy)  source: "commons" -> File: title, "pexels" -> photo id
PLAN = {
 "a-gulf-cup-26-players": [
  ("hero.jpg",    "pexels",  15998587, 0.50, 0.62),
  ("broll_1.jpg", "commons", "File:AH (cropped).jpg", 0.38, 0.42),
  ("broll_2.jpg", "commons", "File:Prince Abdullah Al-Faisal Sports City.jpg", 0.50, 0.55),
  ("broll_3.jpg", "commons", "File:4822290 AE7I6542 (cropped).jpg", 0.50, 0.35),
 ],
 "b-dollar-158850-159000": [
  ("hero.jpg",    "pexels", 6266699, 0.55, 0.50),
  ("broll_1.jpg", "pexels", 35827231, 0.45, 0.40),
  ("broll_2.jpg", "pexels", 6266459, 0.50, 0.45),
  ("broll_3.jpg", "pexels", 38862154, 0.50, 0.55),
 ],
 "c-hormuz-45-billion": [
  ("hero.jpg",    "pexels",  20412610, 0.50, 0.45),
  ("broll_1.jpg", "commons", "File:Strait of Hormuz and Musandam Peninsula (MODIS 2018-12-10).jpg", 0.55, 0.50),
  ("broll_2.jpg", "commons", "File:Tankers at the Iraqi Al Basra Oil Terminal in the Northern Arabian Gulf.jpg", 0.50, 0.60),
  ("broll_3.jpg", "pexels",  12069460, 0.35, 0.45),
 ],
 "d-mp-nouri-7-years": [
  ("hero.jpg",    "pexels",  6077189, 0.50, 0.45),
  ("broll_1.jpg", "commons", "File:Republican Palace, Baghdad, Iraq front.jpg", 0.72, 0.50),
  ("broll_2.jpg", "pexels",  14655998, 0.50, 0.45),
  ("broll_3.jpg", "pexels",  35029019, 0.50, 0.45),
 ],
 "e-basra-crude-minus-8": [
  ("hero.jpg",    "pexels",  7392237, 0.50, 0.45),
  ("broll_1.jpg", "commons", "File:Al Basrah Oil Terminal essential to Iraq's economy DVIDS202701.jpg", 0.50, 0.45),
  ("broll_2.jpg", "pexels", 35767046, 0.50, 0.50),
  ("broll_3.jpg", "pexels",  5942527, 0.50, 0.45),
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
