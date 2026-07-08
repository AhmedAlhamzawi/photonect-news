#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-08 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces). Reuses gen_2026_05_28 infra.
Each prompt is matched to THAT beat's Arabic text.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-08"
JOBS = [
    # 1 · dinar-dollar-gap
    (f"{D}-dinar-dollar-gap", "hero.jpg", f"Close-up of hands counting a thick stack of Iraqi dinar banknotes beside US dollar bills on a worn wooden money-changer counter in a Baghdad currency exchange, warm tungsten light, tense economic mood, shallow depth of field, {NEG}"),
    (f"{D}-dinar-dollar-gap", "broll_1.jpg", f"A bustling Iraqi currency-exchange shop, a money changer behind a glass counter with dense stacks of dinar and US dollars, customers waiting in line, busy informal market atmosphere, documentary photojournalism, {NEG}"),
    (f"{D}-dinar-dollar-gap", "broll_2.jpg", f"An Iraqi shopper at a crowded Baghdad food market holding a shopping bag and counting dinar banknotes in front of stalls of imported cooking-oil bottles and canned goods, worried expression, natural daylight, {NEG}"),
    (f"{D}-dinar-dollar-gap", "broll_3.jpg", f"A neat stack of Iraqi dinar banknotes next to a single US hundred-dollar bill and a financial calculator on a dark desk, clean editorial still life, dramatic side light, {NEG}"),
    # 2 · iran-oil-snapback-iraq
    (f"{D}-iran-oil-snapback-iraq", "hero.jpg", f"A massive crude-oil supertanker riding low and heavy in calm Gulf water at dawn, golden light on a steel-blue sea, distant hazy coastline, strategic tension, aerial wide cinematic shot, {NEG}"),
    (f"{D}-iran-oil-snapback-iraq", "broll_1.jpg", f"Rows of giant white oil storage tanks and loading jetties at a Gulf oil export terminal at sunrise, pipelines and a moored tanker, immense industrial scale, wide aerial shot, {NEG}"),
    (f"{D}-iran-oil-snapback-iraq", "broll_2.jpg", f"A long queue of Iraqi public-sector workers waiting outside a government pay office in Baghdad, folders and documents in hand, anxious faces, overcast documentary daylight, {NEG}"),
    (f"{D}-iran-oil-snapback-iraq", "broll_3.jpg", f"A formal United Nations Security Council style chamber with a large circular table ringed by national flags, empty leather chairs, dramatic overhead lighting, no identifiable people, {NEG}"),
    # 3 · iraq-crackdown-factions
    (f"{D}-iraq-crackdown-factions", "hero.jpg", f"Elite Iraqi counter-terrorism forces in black tactical gear conducting a pre-dawn raid in Baghdad's fortified Green Zone, vehicle headlights and flashlight beams cutting through darkness, backs and helmets only no faces, tense cinematic documentary, {NEG}"),
    (f"{D}-iraq-crackdown-factions", "broll_1.jpg", f"Seized assets displayed as evidence in a guarded compound at night — stacks of banded cash, gold jewellery on a table and a row of confiscated luxury cars behind, anti-corruption seizure, dramatic documentary, {NEG}"),
    (f"{D}-iraq-crackdown-factions", "broll_2.jpg", f"A tense closed-door meeting of stern political figures around a long polished table in a dim ornate Baghdad government hall, empty chairs and heavy shadows, secrecy and friction, silhouetted no identifiable faces, {NEG}"),
    (f"{D}-iraq-crackdown-factions", "broll_3.jpg", f"The national flag of Iraq (red, white and black horizontal bands with green Arabic takbir script) flying on a tall pole against a dramatic dawn sky over the Baghdad skyline, hopeful yet tense, low heroic angle, {NEG}"),
    # 4 · iraq-gas-power-collapse
    (f"{D}-iraq-gas-power-collapse", "hero.jpg", f"An Iraqi family in a dim sweltering Baghdad apartment during a summer power blackout, lit only by a battery lantern and glowing phone screens, a motionless ceiling fan, oppressive heat, intimate documentary night, {NEG}"),
    (f"{D}-iraq-gas-power-collapse", "broll_1.jpg", f"A gas pipeline and processing facility in an arid landscape at dusk with a single dim weak flare, mostly dark and dormant, sense of collapsed supply, wide cinematic shot, {NEG}"),
    (f"{D}-iraq-gas-power-collapse", "broll_2.jpg", f"A high-voltage electrical substation and transmission towers under a blazing white summer sun with visible heat haze rising, arid Iraqi landscape, strained overloaded grid, wide shot, {NEG}"),
    (f"{D}-iraq-gas-power-collapse", "broll_3.jpg", f"High-voltage transmission towers and power lines marching across a mountainous border landscape at golden hour, cross-border electricity supply toward Iraq, wide cinematic shot, {NEG}"),
    # 5 · iraq-heritage-economy
    (f"{D}-iraq-heritage-economy", "hero.jpg", f"The reconstructed blue-tiled Ishtar Gate and ancient ruins of Babylon under a golden late-afternoon sun, majestic Mesopotamian archaeology, empty of visitors, warm cinematic wide shot, {NEG}"),
    (f"{D}-iraq-heritage-economy", "broll_1.jpg", f"The vast ancient Great Ziggurat of Ur rising from the desert under a clear sky, monumental stepped Mesopotamian architecture, almost no visitors, wide aerial shot, {NEG}"),
    (f"{D}-iraq-heritage-economy", "broll_2.jpg", f"A large crowd of pilgrims and visitors walking through a grand golden-domed Iraqi shrine courtyard, bustling religious tourism, warm afternoon light, documentary wide shot, {NEG}"),
    (f"{D}-iraq-heritage-economy", "broll_3.jpg", f"Conservation workers with scaffolding restoring ancient carved stone columns at a Mesopotamian archaeological site, careful heritage restoration work, bright daylight documentary, {NEG}"),
]


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.5)
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 16 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    j["done"] = True; continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        if pending:
            print(f"    ... {len(pending)} generating", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done {ok}/{len(JOBS)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
