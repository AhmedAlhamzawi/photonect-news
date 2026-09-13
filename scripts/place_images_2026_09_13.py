#!/usr/bin/env python3
"""2026-09-13: KIE (1.5 credits) and Higgsfield (0.38) exhausted. Lead hero = Higgsfield
nano_banana_pro; every other slot = hand-vetted real photo (Pexels / Wikimedia Commons),
chosen from contact sheets and Read-verified. Center-crop to 9:16 (or blur-fill when the
source is too small/landscape), write into my-video/public/images/news/<slug>/."""
import io, json, sys, urllib.request
from pathlib import Path
from PIL import Image, ImageFilter
ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
CAND = Path(sys.argv[1])  # scratchpad/cand
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net)"}
D = "2026-09-13"
PLAN = {  # slug: [(file, cand_tag, idx, mode)] — FINAL mapping after the Opus gate
 "a-farmers-dues-500bn": [("broll_1.jpg","a_money",7,"crop"),("broll_2.jpg","a_harv",3,"crop"),("broll_3.jpg","a_hands",4,"crop")],
 "b-dollar-three-cities": [("hero.jpg","b_cash",1,"crop"),("broll_1.jpg","b_bag2",2,"crop"),("broll_2.jpg","b_basra",6,"fill"),("broll_3.jpg","b_erbil",2,"crop")],
 "c-medical-colleges-warning": [("hero.jpg","c_med2",4,"crop"),("broll_1.jpg","c_med2",1,"crop"),("broll_2.jpg","c_med",1,"crop"),("broll_3.jpg","c_ward",0,"crop")],
 "d-qasim-repairs-400m": [("hero.jpg","d_mech",6,"crop"),("broll_1.jpg","d_sign",6,"crop"),("broll_2.jpg","d_mech",8,"crop"),("broll_3.jpg","d_sign",7,"crop")],
 "e-saudi-drone-platform": [("hero.jpg","e_desert",1,"crop"),("broll_1.jpg","saad_maan",0,"fill"),("broll_2.jpg","e_pipe",0,"fill"),("broll_3.jpg","e_desert",9,"crop")],
}
W, H = 1536, 2730
credits = {}
def full(item):
    u = item["thumb"]
    if item["src"] == "pexels": u = u.split("?")[0] + "?auto=compress&cs=tinysrgb&w=1800"
    return Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read())).convert("RGB")
def crop(im):
    r = W / H
    if im.width / im.height > r:
        nw = int(im.height * r); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / r); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    return im.resize((W, H), Image.LANCZOS)
def fill(im):
    bg = crop(im).filter(ImageFilter.GaussianBlur(40))
    fg = im.copy(); s = min(W / fg.width, H * 0.62 / fg.height); fg = fg.resize((int(fg.width * s), int(fg.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2)); return bg
for slug, jobs in PLAN.items():
    out = IMG / f"{D}-{slug}"; out.mkdir(parents=True, exist_ok=True)
    for f, tag, i, mode in jobs:
        item = json.load(open(CAND / f"{tag}.json"))[i]
        im = full(item); im = crop(im) if mode == "crop" else fill(im)
        im.save(out / f, quality=92)
        credits[f"{slug}/{f}"] = {"src": item["src"], "title": item["title"], "page": item["page"], "artist": item["artist"], "license": item["lic"]}
        print(f"{slug}/{f} <- {item['src']} {item['title'][:50]} ({item['w']}x{item['h']})")
credits["a-farmers-dues-500bn/hero.jpg"] = {"src": "higgsfield nano_banana_pro 9:16 2k", "job": "efb1f370-abf6-4388-a6b3-6984556d4fbc"}
json.dump(credits, open(ROOT / "scripts/_image_credits_2026_09_13.json", "w"), ensure_ascii=False, indent=1)
