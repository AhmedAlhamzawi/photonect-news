#!/usr/bin/env python3
"""Cinematic AI scenes for the 2026-07-01 slate via Nano Banana Pro 9:16 2K.
Face slots handled by fetch_faces_2026_07_01.py: Shelton hero, Araghchi broll_1, Rubio broll_3."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage, no digits")

IRAQ = "2026-07-01-iraq-graft-convictions"
SWIFT = "2026-07-01-nasa-swift-rescue"
LEB = "2026-07-01-lebanon-war-committee"
WIMB = "2026-07-01-wimbledon-shelton-upset"
HEAT = "2026-07-01-europe-heatwave-record"
TREG = "2026-07-01-tregzi-fda-cancer"

JOBS = [
    # IRAQ GRAFT CONVICTIONS (all scenes — sensitive people, use neutral imagery)
    (IRAQ, "hero.jpg", f"Cinematic wide shot of a solemn Iraqi courtroom of justice at dusk, a large empty judge's bench, a set of brass scales of justice in the foreground, a plain Iraqi flag on a stand, dignified anti-corruption mood, dramatic directional light, {NEG}, {X}"),
    (IRAQ, "broll_1.jpg", f"A dramatic close cinematic shot of a wooden judge's gavel resting beside brass scales of justice and stacks of official case documents on a dark desk, solemn courtroom light, a sense of a verdict, {NEG}, {X}"),
    (IRAQ, "broll_2.jpg", f"A symbolic cinematic shot of confiscated wealth behind a heavy open steel bank-vault door, neat stacks of banknotes, gold bars and a set of house keys and small property models, cold blue security light, themes of seized assets, no readable text on the money, {NEG}, {X}"),
    (IRAQ, "broll_3.jpg", f"A cinematic wide exterior of an imposing government finance-ministry building in Baghdad at dusk, classical columns, warm institutional lighting, a sense of state authority and recovered public funds, {NEG}, {X}"),
    # NASA SWIFT RESCUE (all scenes)
    (SWIFT, "hero.jpg", f"A breathtaking cinematic view of a scientific space telescope satellite with gold-foil body and solar panels orbiting high above the curved blue Earth at sunrise, stars in the black cosmos, a subtle sense of peril, ultra detailed, {NEG}, {X}"),
    (SWIFT, "broll_1.jpg", f"A cinematic scene of a compact robotic servicing spacecraft with extended articulated robotic arms slowly approaching and grappling a satellite in low Earth orbit, the blue planet below, dramatic space lighting, {NEG}, {X}"),
    (SWIFT, "broll_2.jpg", f"A tense cinematic shot of a satellite skimming very low over the thin glowing upper atmosphere of Earth, a faint orange reentry heat glow beginning at its edges, the curvature of the planet below, sense of imminent decay, {NEG}, {X}"),
    (SWIFT, "broll_3.jpg", f"A dramatic cinematic close shot of an ion-thruster spacecraft firing a cone of glowing blue plasma in the blackness of space, gently boosting a satellite to a higher orbit, Earth faintly below, {NEG}, {X}"),
    # LEBANON WAR COMMITTEE (hero + broll_2 scenes; broll_1=Araghchi, broll_3=Rubio faces)
    (LEB, "hero.jpg", f"Cinematic wide shot of a tense high-level trilateral diplomatic negotiation room at dusk, a long polished empty table with microphones and water glasses, three plain unmarked flag stands, a blurred Beirut Mediterranean skyline through tall windows, charged anticipatory mood, {NEG}, {X}"),
    (LEB, "broll_2.jpg", f"A dramatic cinematic close shot of a formal signed diplomatic agreement document with two elegant fountain pens on a dark polished desk beside an old brass clock, soft directional light, a sense of a ticking 60-day deadline, no readable text, {NEG}, {X}"),
    # WIMBLEDON (broll scenes; hero=Shelton face)
    (WIMB, "broll_1.jpg", f"A cinematic wide shot of a pristine green grass tennis court during a Grand Slam match, two players mid-rally, packed sunlit grandstands, classic tournament atmosphere, bright crisp daylight, shallow depth of field, {NEG}, {X}"),
    (WIMB, "broll_2.jpg", f"A dramatic slow-motion cinematic close-up of a yellow tennis ball bouncing exactly on the white chalk line of a green grass court, a puff of chalk dust, decisive-point tension, shallow depth of field, {NEG}, {X}"),
    (WIMB, "broll_3.jpg", f"A cinematic shot from behind of a dejected male tennis player sitting alone on the courtside bench with a white towel over his shoulders and a racket beside him, long evening shadows, a sense of a painful defeat, face not visible, {NEG}, {X}"),
    # EUROPE HEATWAVE (all scenes)
    (HEAT, "hero.jpg", f"A cinematic wide shot of a historic European city under a blistering record heatwave, a huge blazing white sun low over the rooftops, intense heat shimmer distorting the air, a hazy bleached sky, oppressive mood, {NEG}, {X}"),
    (HEAT, "broll_1.jpg", f"A cinematic shot of exhausted people seeking relief around a large public fountain in a European city plaza under harsh blazing sunlight, splashing water, heat haze, crowded and sweltering, {NEG}, {X}"),
    (HEAT, "broll_2.jpg", f"A symbolic cinematic close-up of an old analog outdoor thermometer with its red mercury column pushed dangerously near the very top, against a blazing white sun and shimmering hot air, extreme heat, no numbers or digits visible, {NEG}, {X}"),
    (HEAT, "broll_3.jpg", f"A cinematic wide shot of a parched cracked-earth field with withered crops under an orange smoke-hazed sky and a distant wildfire glow on the horizon, climate-change drought mood, {NEG}, {X}"),
    # TREGZI FDA (all scenes)
    (TREG, "hero.jpg", f"A cinematic wide shot of an advanced modern biotech cell-therapy laboratory, glowing vials and cell-culture bioreactors, cool clinical blue and teal light, cutting-edge immunotherapy mood, spotless and futuristic, no readable screens, {NEG}, {X}"),
    (TREG, "broll_1.jpg", f"A cinematic shot of scientists in protective gowns, gloves and masks handling a cell-culture bag beside a bioreactor in a sterile lab, focused professional mood, cool light, no readable screen text, {NEG}, {X}"),
    (TREG, "broll_2.jpg", f"An abstract cinematic microscopic visualization of glowing blue and gold immune T-cells flowing through the bloodstream, protective and regenerative concept, deep clinical blue tones, no labels, {NEG}, {X}"),
    (TREG, "broll_3.jpg", f"A hopeful cinematic shot of a recovering patient resting peacefully near a bright sunlit hospital window at dawn, warm soft optimistic light, calm and healing mood, no distress, no readable text, {NEG}, {X}"),
]


def submit_retry(p, tries=5):
    last = None
    for i in range(tries):
        try: return submit(p)
        except Exception as e: last = e; time.sleep(3*(i+1))
    raise last


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname}"); continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} {tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 18*60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try: r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception: still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url: still.append(j); continue
                try: download(url, j["out"]); j["ok"] = True; print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                except Exception as e: print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr); still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr)
            else: still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} ==", flush=True)
    for j in jobs:
        if not j["ok"]: print(f"  MISSING {j['slug']}/{j['file']}")
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
