#!/usr/bin/env python3
"""Generate the non-face AI scenes for the 2026-06-08 slate via Nano Banana Pro (9:16, 2K).
Real faces (Zverev, Cobolli, al-Sharaa, El Mazned) are fetched separately as Commons portraits.
Every scene prompt MATCHES its target beat's text. Bright/legible lighting to clear engine
luminance floors. Strong no-text/no-UI negatives (KIE screenshot guard)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-08"
GUARD = "absolutely no text, no captions, no Instagram or app UI, no phone screen, no watermark, no logos, photorealistic editorial photograph"

JOBS = [
    # 1. IRAQ WATER CRISIS — all 4 generated (no single named face)
    (f"{D}-iraq-water-crisis", "hero.jpg", f"A vast dried-up riverbed of the Euphrates in Iraq, deeply cracked parched mud stretching to the horizon, a thin shrunken trickle of water in the distance, beached wooden fishing boat on the dry cracked earth, harsh blazing sun and pale washed-out sky, severe drought, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_1.jpg", f"An almost empty Iraqi reservoir behind a large concrete dam, exposed cracked lakebed and dramatic pale bathtub-ring water lines on the banks, a small remaining pool of low turquoise water far below, arid mountains, water reserves at record low, bright daylight aerial wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_2.jpg", f"A parched failing farm field in rural Iraq, withered brown crops and cracked dry soil, a few gaunt sheep and a buffalo standing on barren ground searching for water, an Iraqi farmer in a thobe looking over the ruined land under a hot hazy sky, livestock and agriculture collapse, documentary wide shot, {GUARD}, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_3.jpg", f"The Tigris river running dangerously low through Baghdad, wide exposed sand banks and stranded boats, the city skyline and a bridge in the hazy background under a blazing summer sun, low water levels threatening drinking supply, wide cinematic establishing shot, {GUARD}, {NEG}"),

    # 2. ZVEREV FRENCH OPEN — broll_1 + broll_3 generated (hero=Zverev face, broll_2=Cobolli face)
    (f"{D}-zverev-french-open", "broll_1.jpg", f"The famous orange-red clay tennis court of the grand Philippe-Chatrier stadium at Roland Garros in Paris under bright daylight, crisp white lines, packed tiered stands rising around it, iconic French Open atmosphere, dramatic wide cinematic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-zverev-french-open", "broll_3.jpg", f"A gleaming silver Coupe des Mousquetaires tennis champion trophy standing on a plinth at the edge of an orange clay court in bright golden sunlight, ornate engraved metal, falling confetti, shallow depth of field, triumph and prestige, no people, {GUARD}, {NEG}"),

    # 3. SYRIA TRANSITION YEAR — broll_1/2/3 generated (hero=al-Sharaa face)
    (f"{D}-syria-transition-year", "broll_1.jpg", f"Damascus Syria skyline at golden hour one year after the fall of the old regime, a mix of modern buildings and historic minarets, scaffolding and reconstruction cranes rising over a recovering city, hopeful but fragile atmosphere, wide aerial cinematic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-syria-transition-year", "broll_2.jpg", f"A busy reopened commercial street and bank in central Damascus, shoppers at a modern storefront and an ATM, a sense of returning international commerce and economic reopening, bright daylight, documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-syria-transition-year", "broll_3.jpg", f"Tense Syrian security forces at a checkpoint on the edge of Aleppo, an armored vehicle and a fluttering Syrian flag, alert posture under an overcast sky, fragile fragmented control and lingering internal conflict, documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),

    # 4. ENDOMETRIOSIS BLOOD TEST — all 4 generated (no named face)
    (f"{D}-endometriosis-blood-test", "hero.jpg", f"A bright clean modern medical research laboratory, a gloved scientist's hands holding a small vial of blood beside an advanced analyzer instrument, soft cool daylight, hopeful clinical breakthrough atmosphere, close cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-endometriosis-blood-test", "broll_1.jpg", f"Extreme macro close-up of a single small medical test tube of deep red blood held in a gloved hand over a laboratory bench with pipettes and sample trays, soft bright studio lighting, shallow depth of field, non-invasive diagnostic sample, {GUARD}, {NEG}"),
    (f"{D}-endometriosis-blood-test", "broll_2.jpg", f"One single uncropped photograph, a reassuring modern gynecology clinic consultation room, a woman doctor in a white coat seated speaking gently with a female patient across a wooden desk, warm soft daylight from a window, dignity and relief, single continuous wide editorial shot, faces turned away, no recognizable faces, not a collage, not a grid, not split panels, one frame only, {GUARD}, {NEG}"),
    (f"{D}-endometriosis-blood-test", "broll_3.jpg", f"A scientist viewing glowing single-cell genomic data and machine-learning charts on a large computer screen in a dim modern lab, abstract bright data visualization of cells and biomarkers, cool blue light, cutting-edge multi-omic diagnostics, no readable text, {GUARD}, {NEG}"),

    # 5. NEOM / THE LINE RECKONING — all 4 generated (no named face)
    (f"{D}-neom-line-reckoning", "hero.jpg", f"A vast halted megaproject construction site in the Saudi Arabian desert, a colossal long linear excavation trench stretching to the horizon with idle cranes and stalled earthworks, scaling-back of an ambitious futuristic city, harsh bright desert sun, dramatic wide aerial establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-neom-line-reckoning", "broll_1.jpg", f"A futuristic mirrored linear skyscraper city concept rising from the desert under a bright sky, sleek reflective walls stretching into the distance, ambitious but partly unfinished, cinematic wide establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-neom-line-reckoning", "broll_2.jpg", f"Interior of a vast modern AI data center with endless rows of tall black server racks glowing with cool blue and cyan indicator lights, polished reflective floor, dramatic vanishing-point perspective, a pivot toward artificial intelligence infrastructure, wide cinematic shot, no people, {GUARD}, {NEG}"),
    (f"{D}-neom-line-reckoning", "broll_3.jpg", f"The modern Riyadh skyline of Saudi Arabia at bright midday, the King Abdullah Financial District cluster of distinctive towers, clear sky, a sovereign wealth fund refocusing on near-term returns, wide aerial establishing shot, no recognizable faces, {GUARD}, {NEG}"),

    # 6. UNESCO ARAB CULTURE — broll_1/2/3 generated (hero=El Mazned face if available, else this set covers it)
    (f"{D}-unesco-arab-culture", "broll_1.jpg", f"A vibrant North African Arab music heritage scene, traditional oud and qanun string instruments resting on an ornate Moroccan rug beside a lit lantern, warm golden light, rich cultural craftsmanship, intimate close cinematic still, no people, {GUARD}, {NEG}"),
    (f"{D}-unesco-arab-culture", "broll_2.jpg", f"The grand UNESCO headquarters building in Paris with international flags flying in front under a clear sky, prestigious cultural institution, bright daylight, wide architectural establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-unesco-arab-culture", "broll_3.jpg", f"A lively Arab cultural festival at dusk in a historic Moroccan medina square, a crowd gathered around traditional musicians performing under warm string lights and ancient sandstone architecture, celebration of Arab arts and heritage, wide cinematic documentary shot, no recognizable faces, {GUARD}, {NEG}"),
    # El Mazned face may not be on Commons; generate a dignified portrait-style fallback hero too.
    (f"{D}-unesco-arab-culture", "hero_fallback.jpg", f"A distinguished middle-aged North African Arab cultural figure in elegant attire standing in a beautiful traditional Moroccan riad courtyard with intricate tilework and an oud instrument nearby, warm golden light, dignified portrait of a music and heritage curator, cinematic medium shot, generic non-celebrity face, {GUARD}, {NEG}"),
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
