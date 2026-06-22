#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-22 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. Faces (Vance, Araghchi, al-Zaidi) fetched separately.
For iran-us-switzerland-talks, broll_1/broll_2 are real Commons faces — not generated here.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-22"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no garbled characters"

JOBS = [
    # 1. IRAQ AT THE WORLD CUP — green pitch, fans, no identifiable faces
    (f"{D}-iraq-worldcup-france", "hero.jpg", f"A packed modern World Cup football stadium at night under bright floodlights, a vast crowd waving Iraqi flags (red white black with green stars) in a tifo wall, electric celebratory atmosphere, wide cinematic establishing shot from high in the stands, {NEG}, {X}"),
    (f"{D}-iraq-worldcup-france", "broll_1.jpg", f"Joyful Iraqi football supporters in red and white scarves celebrating in the stands, draped in the Iraqi flag, faces blurred with motion and confetti, warm stadium lights, documentary sports photography, {NEG}, {X}"),
    (f"{D}-iraq-worldcup-france", "broll_2.jpg", f"A generic football team in dark jerseys celebrating a decisive victory on a floodlit pitch, players embracing in a huddle seen from behind, no identifiable faces, confetti falling, dramatic sports photography, {NEG}, {X}"),
    (f"{D}-iraq-worldcup-france", "broll_3.jpg", f"A single football resting on the centre spot of a pristine green floodlit pitch at night inside a huge empty modern stadium, dramatic long shadows, anticipation before kickoff, cinematic wide shot, {NEG}, {X}"),
    # 2. US-IRAN SWITZERLAND — hero + regional scene only (faces fetched separately)
    (f"{D}-iran-us-switzerland-talks", "hero.jpg", f"A formal diplomatic negotiation room in Switzerland, a long polished wooden table with the flag of the United States and the flag of Iran standing upright facing each other, empty leather chairs, soft window light over an Alpine lake view, no people, {NEG}, {X}"),
    (f"{D}-iran-us-switzerland-talks", "broll_3.jpg", f"The Beirut Lebanon skyline at calm dusk seen across the Mediterranean, quiet coastal city lights, a sense of fragile calm after conflict, soft golden-grey sky, cinematic wide aerial shot, {NEG}, {X}"),
    # 3. IRAQ MILITIA DISARMAMENT — Baghdad governance (broll_1 may be replaced by al-Zaidi face)
    (f"{D}-iraq-militia-disarmament", "hero.jpg", f"A large Iraqi national flag (red white black with green Arabic script) flying on a tall pole in front of a sand-coloured government building in Baghdad's Green Zone, bright daylight, low heroic angle, {NEG}, {X}"),
    (f"{D}-iraq-militia-disarmament", "broll_1.jpg", f"A formal Iraqi government meeting room with a long table and the Iraqi flag, empty chairs arranged for a delegation, neutral institutional setting, soft daylight, no people, ultra-realistic, {NEG}, {X}"),
    (f"{D}-iraq-militia-disarmament", "broll_2.jpg", f"A wide view of central Baghdad with government ministry buildings and the Tigris river, bright hazy daylight, palm trees, documentary cityscape, {NEG}, {X}"),
    (f"{D}-iraq-militia-disarmament", "broll_3.jpg", f"A symbolic still of disarmament, plain assault rifles laid down and stacked under the shadow of a large waving Iraqi flag, neutral grey concrete floor, somber documentary lighting, {NEG}, {X}"),
    # 4. GCC UNIFIED VISA + RAIL — bright, kinetic, integration
    (f"{D}-gcc-grand-tours-visa", "hero.jpg", f"A bright stylized map of the six Gulf states glowing gold with luminous open travel routes and arcs of light connecting modern cities, a faint passport silhouette in the foreground, ultra-modern data-visualization aesthetic, no labels, {NEG}, {X}"),
    (f"{D}-gcc-grand-tours-visa", "broll_1.jpg", f"A generic plain navy passport and a boarding scene at a sleek Gulf airport gate, blurred travelers with luggage, bright clean modern terminal, warm light, no readable text on documents, ultra-realistic, {NEG}, {X}"),
    (f"{D}-gcc-grand-tours-visa", "broll_2.jpg", f"A sleek silver high-speed passenger train crossing a sunlit Arabian desert landscape beside modern overhead catenary lines, golden dunes and a distant Gulf skyline, dynamic motion blur, cinematic wide shot, {NEG}, {X}"),
    (f"{D}-gcc-grand-tours-visa", "broll_3.jpg", f"A bright modern Gulf international airport departures hall with travelers walking, soaring glass-and-steel architecture, large windows with desert sunlight, blurred motion, ultra-realistic, {NEG}, {X}"),
    # 5. PANCREATIC-CANCER ORAL DRUG — bright clinical, no readable labels
    (f"{D}-pancreas-cancer-pill", "hero.jpg", f"A single small white oval pill held between two gloved fingers in clean bright clinical light, soft shallow focus, a faint upward survival curve glowing softly in the blurred background, ultra-realistic, {NEG}, {X}"),
    (f"{D}-pancreas-cancer-pill", "broll_1.jpg", f"A plain white unlabeled pill bottle with a few white oval pills spilling onto a clean bright clinical surface, soft medical lighting, no readable text on the bottle, ultra-realistic, {NEG}, {X}"),
    (f"{D}-pancreas-cancer-pill", "broll_2.jpg", f"A scientist in a white coat at a modern laboratory bench examining a glowing 3D molecular protein model on a translucent screen, cool blue lab lighting, blurred lab equipment, ultra-realistic research photography, {NEG}, {X}"),
    (f"{D}-pancreas-cancer-pill", "broll_3.jpg", f"A clean minimalist medical line graph showing a single rising survival curve, soft blue and white, bright, abstract data-visualization, no numbers, no text, {NEG}, {X}"),
    # 6. CLIMATE-RESILIENT CORAL REEFS — vivid underwater nature
    (f"{D}-coral-resilient-reefs", "hero.jpg", f"A vibrant healthy coral reef teeming with colorful fish in clear turquoise tropical water, bright sunbeams filtering from the surface, vivid pink purple and orange corals, ultra-realistic underwater photography, {NEG}, {X}"),
    (f"{D}-coral-resilient-reefs", "broll_1.jpg", f"A thriving dense colorful coral garden with schools of small fish, brilliant healthy reds yellows and blues, crystal clear sunlit water, ultra-realistic underwater nature documentary, {NEG}, {X}"),
    (f"{D}-coral-resilient-reefs", "broll_2.jpg", f"A starkly bleached white coral reef under pale washed-out water, ghostly skeletal coral branches, few fish, somber muted tones, climate-stress documentary photography, {NEG}, {X}"),
    (f"{D}-coral-resilient-reefs", "broll_3.jpg", f"A marine biologist scuba diver surveying a healthy reef with a clipboard, sunbeams from above, colorful corals and clear blue water, ultra-realistic underwater conservation photography, {NEG}, {X}"),
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
                    continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
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
