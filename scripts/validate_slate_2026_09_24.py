#!/usr/bin/env python3
"""Structural gate for the 2026-09-24 slate — run after ANY writer touches the files.

Checks the rules that silently break a render or an editorial standard:
Persian chars, heading/body/hook word caps, voText length + numeral-free +
ends-in-endQuestion, statPop count/uniqueness/verbatim-single-word matchWord,
sources is a list, image refs resolve and are unique per beat, caption shape.
"""
import json, re, sys
from pathlib import Path

D = "2026-09-24"
ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
PUB = ROOT / "my-video" / "public"
PERSIAN = re.compile(r"[یکپچژگ]")
ARABIC_DIGIT = re.compile(r"[0-9٠-٩]")
WORD = re.compile(r"[^\s،.؟!\"«»]+")

bad, warn = [], []
slugs = sorted(p.name for p in POSTS.glob(f"{D}-*") if p.is_dir())
print(f"slate: {len(slugs)} slugs\n")

for slug in slugs:
    d = POSTS / slug
    props = json.loads((d / ".meta/props.json").read_text(encoding="utf-8"))
    cap = (d / "caption.txt").read_text(encoding="utf-8")
    vb = d / ".meta/v11-brief.json"
    tag = slug.replace(f"{D}-", "")

    blob = json.dumps(props, ensure_ascii=False) + cap
    if vb.exists():
        blob += vb.read_text(encoding="utf-8")
    for m in PERSIAN.finditer(blob):
        bad.append(f"{tag}: PERSIAN CHAR U+{ord(m.group()):04X} {m.group()!r}")
        break

    if not isinstance(props.get("sources"), list):
        bad.append(f"{tag}: sources is not a list")

    used = []
    refs = [props["breaking"]["heroMedia"]] + [b["broll"] for b in props["beats"]]
    for r in refs:
        if not (PUB / r).exists():
            bad.append(f"{tag}: missing image {r}")
        used.append(r)
    if len(set(used)) != len(used):
        bad.append(f"{tag}: an image is reused across beats")

    for i, b in enumerate(props["beats"], 1):
        h, body = b["arabicHeading"], b["arabicBody"]
        if len(h.split()) > 8:
            bad.append(f"{tag} beat{i}: heading {len(h.split())} words > 8 — {h}")
        if len(body.split()) > 26:
            bad.append(f"{tag} beat{i}: body {len(body.split())} words > 26")
        if not b.get("bigStat", {}).get("value"):
            bad.append(f"{tag} beat{i}: no bigStat value")

    # caption shape
    lines = [l for l in cap.strip().splitlines() if l.strip()]
    if len(lines[0].split()) > 12:
        bad.append(f"{tag}: caption line 1 is {len(lines[0].split())} words > 12")
    if ARABIC_DIGIT.search(lines[0]):
        warn.append(f"{tag}: caption line 1 contains a figure — should be an SEO hook, not a numbers headline")
    tags = [w for w in cap.split() if w.startswith("#")]
    if not (3 <= len(tags) <= 5):
        bad.append(f"{tag}: {len(tags)} hashtags (need 3-5)")
    if "@photonect.news" not in cap:
        bad.append(f"{tag}: caption missing @photonect.news")
    if "المصادر" not in cap:
        bad.append(f"{tag}: caption missing sources tail")

    if vb.exists():
        v = json.loads(vb.read_text(encoding="utf-8"))
        vo, eq = v["voText"], v["endQuestion"]
        if len(v["hookHeadline"].split()) > 7:
            bad.append(f"{tag}: hookHeadline {len(v['hookHeadline'].split())} words > 7")
        n = len(vo.split())
        if not (70 <= n <= 85):
            (warn if 65 <= n <= 92 else bad).append(f"{tag}: voText {n} words (target 70-85)")
        if ARABIC_DIGIT.search(vo):
            bad.append(f"{tag}: voText contains a DIGIT — TTS has no numeral normaliser")
        if not vo.rstrip().endswith(eq.rstrip()):
            bad.append(f"{tag}: voText does not end with endQuestion")
        pops = v.get("statPops", [])
        if len(pops) != 2:
            bad.append(f"{tag}: {len(pops)} statPops (need exactly 2)")
        vo_words = WORD.findall(vo)
        seen = set()
        for sp in pops:
            mw = sp.get("matchWord", "")
            if len(mw.split()) != 1:
                bad.append(f"{tag}: matchWord {mw!r} is not ONE word")
            elif mw not in vo_words:
                bad.append(f"{tag}: matchWord {mw!r} NOT verbatim in voText -> pop drops silently")
            if mw in seen:
                bad.append(f"{tag}: duplicate matchWord {mw!r}")
            seen.add(mw)
        for im in v["images"]:
            if not (PUB / im).exists():
                bad.append(f"{tag}: brief image missing {im}")
        print(f"  {tag:32s} V11  vo={n}w pops={len(pops)} hook={v['hookHeadline']!r}")
    else:
        print(f"  {tag:32s} V10.1 CONTROL (silent)")

print()
for w in warn:
    print("  WARN ", w)
for b in bad:
    print("  FAIL ", b)
print("\nRESULT:", "PASS" if not bad else f"{len(bad)} FAILURE(S)")
sys.exit(1 if bad else 0)
