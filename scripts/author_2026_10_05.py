#!/usr/bin/env python3
"""Author the 2026-10-05 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source (PM office, MoT and Integrity Commission statements via Shafaq / 964 / Ultra Iraq; Najaf agriculture via Shafaq / Video News Agency). Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + two gate passes (apply_gate*_2026_10_05.py)
then edited the files on disk — do NOT re-run this script, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_10_05.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-05"
DATE_LABEL = "OCT 05 • 2026"
AR_DATE = "5 تشرين الأول 2026"
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

# ═══════════ A · 18:00 · P1 money (LEAD) — PM al-Zaidi's 3.5T IQD package ═══════════
slug = f"{D}-a-package-3-5-trillion"
p = base(slug, "iraq_money", "A", "الحزمة الاقتصادية", "3.5 تريليون دينار.. منها مستحقات المزارعين والمقاولين",
  ("BAGHDAD · OCT 4 | PM ALI AL-ZAIDI'S OFFICE (VIA SHAFAQ NEWS, 964, ULTRA IRAQ): 3.5T IQD PACKAGE — 1T OF CBI INITIATIVES TO "
   "REAL ESTATE & HOUSING, ≥1T EXTRA LIQUIDITY FOR TBI + INDUSTRIAL BANK, 500B FOR CONTRACTORS' DUES, 500B FOR FARMERS' DUES, "
   "500B MORE FOR THE GENERATIONS FUND (1T -> 1.5T)"))
p["beats"] = [
 beat("الإسكان والصناعة", "تريليونان للسكن والمصانع",
  "بيان مكتب رئيس الوزراء علي الزيدي: تريليون دينار من مبادرات البنك المركزي للعقار والإسكان، وتريليون إضافي على الأقل لمصرفي التجارة والصناعي.",
  "2", "Trillion IQD: 1T of CBI initiatives to housing + at least 1T extra liquidity for TBI & Industrial Bank (PM office via Shafaq / 964)",
  "تريليون دينار للإسكان والصناعة",
  [("الإسكان", "1 تريليون"), ("التجارة والصناعي", "1 تريليون على الأقل"), ("مجموع الحزمة", "3.5 تريليون")], 1, slug,
  ["حزمة 3.5 تريليون", "تريليون للإسكان", "وتريليون للصناعة"], STOCK),
 beat("المستحقات", "500 مليار للمزارعين.. و500 للمقاولين",
  "بحسب البيان، تموّل وزارة المالية مستحقات المقاولين بـ500 مليار دينار، وتُسدَّد مستحقات المزارعين بـ500 مليار دينار أخرى.",
  "500", "Billion IQD each: contractors' dues (funded by MoF) and farmers' dues (PM office statement via Shafaq / 964 / Ultra Iraq)",
  "مليار دينار لكل منهما",
  [("المزارعون", "500 مليار"), ("المقاولون", "500 مليار"), ("المجموع", "1 تريليون")], 2, slug,
  ["مستحقات المزارعين 500 مليار", "المقاولين 500 مليار", "المجموع تريليون"], STOCK),
 beat("صندوق الأجيال", "صندوق الأجيال يصعد إلى 1.5 تريليون",
  "الحزمة تضيف 500 مليار دينار لمبادرة صندوق الأجيال فوق رصيده البالغ تريليون دينار، والزيدي وجّه بالإسراع في التنفيذ، وفق البيان.",
  "1.5", "Trillion IQD Generations Fund balance after the 500B top-up (was 1T) (PM office via Shafaq / 964)",
  "تريليون دينار رصيد صندوق الأجيال",
  [("الرصيد السابق", "1 تريليون"), ("الإضافة", "500 مليار"), ("التوجيه", "الإسراع بالتنفيذ")], 3, slug,
  ["صندوق الأجيال +500 مليار", "الرصيد 1.5 تريليون", "والتوجيه: تنفيذ سريع"], STOCK),
]
p["arabicTicker"] = [
 "مكتب رئيس الوزراء علي الزيدي: حزمة تمويلية بـ3.5 تريليون دينار (شبكة 964)",
 "تريليون دينار من مبادرات البنك المركزي للعقار والإسكان",
 "تريليون دينار إضافي على الأقل لمصرفي التجارة العراقي والصناعي",
 "500 مليار لمستحقات المقاولين و500 مليار لمستحقات المزارعين",
 "500 مليار إضافية لصندوق الأجيال ليرتفع رصيده إلى 1.5 تريليون",
 "تنتظر مستحقات من الدولة؟"]
p["endQuestion"] = "تنتظر مستحقات من الدولة؟"
p["sources"] = [{"name": "مكتب رئيس الوزراء", "domain": "pmo.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}, {"name": "ألترا عراق", "domain": "ultrairaq.ultrasawt.com"}]
SLATE[slug] = {"props": p, "caption": """حزمة الزيدي الاقتصادية — مستحقات المزارعين والمقاولين شنو صار بيها؟

3.5 تريليون دينار.. وين راح تتوزع؟ التفاصيل بالفيديو.

تنتظر مستحقات من الدولة؟

المصادر: مكتب رئيس الوزراء عبر شفق نيوز، شبكة 964، ألترا عراق (4 تشرين الأول 2026)

#العراق #الاقتصاد_العراقي #المزارعين #صندوق_الأجيال #photonectnews
@photonect.news""",
 "brief": {"kicker": "الحزمة الاقتصادية", "hookHeadline": "3.5 تريليون.. وين راح تروح؟",
  "voText": "أعلن مكتب رئيس الوزراء علي الزيدي الأحد حزمة تمويلية بقيمة ثلاثة تريليونات ونصف تريليون دينار. وبحسب البيان، توجَّه تريليون دينار من مبادرات البنك المركزي إلى العقار والإسكان، وتريليون آخر على الأقل إلى مصرفي التجارة والصناعي. كما تموّل وزارة المالية مستحقات المقاولين بخمسمئة مليار دينار، وتُسدَّد مستحقات المزارعين بخمسمئة مليار أخرى، ويضاف المبلغ نفسه إلى صندوق الأجيال ليرتفع رصيده إلى تريليون ونصف. ووجّه الزيدي بالإسراع في التنفيذ. تنتظر مستحقات من الدولة؟",
  "endQuestion": "تنتظر مستحقات من الدولة؟",
  "sourcesLine": "المصادر: مكتب رئيس الوزراء عبر شفق نيوز · شبكة 964 · ألترا عراق — 4 تشرين الأول 2026",
  "statPops": [{"value": "3.5", "label": "تريليون دينار — مجموع الحزمة", "matchWord": "تمويلية"},
               {"value": "500", "label": "مليار دينار لمستحقات المزارعين", "matchWord": "المزارعين"}]}}


# ═══════════ B · 19:45 · P1 dollar anchor — Monday 159,050, 964 lists 160,500 ═══════════
slug = f"{D}-b-dollar-159050-160k"
p = base(slug, "iraq_money", "B", "سعر الدولار", "الدولار يقترب من 160 ألفاً في بورصة بغداد",
  "159,050 IQD/$100 MON AM (SHAFAQ) | SUN CLOSE 158,050 | 964: BAGHDAD SELL 160,500, ERBIL 160,150, BASRA 159,500 | OFFICIAL 131,000")
p["beats"] = [
 beat("صباح الاثنين", "الكفاح: 159,050 صباح الاثنين",
  "بحسب شفق نيوز، سجلت بورصتا الكفاح والحارثية صباح الاثنين 159,050 ديناراً لكل 100 دولار، بعد إغلاق الأحد على 158,050.",
  "159,050", "IQD per $100, Kifah & Harithiya, Monday morning (Shafaq News)", "دينار لكل 100 دولار",
  [("إغلاق الأحد", "158,050"), ("الفرق", "+1,000 (محتسب)"), ("صباح الأحد", "157,950")], 1, slug,
  ["الكفاح والحارثية 159,050", "إغلاق الأحد 158,050", "أعلى بألف دينار (محتسب)"], STOCK),
 beat("البورصات", "964: بغداد تبيع بـ160,500",
  "قائمة شبكة 964 لبورصات العراق صباح الاثنين: سعر البيع 160,500 في بغداد، و160,150 في أربيل، و159,500 في البصرة، لكل 100 دولار.",
  "160,500", "IQD per $100, Baghdad selling price, Monday (964 bourse list)", "دينار بيع بغداد (964)",
  [("أربيل", "160,150"), ("البصرة", "159,500"), ("شراء بغداد", "159,500")], 2, slug,
  ["بغداد تبيع بـ160,500", "أربيل 160,150", "البصرة 159,500"], STOCK),
 beat("فوق الرسمي", "فوق الرسمي بـ28,050 لكل 100 دولار",
  "السعر الرسمي 131 ألف دينار لكل 100 دولار بحسب 964، أي أن سعر الكفاح الصباحي أعلى منه بـ28,050 ديناراً (محتسب).",
  "28,050", "IQD per $100 above the official 131,000 rate (Kifah 159,050 − 131,000, computed)", "دينار فوق الرسمي لكل 100 دولار",
  [("الرسمي", "131,000"), ("الكفاح", "159,050"), ("لكل 1,000 دولار", "280,500 (محتسب)")], 3, slug,
  ["الرسمي 131 ألف", "الكفاح 159,050", "الفرق 28,050 (محتسب)"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الكفاح والحارثية صباح الاثنين 159,050 ديناراً لكل 100 دولار",
 "إغلاق الأحد كان 158,050 (شفق نيوز) — أعلى بـ1,000 دينار (محتسب)",
 "شبكة 964: البيع في بغداد 160,500، أربيل 160,150، البصرة 159,500",
 "شبكة 964: السعر الرسمي 131 ألف دينار لكل 100 دولار",
 "اشتريت دولار هالأسبوع؟"]
p["endQuestion"] = "اشتريت دولار هالأسبوع؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — وصل 160 ألف؟

البورصة صعدت من إغلاق الأحد.. وشكد صار الفرق عن الرسمي؟ بالفيديو.

اشتريت دولار هالأسبوع؟

المصادر: شفق نيوز، شبكة 964 (4 و5 تشرين الأول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #بورصة_الكفاح #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "سعر الدولار", "hookHeadline": "الدولار على باب الـ160 ألف",
  "voText": "سجلت بورصتا الكفاح والحارثية في بغداد صباح الاثنين مئة وتسعة وخمسين ألفاً وخمسين ديناراً لكل مئة دولار، بحسب شفق نيوز، بعد إغلاق الأحد على مئة وثمانية وخمسين ألفاً وخمسين، أي بزيادة ألف دينار. وفي قائمة شبكة تسعة ستة أربعة، بلغ سعر البيع في بغداد مئة وستين ألفاً وخمسمئة دينار. أما السعر الرسمي للبنك المركزي فهو مئة وواحد وثلاثون ألفاً، أي أن سعر البورصة أعلى منه بأكثر من ثمانية وعشرين ألف دينار لكل مئة دولار. اشتريت دولار هالأسبوع؟",
  "endQuestion": "اشتريت دولار هالأسبوع؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 4 و5 تشرين الأول 2026",
  "statPops": [{"value": "159,050", "label": "دينار لكل 100 دولار — الكفاح صباح الاثنين", "matchWord": "والحارثية"},
               {"value": "28,050", "label": "دينار فوق السعر الرسمي لكل 100 دولار (محتسب)", "matchWord": "الرسمي"}]}}


# ═══════════ C · 21:15 · P2 Gulf trade (V10.1 CONTROL) — Iraqi Line back in the Gulf, Jebel Ali → Umm Qasr ═══════════
slug = f"{D}-c-iraqi-line-umm-qasr"
p = base(slug, "mena_geo", "A", "النقل البحري", "بعد أكثر من نصف قرن.. الخط البحري العراقي يعود إلى الخليج",
  ("BAGHDAD · OCT 5 | MINISTRY OF TRANSPORT (VIA SHAFAQ NEWS, 964): STATE SHIPPING LINE 'IRAQI LINE' TO RESUME COMMERCIAL GULF "
   "SERVICE — FIRST VOYAGE 15 OCTOBER, JEBEL ALI (UAE) -> UMM QASR | LAST IRAQI CARGO-SHIP VOYAGES IN THE REGION: MID-1960s"))
p["beats"] = [
 beat("الموعد", "أول رحلة في 15 تشرين الأول",
  "وزارة النقل أعلنت الاثنين استعداد الخط البحري العراقي لاستئناف نشاطه التجاري في الخليج، وأولى رحلاته في 15 تشرين الأول، بحسب شفق نيوز و964.",
  "15", "October 2026 — first voyage of the Iraqi Line (Ministry of Transport via Shafaq News / 964)", "تشرين الأول — أول رحلة",
  [("الانطلاق", "جبل علي"), ("الوصول", "أم قصر"), ("الحمولة", "حاويات وبضائع")], 1, slug,
  ["الخط البحري العراقي يعود", "أول رحلة 15 تشرين الأول", "من جبل علي إلى أم قصر"], STOCK),
 beat("التوقف", "آخر رحلة.. منتصف الستينيات",
  "بحسب الوزارة، آخر رحلات نفذتها سفن الشحن العراقية في المنطقة تعود إلى منتصف ستينيات القرن الماضي، أي توقف لأكثر من نصف قرن.",
  "50", "Years and more since Iraqi cargo ships last sailed regional routes, mid-1960s (Ministry of Transport via Shafaq / 964)", "عاماً وأكثر من التوقف",
  [("آخر الرحلات", "منتصف الستينيات"), ("الناقل", "Iraqi Line"), ("الوزير", "وهب الحسني")], 2, slug,
  ["آخر رحلة منتصف الستينيات", "توقف أكثر من 50 عاماً", "والعودة بقرار وزارة النقل"], STOCK),
 beat("الهدف", "ميناءان على الخط الأول",
  "تقول الوزارة إن الهدف تعزيز نقل البضائع عبر الموانئ العراقية، ودعم التجارة مع دول المنطقة، وفتح خيار وطني لنقل الحاويات والبضائع.",
  "2", "Ports on the first route: Jebel Ali (UAE) and Umm Qasr (Iraq) (Ministry of Transport via Shafaq / 964)", "ميناءان: جبل علي وأم قصر",
  [("الإمارات", "جبل علي"), ("العراق", "أم قصر"), ("الهدف", "تجارة إقليمية")], 3, slug,
  ["جبل علي ← أم قصر", "دعم التجارة مع المنطقة", "خيار وطني للحاويات"], STOCK),
]
p["arabicTicker"] = [
 "وزارة النقل: الخط البحري العراقي (Iraqi Line) يستعد لاستئناف نشاطه في الخليج",
 "أولى الرحلات في 15 تشرين الأول من ميناء جبل علي في الإمارات إلى أم قصر",
 "الوزارة: آخر رحلات سفن الشحن العراقية في المنطقة تعود إلى منتصف الستينيات",
 "الهدف بحسب الوزارة: تعزيز نقل البضائع عبر الموانئ العراقية ودعم التجارة الإقليمية",
 "تستورد بضاعة من دبي؟"]
p["endQuestion"] = "تستورد بضاعة من دبي؟"
p["sources"] = [{"name": "وزارة النقل", "domain": "motc.gov.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """الخط البحري العراقي يرجع للخليج — من جبل علي لأم قصر

آخر رحلة كانت قبل أكثر من نصف قرن.. وموعد العودة بالفيديو.

تستورد بضاعة من دبي؟

المصادر: وزارة النقل عبر شفق نيوز وشبكة 964 (5 تشرين الأول 2026)

#العراق #ميناء_أم_قصر #النقل_البحري #الإمارات #photonectnews
@photonect.news""", "brief": None}


# ═══════════ D · 22:30 · P1 corruption — Diwaniyah: 141 MasterCards with two education employees ═══════════
slug = f"{D}-d-diwaniya-141-cards"
p = base(slug, "iraq_accountability", "B", "النزاهة", "النزاهة: 141 بطاقة ماستر كارد بحوزة موظفَين في تربية الديوانية",
  ("DIWANIYAH · OCT 5 | FEDERAL INTEGRITY COMMISSION (VIA 964, ULTRA IRAQ): TWO EDUCATION-DIRECTORATE EMPLOYEES ACCUSED OF "
   "MANIPULATING ADMIN ORDERS OF THE LATEST APPOINTMENTS ANNEX FOR MONEY; 141 MASTERCARD CARDS FOUND WITH THEM | SEPARATELY A "
   "GOVERNORATE-OFFICE EMPLOYEE CAUGHT RECEIVING A BRIBE OVER A LAND-PLOT ALLOCATION | ALL DETAINED UNDER PENAL CODE ART. 308 "
   "AND RCC DECISION 160/1983 — NOT CONVICTED"))
p["beats"] = [
 beat("الضبط", "ضبط موظفَين في تربية الديوانية",
  "هيئة النزاهة الاتحادية أعلنت الاثنين ضبط موظفَين في مديرية تربية الديوانية، بتهمة التلاعب بأوامر ملحق التعيينات الأخير مقابل مبالغ مالية.",
  "2", "Education-directorate employees detained (Federal Integrity Commission statement via 964 / Ultra Iraq)", "موظفان متهمان",
  [("الملف", "ملحق التعيينات"), ("المحافظة", "الديوانية"), ("المجموع", "3 موظفين")], 1, slug,
  ["النزاهة تضبط موظفَين", "بتربية الديوانية", "تهمة: أوامر التعيينات"], STOCK),
 beat("البطاقات", "141 بطاقة ماستر كارد بحوزتهما",
  "بحسب بيان الهيئة، ضُبطت بحوزة الموظفَين 141 بطاقة ماستر كارد، تقول الهيئة إنها صدرت بالاشتراك مع بعض الموظفين.",
  "141", "MasterCard cards found with the two accused employees (Federal Integrity Commission via 964 / Ultra Iraq)", "بطاقة ماستر كارد",
  [("النوع", "ماستر كارد"), ("المصدر", "بيان النزاهة"), ("الإدانة", "لم تصدر")], 2, slug,
  ["141 بطاقة ماستر كارد", "بحوزة الموظفَين", "بحسب بيان الهيئة"], STOCK),
 beat("ديوان المحافظة", "وموظف ثالث بتهمة رشوة",
  "وبعملية منفصلة، تقول الهيئة إنها ضبطت موظفاً بديوان المحافظة يتسلّم رشوة لقاء التوسط بتخصيص قطعة أرض. والقاضي أوقف الثلاثة وفق المادة 308.",
  "308", "Iraqi Penal Code article (with RCC decision 160/1983) under which the investigating judge ordered detention", "مادة التوقيف بقانون العقوبات",
  [("القرار", "160 لسنة 1983"), ("الإجراء", "توقيف للتحقيق"), ("الحكم", "لم يصدر")], 3, slug,
  ["موظف ثالث بديوان المحافظة", "توقيف وفق المادة 308", "ولا إدانة بعد"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة الاتحادية: ضبط موظفَين في مديرية تربية الديوانية",
 "الهيئة: تهمة التلاعب بالأوامر الإدارية لملحق التعيينات الأخير مقابل مبالغ مالية",
 "الهيئة: ضبط 141 بطاقة ماستر كارد بحوزتهما صدرت بالاشتراك مع بعض الموظفين",
 "وبعملية منفصلة: ضبط موظف في ديوان المحافظة بتهمة تسلّم رشوة لتخصيص قطعة أرض",
 "قاضي التحقيق قرر التوقيف وفق المادة 308 — ولم تصدر إدانة",
 "قدّمت على تعيين بالتربية؟"]
p["endQuestion"] = "قدّمت على تعيين بالتربية؟"
p["sources"] = [{"name": "هيئة النزاهة الاتحادية", "domain": "nazaha.iq"}, {"name": "شبكة 964", "domain": "964media.com"}, {"name": "ألترا عراق", "domain": "ultrairaq.ultrasawt.com"}]
SLATE[slug] = {"props": p, "caption": """ملحق التعيينات بتربية الديوانية — شنو قالت هيئة النزاهة؟

141 بطاقة ماستر كارد.. وتفاصيل التهمة بالفيديو.

قدّمت على تعيين بالتربية؟

المصادر: هيئة النزاهة الاتحادية عبر شبكة 964 وألترا عراق (5 تشرين الأول 2026)

#هيئة_النزاهة #الديوانية #التعيينات #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "141 ماستر كارد بحوزة موظفَين",
  "voText": "أعلنت هيئة النزاهة الاتحادية الاثنين ضبط موظفَين في مديرية تربية الديوانية، بتهمة التلاعب بالأوامر الإدارية لملحق التعيينات الأخير مقابل مبالغ مالية. وتقول الهيئة إنها ضبطت بحوزتهما مئة وواحداً وأربعين بطاقة ماستر كارد، صدرت بالاشتراك مع بعض الموظفين. وفي عملية منفصلة، أعلنت الهيئة ضبط موظف في ديوان المحافظة بتهمة تسلّم رشوة لقاء التوسط في تخصيص قطعة أرض. وقرر قاضي التحقيق توقيف المتهمين الثلاثة وفق المادة ثلاثمئة وثمانية من قانون العقوبات، ولم تصدر إدانة بعد. قدّمت على تعيين بالتربية؟",
  "endQuestion": "قدّمت على تعيين بالتربية؟",
  "sourcesLine": "المصادر: هيئة النزاهة الاتحادية عبر شبكة 964 · ألترا عراق — 5 تشرين الأول 2026",
  "statPops": [{"value": "141", "label": "بطاقة ماستر كارد بحوزة المتهمَين", "matchWord": "ماستر"},
               {"value": "308", "label": "مادة التوقيف — قانون العقوبات", "matchWord": "ثلاثمئة"}]}}


# ═══════════ E · 23:45 · P3 pride/agri — red palm weevil in 7+ governorates ═══════════
slug = f"{D}-e-palm-weevil-7-provinces"
p = base(slug, "region_culture", "C", "النخيل", "سوسة النخيل الحمراء بأكثر من 7 محافظات عراقية",
  ("NAJAF · OCT 4-5 | AMIR SAHIB AL-HADDAD, HEAD OF PLANT PROTECTION, NAJAF AGRICULTURE DIRECTORATE (VIA SHAFAQ NEWS, VIDEO NEWS AGENCY): "
   "RED PALM WEEVIL RECORDED IN MORE THAN 7 GOVERNORATES | ONE NAJAF FOCUS: 28 PALMS INFECTED, 25 TREATED, 3 ADVANCED CASES FELL | "
   "INFECTED OFFSHOOTS THE MAIN SPREAD ROUTE — 3-DAY DIP/SPRAY + HEALTH CERTIFICATE BEFORE TRANSFER"))
p["beats"] = [
 beat("الانتشار", "أكثر من 7 محافظات مصابة",
  "رئيس قسم الوقاية بزراعة النجف أمير صاحب الحداد قال لشفق نيوز إن سوسة النخيل الحمراء سُجلت بأكثر من سبع محافظات وبنسب متفاوتة.",
  "7", "Governorates and more where red palm weevil infestation has been recorded (Najaf plant-protection head via Shafaq / Video News Agency)", "محافظات وأكثر",
  [("النجف", "منذ تموز 2025"), ("الأصل", "هندي (الحداد)"), ("نخيل النجف", "31 ألف دونم")], 1, slug,
  ["سوسة النخيل الحمراء", "بأكثر من 7 محافظات", "بنسب متفاوتة"], STOCK),
 beat("بؤرة واحدة", "بؤرة واحدة: 28 نخلة مصابة",
  "بحسب الحداد، أصيبت 28 نخلة في بؤرة البو منيثم بالنجف، عولجت 25 منها، وسقطت 3 حالات متقدمة كانت فارغة من الداخل.",
  "28", "Palms infected in one Najaf focus (Al-Bu Munaythim): 25 treated, 3 advanced cases fell (al-Haddad via Shafaq)", "نخلة مصابة ببؤرة واحدة",
  [("عولجت", "25"), ("سقطت", "3"), ("المعالجة بالنجف", "مجانية")], 2, slug,
  ["28 نخلة ببؤرة واحدة", "25 عولجت", "3 سقطت"], STOCK),
 beat("الفسيلة", "الفسيلة المصابة أخطر ناقل",
  "الحداد: الفسائل المصابة العامل الأساسي بنقل الآفة، لذلك تُغطَّس أو تُرش 3 أيام وتأخذ شهادة صحية قبل نقلها بين المحافظات.",
  "3", "Days of dipping or spraying an offshoot before a transfer permit is issued (al-Haddad via Shafaq)", "أيام تعقيم قبل نقل الفسيلة",
  [("الطيران", "500 م - 1 كم"), ("الأجيال", "5 - 6"), ("النقل", "بشهادة صحية")], 3, slug,
  ["الفسائل أخطر ناقل", "تعقيم 3 أيام", "وشهادة صحية للنقل"], STOCK),
]
p["arabicTicker"] = [
 "زراعة النجف: سوسة النخيل الحمراء مسجلة في أكثر من سبع محافظات (شفق نيوز)",
 "الحداد: الحشرة تتغذى داخل جذع النخلة وقد تبدو الشجرة سليمة في البداية",
 "بؤرة البو منيثم بالنجف: 28 نخلة مصابة، عولجت 25 وسقطت 3",
 "الفسائل المصابة العامل الأساسي في النقل — تعقيم 3 أيام وشهادة صحية",
 "عدكم نخل بالبيت؟"]
p["endQuestion"] = "عدكم نخل بالبيت؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "وكالة فيديو الإخبارية", "domain": "video-agencyia.iq"}]
SLATE[slug] = {"props": p, "caption": """سوسة النخيل الحمراء في العراق — نخلتك بأمان؟

وصلت أكثر من سبع محافظات.. وشلون تنتقل بالفيديو.

عدكم نخل بالبيت؟

المصادر: مديرية زراعة النجف عبر شفق نيوز ووكالة فيديو الإخبارية (4 و5 تشرين الأول 2026)

#النخيل #سوسة_النخيل_الحمراء #التمور #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "النخيل", "hookHeadline": "السوسة الحمراء بأكثر من 7 محافظات",
  "voText": "قال رئيس قسم الوقاية في زراعة النجف أمير صاحب الحداد، لشفق نيوز، إن سوسة النخيل الحمراء سُجلت في أكثر من سبع محافظات عراقية وبنسب متفاوتة. وأوضح أن الحشرة تتغذى داخل جذع النخلة، وقد تبدو الشجرة سليمة في البداية. وفي بؤرة واحدة بالنجف أصيبت ثماني وعشرون نخلة، عولجت خمس وعشرون منها وسقطت ثلاث. ويقول الحداد إن الفسائل المصابة هي العامل الأساسي في نقل الآفة، لذلك تُعقَّم قبل نقلها وتُمنح شهادة صحية. عدكم نخل بالبيت؟",
  "endQuestion": "عدكم نخل بالبيت؟",
  "sourcesLine": "المصادر: مديرية زراعة النجف عبر شفق نيوز · وكالة فيديو الإخبارية — 4 و5 تشرين الأول 2026",
  "statPops": [{"value": "+7", "label": "محافظات سُجلت فيها الإصابة", "matchWord": "سبع"},
               {"value": "28", "label": "نخلة مصابة ببؤرة واحدة بالنجف", "matchWord": "بؤرة"}]}}



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
