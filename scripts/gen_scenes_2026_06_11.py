#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-11 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives (KIE screenshot + triptych + brand-logo guard,
critical for the gulf-ai slug). The iraq broll_2 (PM Zaidi beat) may be overwritten by a
real Commons portrait via fetch_faces_2026_06_11.py; generated here as a neutral fallback.
Bright/clean lighting to clear engine luminance floors (deep-sea + sudan scenes intentionally
darker and may warn)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-11"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, one single uncropped photograph, single continuous wide shot, one frame only, "
         "not a collage, not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ MILITIA DISARMAMENT (broll_2 = PM Zaidi face if fetched; neutral fallback here)
    (f"{D}-iraq-militia-disarmament", "hero.jpg", f"A formal Iraqi government setting, the Iraqi national flag with green white black and red on a flagpole in front of a large sand-colored official government building in Baghdad under bright clear daylight, a sense of state authority and sovereignty, photorealistic editorial wide establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-militia-disarmament", "broll_1.jpg", f"A neutral symbolic disarmament scene, several military rifles laid down and stacked on a plain cloth-covered table inside a bare official hall, a weapons handover to the state concept, no insignia, no flags, no recognizable faces, photorealistic documentary photograph, {GUARD}, {NEG}"),
    (f"{D}-iraq-militia-disarmament", "broll_2.jpg", f"A formal Iraqi government meeting room with a long polished wooden table and empty leather chairs, a single Iraqi flag in the corner, neutral diplomatic atmosphere, soft daylight through tall windows, no people, wide cinematic interior shot, {GUARD}, {NEG}"),
    (f"{D}-iraq-militia-disarmament", "broll_3.jpg", f"Iraqi security forces vehicles and soldiers in olive-green uniforms standing in orderly formation on a wide Baghdad street under bright hazy daylight, a sense of state security and order, documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),
    # 2. SUDAN EL FASHER FAMINE (neutral, sensitive, no faces)
    (f"{D}-sudan-elfasher-famine", "hero.jpg", f"A vast arid Darfur landscape in Sudan at harsh midday, a sprawling makeshift displacement camp of simple tents and shelters stretching to the horizon under a dusty hazy sky, a somber humanitarian crisis atmosphere, wide cinematic editorial establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-sudan-elfasher-famine", "broll_1.jpg", f"Long rows of simple white humanitarian aid tents in a sun-baked desert camp in Sudan, empty plastic water containers in the dusty foreground, heat haze, a stark famine and displacement scene, documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-sudan-elfasher-famine", "broll_2.jpg", f"A neutral institutional accountability scene, an empty formal briefing room with a plain wooden podium and a few microphones, soft cool window light, a human-rights and justice atmosphere, no logos, no readable text, no people, wide cinematic interior shot, {GUARD}, {NEG}"),
    (f"{D}-sudan-elfasher-famine", "broll_3.jpg", f"A wide arid Kordofan savanna landscape in central Sudan at golden hour, scattered acacia trees and a dusty dirt road crossing open grassland, a contested resource-rich heartland, somber documentary wide shot, no people, {GUARD}, {NEG}"),
    # 3. PANCREATIC CANCER DRUG (clean, hopeful, no faces, no readable text)
    (f"{D}-pancreatic-cancer-drug", "hero.jpg", f"A bright modern oncology research laboratory, a glowing abstract illustration of a cancer cell and a DNA double helix on a large clean display screen, a hopeful medical breakthrough atmosphere, soft clean daylight, shallow depth of field, no readable text, no people, {GUARD}, {NEG}"),
    (f"{D}-pancreatic-cancer-drug", "broll_1.jpg", f"A clean bright clinical desk scene, a tablet on a stand showing a simple rising survival-curve graph with no readable numbers or text, a stethoscope and a notepad beside it, a hopeful oncology concept, soft daylight, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-pancreatic-cancer-drug", "broll_2.jpg", f"A bright scientific three-dimensional illustration of a RAS protein molecule and a small targeted drug compound glowing against a dark clean laboratory display, a molecular-biology concept, sleek polished render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-pancreatic-cancer-drug", "broll_3.jpg", f"Several modern pharmaceutical pill bottles and a blister pack of white capsules arranged on a clean bright pharmacy counter, a modern oncology treatment concept, soft studio lighting, shallow depth of field, no readable labels, no people, {GUARD}, {NEG}"),
    # 4. GULF AI YEAR (tech_ai — strict no logos/UI/readable text, no faces)
    (f"{D}-gulf-ai-year", "hero.jpg", f"A futuristic sovereign artificial-intelligence data-center concept in a Gulf desert at dusk, a sleek modern building with warm interior glow beside a distant Riyadh skyline silhouette, a softly glowing abstract network of blue-white light floating above, no screens with interfaces, no brand marks, photorealistic cinematic wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-gulf-ai-year", "broll_1.jpg", f"A modern minimalist government-style hall with sleek architecture and a large softly glowing abstract sphere of blue and white light representing artificial intelligence, a futuristic national-strategy atmosphere, no readable text, no logos, no interface, wide cinematic interior shot, no people, {GUARD}, {NEG}"),
    (f"{D}-gulf-ai-year", "broll_2.jpg", f"An abstract visualization of a large artificial-intelligence model, a luminous flowing network of glowing blue and gold nodes with a soft sound-waveform on a dark gradient background, sleek high-tech render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-gulf-ai-year", "broll_3.jpg", f"A vast modern data-center hall with long rows of glowing server racks receding into the distance, cool blue and warm amber indicator lights, a high-tech sovereign-compute atmosphere, no logos, no readable text, no people, wide cinematic shot, {GUARD}, {NEG}"),
    # 5. DEEP-SEA NEW SPECIES (vivid bioluminescence; hero/broll_2/3 intentionally dark)
    (f"{D}-deepsea-new-species", "hero.jpg", f"A mesmerizing bioluminescent deep-sea jellyfish glowing electric blue and violet in the pitch-black midwater of the deep ocean, delicate translucent tentacles trailing, dramatic darkness all around, photorealistic underwater macro scene, no people, {GUARD}, {NEG}"),
    (f"{D}-deepsea-new-species", "broll_1.jpg", f"A modern ocean research vessel on a calm deep-blue sea at golden hour, a yellow remotely operated underwater vehicle being lowered by a crane toward the water, a scientific deep-sea expedition atmosphere, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-deepsea-new-species", "broll_2.jpg", f"A luminous translucent deep-sea siphonophore, a long delicate chain-like gelatinous creature glowing softly with blue light in the dark midwater of the ocean, ethereal bioluminescence, photorealistic underwater scene, no people, {GUARD}, {NEG}"),
    (f"{D}-deepsea-new-species", "broll_3.jpg", f"A translucent gossamer deep-sea worm and a glowing comb jelly drifting in the dark blue midwater zone of the ocean, shimmering iridescent rainbow cilia, photorealistic underwater macro scene, no people, {GUARD}, {NEG}"),
    # 6. WORLD CUP 2026 KICKOFF (festive, no readable text, no recognizable faces)
    (f"{D}-worldcup-2026-kickoff", "hero.jpg", f"A massive packed football stadium at night during a World Cup opening ceremony, brilliant floodlights, colorful fireworks bursting over the green pitch, a sea of fans waving many different national flags, a euphoric celebratory atmosphere, wide cinematic establishing shot, no readable text, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-worldcup-2026-kickoff", "broll_1.jpg", f"The exterior of a huge iconic football stadium in Mexico City glowing warm at dusk, enormous crowds of excited fans streaming toward the entrances, a festive World Cup opening atmosphere, no readable signage text, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-worldcup-2026-kickoff", "broll_2.jpg", f"A bright green football pitch under powerful stadium floodlights surrounded by a packed crowd, many different national flags of the world displayed around the stands, a global tournament atmosphere, no readable text, no recognizable faces, wide cinematic shot, {GUARD}, {NEG}"),
    (f"{D}-worldcup-2026-kickoff", "broll_3.jpg", f"A gleaming generic golden football championship trophy on a pedestal under a dramatic spotlight in a darkened stadium, blurred floodlights behind, a prestige final atmosphere, no readable text, no logos, shallow depth of field, {GUARD}, {NEG}"),
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
            print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n{ok}/{len(jobs)} scenes generated", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
