#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-13 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-13"

TAGS = {
    "iraq-kurdistan-oil-restart": ["#العراق", "#كردستان", "#النفط", "#الصادرات", "#بغداد", "#الزيدي", "#Iraq", "#Kurdistan", "#Oil"],
    "gaza-phase-two": ["#غزة", "#وقف_إطلاق_النار", "#إعادة_الإعمار", "#فلسطين", "#الشرق_الأوسط", "#Gaza", "#Ceasefire", "#Palestine"],
    "saudi-vision2030-nextphase": ["#السعودية", "#رؤية_2030", "#الاقتصاد", "#السياحة", "#الخليج", "#SaudiArabia", "#Vision2030", "#Economy"],
    "juno-neutrino-result": ["#فيزياء", "#علوم", "#النيوترينو", "#جونو", "#الصين", "#Science", "#Physics", "#Neutrino", "#JUNO"],
    "stanford-cartilage-regrow": ["#صحة", "#طب", "#الغضروف", "#التهاب_المفاصل", "#ستانفورد", "#Health", "#Cartilage", "#Stanford"],
    "nba-finals-knicks": ["#كرة_السلة", "#NBA", "#نيكس", "#نهائي_NBA", "#رياضة", "#Knicks", "#NBAFinals", "#Brunson"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iraq-kurdistan-oil-restart": "العراق اليوم",
    "gaza-phase-two": "الملف الإقليمي",
    "saudi-vision2030-nextphase": "اقتصاد الخليج",
    "juno-neutrino-result": "علوم وطبيعة",
    "stanford-cartilage-regrow": "صحة عالمية",
    "nba-finals-knicks": "رياضة",
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
