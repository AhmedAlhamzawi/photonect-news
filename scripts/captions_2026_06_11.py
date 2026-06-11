#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-11 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-11"

TAGS = {
    "iraq-militia-disarmament": ["#العراق", "#بغداد", "#الحشد_الشعبي", "#حصر_السلاح", "#الفصائل", "#الزيدي", "#Iraq", "#Baghdad"],
    "sudan-elfasher-famine": ["#السودان", "#الفاشر", "#دارفور", "#كردفان", "#مجاعة", "#الدعم_السريع", "#Sudan", "#ElFasher"],
    "pancreatic-cancer-drug": ["#سرطان_البنكرياس", "#صحة", "#علاج", "#ASCO", "#طب", "#PancreaticCancer", "#Health", "#Oncology"],
    "gulf-ai-year": ["#السعودية", "#الذكاء_الاصطناعي", "#هيومين", "#علّام", "#تقنية", "#SaudiArabia", "#AI", "#Humain"],
    "deepsea-new-species": ["#المحيط", "#اكتشاف", "#علوم", "#أعماق_البحار", "#البرازيل", "#Ocean", "#DeepSea", "#Science"],
    "worldcup-2026-kickoff": ["#كأس_العالم", "#مونديال_2026", "#كرة_القدم", "#فيفا", "#رياضة", "#WorldCup2026", "#FIFA", "#Football"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iraq-militia-disarmament": "العراق اليوم",
    "sudan-elfasher-famine": "الملف الإقليمي",
    "pancreatic-cancer-drug": "صحة عالمية",
    "gulf-ai-year": "عالم التقنية",
    "deepsea-new-species": "علوم وطبيعة",
    "worldcup-2026-kickoff": "رياضة",
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
