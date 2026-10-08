#!/usr/bin/env python3
"""2026-10-08 Opus gate pass 2 fixes.
b BLOCKER: the 1,900 line omitted that the CBI rejected it and held 1,500 (source: CBI media director via 964).
d BLOCKER: d/broll_1 was a Turkish city highway — replaced with a meter close-up (place_images_2026_10_08.py).
Warnings: b hook/caption say the dip was a MORNING reading; d 10M pop label no longer repeats 'million'."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"

def rep(s, a, b):
    assert a in s, f"missing: {a}"
    return s.replace(a, b)

m = P / "2026-10-08-b-dollar-166800-1900"
b = json.loads((m / ".meta/v11-brief.json").read_text())
b["voText"] = rep(b["voText"],
  "لتأمين رواتب أكثر من تسعة ملايين موظف، وإن أرقاماً طُرحت وصلت إلى ألف وتسعمئة دينار للدولار.",
  "لتأمين الرواتب، وإن أرقاماً طُرحت وصلت إلى ألف وتسعمئة دينار للدولار، لكن البنك أصرّ على ألف وخمسمئة.")
b["hookHeadline"] = "الدولار نزل صباحاً.. وشنو قصة 1,900؟"
for s in b["statPops"]:
    if s["value"] == "1,900": s["label"] = "دينار للدولار — رقم طُرح ورفضه المركزي"
(m / ".meta/v11-brief.json").write_text(json.dumps(b, ensure_ascii=False, indent=1))
p = json.loads((m / ".meta/props.json").read_text())
bt = p["beats"][2]
bt["arabicBody"] = "مدير إعلام البنك المركزي حيدر غازي لقناة دجلة: أرقام طُرحت وصلت 1,900، لكن البنك أصرّ على 1,500. والحكومة استهلكت أجزاءً غير هيّنة من الاحتياطي للرواتب."
bt["bigStat"]["arabicLabel"] = "دينار للدولار — رقم طُرح ورفضه المركزي"
p["breaking"]["arabicHeadline"] = "الدولار نزل صباحاً.. والمركزي: 1,900 طُرح ورفضناه"
p["arabicTicker"] = [rep(t, "وصلت إلى 1,900 دينار للدولار", "وصلت إلى 1,900 لكن البنك أصرّ على 1,500") if "1,900" in t else t for t in p["arabicTicker"]]
(m / ".meta/props.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
cp = m / "caption.txt"
cp.write_text(rep(cp.read_text(), "البورصة نزلت شوية ثاني يوم", "البورصة نزلت شوية صباح الخميس"))

m = P / "2026-10-08-d-karbala-meter-bribe"
b = json.loads((m / ".meta/v11-brief.json").read_text())
for s in b["statPops"]:
    if s["value"] == "10M": s["label"] = "دينار — قيمة الغرامة"
(m / ".meta/v11-brief.json").write_text(json.dumps(b, ensure_ascii=False, indent=1))
print("✓ gate 2 fixes applied")
