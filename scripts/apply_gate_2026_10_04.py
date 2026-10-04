#!/usr/bin/env python3
"""Apply Opus gate pass-1 warnings to the 2026-10-04 slate (no blockers were raised)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
def edit(slug, fn, f):
    p = P / f"2026-10-04-{slug}" / fn
    s = p.read_text(encoding="utf-8"); n = f(s)
    assert n != s, f"no change: {slug}/{fn}"
    p.write_text(n, encoding="utf-8")
def rep(a, b):
    def f(s):
        assert a in s, f"missing: {a[:40]}"
        return s.replace(a, b)
    return f
def chain(*fs):
    def g(s):
        for f in fs: s = f(s)
        return s
    return g

# a — endQuestion insinuated salary delay; make hook claim derivable in VO
OLDQ, NEWQ = "راتبك لشهر أيلول وصل بموعده؟", "تستلم راتب أو إعانة من الدولة؟"
for fn in (".meta/props.json", ".meta/v11-brief.json", "caption.txt"):
    edit("a-deficit-26-trillion", fn, rep(OLDQ, NEWQ))
edit("a-deficit-26-trillion", ".meta/v11-brief.json", rep("والرواتب وحدها تخطّت خمسة وثلاثين تريليوناً.",
     "والرواتب وحدها تخطّت خمسة وثلاثين تريليوناً، والرعاية الاجتماعية نحو ستة عشر تريليوناً."))
# b — attribute gold in VO
edit("b-dollar-157950-gold", ".meta/v11-brief.json", rep("أما الذهب، فارتفع سعر بيع مثقال", "أما الذهب، فبحسب شفق نيوز ارتفع سعر بيع مثقال"))
# c — caption hook, pill label, pill clip
edit("c-toman-270950-record", "caption.txt", lambda s: s.replace(s.splitlines()[0], "سعر الدولار في إيران اليوم والتومان يواصل الهبوط", 1))
def c_props(s):
    d = json.loads(s); st = d["beats"][2]["supportingStats"]
    for x in st:
        if x["label"] == "التضخم السنوي": x["label"] = "متوسط التضخم"
        if "27,095,000" in x["value"]: x["label"], x["value"] = "تومان لـ100$ (محتسب)", "27,095,000"
    return json.dumps(d, ensure_ascii=False, indent=1)
edit("c-toman-270950-record", ".meta/props.json", c_props)
# d — hook
edit("d-ishaqi-wheat-bribe", ".meta/v11-brief.json", rep("النزاهة: مبالغ مقابل استلام الحنطة", "النزاهة تتهم موظفاً بمبالغ مقابل الحنطة"))
# e — latent ticker wording
edit("e-hajj-lottery-5-5-percent", ".meta/props.json", rep("حصص ثابتة", "حصص بحسب الهيئة"))
print("gate-1 fixes applied")
# a: trimmed «الاقتصادي» from VO to 85 words (applied inline after gate-1)
