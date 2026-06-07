#!/usr/bin/env python3
"""Generate the non-face AI scenes for the 2026-06-07 slate via Nano Banana Pro (9:16, 2K).
Real faces (Andreeva, Chwalinska, al-Zaidi) are fetched separately. Every scene prompt
MATCHES its target beat's text. Bright lighting to clear engine luminance floors. Strong
no-text/no-UI negatives (KIE screenshot guard). Tasteful: no bodies, no gore."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-07"
GUARD = "absolutely no text, no captions, no Instagram or app UI, no phone screen, no watermark, no logos, photorealistic editorial photograph"

JOBS = [
    # 1. IRAQ ZAIDI ANTI-CORRUPTION (hero = real al-Zaidi if available; broll_1/2/3 generated)
    (f"{D}-iraq-zaidi-anticorruption", "broll_1.jpg", f"A formal Iraqi government press conference podium with microphones and the flag of Iraq (red white black horizontal bands with green Arabic script) behind it in a bright official hall, empty lectern, sense of a major anti-corruption announcement, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-zaidi-anticorruption", "broll_2.jpg", f"Neat stacks of seized hundred-dollar banknotes arranged on a table beside an official government seal in a bright room, anti-corruption investigation evidence, shallow depth of field, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-zaidi-anticorruption", "broll_3.jpg", f"Exterior of an official Iraqi government ministry building in Baghdad with the Iraqi flag flying on a tall pole and a guarded gate, bright clear daylight, sandstone official architecture, sense of state authority over the oil sector, wide establishing shot, {GUARD}, {NEG}"),
    # 2. IRAQ FISCAL CRISIS / DINAR PRINTING (all 4 generated)
    (f"{D}-iraq-fiscal-crisis", "hero.jpg", f"Close-up of large neat stacks and bundles of Iraqi dinar banknotes filling the frame on a dark surface under dramatic lighting, currency and monetary pressure, shallow depth of field, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-fiscal-crisis", "broll_1.jpg", f"An industrial currency printing press producing sheets of banknotes in a secure facility, rolls of paper currency and machinery, cool industrial lighting, sense of money being printed at scale, wide cinematic shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-fiscal-crisis", "broll_2.jpg", f"Aerial view of a massive crude oil supertanker idling at a Gulf export terminal at dusk with cranes and pipelines, calm steel-blue Persian Gulf water, halted oil exports, strategic chokepoint tension, cinematic wide shot, {GUARD}, {NEG}"),
    (f"{D}-iraq-fiscal-crisis", "broll_3.jpg", f"A busy Iraqi street market in Baghdad with vendors and produce stalls under bright daylight, ordinary people shopping in the distance, sense of household cost of living and inflation, wide cinematic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    # 3. GAZA CEASEFIRE SIX MONTHS (all 4 generated; tasteful, no bodies)
    (f"{D}-gaza-ceasefire-sixmonths", "hero.jpg", f"A wide cinematic skyline view of a dense Middle Eastern coastal city with damaged grey concrete buildings and a thin column of distant smoke rising under a hazy pale sky, fragile ceasefire atmosphere, no people, no bodies, restrained and tasteful, {GUARD}, {NEG}"),
    (f"{D}-gaza-ceasefire-sixmonths", "broll_1.jpg", f"A quiet damaged urban street in a Middle Eastern city with rubble cleared to the sides and shuttered shops, faint dust in the air under daylight, aftermath of conflict during a fragile truce, wide cinematic shot, no people, no bodies, restrained, {GUARD}, {NEG}"),
    (f"{D}-gaza-ceasefire-sixmonths", "broll_2.jpg", f"White humanitarian aid trucks lined up at a border crossing checkpoint under bright daylight, stacked relief supplies and pallets, sense of constrained humanitarian access, wide establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-gaza-ceasefire-sixmonths", "broll_3.jpg", f"A formal international diplomacy setting, a long polished table with neutral national flags and empty chairs in a bright conference room, stalled peace negotiations, soft window light, no people, {GUARD}, {NEG}"),
    # 4. FRENCH OPEN ANDREEVA (hero = real Andreeva; broll_2 = real Chwalinska; broll_1/3 generated)
    (f"{D}-french-open-andreeva", "broll_1.jpg", f"The famous orange-red clay tennis court of Roland-Garros grand Paris stadium under bright daylight, crisp white lines, empty tiered stands rising around it, iconic French Open atmosphere, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-french-open-andreeva", "broll_3.jpg", f"A gleaming silver tennis champion trophy cup standing on a plinth at the edge of an orange clay court in bright golden sunlight, ornate engraved metal, shallow depth of field, prestige and triumph, no people, {GUARD}, {NEG}"),
    # 5. ROMAN SPACE TELESCOPE (all 4 generated)
    (f"{D}-roman-telescope", "hero.jpg", f"A large modern space telescope spacecraft with a golden cylindrical body and deployed solar panels floating in deep space above the curved blue limb of Earth, brilliant starfield behind it, dramatic cinematic NASA-style render, {GUARD}, {NEG}"),
    (f"{D}-roman-telescope", "broll_1.jpg", f"Engineers in white clean-room bunny suits preparing a large gold-foil-wrapped space telescope inside a brightly lit spacecraft assembly clean room, high-tech aerospace facility, wide cinematic shot, {GUARD}, {NEG}"),
    (f"{D}-roman-telescope", "broll_2.jpg", f"A vast cosmic field of countless distant stars and several colorful exoplanets and galaxies scattered across deep space, rich blues purples and gold, awe-inspiring wide-field survey of the universe, cinematic astronomical render, {GUARD}, {NEG}"),
    (f"{D}-roman-telescope", "broll_3.jpg", f"A breathtaking spiral galaxy and the glowing cosmic web of distant galaxies stretching across deep space, dark energy and dark matter survey, deep field astronomy, brilliant and colorful, cinematic render, {GUARD}, {NEG}"),
    # 6. DRC EBOLA EMERGENCY (all 4 generated; tasteful, clinical, hopeful)
    (f"{D}-drc-ebola-emergency", "hero.jpg", f"Health workers in full white protective personal protective equipment and face shields walking toward a bright clean field treatment tent at a medical response site in central Africa, blue sky, organized public health emergency response, wide cinematic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-drc-ebola-emergency", "broll_1.jpg", f"A row of white medical isolation tents at an Ebola treatment center under bright daylight with health staff in protective gear in the distance, organized outbreak response in central Africa, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-drc-ebola-emergency", "broll_2.jpg", f"A bright modern virology research laboratory, scientists in protective gear examining vials and samples under clinical light, vaccine and treatment research, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-drc-ebola-emergency", "broll_3.jpg", f"A community health screening station in an African town with a hand-washing and temperature-check point and health workers in protective gear at a distance under bright daylight, hopeful containment effort, wide establishing shot, no recognizable faces, {GUARD}, {NEG}"),
]


def main():
    only = set(sys.argv[1:])
    sel = [(s, f, p) for (s, f, p) in JOBS if not only or f"{s}/{f}" in only or s in only]
    print(f"== Submitting {len(sel)} scene jobs ==", flush=True)
    jobs = []
    for slug, fname, prompt in sel:
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
    deadline = time.time() + 18 * 60
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
    print(f"\n== Done {ok}/{len(sel)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(sel) else 1


if __name__ == "__main__":
    sys.exit(main())
