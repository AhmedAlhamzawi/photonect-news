#!/usr/bin/env python3
"""Apply the 2026-09-10 Opus editorial-gate blockers + selected nits (idempotent)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
def load(s, f): return json.loads((P / s / ".meta" / f).read_text(encoding="utf-8"))
def save(s, f, d): (P / s / ".meta" / f).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
def cap(s): return (P / s / "caption.txt")
def swap_eq(s, old, new, vo=None):
    p = load(s, "props.json"); p["endQuestion"] = new
    p["arabicTicker"] = [new if t == old else t for t in p["arabicTicker"]]
    save(s, "props.json", p)
    b = load(s, "v11-brief.json"); b["endQuestion"] = new
    if vo: b["voText"] = vo
    else: b["voText"] = b["voText"].replace(old, new)
    assert b["voText"].endswith(new), s
    save(s, "v11-brief.json", b)
    c = cap(s).read_text(encoding="utf-8"); cap(s).write_text(c.replace(old, new), encoding="utf-8")

# ── b · BLOCKER B1: no 964-bourse vs Shafaq-shop juxtaposition anywhere that airs
s = "2026-09-10-b-dollar-official-gap"
b = load(s, "v11-brief.json")
b["voText"] = "بحسب نشرة بورصات العراق صباح اليوم الخميس، بلغ سعر بيع مئة دولار في بغداد مئة وستة وخمسين ألفاً وسبعمئة وخمسين ديناراً، بينما السعر الرسمي المعتمد من البنك المركزي مئة وواحد وثلاثون ألفاً، بحسب النشرة نفسها. الفارق، بحسابنا، خمسة وعشرون ألفاً وسبعمئة وخمسون ديناراً على كل مئة دولار. أي أن من يشتري ألف دولار بسعر بورصة بغداد يدفع مئتين وسبعة وخمسين ألفاً وخمسمئة دينار فوق السعر الرسمي. بشكد اشتريت آخر مية دولار؟"
b["sourcesLine"] = "المصادر: شبكة 964 — نشرة بورصات العراق 10 أيلول 2026"
save(s, "v11-brief.json", b)
p = load(s, "props.json")
bt = p["beats"][2]   # V10 fallback surface: same fix
bt["arabicBody"] = "من يشتري 1,000 دولار بسعر بورصة بغداد يدفع 257,500 ديناراً فوق السعر الرسمي (محتسب من نشرة 964 نفسها)."
bt["supportingStats"] = [{"label": "لكل 1,000 دولار", "value": "257,500"}, {"label": "السعر الرسمي", "value": "131,000"}, {"label": "الأساس", "value": "بورصة"}]
bt["subtitlePhrases"] = [x for x in bt["subtitlePhrases"] if "شفق" not in x] + (["محتسب من النشرة نفسها"] if any("شفق" in x for x in bt["subtitlePhrases"]) else [])
save(s, "props.json", p)
c = cap(s).read_text(encoding="utf-8").splitlines()
c[0] = "سعر الدولار اليوم ببورصة بغداد: 25,750 فوق الرسمي لكل 100 دولار"
c = [("المصادر: شبكة 964 (نشرة بورصات العراق، 10 أيلول 2026)" if l.startswith("المصادر:") else l) for l in c]
cap(s).write_text("\n".join(c) + "\n", encoding="utf-8")

# ── d · BLOCKER D3 (+ «حتى الآن», no undated «اليوم») and hook attribution nit
s = "2026-09-10-d-taif-depositors-basra"
NEW = "عندك حساب بمصرف الطيف؟"
swap_eq(s, "راتبك موطّن بمصرف أهلي؟", NEW,
        vo="في البصرة، احتج مودعو مصرف الطيف بعد تعطل بطاقاتهم وتوقف السحب، ويقول المحتجون إن المتضررين يتجاوزون مئتي شخص. وقالت إحدى المودعات إن المصرف صرف الرواتب الموطّنة ولم يصرف للمودعين حتى الآن. البنك المركزي فرض الوصاية على المصرف ثمانية عشر شهراً، وأكد أن حقوق المودعين محفوظة وأن السحب سيُنظَّم تدريجياً مع أولوية للرواتب. ورئيس رابطة المصارف الخاصة قال إن شركة ضمان الودائع تغطي بالكامل ما دون خمسة وعشرين مليون دينار في حال الإفلاس، فيما يؤكد المركزي أن الوصاية لا تعني الإفلاس. " + NEW)
HOOK = "المركزي يقدّم الرواتب.. ومودعو الطيف ينتظرون"
b = load(s, "v11-brief.json"); b["hookHeadline"] = HOOK; save(s, "v11-brief.json", b)
p = load(s, "props.json"); p["breaking"]["arabicHeadline"] = HOOK
p["arabicTicker"] = [HOOK if "الرواتب أولاً" in t else t for t in p["arabicTicker"]]
save(s, "props.json", p)

# ── c · nits: keep attacker unambiguous; drop the Basra price from the Hormuz beat body
s = "2026-09-10-c-tanker-iraqi-waters"
p = load(s, "props.json")
p["beats"][1]["arabicBody"] = "رويترز عن مسؤولين بالموانئ: «نيو أندروس» تحمل نحو مليوني برميل وضُربت بمسيّرة، وطاقمها 22 بلا إصابات. ولم تعلن أي جهة مسؤوليتها حتى الآن (رووداو)."
p["beats"][2]["arabicBody"] = "بيانات تتبع نقلتها شفق نيوز: 7 سفن عبرت هرمز الأربعاء مقابل 12 قبلها بيوم، ومتوسط 10 أيام 14. وبعض السفن تعبر بأجهزة تتبع مطفأة."
p["beats"][2]["subtitlePhrases"] = [("وبعض السفن بأجهزة تتبع مطفأة" if "92.02" in x else x) for x in p["beats"][2]["subtitlePhrases"]]
save(s, "props.json", p)

# ── e · nit: endQuestion no longer links routine paperwork delays to bribery
s = "2026-09-10-e-bribe-car-papers"
swap_eq(s, "كم مراجعة احتاجت آخر معاملة إلك؟", "راجعت دائرة تنفيذ قبل؟")
print("gate fixes applied")
