#!/usr/bin/env python3
"""Apply Opus editorial-gate pass-1 fixes to the 2026-09-29 slate. Every replacement must hit."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
D = "2026-09-29"
TXT = {
 "a-mp-farman-28-billion": {
  ".meta/v11-brief.json": [("وبحسب شفق نيوز، سبق ذلك حكمان بسجن نائبتين في الثالث والعشرين من أيلول.", "وبحسب شفق نيوز، أعلنت الهيئة في الثالث والعشرين من أيلول حكمين بسجن نائبتين."),
                           ("نحو أحد عشر مليار وثمانمئة مليون دينار", "نحو أحد عشر ملياراً وثمانمئة مليون دينار")],
  "caption.txt": [("حكم سجن نائب حالي", "حكم بسجن نائب حالي"), ("سبقه بستة أيام حكمان بسجن نائبتين", "سبقه في 23 أيلول حكمان بسجن نائبتين")],
 },
 "b-dollar-157000-gold-up": {
  ".meta/v11-brief.json": [("المصادر: شفق نيوز · شبكة 964 — 29 أيلول 2026", "المصادر: شفق نيوز — 29 أيلول 2026")],
  "caption.txt": [("المصادر: شفق نيوز، شبكة 964 (29 أيلول 2026)", "المصادر: شفق نيوز (29 أيلول 2026)")],
 },
 "c-zaidi-trump-oil-firms": {
  "caption.txt": [("(28-29 أيلول 2026)", "(28 أيلول 2026)")],
  ".meta/props.json": [("بعد استقبال جماعي للقادة في الأمم المتحدة،", "بعد استقبال جماعي أقامه لقادة اجتماعات الأمم المتحدة،"),
                       ("في اجتماع ناقش أيضاً حظر الطيران الإيراني، بغياب المالكي والعامري.", "في اجتماع خُصص لحظر الطيران الإيراني، غاب عنه المالكي والعامري لالتزامات خاصة."),
                       ('"arabicLabel": "جهة طيران إيرانية معاقَبة"', '"arabicLabel": "جهة مرتبطة بالطيران الإيراني (الخزانة الأميركية)"'),
                       ('"arabicLabel": "ملفات حسب العبودي"', '"arabicLabel": "لقاء بعد استقبال جماعي (العبودي)"'),
                       ('"arabicKicker": "العراق وأمريكا"', '"arabicKicker": "صورة أرشيفية · تموز"')],
 },
 "d-customs-transfers-1-october": {
  ".meta/v11-brief.json": [("بحسب مدير هيئة الكمارك ثامر قاسم داود لشبكة تسعة ستة أربعة.", "بحسب مدير هيئة الكمارك ثامر قاسم داود في حديث لقناة دجلة تابعته شبكة تسعة ستة أربعة.")],
 },
 "e-kurdistan-seats-1250": {
  "caption.txt": [("مقاعد أكثر للطلبة وعائلاتهم", "مقاعد أكثر للطلبة من الجانبين"), ("#القبول_المركزي", "#الجامعات_العراقية")],
 },
}
miss = 0
for slug, files in TXT.items():
    for f, reps in files.items():
        p = P / f"{D}-{slug}" / f; s = p.read_text(encoding="utf-8")
        for a, b in reps:
            if s.count(a) != 1: print(f"MISS/{s.count(a)}x {slug}/{f}: {a[:60]}"); miss += 1; continue
            s = s.replace(a, b)
        p.write_text(s, encoding="utf-8")
# c: structural edits on beat 1 bigStat, duplicate chip, englishSubhead
p = P / f"{D}-c-zaidi-trump-oil-firms/.meta/props.json"; d = json.loads(p.read_text(encoding="utf-8"))
b1 = d["beats"][0]
assert b1["bigStat"]["value"] == "4", b1["bigStat"]
b1["bigStat"]["value"] = "منفرد"
b1["bigStat"]["label"] = "One-on-one meeting after a group reception, per spokesman al-Aboudi (Dijla via 964)"
for st in b1["supportingStats"]:
    if st["value"] == "لقاء منفرد": st["label"], st["value"] = "من الملفات", "الفساد والسلاح"
d["breaking"]["englishSubhead"] = "ARCHIVE PHOTO: WHITE HOUSE, 14 JULY 2026 | NEW YORK MEETING PER GOVT SPOKESMAN"
p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("misses:", miss); sys.exit(1 if miss else 0)
