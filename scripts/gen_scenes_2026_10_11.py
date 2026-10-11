#!/usr/bin/env python3
"""Generate the 2026-10-11 slate scenes via KIE Nano Banana Pro (9:16 2K).

KIE balance at start: 531.5 credits. 14 generated frames; the other 6 are reused/real (see place_images_2026_10_11.py).
Task IDs are persisted BEFORE polling; download passes info["data"] to first_image_url; curl with a browser UA.
No real named individual is depicted in any generated frame. Re-run with "slug/file" args to regenerate specific slots.
"""
from __future__ import annotations
import sys, time, json, io, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import NEG, STATUS_URL, http_get, first_image_url, submit  # type: ignore
from PIL import Image

D = "2026-10-11"
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
 # ── A · Watan free plots ──
 (f"{D}-a-watan-95k-plots", "hero.jpg",
  f"{LEAD} Wide aerial drone photo at golden hour of a vast flat empty plot of desert land on the edge of Karbala, freshly graded dirt roads dividing it into a neat grid of hundreds of "
  f"residential plots marked by small concrete boundary stakes, a few date palms and low beige houses on the far horizon, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-a-watan-95k-plots", "broll_1.jpg",
  f"{LEAD} Ground-level editorial shot of a surveyor's red-and-white ranging pole and a theodolite on a tripod standing on an empty graded residential plot outside Najaf, "
  f"rows of concrete boundary stakes stretching to the horizon, a yellow grader working in the far distance, late afternoon light, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-a-watan-95k-plots", "broll_2.jpg",
  f"{LEAD} Editorial photo of an informal unplanned housing area on the edge of an Iraqi city: rough unplastered breezeblock houses, tangled overhead cables, a dirt alley with puddles, "
  f"an anonymous father and child in light clothes seen from behind walking home, {IQ_ARCH}, {WARM}, {UP}, {NOFACE}, {BLANK}, {NOUI}, {NEG}"),
 # ── C · Riyadh airport attack / Iraqi skies ──
 (f"{D}-c-riyadh-airport-flights", "hero.jpg",
  f"Editorial photo inside a large modern Gulf airport departures hall at night, almost empty, a few stranded travellers with suitcases sitting on the floor seen from behind, "
  f"blank dark flight-information screens, cool overhead light, sense of suspended flights, {UP}, {NOFACE}, {BLANK}, no airline logos, {NOUI}, {NEG}"),
 (f"{D}-c-riyadh-airport-flights", "broll_1.jpg",
  f"Wide editorial dusk photo of a large desert international airport with operations suspended: several white airliners parked motionless at their gates, an empty runway, "
  f"no smoke, no fire, no damage, calm orange-blue sky, sense of a grounded airport, {UP}, {NOPEOPLE}, {BLANK}, no airline logos or liveries, no lettering, {NOUI}, {NEG}"),
 (f"{D}-c-riyadh-airport-flights", "broll_2.jpg",
  f"Editorial photo looking up from the ground at a white twin-engine airliner banking away against a deep evening sky over the Gulf desert, contrail, "
  f"sense of a diverted flight, {UP}, {NOPEOPLE}, {BLANK}, no airline logo or livery, no lettering, {NOUI}, {NEG}"),
 (f"{D}-c-riyadh-airport-flights", "broll_3.jpg",
  f"Wide editorial photo of a large steel crude-oil pipeline running straight across a flat empty Arabian desert towards the horizon at sunrise, supported on concrete sleepers, "
  f"long shadows, pale golden sky, {UP}, {NOPEOPLE}, {BLANK}, no logos, {NOUI}, {NEG}"),
 # ── D · Salahaddin accounts director ──
 (f"{D}-d-salahaddin-7-properties", "hero.jpg",
  f"{LEAD} Editorial street photo of a row of new two-storey beige villas with ornate gates in a gated residential complex in a small Iraqi town in Salahaddin, palm trees, "
  f"clean paved street, late afternoon light, {UP}, {NOPEOPLE}, {BLANK}, no house numbers, {NOUI}, {NEG}"),
 (f"{D}-d-salahaddin-7-properties", "broll_1.jpg",
  f"{LEAD} Close-up editorial photo on a plain wooden office desk of several thick old government property-file folders tied with string and a stack of stamped title-deed papers, "
  f"a rubber stamp and a pen, all paper completely blank with no readable text, warm desk-lamp light, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-d-salahaddin-7-properties", "broll_2.jpg",
  f"{LEAD} Aerial drone photo looking down on a residential housing complex in a small Iraqi town: rows of identical two-storey beige houses with flat roofs, water tanks and small courtyards, "
  f"straight paved streets, palm trees, late afternoon light, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-d-salahaddin-7-properties", "broll_3.jpg",
  f"Close-up editorial photo of a wooden judge's gavel resting on its sound block on a dark wooden courtroom bench, a closed blank case file beside it, shallow depth of field, "
  f"dim warm light, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 # ── E · waste collection (V10.1 control) ──
 (f"{D}-e-waste-third-uncollected", "hero.jpg",
  f"{LEAD} Editorial street photo of a pile of overflowing black garbage bags and loose rubbish heaped against a wall at the corner of a residential alley in an Iraqi city, "
  f"a stray cat nearby, {IQ_ARCH}, hazy afternoon light, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-e-waste-third-uncollected", "broll_1.jpg",
  f"{LEAD} Editorial morning photo of an orange municipal garbage compactor truck in a clean Iraqi city street, two sanitation workers in orange vests seen from behind lifting a large bin, "
  f"{IQ_ARCH}, {UP}, {NOFACE}, {BLANK}, no lettering or logos on the truck, the truck front grille out of frame, {NOUI}, {NEG}"),
 (f"{D}-e-waste-third-uncollected", "broll_2.jpg",
  f"{LEAD} Editorial photo of the edge of a small rural village in southern Iraq, mud-brick and breezeblock houses, plastic rubbish scattered along a dusty canal bank and being burned in a small smouldering heap, "
  f"a few sheep, date palms, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-e-waste-third-uncollected", "broll_3.jpg",
  f"Wide editorial photo of a large open municipal landfill site in the Iraqi desert, a bulldozer pushing mounds of rubbish, flocks of birds, a garbage truck tipping its load, hazy sky, "
  f"{UP}, {NOPEOPLE}, {BLANK}, no lettering or logos, {NOUI}, {NEG}"),
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
