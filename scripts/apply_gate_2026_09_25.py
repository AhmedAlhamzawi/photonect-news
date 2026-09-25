#!/usr/bin/env python3
"""Apply Opus editorial-gate pass-1 fixes to the 2026-09-25 slate. Every replacement must hit."""
import sys
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
FILES = [".meta/props.json", ".meta/v11-brief.json", "caption.txt"]
FIX = {
 "a-oil-theft-500-million": [
  ("نصف مليار دينار شهرياً من خرقين بأنبوب", "التحقيقات: نصف مليار دينار شهرياً من أنبوب"),
  ('"500M"', '"500 مليون"'),
  ("أُحيلوا للقضاء", "أُحيلوا للجهات المختصة"),
 ],
 "b-dollar-friday-spread": [
  ('"kicker": "الدولار اليوم"', '"kicker": "آخر سعر قبل العطلة"'),
  ('"arabicKicker": "الدولار اليوم"', '"arabicKicker": "آخر سعر قبل العطلة"'),
 ],
 "c-najaf-iran-flights": [
  ("وعلّق مطارا أربيل والسليمانية رحلاتهما أيضاً.", "وتوقفت رحلات إيران أيضاً في مطاري أربيل والسليمانية."),
  ("إن بغداد أبلغت طهران بالحظر، وستناقشه مع واشنطن.", "إن بغداد أبلغت طهران بالحظر، وستناقش العقوبات الأمريكية على الطيران الإيراني مع واشنطن."),
  ("ومسافرون عالقون عند البوابات", "ومسافرون عالقون عند بوابة النجف"),
  ("ومرة للطريق البري", "ومرة للنقل البري"),
 ],
 "d-somo-oil-buyers": [
  ('"label": "السبب"', '"label": "المؤشر"'),
 ],
 "e-syria-petrol-baniyas": [
  ("أول بنزين للعراق ينطلق من موانئ سوريا", "أول شحنة بنزين للعراق عبر موانئ سوريا"),
  ("ناقلات فرّغت في الموانئ السورية، وقوافل صهاريج", "ناقلة فرّغت حمولتها في الموانئ السورية واثنتان تنتظران، وقوافل صهاريج"),
  ("وبدأ التحميل في الثاني والعشرين من أيلول بقافلتين", "وبحسب الشركة، بدأ التحميل في الثاني والعشرين من أيلول بقافلتين"),
 ],
}
miss = 0
for slug, pairs in FIX.items():
    d = P / f"2026-09-25-{slug}"
    texts = {f: (d / f).read_text(encoding="utf-8") for f in FILES if (d / f).exists()}
    for old, new in pairs:
        n = sum(t.count(old) for t in texts.values())
        if not n:
            print(f"MISS {slug}: {old}"); miss += 1; continue
        for f in texts: texts[f] = texts[f].replace(old, new)
        print(f"ok   {slug}: {n}x {old[:40]}")
    for f, t in texts.items(): (d / f).write_text(t, encoding="utf-8")
sys.exit(1 if miss else 0)
