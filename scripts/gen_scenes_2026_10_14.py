#!/usr/bin/env python3
"""Generate the 2026-10-14 slate scenes via KIE Nano Banana Pro (9:16 2K).

KIE balance at start: 225.5 credits. 11 generated frames; the other 9 are reused/real (see place_images_2026_10_14.py).
Task IDs are persisted BEFORE polling; download passes info["data"] to first_image_url; curl with a browser UA.
No real named individual is depicted in any generated frame. Re-run with "slug/file" args to regenerate specific slots.
"""
from __future__ import annotations
import sys, time, json, io, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import NEG, STATUS_URL, http_get, first_image_url, submit  # type: ignore
from PIL import Image

D = "2026-10-14"
LEAD = "IRAQ, MIDDLE EAST."
NOUI = ("FULL-BLEED photograph filling the entire frame edge to edge; absolutely no smartphone status bar, no battery/wifi/clock, "
        "no app interface, no news graphics, no headline or paragraph text, no UI chrome, no screenshot, no border, no letters of any alphabet, "
        "no burned-in captions, no price boards, one single uncropped photograph, not a collage, not a grid")
UP = "upright vertical portrait orientation, level horizon, not rotated, not tilted"
NOFACE = "anonymous ordinary Iraqi Arab people, faces turned away or out of focus, no recognisable person, absolutely not South Asian, not East Asian, not Western"
NOPEOPLE = "no people at all anywhere in the frame"
BLANK = "all signage, plaques and surfaces completely blank, no lettering of any alphabet anywhere, no logos, no flags"
WARM = "warm early-October weather, light shirts, no winter coats"
NOTES = ("banknotes stacked edge-on and out of focus so that no denomination, portrait or lettering is legible anywhere, no face on any note, "
         "absolutely no US dollar bills unless stated")
IQ_ARCH = "beige concrete-block buildings, flat roofs, wall-mounted AC units, tangled overhead cables, dusty pavement"

JOBS = [
 # ── A · customs exemption on imported food + medicine ──
 (f"{D}-a-customs-food-medicine", "hero.jpg",
  f"{LEAD} Wide editorial photo at golden hour of the container terminal at Umm Qasr port in Basra: stacks of plain unbranded shipping containers, a gantry crane lifting a container, "
  f"a few refrigerated food containers on trucks at a customs inspection lane, hazy warm sky, {UP}, {NOPEOPLE}, {BLANK}, no shipping-line logos, {NOUI}, {NEG}"),
 (f"{D}-a-customs-food-medicine", "broll_1.jpg",
  f"{LEAD} Editorial photo inside a small Baghdad pharmacy: tall shelves packed with plain white and pastel medicine boxes, a pharmacist's hands placing a box on the glass counter, "
  f"an anonymous customer seen from behind, warm fluorescent light, all packaging completely blank, {UP}, {NOFACE}, {BLANK}, {NOUI}, {NEG}"),
 # ── B · dollar 167,000 ──
 (f"{D}-b-dollar-167000-rebound", "hero.jpg",
  f"{LEAD} Editorial close-up photo at a money-exchange counter in Baghdad's Kifah street: a cashier's hands fanning a thick stack of green US dollar banknotes held edge-on above a glass counter, "
  f"a banknote counting machine blurred behind, warm tungsten light, {NOTES}, {UP}, {NOFACE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-b-dollar-167000-rebound", "broll_3.jpg",
  f"{LEAD} Editorial photo of a busy traditional food market in Baghdad: sacks of rice, sugar and lentils, crates of tomatoes, an anonymous woman in an abaya seen from behind choosing produce, "
  f"{IQ_ARCH}, {WARM}, {UP}, {NOFACE}, {BLANK}, no price tags or price boards, {NOUI}, {NEG}"),
 # ── C · Jordan lost Kirkuk oil ──
 (f"{D}-c-jordan-kirkuk-oil", "broll_1.jpg",
  f"Wide editorial photo of a long convoy of plain white oil tanker trucks driving along a straight two-lane desert highway in western Iraq towards the Jordanian border at sunrise, "
  f"flat empty desert, long shadows, {UP}, {NOPEOPLE}, {BLANK}, no logos or lettering on the tankers, {NOUI}, {NEG}"),
 # ── D · retiree loan fraud ──
 (f"{D}-d-retirees-loans-fraud", "hero.jpg",
  f"{LEAD} Editorial photo of an elderly Iraqi retired man in a grey suit jacket and a traditional cap, seen from behind and slightly side-on, waiting in a queue in a plain bank hall, "
  f"holding a worn paper envelope, soft window light, {UP}, {NOFACE}, {BLANK}, no bank logos, {NOUI}, {NEG}"),
 (f"{D}-d-retirees-loans-fraud", "broll_2.jpg",
  f"{LEAD} Editorial photo inside a crowded home-appliance shop in Baghdad: rows of new refrigerators, washing machines and air-conditioners in plastic wrap, "
  f"an anonymous elderly man seen from behind talking to a salesman, {UP}, {NOFACE}, {BLANK}, no brand logos on any appliance, no price tags, {NOUI}, {NEG}"),
 # ── E · marriage + divorce (V10.1 control) ──
 (f"{D}-e-marriage-35440-divorce", "hero.jpg",
  f"{LEAD} Editorial night photo of a joyful Iraqi wedding procession in a Baghdad street: a bride in a white gown and a groom in a dark suit seen from behind walking arm in arm, "
  f"relatives clapping, strings of warm fairy lights, confetti, {UP}, {NOFACE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-e-marriage-35440-divorce", "broll_1.jpg",
  f"Close-up editorial photo of two plain gold wedding rings resting on a blank cream-coloured paper document on a dark wooden desk, a fountain pen beside them, "
  f"soft warm light, shallow depth of field, {UP}, {NOPEOPLE}, {BLANK}, all paper completely blank, {NOUI}, {NEG}"),
 (f"{D}-e-marriage-35440-divorce", "broll_2.jpg",
  f"{LEAD} Wide aerial drone photo of Baghdad at blue hour: the Tigris river curving through the city, bridges with traffic light trails, dense low beige buildings, palm trees, "
  f"{UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-e-marriage-35440-divorce", "broll_3.jpg",
  f"Editorial photo of a long empty corridor inside an Iraqi personal-status court building: plain wooden benches along beige walls, closed wooden doors, "
  f"a single anonymous woman in an abaya sitting far away at the end, seen from behind, cool daylight, {UP}, {NOFACE}, {BLANK}, no signs or plaques, {NOUI}, {NEG}"),
]

M = Path(__file__).with_name(f"_kie_jobs_{D.replace('-','_')}.json")
IMG = Path(__file__).resolve().parent.parent / "my-video" / "public" / "images" / "news"


def main():
    only = set(sys.argv[1:])
    jobs = json.loads(M.read_text()) if M.exists() else []
    for slug, f, p in JOBS:
        key = f"{slug}/{f}"
        if only and key not in only:
            continue
        out = IMG / slug / f
        if not only and out.exists() and out.stat().st_size > 50_000:
            continue
        tid = submit(p)
        jobs.append({"slug": slug, "file": f, "tid": tid, "out": str(out)})
        M.write_text(json.dumps(jobs, ensure_ascii=False, indent=1))
        print("submitted", slug, f, tid, flush=True)
    pending = [j for j in jobs if not j.get("ok")]
    deadline = time.time() + 14 * 60
    while pending and time.time() < deadline:
        still = []
        for j in pending:
            try:
                info = http_get(f"{STATUS_URL}?taskId={j['tid']}")
                data = info.get("data") or {}
                url = first_image_url(data)
                st = str(data.get("state") or "").lower()
                if url:
                    raw = subprocess.run(["curl", "-sL", "-A", "Mozilla/5.0", url], capture_output=True, check=True).stdout
                    im = Image.open(io.BytesIO(raw)); im.load()
                    out = Path(j["out"]); out.parent.mkdir(parents=True, exist_ok=True)
                    im.convert("RGB").save(out, "JPEG", quality=92)
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {im.size}", flush=True); continue
                if st in ("fail", "failed", "error"):
                    print(f"  ✗ {j['slug']}/{j['file']} {data.get('failMsg')}", flush=True); j["ok"] = "failed"; continue
            except Exception as e:
                print("  .", j["file"], e, flush=True)
            still.append(j)
        pending = still
        M.write_text(json.dumps(jobs, ensure_ascii=False, indent=1))
        if pending:
            time.sleep(8)
    print("== done ==", sum(1 for j in jobs if j.get("ok") is True), "/", len(jobs), flush=True)


if __name__ == "__main__":
    main()
