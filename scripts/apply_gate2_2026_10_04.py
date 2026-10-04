#!/usr/bin/env python3
"""Apply Opus gate pass-2 warnings to the 2026-10-04 slate (no blockers)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
def edit(slug, fn, a, b):
    p = P / f"2026-10-04-{slug}" / fn
    s = p.read_text(encoding="utf-8")
    assert a in s, f"missing in {slug}/{fn}: {a[:40]}"
    p.write_text(s.replace(a, b), encoding="utf-8")
# a — accusative object in endQuestion (all surfaces)
for fn in (".meta/props.json", ".meta/v11-brief.json", "caption.txt"):
    edit("a-deficit-26-trillion", fn, "تستلم راتب أو إعانة", "تستلم راتباً أو إعانة")
# b — statPop label says sell
edit("b-dollar-157950-gold", ".meta/v11-brief.json", '"label": "دينار لمثقال الخليجي عيار 21"', '"label": "دينار بيعاً لمثقال الخليجي عيار 21"')
# c — pill clip + Darabi's exact title
edit("c-toman-270950-record", ".meta/props.json", "تومان لـ100$ (محتسب)", "لكل 100$ (محتسب)")
edit("c-toman-270950-record", ".meta/props.json", "مستشار المركزي مهدي دارابي", "مستشار محافظ المركزي مهدي دارابي")
edit("c-toman-270950-record", ".meta/props.json", "مستشار المركزي: هبوط مؤقت", "مستشار محافظ المركزي: هبوط مؤقت")
# d — hook clarity, "some sums", neutral pop label
edit("d-ishaqi-wheat-bribe", ".meta/v11-brief.json", "النزاهة تتهم موظفاً بمبالغ مقابل الحنطة", "النزاهة تتهم موظفاً بتقاضي مبالغ مقابل الحنطة")
edit("d-ishaqi-wheat-bribe", ".meta/v11-brief.json", "إنه اعترف بتسلّم المبالغ.", "إنه اعترف بتسلّم مبالغ مالية.")
edit("d-ishaqi-wheat-bribe", ".meta/v11-brief.json", "مادة الرشوة — قانون العقوبات", "المادة التي أُوقف وفقها")
# e — foundations
edit("e-hajj-lottery-5-5-percent", ".meta/v11-brief.json", "بعد حصص الإقليم والشهداء والسجناء والخدمات", "بعد حصص الإقليم ومؤسستي الشهداء والسجناء والخدمات")
print("gate-2 fixes applied")
