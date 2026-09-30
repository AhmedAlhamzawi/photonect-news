#!/usr/bin/env python3
"""2026-09-30: all 20 frames (KIE -0.5 credits + Higgsfield 0.38 = no generation possible) sourced from
Pexels + Wikimedia Commons, hand-vetted from contact sheets. Crop to 9:16 around a
(cx, cy) centre fraction (default centre), resize 1536x2730, JPEG q92.
Writes my-video/public/images/news/2026-09-30-<slug>/ and scripts/_image_credits_2026_09_30.json.
Usage: place_images_2026_09_30.py [slug | slug/file]"""
import io, json, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"}
D = "2026-09-30"
W, H = 1536, 2730

# (file, source, id, cx, cy)  source: "commons" -> File: title, "pexels" -> photo id
PLAN = {
 "a-gold-5kg-land-registry": [
  ("hero.jpg",    "pexels", 10816570, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 32077588, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 36824933, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 10481263, 0.50, 0.5),
 ],
 "b-dollar-157250-third-rise": [
  ("hero.jpg",    "pexels", 14820453, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 7111579, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 6266638, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 8886968, 0.50, 0.5),
 ],
 "c-coalition-mission-ends": [
  ("hero.jpg",    "commons", "File:2026 Ali al-Zaidi (cropped).jpg", 0.50, 0.5),
  ("broll_1.jpg", "commons", "File:Iraqi soldiers with 2nd Battalion, Commando Brigade, practice marksmanship training with Task Force Al-Taqaddum, Combined Joint Task Force – Operation Inherent Resolve, April 17, 2017.jpg", 0.50, 0.5),
  ("broll_2.jpg", "commons", "File:Erbil International Airport - August 2025.jpg", 0.50, 0.5),
  ("broll_3.jpg", "commons", "File:Moqtada al-Sader in tehran 2019 (cropped).jpg", 0.50, 0.5),
 ],
 "d-watan-275000-plots": [
  ("hero.jpg",    "pexels", 16234528, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 37618622, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 6070743, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 10349587, 0.50, 0.5),
 ],
 "e-ali-ammar-219kg": [
  ("hero.jpg",    "commons", "File:CGI Iraq Flag.png", 0.50, 0.5),
  ("broll_1.jpg", "pexels", 7811531, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 28320724, 0.50, 0.5),
  ("broll_3.jpg", "commons", "File:Russian championship in weightlifting 39.jpg", 0.50, 0.5),
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
