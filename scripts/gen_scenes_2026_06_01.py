#!/usr/bin/env python3
"""Generate the 22 non-face AI scenes for 2026-06-01 via Nano Banana Pro (9:16, 2K).
Faces (Lagarde -> ecb broll_1, al-Kaabi -> qatar broll_1) are real photos fetched
separately. Every scene prompt MATCHES its target beat's text. Bright lighting to
clear engine luminance floors (hero>=62, broll>=45).
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-01"
# (slug, filename, prompt)
JOBS = [
    # 1. IRAQ OIL & GAS LAW (all 4 generated)
    (f"{D}-iraq-oil-gas-law", "hero.jpg", f"Interior of a modern Iraqi parliamentary chamber, curved rows of wooden seats, the flag of Iraq (red white black bands with green Arabic script) on the front wall, bright daylight pouring through tall windows, formal Arab government assembly hall, wide cinematic establishing shot, {NEG}"),
    (f"{D}-iraq-oil-gas-law", "broll_1.jpg", f"Exterior of a grand Iraqi federal government building in Baghdad with the Iraqi flag flying on a tall pole, bright clear morning sunlight, official sandstone architecture, palm trees, wide establishing shot, {NEG}"),
    (f"{D}-iraq-oil-gas-law", "broll_2.jpg", f"Aerial wide shot of a large crude oil pipeline crossing arid terrain toward a Mediterranean export terminal with rows of white storage tanks, bright daylight, Kirkuk-Ceyhan oil route, {NEG}"),
    (f"{D}-iraq-oil-gas-law", "broll_3.jpg", f"An Iraqi oil field with several pumpjacks and a distant gas flare under a bright blue sky, oil-rich desert, heat shimmer, wide cinematic establishing shot, {NEG}"),
    # 2. RED SEA REOPENS (all 4 generated)
    (f"{D}-redsea-reopens", "hero.jpg", f"A massive Maersk-style container ship loaded with stacked colorful shipping containers crossing the calm bright blue Red Sea, clear midday sun, aerial wide cinematic establishing shot, {NEG}"),
    (f"{D}-redsea-reopens", "broll_1.jpg", f"A large container cargo ship sailing through the narrow Bab el-Mandeb strait, bright midday sun on turquoise water, rocky coastline on both sides, aerial wide shot, {NEG}"),
    (f"{D}-redsea-reopens", "broll_2.jpg", f"Aerial view of the Suez Canal with a long container ship transiting between sandy desert banks, bright daylight, global trade artery, wide shot, {NEG}"),
    (f"{D}-redsea-reopens", "broll_3.jpg", f"A container ship sailing on the open blue ocean off the rugged coast of the Cape of Good Hope southern Africa, bright daylight, long alternative shipping route, wide cinematic, {NEG}"),
    # 3. AI PRICE WAR (all 4 generated)
    (f"{D}-ai-price-war", "hero.jpg", f"Establishing shot inside a vast modern AI data center, endless symmetrical rows of tall server racks glowing with cool blue and cyan lights, bright clean high-tech facility, polished reflective floor, dramatic vanishing-point perspective, {NEG}"),
    (f"{D}-ai-price-war", "broll_1.jpg", f"Extreme close-up of advanced AI GPU server hardware, dense green circuit boards and gold connectors, glowing blue and amber status LEDs, bright clean studio lighting, shallow depth of field, {NEG}"),
    (f"{D}-ai-price-war", "broll_2.jpg", f"A young Arab entrepreneur in a bright modern co-working office in the Gulf using a laptop showing an abstract glowing blue AI interface, large windows with a sunny city skyline behind, optimistic bright lighting, {NEG}"),
    (f"{D}-ai-price-war", "broll_3.jpg", f"An abstract three-dimensional visualization of a glowing neural network with flowing blue and gold data streams on a bright clean background, futuristic artificial intelligence concept, {NEG}"),
    # 4. QATAR LNG EXPANSION (broll_1 = al-Kaabi face)
    (f"{D}-qatar-lng-expansion", "hero.jpg", f"A massive LNG liquefied natural gas plant on the Qatar coast in bright daylight, huge white spherical storage tanks, towering silver distillation columns, networks of pipelines, industrial mega-facility, wide aerial establishing shot, {NEG}"),
    (f"{D}-qatar-lng-expansion", "broll_2.jpg", f"A giant LNG carrier tanker with white spherical gas tanks docked at a Qatari export terminal under a bright blue sky, loading arms and pipelines, calm gulf water, wide aerial shot, {NEG}"),
    (f"{D}-qatar-lng-expansion", "broll_3.jpg", f"An offshore natural gas platform in the bright blue Persian Gulf with a flare stack and supply vessels alongside, North Field gas infrastructure, wide cinematic daylight shot, {NEG}"),
    # 5. ECB RATE HIKE (broll_1 = Lagarde face)
    (f"{D}-ecb-rate-hike", "hero.jpg", f"The European Central Bank headquarters twin-tower skyscraper in Frankfurt Germany, the giant blue and yellow euro currency sign sculpture in the foreground, bright clear daylight, modern glass tower, wide establishing shot, {NEG}"),
    (f"{D}-ecb-rate-hike", "broll_2.jpg", f"Aerial wide shot of a giant crude oil supertanker crossing the Strait of Hormuz in bright daylight, steel-blue gulf water, hazy distant coastline, strategic oil chokepoint, {NEG}"),
    (f"{D}-ecb-rate-hike", "broll_3.jpg", f"A bright modern financial trading floor with large glowing wall screens showing rising line charts and candlestick graphs, blurred traders in the foreground, daylight, tense market mood, {NEG}"),
    # 6. WHITE HYDROGEN (all 4 generated)
    (f"{D}-white-hydrogen", "hero.jpg", f"A vast rugged ancient rock landscape of the Canadian Shield in northern Ontario under a bright blue sky, exposed grey billion-year-old bedrock, sparse boreal forest and a lake, wide aerial establishing shot, bright daylight, {NEG}"),
    (f"{D}-white-hydrogen", "broll_1.jpg", f"An active mining site near Timmins Ontario with drilling rigs and boreholes in grey rock, bright overcast daylight, industrial mining equipment, documentary wide shot, {NEG}"),
    (f"{D}-white-hydrogen", "broll_2.jpg", f"A clean modern hydrogen energy facility with white cylindrical storage tanks and silver pipes beside a green field under a bright blue sky, renewable clean-energy infrastructure, wide shot, {NEG}"),
    (f"{D}-white-hydrogen", "broll_3.jpg", f"An exploratory drilling rig prospecting in a remote rocky landscape under bright golden daylight, sense of an energy exploration race, wide cinematic establishing shot, {NEG}"),
]


def main():
    only = set(sys.argv[1:])  # optional "slug/file" filters
    jobs = []
    sel = [(s, f, p) for (s, f, p) in JOBS if not only or f"{s}/{f}" in only or s in only]
    print(f"== Submitting {len(sel)} scene jobs ==", flush=True)
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
    print(f"\n== Done {ok}/{len(sel)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(sel) else 1


if __name__ == "__main__":
    sys.exit(main())
