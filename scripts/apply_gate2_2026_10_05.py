#!/usr/bin/env python3
"""Apply Opus gate pass-2 findings (2026-10-05). a/hero swapped (Soviet roubles -> Pexels 35827231) in place_images."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
FIX = {
 "2026-10-05-a-package-3-5-trillion": [("لمصرفي التجارة العراقي والصناعي", "للمصرف العراقي للتجارة والمصرف الصناعي")],
 "2026-10-05-c-iraqi-line-umm-qasr": [('"label": "الحمولة"', '"label": "النقل"'),
   ("آخر رحلات الشحن العراقية: منتصف الستينيات", "آخر رحلات الشحن العراقية بالمنطقة: منتصف الستينيات"),
   ("والعودة بقرار وزارة النقل", "والعودة بتوجيه من وزير النقل")],
 "2026-10-05-d-diwaniya-141-cards": [('"hookHeadline": "141 ماستر كارد بحوزة موظفَين"', '"hookHeadline": "النزاهة: 141 ماستر كارد بحوزة موظفَين"'),
   ("إنها ضبطت الاثنين موظفَين", "إنها ضبطت موظفَين"),
   ("141 بطاقة ماستر كارد.. لماذا بحوزتهما؟", "141 بطاقة ماستر كارد بحوزة الموظفَين")],
 "2026-10-05-e-palm-weevil-7-provinces": [("وفي بؤرة البو منيثم أصيبت", "وفي بؤرة البو منيثم، بحسب الحداد، أصيبت"),
   ("الحداد: اليرقة تتغذى داخل جذع النخلة وقد تبدو الشجرة سليمة في البداية", "الحداد: اليرقة تتغذى داخل جذع النخلة، ومختصون: قد تبدو الشجرة سليمة في البداية")],
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
        print(f"{slug[11:]:30s} {'OK ' if hits else 'MISS'} x{hits}: {old[:45]}")
