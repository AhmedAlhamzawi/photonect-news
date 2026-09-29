#!/usr/bin/env python3
"""Author the 2026-09-29 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source published 27-29 Sep 2026. Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + two gate passes (apply_gate*_2026_09_29.py)
then edited the files on disk — do NOT re-run this script, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_09_29.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-29"
DATE_LABEL = "SEP 29 • 2026"
AR_DATE = "29 أيلول 2026"
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


# ═══════════ A · 18:00 · P1 corruption — MP Farman verdict (LEAD) ═══════════
slug = f"{D}-a-mp-farman-28-billion"
p = base(slug, "iraq_corruption", "A", "النزاهة", "نائب حالي.. 7 سنوات سجن و28 مليار دينار",
  ("BAGHDAD · SEP 29 | FEDERAL INTEGRITY COMMISSION: THE CENTRAL ANTI-CORRUPTION FELONY COURT ISSUED A VERDICT IN "
   "PRESENTIA SENTENCING SITTING MP MOHAMMED FARMAN SHAHER SALMAN AL-JUBOURI TO 7 YEARS FOR ILLICIT ENRICHMENT (ART. 19/2, "
   "LAW 30 OF 2011) | ORDERED TO RETURN IQD 11,795,949,238 AND $1,729,300 PLUS AN EQUAL FINE — TOTAL IQD 28,157,250,476 | "
   "SEPARATE 3-YEAR SENTENCE FOR CONCEALMENT, HARSHER PENALTY APPLIES | ASSET FREEZE UPHELD; COMPENSATION CLAIM AFTER THE "
   "VERDICT BECOMES FINAL (INTEGRITY COMMISSION VIA SHAFAQ NEWS, 964)"))
p["beats"] = [
 beat("الحكم", "7 سنوات سجن لنائب حالي",
  "محكمة جنايات مكافحة الفساد أصدرت حكماً حضورياً بسجن النائب محمد فرمان شاهر الجبوري 7 سنوات بجريمة الكسب غير المشروع (هيئة النزاهة).",
  "7", "Years in prison for sitting MP Mohammed Farman al-Jubouri, illicit enrichment (Integrity Commission)",
  "سنوات سجن بحكم حضوري — الكسب غير المشروع (النزاهة)",
  [("الحكم", "حضوري"), ("المادة", "19/ثانياً"), ("القانون", "30 لسنة 2011")], 1, slug,
  ["نائب حالي", "7 سنوات سجن", "الكسب غير المشروع"], STOCK),
 beat("المبالغ", "ردّ وغرامة: أكثر من 28 مليار",
  "إلزامه بردّ 11,795,949,238 ديناراً و1,729,300 دولار، مع غرامة تعادل قيمة الكسب، والمجموع 28,157,250,476 ديناراً (النزاهة عبر شفق نيوز و964).",
  "+28 مليار", "IQD total to be returned plus equal fine: 28,157,250,476 (Integrity Commission)",
  "دينار مجموع الردّ والغرامة (النزاهة)",
  [("بالدينار", "11,795,949,238"), ("بالدولار", "1,729,300$"), ("الغرامة", "تعادل الكسب")], 2, slug,
  ["ردّ الأموال", "وغرامة تعادلها", "أكثر من 28 مليار"], STOCK),
 beat("الأموال", "حجز الأموال.. وحكم ثانٍ بالحبس",
  "حكم آخر بحبسه 3 سنوات عن جريمة الإخفاء مع تطبيق العقوبة الأشد، وتأييد الحجز على أمواله، والتعويض بعد اكتساب الحكم الدرجة القطعية.",
  "3", "Years of hard imprisonment in a second verdict for concealment; harsher penalty applies (Integrity Commission)",
  "سنوات حبس شديد عن جريمة الإخفاء — تُطبَّق الأشد (النزاهة)",
  [("أمواله", "الحجز مؤيَّد"), ("التعويض", "بعد القطعية"), ("قبله", "نائبتان في 23 أيلول")], 3, slug,
  ["حكم ثانٍ بالحبس", "الحجز على أمواله", "التعويض بعد القطعية"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة: حكم حضوري بسجن النائب محمد فرمان شاهر سلمان الجبوري 7 سنوات عن جريمة الكسب غير المشروع (29 أيلول)",
 "المحكمة ألزمته بردّ 11,795,949,238 ديناراً و1,729,300 دولار مع غرامة تعادلها — المجموع 28,157,250,476 ديناراً",
 "حكم ثانٍ بالحبس الشديد 3 سنوات عن جريمة الإخفاء مع تطبيق العقوبة الأشد، وتأييد الحجز على أمواله المنقولة وغير المنقولة",
 "شفق نيوز: الحكم يأتي بعد حكمين بسجن النائبتين عالية نصيف وأشواق سالم حسن 7 سنوات في 23 أيلول",
 "تعرف اسم نائب منطقتك؟"]
p["endQuestion"] = "تعرف اسم نائب منطقتك؟"
p["sources"] = [{"name": "هيئة النزاهة", "domain": "nazaha.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """حكم سجن نائب في العراق بالكسب غير المشروع — شكد المبلغ؟

ثالث نائب يُحكم خلال أسبوع.. والتفاصيل بالفيديو.

تعرف اسم نائب منطقتك؟

المصادر: هيئة النزاهة عبر شفق نيوز وشبكة 964 (29 أيلول 2026)

#العراق #هيئة_النزاهة #الفساد #مجلس_النواب #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "نائب حالي.. سبع سنوات سجن",
  "voText": "أعلنت هيئة النزاهة، يوم الثلاثاء، صدور حكم حضوري بسجن النائب محمد فرمان شاهر الجبوري سبع سنوات، بجريمة الكسب غير المشروع. وألزمته محكمة جنايات مكافحة الفساد بردّ نحو أحد عشر مليار وثمانمئة مليون دينار، ومليون وسبعمئة وتسعة وعشرين ألف دولار، مع غرامة تعادلها، ليتجاوز المجموع ثمانية وعشرين مليار دينار. كما أيّدت المحكمة الحجز على أمواله. وبحسب شفق نيوز، سبق ذلك حكمان بسجن نائبتين في الثالث والعشرين من أيلول. تعرف اسم نائب منطقتك؟",
  "endQuestion": "تعرف اسم نائب منطقتك؟",
  "sourcesLine": "المصادر: هيئة النزاهة عبر شفق نيوز · شبكة 964 — 29 أيلول 2026",
  "statPops": [{"value": "7", "label": "سنوات سجن — حكم حضوري", "matchWord": "سنوات"},
               {"value": "+28 مليار", "label": "دينار ردّ وغرامة (النزاهة)", "matchWord": "المجموع"}]}}

# ═══════════ B · 19:45 · P1 dollar anchor (+ gold) ═══════════
slug = f"{D}-b-dollar-157000-gold-up"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار 157 ألف.. والذهب يصعد وياه",
  ("BAGHDAD · SEP 29 | SHAFAQ NEWS: KIFAH & HARITHIYA BOURSES 157,000 IQD PER $100 TUESDAY MORNING, UP FROM 156,000 "
   "MONDAY MORNING (+1,000, COMPUTED) | BAGHDAD EXCHANGE SHOPS: SELL 157,500 / BUY 156,500; ERBIL SELL 157,400 / BUY 157,350 "
   "| GOLD, SHORJA AL-NAHR WHOLESALE: 21K GULF/TURKISH/EUROPEAN MITHQAL SELLS AT 915,000 IQD, UP FROM 910,000 MONDAY "
   "(SHAFAQ NEWS) | OFFICIAL CBI RATE 131,000 PER $100 (964) — BOURSE PREMIUM 26,000 (COMPUTED)"))
p["beats"] = [
 beat("البورصة", "157,000 صباح الثلاثاء",
  "شفق نيوز: بورصتا الكفاح والحارثية سجّلتا صباح الثلاثاء 157,000 دينار لكل 100 دولار، بعد 156,000 صباح الاثنين.",
  "157,000", "IQD per $100, Kifah & Harithiya bourses, Tuesday morning (Shafaq News)",
  "دينار لكل 100 دولار — الكفاح والحارثية صباح الثلاثاء (شفق نيوز)",
  [("الاثنين صباحاً", "156,000"), ("الفرق", "1,000+ (محتسب)"), ("الرسمي", "131,000")], 1, slug,
  ["الدولار يواصل الصعود", "157,000 دينار", "الاثنين كان 156,000"], STOCK),
 beat("الصيرفة", "محلات بغداد تبيع بـ157,500",
  "محال الصيرفة ببغداد: البيع 157,500 والشراء 156,500. وبأربيل: البيع 157,400 والشراء 157,350 (شفق نيوز).",
  "157,500", "IQD per $100, Baghdad exchange-shop selling price, Tuesday morning (Shafaq News)",
  "دينار سعر البيع لكل 100 دولار بمحلات بغداد (شفق نيوز)",
  [("بغداد شراء", "156,500"), ("أربيل بيع", "157,400"), ("أربيل شراء", "157,350")], 2, slug,
  ["البيع 157,500", "الشراء 156,500", "وأربيل 157,400"], STOCK),
 beat("الذهب", "المثقال 915 ألف بشارع النهر",
  "شفق نيوز: مثقال الذهب عيار 21 الخليجي والتركي والأوروبي بجملة شارع النهر بـ915,000 دينار بيعاً، بعد 910,000 الاثنين.",
  "915,000", "IQD per mithqal, 21K Gulf/Turkish/European gold, Al-Nahr St wholesale sell price (Shafaq News)",
  "دينار مثقال عيار 21 — جملة شارع النهر (شفق نيوز)",
  [("الاثنين", "910,000"), ("الشراء", "911,000"), ("العراقي عيار 21", "885,000")], 3, slug,
  ["الذهب يصعد وياه", "المثقال 915 ألف", "الاثنين 910 آلاف"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الدولار في بورصتي الكفاح والحارثية 157,000 دينار لكل 100 دولار صباح الثلاثاء، بعد 156,000 صباح الاثنين",
 "محال الصيرفة ببغداد: البيع 157,500 والشراء 156,500 — أربيل: البيع 157,400 والشراء 157,350",
 "الذهب في جملة شارع النهر: مثقال عيار 21 الخليجي والتركي والأوروبي 915,000 دينار بيعاً بعد 910,000 الاثنين",
 "السعر الرسمي المقرر من البنك المركزي: 131,000 دينار لكل 100 دولار (شبكة 964)",
 "اشتريت دولار هالأسبوع؟"]
p["endQuestion"] = "اشتريت دولار هالأسبوع؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — والذهب شصار بيه؟

البورصة والصيرفة ومثقال شارع النهر.. الأرقام بالفيديو.

اشتريت دولار هالأسبوع؟

المصادر: شفق نيوز، شبكة 964 (29 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #سعر_الذهب #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "الدولار يصعد.. والذهب وياه",
  "voText": "واصل الدولار ارتفاعه في بغداد صباح الثلاثاء. وبحسب شفق نيوز، سجّلت بورصتا الكفاح والحارثية مئة وسبعة وخمسين ألف دينار لكل مئة دولار، بعد مئة وستة وخمسين ألفاً صباح الاثنين. وبلغ سعر البيع في محال الصيرفة ببغداد مئة وسبعة وخمسين ألفاً وخمسمئة دينار. ومع الصرف ارتفع الذهب أيضاً، إذ سجّل مثقال عيار واحد وعشرين الخليجي في جملة شارع النهر تسعمئة وخمسة عشر ألف دينار، بعد تسعمئة وعشرة آلاف يوم الاثنين. اشتريت دولار هالأسبوع؟",
  "endQuestion": "اشتريت دولار هالأسبوع؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 29 أيلول 2026",
  "statPops": [{"value": "157,000", "label": "بورصة الكفاح — صباح الثلاثاء", "matchWord": "والحارثية"},
               {"value": "915,000", "label": "دينار مثقال عيار 21 — شارع النهر", "matchWord": "النهر"}]}}

# ═══════════ C · 21:15 · P2 Zaidi–Trump → oil firms (V10.1 CONTROL) ═══════════
slug = f"{D}-c-zaidi-trump-oil-firms"
p = base(slug, "mena_geo", "A", "العراق وأمريكا", "الزيدي وترامب منفردين.. شنو انطرح عن النفط؟",
  ("BAGHDAD / NEW YORK · SEP 28 | GOVT SPOKESMAN HAIDAR AL-ABOUDI (DIJLA TV VIA 964): PM ALI AL-ZAIDI MET PRESIDENT TRUMP "
   "ONE-ON-ONE AFTER A GROUP RECEPTION FOR LEADERS AT THE UN | TOPICS: STABILITY, INVESTMENT, US COMPANIES IN OIL AND ENERGY, "
   "ANTI-CORRUPTION, STATE MONOPOLY ON WEAPONS | GOVT TARGETS 10M BPD OUTPUT BY 2030; DECISION TAKEN ON THE BANIYAS PIPELINE, "
   "CONTRACTS WITH AN INTERNATIONAL CONSORTIUM 'TAKING SHAPE' | SHAFAQ NEWS SOURCE: ZAIDI BRIEFED COORDINATION FRAMEWORK "
   "LEADERS; IRANIAN FLIGHT BAN ON THE AGENDA | ARCHIVE PHOTO: OVAL OFFICE, 14 JULY 2026 (WHITE HOUSE)"))
p["beats"] = [
 beat("اللقاء", "لقاء منفرد بنيويورك.. شنو انطرح؟",
  "العبودي: الزيدي التقى ترامب منفرداً بعد استقبال جماعي للقادة بالأمم المتحدة، وناقشا الاستثمار والشركات الأميركية بالنفط والفساد والسلاح (دجلة عبر 964).",
  "4", "Files the PM raised, per the government spokesman: corruption, weapons, rule of law, economy (964; count computed)",
  "ملفات عرضها الزيدي حسب العبودي: الفساد، السلاح، القانون، الاقتصاد (محتسب)",
  [("المكان", "نيويورك"), ("الصيغة", "لقاء منفرد"), ("المصدر", "الناطق الحكومي")], 1, slug,
  ["لقاء منفرد", "الشركات الأميركية", "بالنفط والطاقة"], "صورة أرشيفية — مقر الأمم المتحدة"),
 beat("الهدف", "10 ملايين برميل يومياً بـ2030",
  "العبودي: الحكومة تستهدف إنتاج 10 ملايين برميل يومياً بحلول 2030، وقرار أنبوب بانياس اتُّخذ، والعقود مع ائتلاف شركات دولية «في طور التبلور».",
  "10M", "Barrels per day — government output target for 2030 (spokesman al-Aboudi via 964)",
  "برميل يومياً — هدف الحكومة لعام 2030 (العبودي)",
  [("الموعد", "2030"), ("بانياس", "العقود قيد التبلور"), ("التنفيذ", "ائتلاف دولي")], 2, slug,
  ["10 ملايين برميل", "بحلول 2030", "وأنبوب بانياس"], STOCK),
 beat("الإطار", "الزيدي يطلع الإطار على التفاهمات",
  "مصدر لشفق نيوز: الزيدي أطلع قادة الإطار على تفاهماته مع ترامب، وحظر الطيران الإيراني كان على الطاولة، بغياب المالكي والعامري.",
  "36", "Iranian aviation-linked entities sanctioned by the US Treasury on 8 September (Shafaq News)",
  "جهة إيرانية بقطاع الطيران عاقبتها الخزانة الأميركية في 8 أيلول (شفق نيوز)",
  [("الاجتماع", "تشاوري"), ("الملف", "الطيران الإيراني"), ("الغائبان", "المالكي والعامري")], 3, slug,
  ["الإطار يسمع التفاصيل", "الطيران الإيراني", "على الطاولة"], STOCK),
]
p["arabicTicker"] = [
 "الناطق الحكومي حيدر العبودي: لقاء الزيدي وترامب في نيويورك جرى بشكل منفرد بعد استقبال جماعي للقادة (دجلة عبر شبكة 964)",
 "العبودي: اللقاء تناول الاستثمار وحضور الشركات الأميركية في قطاعي النفط والطاقة",
 "العبودي: الحكومة تستهدف إنتاج 10 ملايين برميل يومياً بحلول 2030، وقرار أنبوب بانياس اتُّخذ",
 "مصدر لشفق نيوز: الزيدي أطلع قادة الإطار التنسيقي على تفاهماته مع ترامب بغياب المالكي والعامري",
 "تشتغل بشركة نفطية؟"]
p["endQuestion"] = "تشتغل بشركة نفطية؟"
p["sources"] = [{"name": "شبكة 964", "domain": "964media.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """لقاء الزيدي وترامب في نيويورك — شنو يعني لنفط العراق؟

الشركات الأميركية وهدف 2030 وأنبوب بانياس.. بالفيديو.

تشتغل بشركة نفطية؟

المصادر: شبكة 964، شفق نيوز (28-29 أيلول 2026)

#العراق #نفط_العراق #الزيدي #ترامب #photonectnews
@photonect.news""", "brief": None}

# ═══════════ D · 22:30 · P1 customs pre-payment rule ═══════════
slug = f"{D}-d-customs-transfers-1-october"
p = base(slug, "iraq_money", "B", "الكمارك", "من الخميس: ما يطلع دولار قبل الرسوم",
  ("BAGHDAD · SEP 28 | CUSTOMS AUTHORITY DIRECTOR THAMER QASSEM DAWOOD (DIJLA TV VIA 964): FROM 1 OCTOBER NO IMPORT-RELATED "
   "DOLLAR TRANSFER ABROAD WITHOUT PRIOR PAYMENT OF CUSTOMS DUTIES AND TAX DEPOSITS, UNDER CABINET DECISION 413 OF 2026 | "
   "NEW PRE-DECLARATION 07 VIA ASYCUDA FOR TRANSFERS; 06 FOR IMPORTS WITHOUT A BANK TRANSFER, DECLARING SOURCE OF FUNDS | "
   "BANKS VERIFY THE PRE-DECLARATION NUMBER BEFORE TRANSFERRING (CUSTOMS STATEMENT VIA AL-MUSTAQILA, SHAFAQNA) | "
   "RECORDED CUSTOMS REVENUE IQD 3.15 TRILLION, 'UNPRECEDENTED' (DAWOOD)"))
p["beats"] = [
 beat("القاعدة", "من الخميس: لا تحويل قبل الرسوم",
  "مدير الكمارك: من 1 تشرين الأول لن يُحوَّل دولار للخارج للاستيراد دون استيفاء الرسوم الكمركية والأمانات الضريبية، تطبيقاً لقرار مجلس الوزراء 413 (964).",
  "413", "Cabinet decision number (2026) behind customs pre-payment on import transfers (Customs Authority)",
  "رقم قرار مجلس الوزراء لسنة 2026 (هيئة الكمارك)",
  [("البدء", "1 تشرين الأول"), ("النظام", "الأسيكودا"), ("البيان", "07 للتحويلات")], 1, slug,
  ["من الخميس", "ما يطلع دولار", "قبل الرسوم"], STOCK),
 beat("المصارف", "المصرف يتحقق قبل ما يحوّل",
  "بيان الكمارك: المصارف تتحقق من البيان المسبق وتضيف رقمه للتحويل، والاستيراد دون تحويل مصرفي يُصرَّح فيه بمصدر الأموال (المستقلة، شفقنا).",
  "06", "Pre-declaration form for imports without a bank transfer — declares source of funds (Customs Authority)",
  "بيان مسبق للاستيراد دون تحويل مالي — مع مصدر الأموال (الكمارك)",
  [("المصرف", "يتحقق من البيان"), ("بدون تحويل", "تصريح بالمصدر"), ("الاسترداد", "بعد إعادة المبلغ")], 2, slug,
  ["المصرف يتحقق", "رقم البيان المسبق", "ومصدر الأموال"], STOCK),
 beat("الإيرادات", "إيرادات الكمارك 3 تريليون و150 مليار",
  "داود: الإيرادات المسجلة بلغت 3 تريليون و150 مليار دينار ويصفها بغير المسبوقة، وأكثر التبادل التجاري عبر سوريا من منفذي ربيعة والوليد.",
  "3,150 مليار", "IQD recorded customs revenue, described as unprecedented (Customs director via 964)",
  "دينار إيرادات الكمارك المسجلة (مدير الكمارك عبر 964)",
  [("الأول بالتبادل", "سوريا"), ("المنافذ", "ربيعة والوليد"), ("إيران", "الرابعة")], 3, slug,
  ["الإيرادات 3 تريليون", "و150 مليار", "وسوريا بالصدارة"], STOCK),
]
p["arabicTicker"] = [
 "مدير الكمارك ثامر قاسم داود: من 1 تشرين الأول لن يُحوَّل دولار للخارج دون استيفاء الرسوم الكمركية والأمانات الضريبية (964)",
 "الآلية تطبيق لقرار مجلس الوزراء 413 لسنة 2026 عبر بيان كمركي مسبق بنظام الأسيكودا",
 "بيان الكمارك: المصارف تتحقق من البيان المسبق وتضيف رقمه لبيانات التحويل (المستقلة، شفقنا)",
 "الاستيراد دون تحويل مصرفي: بيان مسبق مع حقل للتصريح عن مصدر الأموال",
 "تشتغل بالاستيراد أو التحويل؟"]
p["endQuestion"] = "تشتغل بالاستيراد أو التحويل؟"
p["sources"] = [{"name": "شبكة 964", "domain": "964media.com"}, {"name": "المستقلة", "domain": "mustaqila.com"}, {"name": "شفقنا العراق", "domain": "iraq.shafaqna.com"}]
SLATE[slug] = {"props": p, "caption": """تحويل الدولار للخارج في العراق — شنو يتغيّر بتشرين الأول؟

قاعدة جديدة للمستوردين والمصارف.. التفاصيل بالفيديو.

تشتغل بالاستيراد أو التحويل؟

المصادر: هيئة الكمارك عبر شبكة 964، المستقلة، شفقنا (27-28 أيلول 2026)

#العراق #الكمارك #الدولار #الاستيراد #photonectnews
@photonect.news""",
 "brief": {"kicker": "الكمارك", "hookHeadline": "من الخميس.. ما يطلع دولار قبل الرسوم",
  "voText": "اعتباراً من يوم الخميس، الأول من تشرين الأول، لن يُحوَّل أي دولار إلى الخارج لأغراض الاستيراد قبل دفع الرسوم الكمركية والأمانات الضريبية، بحسب مدير هيئة الكمارك ثامر قاسم داود لشبكة تسعة ستة أربعة. ويأتي ذلك تطبيقاً لقرار مجلس الوزراء، عبر بيان كمركي مسبق تتحقق المصارف من رقمه قبل التحويل. أما الاستيراد دون تحويل مصرفي، فيُطلب فيه التصريح بمصدر الأموال. ويقول داود إن إيرادات الكمارك المسجلة بلغت ثلاثة تريليونات ومئة وخمسين مليار دينار. تشتغل بالاستيراد أو التحويل؟",
  "endQuestion": "تشتغل بالاستيراد أو التحويل؟",
  "sourcesLine": "المصادر: هيئة الكمارك عبر شبكة 964 · المستقلة · شفقنا — 27-28 أيلول 2026",
  "statPops": [{"value": "1 تشرين الأول", "label": "بدء الاستيفاء المسبق للرسوم", "matchWord": "الخميس"},
               {"value": "3,150 مليار", "label": "دينار إيرادات الكمارك المسجلة (داود)", "matchWord": "تريليونات"}]}}

# ═══════════ E · 23:45 · P3 education — Baghdad–Kurdistan mutual admission ═══════════
slug = f"{D}-e-kurdistan-seats-1250"
p = base(slug, "iraq_society", "C", "التعليم العالي", "بغداد والإقليم: مقاعد الطلبة من 500 إلى 1250",
  ("BAGHDAD · SEP 29 | FEDERAL HIGHER EDUCATION MINISTRY: MUTUAL ADMISSION BETWEEN FEDERAL AND KURDISTAN REGION "
   "UNIVERSITIES RAISED TO 1,250 STUDENTS A YEAR FROM 500 | UNDERGRADUATE SEATS 400 → 1,000; POSTGRADUATE 100 → 250, FOR NEXT "
   "ACADEMIC YEAR | MEETING CHAIRED BY DEPUTY MINISTER HAIDAR ABD DHAHAD WITH KRG MINISTRY ADVISER SABAH IBRAHIM WAIS; "
   "ADMINISTRATIVE HURDLES AND DEGREE EQUIVALENCY DISCUSSED (MINISTRY STATEMENT VIA SHAFAQ NEWS, KALIMA)"))
p["beats"] = [
 beat("القرار", "من 500 إلى 1250 مقعداً",
  "وزارة التعليم العالي وسّعت القبول المتبادل بين الجامعات الاتحادية وجامعات إقليم كوردستان إلى 1250 طالباً سنوياً بعد 500 فقط (بيان الوزارة عبر شفق نيوز).",
  "1,250", "Students a year in federal–Kurdistan mutual university admission, up from 500 (Higher Education Ministry)",
  "طالباً سنوياً بالقبول المتبادل بدل 500 (وزارة التعليم العالي)",
  [("قبل", "500"), ("بعد", "1,250"), ("الزيادة", "750 (محتسب)")], 1, slug,
  ["القبول المتبادل", "من 500", "إلى 1250"], "صورة أرشيفية — جامعة السليمانية"),
 beat("الأولية", "الدراسات الأولية: 400 تصير 1000",
  "مقاعد الدراسات الأولية ترتفع من 400 إلى 1000 طالب للعام الدراسي المقبل، حسب بيان الوزارة.",
  "1,000", "Undergraduate mutual-admission seats for next academic year, up from 400 (Higher Education Ministry)",
  "مقعد للدراسات الأولية بدل 400 (وزارة التعليم العالي)",
  [("قبل", "400"), ("بعد", "1,000"), ("الموعد", "العام الدراسي المقبل")], 2, slug,
  ["الدراسات الأولية", "من 400", "إلى 1000"], "صورة أرشيفية — جامعة بغداد"),
 beat("العليا", "الدراسات العليا: 100 تصير 250",
  "مقاعد الدراسات العليا ترتفع من 100 إلى 250، والجانبان بحثا تذليل عقبات القبول ومعادلة الشهادات (الوزارة، شفق نيوز، كلمة).",
  "250", "Postgraduate mutual-admission seats, up from 100 (Higher Education Ministry)",
  "مقعداً للدراسات العليا بدل 100 (وزارة التعليم العالي)",
  [("قبل", "100"), ("بعد", "250"), ("الملف التالي", "معادلة الشهادات")], 3, slug,
  ["الدراسات العليا", "من 100 إلى 250", "ومعادلة الشهادات"], "صورة أرشيفية — طلبة في السليمانية"),
]
p["arabicTicker"] = [
 "وزارة التعليم العالي: توسيع القبول المتبادل مع جامعات إقليم كوردستان إلى 1250 طالباً سنوياً بعد 500 (29 أيلول)",
 "الدراسات الأولية: من 400 إلى 1000 مقعد — الدراسات العليا: من 100 إلى 250 مقعداً للعام الدراسي المقبل",
 "الاجتماع برئاسة وكيل الوزارة للشؤون العلمية حيدر عبد ضهد وبحضور مستشار وزارة التعليم العالي في الإقليم صباح إبراهيم ويس",
 "الجانبان بحثا تذليل العقبات الإدارية والفنية أمام القبول المتبادل ومعادلة الشهادات",
 "عندك أحد يدرس بجامعة بالإقليم؟"]
p["endQuestion"] = "عندك أحد يدرس بجامعة بالإقليم؟"
p["sources"] = [{"name": "وزارة التعليم العالي", "domain": "mohesr.gov.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "كلمة", "domain": "kalimaiq.com"}]
SLATE[slug] = {"props": p, "caption": """القبول المتبادل بين جامعات بغداد وإقليم كوردستان — كم مقعد صار؟

الدراسات الأولية والعليا.. الأرقام بالفيديو.

عندك أحد يدرس بجامعة بالإقليم؟

المصادر: وزارة التعليم العالي عبر شفق نيوز، كلمة (29 أيلول 2026)

#العراق #التعليم_العالي #اقليم_كوردستان #القبول_المركزي #photonectnews
@photonect.news""",
 "brief": {"kicker": "التعليم العالي", "hookHeadline": "مقاعد الطلبة بالإقليم صارت أكثر",
  "voText": "أعلنت وزارة التعليم العالي، يوم الثلاثاء، رفع مقاعد القبول المتبادل بين الجامعات الاتحادية وجامعات إقليم كوردستان إلى ألف ومئتين وخمسين طالباً سنوياً، بعدما كانت خمسمئة فقط. ففي الدراسات الأولية ترتفع المقاعد من أربعمئة إلى ألف طالب، وفي الدراسات العليا من مئة إلى مئتين وخمسين، للعام الدراسي المقبل. وبحث ممثلو الوزارتين في بغداد والإقليم أيضاً تذليل عقبات القبول ومعادلة الشهادات، بحسب بيان الوزارة الذي نقلته شفق نيوز. عندك أحد يدرس بجامعة بالإقليم؟",
  "endQuestion": "عندك أحد يدرس بجامعة بالإقليم؟",
  "sourcesLine": "المصادر: وزارة التعليم العالي عبر شفق نيوز · كلمة — 29 أيلول 2026",
  "statPops": [{"value": "1,250", "label": "طالباً سنوياً بدل 500", "matchWord": "سنوياً"},
               {"value": "1,000", "label": "مقعد دراسات أولية بدل 400", "matchWord": "الأولية"}]}}

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
