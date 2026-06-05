#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-05 slate
from each slug's props.json. Hook + numbers + story-in-brief + sources + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-05"

TAGS = {
    "iraq-power-revenue": ["#العراق", "#كهرباء_العراق", "#بغداد", "#الكهرباء", "#الموازنة"],
    "sudan-kordofan-offensive": ["#السودان", "#كردفان", "#الجيش_السوداني", "#الدعم_السريع", "#دارفور"],
    "pancreatic-cancer-drug": ["#سرطان_البنكرياس", "#طب", "#علاج", "#صحة", "#اختراق_طبي"],
    "ai-universal-vaccine": ["#لقاح", "#الذكاء_الاصطناعي", "#كورونا", "#كامبريدج", "#علوم", "#صحة"],
    "worldcup-2026-kickoff": ["#كأس_العالم", "#مونديال_2026", "#المغرب", "#السعودية", "#WorldCup2026"],
    "gulf-nonoil-economy": ["#الخليج", "#الإمارات", "#السعودية", "#اقتصاد", "#تنويع_اقتصادي"],
}
BASE_TAGS = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect"]


def build(slug_key, d):
    h = d["breaking"]["arabicHeadline"]
    beats = d["beats"]
    sources = "، ".join(s["name"] for s in d["sources"][:4])
    tags = " ".join(TAGS.get(slug_key, []) + BASE_TAGS)
    lines = [h, "", "الأرقام:"]
    for b in beats:
        bs = b.get("bigStat", {})
        lines.append(f"• {bs.get('value','')} — {bs.get('arabicLabel', b.get('label',''))}")
    lines.append("")
    lines.append("القصة باختصار:")
    for b in beats:
        lines.append(f"• {b['arabicHeading']}")
    lines += ["", f"المصادر: {sources}", "", tags, "", "@photonect.news"]
    return "\n".join(lines) + "\n"


for slug_key in TAGS:
    slug = f"{DATE}-{slug_key}"
    p = ROOT / slug / ".meta" / "props.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    cap = build(slug_key, d)
    (ROOT / slug / "caption.txt").write_text(cap, encoding="utf-8")
    print(f"caption: {slug} ({len(cap.splitlines())} lines)")
