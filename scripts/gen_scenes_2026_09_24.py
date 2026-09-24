#!/usr/bin/env python3
"""Generate the 2026-09-24 slate HERO scenes via KIE Nano Banana Pro (9:16 2K).

Budget: KIE had 101.5 credits at start and Higgsfield 0.38, so only the five
heroes are generated; brolls come from Commons/Pexels (see _image_credits_2026_09_24.json).
Task IDs are persisted BEFORE polling; download passes info["data"] to first_image_url.
No real named individual is depicted in any generated frame.
"""
from __future__ import annotations
import sys, time, json, io, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import NEG, STATUS_URL, http_get, first_image_url, submit  # type: ignore
from PIL import Image

D = "2026-09-24"
LEAD = "IRAQ, MIDDLE EAST."
NOUI = ("absolutely no user-interface, no app screens, no news graphics, no readable text "
        "on any screen, no phone or tablet UI, no burned-in captions, no price boards")
UP = "upright vertical portrait orientation, level horizon, not rotated, not tilted"
NOFACE = "anonymous ordinary people, faces turned away or out of focus, no recognisable person"
NOPEOPLE = "no people at all anywhere in the frame"
BLANK = "all signage and surfaces completely blank, no lettering of any alphabet anywhere"
WARM = "warm late-September weather, light shirts, no winter coats"
NOTE_EDGE = ("banknotes stacked edge-on and out of focus so that no denomination, portrait or "
             "lettering is legible anywhere, no face on any note")

JOBS = [
 (f"{D}-a-france-13-million", "hero.jpg",
  f"Editorial photograph inside a modern European bank vault, a heavy round steel vault door standing open, "
  f"a metal trolley with neatly strapped cash bundles, {NOTE_EDGE}, cool blue-grey light, polished floor, "
  f"sense of money being released and returned, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-b-dollar-week-2000", "hero.jpg",
  f"{LEAD} Street-level editorial shot of a small currency exchange shop on a busy Baghdad market street in "
  f"late-afternoon light, glass counter, roll-up shutter raised, an anonymous man in a light shirt at the "
  f"counter seen from behind, dusty pavement, tangled overhead cables, {WARM}, {UP}, {NOFACE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-c-ebrd-minus-12", "hero.jpg",
  f"Wide cinematic editorial shot of several large crude oil tankers lying idle at anchor in a hazy Gulf sea "
  f"at dusk, flat calm water, orange sky, distant arid coastline, a sense of stalled trade, no company logos, "
  f"no flags, no hull markings, {UP}, {NOPEOPLE}, {BLANK}, {NOUI}, {NEG}"),
 (f"{D}-d-gulf-cup-oman-draw", "hero.jpg",
  f"{LEAD} Night football stadium in the Gulf, packed stands of anonymous Iraqi supporters seen from behind "
  f"waving plain red, white and black flags without any emblem or writing, floodlights, green pitch below, "
  f"warm humid night, joyful atmosphere, {UP}, {NOFACE}, {BLANK}, no team crests, no sponsor boards, {NOUI}, {NEG}"),
 (f"{D}-e-mehran-453-million", "hero.jpg",
  f"{LEAD} Long queue of heavy cargo lorries loaded with pallets of ceramic tiles and bundled steel rebar "
  f"waiting at a desert land border crossing between Iran and Iraq, low mountains behind, hazy afternoon "
  f"sun, dust, plain unmarked customs canopy, {UP}, {NOFACE}, {BLANK}, no licence plates legible, no logos, {NOUI}, {NEG}"),
]

M = Path(__file__).with_name(f"_kie_jobs_{D.replace('-','_')}.json")
IMG = Path(__file__).resolve().parent.parent / "my-video" / "public" / "images" / "news"

def main():
    only = set(sys.argv[1:])
    jobs = json.loads(M.read_text()) if M.exists() else []
    for slug, f, p in JOBS:
        if only and f"{slug}/{f}" not in only: continue
        tid = submit(p)
        jobs.append({"slug": slug, "file": f, "tid": tid, "out": str(IMG / slug / f)})
        M.write_text(json.dumps(jobs, ensure_ascii=False, indent=1))
        print("submitted", slug, f, tid, flush=True)
    pending = [j for j in jobs if not j.get("ok")]
    deadline = time.time() + 12 * 60
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
        if pending: time.sleep(8)
    print("== done ==", sum(1 for j in jobs if j.get("ok") is True), "/", len(jobs))

if __name__ == "__main__":
    main()
