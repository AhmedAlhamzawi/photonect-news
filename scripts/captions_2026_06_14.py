#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-14 slate
from each slug's props.json. Hook + الأرقام + القصة باختصار + المصادر + hashtags."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-14"

TAGS = {
    "iraq-government-cabinet": ["#العراق", "#بغداد", "#الحكومة", "#البرلمان", "#الزيدي", "#الموازنة", "#Iraq", "#Baghdad", "#Government"],
    "lenacapavir-hiv-shot": ["#صحة", "#الإيدز", "#الوقاية", "#لیناكابافير", "#جنوب_أفريقيا", "#منظمة_الصحة", "#Health", "#HIV", "#Lenacapavir"],
    "syria-reconstruction": ["#سوريا", "#إعادة_الإعمار", "#التطبيع", "#دمشق", "#الشرع", "#الشرق_الأوسط", "#Syria", "#Reconstruction", "#Damascus"],
    "jwst-sleeping-giant": ["#علوم", "#فضاء", "#ثقب_أسود", "#جيمس_ويب", "#فلك", "#الكون", "#Science", "#Space", "#BlackHole", "#JWST"],
    "gcc-unified-visa": ["#الخليج", "#تأشيرة_موحدة", "#مجلس_التعاون", "#سياحة", "#سفر", "#شنغن_الخليج", "#Gulf", "#GCC", "#Travel", "#Visa"],
    "nhl-stanley-cup-final": ["#هوكي", "#NHL", "#كأس_ستانلي", "#كارولينا", "#فيغاس", "#رياضة", "#Hockey", "#StanleyCup", "#NHLFinal"],
}
BASE = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect", "#photonectnews"]
SERIES = {
    "iraq-government-cabinet": "العراق اليوم",
    "lenacapavir-hiv-shot": "صحة عالمية",
    "syria-reconstruction": "الملف الإقليمي",
    "jwst-sleeping-giant": "علوم وفضاء",
    "gcc-unified-visa": "اقتصاد الخليج",
    "nhl-stanley-cup-final": "رياضة",
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
