#!/usr/bin/env python3
"""Consolidated pre-air fixes for the 2026-09-20 slate.

Sources of the fixes: my own pre-air review + the Opus editorial gate.
Gate Blocker 7 (c cites Shafaq without a Shafaq source) was REJECTED after
verification: the Shafaq sandstorm article exists, is same-day (2026-09-20
07:21Z) and is now saved as sources/C_shafaq_sandstorms.txt. Citation stands.

Gate Blocker 1 was adopted in substance but NOT as prescribed. The gate wanted
159,750 relabelled a SHOP price. 964 explicitly publishes it under «في بورصات
العراق», while Shafaq calls 159,750 the shop price and puts the bourse at
159,250 — the two outlets disagree on the venue taxonomy. Rather than pick a
side and misattribute, every surface now says «في بغداد» / «قائمة 964», which
is accurate to our cited source and removes the collision.
"""
import json
from pathlib import Path

P = Path("data/posts")
def load(s, f): return json.loads((P/f"2026-09-20-{s}"/f).read_text(encoding="utf-8"))
def save(s, f, o): (P/f"2026-09-20-{s}"/f).write_text(json.dumps(o, ensure_ascii=False, indent=1)+"\n", encoding="utf-8")
def cap(s, fn):
    p = P/f"2026-09-20-{s}"/"caption.txt"; p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")

# ══════════════════════════════════════════════════════════ A ═══
# Mine: Reuters described FLAMES AND SMOKE (AFP reported hearing blasts).
# Gate 3: Saturday facts were folded into an "اليوم الأحد" VO.
# Gate 4: «هالأسبوع» invented a time window the advisory never gives.
s = "a-us-warning-flights"
pr, br = load(s, ".meta/props.json"), load(s, ".meta/v11-brief.json")
pr["beats"][1]["arabicHeading"] = "أمس: لهب ودخان قرب مطار الملك خالد"
pr["beats"][1]["arabicBody"] = ("أمس السبت شوهدت ألسنة لهب وأعمدة دخان قرب مطار الملك خالد بالرياض "
                                "وأعلن الدفاع المدني الطوارئ، والإنذار شمل الرياض والخرج (رويترز عبر شبكة 964).")
pr["beats"][1]["subtitlePhrases"] = ["ألسنة لهب وأعمدة دخان", "قرب مطار الملك خالد", "والإنذار شمل الخرج"]
pr["arabicTicker"][2] = ("أمس السبت: ألسنة لهب وأعمدة دخان وطوارئ دفاع مدني قرب مطار الملك خالد، "
                         "والإنذار شمل الرياض والخرج (رويترز عبر شبكة 964 — 19 أيلول)")
pr["endQuestion"] = "عندك سفرة قريبة لو لا؟"
pr["arabicTicker"][4] = "عندك سفرة قريبة لو لا؟"
br["hookHeadline"] = "تحذير أميركي: رحلتك ممكن تنلغي؟"
br["endQuestion"] = "عندك سفرة قريبة لو لا؟"
br["voText"] = ("تحذير جديد من السفارة الأميركية في بغداد اليوم الأحد: البيئة الأمنية لا تزال معقدة، "
                "والتصعيد غير المتوقع وارد. ودعت السفارة رعاياها إلى متابعة احتمالات إلغاء الرحلات "
                "وإغلاق المجال الجوي واضطرابات السفر. وكانت ألسنة لهب وأعمدة دخان قد شوهدت أمس السبت "
                "قرب مطار الملك خالد في الرياض، وشمل الإنذار الرياض والخرج، بحسب رويترز. وقالت وزارة "
                "النقل العراقية أمس السبت إن العبور الدولي تجاوز سبعة آلاف ووصل أواسط آسيا، وإن نحو "
                "ألف وخمسمئة شاحنة تخرج عبر المنفذ الغربي. عندك سفرة قريبة لو لا؟")
save(s, ".meta/props.json", pr); save(s, ".meta/v11-brief.json", br)
cap(s, lambda t: t
    .replace("تحذير السفارة الأميركية في بغداد — شنو يعني لسفرتك هالأسبوع؟",
             "تحذير السفارة الأميركية في بغداد — شنو يعني لسفرتك؟")
    .replace("ووزارة النقل تقول البر لهسّه ماشي.", "ووزارة النقل قالت السبت إن البر لهسّه ماشي.")
    .replace("مسافر هالأسبوع لو أجّلت؟", "عندك سفرة قريبة لو لا؟"))

# ══════════════════════════════════════════════════════════ B ═══
# Mine: we asserted a FALL in our own voice on figures that don't show one, and
#       159,750 collided (964 "today" vs Shafaq "yesterday").
# Gate 1: venue taxonomy disputed between outlets -> go venue-neutral.
# Gate 2: rumour aired with no CBI rebuttal; the rebuttal was in our sources.
s = "b-dollar-159750-zero-rumor"
pr, br = load(s, ".meta/props.json"), load(s, ".meta/v11-brief.json")
pr["breaking"]["arabicHeadline"] = "الدولار تحت 160 ألفاً.. والسعر الرسمي بعده 131"
pr["beats"][0]["arabicHeading"] = "قائمة 964 اليوم: البيع 159,750 ببغداد"
pr["beats"][0]["arabicBody"] = ("قائمة 964 الصباحية اليوم الأحد: بيع 100 دولار في بغداد بـ159,750 ديناراً، "
                                "وأربيل بـ158,700، والبصرة بـ159,000 — والرسمي عند المركزي 131,000.")
pr["beats"][0]["subtitlePhrases"] = ["قائمة 964 الصباحية", "بغداد البيع 159,750", "والرسمي 131,000"]
pr["beats"][0]["bigStat"]["arabicLabel"] = "دينار سعر بيع 100 دولار في بغداد صباح الأحد (قائمة شبكة 964)"
pr["beats"][2]["supportingStats"][2] = {"label": "الذهب العراقي", "value": "953,000"}
pr["arabicTicker"][0] = ("قائمة 964 الصباحية للأحد: بيع 100 دولار في بغداد 159,750 ديناراً والشراء 159,000 "
                         "(شبكة 964 — 20 أيلول)")
pr["arabicTicker"][2] = ("شفق نيوز: تراجع طفيف بأسعار صرف الدولار في بغداد وأربيل خلال تداولات صباح اليوم الأحد")
pr["arabicTicker"].insert(4, ("البنك المركزي أمس: الاحتياطيات الأجنبية كافية والارتفاع سببه المضاربات "
                              "(شبكة 964 — 19 أيلول)"))
br["hookHeadline"] = "تحت 160 ألف.. ليش الناس تشتري؟"
br["voText"] = ("بقي الدولار تحت مئة وستين ألف دينار في أسواق العراق اليوم الأحد. فبحسب القائمة "
                "الصباحية لشبكة تسعة ستة أربعة، بلغ سعر بيع مئة دولار في بغداد مئة وتسعة وخمسين ألفاً "
                "وسبعمئة وخمسين ديناراً، بينما بقي السعر الرسمي لدى البنك المركزي عند مئة وواحد "
                "وثلاثين ألفاً. ويعزو الباحث عمرو هشام الصعود الأخير إلى تصريحات عن حذف أصفار من "
                "العملة دفعت مواطنين إلى التحوّط، فيما قال البنك المركزي أمس إن احتياطياته كافية وإن "
                "الارتفاع سببه المضاربات. بكم اشتريت الدولار آخر مرة؟")
br["statPops"][0]["matchWord"] = "بغداد"      # «بورصات» no longer appears in the VO
br["sourcesLine"] = "المصادر: شبكة 964 · شفق نيوز · البنك المركزي — 20 أيلول 2026"
save(s, ".meta/props.json", pr); save(s, ".meta/v11-brief.json", br)
cap(s, lambda t: t
    .replace("سعر الدولار اليوم في العراق — نزل لو طلع في بورصات بغداد؟",
             "سعر الدولار اليوم في العراق — نزل لو طلع؟")
    .replace("البورصات تبيع المية دولار بـ159,750.. وباحث اقتصادي يشرح ليش صارت الناس تشتري.",
             "قائمة 964 تسجّل بيع المية دولار بـ159,750.. وباحث اقتصادي يشرح ليش صارت الناس تشتري."))

# ══════════════════════════════════════════════════════════ C ═══
# Gate 6: we compared 300 DAYS to 24 STORMS in our own voice (the source
#         compares storms to storms), and "1951-1990" spelled out is unspeakable.
# Gate 7 REJECTED — Shafaq article verified, citation kept.
s = "c-sandstorms-300-days"
br = load(s, ".meta/v11-brief.json")
br["voText"] = ("حذّر مرصد العراق الأخضر اليوم الأحد من أن العواصف الترابية والرملية قد تصل إلى ثلاثمئة "
                "يوم سنوياً خلال السنوات العشر المقبلة. وحدّد المرصد ست بؤر ساخنة تنطلق منها هذه "
                "العواصف في وسط العراق وغربه وجنوبه، وقال إن غالبيتها متوطنة في المحافظات الجنوبية، "
                "وإن تكوّنها يعود إلى التصحّر الذي أصاب غالبية الأراضي في تلك المناطق. وبحسب المرصد، "
                "حتى التسعينات لم يكن عدد العواصف يتجاوز أربعاً وعشرين عاصفة في السنة. شكد يوم تعطّل "
                "دوام أولادك بسبب الغبار؟")
br["hookHeadline"] = "توقّع: 300 يوم غبار بالسنة؟"
save(s, ".meta/v11-brief.json", br)

# ══════════════════════════════════════════════════════════ D ═══
# Gate 5: «منصة أور» came from a WebSearch SUMMARY I never verified against the
#         page — no saved source supports it, and it was folded into the bank's
#         own «وأضاف». Removed everywhere, and «هذا اليوم» dropped as a source.
s = "d-solar-loans-30-million"
pr, br = load(s, ".meta/props.json"), load(s, ".meta/v11-brief.json")
pr["beats"][2]["arabicBody"] = ("المصرف قال إن المبادرة تأتي لدعم استخدام الطاقة النظيفة وتقليل الاعتماد "
                                "على مصادر الطاقة التقليدية، والتمويل مقدَّم من البنك المركزي (شبكة 964).")
pr["beats"][2]["supportingStats"][2] = {"label": "الجهة", "value": "مصرف الرشيد"}
pr["beats"][2]["subtitlePhrases"] = ["إمهال ستة أشهر", "قبل أول قسط", "والتمويل من البنك المركزي"]
pr["arabicTicker"][3] = "فترة إمهال تصل إلى 6 أشهر قبل أول قسط (مصرف الرشيد عبر شبكة 964)"
pr["sources"] = [{"name": "مصرف الرشيد", "domain": "rasheedbank.gov.iq"},
                 {"name": "شبكة 964", "domain": "964media.com"}]
br["sourcesLine"] = "المصادر: مصرف الرشيد · شبكة 964 — 20 أيلول 2026"
br["voText"] = ("أعلن مصرف الرشيد اليوم الأحد إطلاق قروض لشراء منظومات الطاقة الشمسية والمتجددة، "
                "بتمويل من البنك المركزي العراقي، وبحد أقصى ثلاثين مليون دينار. وقال المصرف في بيان "
                "تابعته شبكة تسعة ستة أربعة إن القروض تشمل المواطنين والموظفين، وإن الفائدة الإجمالية "
                "ثلاثة بالمئة سنوياً، ومدة السداد تصل إلى سبع سنوات، مع فترة إمهال تصل إلى ستة أشهر "
                "قبل أول قسط. وأضاف أن المبادرة تأتي لدعم استخدام الطاقة النظيفة وتقليل الاعتماد على "
                "مصادر الطاقة التقليدية. شكد تدفع للمولدة بالشهر؟")
save(s, ".meta/props.json", pr); save(s, ".meta/v11-brief.json", br)
cap(s, lambda t: t
    .replace("تمويل من البنك المركزي لشراء المنظومة.. وفترة إمهال قبل ما يبدي القسط.",
             "تمويل من البنك المركزي لشراء المنظومة.. وفترة إمهال قبل ما يبدي القسط.")
    .replace("المصادر: مصرف الرشيد، شبكة 964، هذا اليوم (20 أيلول 2026)",
             "المصادر: مصرف الرشيد، شبكة 964 (20 أيلول 2026)")
    .replace("#photonectnews", "#أخبار_العراق"))

# ══════════════════════════════════════════════════════════ E ═══
# Gate 8: end question presupposed a salary delay the reel never establishes.
# Gate 9: creditor direction inverted on the 72.5T line.
# Gate 10: «حوالات مخصومة» (72.5T) vs «حوالات خزينة» (8.74T) collision.
s = "e-public-debt-109-trillion"
pr = load(s, ".meta/props.json")
pr["beats"][1]["arabicBody"] = ("يتوزع الدين بين 72.5 تريليون مطالبات على وزارة المالية لصالح البنك المركزي، "
                                "و18.95 تريليون قروضاً، و9.33 تريليون سندات، و8.74 تريليون حوالات خزينة (شفق نيوز).")
pr["beats"][1]["bigStat"]["arabicLabel"] = ("حصة الحوالات المخصومة لدى المركزي — 72.5 تريليون من أصل 109.5 "
                                            "(نبيل المرسومي عبر شبكة 964)")
pr["beats"][1]["subtitlePhrases"] = ["72.5 تريليوناً مطالبات", "لصالح البنك المركزي", "أي 66% من الدين"]
pr["arabicTicker"][3] = ("التوزيع: 72.5 تريليون مطالبات على وزارة المالية لصالح المركزي، 18.95 تريليون قروض، "
                         "9.33 تريليون سندات، 8.74 تريليون حوالات خزينة (شفق نيوز)")
pr["arabicTicker"][4] = ("نبيل المرسومي: الحوالات المخصومة لدى المركزي (72.5 تريليون) تشكل 66% من الدين "
                         "الداخلي (شبكة 964 — 20 أيلول)")
pr["endQuestion"] = "راتبك من الحكومة لو من الخاص؟"
pr["arabicTicker"][5] = "راتبك من الحكومة لو من الخاص؟"
save(s, ".meta/props.json", pr)
cap(s, lambda t: t
    .replace("راتبك وصل بموعده هذا الشهر لو تأخر؟", "راتبك من الحكومة لو من الخاص؟")
    .replace("#photonectnews", "#أخبار_العراق"))

print("applied: A(3) B(4) C(2) D(3) E(3) fixes")
