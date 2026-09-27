#!/usr/bin/env python3
"""Apply Opus editorial-gate pass-1 + pass-2 fixes to the 2026-09-27 slate. Every replacement must hit."""
import sys
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
FILES = [".meta/props.json", ".meta/v11-brief.json", "caption.txt"]
FIX1 = {
 "a-pension-bribes-nazaha": [
  ("رشوة في دوائر التقاعد؟ النزاهة تضبط متهمين في بغداد والأنبار", "النزاهة تضبط متهمين بالرشوة في التقاعد والتأمين ببغداد والأنبار"),
  ("الأول مدير القسم القانوني في شركة التأمين الوطنية، لقاء تجديد عقد تأجير قطعتي أرض في الديوانية. والثاني موظف في هيئة التقاعد، قسم السجناء السياسيين، تسلّم مليوني دينار",
   "الأول مدير القسم القانوني في شركة التأمين الوطنية، ضُبط بحسب الهيئة لقاء تجديد عقد تأجير قطعتي أرض في الديوانية. والثاني موظف في هيئة التقاعد، قسم السجناء السياسيين، تقول الهيئة إنه تسلّم مليوني دينار"),
  ('"3 مليون"', '"3 ملايين"'),
  ("دينار لرفع حجز تقاعد — الأنبار", "دينار لرفع حجز عن حصة تقاعدية — الأنبار"),
 ],
 "b-dollar-155250-shipment": [
  ("سعر الدولار اليوم في العراق.. ليش نزل بالبورصة صباح الأحد؟", "سعر الدولار اليوم في العراق.. نزول في بورصة بغداد صباح الأحد"),
  ("الدولار نزل تحت 156 ألف.. شنو السبب؟", "الدولار نزل تحت 156 ألف.. والحكومة تتحدث عن شحنة"),
 ],
 "c-us-warning-iraq-airports": [
  ("مطارات أوقفت الاستقبال", "بغداد والبصرة والنجف (964)"),
 ],
 "d-electricity-52-percent-lost": [
  ("تلتها بغداد الصدر بخمسة وستين", "تلتها توزيع الصدر في بغداد بخمسة وستين"),
 ],
 "e-hajj-lottery-2030": [
  ('"matchWord": "سبع"', '"matchWord": "جهات"'),
 ],
}
FIX2 = {
 "a-pension-bribes-nazaha": [
  ("ضُبط بحسب الهيئة لقاء تجديد", "ضُبط بحسب الهيئة يتسلّم رشوة لقاء تجديد"),
 ],
 "c-us-warning-iraq-airports": [
  ('"value": "3",\n        "label": "Airports halting Iranian flights, per 964",\n        "arabicLabel": "بغداد والبصرة والنجف (964)"',
   '"value": "36",\n        "label": "Iranian aviation entities under US Treasury sanctions (Sep 8), per Shafaq",\n        "arabicLabel": "جهة طيران إيرانية معاقبة"'),
  ("طالب في إيران\"", "طالب في إيران (نواب)\""),
  ("شبكة 964: مطارات بغداد والبصرة والنجف", "شبكة 964: مطارات بينها بغداد والبصرة والنجف"),
 ],
 "d-electricity-52-percent-lost": [
  ("تلتها توزيع الصدر", "تلاها توزيع الصدر"),
  ("عبر شفق نيوز والمستقلة\n", "عبر شفق نيوز والمستقلة (27 أيلول 2026)\n"),
 ],
 "e-hajj-lottery-2030": [
  ("من 2027 التكميلي حتى 2030: 7 جهات حكومية وقضاة أشرفوا على القرعة، والهيئة تقول إنها استبعدت أسماء وهمية.",
   "من 2027 التكميلي حتى 2030: بحسب الهيئة، 7 جهات حكومية وقضاة أشرفوا على القرعة، واستُبعدت أسماء وهمية."),
 ],
}
FIX = FIX2 if "--pass2" in sys.argv else FIX1
miss = 0
for slug, pairs in FIX.items():
    d = P / f"2026-09-27-{slug}"
    texts = {f: (d / f).read_text(encoding="utf-8") for f in FILES if (d / f).exists()}
    for old, new in pairs:
        n = sum(t.count(old) for t in texts.values())
        if not n:
            print(f"MISS {slug}: {old}"); miss += 1; continue
        for f in texts: texts[f] = texts[f].replace(old, new)
        print(f"ok   {slug}: {n}x {old[:40]}")
    for f, t in texts.items(): (d / f).write_text(t, encoding="utf-8")
sys.exit(1 if miss else 0)
