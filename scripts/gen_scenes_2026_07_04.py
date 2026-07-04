#!/usr/bin/env python3
"""Cinematic KIE nano-banana-pro 9:16 2K scenes for the 2026-07-04 slate.
All 5 stories are scene-based (no single named person → no face slots)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage, no digits, no charts with numbers")

PWR = "2026-07-04-baghdad-power-blackout"
AI  = "2026-07-04-gulf-ai-sovereign-funds"
SAL = "2026-07-04-iraq-salary-payment-risk"
OPC = "2026-07-04-opec-august-output-hike"
TIG = "2026-07-04-tigris-lost-city"

JOBS = [
    # 1) BAGHDAD POWER / heat — grid under summer strain
    (PWR, "hero.jpg",   f"A cinematic wide aerial of a sprawling Baghdad residential neighbourhood at dusk in a sweltering summer heatwave, most buildings dark in a blackout while a few rooftops glow from private diesel generators, tangled wires overhead, heavy orange haze, thermal shimmer, a sense of a city without power in extreme heat, {NEG}, {X}"),
    (PWR, "broll_1.jpg",f"A cinematic wide shot of a huge Iraqi gas-fired power station at dusk, tall cooling stacks and turbine halls, several units idle and unlit, a lone flare in the distance, dramatic industrial silhouette against a burnt orange sky, sense of fuel shortage, {NEG}, {X}"),
    (PWR, "broll_2.jpg",f"A gritty documentary street shot of a dense Baghdad market alley at night lit only by warm bulbs wired to rows of small private neighbourhood diesel generators on the pavement, thick cables snaking along walls, exhaust haze, resigned everyday life during power cuts, {NEG}, {X}"),
    (PWR, "broll_3.jpg",f"A cinematic close shot of an ordinary Iraqi family apartment interior during a summer blackout, a single battery lamp glowing, a plastic hand fan, sweat on brows, sunset light through a window, quiet endurance in extreme heat, faces not clearly identifiable, {NEG}, {X}"),
    # 2) GULF AI SOVEREIGN FUNDS — money & power / tech future
    (AI, "hero.jpg",    f"A breathtaking cinematic wide shot inside a vast futuristic Gulf hyperscale AI data center, endless symmetrical rows of tall black server racks glowing cool blue and cyan, polished reflective floor, dramatic vanishing-point perspective, immense sovereign-scale investment, {NEG}, {X}"),
    (AI, "broll_1.jpg", f"A cinematic dusk aerial of the Abu Dhabi skyline with gleaming modern towers and the Gulf waterfront, warm golden haze over a wealthy futuristic capital, sense of sovereign capital and ambition, wide establishing shot, {NEG}, {X}"),
    (AI, "broll_2.jpg", f"An extreme cinematic macro close-up of a cutting-edge AI accelerator chip on a dense green circuit board with gold connectors and glowing blue traces, shallow depth of field, frontier technology, {NEG}, {X}"),
    (AI, "broll_3.jpg", f"A cinematic wide shot of a sleek modern Gulf financial district at blue hour, mirror-glass skyscrapers reflecting city lights, a quiet sense of enormous wealth being deployed, low heroic angle, {NEG}, {X}"),
    # 3) IRAQ SALARY / payroll risk — wallet
    (SAL, "hero.jpg",   f"A cinematic close still-life of neat thick stacks of Iraqi dinar banknotes on a worn wooden desk beside an empty government pay envelope, hard directional window light casting long shadows, a tense mood of money running short, {NEG}, {X}"),
    (SAL, "broll_1.jpg",f"A documentary wide shot of a long queue of ordinary Iraqi people waiting outside a state bank branch under harsh daylight, anxious body language, plain modern concrete facade, sense of salary day uncertainty, faces not clearly identifiable, {NEG}, {X}"),
    (SAL, "broll_2.jpg",f"A cinematic shot of an empty bank teller counter with a closed metal shutter half down and a lone security guard, cool fluorescent light, a sense of depleted liquidity and delayed payments, {NEG}, {X}"),
    (SAL, "broll_3.jpg",f"A cinematic wide interior of a grand Iraqi government finance ministry corridor, polished floors, an official walking away down a long empty hall, weight of a fiscal decision, dramatic overhead light, no identifiable face, {NEG}, {X}"),
    # 4) OPEC+ AUGUST OUTPUT — markets / oil
    (OPC, "hero.jpg",   f"A cinematic wide aerial of a vast southern Iraq oilfield at golden dusk, rows of pumpjacks and gas flares, sprawling pipelines and storage tanks, heat haze, immense scale of crude production being raised, {NEG}, {X}"),
    (OPC, "broll_1.jpg",f"A grand OPEC-style oil ministers summit hall, a large circular polished conference table ringed with many plain unmarked national flag stands and empty leather chairs, modern wood-panelled international conference room, dramatic chandelier light, no identifiable people, {NEG}, {X}"),
    (OPC, "broll_2.jpg",f"A cinematic wide aerial of a giant crude oil supertanker riding low in the water crossing the calm blue Strait of Hormuz at dawn, golden light on steel-blue sea, distant hazy coastline, recovering shipping traffic, {NEG}, {X}"),
    (OPC, "broll_3.jpg",f"A moody cinematic shot of a massive oil refinery and petrochemical complex at night, glowing gas flares, webs of illuminated pipes and distillation towers, rising steam, dramatic industrial nightscape, wide aerial, {NEG}, {X}"),
    # 5) TIGRIS LOST CITY — heritage / pride (feature)
    (TIG, "hero.jpg",   f"A breathtaking cinematic aerial at golden hour of vast ancient mud-brick ruins of a lost Hellenistic city on a flat southern Iraqi desert plain beside a shifted old river channel, faint grid of streets and a long low city wall visible in the sand, archaeological grandeur, {NEG}, {X}"),
    (TIG, "broll_1.jpg",f"A cinematic ground shot of eroded ancient mud-brick city walls rising several metres from desert sand under a dramatic low sun, long shadows, weathered ramparts of a 2000-year-old metropolis, {NEG}, {X}"),
    (TIG, "broll_2.jpg",f"A cinematic overhead drone shot revealing the buried grid layout of an ancient planned city in the desert, faint lines of wide streets, housing blocks, temple compounds and old harbour basins traced in the sand, archaeological survey mood, {NEG}, {X}"),
    (TIG, "broll_3.jpg",f"An evocative cinematic shot of an ancient river harbour basin now dry and silted in the desert, cracked earth where water once linked Mesopotamia to the Gulf, warm dusk light, a sense of a great trade hub lost to a moved river, {NEG}, {X}"),
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
    deadline = time.time() + 20*60
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
