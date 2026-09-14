#!/usr/bin/env python3
"""2026-09-14: KIE (1.5 credits) and Higgsfield (0.38) exhausted -> every slot is a hand-vetted
REAL photo (Pexels / Wikimedia Commons), chosen from contact sheets and Read-verified.
Center-crop to 9:16, or crop a fractional box (x0,y0,x1,y1) first to isolate a named person.
Writes into my-video/public/images/news/<slug>/ and scripts/_image_credits_2026_09_14.json."""
import io, json, sys, urllib.request
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
CAND = Path(sys.argv[1])  # scratchpad/cand
ONLY = sys.argv[2] if len(sys.argv) > 2 else None
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net)"}
D = "2026-09-14"
PLAN = {  # slug: [(file, cand_tag, idx, box-or-None)]
 "a-electricity-director-7-years": [("hero.jpg","a_tower",6,None),("broll_1.jpg","a_gavel",3,None),("broll_2.jpg","b_100usd",4,None),("broll_3.jpg","a_gavel",11,None)],
 "b-dollar-buy-sell-gap": [("hero.jpg","b_count",1,None),("broll_1.jpg","b_count",7,None),("broll_2.jpg","b_100usd",9,None),("broll_3.jpg","b_count",0,None)],
 "c-basra-ammonia-114": [("hero.jpg","c_ammonia",7,None),("broll_1.jpg","c_ammonia",5,None),("broll_2.jpg","c_ambn",4,None),("broll_3.jpg","c_pipes2",2,None)],
 "d-retirees-million-minimum": [("hero.jpg","d_beadhands",5,None),("broll_1.jpg","d_beadhands",3,None),("broll_2.jpg","d_beads",11,None),("broll_3.jpg","d_beadhands",2,None)],
 "e-zaidi-total-10m-barrels": [("hero.jpg","e_zaidi",1,(0.03,0.03,0.53,0.71)),("broll_1.jpg","e_elysee",8,None),("broll_2.jpg","e_flare",4,None),("broll_3.jpg","e_pouy",5,None)],
}
W, H = 1536, 2730
cp = ROOT / "scripts/_image_credits_2026_09_14.json"
credits = json.load(open(cp)) if cp.exists() else {}
def full(item):
    u = item["thumb"]
    if item["src"] == "pexels": u = u.split("?")[0] + "?auto=compress&cs=tinysrgb&w=2000"
    return Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read())).convert("RGB")
def crop(im):
    r = W / H
    if im.width / im.height > r:
        nw = int(im.height * r); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / r); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    return im.resize((W, H), Image.LANCZOS)
for slug, jobs in PLAN.items():
    out = IMG / f"{D}-{slug}"; out.mkdir(parents=True, exist_ok=True)
    for f, tag, i, box in jobs:
        if ONLY and f"{slug}/{f}" != ONLY and slug != ONLY: continue
        item = json.load(open(CAND / f"{tag}.json"))[i]
        im = full(item)
        if box: im = im.crop((int(box[0]*im.width), int(box[1]*im.height), int(box[2]*im.width), int(box[3]*im.height)))
        crop(im).save(out / f, quality=92)
        credits[f"{slug}/{f}"] = {"src": item["src"], "title": item["title"], "page": item["page"], "artist": item["artist"], "license": item["lic"]}
        print(f"{slug}/{f} <- {item['src']} {item['title'][:60]} ({item['w']}x{item['h']})")
json.dump(credits, open(cp, "w"), ensure_ascii=False, indent=1)
