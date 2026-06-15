#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-15 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-15"

TAGS = {
    "iran-us-war-deal": ["#إيران", "#أميركا", "#الاتفاق", "#هرمز", "#الحرب", "#سويسرا", "#Iran", "#USA", "#Hormuz", "#Ceasefire"],
    "le-mans-toyota-win": ["#لومان", "#تويوتا", "#فيراري", "#سباق", "#تحمل", "#رياضة", "#LeMans", "#Toyota", "#Motorsport", "#WEC"],
    "iraq-water-crisis": ["#العراق", "#المياه", "#الجفاف", "#البصرة", "#الأهوار", "#المناخ", "#Iraq", "#Water", "#Drought", "#Climate"],
    "keck-planet-spins": ["#علوم", "#فضاء", "#كواكب", "#فلك", "#مرصد_كيك", "#اكتشاف", "#Science", "#Space", "#Exoplanets", "#Keck"],
    "markets-hormuz-reopen": ["#اقتصاد", "#النفط", "#الأسواق", "#برنت", "#هرمز", "#بورصة", "#Oil", "#Markets", "#Brent", "#Economy"],
    "smoking-drug-cytisinicline": ["#صحة", "#التدخين", "#الإقلاع", "#دواء", "#نيكوتين", "#الفيب", "#Health", "#Smoking", "#FDA", "#QuitSmoking"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iran-us-war-deal": "الملف الإقليمي",
    "le-mans-toyota-win": "رياضة",
    "iraq-water-crisis": "العراق اليوم",
    "keck-planet-spins": "علوم وفضاء",
    "markets-hormuz-reopen": "اقتصاد",
    "smoking-drug-cytisinicline": "صحة عالمية",
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
