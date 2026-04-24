#!/usr/bin/env python3
"""
apply-v5-signatures.py

V5 per-slug signature enforcement. For every April 21 slug, applies a unique
(variant, accent, audioBed) triplet so the slate reads as 12 distinct reels
instead of "3 templates copy-pasted 4 times each."

The assignment is deterministic and derived from the slug — editing this script
is the single source of truth for per-slug visual identity.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")

# V5 per-slug signature table. variant rotates through A/B/C with zero bucket
# adjacency; accent is slug-specific; audioBed is unique across all 12 slugs.
SIGNATURES = {
    "2026-04-21-iraq-vote": {
        "variant": "A",
        "accent": "#FFD447",          # warm political yellow
        "audioBed": "audio/news_bed_urgent.mp3",
        "motionNote": "MONEY-SHOT — 227 count-up",
    },
    "2026-04-21-brent-150": {
        "variant": "B",
        "accent": "#FF8C42",          # amber — oil
        "audioBed": "audio/news_bed_electric.mp3",
        "motionNote": "KINETIC-SPLIT — market shock",
    },
    "2026-04-21-ceasefire-break": {
        "variant": "A",
        "accent": "#FF2D55",          # hot red — violence
        "audioBed": "audio/news_bed_dread.mp3",
        "motionNote": "MONEY-SHOT — 47 dead",
    },
    "2026-04-21-ai-nuclear-sim": {
        "variant": "B",
        "accent": "#00F0FF",          # cyan — tech
        "audioBed": "audio/news_bed_pulse.mp3",
        "motionNote": "KINETIC-SPLIT — 0.3% failure",
    },
    "2026-04-21-berlin-protest": {
        "variant": "C",
        "accent": "#8E9AFF",          # steel blue — civic
        "audioBed": "audio/news_bed_stark.mp3",
        "motionNote": "CINEMA — 500K on Brandenburg",
    },
    "2026-04-21-un-secgen-plan": {
        "variant": "A",
        "accent": "#B8DBD9",          # pale teal — diplomatic
        "audioBed": "audio/news_bed_tense.mp3",
        "motionNote": "MONEY-SHOT — 7 points / veto",
    },
    "2026-04-21-crypto-tether-depeg": {
        "variant": "B",
        "accent": "#39FF14",          # electric green — collapse markets
        "audioBed": "audio/news_bed_chase.mp3",
        "motionNote": "KINETIC-SPLIT — $0.87",
    },
    "2026-04-21-opec-emergency-2": {
        "variant": "C",
        "accent": "#E8B923",          # gold — oil
        "audioBed": "audio/news_bed_somber.mp3",
        "motionNote": "CINEMA — Vienna emergency",
    },
    "2026-04-21-kdp-split": {
        "variant": "A",
        "accent": "#C3272B",          # Kurdish red
        "audioBed": "audio/news_bed.mp3",
        "motionNote": "MONEY-SHOT — 58 MPs defect",
    },
    "2026-04-21-imf-sa-loan": {
        "variant": "B",
        "accent": "#00E5A0",          # mint — finance
        "audioBed": "audio/news_bed_uplift.mp3",
        "motionNote": "KINETIC-SPLIT — $40B IMF",
    },
    "2026-04-21-egypt-mobilize": {
        "variant": "C",
        "accent": "#C9A66B",          # desert sand
        "audioBed": "audio/news_bed_drone.mp3",
        "motionNote": "CINEMA — 200K to Sinai",
    },
    "2026-04-21-north-korea-ship": {
        "variant": "C",
        "accent": "#FF006E",          # magenta — intercept alert
        "audioBed": "audio/news_bed_mist.mp3",
        "motionNote": "CINEMA — DPRK intercept",
    },
}


def apply(slug: str, sig: dict) -> tuple[bool, list[str]]:
    props_path = ROOT / slug / "props.json"
    if not props_path.exists():
        return False, [f"missing {props_path}"]

    props = json.loads(props_path.read_text())
    changes = []

    # Top-level overrides
    if props.get("variant") != sig["variant"]:
        changes.append(f"variant: {props.get('variant', '(unset)')} → {sig['variant']}")
        props["variant"] = sig["variant"]
    if props.get("audioBed") != sig["audioBed"]:
        changes.append(f"audioBed: {props.get('audioBed', '(unset)')} → {sig['audioBed']}")
        props["audioBed"] = sig["audioBed"]

    # Per-beat accent
    for i, beat in enumerate(props.get("beats", [])):
        if beat.get("accent") != sig["accent"]:
            changes.append(f"beat[{i}].accent: {beat.get('accent', '(unset)')} → {sig['accent']}")
            beat["accent"] = sig["accent"]

    if changes:
        props_path.write_text(json.dumps(props, indent=2, ensure_ascii=False) + "\n")

    return True, changes


def main() -> None:
    print("V5 per-slug signature enforcement — 12 slugs")
    print("=" * 60)
    total_changes = 0
    for slug, sig in SIGNATURES.items():
        ok, changes = apply(slug, sig)
        if not ok:
            print(f"  {slug:40s}  SKIP ({changes[0]})")
            continue
        if not changes:
            print(f"  {slug:40s}  (already up to date)")
            continue
        print(f"  {slug:40s}  [{sig['variant']}] → {sig['audioBed'].split('/')[-1]}")
        for c in changes:
            print(f"    · {c}")
        total_changes += len(changes)

    print("=" * 60)
    print(f"Total field changes: {total_changes}")


if __name__ == "__main__":
    main()
