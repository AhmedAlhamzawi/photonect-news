#!/usr/bin/env python3
"""Cinematic AI scenes for the 3-reel Iraq "تغطية خاصة" special (Green Zone raid).
Nano Banana Pro 9:16 2K via the shared KIE harness. MASTERPIECE bar:
dramatic, cohesive, neutral, SYMBOLIC — no faces of the accused, no text/UI/logos.
One hero + 3 brolls per slug → 12 stills into images/news/<slug>/."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, "
     "no fake screenshots, no watermark, no logos, no brand marks, no garbled characters, "
     "no recognizable real faces of identifiable people")

RAID = "2026-06-28-iraq-special-raid"
GRAFT = "2026-06-28-iraq-special-graft"
STAKES = "2026-06-28-iraq-special-stakes"

JOBS = [
    # 1 — THE RAID
    (RAID, "hero.jpg", f"Cinematic night aerial establishing shot of a heavily fortified Middle Eastern government 'green zone' district sealed off by security forces, towering concrete blast walls and checkpoints, armored vehicles with headlights on empty boulevards, cold blue and red emergency light glow, tense dramatic atmosphere, wide anamorphic cinematic shot, {NEG}, {X}"),
    (RAID, "broll_1.jpg", f"A tense nighttime security cordon at a city checkpoint, distant silhouetted soldiers and armored vehicles blocking a road behind concrete barriers and razor wire, harsh floodlights cutting the dark, dramatic chiaroscuro, documentary wide shot, faces not visible, {NEG}, {X}"),
    (RAID, "broll_2.jpg", f"A dim official investigation room, tall stacks of bundled case files and document folders on a steel table under a single hard desk lamp, long deep shadows, a sense of unfolding evidence, no people, moody cinematic still, {NEG}, {X}"),
    (RAID, "broll_3.jpg", f"An austere empty government press podium with plain unmarked flag stands in a quiet official hall at dawn, soft grey light through tall windows, institutional stillness and anticipation, no people, no readable text, cinematic, {NEG}, {X}"),
    # 2 — THE GRAFT CASE
    (GRAFT, "hero.jpg", f"A stark dramatic overhead scene of large bundles of seized banknotes stacked and laid out across a steel evidence table under harsh investigative light, an anti-corruption cash seizure, serious forensic mood, shallow depth of field, no readable text on the money, cinematic, {NEG}, {X}"),
    (GRAFT, "broll_1.jpg", f"A nighttime forensic excavation under floodlights where investigators have unearthed buried bundles of cash from a deep pit in bare ground, a mechanical digger and shovels nearby, dramatic crime-scene atmosphere, faces not visible, wide cinematic shot, {NEG}, {X}"),
    (GRAFT, "broll_2.jpg", f"A symbolic cinematic still of polished metal handcuffs resting on a stack of official document folders, the faint silhouette of an oil refinery and its towers at dusk in the soft-focus background, themes of accountability, moody lighting, no people, no readable text, {NEG}, {X}"),
    (GRAFT, "broll_3.jpg", f"A gleaming brass scales of justice on a dark polished wooden desk in a quiet courtroom, soft directional window light, fine dust drifting in the air, perfectly balanced and neutral, shallow depth of field, no text, cinematic, {NEG}, {X}"),
    # 3 — THE STAKES
    (STAKES, "hero.jpg", f"A cinematic wide establishing shot of an imposing modern Iraqi government complex in Baghdad at dramatic dusk, an Iraqi flag flying, a brooding sky suggesting a moment of national reckoning, dignified and neutral, no readable text, anamorphic, {NEG}, {X}"),
    (STAKES, "broll_1.jpg", f"A clean modern government corridor leading toward an austere official chamber, an Iraqi flag on a stand, polished floor reflecting soft cool light, a sense of new leadership and reform, no people, no readable text, cinematic, {NEG}, {X}"),
    (STAKES, "broll_2.jpg", f"A large empty parliamentary debating chamber with curved rows of vacant seats during recess, dramatic overhead lighting and deep shadows, quiet institutional tension, wide cinematic shot, no people, no readable text, {NEG}, {X}"),
    (STAKES, "broll_3.jpg", f"A symbolic cinematic close shot of a judge's wooden gavel and sound block on a desk at first light, soft hopeful glow, themes of justice and accountability ahead, shallow depth of field, no text, {NEG}, {X}"),
]


def submit_retry(prompt, tries=5):
    last = None
    for i in range(tries):
        try:
            return submit(prompt)
        except Exception as e:
            last = e; time.sleep(3 * (i + 1))
    raise last


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} Iraq-special scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname} (on disk)", flush=True); continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
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
                    still.append(j); continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl retry {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True); still.append(j)
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
