#!/usr/bin/env python3
"""Cinematic KIE nano-banana-pro 9:16 2K scenes for the 2026-07-06 slate.
Throughline: Iraq money & power — anti-graft reckoning, oil-price slide, cyber-law,
Arbaeen non-oil economy, and the KRG salary/oil feud. All scene-based (no named-person
portraits → no Commons faces). One still per beat, matched to that beat's text."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

# Hard anti-UI / anti-text guard + upright-portrait guard (learned gotchas).
X = ("vertical portrait 9:16, upright orientation, level horizon, "
     "absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage, no digits, no charts with numbers")

GRAFT = "2026-07-06-baghdad-graft-2trillion"
CRUDE = "2026-07-06-crude-price-slide"
CYBER = "2026-07-06-iraq-cyber-law"
ARBA  = "2026-07-06-karbala-arbaeen-economy"
KRG   = "2026-07-06-kurdistan-salary-oil"

JOBS = [
    # 1) GRAFT — $2tn anti-corruption reckoning
    (GRAFT, "hero.jpg",   f"A cinematic wide interior of a grand austere Iraqi high court chamber at dramatic overhead light, a tall national emblem on the wall, an empty defendant's dock, polished dark wood, a heavy sense of a national corruption reckoning, no identifiable people, {NEG}, {X}"),
    (GRAFT, "broll_1.jpg",f"A tense pre-dawn anti-corruption raid scene: a convoy of unmarked official vehicles with faint blue lights parked outside the tall gates of a lavish villa, shadowy figures in the distance, cold blue night, no identifiable faces, {NEG}, {X}"),
    (GRAFT, "broll_2.jpg",f"An opulent marble mansion interior dripping with gold trim, a crystal chandelier and luxury furniture, cinematic moody light casting long shadows, a quiet unsettling sense of hidden ill-gotten wealth, no people, {NEG}, {X}"),
    (GRAFT, "broll_3.jpg",f"A formal empty courtroom prepared for a televised public trial: a wooden judge's bench and gavel, broadcast camera silhouettes and lighting rigs set up facing the dock, a national flag, solemn accountability mood, no identifiable people, {NEG}, {X}"),
    # 2) CRUDE PRICE SLIDE — oversupply squeezes Iraq's oil budget
    (CRUDE, "hero.jpg",   f"A cinematic wide aerial at dusk of a vast crude-oil export terminal with several supertankers berthed loading, endless white storage tanks, a brooding oversupplied heavy mood, immense petroleum infrastructure, {NEG}, {X}"),
    (CRUDE, "broll_1.jpg",f"A cinematic row of desert oil pumpjacks working hard against a burnt-orange sunset with a distant gas flare, heat haze, a sense of surging abundant production, {NEG}, {X}"),
    (CRUDE, "broll_2.jpg",f"A high cinematic aerial of a convoy of several fully loaded crude oil supertankers riding low in calm blue Gulf water, a glut of oil at sea, golden light, immense scale, {NEG}, {X}"),
    (CRUDE, "broll_3.jpg",f"A moody cinematic dusk aerial of the Baghdad skyline along the Tigris with the Iraqi tricolour flag flying on a tall pole, warm hazy light, a subtle heavy sense of fiscal pressure over an oil-dependent capital, {NEG}, {X}"),
    # 3) CYBER LAW — cybercrime bill / online speech
    (CYBER, "hero.jpg",   f"An extreme cinematic close-up of a pair of hands holding a glowing blank smartphone in a darkened room, a faint suggestion of a chain-link shadow across the screen light, a tense surveillance mood, blank screen no text, {NEG}, {X}"),
    (CYBER, "broll_1.jpg",f"A cinematic interior of an Iraqi parliament chamber, curved rows of empty seats, a national flag at the front, dramatic formal legislative-session light, no identifiable people, {NEG}, {X}"),
    (CYBER, "broll_2.jpg",f"A moody cinematic shot of a dim prison corridor with steel bars and hard cold light, a single glowing smartphone left on a bare table in the foreground, a heavy sense of harsh penalty, no people, {NEG}, {X}"),
    (CYBER, "broll_3.jpg",f"A cinematic low-key shot of a young person's silhouette hunched typing on a glowing laptop in a dark room, a subtle unsettling sense of being watched, muted blue tones, face not identifiable, {NEG}, {X}"),
    # 4) ARBAEEN — world's largest gathering / non-oil economy
    (ARBA,  "hero.jpg",   f"A breathtaking cinematic aerial at golden dusk of an immense sea of pilgrims filling the wide streets around a magnificent golden-domed shrine in Karbala Iraq, endless human multitude, warm reverent light, no readable signage, {NEG}, {X}"),
    (ARBA,  "broll_1.jpg",f"A cinematic wide shot of an endless column of pilgrims walking a desert highway between Najaf and Karbala under a hazy sun, black mourning flags, immense scale of the world's largest annual march, faces not identifiable, {NEG}, {X}"),
    (ARBA,  "broll_2.jpg",f"A vibrant documentary shot of bustling roadside hospitality tents serving pilgrims, huge steaming cauldrons of food and rows of served dishes, generous communal service, warm colour, no readable text, faces not identifiable, {NEG}, {X}"),
    (ARBA,  "broll_3.jpg",f"A warm cinematic night shot of a diverse crowd of pilgrims from many nations gathered before the brilliantly illuminated golden Karbala shrine, glowing lights, a tender sense of unity and pride, faces not clearly identifiable, {NEG}, {X}"),
    # 5) KRG SALARY / OIL — Erbil-Baghdad feud
    (KRG,   "hero.jpg",   f"A cinematic dusk aerial of the Erbil Kurdistan city skyline with the ancient citadel silhouette and distant oil infrastructure on the horizon, a tense mood balancing oil wealth against livelihoods, warm hazy light, {NEG}, {X}"),
    (KRG,   "broll_1.jpg",f"A gritty documentary shot of a long anxious queue of ordinary public-sector workers waiting outside a bank under flat grey light, worried body language, waiting for delayed wages, faces not clearly identifiable, {NEG}, {X}"),
    (KRG,   "broll_2.jpg",f"A cinematic wide shot of a Kurdistan oil field at dusk, pumpjacks valves and a snaking pipeline, warm work-lights, the lever of contested oil revenue, no people, {NEG}, {X}"),
    (KRG,   "broll_3.jpg",f"A cold cinematic shot of an empty formal negotiation hall with a long polished table and two facing sets of plain unmarked flag stands, dramatic overhead light, a sense of deadlocked talks, no people, {NEG}, {X}"),
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
    deadline = time.time() + 22*60
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
    return 0 if ok == len(JOBS) else 1

if __name__ == "__main__":
    sys.exit(main())
