#!/usr/bin/env python3
"""Build ready-to-paste Arabic IG captions (caption.txt) for the 2026-06-22 slate
from each slug's props.json. Hook + numbers + story-in-brief + sources + hashtags.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-22"

TAGS = {
    "iraq-worldcup-france": ["#العراق", "#كأس_العالم", "#أسود_الرافدين", "#فرنسا", "#مونديال_2026"],
    "iran-us-switzerland-talks": ["#إيران", "#أمريكا", "#لبنان", "#سويسرا", "#الشرق_الأوسط"],
    "iraq-militia-disarmament": ["#العراق", "#حصر_السلاح", "#بغداد", "#الفصائل", "#الزيدي"],
    "gcc-grand-tours-visa": ["#الخليج", "#تأشيرة_موحدة", "#سكة_الخليج", "#سياحة", "#مجلس_التعاون"],
    "pancreas-cancer-pill": ["#صحة", "#سرطان_البنكرياس", "#دواء", "#علوم", "#طب"],
    "coral-resilient-reefs": ["#بيئة", "#الشعاب_المرجانية", "#مناخ", "#المحيطات", "#علوم"],
}
BASE_TAGS = ["#فوتونكت", "#أخبار", "#الشرق_الأوسط", "#photonect"]


def build(slug_key, d):
    h = d["breaking"]["arabicHeadline"]
    beats = d["beats"]
    sources = "، ".join(s["name"] for s in d["sources"][:4])
    tags = " ".join(TAGS.get(slug_key, []) + BASE_TAGS)
    lines = []
    lines.append(h)
    lines.append("")
    lines.append("الأرقام:")
    for b in beats:
        bs = b.get("bigStat", {})
        val = bs.get("value", "")
        lbl = bs.get("arabicLabel", b.get("label", ""))
        lines.append(f"• {val} — {lbl}")
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
