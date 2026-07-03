#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-07-03 slate
from each slug's finalized props.json. Hook + numbers + story-in-brief + sources + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-07-03"

TAGS = {
    "global-wildfire-record": ["#حرائق", "#المناخ", "#تغير_المناخ", "#النينيو", "#الأمازون"],
    "iraq-budget-freeze": ["#العراق", "#الموازنة", "#بغداد", "#اقتصاد_العراق", "#البرلمان"],
    "milkyway-dark-matter": ["#الفضاء", "#المادة_المظلمة", "#درب_التبانة", "#علوم", "#فلك"],
    "nba-free-agency-quake": ["#NBA", "#ليبرون_جيمس", "#كرة_السلة", "#يانيس", "#انتقالات"],
    "qatar-fdi-record": ["#قطر", "#الإمارات", "#استثمار", "#الخليج", "#اقتصاد"],
    "saudi-led-axis": ["#السعودية", "#الشرق_الأوسط", "#تحالفات", "#قطر", "#تركيا"],
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
