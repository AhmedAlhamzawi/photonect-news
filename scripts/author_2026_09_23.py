#!/usr/bin/env python3
"""Author the 2026-09-23 slate: props.json + caption.txt (+ v11-brief.json on a-d).

Every figure below is traced to a named source published 23 Sep 2026 unless the
text itself dates it otherwise. Computed figures carry (محتسب).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-23"
DATE_LABEL = "SEP 23 • 2026"
AR_DATE = "23 أيلول 2026"
IMG = "images/news"

def beat(label, heading, body, val, en_label, ar_label, stats, idx, slug, phrases, accent="#FFC217"):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": val, "label": en_label, "arabicLabel": ar_label},
        "supportingStats": [{"label": k, "value": v} for k, v in stats],
        "broll": f"{IMG}/{slug}/broll_{idx}.jpg",
        "brolls": [f"{IMG}/{slug}/broll_{idx}.jpg"],
        "brollType": "image",
        "accent": accent,
        "brollSource": "صورة توضيحية · KIE",
        "subtitlePhrases": phrases,
    }

SLATE = {}

# ════════════════════════ A · 18:00 · P1 corruption (LEAD) ════════════════════
slug = f"{D}-a-two-mps-seven-years"
SLATE[slug] = {
 "props": {
  "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
  "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_money", "variant": "A",
  "breaking": {
   "arabicKicker": "عاجل",
   "arabicHeadline": "بيوم واحد.. السجن 7 سنوات لنائبتين بالكسب غير المشروع",
   "englishSubhead": ("BAGHDAD · SEP 23 | CENTRAL FELONY COURT FOR CORRUPTION CASES SENTENCED TWO SITTING MPs "
     "ON WEDNESDAY 23 SEP, EACH TO 7 YEARS FOR ILLICIT ENRICHMENT PLUS 3 YEARS FOR CONCEALING FINANCIAL "
     "DISCLOSURE DATA, THE HEAVIER TERM APPLIED | ALIA NASSIF JASSIM: RESTITUTION 14.239BN IQD + $12.442M, "
     "FINE EQUAL TO THE GAINS, SEIZURE OF MOVABLE AND IMMOVABLE ASSETS UPHELD | ASHWAQ SALEM HASSAN: "
     "RESTITUTION ~11.9BN IQD ON THE SAME COUNTS | INTEGRITY COMMISSION MAY PURSUE FURTHER COMPENSATION "
     "ONCE THE RULINGS BECOME FINAL — I.E. THEY ARE NOT YET FINAL | SEPARATELY SEP 23, IRAQ AGREED WITH "
     "4 ARAB STATES TO EXCHANGE INFORMATION ON CROSS-BORDER CORRUPTION | SOURCE: 964 NETWORK"),
   "heroMedia": f"{IMG}/{slug}/hero.jpg", "heroMediaType": "image"},
  "beats": [
   beat("الحكم", "نائبتان.. ونفس العقوبة بنفس اليوم",
    "محكمة الجنايات المركزية المختصة بقضايا الفساد حكمت اليوم الأربعاء بالسجن سبع سنوات على النائبتين عالية نصيف وأشواق سالم حسن، عن جريمة الكسب غير المشروع (شبكة 964).",
    "7", "Years in prison for each of two sitting MPs, ruled Wednesday 23 Sep",
    "سنوات سجناً لكل من النائبتين بحكم صدر الأربعاء 23 أيلول (شبكة 964)",
    [("نائبتان", "2"), ("تهمة ثانية", "3 سنوات"), ("تاريخ الحكم", "23 أيلول")], 1, slug,
    ["نائبتان بنفس اليوم", "السجن سبع سنوات", "الكسب غير المشروع"]),
   beat("المبالغ", "14.239 مليار دينار و12.442 مليون دولار",
    "المحكمة ألزمت عالية نصيف بردّ 14.239 مليار دينار و12.442 مليون دولار مع غرامة بمقدار المبلغ، وأشواق سالم حسن بردّ نحو 11.9 مليار دينار (شبكة 964).",
    "14.239", "Billion dinars Alia Nassif was ordered to return, alongside $12.442m",
    "مليار دينار ألزمت المحكمة عالية نصيف بردّها إضافة إلى 12.442 مليون دولار (شبكة 964)",
    [("بالدولار", "12.442 مليون"), ("الثانية", "11.9 مليار"), ("الغرامة", "بمقدار المبلغ")], 2, slug,
    ["ردّ 14.239 مليار دينار", "و12.442 مليون دولار", "والثانية 11.9 مليار"]),
   beat("بعدين", "الحكم مو بات.. والحجز على الأموال مستمر",
    "القرار صادّقت عليه المحكمة مع الحجز على الأموال المنقولة وغير المنقولة، وللنزاهة مطالبة بتعويضات إضافية بعد اكتساب الحكم الدرجة القطعية — أي أنه قابل للطعن (شبكة 964).",
    "4", "Arab states Iraq agreed with on 23 Sep to exchange cross-border corruption information",
    "دول عربية اتفق معها العراق في 23 أيلول على تبادل معلومات جرائم الفساد العابرة للحدود (شبكة 964)",
    [("الحجز", "منقول وغير منقول"), ("الطعن", "ما زال ممكناً"), ("تعاون عربي", "4 دول")], 3, slug,
    ["الحكم لسه قابل للطعن", "والحجز على الأموال مستمر", "وتعاون مع أربع دول عربية"]),
  ],
  "arabicTicker": [
   "محكمة الجنايات المركزية المختصة بقضايا الفساد: السجن 7 سنوات للنائبة عالية نصيف جاسم عن الكسب غير المشروع (شبكة 964 — 23 أيلول)",
   "والسجن 7 سنوات للنائبة أشواق سالم حسن عن التهمة نفسها، مع 3 سنوات عن إخفاء بيانات في استمارة الذمة المالية ونفّذت الأشد (شبكة 964)",
   "إلزام عالية نصيف بردّ 14.239 مليار دينار و12.442 مليون دولار وغرامة بمقدار مبلغ الكسب غير المشروع (شبكة 964)",
   "إلزام أشواق سالم حسن بردّ نحو 11.9 مليار دينار وغرامة مماثلة (شبكة 964)",
   "تصديق الحجز على الأموال المنقولة وغير المنقولة، ولهيئة النزاهة المطالبة بتعويضات بعد اكتساب الحكم الدرجة القطعية (شبكة 964)",
   "العراق ينسق مع 4 دول عربية لتبادل المعلومات بشأن جرائم الفساد العابرة للحدود (شبكة 964 — 23 أيلول)",
   "دفعت رشوة حتى تخلّص معاملة؟"],
  "endQuestion": "دفعت رشوة حتى تخلّص معاملة؟",
  "sources": [{"name": "شبكة 964", "domain": "964media.com"},
              {"name": "مجلس القضاء الأعلى", "domain": "sjc.iq"},
              {"name": "هيئة النزاهة", "domain": "nazaha.iq"}]},
 "caption": """قضية فساد نائبة في العراق — شنو صار اليوم؟

محكمة الفساد حكمت بالسجن سبع سنوات على نائبتين بيوم واحد.. والمبالغ المطلوب ردّها كبيرة.

دفعت رشوة حتى تخلّص معاملة؟

المصادر: شبكة 964 (23 أيلول 2026)

#فساد #هيئة_النزاهة #العراق #بغداد #photonectnews
@photonect.news""",
 "brief": {
  "kicker": "عاجل",
  "hookHeadline": "نائبتان.. وسبع سنوات بيوم واحد",
  "voText": ("حكمت محكمة الجنايات المركزية المختصة بقضايا الفساد اليوم الأربعاء بالسجن سبع سنوات على "
    "النائبتين عالية نصيف وأشواق سالم حسن، عن جريمة الكسب غير المشروع. وألزمت المحكمة عالية نصيف "
    "بردّ أربعة عشر ملياراً ومئتين وتسعة وثلاثين مليون دينار، وباثني عشر مليوناً وأربعمئة واثنين "
    "وأربعين ألف دولار، فيما ألزمت أشواق سالم حسن بردّ نحو أحد عشر ملياراً وتسعمئة مليون دينار. "
    "وصادقت المحكمة الحجز على الأموال. والحكمان ما زالا قابلين للطعن ولم يكتسبا الدرجة القطعية، "
    "بحسب شبكة تسعة ستة أربعة. دفعت رشوة حتى تخلّص معاملة؟"),
  "endQuestion": "دفعت رشوة حتى تخلّص معاملة؟",
  "sourcesLine": "المصادر: شبكة 964 · مجلس القضاء الأعلى — 23 أيلول 2026",
  "statPops": [{"value": "7 سنوات", "label": "لكل من النائبتين عن الكسب غير المشروع", "matchWord": "سبع"},
               {"value": "$12.442M", "label": "بالدولار ضمن ما ألزمت به عالية نصيف", "matchWord": "دولار"}]}}

# ════════════════════════ B · 19:45 · P1 dollar anchor ════════════════════════
slug = f"{D}-b-dollar-156750-network"
SLATE[slug] = {
 "props": {
  "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
  "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "iraq_money", "variant": "B",
  "breaking": {
   "arabicKicker": "الدولار اليوم",
   "arabicHeadline": "الدولار ينزل تحت 157 ألفاً.. وشبكة مضاربة تتفكك",
   "englishSubhead": ("BAGHDAD · SEP 23 | 964 MORNING LIST (11:19, WED 23 SEP), PER $100: BAGHDAD SELL 157,000 / "
     "BUY 156,750; ERBIL SELL 157,000 / BUY 156,500; BASRA SELL 156,750 / BUY 156,250; CBI OFFICIAL 131,000 | "
     "SHAFAQ AT CLOSE (13:26, WED): KIFAH & HARITHIYA CLOSED 156,750, DOWN FROM 157,000 THAT MORNING; BAGHDAD "
     "SHOPS SELL 157,250 / BUY 156,250; ERBIL SELL 156,750 / BUY 156,700 | 964'S OWN MORNING LIST ON SUN 20 SEP "
     "PUT BAGHDAD SELL AT 159,750 — A LIKE-FOR-LIKE FALL OF 2,750 IN THREE DAYS (COMPUTED FROM 964'S TWO LISTS) | "
     "GOLD, SHAFAQ WED: NAHR ST WHOLESALE 21K FOREIGN MITHQAL SELL 973,000, UP FROM 965,000 TUESDAY | "
     "INTERIOR MINISTRY FEDERAL INTELLIGENCE AGENCY DISMANTLED A CURRENCY-SPECULATION RING IN RUSAFA: "
     "5 HELD, $240,000 SEIZED, REFERRED UNDER ARTICLE 57 OF THE BANKING LAW"),
   "heroMedia": f"{IMG}/{slug}/hero.jpg", "heroMediaType": "image"},
  "beats": [
   beat("السعر", "قائمة 964: بيع 157,000 ببغداد صباحاً",
    "قائمة شبكة 964 صباح الأربعاء: بيع 100 دولار ببغداد 157,000 دينار، وأربيل 157,000، والبصرة 156,750 — والرسمي عند المركزي 131,000.",
    "157,000", "Dinars, selling price per $100 in Baghdad, 964 morning list, Wednesday",
    "دينار سعر بيع 100 دولار ببغداد في قائمة شبكة 964 صباح الأربعاء",
    [("أربيل", "157,000"), ("البصرة", "156,750"), ("الرسمي", "131,000")], 1, slug,
    ["قائمة 964 صباح الأربعاء", "بغداد البيع 157,000", "والرسمي 131,000"]),
   beat("النزول", "بثلاثة أيام.. نزل 2,750 ديناراً",
    "بإغلاق البورصة سجّلت شفق نيوز 156,750 بعد 157,000 صباحاً. وقائمة 964 نفسها كانت 159,750 يوم الأحد — أي نزول 2,750 ديناراً بثلاثة أيام (محتسب من قائمتَي 964).",
    "2,750", "Dinars the 964 Baghdad morning sell price fell between Sunday and Wednesday (computed)",
    "ديناراً نزول سعر بيع بغداد بين قائمتَي 964 يوم الأحد ويوم الأربعاء (محتسب)",
    [("الأحد", "159,750"), ("الأربعاء", "157,000"), ("الإغلاق", "156,750")], 2, slug,
    ["الإغلاق نزل لـ156,750", "والأحد كان 159,750", "نزول 2,750 ديناراً"]),
   beat("المضاربة", "الاستخبارات تفكك شبكة.. و240 ألف دولار",
    "وكالة الاستخبارات والتحقيقات الاتحادية بالداخلية أعلنت ضبط 5 أشخاص بالرصافة بتهمة المتاجرة بالعملة، وصادرت 240 ألف دولار وأحالتهم وفق المادة 57 من قانون المصارف (شبكة 964).",
    "240,000", "US dollars seized with five suspects in the Rusafa currency-speculation case",
    "دولار صادرتها الاستخبارات مع ضبط 5 أشخاص بقضية المضاربة بالرصافة (شبكة 964)",
    [("الموقوفون", "5"), ("المادة", "57"), ("المكان", "الرصافة")], 3, slug,
    ["الاستخبارات فككت شبكة مضاربة", "خمسة موقوفين بالرصافة", "و240 ألف دولار مصادرة"]),
  ],
  "arabicTicker": [
   "قائمة شبكة 964 صباح الأربعاء: بيع 100 دولار ببغداد 157,000 دينار والشراء 156,750 (شبكة 964 — 23 أيلول)",
   "أربيل: البيع 157,000 والشراء 156,500 — البصرة: البيع 156,750 والشراء 156,250 (شبكة 964)",
   "شفق نيوز عند الإغلاق: بورصتا الكفاح والحارثية 156,750 بعد 157,000 في الصباح، ومحال بغداد بيع 157,250 وشراء 156,250",
   "قائمة 964 يوم الأحد 20 أيلول كانت 159,750 لبيع بغداد — نزول 2,750 ديناراً بثلاثة أيام (محتسب من قائمتَي الشبكة نفسها)",
   "السعر الرسمي للبنك المركزي 131,000 دينار لكل 100 دولار",
   "الذهب: مثقال الأجنبي عيار 21 بشارع النهر بيع 973,000 دينار بعد 965,000 يوم الثلاثاء (شفق نيوز)",
   "الصيرفة بمنطقتك بيعتك بكم اليوم؟"],
  "endQuestion": "الصيرفة بمنطقتك بيعتك بكم اليوم؟",
  "sources": [{"name": "شبكة 964", "domain": "964media.com"},
              {"name": "شفق نيوز", "domain": "shafaq.com"},
              {"name": "وزارة الداخلية", "domain": "moi.gov.iq"}]},
 "caption": """سعر الدولار اليوم في العراق — نزل لوين؟

قائمة 964 تسجّل 157,000 ببغداد والإغلاق أقل.. وبنفس اليوم الاستخبارات تفكك شبكة مضاربة بالعملة.

الصيرفة بمنطقتك بيعتك بكم اليوم؟

المصادر: شبكة 964، شفق نيوز (23 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #بغداد #photonectnews
@photonect.news""",
 "brief": {
  "kicker": "الدولار اليوم",
  "hookHeadline": "نزل تحت 157.. وشبكة تتفكك",
  "voText": ("تراجع الدولار اليوم الأربعاء في الأسواق العراقية. فبحسب القائمة الصباحية لشبكة تسعة ستة "
    "أربعة، بلغ سعر بيع مئة دولار في بغداد مئة وسبعة وخمسين ألف دينار، بينما بقي السعر الرسمي لدى "
    "البنك المركزي عند مئة وواحد وثلاثين ألفاً. وعند الإغلاق سجّلت شفق نيوز مئة وستة وخمسين ألفاً "
    "وسبعمئة وخمسين. وفي اليوم نفسه أعلنت وكالة الاستخبارات الاتحادية ضبط خمسة أشخاص في الرصافة "
    "بتهمة المتاجرة بالعملة، ومصادرة مئتين وأربعين ألف دولار. الصيرفة بمنطقتك بيعتك بكم اليوم؟"),
  "endQuestion": "الصيرفة بمنطقتك بيعتك بكم اليوم؟",
  "sourcesLine": "المصادر: شبكة 964 · شفق نيوز · وزارة الداخلية — 23 أيلول 2026",
  "statPops": [{"value": "157,000", "label": "بيع 100 دولار في بغداد (قائمة 964)", "matchWord": "بغداد"},
               {"value": "$240K", "label": "مصادرة بقضية المضاربة في الرصافة", "matchWord": "الرصافة"}]}}

# ════════════════════════ C · 21:15 · P2 geopolitics ══════════════════════════
slug = f"{D}-c-withdrawal-30-september"
SLATE[slug] = {
 "props": {
  "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
  "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "mena_geo", "variant": "A",
  "breaking": {
   "arabicKicker": "المنطقة",
   "arabicHeadline": "30 أيلول.. موعد واحد للانسحاب ولخطة حصر السلاح",
   "englishSubhead": ("BAGHDAD / WASHINGTON · SEP 23 | A US STATE DEPARTMENT SPOKESPERSON TOLD SHAFAQ NEWS (08:02, "
     "WED 23 SEP) WASHINGTON IS PROCEEDING ON THE TRANSITION TIMELINE AGREED WITH BAGHDAD TO END COALITION "
     "MILITARY OPERATIONS, AND IS 'FOCUSED ON COMPLETING THE WITHDRAWAL OF OUR FORCES BY 30 SEPTEMBER', ALIGNED "
     "WITH THE END OF OPERATION INHERENT RESOLVE | SAME DAY, NOURI AL-MALIKI TOLD US CHARGE D'AFFAIRES STEPHEN "
     "FAGEN IRAQ IS PROCEEDING ON PLACING WEAPONS IN STATE HANDS PER CONSTITUTION AND LAW, AND THAT A PLAN AND "
     "TIMELINE WILL BE ANNOUNCED ON 30 SEPTEMBER | AL-MALIKI RESTATED IRAQ REJECTS ITS TERRITORY BEING USED TO "
     "ATTACK NEIGHBOURS | THE SPOKESPERSON DID NOT STATE A POSITION ON A DISARMAMENT PLAN RUNNING TO MID-2027 | "
     "BAHAA AL-ARAJI SAYS FACTIONS ACCEPTED THE PRINCIPLE, DISPUTE IS OVER THE HANDOVER DEADLINE"),
   "heroMedia": f"{IMG}/{slug}/hero.jpg", "heroMediaType": "image"},
  "beats": [
   beat("الانسحاب", "واشنطن: نركز على إكمال الانسحاب بـ30 أيلول",
    "متحدث باسم الخارجية الأميركية قال لشفق نيوز إن واشنطن ماضية بالجدول المتفق عليه مع بغداد لإنهاء عمليات التحالف، وتركز على إكمال انسحاب قواتها بحلول 30 أيلول.",
    "30", "September — the date Washington says it is focused on completing the withdrawal by",
    "أيلول الموعد الذي تقول واشنطن إنها تركز على إكمال الانسحاب بحلوله (شفق نيوز)",
    [("المصدر", "الخارجية الأميركية"), ("العملية", "العزم الصلب"), ("التاريخ", "30 أيلول")], 1, slug,
    ["واشنطن تتحدث لشفق نيوز", "نركز على إكمال الانسحاب", "بحلول 30 أيلول"]),
   beat("السلاح", "المالكي: الخطة والسقف الزمني بنفس اليوم",
    "نوري المالكي أبلغ القائم بالأعمال الأميركي ستيفن فيغن أن العراق ماضٍ بملف حصر السلاح وفق الدستور والقانون، وأن خطة وسقفاً زمنياً سيُعلنان في 30 أيلول (شبكة 964).",
    "7", "Days between this ruling-day briefing on 23 Sep and the 30 Sep announcement (computed)",
    "أيام تفصل بين تصريح 23 أيلول وموعد الإعلان في 30 أيلول (محتسب)",
    [("الجهة", "نوري المالكي"), ("المخاطَب", "ستيفن فيغن"), ("الإعلان", "30 أيلول")], 2, slug,
    ["المالكي يبلغ القائم بالأعمال", "حصر السلاح وفق الدستور", "والإعلان بـ30 أيلول"]),
   beat("الخلاف", "الاتفاق على المبدأ.. والخلاف على المهلة",
    "بهاء الأعرجي قال إن الفصائل وافقت على حصر السلاح والخلاف على مهلة التسليم. والمتحدث الأميركي لم يُبدِ موقفاً من خطة تمتد إلى منتصف 2027 (شبكة 964، شفق نيوز).",
    "2027", "Mid-year the reported disarmament plan runs to; Washington took no position on it",
    "منتصف العام الذي تمتد إليه الخطة المتداولة لحصر السلاح دون موقف أميركي معلن (شفق نيوز)",
    [("الموقف", "الفصائل وافقت"), ("الخلاف", "مهلة التسليم"), ("واشنطن", "بلا موقف معلن")], 3, slug,
    ["الفصائل وافقت على المبدأ", "والخلاف على مهلة التسليم", "وخطة تمتد لمنتصف 2027"]),
  ],
  "arabicTicker": [
   "متحدث باسم الخارجية الأميركية لشفق نيوز: نركز على استكمال انسحاب قواتنا من العراق بحلول 30 أيلول (شفق نيوز — 23 أيلول)",
   "واشنطن: ماضون وفق الجدول الانتقالي المتفق عليه مع بغداد لإنهاء العمليات العسكرية لقوات التحالف (شفق نيوز)",
   "نوري المالكي للقائم بالأعمال الأميركي ستيفن فيغن: خطة وسقف زمني لحصر السلاح سيُعلنان في 30 أيلول (شبكة 964 — 23 أيلول)",
   "المالكي: معالجة الملف عبر الحوار والتفاهم ووفق الأطر الدستورية والقانونية، ورفض استخدام أرض العراق لمهاجمة أي دولة جوار (شبكة 964)",
   "المتحدث الأميركي لم يحدد موقفاً من خطة لحصر السلاح تمتد إلى منتصف 2027 (شفق نيوز)",
   "بهاء الأعرجي: الفصائل وافقت على حصر السلاح والخلاف حول مهلة التسليم (شبكة 964)",
   "تحس منطقتك أأمن من قبل سنة؟"],
  "endQuestion": "تحس منطقتك أأمن من قبل سنة؟",
  "sources": [{"name": "شفق نيوز", "domain": "shafaq.com"},
              {"name": "شبكة 964", "domain": "964media.com"},
              {"name": "الخارجية الأميركية", "domain": "state.gov"}]},
 "caption": """انسحاب القوات الأميركية من العراق — شنو يصير بـ30 أيلول؟

واشنطن تحچي لشفق نيوز عن موعد الانسحاب.. وبنفس التاريخ تُعلن خطة حصر السلاح.

تحس منطقتك أأمن من قبل سنة؟

المصادر: شفق نيوز، شبكة 964 (23 أيلول 2026)

#العراق #الانسحاب_الأميركي #حصر_السلاح #بغداد #photonectnews
@photonect.news""",
 "brief": {
  "kicker": "المنطقة",
  "hookHeadline": "تاريخ واحد.. وملفّان كبيران",
  "voText": ("قال متحدث باسم الخارجية الأميركية لشفق نيوز اليوم الأربعاء إن واشنطن ماضية وفق الجدول "
    "الانتقالي المتفق عليه مع بغداد لإنهاء العمليات العسكرية لقوات التحالف، وإنها تركز على استكمال "
    "انسحاب قواتها بحلول الثلاثين من أيلول. وفي اليوم نفسه أبلغ نوري المالكي القائم بالأعمال الأميركي "
    "ستيفن فيغن أن العراق ماضٍ في ملف حصر السلاح وفق الدستور والقانون، وأن خطة وسقفاً زمنياً سيُعلنان "
    "في التاريخ ذاته. أما مهلة التسليم فما زالت موضع خلاف. تحس منطقتك أأمن من قبل سنة؟"),
  "endQuestion": "تحس منطقتك أأمن من قبل سنة؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 23 أيلول 2026",
  "statPops": [{"value": "30 أيلول", "label": "موعد إكمال الانسحاب بحسب واشنطن", "matchWord": "الثلاثين"},
               {"value": "حصر السلاح", "label": "خطة وسقف زمني يُعلنان بالتاريخ نفسه", "matchWord": "فيغن"}]}}

# ════════════════════════ D · 22:30 · P1 fuel / parliament ════════════════════
slug = f"{D}-d-fuel-decision-429"
SLATE[slug] = {
 "props": {
  "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
  "audioBed": "audio/mood_mideast.mp3", "topicBucket": "iraq_money", "variant": "B",
  "breaking": {
   "arabicKicker": "قرار",
   "arabicHeadline": "البرلمان يطالب الحكومة بالتراجع عن رفع أسعار الوقود",
   "englishSubhead": ("BAGHDAD · SEP 23 | PARLIAMENT ISSUED LEGISLATIVE DECISION No. 55 OF 2026 CALLING ON THE "
     "GOVERNMENT TO RECONSIDER CABINET DECISION No. 429 OF 2026, WHICH RAISED PETROLEUM-DERIVATIVE PRICES, AND "
     "TO COMMISSION A STUDY OF THE ECONOMIC AND SOCIAL EFFECTS ON TRANSPORT, PRODUCTION AND EMPLOYMENT COSTS | "
     "12 RECOMMENDATIONS INCLUDE RESTORING THE AGRICULTURAL FUEL SUBSIDY, ELECTRONIC MONITORING AGAINST "
     "SMUGGLING, AND TIMELINES FOR REFINERY PROJECTS | SHAFAQ REPORTS THE RECOMMENDATIONS WERE VOTED ON MON 21 "
     "SEP WITH 232 MPs PRESENT | NEITHER THE DECISION TEXT AS PUBLISHED NOR THE PARLIAMENT REPORTING DISCLOSES "
     "PER-LITRE PRICES, AND THE REELS MAKES NO CLAIM ABOUT PUMP PRICES FOR CITIZENS | SOURCES: 964, SHAFAQ"),
   "heroMedia": f"{IMG}/{slug}/hero.jpg", "heroMediaType": "image"},
  "beats": [
   beat("القرار", "قرار نيابي 55 يطالب بمراجعة قرار 429",
    "مجلس النواب أصدر القرار النيابي رقم 55 لسنة 2026 داعياً الحكومة لإعادة النظر بقرار مجلس الوزراء رقم 429 القاضي بزيادة أسعار المشتقات النفطية (شبكة 964).",
    "55", "The parliamentary decision number issued on 23 Sep against Cabinet decision 429",
    "رقم القرار النيابي الصادر في 23 أيلول بمواجهة قرار مجلس الوزراء 429 (شبكة 964)",
    [("قرار الوزراء", "429"), ("قرار النواب", "55"), ("السنة", "2026")], 1, slug,
    ["قرار نيابي رقم 55", "يطالب بإعادة النظر", "بقرار الوزراء 429"]),
   beat("الطلبات", "12 توصية.. ودعم الزراعة يرجع",
    "التوصيات شملت دراسة الآثار الاقتصادية والاجتماعية على كلف النقل والإنتاج، وإعادة دعم الوقود للقطاع الزراعي، ومراقبة إلكترونية لمنع التهريب، وسقوفاً زمنية لمشاريع المصافي.",
    "12", "Recommendations parliament attached to its decision",
    "توصية أرفقها مجلس النواب بقراره (شبكة 964)",
    [("النقل", "دراسة الكلف"), ("الزراعة", "إعادة الدعم"), ("التهريب", "مراقبة إلكترونية")], 2, slug,
    ["اثنا عشر توصية بالقرار", "إعادة دعم الوقود للزراعة", "ومراقبة إلكترونية للتهريب"]),
   beat("الغامض", "بس الأسعار باللتر.. ما انذكرت",
    "شفق نيوز ذكرت أن التصويت جرى الاثنين بحضور 232 نائباً. ولا نص القرار المنشور ولا تغطية الجلسة ذكرا سعر اللتر، والبرلمان طلب تقريراً بالإنتاج والاستيراد والاستهلاك والخزين.",
    "232", "MPs present at the vote on the fuel recommendations, per Shafaq",
    "نائباً حضروا التصويت على توصيات أزمة الوقود بحسب شفق نيوز",
    [("التصويت", "الاثنين 21 أيلول"), ("الحضور", "232 نائباً"), ("سعر اللتر", "غير معلن")], 3, slug,
    ["التصويت بحضور 232 نائباً", "بس سعر اللتر ما انذكر", "والبرلمان يطلب تقريراً بالأرقام"]),
  ],
  "arabicTicker": [
   "مجلس النواب يصدر القرار النيابي رقم (55) لسنة 2026 داعياً لإعادة النظر بقرار مجلس الوزراء رقم (429) لسنة 2026 برفع أسعار المشتقات النفطية (شبكة 964 — 23 أيلول)",
   "البرلمان يطالب بدراسة تقييمية للآثار الاقتصادية والاجتماعية الناجمة عن الترفيع، وخصوصاً على كلف النقل والإنتاج والتشغيل (شبكة 964)",
   "من التوصيات: إعادة دعم الوقود للقطاع الزراعي، ومراقبة إلكترونية لمنع التهريب، وسقوف زمنية لمشاريع تطوير المصافي (شبكة 964)",
   "ومنها كذلك: خطة عاجلة لمنع تكرار أزمات الوقود وضمان انسيابية التجهيز بين المحافظات (شفق نيوز)",
   "وتقرير مفصل إلى المجلس يتضمن حجم الإنتاج والاستيراد والاستهلاك والكلف والخزين الستراتيجي (شفق نيوز)",
   "شفق نيوز: التصويت على التوصيات جرى الاثنين 21 أيلول بحضور 232 نائباً — ولم يُعلَن سعر اللتر في أي من التغطيتين",
   "شكد تدفع بنزين بالأسبوع؟"],
  "endQuestion": "شكد تدفع بنزين بالأسبوع؟",
  "sources": [{"name": "شبكة 964", "domain": "964media.com"},
              {"name": "شفق نيوز", "domain": "shafaq.com"},
              {"name": "مجلس النواب العراقي", "domain": "parliament.iq"}]},
 "caption": """أسعار الوقود في العراق — البرلمان شنو قرر؟

قرار نيابي يطالب الحكومة تراجع زيادة أسعار المشتقات.. و12 توصية وراه.

شكد تدفع بنزين بالأسبوع؟

المصادر: شبكة 964، شفق نيوز (23 أيلول 2026)

#أسعار_الوقود #البرلمان_العراقي #العراق #بغداد #photonectnews
@photonect.news""",
 "brief": {
  "kicker": "قرار",
  "hookHeadline": "البرلمان يقول: راجعوا الزيادة",
  "voText": ("أصدر مجلس النواب العراقي اليوم الأربعاء قراراً نيابياً يحمل الرقم خمسة وخمسين لسنة ألفين "
    "وستة وعشرين، يدعو الحكومة إلى إعادة النظر في قرار مجلس الوزراء الذي رفع أسعار المشتقات النفطية، "
    "وإلى إعداد دراسة للآثار الاقتصادية والاجتماعية على كلف النقل والإنتاج. وتضمّن القرار توصيات منها "
    "إعادة دعم الوقود للقطاع الزراعي ومراقبة إلكترونية لمنع التهريب. ولم يُعلَن سعر اللتر في نص القرار "
    "ولا في تغطية الجلسة، بحسب شبكة تسعة ستة أربعة وشفق نيوز. شكد تدفع بنزين بالأسبوع؟"),
  "endQuestion": "شكد تدفع بنزين بالأسبوع؟",
  "sourcesLine": "المصادر: شبكة 964 · شفق نيوز · مجلس النواب — 23 أيلول 2026",
  "statPops": [{"value": "قرار 55", "label": "القرار النيابي الصادر اليوم", "matchWord": "نيابياً"},
               {"value": "الزراعة", "label": "إعادة دعم الوقود للقطاع الزراعي", "matchWord": "الزراعي"}]}}

# ═══════════════ E · 23:45 · P3 health/environment · V10.1 CONTROL ════════════
slug = f"{D}-e-tigris-euphrates-pollution"
SLATE[slug] = {
 "props": {
  "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
  "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "region_health", "variant": "C",
  "breaking": {
   "arabicKicker": "بيئة",
   "arabicHeadline": "لجنة نيابية: تلوث دجلة والفرات يسبب سرطانات",
   "englishSubhead": ("BAGHDAD · SEP 23 | PARLIAMENTARY COMMITTEE No. 63 OF 2026 ON TIGRIS AND EUPHRATES POLLUTION, "
     "CHAIRED BY MP YOUSUF AL-KALABI, SAID ON WED 23 SEP THERE ARE DOZENS OF POLLUTION PROBLEMS IN BOTH RIVERS "
     "CAUSING CATASTROPHIC OUTCOMES INCLUDING CANCER AND KIDNEY FAILURE | AL-KALABI SAID WHAT IRAQ LOSES ANNUALLY "
     "TO WATER POLLUTION 'MAY MATCH THE NUMBER OF TERRORISM VICTIMS' — HIS CHARACTERISATION, NOT A MEASURED "
     "FIGURE; NO CASE COUNT WAS PUBLISHED | THE COMMITTEE EXAMINED THE DIYALA TRIBUTARY'S DISCHARGE INTO THE "
     "TIGRIS | RECOMMENDATIONS DUE 24 SEP INCLUDE DECLARING MAXIMUM EMERGENCY, A NATIONAL CAMPAIGN LED BY THE "
     "PM, AND HEAVIER PENALTIES UNDER THE ENVIRONMENT LAW | SOURCE: 964 NETWORK, 14:35"),
   "heroMedia": f"{IMG}/{slug}/hero.jpg", "heroMediaType": "image"},
  "beats": [
   beat("التحذير", "دجلة والفرات وديالى.. عشرات مشاكل التلوث",
    "اللجنة النيابية رقم 63 لسنة 2026 الخاصة بتلوث دجلة والفرات قالت إن بالنهرين عشرات مشاكل التلوث تسبب أمراضاً كارثية منها السرطان والفشل الكلوي (شبكة 964).",
    "3", "Waterways the committee examined: the Tigris, the Euphrates and the Diyala tributary",
    "مجارٍ مائية بحثتها اللجنة: دجلة والفرات ورافد ديالى (شبكة 964)",
    [("اللجنة", "رقم 63"), ("الأنهر", "دجلة والفرات"), ("الرافد", "ديالى")], 1, slug,
    ["لجنة نيابية تفحص النهرين", "عشرات مشاكل التلوث", "سرطان وفشل كلوي"]),
   beat("المقارنة", "رئيس اللجنة يشبّهها بضحايا الإرهاب",
    "رئيس اللجنة النائب يوسف الكلابي قال إن ما يخسره العراق سنوياً من تلوث المياه قد يوازي عدد ضحايا الإرهاب — وهو توصيف منه، ولم تُنشر أرقام حالات (شبكة 964).",
    "63", "The number of the parliamentary committee formed on river pollution this year",
    "رقم اللجنة النيابية المشكّلة هذا العام بشأن تلوث النهرين (شبكة 964)",
    [("المتحدث", "يوسف الكلابي"), ("الصفة", "رئيس اللجنة"), ("أرقام الحالات", "غير منشورة")], 2, slug,
    ["رئيس اللجنة يوسف الكلابي", "يشبّهها بضحايا الإرهاب", "وما نُشرت أرقام حالات"]),
   beat("التوصيات", "طوارئ قصوى.. والتوصيات بكرة",
    "اللجنة قالت إن توصياتها تُعلن في 24 أيلول وتشمل إعلان حالة طوارئ قصوى وحملة وطنية برئاسة رئيس الوزراء، وتشديد عقوبات قانون البيئة (شبكة 964).",
    "24", "September — the day the committee said its recommendations would be announced",
    "أيلول موعد إعلان توصيات اللجنة بحسب ما نقلته الشبكة (شبكة 964)",
    [("الطوارئ", "قصوى"), ("الحملة", "برئاسة الوزراء"), ("العقوبات", "تشديد")], 3, slug,
    ["التوصيات تُعلن بـ24 أيلول", "طوارئ قصوى وحملة وطنية", "وتشديد عقوبات البيئة"]),
  ],
  "arabicTicker": [
   "اللجنة النيابية رقم (63) لسنة 2026 الخاصة بتلوث نهري دجلة والفرات تحذّر من عشرات مشاكل التلوث في النهرين (شبكة 964 — 23 أيلول)",
   "اللجنة: التلوث يسبب مشاكل كارثية من بينها السرطان والفشل الكلوي (شبكة 964)",
   "رئيس اللجنة النائب يوسف الكلابي: ما يخسره العراق سنوياً من تلوث المياه قد يوازي عدد ضحايا الإرهاب — توصيف منه ولم تُنشر أرقام حالات",
   "اللجنة بحثت اندفاع المياه من رافد ديالى إلى نهر دجلة (شبكة 964)",
   "التوصيات تُعلن في 24 أيلول وتشمل إعلان حالة طوارئ قصوى وحملة وطنية برئاسة رئيس مجلس الوزراء (شبكة 964)",
   "ومن التوصيات كذلك تشديد العقوبات في قانون حماية وتحسين البيئة (شبكة 964)",
   "تشرب من مي الإسالة لو تشتري؟"],
  "endQuestion": "تشرب من مي الإسالة لو تشتري؟",
  "sources": [{"name": "شبكة 964", "domain": "964media.com"},
              {"name": "مجلس النواب العراقي", "domain": "parliament.iq"},
              {"name": "وزارة البيئة", "domain": "moen.gov.iq"}]},
 "caption": """تلوث دجلة والفرات — شنو تقول اللجنة النيابية؟

لجنة برلمانية تتحدث عن عشرات مشاكل التلوث بالنهرين وأمراض خطيرة.. وتوصياتها تنزل بكرة.

تشرب من مي الإسالة لو تشتري؟

المصادر: شبكة 964 (23 أيلول 2026)

#دجلة #تلوث_المياه #العراق #صحة #photonectnews
@photonect.news""",
 "brief": None}


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
                 "audioBed": data["props"]["audioBed"],
                 "statPops": b.pop("statPops")}
            # keep canonical key order
            order = ["slug", "kicker", "hookHeadline", "voText", "endQuestion",
                     "sourcesLine", "images", "audioBed", "statPops"]
            b = {k: b[k] for k in order}
            (d / "v11-brief.json").write_text(json.dumps(b, ensure_ascii=False, indent=1))
        print(f"  ✓ {slug}  (brief={'yes' if data['brief'] else 'NO — V10.1 control'})")
    print(f"\n== authored {len(SLATE)} slugs ==")


if __name__ == "__main__":
    main()
