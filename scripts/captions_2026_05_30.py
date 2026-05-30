#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-05-30 slate
from each slug's props.json. Hook + numbers + story-in-brief + sources + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-05-30"

TAGS = {
    "iraq-water-crisis": ["#العراق", "#الجفاف", "#دجلة", "#الفرات", "#أزمة_المياه", "#البصرة"],
    "gaza-seizure-70": ["#غزة", "#فلسطين", "#حماس", "#نتنياهو", "#هدنة_غزة"],
    "oil-worst-month": ["#النفط", "#برنت", "#أوبك", "#الأسواق", "#مضيق_هرمز", "#اقتصاد"],
    "neom-line-halt": ["#نيوم", "#ذا_لاين", "#السعودية", "#رؤية_2030", "#NEOM"],
    "syria-energy-deal": ["#سوريا", "#دمشق", "#الطاقة", "#إعمار_سوريا", "#الشرع"],
    "nasa-moonbase": ["#ناسا", "#القمر", "#الفضاء", "#بلو_أوريجن", "#أرتميس", "#NASA"],
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
        lines.append(f"• {bs.get('value','')} — {bs.get('arabicLabel', bs.get('label',''))}")
    lines.append("")
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


for slug_key in TAGS:
    slug = f"{DATE}-{slug_key}"
    p = ROOT / slug / ".meta" / "props.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    cap = build(slug_key, d)
    (ROOT / slug / "caption.txt").write_text(cap, encoding="utf-8")
    print(f"caption: {slug} ({len(cap.splitlines())} lines)")
