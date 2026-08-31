#!/usr/bin/env python3
"""Apply the 2026-08-31 editorial-gate findings.

GATE 1 (fact/source) returned DO-NOT-SHIP with 5 blockers + 14 nits.
Every edit below is a verbatim string swap so nothing else can drift.

BLOCKERS
 1. C — «لا نية للتأخير أو للصرف كل 45 يوماً» was put in Finance Minister
    al-Sari's mouth. Shafaq attributes it to الحكومة ووزارة المالية in a
    SEPARATE sentence from his 7.7tn remark. Re-attributed on every surface.
 2. C — Shafaq hedges the Interior payout («تشير المتابعات إلى صرف...»).
    We stated it as accomplished fact. Hedge restored on every surface.
 3. E — the endQuestion «تأخرت رحلتك من مطار عراقي هالأسبوع؟» presupposed
    flight delays that the source EXPLICITLY says were never declared (our own
    statPop reads «0 · إغلاق رسمي معلن»), swapped transit overflight for airport
    departures, and stretched one overnight pause into a week — all while a
    night-apron aircraft frame was on screen. Replaced with a question that
    presupposes nothing and is still answerable in one word.
 4. B — the source labels Baghdad's pair «محال الصيرفة» but gives Erbil's only
    as «وفي أربيل». Our copy asserted «محال أربيل» and then CERTIFIED
    «محلاً مقابل محل». The comparison is sound; the certification over-claims.
    Recast as sell-price vs sell-price throughout.
 5. B — statPop «550» carried no basis and rendered straight after the bourse
    statPop, inviting the exact bourse-vs-shop inversion that burned us on 08-17.

NITS applied: A 20m→20m+340k, A hook attributor, A «ما سمي», A subhead title;
C bigStat «1»→البصرة, C sourcesLine; E sourcesLine, E «بشهره السادس»,
E unnamed source, E staged resumption restored; D period anchor, D «فقط»,
D ticker wording.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
D = "2026-08-31"

# (slug, relative file, old, new)
EDITS: list[tuple[str, str, str, str]] = []


def E(slug, f, old, new):
    EDITS.append((f"{D}-{slug}", f, old, new))


# ══════════════ A · nits 1-4 ══════════════
A = "a-jumaili-office-seizure"
E(A, ".meta/v11-brief.json",
  "بملف الجميلي: 7 مليارات دينار و35 عقاراً مضبوطة",
  "بملف الجميلي: القضاء يعلن ضبط 7 مليارات و35 عقاراً")
E(A, ".meta/props.json",
  "OIL-MINISTRY UNDERSECRETARY ADNAN AL-JUMAILI",
  "OIL-MINISTRY UNDERSECRETARY FOR REFINING AFFAIRS ADNAN AL-JUMAILI")
# 20 مليون دولار understated the source's «20 مليون دولار و340 ألف دولار»
E(A, ".meta/props.json",
  "وسبق إعلان ضبط 20 مليون دولار واسترجاع 60 كيلوغراماً من الذهب",
  "وسبق إعلان ضبط 20 مليون و340 ألف دولار واسترجاع 60 كيلوغراماً من الذهب")
E(A, ".meta/props.json",
  "60 كيلوغراماً، مع 20 مليون دولار و200 مليون دينار",
  "60 كيلوغراماً، مع 20 مليون و340 ألف دولار و200 مليون دينار")
E(A, ".meta/props.json", '"value": "20 مليون $"', '"value": "20.34 مليون $"')
E(A, ".meta/props.json",
  "وسبق إعلان ضبط 20 مليون دولار",
  "وسبق إعلان ضبط 20 مليون و340 ألف دولار")
E(A, ".meta/props.json",
  "وسبق أن أعلن القضاء ضبط 20 مليون دولار واسترجاع",
  "وسبق أن أعلن القضاء ضبط 20 مليون و340 ألف دولار واسترجاع")
E(A, "caption.txt",
  "صولة الفجر: القضاء يعلن ضبط 7 مليارات دينار و35 عقاراً",
  "ما سمي «صولة الفجر»: القضاء يعلن ضبط 7 مليارات دينار و35 عقاراً")

# ══════════════ B · blockers 4-5 ══════════════
B = "b-dollar-flat-second-day"
E(B, ".meta/props.json",
  "الدولار ثابت لليوم الثاني.. ومحال أربيل أرخص 550 ديناراً (محتسب)",
  "الدولار ثابت لليوم الثاني.. وأربيل أرخص 550 ديناراً (محتسب)")
E(B, ".meta/props.json",
  "ERBIL SHOPS SELL 153,950 — A 550-DINAR GAP, SHOP TO SHOP, OUR OWN ARITHMETIC",
  "ERBIL SELLS 153,950 — A 550-DINAR GAP, SELL PRICE VS SELL PRICE, OUR OWN ARITHMETIC")
E(B, ".meta/props.json",
  "بمحال الصيرفة، بغداد تبيع 100 دولار بـ154,500 دينار وأربيل بـ153,950، أي أرخص بـ550 ديناراً — محلاً مقابل محل لا مقابل البورصة (محتسب · شفق نيوز).",
  "سعر بيع محال الصيرفة ببغداد 154,500 دينار لكل 100 دولار، وسعر البيع بأربيل 153,950 — أرخص بـ550 ديناراً، سعر بيع مقابل سعر بيع لا مقابل البورصة (محتسب · شفق نيوز).")
E(B, ".meta/props.json",
  "وسعر بيع محال أربيل 153,950 لكل 100 دولار، محتسب من رقمي شفق نيوز، ومقارنة محال بمحال لا بالبورصة",
  "وسعر البيع بأربيل 153,950 لكل 100 دولار، محتسب من رقمي شفق نيوز، ومقارنة سعر بيع بسعر بيع لا بالبورصة")
E(B, ".meta/props.json",
  "IQD cheaper per $100 in Erbil shops than Baghdad shops — our subtraction",
  "IQD cheaper per $100 in Erbil than in Baghdad shops, sell price vs sell price — our subtraction")
E(B, ".meta/props.json",
  '"أرخص بـ550 ديناراً محلاً مقابل محل (محتسب)"',
  '"أرخص بـ550 ديناراً، بيع مقابل بيع (محتسب)"')
E(B, ".meta/props.json",
  "سعر الشراء بمحال بغداد 153,500 وبأربيل 153,850 — يعني محال أربيل تدفع لك 350 ديناراً زيادة عن كل 100 دولار تبيعها (محتسب · شفق نيوز).",
  "سعر الشراء بمحال بغداد 153,500 وبأربيل 153,850 — يعني بأربيل تقبض 350 ديناراً زيادة عن كل 100 دولار تبيعها (محتسب · شفق نيوز).")
E(B, ".meta/props.json",
  "الفارق بين سعر شراء محال أربيل 153,850 وسعر شراء محال بغداد 153,500",
  "الفارق بين سعر الشراء بأربيل 153,850 وسعر شراء محال بغداد 153,500")
E(B, ".meta/props.json",
  '"IQD more per $100 an Erbil shop pays you to buy your dollars — our subtraction"',
  '"IQD more per $100 paid for your dollars in Erbil than in Baghdad shops — our subtraction"')
E(B, ".meta/props.json",
  '"وبمحال أربيل 153,850"', '"وبأربيل 153,850"')
E(B, ".meta/props.json",
  '"أربيل تدفع لك 350 ديناراً أكثر (محتسب)"', '"بأربيل تقبض 350 ديناراً أكثر (محتسب)"')
E(B, ".meta/props.json",
  '"وبمحال أربيل 153,950"', '"وسعر البيع بأربيل 153,950"')
E(B, ".meta/props.json",
  "الدولار ثابت لليوم الثاني.. ومحال أربيل أرخص 550 ديناراً (محتسب)\",",
  "الدولار ثابت لليوم الثاني.. وأربيل أرخص 550 ديناراً (محتسب)\",")
E(B, ".meta/props.json",
  "محال أربيل: بيع 153,950 وشراء 153,850 — أرخص للشاري وأعلى للبائع (محتسب)",
  "وفي أربيل: بيع 153,950 وشراء 153,850 — أرخص للشاري وأعلى للبائع (محتسب)")
E(B, ".meta/props.json",
  "كل الفوارق محتسبة من أرقام شفق نيوز، ومقارنة محال بمحال لا بالبورصة",
  "كل الفوارق محتسبة من أرقام شفق نيوز، ومقارنة سعر بيع بسعر بيع لا بالبورصة")
E(B, ".meta/v11-brief.json",
  "وهو فارق محتسب من رقمي شفق نيوز، محلاً مقابل محل لا مقابل البورصة.",
  "وهو فارق محتسب من رقمي البيع اللذين نشرتهما شفق نيوز، سعر بيع مقابل سعر بيع لا مقابل البورصة.")
E(B, ".meta/v11-brief.json",
  "وإذا كنت تبيع دولارك، فمحال أربيل تدفع لك أكثر من محال بغداد.",
  "وإذا كنت تبيع دولارك، فسعر الشراء بأربيل أعلى منه في محال بغداد.")
E(B, ".meta/v11-brief.json",
  '"label": "أرخص بأربيل لكل 100 دولار (محتسب)"',
  '"label": "فرق سعر بيع أربيل عن بغداد (محتسب)"')
E(B, "caption.txt",
  "والفارق بين محال بغداد ومحال أربيل 550 ديناراً لكل 100 دولار (محتسب · محلاً مقابل محل لا مقابل البورصة)",
  "والفارق بين سعر بيع بغداد وسعر بيع أربيل 550 ديناراً لكل 100 دولار (محتسب · سعر بيع مقابل سعر بيع لا مقابل البورصة)")

# ══════════════ C · blockers 1-2 + nits 5-6 ══════════════
C = "c-salaries-august-last-day"
E(C, ".meta/props.json",
  "الداخلية قبضت.. والتربية والصحة والكهرباء تنتظر",
  "متابعات: الداخلية قبضت.. والتربية والصحة تنتظر")
E(C, ".meta/props.json",
  "بآخر يوم من آب، صُرفت رواتب الداخلية ودوائر أخرى، بينما",
  "بآخر يوم من آب، وبحسب متابعات شفق نيوز صُرفت رواتب الداخلية ودوائر أخرى، بينما")
E(C, ".meta/props.json",
  '"الداخلية ودوائر أخرى صُرفت رواتبها"',
  '"متابعات شفق: الداخلية ودوائر أخرى صُرفت"')
E(C, ".meta/props.json",
  "شفق نيوز: صُرفت رواتب الداخلية ودوائر أخرى، فيما التربية والصحة والكهرباء بعدها تنتظر",
  "متابعات شفق نيوز تشير إلى صرف رواتب الداخلية ودوائر أخرى، فيما التربية والصحة والكهرباء بعدها تنتظر")
E(C, ".meta/props.json",
  "وقال إنها مؤمّنة بالكامل ولا نية للتأخير أو الصرف كل 45 يوماً (شفق نيوز)",
  "وقال إنها مؤمّنة بالكامل، فيما تؤكد الحكومة ووزارة المالية أنه لا نية للتأخير أو الصرف كل 45 يوماً (شفق نيوز)")
E(C, ".meta/props.json",
  '"ولا نية للتأخير أو للصرف كل 45 يوماً"',
  '"والحكومة والمالية: لا نية للتأخير أو للصرف كل 45 يوماً"')
E(C, ".meta/props.json",
  "الساري: لا نية للتأخير ولا للصرف كل 45 يوماً، بحسب شفق نيوز",
  "الحكومة ووزارة المالية: لا نية للتأخير ولا للصرف كل 45 يوماً (شفق نيوز)")
E(C, ".meta/props.json",
  '"value": "1",\n        "label": "university where staff struck on Monday — Basra, over delayed pay and stalled allowances"',
  '"value": "البصرة",\n        "label": "the university whose staff struck on Monday, over delayed pay and stalled allowances"')
E(C, ".meta/v11-brief.json",
  "صرفت رواتب وزارة الداخلية ودوائر أخرى، فيما ينتظر موظفو التربية والتعليم العالي والكهرباء والصحة. وزارة المالية أعلنت في السادس والعشرين من آب مباشرتها بتمويل الرواتب، والصرف يجري تدريجياً بحسب الجهات. ووزير المالية فالح الساري قال إن الكلفة الشهرية نحو سبعة فاصلة سبعة تريليون دينار، مؤمنة بالكامل، ولا نية للتأخير أو للصرف كل خمسة وأربعين يوماً. وفي البصرة، اعتصم",
  "وبحسب متابعات شفق نيوز صرفت رواتب وزارة الداخلية ودوائر أخرى، فيما ينتظر موظفو التربية والتعليم العالي والكهرباء والصحة. وزارة المالية أعلنت في السادس والعشرين من آب مباشرتها بتمويل الرواتب تدريجياً بحسب الجهات. ووزير المالية فالح الساري قال إن الكلفة الشهرية نحو سبعة فاصلة سبعة تريليون دينار وإنها مؤمنة بالكامل، فيما تؤكد الحكومة ووزارة المالية أنه لا نية للتأخير. وفي البصرة اعتصم")
E(C, ".meta/v11-brief.json",
  '"sourcesLine": "المصادر: شفق نيوز · وزارة المالية"',
  '"sourcesLine": "المصادر: شفق نيوز"')
E(C, "caption.txt",
  "الداخلية ودوائر أخرى صُرفت،",
  "بحسب متابعات شفق نيوز، الداخلية ودوائر أخرى صُرفت،")
E(C, "caption.txt",
  "ووزير المالية فالح الساري يؤكد أن الكلفة الشهرية نحو 7.7 تريليون دينار ومؤمّنة بالكامل ولا نية للتأخير.",
  "ووزير المالية فالح الساري يؤكد أن الكلفة الشهرية نحو 7.7 تريليون دينار ومؤمّنة بالكامل، فيما تؤكد الحكومة والمالية أنه لا نية للتأخير.")
E(C, "caption.txt", "المصادر: شفق نيوز، وزارة المالية", "المصادر: شفق نيوز")

# ══════════════ D · nits 11-13 ══════════════
Dg = "d-internal-debt-106"
E(Dg, ".meta/props.json",
  "بيانات المركزي: الدين الداخلي زاد 15.557 تريليون دينار بستة أشهر\",\n    \"englishSubhead",
  "بيانات المركزي: الدين الداخلي زاد 15.557 تريليون دينار بستة أشهر حتى حزيران\",\n    \"englishSubhead")
E(Dg, ".meta/props.json", "زاد 15.557 تريليوناً بستة أشهر فقط", "زاد 15.557 تريليوناً بستة أشهر")
E(Dg, ".meta/props.json",
  "التوزيع: مطالبات المالية لدى المركزي 67.499",
  "التوزيع: مطالبات وزارة المالية لصالح البنك المركزي 67.499")

# ══════════════ E · blocker 3 + nits 7-10 ══════════════
Eg = "e-oil-larak-airspace"
OLDQ = "تأخرت رحلتك من مطار عراقي هالأسبوع؟"
NEWQ = "عندك سفرة من مطار عراقي هالأسبوع؟"
E(Eg, ".meta/props.json", OLDQ, NEWQ)
E(Eg, ".meta/v11-brief.json", f'"endQuestion": "{OLDQ}"', f'"endQuestion": "{NEWQ}"')
E(Eg, "caption.txt", OLDQ, NEWQ)
E(Eg, ".meta/v11-brief.json",
  "وفي العراق، قال مصدر أمني عراقي إن حركة الطيران العابر توقفت ساعات بعد منتصف الليل، ثم عادت طبيعية صباحاً، وإنه لم يعلن رسمياً أي إغلاق للأجواء أو تأخير للرحلات، وذلك تزامناً مع هذه التطورات. ومفاوضات إعادة فتح المضيق وصلت إلى طريق مسدود. " + OLDQ,
  "وفي العراق، قال مصدر أمني لم يكشف عن اسمه إن الطيران العابر توقف ساعات بعد منتصف الليل، ثم عاد أولاً للرحلات المتجهة إلى أربيل قبل أن يعود طبيعياً على كل الأجواء، وإنه لم يعلن رسمياً أي إغلاق أو تأخير للرحلات، تزامناً مع هذه التطورات. " + NEWQ)
E(Eg, ".meta/v11-brief.json",
  '"sourcesLine": "المصادر: شفق نيوز · رويترز"',
  '"sourcesLine": "المصادر: شفق نيوز"')
E(Eg, "caption.txt", "المصادر: شفق نيوز، رويترز", "المصادر: شفق نيوز")
E(Eg, ".meta/props.json",
  '"label": "عمر الصراع",\n          "value": "6 أشهر"',
  '"label": "الصراع",\n          "value": "بشهره السادس"')
E(Eg, ".meta/props.json",
  "بحسب مصدر أمني عراقي تحدث لشفق نيوز، رغم توقف الطيران العابر ساعات بعد منتصف الليل",
  "بحسب مصدر أمني عراقي لم يكشف عن اسمه تحدث لشفق نيوز، رغم توقف الطيران العابر ساعات بعد منتصف الليل")
E(Eg, ".meta/props.json",
  "مصدر أمني عراقي: الطيران العابر توقف ساعات بعد منتصف الليل ثم عاد طبيعياً صباحاً",
  "مصدر أمني عراقي لم يكشف عن اسمه: الطيران العابر توقف ساعات ثم عاد طبيعياً صباحاً")
E(Eg, ".meta/props.json",
  '"بعد منتصف الليل ثم عاد طبيعياً صباحاً",',
  '"بعد منتصف الليل، وعاد أولاً لرحلات أربيل",')


def main() -> int:
    misses = 0
    touched: dict[str, int] = {}
    for slug, rel, old, new in EDITS:
        p = POSTS / slug / rel
        txt = p.read_text(encoding="utf-8")
        if old not in txt:
            print(f"  MISS  {slug}/{rel}: {old[:70]!r}")
            misses += 1
            continue
        p.write_text(txt.replace(old, new), encoding="utf-8")
        touched[f"{slug}/{rel}"] = touched.get(f"{slug}/{rel}", 0) + 1
    for k in sorted(touched):
        print(f"  ok  {k}  ({touched[k]} edits)")
    # JSON must still parse
    for p in sorted(POSTS.glob(f"{D}-*/.meta/*.json")):
        json.loads(p.read_text(encoding="utf-8"))
    print(f"\n{len(EDITS)-misses}/{len(EDITS)} edits applied, all JSON valid.")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
