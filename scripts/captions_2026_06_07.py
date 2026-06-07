#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-07 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-07"

TAGS = {
    "iraq-zaidi-anticorruption": ["#العراق", "#علي_الزيدي", "#الفساد", "#النزاهة", "#بغداد", "#وزارة_النفط", "#Iraq", "#Baghdad"],
    "gaza-ceasefire-sixmonths": ["#غزة", "#فلسطين", "#الهدنة", "#وقف_إطلاق_النار", "#الشرق_الأوسط", "#Gaza", "#Palestine"],
    "french-open-andreeva": ["#أندريفا", "#رولان_غاروس", "#فرنسا_المفتوحة", "#تنس", "#FrenchOpen", "#RolandGarros", "#Andreeva", "#Tennis"],
    "iraq-fiscal-crisis": ["#العراق", "#الدينار_العراقي", "#الاقتصاد", "#البنك_المركزي", "#النفط", "#Iraq", "#IraqiDinar"],
    "roman-telescope": ["#ناسا", "#الفضاء", "#تلسكوب", "#علوم", "#الكواكب", "#NASA", "#Space", "#RomanTelescope"],
    "drc-ebola-emergency": ["#إيبولا", "#الكونغو", "#الصحة", "#منظمة_الصحة_العالمية", "#أوغندا", "#Ebola", "#Congo", "#WHO"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iraq-zaidi-anticorruption": "العراق اليوم",
    "iraq-fiscal-crisis": "اقتصاد العراق",
    "gaza-ceasefire-sixmonths": "الملف الفلسطيني",
    "french-open-andreeva": "رياضة عالمية",
    "roman-telescope": "علوم وفضاء",
    "drc-ebola-emergency": "صحة عالمية",
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
    # closing reader question from the last ticker line if it ends with ؟
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
