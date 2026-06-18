#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-18 slate
from each slug's polished props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-18"

TAGS = {
    "iraq-mosul-museum": ["#الموصل", "#العراق", "#متحف_الموصل", "#تراث", "#آثار", "#اللوفر", "#Mosul", "#Iraq", "#Heritage", "#Museum"],
    "iran-us-deal-signing": ["#إيران", "#أمريكا", "#سويسرا", "#اتفاق", "#الشرق_الأوسط", "#سلام", "#Iran", "#USA", "#Switzerland", "#Diplomacy"],
    "mammal-regeneration": ["#علوم", "#تجدد", "#طب", "#الثدييات", "#اكتشاف", "#خلايا", "#Science", "#Regeneration", "#Biology", "#Research"],
    "saudi-seha-hospital": ["#السعودية", "#صحة", "#رؤية_2030", "#طب_عن_بعد", "#مستشفى_صحة", "#تقنية", "#SaudiArabia", "#Health", "#Telemedicine", "#Vision2030"],
    "jwst-exoplanet-roasted": ["#فضاء", "#ناسا", "#جيمس_ويب", "#كوكب", "#فلك", "#اكتشاف", "#NASA", "#JWST", "#Exoplanet", "#Space"],
    "superconductor-leap": ["#علوم", "#فيزياء", "#توصيل_فائق", "#تكنولوجيا", "#السويد", "#حوسبة_كمومية", "#Science", "#Superconductivity", "#Physics", "#Quantum"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iraq-mosul-museum": "تراث وآثار",
    "iran-us-deal-signing": "الملف الإقليمي",
    "mammal-regeneration": "علوم وطب",
    "saudi-seha-hospital": "صحة الخليج",
    "jwst-exoplanet-roasted": "فضاء وفلك",
    "superconductor-leap": "علوم وتقنية",
}


def build(key, d):
    h = d["breaking"]["arabicHeadline"]
    beats = d["beats"]
    sources = " • ".join(s["name"] for s in d["sources"][:4])
    tags = " ".join(TAGS.get(key, []) + BASE)
    L = []
    L.append(h + ".")
    L.append("")
    L.append("الأرقام كما هي:")
    for b in beats:
        bs = b.get("bigStat", {})
        L.append(f"• {bs.get('value','')} — {bs.get('arabicLabel', b.get('label',''))}")
    L.append("")
    L.append("القصة باختصار:")
    for b in beats:
        L.append(f"• {b['arabicHeading']}")
    tick = d.get("arabicTicker", [])
    if tick and tick[-1].strip().endswith("؟"):
        L.append("")
        L.append(tick[-1].strip())
    L.append("")
    L.append(f"📍 المصادر: {sources}")
    L.append("")
    L.append(tags)
    L.append("")
    L.append("@photonect.news")
    L.append(f"سلسلة: {SERIES.get(key,'')}")
    L.append("إعداد وتحرير: فريق فوتونكت")
    return "\n".join(L) + "\n"


for key in TAGS:
    slug = f"{DATE}-{key}"
    p = ROOT / slug / ".meta" / "props.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    cap = build(key, d)
    (ROOT / slug / "caption.txt").write_text(cap, encoding="utf-8")
    print(f"caption: {slug} ({len(cap.splitlines())} lines)")
