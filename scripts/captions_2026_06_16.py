#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-16 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-16"

TAGS = {
    "iraq-world-cup-return": ["#العراق", "#كأس_العالم", "#أسود_الرافدين", "#كرة_القدم", "#النرويج", "#المونديال", "#Iraq", "#WorldCup", "#WorldCup2026", "#Football"],
    "fungi-underground-map": ["#علوم", "#الفطريات", "#البيئة", "#التربة", "#المناخ", "#اكتشاف", "#Science", "#Fungi", "#Mycorrhizal", "#Climate"],
    "g7-evian-summit": ["#مجموعة_السبع", "#إيفيان", "#فرنسا", "#أوكرانيا", "#دبلوماسية", "#قمة", "#G7", "#Évian", "#Ukraine", "#Diplomacy"],
    "glp1-diabetes-pill": ["#صحة", "#السكري", "#السمنة", "#دواء", "#تنحيف", "#حبة", "#Health", "#Diabetes", "#GLP1", "#WeightLoss"],
    "qatar-air-global-hub": ["#الخطوط_القطرية", "#الطيران", "#قطر", "#الخليج", "#سفر", "#اقتصاد", "#QatarAirways", "#Aviation", "#Gulf", "#Travel"],
    "stonehenge-altar-stone": ["#ستونهنج", "#آثار", "#اسكتلندا", "#تاريخ", "#اكتشاف", "#علوم", "#Stonehenge", "#Archaeology", "#Scotland", "#History"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iraq-world-cup-return": "العراق اليوم",
    "fungi-underground-map": "علوم وبيئة",
    "g7-evian-summit": "الملف الدولي",
    "glp1-diabetes-pill": "صحة عالمية",
    "qatar-air-global-hub": "اقتصاد الخليج",
    "stonehenge-altar-stone": "تاريخ وآثار",
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
