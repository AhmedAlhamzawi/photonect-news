#!/usr/bin/env python3
"""Apply Opus gate pass-1 findings (2026-10-05) across props.json / v11-brief.json / caption.txt."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
FIX = {
 "2026-10-05-a-package-3-5-trillion": [("إلى مصرفي التجارة والصناعي", "لسيولة المصرف العراقي للتجارة والمصرف الصناعي")],
 "2026-10-05-b-dollar-159050-160k": [("سعر الدولار اليوم في بغداد وأربيل والبصرة.. شكد صار بالبورصة؟", "سعر الدولار اليوم في بغداد.. شكد صار بالبورصة؟")],
 "2026-10-05-c-iraqi-line-umm-qasr": [("أول رحلة: من جبل علي إلى أم قصر", "الهدف: دعم التجارة عبر الموانئ العراقية")],
 "2026-10-05-d-diwaniya-141-cards": [("مئة وواحداً وأربعين بطاقة", "مئة وإحدى وأربعين بطاقة")],
 "2026-10-05-e-palm-weevil-7-provinces": [
   ("لذلك تُعقَّم ثلاثة أيام", "لذلك تُعقَّم الفسائل ثلاثة أيام"),
   ("تتغذى داخل الجذع، وقد تبدو النخلة سليمة في البداية", "تتغذى داخل الجذع، فيما يقول مختصون إن النخلة قد تبدو سليمة في البداية"),
   ("ثماني وعشرون نخلة", "ثمانٍ وعشرون نخلة")],
}
for slug, pairs in FIX.items():
    files = [P/slug/".meta/props.json", P/slug/".meta/v11-brief.json", P/slug/"caption.txt"]
    for old, new in pairs:
        hits = 0
        for f in files:
            if f.exists():
                t = f.read_text(encoding="utf-8")
                if old in t:
                    f.write_text(t.replace(old, new), encoding="utf-8"); hits += t.count(old)
        print(f"{slug[11:]:30s} {'OK ' if hits else 'MISS'} x{hits}: {old[:40]}")
