#!/usr/bin/env python3
"""Generate AI scenes for the 2026-06-28 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. Real faces (Rafael Fiziev, Abdel Fattah
al-Burhan) are fetched separately into their broll_1.jpg, so this script skips
those two slots. Toy Story 5 scenes are GENERIC cinema imagery — no Pixar
characters/IP depicted."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-28"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no brand marks, no garbled characters"

JOBS = [
    # 1. IRAQ GREEN ZONE ARRESTS — govt district at night, security cordon, seized cash, parliament
    (f"{D}-iraq-greenzone-arrests", "hero.jpg", f"A fortified government district in Baghdad at night, wide boulevards lined with tall concrete blast walls and palm trees, distant lit government buildings, a tense quiet curfew atmosphere under sodium street lights, wide cinematic establishing aerial shot, {NEG}, {X}"),
    (f"{D}-iraq-greenzone-arrests", "broll_2.jpg", f"Neat stacks and bundles of seized banknotes laid out as evidence on a dark official table under a single overhead light, an anti-corruption investigation mood, shallow depth of field, no readable text on the notes, serious documentary still, {NEG}, {X}"),
    (f"{D}-iraq-greenzone-arrests", "broll_3.jpg", f"A grand Middle Eastern parliament and government building exterior at dawn, sand-colored stone facade with a flagpole and an empty plaza, institutional and austere, soft early light, wide cinematic shot, no readable text, {NEG}, {X}"),
    # 2. UFC BAKU FIZIEV — arena octagon, (broll_1 = real Fiziev, fetched), action kick, crowd
    (f"{D}-ufc-baku-fiziev", "hero.jpg", f"A dramatic mixed-martial-arts arena interior, an empty hexagonal fighting cage in the center under intense focused spotlights, deep dark stands beyond, smoke and atmosphere, high-energy fight-night mood, wide cinematic establishing shot, no logos or text, {NEG}, {X}"),
    (f"{D}-ufc-baku-fiziev", "broll_2.jpg", f"A powerful male mixed-martial-arts fighter mid spinning wheel kick inside a brightly lit cage, dynamic frozen motion, sweat and intensity, shallow depth of field, dramatic sports photography, face not identifiable, no logos or text, {NEG}, {X}"),
    (f"{D}-ufc-baku-fiziev", "broll_3.jpg", f"A packed combat-sports arena crowd on its feet cheering at night, sea of blurred faces lit by stage lighting and phone flashes, electric celebratory atmosphere, wide cinematic shot, no logos or readable text, {NEG}, {X}"),
    # 3. SUDAN BURHAN DEADLOCK — Khartoum/Nile, (broll_1 = real Burhan, fetched), diplomacy table, displacement
    (f"{D}-sudan-burhan-deadlock", "hero.jpg", f"Khartoum Sudan at tense dusk, the confluence of the Blue and White Nile rivers seen from above with low city rooftops and minarets, hazy amber and grey smoke-tinged sky, a nation at war mood, wide cinematic establishing aerial shot, {NEG}, {X}"),
    (f"{D}-sudan-burhan-deadlock", "broll_2.jpg", f"A formal international mediation room with a long polished table and rows of empty chairs, blank neutral flag stands and microphones, stalled-negotiations emptiness, cool daylight through tall windows, no people, no readable text, {NEG}, {X}"),
    (f"{D}-sudan-burhan-deadlock", "broll_3.jpg", f"A long line of displaced African civilians walking across an arid dusty landscape carrying bundles and water containers, distant white humanitarian tents, harsh sun and haze, a refugee crisis documentary wide shot, dignified and sober, no readable text, {NEG}, {X}"),
    # 4. EXOPLANETS SUPER-PUFF — puffy planets by a star, telescope, wispy planet, citizen scientist
    (f"{D}-exoplanets-superpuff", "hero.jpg", f"A breathtaking deep-space scene of two enormous pale pastel pink and cream gas-giant planets, extremely puffy diffuse and wispy like cotton candy, glowing softly beside a distant bright dwarf star against the black star-filled cosmos, ethereal astrophysical visualization, cinematic, no labels or text, {NEG}, {X}"),
    (f"{D}-exoplanets-superpuff", "broll_1.jpg", f"A sleek space telescope satellite drifting in orbit against a vast field of stars and the faint band of the Milky Way, solar panels catching distant starlight, awe and scale, wide cinematic space shot, no text, {NEG}, {X}"),
    (f"{D}-exoplanets-superpuff", "broll_2.jpg", f"An extreme close visualization of a single colossal ultra-low-density planet, translucent wispy pastel cloud bands so diffuse you can almost see through it, soft backlight from a distant sun, dreamy cotton-candy texture, dark starry background, no labels or text, {NEG}, {X}"),
    (f"{D}-exoplanets-superpuff", "broll_3.jpg", f"A volunteer citizen-scientist silhouetted in a dim room studying glowing screens filled with abstract astronomical light-curve graphs and a highlighted bright dip, quiet discovery moment, cinematic, no readable text, {NEG}, {X}"),
    # 5. UAE ETIHAD RAIL — sleek train at desert station, platform, line across desert, transit hub
    (f"{D}-uae-etihad-rail", "hero.jpg", f"A sleek modern silver-and-red high-speed intercity passenger train waiting at a gleaming new desert railway station at golden dusk in the United Arab Emirates, clean architecture, distant dunes and a city skyline, optimistic, wide cinematic establishing shot, no logos or text, {NEG}, {X}"),
    (f"{D}-uae-etihad-rail", "broll_1.jpg", f"A bright modern train platform with a streamlined passenger train doors open, a few travelers with luggage about to board, polished floors and clean contemporary Gulf station design, warm welcoming light, wide shot, no readable text or logos, {NEG}, {X}"),
    (f"{D}-uae-etihad-rail", "broll_2.jpg", f"A sweeping aerial of a long modern railway line cutting straight across golden desert dunes toward a distant glittering Gulf city skyline at dusk, sense of national scale and connection, wide cinematic drone shot, no text, {NEG}, {X}"),
    (f"{D}-uae-etihad-rail", "broll_3.jpg", f"The bright airy interior concourse of a futuristic Gulf transit hub, soaring white architecture, escalators and walkways, a few blurred commuters in motion, modern public-transport optimism, wide shot, no readable text or logos, {NEG}, {X}"),
    # 6. TOY STORY 5 RECORD — GENERIC cinema only, no Pixar IP — auditorium, marquee, studio, lobby
    (f"{D}-toystory5-record", "hero.jpg", f"A packed modern cinema auditorium seen from the front, rows of silhouetted audience heads watching a huge bright glowing blank screen, warm projector beam cutting through the dark, blockbuster opening-night atmosphere, wide cinematic shot, the screen shows only abstract colorful light no characters, {NEG}, {X}"),
    (f"{D}-toystory5-record", "broll_1.jpg", f"A nostalgic cinema lobby at night, a glowing blank illuminated marquee and movie-poster light boxes with no readable text, a fresh tub of buttered popcorn and tickets in the foreground in soft focus, festive box-office-record mood, warm bokeh lights, {NEG}, {X}"),
    (f"{D}-toystory5-record", "broll_2.jpg", f"A colorful modern 3D animation studio workstation, large monitors showing abstract generic colorful clay-like shapes and color swatches, sculpting tools and toys-as-inspiration on the desk, creative animation craft mood, no recognizable characters, no readable text, shallow depth of field, {NEG}, {X}"),
    (f"{D}-toystory5-record", "broll_3.jpg", f"A happy family with two excited children walking into a bright modern movie-theater lobby holding popcorn, warm welcoming light, blurred poster light boxes behind with no readable text, joyful family-cinema outing, wide candid shot, {NEG}, {X}"),
]


def submit_retry(prompt, tries=5):
    last = None
    for i in range(tries):
        try:
            return submit(prompt)
        except Exception as e:
            last = e
            time.sleep(3 * (i + 1))
    raise last


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs (skip existing) ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname} (already on disk)", flush=True)
            continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
    if not jobs:
        print("== nothing to generate; all on disk ==", flush=True)
        return 0
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
                    continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl retry {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:160]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} scenes ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"  MISSING {j['slug']}/{j['file']}", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
