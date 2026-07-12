#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-12 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces — several officials here are new
2026 figures with no real Commons portrait; scene-based avoids wrong-face + fake-face
risk, matching the 2026-07-11 precedent). Each prompt is matched to THAT beat's Arabic
text. Hardened anti-UI / anti-text / anti-foreign-flag negatives (see
feedback_kie_fake_ui_govbuilding). Read-verify every image before accept.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

# Extra-hard negatives for the map / network / UI-risk shots.
HARD = "absolutely no readable text, no numbers, no letters, no user interface, no app screen, no news graphics, no maps with labels, no watermark, no logos"

D = "2026-07-12"
JOBS = [
    # 1 · graft-money-abroad (P1, V11 — Integrity Commission + Interpol hunt fled assets)
    (f"{D}-graft-money-abroad", "hero.jpg", f"An editorial evidence still on a dark table, neat tall stacks of seized US hundred-dollar banknotes and gold bars under a hard police spotlight, a major state corruption seizure, no logos, no readable text, {NEG}"),
    (f"{D}-graft-money-abroad", "broll_1.jpg", f"A darkened financial-crime operations center at night, a huge glowing world map on the wall with faint arcing light lines between distant continents, a lone analyst silhouetted from behind tracking fleeing assets, cool blue cinematic light, {HARD}, {NEG}"),
    (f"{D}-graft-money-abroad", "broll_2.jpg", f"Elite Iraqi anti-corruption officers in black tactical gear escorting a detained official out of a government building at dawn, the suspect faceless from behind with hands held behind the back, tense documentary photojournalism, no faces visible, {NEG}"),
    (f"{D}-graft-money-abroad", "broll_3.jpg", f"Two empty facing chairs at a bare diplomatic negotiating table in a plain official room with soft grey window light, a stalled extradition and asset-return negotiation between states, minimalist editorial, no readable text, {NEG}"),
    # 2 · zaidi-washington-fund (P2 — Iraqi PM visits Washington: energy fund, LNG, waiver)
    (f"{D}-zaidi-washington-fund", "hero.jpg", f"The White House exterior at golden hour, an Iraqi flag and an American flag side by side on tall poles in the foreground, a high-stakes state visit mood, cinematic editorial wide shot, {HARD}, {NEG}"),
    (f"{D}-zaidi-washington-fund", "broll_1.jpg", f"A formal bilateral meeting room, two national delegations seated across a long polished table with an Iraqi flag and an American flag behind them, figures seen from behind and the side with no clear faces, business delegation diplomacy, editorial, no readable text, {NEG}"),
    (f"{D}-zaidi-washington-fund", "broll_2.jpg", f"A floating storage and regasification LNG vessel moored at a Basra Gulf import terminal at dusk, pipelines and storage tanks, gas-import infrastructure to power the grid, industrial cinematic aerial shot, no readable text, {NEG}"),
    (f"{D}-zaidi-washington-fund", "broll_3.jpg", f"A large crude oil pipeline and a bright gas flare under a tense grey sky in a border desert region, energy dependence and sanctions pressure, moody industrial editorial mid shot, no readable text, {NEG}"),
    # 3 · power-summer-blackout (P1, V11 — grid loses 5000 MW as Iran gas is cut)
    (f"{D}-power-summer-blackout", "hero.jpg", f"A Baghdad residential neighborhood at night during a power blackout, mostly dark apartment blocks with only a few windows lit, a single private diesel generator glowing in an alley, oppressive summer heat haze, cinematic editorial wide shot, no readable text, {NEG}"),
    (f"{D}-power-summer-blackout", "broll_1.jpg", f"Rows of high-voltage electricity transmission towers and a substation silhouetted at dusk under a dramatic dark sky, a national power grid under strain, industrial editorial wide shot, no readable text, {NEG}"),
    (f"{D}-power-summer-blackout", "broll_2.jpg", f"A gas-fired power plant with tall stacks and a low weak flare under a hazy, blistering hot sky, turbines running below capacity from reduced gas supply, industrial documentary, no readable text, {NEG}"),
    (f"{D}-power-summer-blackout", "broll_3.jpg", f"A neighborhood diesel generator with a tangle of cables powering a row of small shops on a hot night street in Iraq, ordinary people relying on private generators, gritty documentary photojournalism, no readable text, {NEG}"),
    # 4 · iraq-data-corridor (P2 — Iraq becomes a regional internet-transit corridor)
    (f"{D}-iraq-data-corridor", "hero.jpg", f"A modern data-center server hall, long rows of tall server racks with glowing blue and cyan LED lights receding into the distance, cool high-tech cinematic atmosphere, {HARD}, {NEG}"),
    (f"{D}-iraq-data-corridor", "broll_1.jpg", f"A subsea fiber-optic cable being laid from the drum of a cable-laying ship into a calm blue sea at dawn, international telecom transit infrastructure, industrial editorial aerial shot, no readable text, {NEG}"),
    (f"{D}-iraq-data-corridor", "broll_2.jpg", f"A tall 5G mobile-network tower rising over Iraqi city rooftops at golden hour, modern connectivity reaching a dense neighborhood, clean editorial telecom shot, no readable text, {NEG}"),
    (f"{D}-iraq-data-corridor", "broll_3.jpg", f"An abstract glowing data-corridor concept, streams of light flowing across a dark stylized landscape from the Gulf coast overland toward Europe, a high-tech connectivity artery, {HARD}, {NEG}"),
    # 5 · gene-cure-thalassemia (P3 — CRISPR gene therapy for thalassemia reaches MENA)
    (f"{D}-gene-cure-thalassemia", "hero.jpg", f"A warm, hopeful pediatric hospital scene, a young child patient's small hand with a tiny bandage resting on a soft blanket, gentle window light, a sense of healing and new hope, tender medical editorial, no readable text, {NEG}"),
    (f"{D}-gene-cure-thalassemia", "broll_1.jpg", f"A bright modern gene-therapy laboratory, a scientist in full PPE and gloves holding up a small vial of edited cells under blue lab light, advanced biotechnology, cinematic editorial, no readable text, {NEG}"),
    (f"{D}-gene-cure-thalassemia", "broll_2.jpg", f"A gentle bright pediatric ward, a nurse in scrubs adjusting an IV line for a calm young child in bed, warm hopeful family-centered light, medical documentary, no readable text, {NEG}"),
    (f"{D}-gene-cure-thalassemia", "broll_3.jpg", f"A modern regional hospital exterior in the Gulf at golden hour with palm trees and clean architecture, advanced medical care close to home, calm editorial establishing shot, no readable text, {NEG}"),
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
    deadline = time.time() + 20 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception as e:
                msg = str(e)
                if "402" in msg:
                    print("  !! KIE 402 out-of-credits — aborting, fall back to Pexels/Commons", file=sys.stderr, flush=True)
                    return 2
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    print(f"  ? {j['slug']}/{j['file']}: success but no url", file=sys.stderr, flush=True)
                    continue
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  OK {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  X {j['slug']}/{j['file']}: fail — {data.get('failMsg','?')}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(JOBS)} images ==", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
