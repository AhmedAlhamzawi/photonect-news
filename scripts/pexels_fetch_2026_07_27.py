#!/usr/bin/env python3
"""FALLBACK media for the 2026-07-27 slate — KIE Nano Banana Pro returned HTTP 402
(credits insufficient) on ALL 20 submissions, so the entire slate falls back to
Pexels (the engine's documented tier-2 fallback).

One matched still per beat. Portrait orientation, center-cropped to 9:16, saved
as JPEG into the engine's image tree. Each slot has a list of candidate queries;
first query that returns a large-enough portrait wins. Every result is
Read-verified by hand before acceptance.
"""
from __future__ import annotations
import io, sys, time, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image  # type: ignore

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
D = "2026-07-27"


def load_key() -> str:
    for fn in (".env.local", ".env"):
        p = ROOT / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            if line.strip().startswith("PEXELS_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


KEY = load_key()
UA = "PhotonectNewsBot/1.0 (https://photonect.net)"

JOBS = [
    # 1. BANK FORGERY NETWORK — 31 detained, 243 forged loan files, 12 state banks
    (f"{D}-bank-forgery-network", "hero.jpg",
     ["investigation documents desk files", "office desk stacked documents folders", "paperwork investigation archive desk"]),
    (f"{D}-bank-forgery-network", "broll_1.jpg",
     ["rubber stamp document paperwork", "official stamp seal papers", "signing contract stamp documents"]),
    (f"{D}-bank-forgery-network", "broll_2.jpg",
     ["bank counter interior", "bank teller window", "bank lobby interior people"]),
    (f"{D}-bank-forgery-network", "broll_3.jpg",
     ["gold bars stack", "gold bullion money", "gold ingots cash"]),
    # 2. DOLLAR vs OFFICIAL RATE GAP — 150,200 street vs 132,000 official per $100
    (f"{D}-dollar-official-gap", "hero.jpg",
     ["money exchange counter cash", "currency exchange market", "counting cash banknotes market"]),
    (f"{D}-dollar-official-gap", "broll_1.jpg",
     ["hundred dollar bills hand", "dollar banknotes closeup", "cash dollars fan hand"]),
    (f"{D}-dollar-official-gap", "broll_2.jpg",
     ["classical bank building columns", "government building columns facade", "marble hall columns institution"]),
    (f"{D}-dollar-official-gap", "broll_3.jpg",
     ["man paying cash counter", "hand giving money cashier", "paying banknotes shop counter"]),
    # 3. IRAQI FUEL OIL TO LEBANON — $2.7bn owed, 2m tons/yr
    (f"{D}-fuel-to-lebanon-debt", "hero.jpg",
     ["oil tanker ship port", "fuel tanker vessel terminal", "cargo tanker harbour"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_1.jpg",
     ["power plant smokestacks dusk", "thermal power station coast", "industrial plant chimneys evening"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_2.jpg",
     ["empty conference table meeting room", "negotiation table chairs room", "boardroom empty chairs"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_3.jpg",
     ["stacked invoices paperwork desk", "accounting ledger book desk", "bills documents pile office"]),
    # 4. GULF POWER LINK DELAYED — 500 MW phase 1, slipped to end-Aug 2026 or later
    (f"{D}-gulf-power-link-delay", "hero.jpg",
     ["electricity pylons desert", "high voltage transmission towers", "power lines towers landscape"]),
    (f"{D}-gulf-power-link-delay", "broll_1.jpg",
     ["electrical substation transformers", "power substation equipment", "electric transformer station"]),
    (f"{D}-gulf-power-link-delay", "broll_2.jpg",
     ["dark room electric fan heat", "power outage candle home", "hot room fan window"]),
    (f"{D}-gulf-power-link-delay", "broll_3.jpg",
     ["power plant turbines industrial", "gas power plant aerial", "energy plant facility"]),
    # 5. PM ANKARA VISIT: WATER + DEVELOPMENT ROAD  (silent V10 control)
    (f"{D}-turkey-water-road-visit", "hero.jpg",
     ["dam reservoir mountains", "hydroelectric dam water", "concrete dam aerial"]),
    (f"{D}-turkey-water-road-visit", "broll_1.jpg",
     ["dry cracked riverbed drought", "dried river bed earth", "drought cracked ground water"]),
    (f"{D}-turkey-water-road-visit", "broll_2.jpg",
     ["railway construction desert", "highway construction machinery", "road construction excavator landscape"]),
    (f"{D}-turkey-water-road-visit", "broll_3.jpg",
     ["irrigation canal farm field", "water channel agriculture field", "farmer irrigation water crops"]),
]


def search(query: str):
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": "portrait", "per_page": 8, "size": "large"})
    req = urllib.request.Request(url, headers={"Authorization": KEY, "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        import json
        return json.loads(r.read().decode()).get("photos", [])


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def save_916(data: bytes, out: Path) -> tuple:
    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    target = 9 / 16
    if w / h > target:
        nw = int(h * target); x = (w - nw) // 2
        im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target); y = (h - nh) // 2
        im = im.crop((0, y, w, y + nh))
    if im.width > 1080:
        im = im.resize((1080, 1920), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=92)
    return im.size


def main() -> int:
    only = set(sys.argv[1:])
    jobs = [j for j in JOBS if not only or j[0] in only or f"{j[0]}/{j[1]}" in only]
    ok = 0
    for slug, fname, queries in jobs:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname} (on disk)"); ok += 1; continue
        done = False
        for q in queries:
            try:
                photos = search(q)
            except Exception as e:
                print(f"  ! search '{q}' {slug}/{fname}: {e}", file=sys.stderr); time.sleep(1); continue
            for p in photos:
                src = p.get("src", {})
                url = src.get("large2x") or src.get("original") or src.get("large")
                if not url:
                    continue
                try:
                    size = save_916(fetch(url), out)
                    print(f"  OK {slug}/{fname}  q='{q}'  {size}  id={p.get('id')}  by={p.get('photographer')}")
                    ok += 1; done = True
                except Exception as e:
                    print(f"  ! dl {slug}/{fname}: {e}", file=sys.stderr)
                break
            if done:
                break
            time.sleep(0.3)
        if not done:
            print(f"  MISSING {slug}/{fname}", file=sys.stderr)
        time.sleep(0.3)
    print(f"\n== {ok}/{len(jobs)} fetched ==")
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
