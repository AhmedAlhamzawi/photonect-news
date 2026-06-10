#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-10 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-10"

TAGS = {
    "artemis-3-moon-crew": ["#أرتميس", "#ناسا", "#القمر", "#الفضاء", "#رواد_الفضاء", "#NASA", "#ArtemisIII", "#Moon"],
    "baghdad-power-crisis": ["#العراق", "#بغداد", "#الكهرباء", "#أزمة_الكهرباء", "#الخدمات", "#الموازنة", "#Iraq", "#Baghdad"],
    "lebanon-israel-ceasefire": ["#لبنان", "#إسرائيل", "#الهدنة", "#حزب_الله", "#الجيش_اللبناني", "#الشرق_الأوسط", "#Lebanon", "#Ceasefire"],
    "obesity-drug-retatrutide": ["#السمنة", "#ريتاتروتيد", "#الصحة", "#السكري", "#إنقاص_الوزن", "#Obesity", "#Retatrutide", "#Health"],
    "siri-ai-wwdc": ["#آبل", "#سيري", "#الذكاء_الاصطناعي", "#WWDC", "#آيفون", "#تقنية", "#Apple", "#Siri", "#WWDC2026"],
    "tony-awards-2026": ["#جوائز_توني", "#برودواي", "#مسرح", "#ثقافة", "#شميغادون", "#TonyAwards", "#Broadway", "#Theatre"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "artemis-3-moon-crew": "علوم وفضاء",
    "baghdad-power-crisis": "العراق اليوم",
    "lebanon-israel-ceasefire": "الملف الإقليمي",
    "obesity-drug-retatrutide": "صحة عالمية",
    "siri-ai-wwdc": "عالم التقنية",
    "tony-awards-2026": "ثقافة وفنون",
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
