#!/usr/bin/env python3
"""V11 props builder — VO-first timeline assembly.

Input: a "brief" JSON:
{
  "slug": "2026-07-03-iraq-grid-v11-golden",
  "kicker": "عاجل",
  "hookHeadline": "...",             # on-screen kinetic hook (dialect allowed)
  "voText": "...",                   # MSA newscast narration, ~60-85 words
  "endQuestion": "...",
  "sourcesLine": "المصادر: ...",
  "images": ["images/news/<slug>/hero.jpg", ... 4 paths rel. to public/],
  "audioBed": "audio/mood_newsroom.mp3",
  "statPops": [{"value":"50,000","label":"...","matchWord":"خمسين"}, ...]
}

Does: VO gen (generate-vo-v11.py, auto engine) → word timings → shots cut on
word boundaries (~3.2s each, deterministic Ken-Burns presets, 4 images cycled)
→ karaoke lines (≤5 words, break on punctuation/gaps) → stat pops synced to the
word where the number is SPOKEN → writes:
  data/posts/<slug>/.meta/v11-props.json
  my-video/src/compositions/NewsReelV11/defaultProps.ts   (--default flag)
"""
from __future__ import annotations
import argparse, json, math, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "my-video" / "public"
FPS = 30
ENDCARD = 75
TARGET_SHOT_F = 96          # ~3.2s
PUNCT = "؟?!.،:؛"

# Deterministic Ken-Burns presets, cycled by shot index (no randomness — reproducible renders)
MOVES = [
    dict(fromScale=1.06, toScale=1.24, fromX=0.0, fromY=0.0, toX=0.0, toY=-0.35),
    dict(fromScale=1.28, toScale=1.10, fromX=-0.4, fromY=0.2, toX=0.3, toY=0.0),
    dict(fromScale=1.10, toScale=1.30, fromX=0.35, fromY=-0.2, toX=-0.3, toY=0.15),
    dict(fromScale=1.32, toScale=1.12, fromX=0.0, fromY=-0.4, toX=0.0, toY=0.3),
    dict(fromScale=1.08, toScale=1.26, fromX=-0.3, fromY=-0.25, toX=0.35, toY=0.2),
    dict(fromScale=1.26, toScale=1.08, fromX=0.3, fromY=0.3, toX=-0.25, toY=-0.2),
]


def f(sec: float) -> int:
    return int(round(sec * FPS))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("brief")
    ap.add_argument("--engine", default="auto")
    ap.add_argument("--default", action="store_true", help="also write defaultProps.ts for Studio")
    args = ap.parse_args()

    brief = json.loads(Path(args.brief).read_text())
    slug = brief["slug"]
    meta_dir = ROOT / "data" / "posts" / slug / ".meta"
    meta_dir.mkdir(parents=True, exist_ok=True)

    # 1) VO + word timings (audio lands in public/ so the comp can play it)
    vo_dir = PUB / "vo" / slug
    r = subprocess.run([sys.executable, str(ROOT / "automation/scripts/generate-vo-v11.py"),
                        "--text", brief["voText"], "--out-dir", str(vo_dir), "--engine", args.engine],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        sys.exit(f"VO generation failed (HOLD): {r.stderr.strip()[:400]}")
    wdata = json.loads((vo_dir / "words.json").read_text())
    words = wdata["words"]
    vo_dur = wdata["durationSeconds"]
    vo_f = f(vo_dur)
    total_f = vo_f + ENDCARD

    # word frames
    W = [{"word": w["word"], "startF": f(w["start"]), "endF": f(w["end"])} for w in words]

    # 2) shots — cut points snapped to nearest word start
    n_shots = max(6, min(14, round(vo_f / TARGET_SHOT_F)))
    starts_ideal = [round(i * vo_f / n_shots) for i in range(n_shots)]
    word_starts = [w["startF"] for w in W]
    cut_frames = [0]
    for ideal in starts_ideal[1:]:
        nearest = min(word_starts, key=lambda ws: abs(ws - ideal))
        if nearest - cut_frames[-1] >= 45:          # never a shot under 1.5s
            cut_frames.append(nearest)
    cut_frames.append(vo_f + ENDCARD)               # last shot runs under the end card
    images = brief["images"]
    shots = []
    for i in range(len(cut_frames) - 1):
        mv = MOVES[i % len(MOVES)]
        shots.append({
            "img": images[i % len(images)],
            "startF": cut_frames[i],
            "durationF": cut_frames[i + 1] - cut_frames[i],
            **mv,
        })

    # 3) karaoke lines — ≤5 words, break on punctuation or ≥0.6s gap
    lines, cur = [], []
    for i, w in enumerate(W):
        cur.append(w)
        gap_next = (W[i + 1]["startF"] - w["endF"]) if i + 1 < len(W) else 999
        if (len(cur) >= 5 or w["word"][-1] in PUNCT or gap_next >= f(0.6)) and cur:
            lines.append({"words": cur, "startF": cur[0]["startF"], "endF": cur[-1]["endF"]})
            cur = []
    if cur:
        lines.append({"words": cur, "startF": cur[0]["startF"], "endF": cur[-1]["endF"]})

    # 4) stat pops — synced to the word where the number is spoken
    pops = []
    for sp in brief.get("statPops", [])[:2]:
        m = sp.get("matchWord", "")
        hit = next((w for w in W if m and m in w["word"]), None)
        if hit:
            pops.append({"value": sp["value"], "labelArabic": sp["label"],
                         "atFrame": max(0, hit["startF"] - 2), "holdFrames": 75})
        else:
            print(f"  ⚠ statPop matchWord not found in VO: {m!r} — skipped")

    props = {
        "kicker": brief.get("kicker", "عاجل"),
        "hookHeadline": brief["hookHeadline"],
        "vo": f"vo/{slug}/vo.mp3",
        "audioBed": brief.get("audioBed", ""),
        "bedVolume": 0.16,
        "shots": shots,
        "lines": lines,
        "statPops": pops,
        "endQuestion": brief["endQuestion"],
        "handle": "@photonect.news",
        "sourcesLine": brief.get("sourcesLine", ""),
        "totalFrames": total_f,
    }

    out = meta_dir / "v11-props.json"
    out.write_text(json.dumps(props, ensure_ascii=False, indent=1))
    print(f"✓ {out}")
    print(f"  vo={vo_dur:.1f}s total={total_f}f ({total_f/FPS:.1f}s) shots={len(shots)} lines={len(lines)} pops={len(pops)}")

    if args.default:
        ts = ROOT / "my-video/src/compositions/NewsReelV11/defaultProps.ts"
        ts.write_text("// AUTO-GENERATED by scripts/build_v11_props.py\n"
                      "import type { NewsReelV11Props } from \"./schema\";\n\n"
                      "export const v11DefaultProps: NewsReelV11Props = "
                      + json.dumps(props, ensure_ascii=False, indent=2) + ";\n")
        print(f"✓ {ts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
