#!/usr/bin/env python3
"""Author the 2026-10-07 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source (Cabinet decision 544 / CBI / MoF statements via Shafaq, 964, Rudaw, Baghdad Today;
Integrity Commission via Shafaq / 964 / Baghdad Today; Reuters + Bloomberg + Kpler via Shafaq; Najaf Health + Meteorology
+ Green Iraq via Shafaq / 964 / Baghdad Today). Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + gate passes then edit the files on disk —
do NOT re-run this script after that, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_10_07.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-07"
DATE_LABEL = "OCT 07 • 2026"
AR_DATE = "7 تشرين الأول 2026"
IMG = "images/news"


def beat(label, heading, body, val, en_label, ar_label, stats, idx, slug, phrases, src, accent="#FFC217"):
    return {
        "label": label, "arabicHeading": heading, "arabicBody": body,
        "bigStat": {"value": val, "label": en_label, "arabicLabel": ar_label},
        "supportingStats": [{"label": k, "value": v} for k, v in stats],
        "broll": f"{IMG}/{slug}/broll_{idx}.jpg", "brolls": [f"{IMG}/{slug}/broll_{idx}.jpg"],
        "brollType": "image", "accent": accent, "brollSource": src, "subtitlePhrases": phrases,
    }


def base(slug, bucket, variant, kicker, headline, subhead):
    return {"dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
            "audioBed": "audio/mood_newsroom.mp3", "topicBucket": bucket, "variant": variant,
            "breaking": {"arabicKicker": kicker, "arabicHeadline": headline, "englishSubhead": subhead,
                         "heroMedia": f"{IMG}/{slug}/hero.jpg", "heroMediaType": "image"}}


STOCK = "صورة أرشيفية"
SLATE = {}

# ═══════════ A · 18:00 · P1 money (LEAD) — official rate moves to 1,520 ═══════════
slug = f"{D}-a-dinar-1520-official"
p = base(slug, "iraq_money", "A", "سعر الصرف", "رسمياً: الـ100 دولار صارت بـ152 ألف دينار",
  ("BAGHDAD · OCT 7 | CABINET DECISION 544 (SESSION 22, OCT 6) + CBI CIRCULAR (VIA SHAFAQ NEWS, 964, RUDAW, BAGHDAD TODAY): "
   "MoF SELLS $ TO CBI AT 1,500 IQD, CBI SELLS TO BANKS AT 1,510, TO THE PUBLIC AT 1,520 (152,000 PER $100), EFFECTIVE OCT 7 | "
   "BUDGET-LAW RATE WAS 130,000 PER $100 (RUDAW) | MoF HALTS CUSTOMS PRE-PAYMENT DECISION 413"))
p["beats"] = [
 beat("القرار", "1,520 ديناراً للدولار.. من اليوم",
  "قرار مجلس الوزراء 544: البنك المركزي يشتري الدولار من المالية بـ1,500 دينار، ويبيعه للمصارف بـ1,510، وللمواطنين بـ1,520، اعتباراً من الأربعاء.",
  "1,520", "IQD per dollar — new CBI cash sale price to the public from Oct 7 (Cabinet decision 544 / CBI, via Shafaq / 964 / Rudaw)",
  "دينار للدولار — سعر البيع للمواطنين",
  [("شراء من المالية", "1,500"), ("بيع للمصارف", "1,510"), ("لكل 100 دولار", "152,000")], 1, slug,
  ["الدولار الرسمي 1,520", "المصارف 1,510", "المالية 1,500"], STOCK),
 beat("الفرق", "سعر الموازنة كان 130 ألفاً",
  "بحسب رووداو، ثُبّت سعر 100 دولار عند 130 ألف دينار في قانون الموازنة الثلاثية. سعر وزارة المالية الجديد أعلى منه بـ200 دينار لكل دولار (محتسب).",
  "200", "IQD per dollar: MoF rate 1,500 vs budget-law 1,300 (Rudaw; computed)", "دينار زيادة لكل دولار (محتسب)",
  [("سعر الموازنة", "130,000"), ("سعر المالية الجديد", "150,000"), ("لكل 100 دولار", "+20,000 (محتسب)")], 2, slug,
  ["الموازنة: 130 ألف", "المالية الآن: 150 ألف", "+200 دينار للدولار (محتسب)"], STOCK),
 beat("ردود الفعل", "المركزي يطمئن.. ونواب يطلبون جلسة طارئة",
  "المركزي يقول إن احتياطياته كافية لكل طلبات التحويل والبطاقات والمسافرين دون قيود. نواب طالبوا بجلسة طارئة للتراجع عن القرار.",
  "544", "Number of the Cabinet decision changing the rate (MoF statement via Shafaq / 964)", "رقم قرار مجلس الوزراء",
  [("المالية", "إيقاف الاستيفاء المسبق للجمارك"), ("المركزي", "الاحتياطيات كافية"), ("نواب", "جلسة طارئة")], 3, slug,
  ["المركزي: الاحتياطي كافٍ", "المالية توقف الاستيفاء المسبق", "نواب: جلسة طارئة"], STOCK),
]
p["arabicTicker"] = [
 "مجلس الوزراء يعدّل سعر الصرف بالقرار 544 — التطبيق من الأربعاء 7 تشرين الأول",
 "البنك المركزي: 1,500 شراء من المالية، 1,510 للمصارف، 1,520 للمواطنين",
 "رووداو: سعر 100 دولار كان 130 ألف دينار في قانون الموازنة الثلاثية",
 "وزارة المالية توقف قرار الاستيفاء المسبق للرسوم الجمركية رقم 413",
 "المركزي: الاحتياطيات تلبي التحويل والبطاقات والمسافرين دون قيود",
 "لاحظت غلاء بالسوق هالأسبوع؟"]
p["endQuestion"] = "لاحظت غلاء بالسوق هالأسبوع؟"
p["sources"] = [{"name": "البنك المركزي العراقي", "domain": "cbi.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "شبكة 964", "domain": "964media.com"}, {"name": "رووداو", "domain": "rudawarabia.net"}]
SLATE[slug] = {"props": p, "caption": """سعر صرف الدولار الرسمي الجديد في العراق — شنو تغيّر عليك؟

من اليوم الـ100 دولار بالسعر الرسمي صار لها رقم جديد.. التفاصيل بالفيديو.

لاحظت غلاء بالسوق هالأسبوع؟

المصادر: البنك المركزي ووزارة المالية عبر شفق نيوز، شبكة 964، رووداو (6 و7 تشرين الأول 2026)

#سعر_الصرف #الدينار_العراقي #البنك_المركزي_العراقي #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "سعر الصرف", "hookHeadline": "رسمياً: الـ100 دولار بـ152 ألف",
  "voText": "قرر مجلس الوزراء الثلاثاء تعديل سعر صرف الدولار، وبدأ التطبيق اليوم الأربعاء. وبحسب البنك المركزي، يشتري البنك الدولار من وزارة المالية بألف وخمسمئة دينار، ويبيعه للمصارف بألف وخمسمئة وعشرة، وللمواطنين بألف وخمسمئة وعشرين، أي مئة واثنين وخمسين ألفاً لكل مئة دولار. وتقول رووداو إن سعر الموازنة السابق كان مئة وثلاثين ألفاً. ويؤكد المركزي أن احتياطياته كافية لكل طلبات التحويل والمسافرين دون قيود، فيما يطالب نواب بجلسة طارئة للتراجع عن القرار. لاحظت غلاء بالسوق هالأسبوع؟",
  "endQuestion": "لاحظت غلاء بالسوق هالأسبوع؟",
  "sourcesLine": "المصادر: البنك المركزي ووزارة المالية عبر شفق نيوز · شبكة 964 · رووداو — 6 و7 تشرين الأول 2026",
  "statPops": [{"value": "152,000", "label": "دينار لكل 100 دولار — السعر الرسمي للمواطنين", "matchWord": "وللمواطنين"},
               {"value": "130,000", "label": "سعر 100 دولار في قانون الموازنة (رووداو)", "matchWord": "الموازنة"}]}}


# ═══════════ B · 19:45 · P1 dollar anchor — bourse 168,500, some shops past 170k ═══════════
slug = f"{D}-b-dollar-168500-bourse"
p = base(slug, "iraq_money", "B", "سعر الدولار", "بعد القرار.. البورصة تقفز إلى 168,500",
  "168,500 IQD/$100 KIFAH & HARITHIYA WED AM (SHAFAQ) | TUE AM 159,800 | >170,000 IN SOME SHOPS (964, BAGHDAD TODAY) | NEW OFFICIAL 152,000")
p["beats"] = [
 beat("صباح الأربعاء", "الكفاح: 168,500 صباح الأربعاء",
  "بحسب شفق نيوز، سجلت بورصتا الكفاح والحارثية صباح الأربعاء 168,500 دينار لكل 100 دولار، بعدما كانت 159,800 صباح الثلاثاء.",
  "168,500", "IQD per $100, Kifah & Harithiya, Wednesday morning (Shafaq News)", "دينار لكل 100 دولار",
  [("صباح الثلاثاء", "159,800"), ("محال بغداد بيع", "169,000"), ("أربيل بيع", "168,200")], 1, slug,
  ["الكفاح 168,500", "صباح الثلاثاء 159,800", "أربيل 168,200"], STOCK),
 beat("الإرباك", "فوق 170 ألفاً.. ومحال توقف البيع",
  "شبكة 964 وبغداد اليوم: السعر تجاوز 170 ألفاً لكل 100 دولار في بعض المحال. وبحسب شفق نيوز، أوقفت محال صيرفة في بغداد وكركوك البيع مؤقتاً.",
  "170,000", "IQD per $100 — level crossed in some shops/bourse on Wednesday (964, Baghdad Today)", "دينار تجاوزها السعر ببعض المحال",
  [("964", "فوق 170 ألف"), ("بغداد اليوم", "170 ألف"), ("كركوك", "تعليق التعامل")], 2, slug,
  ["فوق 170 ألف ببعض المحال", "صيرفات توقف البيع", "كركوك تعلّق التعامل"], STOCK),
 beat("الفجوة والذهب", "فوق الرسمي الجديد بـ16,500",
  "السعر الرسمي الجديد 152 ألفاً لكل 100 دولار، أي أن سعر الكفاح الصباحي أعلى بـ16,500 (محتسب). ومثقال الذهب الخليجي عيار 21 في شارع النهر: 978 ألفاً.",
  "16,500", "IQD per $100 above the new official 152,000 (Kifah 168,500 − 152,000, computed)", "دينار فوق الرسمي الجديد (محتسب)",
  [("الرسمي الجديد", "152,000"), ("ذهب 21 اليوم", "978 ألف"), ("ذهب 21 الثلاثاء", "930 ألف")], 3, slug,
  ["الرسمي الجديد 152 ألف", "الفرق 16,500 (محتسب)", "الذهب 978 ألف للمثقال"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الكفاح والحارثية صباح الأربعاء 168,500 دينار لكل 100 دولار",
 "صباح الثلاثاء كان 159,800 (شفق نيوز)",
 "شبكة 964 وبغداد اليوم: تجاوز 170 ألفاً في بعض المحال",
 "محال صيرفة في بغداد وكركوك أوقفت البيع مؤقتاً (شفق نيوز)",
 "مثقال الذهب الخليجي عيار 21: 978 ألفاً بعد 930 ألفاً الثلاثاء",
 "شكد اشتريت الـ100 دولار اليوم؟"]
p["endQuestion"] = "شكد اشتريت الـ100 دولار اليوم؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار اليوم في بغداد بعد السعر الرسمي الجديد — شكد صار؟

البورصة تحركت بسرعة والصيرفات ارتبكت.. الأرقام بالفيديو.

شكد اشتريت الـ100 دولار اليوم؟

المصادر: شفق نيوز، شبكة 964، بغداد اليوم (6 و7 تشرين الأول 2026)

#سعر_الدولار_اليوم #بورصة_الكفاح #الدينار_العراقي #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "سعر الدولار", "hookHeadline": "البورصة تقفز بعد القرار",
  "voText": "سجلت بورصتا الكفاح والحارثية في بغداد صباح الأربعاء مئة وثمانية وستين ألفاً وخمسمئة دينار لكل مئة دولار، بحسب شفق نيوز، بعد أن كانت صباح الثلاثاء مئة وتسعة وخمسين ألفاً وثمانمئة. وتقول شبكة تسعة ستة أربعة وبغداد اليوم إن السعر تجاوز مئة وسبعين ألفاً في بعض المحال، فيما أوقفت محال صيرفة في بغداد وكركوك البيع مؤقتاً. وبذلك يزيد سعر البورصة على السعر الرسمي الجديد بستة عشر ألفاً وخمسمئة دينار. شكد اشتريت الميّة دولار اليوم؟",
  "endQuestion": "شكد اشتريت الـ100 دولار اليوم؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 · بغداد اليوم — 6 و7 تشرين الأول 2026",
  "statPops": [{"value": "168,500", "label": "دينار لكل 100 دولار — الكفاح صباح الأربعاء", "matchWord": "والحارثية"},
               {"value": "16,500", "label": "دينار فوق السعر الرسمي الجديد (محتسب)", "matchWord": "الرسمي"}]}}


# ═══════════ C · 21:15 · P2 Gulf/Iran oil (V10.1 CONTROL) — Basra crude replaces Iranian barrels in China ═══════════
slug = f"{D}-c-basra-crude-china"
p = base(slug, "mena_geo", "A", "النفط", "مصافي الصين تشتري نفط البصرة بدل الإيراني",
  ("REUTERS / BLOOMBERG (VIA SHAFAQ NEWS), KPLER DATA: CHINESE INDEPENDENT REFINERS BOUGHT AT LEAST 12M BBL OF IRAQI + QATARI CRUDE "
   "FOR OCT-NOV (ONE TRADER: 15-20M), MOSTLY BASRA MEDIUM/HEAVY, AT $12-20 OVER ICE BRENT | CHINA'S IRANIAN IMPORTS 590K BPD IN SEPT, "
   "LOWEST SINCE JAN 2023 | IRAN EXPORTED NO CRUDE IN SEPT (KPLER)"))
p["beats"] = [
 beat("الصفقات", "12 مليون برميل على الأقل",
  "بحسب رويترز، اشترت مصافٍ صينية مستقلة 12 مليون برميل على الأقل من الخام العراقي والقطري لشحنات تشرين الأول والثاني، وأحد التجار قدّرها بين 15 و20 مليوناً.",
  "12", "Million barrels minimum of Iraqi + Qatari crude bought by Chinese independents for Oct-Nov (Reuters via Shafaq)",
  "مليون برميل على الأقل",
  [("تقدير تاجر", "15 - 20 مليون"), ("الخامات", "البصرة المتوسط والثقيل"), ("الوسطاء", "ميركوريا · توتسا · ترافيغورا")], 1, slug,
  ["مصافي الصين المستقلة", "12 مليون برميل على الأقل", "أغلبها من خام البصرة"], STOCK),
 beat("الإيراني", "واردات الصين من إيران: 590 ألف برميل",
  "وفق بيانات كبلر، تراجعت واردات الصين من النفط الإيراني في أيلول إلى 590 ألف برميل يومياً، الأدنى منذ كانون الثاني 2023، ولم تصدّر إيران خاماً خلال أيلول.",
  "590", "Thousand bpd of Iranian crude into China in September, ~half year-on-year, lowest since Jan 2023 (Kpler via Reuters / Shafaq)",
  "ألف برميل يومياً من إيران للصين",
  [("المقارنة السنوية", "نحو النصف"), ("المخزون العائم", "45 مليون برميل"), ("أواخر تموز", "100 مليون")], 2, slug,
  ["الإيراني إلى الصين: 590 ألف", "الأدنى منذ 2023", "وإيران بلا صادرات خام بأيلول"], STOCK),
 beat("السعر", "علاوة حتى 20 دولاراً فوق برنت",
  "بحسب رويترز، بيعت الشحنات بعلاوات بين 12 و20 دولاراً للبرميل فوق برنت، وقال أحد المتعاملين إن النفط العراقي صار المعيار الجديد للمصافي المستقلة.",
  "20", "USD per barrel — top of the $12-20 premium over ICE Brent paid for the cargoes (Reuters via Shafaq)",
  "دولاراً علاوة فوق برنت",
  [("أدنى علاوة", "12 دولاراً"), ("أعلى علاوة", "20 دولاراً"), ("المشترون", "مصافٍ مستقلة")], 3, slug,
  ["علاوة 12 - 20 دولاراً", "فوق سعر برنت", "العراقي المعيار الجديد"], STOCK),
]
p["arabicTicker"] = [
 "رويترز: مصافٍ صينية مستقلة اشترت 12 مليون برميل على الأقل من الخام العراقي والقطري",
 "أغلب المشتريات من خامي البصرة المتوسط والثقيل",
 "كبلر: واردات الصين من النفط الإيراني 590 ألف برميل يومياً في أيلول",
 "كبلر: إيران لم تصدّر أي خام في أيلول لأول مرة منذ 2013",
 "تشتغل بقطاع النفط؟"]
p["endQuestion"] = "تشتغل بقطاع النفط؟"
p["sources"] = [{"name": "رويترز", "domain": "reuters.com"}, {"name": "بلومبيرغ", "domain": "bloomberg.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """نفط البصرة في الصين — ليش المصافي تشتريه بدل الإيراني؟

ملايين البراميل بعلاوة فوق برنت.. التفاصيل بالفيديو.

تشتغل بقطاع النفط؟

المصادر: رويترز، بلومبيرغ، بيانات كبلر — عبر شفق نيوز (6 و7 تشرين الأول 2026)

#نفط_البصرة #النفط_العراقي #الصين #العراق #photonectnews
@photonect.news""", "brief": None}


# ═══════════ D · 22:30 · P1 corruption — Salah al-Din traffic-fine receipts ═══════════
slug = f"{D}-d-salahaldin-56k-receipts"
p = base(slug, "iraq_money", "B", "النزاهة", "النزاهة: 56 ألف وصل غرامة.. وأكثر من ملياري دينار",
  ("SALAH AL-DIN · OCT 7 | FEDERAL INTEGRITY COMMISSION (VIA SHAFAQ NEWS, 964, BAGHDAD TODAY): COLONEL HEADING THE FINES SECTION "
   "ACCUSED OF MANIPULATING 34,164 TRAFFIC-FINE RECEIPTS, EMBEZZLING 1,853,200,000 IQD | SECOND COLONEL: 22,000 RECEIPTS, 339,135,000 IQD | "
   "BOTH DETAINED PENDING INVESTIGATION (ART. 315) | 1 BRIGADIER + 2 COLONELS PROBED FOR FAILING TO AUDIT | NO CONVICTION"))
p["beats"] = [
 beat("العملية الأولى", "34,164 وصلاً.. و1.85 مليار",
  "هيئة النزاهة: عقيد مسؤول عن شعبة الغرامات في مرور صلاح الدين متهم بالتلاعب بـ34,164 وصل غرامة واختلاس 1,853,200,000 دينار. وهو موقوف على ذمة التحقيق.",
  "34,164", "Traffic-fine receipts allegedly manipulated by the fines-section colonel (Integrity Commission via Shafaq / 964)",
  "وصل غرامة — العملية الأولى",
  [("المبلغ", "1,853,200,000 دينار"), ("المتهم", "عقيد موقوف"), ("المادة", "315")], 1, slug,
  ["مرور صلاح الدين", "34,164 وصل غرامة", "1.85 مليار دينار"], STOCK),
 beat("العملية الثانية", "22 ألف وصل.. و339 مليوناً",
  "وفي عملية ثانية، تتهم الهيئة عقيداً آخر موقوفاً بالتلاعب بوصولات الغرامات الفورية واختلاس 339,135,000 دينار، وضُبط 22,000 وصل.",
  "22,000", "Receipts seized in the second operation; 339,135,000 IQD allegedly embezzled (Integrity Commission via Shafaq / 964)",
  "وصل ضُبط — العملية الثانية",
  [("المبلغ", "339,135,000 دينار"), ("المجموع", "56,164 وصلاً (محتسب)"), ("الإجمالي", "2,192,335,000 (محتسب)")], 2, slug,
  ["عقيد ثانٍ موقوف", "22,000 وصل", "339 مليون دينار"], STOCK),
 beat("التدقيق", "التحقيق يشمل عميداً وعقيدين",
  "تقول الهيئة إن التحقيق يشمل ثلاثة ضباط آخرين، عميداً وعقيدين، لعدم تدقيقهم الإرساليات بدقة. القضية أمام قاضي التحقيق ولم تصدر إدانة.",
  "5", "Officers in the investigation: 2 detained colonels + 1 brigadier and 2 colonels probed for failing to audit (Integrity via 964)",
  "ضباط يشملهم التحقيق",
  [("موقوفان", "عقيدان"), ("قيد التحقيق", "عميد وعقيدان"), ("الحكم", "لم يصدر")], 3, slug,
  ["5 ضباط بالتحقيق", "بينهم عميد", "ولا إدانة بعد"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة: التلاعب بأكثر من 56 ألف وصل غرامة مرورية في صلاح الدين",
 "عقيد مسؤول شعبة الغرامات متهم باختلاس 1,853,200,000 دينار",
 "عقيد ثانٍ متهم باختلاس 339,135,000 دينار — كلاهما موقوف على ذمة التحقيق",
 "التحقيق يشمل عميداً وعقيدين لعدم التدقيق — ولم تصدر إدانة",
 "دفعت غرامة مرور هالسنة؟"]
p["endQuestion"] = "دفعت غرامة مرور هالسنة؟"
p["sources"] = [{"name": "هيئة النزاهة الاتحادية", "domain": "nazaha.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """غرامات المرور في صلاح الدين — شنو كشفت هيئة النزاهة؟

آلاف الوصولات ومليارات الدنانير.. والضباط موقوفون على ذمة التحقيق. التفاصيل بالفيديو.

دفعت غرامة مرور هالسنة؟

المصادر: هيئة النزاهة الاتحادية عبر شفق نيوز، شبكة 964، بغداد اليوم (7 تشرين الأول 2026)

#هيئة_النزاهة #صلاح_الدين #غرامات_المرور #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "النزاهة: 56 ألف وصل غرامة مرور",
  "voText": "أعلنت هيئة النزاهة الاتحادية الأربعاء أن ضابطاً برتبة عقيد، مسؤولاً عن شعبة الغرامات في مرور صلاح الدين، متهم بالتلاعب بأكثر من أربعة وثلاثين ألف وصل غرامة، واختلاس أكثر من مليار وثمانمئة وثلاثة وخمسين مليون دينار. وفي عملية ثانية، تتهم الهيئة عقيداً آخر باختلاس ثلاثمئة وتسعة وثلاثين مليون دينار، وضُبط اثنان وعشرون ألف وصل. والضابطان موقوفان على ذمة التحقيق، الذي يشمل أيضاً عميداً وعقيدين لعدم التدقيق، ولم تصدر إدانة بعد. دفعت غرامة مرور هالسنة؟",
  "endQuestion": "دفعت غرامة مرور هالسنة؟",
  "sourcesLine": "المصادر: هيئة النزاهة الاتحادية عبر شفق نيوز · شبكة 964 · بغداد اليوم — 7 تشرين الأول 2026",
  "statPops": [{"value": "34,164", "label": "وصل غرامة — العملية الأولى", "matchWord": "الغرامات"},
               {"value": "22,000", "label": "وصل ضُبط — العملية الثانية", "matchWord": "ثانية"}]}}


# ═══════════ E · 23:45 · P3 health/environment — dust storm 139 suffocation cases ═══════════
slug = f"{D}-e-dust-139-cases"
p = base(slug, "region_life", "C", "العاصفة الترابية", "عاصفة الغبار: 139 حالة اختناق بين النجف وديالى",
  ("NAJAF / DIYALA · OCT 6 | NAJAF HEALTH MEDIA DIRECTOR MAHER AL-ABOUDI (VIA SHAFAQ NEWS): 129 SUFFOCATION CASES (AL-HAKIM 52, AL-HURRIYA 27, "
   "NAJAF TEACHING 36, AL-QADISIYA 14) | BAQUBA TEACHING: 10 | METEOROLOGY (VIA SHAFAQ, 964): DUST FROM THE WEST TO SALAH AL-DIN, BAGHDAD, "
   "NAJAF, KARBALA, NASIRIYAH | GREEN IRAQ OBSERVATORY: STORMS LIKELY THROUGH WINTER, 6 ACTIVE HOTSPOTS, >23% DESERTIFIED LAND"))
p["beats"] = [
 beat("النجف", "129 حالة اختناق بالنجف",
  "مدير إعلام صحة النجف ماهر العبودي: 129 حالة اختناق؛ 52 في مستشفى الحكيم، و36 في النجف التعليمي، و27 في الحرية، و14 في القادسية.",
  "129", "Suffocation cases in Najaf hospitals from Tuesday's dust storm (Najaf Health media director via Shafaq)", "حالة اختناق بالنجف",
  [("الحكيم", "52"), ("النجف التعليمي", "36"), ("الحرية + القادسية", "27 + 14")], 1, slug,
  ["صحة النجف: 129 حالة", "الحكيم وحده 52", "علاج ربو وأوكسجين"], STOCK),
 beat("المسار", "من الغرب إلى بغداد والنجف وكربلاء",
  "طوارئ بعقوبة التعليمي استقبلت 10 حالات. وبحسب الأنواء الجوية، امتد الغبار من المناطق الغربية إلى صلاح الدين وبغداد والنجف وكربلاء والناصرية.",
  "139", "Total suffocation cases across Najaf (129) and Diyala (10) (Shafaq; computed)", "حالة اختناق بين النجف وديالى (محتسب)",
  [("ديالى", "10"), ("الرؤية غرباً", "أقل من 1 كم"), ("المصدر", "مرتفع جوي")], 2, slug,
  ["ديالى: 10 حالات", "الغبار من الغرب", "إلى بغداد والفرات الأوسط"], STOCK),
 beat("الشتاء", "6 بؤر نشطة.. والعواصف مستمرة",
  "مرصد العراق الأخضر يرجّح استمرار العواصف الترابية في الشتاء، ويحدد 6 بؤر نشطة داخل العراق، ويقدّر الأراضي المتصحرة والمتروكة بأكثر من 23%.",
  "6", "Active dust hotspots inside Iraq (Green Iraq observatory via Shafaq)", "بؤر غبار نشطة",
  [("الأراضي المتصحرة", "أكثر من 23%"), ("المتوقع", "عواصف بالشتاء"), ("الأكثر تضرراً", "مرضى الربو")], 3, slug,
  ["العراق الأخضر: 6 بؤر", "العواصف مستمرة بالشتاء", "الأخطر على مرضى الربو"], STOCK),
]
p["arabicTicker"] = [
 "صحة النجف: 129 حالة اختناق جراء العاصفة الترابية (شفق نيوز)",
 "مستشفى بعقوبة التعليمي استقبل 10 حالات اختناق",
 "الأنواء الجوية: الغبار امتد إلى صلاح الدين وبغداد والنجف وكربلاء والناصرية",
 "مرصد العراق الأخضر: 6 بؤر نشطة والعواصف مرجحة بالشتاء",
 "عدكم أحد بالبيت عنده ربو؟"]
p["endQuestion"] = "عدكم أحد بالبيت عنده ربو؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}]
SLATE[slug] = {"props": p, "caption": """العاصفة الترابية في العراق — شكد حالة اختناق سجلت؟

مستشفيات النجف استقبلت العشرات.. والشتاء مو أحسن. التفاصيل بالفيديو.

عدكم أحد بالبيت عنده ربو؟

المصادر: صحة النجف عبر شفق نيوز، شبكة 964، بغداد اليوم، مرصد العراق الأخضر (6 و7 تشرين الأول 2026)

#العاصفة_الترابية #النجف #الربو #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "العاصفة الترابية", "hookHeadline": "الغبار يملأ طوارئ النجف",
  "voText": "قال مدير إعلام صحة النجف ماهر العبودي لشفق نيوز إن مستشفيات المحافظة استقبلت مئة وتسعاً وعشرين حالة اختناق بسبب العاصفة الترابية مساء الثلاثاء، فيما استقبل مستشفى بعقوبة التعليمي عشر حالات. وبحسب هيئة الأنواء الجوية، امتد الغبار من المناطق الغربية إلى صلاح الدين وبغداد والنجف وكربلاء والناصرية. ويرجح مرصد العراق الأخضر استمرار العواصف خلال الشتاء، ويحدد ست بؤر نشطة داخل البلاد، ويقدّر الأراضي المتصحرة والمتروكة بأكثر من ثلاثة وعشرين بالمئة. عدكم أحد بالبيت عنده ربو؟",
  "endQuestion": "عدكم أحد بالبيت عنده ربو؟",
  "sourcesLine": "المصادر: صحة النجف عبر شفق نيوز · شبكة 964 · بغداد اليوم — 6 و7 تشرين الأول 2026",
  "statPops": [{"value": "129", "label": "حالة اختناق في مستشفيات النجف", "matchWord": "اختناق"},
               {"value": "6", "label": "بؤر غبار نشطة — مرصد العراق الأخضر", "matchWord": "بؤر"}]}}


def main():
    for slug, data in SLATE.items():
        d = POSTS / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(json.dumps(data["props"], ensure_ascii=False, indent=1))
        (POSTS / slug / "caption.txt").write_text(data["caption"].strip() + "\n")
        if data["brief"]:
            b = dict(data["brief"])
            b = {"slug": slug, **b,
                 "images": [f"{IMG}/{slug}/hero.jpg"] + [f"{IMG}/{slug}/broll_{i}.jpg" for i in (1, 2, 3)],
                 "audioBed": data["props"]["audioBed"], "statPops": b.pop("statPops")}
            order = ["slug", "kicker", "hookHeadline", "voText", "endQuestion", "sourcesLine", "images", "audioBed", "statPops"]
            (d / "v11-brief.json").write_text(json.dumps({k: b[k] for k in order}, ensure_ascii=False, indent=1))
        print(f"  ✓ {slug}  (brief={'yes' if data['brief'] else 'NO — V10.1 control'})")
    print(f"\n== authored {len(SLATE)} slugs ==")

if __name__ == "__main__":
    main()
