#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-05-29 slate
from each slug's props.json. Hook + 3 facts + why-it-matters + sources + hashtags.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-05-29"

# Per-slug extra hashtags (topic-specific) on top of the base set.
TAGS = {
    "iraq-electricity-collapse": ["#العراق", "#كهرباء_العراق", "#بغداد", "#الكهرباء", "#أزمة_الكهرباء"],
    "musk-spacex-ipo": ["#ايلون_ماسك", "#سبيس_إكس", "#اكتتاب", "#ستارشيب", "#xAI", "#SpaceX"],
    "worldcup-messi-ronaldo": ["#كأس_العالم", "#ميسي", "#رونالدو", "#المغرب", "#مونديال_2026", "#WorldCup2026"],
    "lebanon-ceasefire-brink": ["#لبنان", "#حزب_الله", "#سوريا", "#الشرع", "#هدنة"],
    "space-iss-fusion": ["#الفضاء", "#ناسا", "#الاندماج_النووي", "#المريخ", "#علوم", "#NASA"],
    "sudan-famine-year4": ["#السودان", "#دارفور", "#مجاعة", "#أزمة_إنسانية", "#Sudan"],
}
BASE_TAGS = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect"]


def build(slug_key, d):
    h = d["breaking"]["arabicHeadline"]
    beats = d["beats"]
    sources = "، ".join(s["name"] for s in d["sources"][:4])
    tags = " ".join(TAGS.get(slug_key, []) + BASE_TAGS)
    lines = []
    lines.append(h)                      # hook = headline (line 1)
    lines.append("")
    lines.append("الأرقام:")
    for b in beats:
        bs = b.get("bigStat", {})
        val = bs.get("value", "")
        lbl = bs.get("arabicLabel", b.get("label", ""))
        lines.append(f"• {val} — {lbl}")
    lines.append("")
    # why it matters = beat headings condensed
    lines.append("القصة باختصار:")
    for b in beats:
        lines.append(f"• {b['arabicHeading']}")
    lines.append("")
    lines.append(f"المصادر: {sources}")
    lines.append("")
    lines.append(tags)
    lines.append("")
    lines.append("@photonect.news")
    return "\n".join(lines) + "\n"


for slug_key, tags in TAGS.items():
    slug = f"{DATE}-{slug_key}"
    p = ROOT / slug / ".meta" / "props.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    cap = build(slug_key, d)
    (ROOT / slug / "caption.txt").write_text(cap, encoding="utf-8")
    print(f"caption: {slug} ({len(cap.split(chr(10)))} lines)")
