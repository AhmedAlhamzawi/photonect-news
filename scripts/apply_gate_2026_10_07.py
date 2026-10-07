#!/usr/bin/env python3
"""Apply Opus gate pass-1 fixes to the 2026-10-07 slate (exact-string replacements; fails loudly if a target is missing).
Warning 1 (swap Rudaw's 130k budget baseline for Shafaq's 132k previous sale rate) was NOT applied: our 10-05 reel aired
the previous official rate as 131,000 (964), so airing 132,000 would contradict our own archive."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
D = "2026-10-07"
FIX = [  # (slug, file, old, new)
 ("d-salahaldin-56k-receipts", ".meta/v11-brief.json", " · بغداد اليوم — 7 تشرين", " — 7 تشرين"),
 ("d-salahaldin-56k-receipts", "caption.txt", "، شبكة 964، بغداد اليوم (7", "، شبكة 964 (7"),
 ("b-dollar-168500-bourse", ".meta/v11-brief.json", "شكد اشتريت الدولار اليوم؟", "اشتريت دولار اليوم؟"),
 ("b-dollar-168500-bourse", ".meta/props.json", "شكد اشتريت الدولار اليوم؟", "اشتريت دولار اليوم؟"),
 ("b-dollar-168500-bourse", "caption.txt", "شكد اشتريت الدولار اليوم؟", "اشتريت دولار اليوم؟"),
 ("b-dollar-168500-bourse", ".meta/v11-brief.json", "الرسمي 152 ألف.. والبورصة 168,500", "الرسمي 152 ألف.. والبورصة صباحاً 168,500"),
 ("b-dollar-168500-bourse", ".meta/v11-brief.json", "بستة عشر ألفاً وخمسمئة دينار.", "بستة عشر ألفاً وخمسمئة دينار لكل مئة دولار."),
 ("b-dollar-168500-bourse", ".meta/v11-brief.json", "دينار فوق السعر الرسمي الجديد (محتسب)", "دينار لكل 100 دولار فوق السعر الرسمي (محتسب)"),
 ("c-basra-crude-china", ".meta/props.json", "مصافي الصين تعوّض النفط الإيراني بخام البصرة", "مصافٍ صينية مستقلة تعوّض النفط الإيراني بخام البصرة"),
 ("c-basra-crude-china", ".meta/props.json", "ولم تصدّر إيران خاماً خلال الشهر.", "وتراجع خامها المخزّن على ناقلات إلى 45 مليون برميل."),
 ("c-basra-crude-china", ".meta/props.json", "وكبلر: إيران بلا صادرات خام بأيلول", "المخزون العائم: 45 مليون برميل"),
 ("d-salahaldin-56k-receipts", ".meta/v11-brief.json", "النزاهة: 56 ألف وصل مرور.. وعقيدان موقوفان", "النزاهة: +56 ألف وصل مرور.. وعقيدان موقوفان"),
 ("d-salahaldin-56k-receipts", ".meta/v11-brief.json", "عميداً وعقيدين لعدم التدقيق،", "عميداً وعقيدين بسبب ما تقول الهيئة إنه عدم تدقيق،"),
 ("e-dust-139-cases", ".meta/v11-brief.json", "أدوية الحساسية والربو والأوكسجين.", "أدوية الحساسية والربو، والأوكسجين لمن احتاج إليه."),
 ("e-dust-139-cases", ".meta/v11-brief.json", "المصادر: صحة النجف عبر شفق نيوز · شبكة 964 · بغداد اليوم — 6 و7 تشرين الأول 2026",
  "المصادر: صحة النجف والأنواء الجوية ومرصد العراق الأخضر عبر شفق نيوز · شبكة 964 — 6 و7 تشرين الأول 2026"),
]
bad = 0
for slug, fn, old, new in FIX:
    f = P / f"{D}-{slug}" / fn
    s = f.read_text(encoding="utf-8")
    if old not in s:
        print(f"MISSING  {slug}/{fn}: {old[:50]}"); bad += 1; continue
    s = s.replace(old, new)
    if fn.endswith(".json"): json.loads(s)
    f.write_text(s, encoding="utf-8"); print(f"ok       {slug}/{fn}: {new[:50]}")
sys.exit(1 if bad else 0)
# Follow-up trims applied by hand after this script (length limits): d voText «بسبب ما تقول الهيئة إنه عدم تدقيق» → «بتهمة عدم التدقيق»;
# c beat-2 body rewritten to «كبلر: واردات الصين من النفط الإيراني تراجعت في أيلول إلى 590 ألف برميل يومياً، الأدنى منذ كانون الثاني 2023، ومخزونها العائم إلى 45 مليون برميل.»
# Gate pass 2 (applied by hand): c beat-2 «ومخزونها العائم» → «والمخزون الإيراني العائم»; b voText splits the shop-suspension clause
# out under «وبحسب شفق نيوز»; c caption credits the premium to Reuters only; e hero (Mexico City flag) and c hero (named tanker) swapped.
