#!/usr/bin/env python3
"""Post-copywriter verification for the 2026-09-06 slate.

The copywriter subagent rewrites props.json / v11-brief.json / caption.txt in
place. This re-asserts every invariant that only bites at render time or, worse,
after publication:

  1. sources is a list of >=2 {name, domain} dicts   (Sources.tsx calls .map).
     The QA gate cut padded/duplicate entries on three slugs, so the floor is 2:
     a slate must never invent a third outlet to satisfy a schema minimum.
  2. arabicTicker is a list of strings                (schema shape)
  3. no Persian yeh (U+06CC) / kaf (U+06A9) anywhere
  4. exactly 2 statPops per brief, each matchWord present EXACTLY ONCE in voText
  5. voText word count in range, and no ASCII digits in voText (the VO has no
     numeral normaliser, so digits get read as raw numbers)
  6. every image path referenced exists on disk
  7. NUMBER DRIFT: the SET of distinct digit-runs in the shipped files is
     compared against the authored originals (imported from author_2026_09_06,
     which is the transcription of record). A value the copy pass INVENTED, or a
     sourced value it made VANISH, is a hard failure — a silently invented or
     re-based figure is the highest-cost failure this pipeline has. Repeating an
     already-verified number more or fewer times is not drift, so counts are
     ignored; hex accent colours and image paths are excluded as noise.
  8. endQuestion is consistent across props / brief / caption.
"""
from __future__ import annotations
import importlib.util, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
PUB = ROOT / "my-video" / "public"
D = "2026-09-06"

spec = importlib.util.spec_from_file_location("author", ROOT / "scripts" / f"author_{D.replace('-','_')}.py")
author = importlib.util.module_from_spec(spec)
spec.loader.exec_module(author)
ORIG = author.SLATE

PERSIAN = re.compile("[یک]")
NUM = re.compile(r"\d[\d,\.]*")
fails: list[str] = []
warns: list[str] = []


# Fields whose digits are never editorial: accent hex colours, media paths.
NOISE_KEYS = {"accent", "broll", "brolls", "heroMedia", "images", "audioBed",
              "slug", "dateLabel"}


def strings(node, key=None):
    if key in NOISE_KEYS:
        return
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from strings(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from strings(v, key)


def nums(node) -> set:
    out = set()
    for s in strings(node):
        for m in NUM.findall(s):
            out.add(m.rstrip(".,"))
    return out


for slug in sorted(p.name for p in POSTS.glob(f"{D}-*") if p.is_dir()):
    meta = POSTS / slug / ".meta"
    props = json.loads((meta / "props.json").read_text(encoding="utf-8"))
    caption = (POSTS / slug / "caption.txt").read_text(encoding="utf-8")
    bp = meta / "v11-brief.json"
    brief = json.loads(bp.read_text(encoding="utf-8")) if bp.exists() else None
    tag = "V11" if brief else "V10.1 control"

    src = props.get("sources")
    if not isinstance(src, list) or len(src) < 2 or not all(
            isinstance(x, dict) and {"name", "domain"} <= set(x) for x in src):
        fails.append(f"{slug}: sources is not a list of >=2 {{name,domain}} dicts")
    if not isinstance(props.get("arabicTicker"), list):
        fails.append(f"{slug}: arabicTicker is not a list")
    if len(props.get("beats", [])) != 3:
        fails.append(f"{slug}: expected 3 beats, got {len(props.get('beats', []))}")

    for label, blob in (("props", props), ("caption", caption), ("brief", brief or {})):
        for s in strings(blob):
            if PERSIAN.search(s):
                fails.append(f"{slug}: Persian yeh/kaf in {label}: {s[:70]}")

    imgs = [props["breaking"]["heroMedia"]] + [b["broll"] for b in props["beats"]]
    if brief:
        imgs += brief["images"]
    for rel in set(imgs):
        if not (PUB / rel).exists():
            fails.append(f"{slug}: missing image on disk: {rel}")

    if brief:
        vo = brief["voText"]
        pops = brief.get("statPops", [])
        if len(pops) != 2:
            fails.append(f"{slug}: {len(pops)} statPops, want exactly 2")
        for p in pops:
            n = vo.count(p["matchWord"])
            if n == 0:
                fails.append(f"{slug}: statPop matchWord {p['matchWord']!r} absent from voText -> pop dropped")
            elif n > 1:
                fails.append(f"{slug}: statPop matchWord {p['matchWord']!r} occurs {n}x in voText -> anchor collision")
        w = len(vo.split())
        if not 60 <= w <= 95:
            fails.append(f"{slug}: voText {w} words (want 70-85)")
        if re.search(r"\d", vo):
            fails.append(f"{slug}: voText contains ASCII digits -> VO has no numeral normaliser: "
                         f"{re.findall(r'[^ ]*\\d[^ ]*', vo)}")

    eq_props = props.get("endQuestion", "").strip()
    if brief and brief.get("endQuestion", "").strip() != eq_props:
        fails.append(f"{slug}: endQuestion differs between props and brief")
    if eq_props and eq_props not in caption:
        warns.append(f"{slug}: endQuestion not found verbatim in caption")

    o = ORIG[slug]
    before = nums(o["props"]) | nums(o["caption"]) | nums(o["brief"] or {})
    after = nums(props) | nums(caption) | nums(brief or {})
    # Documented exception: slug D's authored pill value "4 تشرين1" was an
    # abbreviation that read as a broken token on screen; the copy pass expanded
    # it to "4 تشرين الأول". That removes a bare "1" that never denoted anything.
    # Documented exceptions: (d) the authored pill "4 تشرين1" was an abbreviation
    # that read as a broken token; expanding it to "4 تشرين الأول" removed a bare
    # "1" that never denoted anything. (e) the editorial gate ruled the beat-1
    # bigStat "0" — "zero licences held by unlicensed entities" — an invented
    # statistic and ordered it removed; the slug now says no figure was published.
    VANISH_OK = {f"{D}-d-asiad-japan-seven-sports": {"1"},
                 f"{D}-e-fake-investment-firms": {"0"}}
    invented = sorted(after - before)
    vanished = sorted((before - after) - VANISH_OK.get(slug, set()))
    if invented:
        fails.append(f"{slug}: NUMBER INVENTED by the copy pass — not in any source: {invented}")
    if vanished:
        fails.append(f"{slug}: SOURCED NUMBER VANISHED in the copy pass: {vanished}")

    print(f"  {slug:44s} [{tag}]  beats={len(props.get('beats',[]))} "
          f"sources={len(src) if isinstance(src,list) else '?'} "
          f"pops={len(brief.get('statPops',[])) if brief else '-'}")

print()
for w in warns:
    print(f"  WARN  {w}")
for f in fails:
    print(f"  FAIL  {f}")
print(f"\n{len(fails)} failures · {len(warns)} warnings")
sys.exit(1 if fails else 0)
