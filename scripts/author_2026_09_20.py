#!/usr/bin/env python3
"""Author the 2026-09-20 Photonect NEWS slate: props.json + v11-brief.json + caption.txt.

Slate (posting order = alphabetical slug order):
  a 18:00  P2  تحذير أميركي: احتمال إلغاء رحلات وإغلاق أجواء        (V11)
  b 19:45  P1  الدولار اليوم + إشاعة حذف الأصفار            ANCHOR (V11)
  c 21:15  P3  300 يوم عواصف رملية و6 بؤر ساخنة                    (V11)
  d 22:30  P1  قروض الرشيد 30 مليون دينار للطاقة الشمسية            (V11)
  e 23:45  P1  الدين الداخلي 109.5 تريليون دينار        V10.1 CONTROL (silent)

Every figure below is traceable to a same-day (2026-09-20) dated article except
where the body text itself names an earlier date. Derived figures are labelled
(محتسب). voText spells every number in Arabic words because the V11 TTS has no
numeral normaliser.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
D = "2026-09-20"
DATE_EN = "SEP 20 • 2026"
DATE_AR = "20 أيلول 2026"
HANDLE = "@photonect.news"
ACC = "#FFC217"
SRC_964 = {"name": "شبكة 964", "domain": "964media.com"}
SRC_SHAFAQ = {"name": "شفق نيوز", "domain": "shafaq.com"}
SRC_HATHA = {"name": "هذا اليوم", "domain": "hathalyoum.net"}
SRC_RASHEED = {"name": "مصرف الرشيد", "domain": "rasheedbank.gov.iq"}


def img(slug: str, name: str) -> str:
    return f"images/news/{D}-{slug}/{name}"


def beat(label, heading, body, big, sup, slug, broll, phrases, src="صورة توضيحية · KIE"):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": big,
        "supportingStats": sup,
        "broll": img(slug, broll),
        "brolls": [img(slug, broll)],
        "brollType": "image",
        "accent": ACC,
        "brollSource": src,
        "subtitlePhrases": phrases,
    }


SLATE: list[dict] = []

# ─────────────────────────────────────────────────────────────── A · 18:00 · P2
s = "a-us-warning-flights"
SLATE.append({
 "slug": s, "variant": "A", "topicBucket": "mena_geo",
 "kicker": "تحذير سفر",
 "headline": "تحذير أميركي: احتمال إلغاء رحلات وإغلاق أجواء",
 "subhead": ("BAGHDAD · SEP 20 | US EMBASSY BAGHDAD STATEMENT, SUN 20 SEP: WARNS OF POSSIBLE "
             "\"UNEXPECTED ESCALATION\", SECURITY ENVIRONMENT \"REMAINS COMPLEX\"; URGES AWARENESS OF "
             "FLIGHT CANCELLATIONS, AIRSPACE CLOSURES, TRAVEL DISRUPTION | CONTEXT SAT 19 SEP (REUTERS "
             "VIA 964): EXPLOSIONS AND CIVIL-DEFENCE EMERGENCY NEAR KING KHALID INTL, RIYADH; WARNINGS "
             "COVERED RIYADH AND AL-KHARJ | IRAQ TRANSPORT MINISTRY SAT 19 SEP: LAND TRANSPORT STILL "
             "ACTIVE, >7,000 INTERNATIONAL TRANSITS REACHING CENTRAL ASIA, ~1,500 TRUCKS VIA THE "
             "WESTERN CROSSING"),
 "beats": [
   beat("التحذير", "السفارة الأميركية تحذر من تصعيد غير متوقع",
        "حذّرت السفارة الأميركية في بغداد اليوم الأحد رعاياها من \"تصعيد غير متوقع\"، وقالت إن البيئة الأمنية \"لا تزال معقدة\" (شبكة 964).",
        {"value": "3", "label": "Disruptions the embassy named: flight cancellations, airspace closures, travel disruption",
         "arabicLabel": "اضطرابات ذكرتها السفارة: إلغاء رحلات، إغلاق مجال جوي، تعطّل سفر"},
        [{"label": "إلغاء", "value": "رحلات"}, {"label": "إغلاق", "value": "أجواء"}, {"label": "تعطّل", "value": "سفر"}],
        s, "broll_2.jpg",
        ["السفارة الأميركية ببغداد", "تحذر من تصعيد", "غير متوقع"]),
   beat("الرياض", "إنذارات السبت شملت الرياض والخرج",
        "أمس السبت شوهدت انفجارات قرب مطار الملك خالد بالرياض وأعلن الدفاع المدني الطوارئ، وشملت الإنذارات الرياض والخرج (رويترز عبر شبكة 964).",
        {"value": "2", "label": "Saudi cities covered by Saturday's alerts: Riyadh and Al-Kharj, per Reuters via 964",
         "arabicLabel": "مدينتان شملهما إنذار السبت: الرياض والخرج (رويترز عبر شبكة 964)"},
        [{"label": "الرياض", "value": "إنذار"}, {"label": "الخرج", "value": "إنذار"}, {"label": "التاريخ", "value": "19 أيلول"}],
        s, "broll_1.jpg",
        ["انفجارات قرب مطار", "الملك خالد بالرياض", "والإنذار شمل الخرج"]),
   beat("على الأرض", "النقل: 7,000 عبور دولي والبر ماشي",
        "وزارة النقل قالت السبت إن تأثير الحرب على مشاريع النقل \"لا يزال محدوداً\"، وإن العبور الدولي تجاوز 7,000 ووصل أواسط آسيا (شبكة 964).",
        {"value": "7,000", "label": "International transits through Iraq reaching Central Asia, Transport Ministry, Sat 19 Sep, per 964",
         "arabicLabel": "عبور دولي عبر العراق وصل أواسط آسيا (وزارة النقل عبر شبكة 964)"},
        [{"label": "عبور دولي", "value": "7,000"}, {"label": "المنفذ الغربي", "value": "1,500"}, {"label": "التأثير", "value": "محدود"}],
        s, "broll_3.jpg",
        ["وزارة النقل تقول", "العبور الدولي تجاوز 7,000", "والتأثير لا يزال محدوداً"]),
 ],
 "ticker": [
   "السفارة الأميركية ببغداد تحذر رعاياها من \"تصعيد غير متوقع\" والبيئة الأمنية \"لا تزال معقدة\" (شبكة 964 — 20 أيلول)",
   "السفارة دعت لمتابعة احتمالات إلغاء الرحلات وإغلاق المجال الجوي واضطرابات السفر (شبكة 964)",
   "السبت: انفجارات وطوارئ قرب مطار الملك خالد بالرياض والإنذار شمل الرياض والخرج (رويترز عبر شبكة 964 — 19 أيلول)",
   "وزارة النقل: العبور الدولي تجاوز 7,000 ووصل أواسط آسيا و1,500 شاحنة عبر المنفذ الغربي (شبكة 964 — 19 أيلول)",
 ],
 "endQuestion": "مسافر هالأسبوع لو أجّلت؟",
 "sources": [SRC_964, SRC_SHAFAQ],
 "v11": {
   "hookHeadline": "رحلتك ممكن تنلغي؟",
   "voText": ("حذّرت السفارة الأميركية في بغداد اليوم الأحد رعاياها من تصعيد غير متوقع، وقالت إن البيئة "
              "الأمنية لا تزال معقدة. ودعت إلى متابعة احتمالات إلغاء الرحلات وإغلاق المجال الجوي "
              "واضطرابات السفر. وكانت انفجارات قد سُمعت أمس قرب مطار الملك خالد في الرياض، وشمل "
              "الإنذار الرياض والخرج، بحسب رويترز. في المقابل، قالت وزارة النقل العراقية إن العبور "
              "الدولي تجاوز سبعة آلاف ووصل أواسط آسيا، وإن نحو ألف وخمسمئة شاحنة تخرج عبر المنفذ "
              "الغربي. مسافر هالأسبوع لو أجّلت؟"),
   "endQuestion": "مسافر هالأسبوع لو أجّلت؟",
   "sourcesLine": "المصادر: شبكة 964 · رويترز · وزارة النقل — 20 أيلول 2026",
   "statPops": [
     {"value": "7,000", "label": "عبور دولي وصل أواسط آسيا", "matchWord": "آسيا"},
     {"value": "1,500", "label": "شاحنة عبر المنفذ الغربي", "matchWord": "شاحنة"},
   ],
 },
 "caption": ("تحذير سفر في الشرق الأوسط — شنو يعني لرحلتك؟\n\n"
             "السفارة الأميركية ببغداد تتحدث عن احتمال إلغاء رحلات وإغلاق مجال جوي.. ووزارة النقل تقول البر ماشي.\n\n"
             "مسافر هالأسبوع لو أجّلت؟\n\n"
             "المصادر: شبكة 964، رويترز، وزارة النقل (20 أيلول 2026)\n\n"
             "#العراق #أخبار_العراق #السفر #مطار_بغداد #الشرق_الأوسط\n"
             "@photonect.news\n"),
})

# ───────────────────────────────────────────────── B · 19:45 · P1 · ANCHOR دولار
s = "b-dollar-159750-zero-rumor"
SLATE.append({
 "slug": s, "variant": "B", "topicBucket": "iraq_money",
 "kicker": "الدولار اليوم",
 "headline": "الدولار نزل تحت 160 ألف.. والرسمي بعده 131",
 "subhead": ("BAGHDAD · SEP 20 | 964 MORNING LIST (10:45, SUN 20 SEP), IRAQ BOURSES PER $100: BAGHDAD "
             "SELL 159,750 / BUY 159,000; ERBIL SELL 158,700 / BUY 158,250; BASRA SELL 159,000 / BUY "
             "158,500; CBI OFFICIAL RATE 131,000 | SHAFAQ (MORNING, SUN 20 SEP): KIFAH & HARITHIYA "
             "BOURSES 159,250, DOWN FROM 159,750 ON SATURDAY PER SHAFAQ'S OWN COMPARISON; BAGHDAD SHOPS "
             "SELL 159,750 / BUY 158,750 | GAP TO OFFICIAL 28,750 (COMPUTED FROM 964'S OWN TWO FIGURES) "
             "| GOLD, SHAFAQ SUN 20 SEP: NAHR ST WHOLESALE 21K GULF MITHQAL SELL 983,000, DOWN FROM "
             "985,000 SATURDAY"),
 "beats": [
   beat("الأسعار", "بغداد اليوم: بيع 159,750 وشراء 159,000",
        "قائمة 964 الصباحية اليوم الأحد لبورصات العراق: بغداد بيع 159,750، أربيل بيع 158,700، البصرة بيع 159,000 لكل 100 دولار.",
        {"value": "159,750", "label": "Dinars, selling price per $100 at Baghdad bourses, Sunday morning, per 964",
         "arabicLabel": "دينار سعر بيع 100 دولار في بورصات بغداد صباح الأحد (شبكة 964)"},
        [{"label": "أربيل", "value": "158,700"}, {"label": "البصرة", "value": "159,000"}, {"label": "الرسمي", "value": "131,000"}],
        s, "broll_1.jpg",
        ["بورصات بغداد اليوم", "بيع 159,750", "وأربيل 158,700"]),
   beat("ليش", "خبير: إشاعة حذف الأصفار دفعت الناس للدولار",
        "الباحث الاقتصادي عمرو هشام عزا الارتفاع الأخير لتصريحات عن \"حذف أصفار\" من العملة دفعت قسماً من المواطنين لشراء الدولار للتحوّط (شبكة 964).",
        {"value": "4", "label": "Drivers the researcher listed: zero-deletion talk, regional tension, reserve pressure, delayed dollar shipment",
         "arabicLabel": "أسباب عدّها الباحث: حذف الأصفار، توترات المنطقة، ضغط الاحتياطيات، تأخر شحنة الدولار"},
        [{"label": "السبب الأول", "value": "حذف الأصفار"}, {"label": "الثاني", "value": "التوترات"}, {"label": "الثالث", "value": "الاحتياطيات"}],
        s, "broll_2.jpg",
        ["الباحث عمرو هشام", "حذف الأصفار دفع الناس", "لشراء الدولار للتحوّط"]),
   beat("الذهب", "الذهب نزل وياه: المثقال 983 ألفاً",
        "مع تراجع الدولار صباح اليوم نزل بيع مثقال الذهب الخليجي عيار 21 في شارع النهر إلى 983 ألف دينار بعد 985 أمس (شفق نيوز).",
        {"value": "983,000", "label": "Dinars, wholesale selling price of one 21k Gulf mithqal on Nahr St, Sunday, per Shafaq",
         "arabicLabel": "دينار سعر بيع مثقال الذهب الخليجي عيار 21 بشارع النهر الأحد (شفق نيوز)"},
        [{"label": "أمس", "value": "985,000"}, {"label": "اليوم", "value": "983,000"}, {"label": "العراقي", "value": "953,000"}],
        s, "broll_3.jpg",
        ["الذهب نزل وياه", "المثقال الخليجي 983 ألفاً", "بعد 985 أمس"]),
 ],
 "ticker": [
   "بورصات بغداد صباح الأحد: البيع 159,750 والشراء 159,000 لكل 100 دولار (شبكة 964 — 20 أيلول)",
   "أربيل: البيع 158,700 والشراء 158,250 — البصرة: البيع 159,000 والشراء 158,500 (شبكة 964)",
   "شفق نيوز: بورصتا الكفاح والحارثية 159,250 اليوم بعد 159,750 أمس السبت",
   "السعر الرسمي للبنك المركزي 131,000 دينار لكل 100 دولار — الفرق عن بيع بغداد 28,750 (محتسب من رقمَي شبكة 964)",
   "الذهب: مثقال عيار 21 الخليجي بشارع النهر 983,000 دينار بعد 985,000 أمس (شفق نيوز)",
 ],
 "endQuestion": "بكم اشتريت الدولار آخر مرة؟",
 "sources": [SRC_964, SRC_SHAFAQ],
 "v11": {
   "hookHeadline": "ليش الناس تشتري دولار؟",
   "voText": ("تراجع الدولار قليلاً في أسواق العراق اليوم الأحد. فبحسب شبكة تسعة ستة أربعة، باعت "
              "بورصات بغداد كل مئة دولار بمئة وتسعة وخمسين ألفاً وسبعمئة وخمسين ديناراً، وفي أربيل "
              "بمئة وثمانية وخمسين ألفاً وسبعمئة، وفي البصرة بمئة وتسعة وخمسين ألفاً. أما السعر "
              "الرسمي للبنك المركزي فما زال مئة وواحداً وثلاثين ألفاً. ويعزو الباحث الاقتصادي عمرو "
              "هشام الصعود الأخير إلى تصريحات عن حذف أصفار من العملة دفعت مواطنين للتحوّط. بكم "
              "اشتريت الدولار آخر مرة؟"),
   "endQuestion": "بكم اشتريت الدولار آخر مرة؟",
   "sourcesLine": "المصادر: شبكة 964 · شفق نيوز — 20 أيلول 2026",
   "statPops": [
     {"value": "159,750", "label": "بيع 100 دولار ببورصات بغداد", "matchWord": "بورصات"},
     {"value": "131,000", "label": "السعر الرسمي للبنك المركزي", "matchWord": "الرسمي"},
   ],
 },
 "caption": ("سعر الدولار اليوم في العراق — نزل لو طلع؟\n\n"
             "بورصات بغداد تبيع المية دولار بـ159,750.. والسبب وراء الحركة صار حديث السوق.\n\n"
             "بكم اشتريت الدولار آخر مرة؟\n\n"
             "المصادر: شبكة 964، شفق نيوز (20 أيلول 2026)\n\n"
             "#سعر_الدولار_اليوم #الدينار_العراقي #العراق #بغداد #الذهب\n"
             "@photonect.news\n"),
})

# ─────────────────────────────────────────────────────────────── C · 21:15 · P3
s = "c-sandstorms-300-days"
SLATE.append({
 "slug": s, "variant": "A", "topicBucket": "region_health",
 "kicker": "تحذير مناخي",
 "headline": "300 يوم غبار بالسنة.. وتحذير من 6 بؤر",
 "subhead": ("BAGHDAD · SEP 20 | IRAQ GREEN OBSERVATORY STATEMENT, SUN 20 SEP, VIA 964: DUST AND SAND "
             "STORMS FORECAST TO REACH 300 DAYS A YEAR WITHIN THE NEXT TEN YEARS; 6 HOTSPOTS IDENTIFIED "
             "IN CENTRAL, WESTERN AND SOUTHERN IRAQ, MOSTLY ENDEMIC TO SOUTHERN PROVINCES, FORMED BY "
             "DESERTIFICATION; MAXIMUM 1951-1990 WAS ABOUT 24 STORMS A YEAR | ALSO CARRIED BY SHAFAQ"),
 "beats": [
   beat("التوقع", "مرصد: 300 يوم عواصف خلال عشر سنوات",
        "مرصد العراق الأخضر أعلن اليوم الأحد توقّع وصول العواصف الترابية والرملية إلى 300 يوم سنوياً خلال السنوات العشر المقبلة (شبكة 964).",
        {"value": "300", "label": "Days of dust and sand storms a year forecast within ten years, Iraq Green Observatory via 964",
         "arabicLabel": "يوم عواصف ترابية ورملية سنوياً متوقعة خلال عشر سنوات (مرصد العراق الأخضر عبر شبكة 964)"},
        [{"label": "المدى", "value": "10 سنوات"}, {"label": "المتوقع", "value": "300 يوم"}, {"label": "البؤر", "value": "6"}],
        s, "broll_2.jpg",
        ["مرصد العراق الأخضر", "يتوقع 300 يوم عواصف", "خلال عشر سنوات"]),
   beat("البؤر", "6 بؤر ساخنة أغلبها بالجنوب",
        "المرصد حدّد 6 بؤر تنطلق منها العواصف في وسط العراق وغربه وجنوبه، وقال إن غالبيتها متوطنة بالمحافظات الجنوبية بسبب التصحّر (شبكة 964).",
        {"value": "6", "label": "Hotspots the observatory identified in central, western and southern Iraq",
         "arabicLabel": "بؤر ساخنة حدّدها المرصد في وسط العراق وغربه وجنوبه (مرصد العراق الأخضر)"},
        [{"label": "الوسط", "value": "بؤر"}, {"label": "الغرب", "value": "بؤر"}, {"label": "الجنوب", "value": "الأغلب"}],
        s, "broll_1.jpg",
        ["ست بؤر ساخنة", "بوسط العراق وغربه وجنوبه", "والسبب التصحّر"]),
   beat("المقارنة", "من 24 عاصفة بالسنة إلى 300 يوم",
        "الحد الأقصى بين 1951 و1990 كان نحو 24 عاصفة سنوياً، مقابل ما يصل إلى 300 يوم متوقعة خلال عقد، بحسب المرصد (شبكة 964).",
        {"value": "24", "label": "Maximum storms a year recorded 1951-1990, per the observatory via 964",
         "arabicLabel": "أقصى عدد عواصف سنوياً بين 1951 و1990 (مرصد العراق الأخضر عبر شبكة 964)"},
        [{"label": "1951-1990", "value": "24"}, {"label": "المتوقع", "value": "300"}, {"label": "السبب", "value": "التصحّر"}],
        s, "broll_3.jpg",
        ["بين 1951 و1990", "كانت 24 عاصفة بالسنة", "واليوم التوقع 300 يوم"]),
 ],
 "ticker": [
   "مرصد العراق الأخضر: العواصف الترابية والرملية قد تصل 300 يوم سنوياً خلال عشر سنوات (شبكة 964 — 20 أيلول)",
   "المرصد: 6 بؤر ساخنة تنطلق منها العواصف بوسط العراق وغربه وجنوبه، أغلبها متوطن بالجنوب",
   "المرصد: الحد الأقصى بين 1951 و1990 كان نحو 24 عاصفة سنوياً",
   "المرصد يربط تكوّن البؤر بالتصحّر الذي أصاب غالبية الأراضي بتلك المناطق (شبكة 964)",
 ],
 "endQuestion": "شكد يوم انقطع دوام أولادك بسبب الغبار؟",
 "sources": [SRC_964, SRC_SHAFAQ],
 "v11": {
   "hookHeadline": "300 يوم غبار بالسنة؟",
   "voText": ("حذّر مرصد العراق الأخضر اليوم الأحد من أن العواصف الترابية والرملية قد تصل إلى ثلاثمئة "
              "يوم سنوياً خلال السنوات العشر المقبلة. وحدّد المرصد ست بؤر ساخنة تنطلق منها هذه "
              "العواصف في وسط العراق وغربه وجنوبه، وقال إن غالبيتها متوطنة في المحافظات الجنوبية، "
              "وإن تكوّنها يعود إلى التصحّر. وللمقارنة، كان الحد الأقصى بين عامي واحد وخمسين وتسعين "
              "نحو أربع وعشرين عاصفة في السنة. وأشار المرصد إلى أن هذه البؤر تكوّنت بفعل التصحّر الذي "
              "أصاب غالبية الأراضي في تلك المناطق. شكد يوم انقطع دوام أولادك بسبب الغبار؟"),
   "endQuestion": "شكد يوم انقطع دوام أولادك بسبب الغبار؟",
   "sourcesLine": "المصادر: مرصد العراق الأخضر · شبكة 964 · شفق نيوز — 20 أيلول 2026",
   "statPops": [
     {"value": "300", "label": "يوم عواصف سنوياً متوقعة", "matchWord": "سنوياً"},
     {"value": "6", "label": "بؤر ساخنة للعواصف", "matchWord": "بؤر"},
   ],
 },
 "caption": ("العواصف الترابية في العراق — شنو ينتظرنا؟\n\n"
             "مرصد العراق الأخضر يتكلم عن رقم مخيف للأيام المغبرة خلال عشر سنوات.. والسبب مو الطقس بس.\n\n"
             "شكد يوم انقطع دوام أولادك بسبب الغبار؟\n\n"
             "المصادر: مرصد العراق الأخضر، شبكة 964، شفق نيوز (20 أيلول 2026)\n\n"
             "#العراق #العواصف_الترابية #الغبار #التصحر #البصرة\n"
             "@photonect.news\n"),
})

# ─────────────────────────────────────────────────────── D · 22:30 · P1 · كهرباء
s = "d-solar-loans-30-million"
SLATE.append({
 "slug": s, "variant": "B", "topicBucket": "iraq_services",
 "kicker": "قروض",
 "headline": "قرض حتى 30 مليوناً للطاقة الشمسية بفائدة 3%",
 "subhead": ("BAGHDAD · SEP 20 | RASHEED BANK STATEMENT, SUN 20 SEP, VIA 964: LOANS LAUNCHED FOR "
             "RENEWABLE AND SOLAR SYSTEMS, FUNDED BY THE CENTRAL BANK OF IRAQ, CEILING 30 MILLION "
             "DINARS; OPEN TO CITIZENS AND STATE EMPLOYEES; TOTAL INTEREST 3% A YEAR; REPAYMENT UP TO 7 "
             "YEARS; GRACE PERIOD UP TO 6 MONTHS | APPLICATION VIA THE UR PLATFORM PER HATHALYOUM | "
             "ALSO ON RASHEED BANK'S OWN SOLAR-LOANS PAGE"),
 "beats": [
   beat("القرض", "الرشيد: قرض حتى 30 مليون دينار",
        "مصرف الرشيد أعلن اليوم الأحد إطلاق قروض لشراء منظومات الطاقة الشمسية والمتجددة بتمويل من البنك المركزي وبحد أقصى 30 مليون دينار (شبكة 964).",
        {"value": "30", "label": "Million dinars, the loan ceiling, Rasheed Bank statement Sun 20 Sep via 964",
         "arabicLabel": "مليون دينار الحد الأقصى للقرض (مصرف الرشيد عبر شبكة 964)"},
        [{"label": "الفائدة", "value": "3%"}, {"label": "السداد", "value": "7 سنوات"}, {"label": "الإمهال", "value": "6 أشهر"}],
        s, "broll_2.jpg",
        ["مصرف الرشيد يطلق", "قرضاً حتى 30 مليون دينار", "للطاقة الشمسية"]),
   beat("الشروط", "فائدة 3% وسداد يوصل 7 سنوات",
        "القروض تشمل المواطنين والموظفين بفائدة إجمالية 3% سنوياً، ومدة سداد تصل إلى 7 سنوات، مع فترة إمهال تصل إلى 6 أشهر (شبكة 964).",
        {"value": "3%", "label": "Total annual interest on the loan, per Rasheed Bank via 964",
         "arabicLabel": "الفائدة الإجمالية السنوية على القرض (مصرف الرشيد عبر شبكة 964)"},
        [{"label": "المشمولون", "value": "مواطنون وموظفون"}, {"label": "السداد", "value": "7 سنوات"}, {"label": "الفائدة", "value": "3%"}],
        s, "broll_1.jpg",
        ["فائدة إجمالية 3% سنوياً", "وسداد يوصل سبع سنوات", "وإمهال ستة أشهر"]),
   beat("ليش يهمك", "إمهال 6 أشهر قبل أول قسط",
        "المصرف قال إن المبادرة تدعم الطاقة النظيفة وتقلل الاعتماد على المصادر التقليدية، والتقديم يجري عبر منصة أور (هذا اليوم).",
        {"value": "6", "label": "Months of grace before repayment starts, per Rasheed Bank via 964",
         "arabicLabel": "أشهر فترة الإمهال قبل بدء السداد (مصرف الرشيد عبر شبكة 964)"},
        [{"label": "الإمهال", "value": "6 أشهر"}, {"label": "التمويل", "value": "البنك المركزي"}, {"label": "التقديم", "value": "منصة أور"}],
        s, "broll_3.jpg",
        ["إمهال ستة أشهر", "قبل أول قسط", "والتقديم عبر منصة أور"]),
 ],
 "ticker": [
   "مصرف الرشيد يطلق قروضاً لشراء منظومات الطاقة الشمسية والمتجددة بحد أقصى 30 مليون دينار (شبكة 964 — 20 أيلول)",
   "التمويل من البنك المركزي العراقي، والقروض تشمل المواطنين والموظفين (مصرف الرشيد)",
   "الفائدة الإجمالية 3% سنوياً ومدة السداد تصل إلى 7 سنوات (شبكة 964)",
   "فترة إمهال تصل إلى 6 أشهر، والتقديم عبر منصة أور (هذا اليوم · مصرف الرشيد)",
 ],
 "endQuestion": "شكد تدفع للمولدة بالشهر؟",
 "sources": [SRC_964, SRC_HATHA, SRC_RASHEED],
 "v11": {
   "hookHeadline": "شكد تدفع للمولدة؟",
   "voText": ("أعلن مصرف الرشيد اليوم الأحد إطلاق قروض لشراء منظومات الطاقة الشمسية والمتجددة، "
              "بتمويل من البنك المركزي العراقي، وبحد أقصى ثلاثين مليون دينار. وقال المصرف إن القروض "
              "تشمل المواطنين والموظفين، وإن الفائدة الإجمالية ثلاثة بالمئة سنوياً، ومدة السداد تصل "
              "إلى سبع سنوات، مع فترة إمهال تصل إلى ستة أشهر قبل بدء التسديد. وأضاف المصرف أن المبادرة "
              "تأتي في إطار دعم استخدام الطاقة النظيفة وتقليل الاعتماد على مصادر الطاقة "
              "التقليدية، وأن التمويل مقدَّم من البنك المركزي العراقي. شكد تدفع للمولدة بالشهر؟"),
   "endQuestion": "شكد تدفع للمولدة بالشهر؟",
   "sourcesLine": "المصادر: مصرف الرشيد · شبكة 964 · هذا اليوم — 20 أيلول 2026",
   "statPops": [
     {"value": "30", "label": "مليون دينار سقف القرض", "matchWord": "ثلاثين"},
     {"value": "6", "label": "أشهر فترة الإمهال", "matchWord": "إمهال"},
   ],
 },
 "caption": ("قرض الطاقة الشمسية بالعراق — شنو شروطه؟\n\n"
             "مصرف الرشيد فتح تمويلاً لمنظومات الطاقة الشمسية للمواطنين والموظفين.. والتفاصيل بالفيديو.\n\n"
             "شكد تدفع للمولدة بالشهر؟\n\n"
             "المصادر: مصرف الرشيد، شبكة 964، هذا اليوم (20 أيلول 2026)\n\n"
             "#العراق #الطاقة_الشمسية #مصرف_الرشيد #الكهرباء #المولدة\n"
             "@photonect.news\n"),
})

# ────────────────────────────────────────── E · 23:45 · P1 · V10.1 SILENT CONTROL
s = "e-public-debt-109-trillion"
SLATE.append({
 "slug": s, "variant": "C", "topicBucket": "iraq_money",
 "kicker": "الدين الداخلي",
 "headline": "الدين الداخلي 109.5 تريليون.. وارتفاع 21% بسبعة أشهر",
 "subhead": ("BAGHDAD · SEP 20 | CBI DATA VIA SHAFAQ, SUN 20 SEP: TOTAL INTERNAL PUBLIC DEBT ~109.5 "
             "TRILLION DINARS AT END-JULY 2026 VS ~90.5 TRILLION AT END-2025, +19 TRILLION / +21% IN "
             "SEVEN MONTHS; PATH 103.2T END-MAY, 106.1T END-JUNE, 109.5T END-JULY; COMPOSITION: MOF "
             "CLAIMS HELD BY CBI 72.5T, LOANS 18.95T, BONDS 9.33T, TREASURY TRANSFERS 8.74T | ECONOMIST "
             "NABIL AL-MARSOUMI VIA 964, SUN 20 SEP: DISCOUNTED TRANSFERS AT THE CBI ARE 66% OF "
             "INTERNAL DEBT; BORROWING SPENT ON SALARIES AND CONSUMPTION LIFTS IMPORT DEMAND AND DRAINS "
             "FX RESERVES"),
 "beats": [
   beat("الرقم", "الدين الداخلي 109.5 تريليون دينار",
        "بيانات البنك المركزي تُظهر ارتفاع الدين العام الداخلي إلى نحو 109.5 تريليون دينار بنهاية تموز، مقابل 90.5 تريليون بنهاية 2025 (شفق نيوز).",
        {"value": "109.5", "label": "Trillion dinars, Iraq's internal public debt at end-July 2026, CBI data via Shafaq",
         "arabicLabel": "تريليون دينار الدين العام الداخلي بنهاية تموز 2026 (بيانات البنك المركزي عبر شفق نيوز)"},
        [{"label": "نهاية 2025", "value": "90.5"}, {"label": "تموز 2026", "value": "109.5"}, {"label": "الزيادة", "value": "19"}],
        s, "broll_1.jpg",
        ["الدين العام الداخلي", "109.5 تريليون دينار", "بنهاية تموز"]),
   beat("التوزيع", "72.5 تريليوناً منها لدى البنك المركزي",
        "يتوزع الدين بين 72.5 تريليون مطالبات لوزارة المالية لدى المركزي، و18.95 تريليون قروضاً، و9.33 تريليون سندات، و8.74 تريليون حوالات خزينة (شفق نيوز).",
        {"value": "66%", "label": "Share of internal debt made up of transfers discounted at the CBI, economist Nabil al-Marsoumi via 964",
         "arabicLabel": "حصة الحوالات المخصومة لدى البنك المركزي من الدين الداخلي (نبيل المرسومي عبر شبكة 964)"},
        [{"label": "المركزي", "value": "72.5"}, {"label": "قروض", "value": "18.95"}, {"label": "سندات", "value": "9.33"}],
        s, "broll_3.jpg",
        ["72.5 تريليوناً منها", "مطالبات لدى البنك المركزي", "أي 66% من الدين"]),
   beat("الاحتياطي", "المرسومي: قروض الرواتب تستنزف الاحتياطي",
        "الخبير نبيل المرسومي قال إن تخصيص الاقتراض الداخلي لتمويل الرواتب والإنفاق الاستهلاكي يرفع الطلب على المستوردات ويستنزف جزءاً من الاحتياطيات الأجنبية (شبكة 964).",
        {"value": "21%", "label": "Rise in Iraq's internal debt across seven months of 2026, CBI data via Shafaq",
         "arabicLabel": "نسبة ارتفاع الدين الداخلي خلال سبعة أشهر من 2026 (بيانات البنك المركزي عبر شفق نيوز)"},
        [{"label": "أيار", "value": "103.2"}, {"label": "حزيران", "value": "106.1"}, {"label": "تموز", "value": "109.5"}],
        s, "broll_2.jpg",
        ["المرسومي يقول", "قروض الرواتب والإنفاق", "تستنزف الاحتياطي الأجنبي"]),
 ],
 "ticker": [
   "بيانات البنك المركزي: الدين العام الداخلي نحو 109.5 تريليون دينار بنهاية تموز 2026 (شفق نيوز — 20 أيلول)",
   "مقابل نحو 90.5 تريليون دينار بنهاية 2025، أي زيادة 19 تريليوناً وبنسبة 21% خلال سبعة أشهر (شفق نيوز)",
   "التوزيع: 72.5 تريليون مطالبات لدى المركزي، 18.95 تريليون قروض، 9.33 تريليون سندات، 8.74 تريليون حوالات خزينة (شفق نيوز)",
   "نبيل المرسومي: الحوالات المخصومة لدى المركزي تشكل 66% من الدين الداخلي (شبكة 964 — 20 أيلول)",
   "المرسومي: تمويل الرواتب والإنفاق الاستهلاكي بالاقتراض يرفع الطلب على المستوردات ويستنزف الاحتياطيات (شبكة 964)",
 ],
 "endQuestion": "راتبك وصل بموعده هذا الشهر لو تأخر؟",
 "sources": [SRC_SHAFAQ, SRC_964],
 "v11": None,   # ← silent V10.1 control
 "caption": ("الدين الداخلي للعراق — شنو يعني لراتبك؟\n\n"
             "بيانات البنك المركزي تكشف قفزة بالدين الداخلي خلال سبعة أشهر.. وخبير يربطها بالاحتياطي الأجنبي.\n\n"
             "راتبك وصل بموعده هذا الشهر لو تأخر؟\n\n"
             "المصادر: شفق نيوز، شبكة 964 (20 أيلول 2026)\n\n"
             "#العراق #الدين_العام #البنك_المركزي #الرواتب #اقتصاد_العراق\n"
             "@photonect.news\n"),
})


PERSIAN = re.compile(r"[یکپچژگ]")


def write() -> None:
    for item in SLATE:
        slug = f"{D}-{item['slug']}"
        d = POSTS / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        props = {
            "dateLabel": DATE_EN,
            "arabicDateLabel": DATE_AR,
            "handle": HANDLE,
            "audioBed": "audio/mood_newsroom.mp3",
            "topicBucket": item["topicBucket"],
            "variant": item["variant"],
            "breaking": {
                "arabicKicker": item["kicker"],
                "arabicHeadline": item["headline"],
                "englishSubhead": item["subhead"],
                "heroMedia": img(item["slug"], "hero.jpg"),
                "heroMediaType": "image",
            },
            "beats": item["beats"],
            "arabicTicker": item["ticker"],
            "endQuestion": item["endQuestion"],
            "sources": item["sources"],
        }
        (d / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=1), encoding="utf-8")
        (POSTS / slug / "caption.txt").write_text(item["caption"], encoding="utf-8")
        if item["v11"]:
            v = item["v11"]
            brief = {
                "slug": slug,
                "kicker": item["kicker"],
                "hookHeadline": v["hookHeadline"],
                "voText": v["voText"],
                "endQuestion": v["endQuestion"],
                "sourcesLine": v["sourcesLine"],
                "images": [img(item["slug"], n) for n in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")],
                "audioBed": "audio/mood_newsroom.mp3",
                "statPops": v["statPops"],
            }
            (d / "v11-brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=1), encoding="utf-8")
        else:
            (d / "v11-brief.json").unlink(missing_ok=True)
        print(f"wrote {slug}  v11={'yes' if item['v11'] else 'NO (control)'}")


def check() -> int:
    bad = 0
    for item in SLATE:
        slug = f"{D}-{item['slug']}"
        blob = json.dumps(item, ensure_ascii=False)
        for m in PERSIAN.finditer(blob):
            print(f"  ✗ {slug}: Persian char U+{ord(m.group()):04X} {m.group()!r}")
            bad += 1
            break
        for b in item["beats"]:
            w = len(b["arabicHeading"].split())
            if w > 8:
                print(f"  ✗ {slug}: heading {w} words > 8 — {b['arabicHeading']}")
                bad += 1
            w = len(b["arabicBody"].split())
            if w > 26:
                print(f"  ✗ {slug}: body {w} words > 26")
                bad += 1
        v = item["v11"]
        if v:
            if len(v["hookHeadline"].split()) > 7:
                print(f"  ✗ {slug}: hookHeadline > 7 words")
                bad += 1
            n = len(v["voText"].split())
            if not (70 <= n <= 90):
                print(f"  ! {slug}: voText {n} words (target 70-85)")
            if len(v["statPops"]) > 2:
                print(f"  ✗ {slug}: >2 statPops")
                bad += 1
            vo_words = set(re.findall(r"[^\s،.؟!]+", v["voText"]))
            for p in v["statPops"]:
                mw = p["matchWord"]
                if len(mw.split()) != 1:
                    print(f"  ✗ {slug}: matchWord {mw!r} is not ONE word")
                    bad += 1
                elif mw not in vo_words:
                    print(f"  ✗ {slug}: matchWord {mw!r} not a standalone word in voText")
                    bad += 1
            if not v["voText"].rstrip().endswith(v["endQuestion"]):
                print(f"  ✗ {slug}: voText does not end in endQuestion")
                bad += 1
        if not isinstance(item["sources"], list):
            print(f"  ✗ {slug}: sources is not a list")
            bad += 1
    print("checks:", "ALL PASS" if not bad else f"{bad} PROBLEM(S)")
    return bad


if __name__ == "__main__":
    n = check()
    write()
    raise SystemExit(0)
