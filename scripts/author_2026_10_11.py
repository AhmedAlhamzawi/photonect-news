#!/usr/bin/env python3
"""Author the 2026-10-11 slate: props.json + caption.txt (+ v11-brief.json on a, b, c, d; e = V10.1 control).

Every figure traces to a named source saved in the session scratchpad (Shafaq full-text RSS, 964 + Rudaw article pages).
Computed figures carry (محتسب). PRE-copywriter draft: do NOT re-run after the Opus copywriter/gate edits.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-11"
DATE_LABEL = "OCT 11 • 2026"
AR_DATE = "11 تشرين الأول 2026"
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


GEN = "صورة توضيحية"
COMMONS = "ويكيميديا كومنز"
SLATE = {}


# ═══════════ A · 18:00 · P1 housing (LEAD) — Watan: 95,000 free plots launched in Karbala + Najaf ═══════════
slug = f"{D}-a-watan-95k-plots"
p = base(slug, "iraq_money", "A", "السكن", "ما عندك بيت؟ 95 ألف قطعة أرض مجاناً",
  ("KARBALA/NAJAF · OCT 10 | PM ALI AL-ZAIDI LAUNCHED WORKS ON 95,000 RESIDENTIAL PLOTS UNDER THE 'WATAN' INITIATIVE: 60,000 IN KARBALA, 35,000 IN NAJAF (RUDAW, 964); "
   "NINEVEH NEXT | TARGET 1 MILLION PLOTS NATIONWIDE | PM OFFICE (VIA SHAFAQ): PLOTS FULLY FREE FOR EVERY FAMILY WHERE NO MEMBER OWNS A HOME OR PROPERTY | "
   "PLANNING MINISTRY (VIA SHAFAQ): ~104,000 FULLY INFORMAL HOUSING UNITS | ZAIDI: DEEDS NEXT, GOVT WILL HELP BUILD, 'COST THE BUDGET NOT ONE DINAR'"))
p["beats"] = [
 beat("الإطلاق", "95 ألف قطعة.. كربلاء أولاً ثم النجف",
  "أطلق رئيس الوزراء علي الزيدي السبت العمل بـ95 ألف قطعة أرض سكنية: 60 ألفاً في كربلاء و35 ألفاً في النجف، ضمن «مبادرة وطن» (رووداو، 964).",
  "95,000", "Residential plots launched on Saturday in Karbala (60,000) and Najaf (35,000) under the Watan initiative (Rudaw / 964)", "قطعة أرض سكنية في كربلاء والنجف",
  [("كربلاء", "60,000"), ("النجف", "35,000"), ("الهدف", "مليون قطعة")], 1, slug,
  ["95 ألف قطعة أرض", "60 ألفاً بكربلاء و35 ألفاً بالنجف", "ضمن «مبادرة وطن»"], GEN),
 beat("من يشمل؟", "مجانية.. لكل عائلة لا تملك سكناً",
  "مكتب رئيس الوزراء لشفق نيوز: القطع مجانية لكل عائلة لا يملك أي من أفرادها سكناً. ووزارة التخطيط تحصي نحو 104 آلاف وحدة سكنية عشوائية.",
  "104,000", "Fully informal housing units counted by the Planning Ministry (via Shafaq News)", "وحدة سكنية عشوائية — وزارة التخطيط",
  [("السعر", "مجاناً"), ("الشرط", "بلا سكن ملك"), ("العشوائيات", "104 آلاف")], 2, slug,
  ["القطع مجانية بالكامل", "لكل عائلة لا تملك سكناً", "104 آلاف وحدة عشوائية"], GEN),
 beat("الوعد", "الزيدي: السندات قادمة.. و«لا كلفة على الموازنة»",
  "الزيدي: المرحلة المقبلة توزيع السندات، والحكومة ستساعد في البناء، والمبادرة «لم تكلف الموازنة ديناراً واحداً» بتعاون رجال أعمال. نينوى المحطة التالية (رووداو، 964).",
  "1,000,000", "Residential plots targeted nationwide by the Watan initiative (PM office via Rudaw / 964)", "قطعة أرض هدف المبادرة في عموم العراق",
  [("التالي", "نينوى"), ("بعدها", "السندات"), ("الموازنة", "لا كلفة (الزيدي)")], 3, slug,
  ["الزيدي: السندات قادمة", "والحكومة تساعد بالبناء", "«لم تكلف الموازنة ديناراً»"], COMMONS),
]
p["arabicTicker"] = [
 "الزيدي يطلق العمل بـ95 ألف قطعة أرض سكنية في كربلاء والنجف ضمن «مبادرة وطن» (رووداو، 964)",
 "كربلاء 60 ألف قطعة — النجف 35 ألفاً — ونينوى المحطة التالية",
 "مكتب رئيس الوزراء: القطع مجانية لكل عائلة لا يملك أي من أفرادها سكناً (شفق نيوز)",
 "وزارة التخطيط: نحو 104 آلاف وحدة سكنية عشوائية بالكامل",
 "ساكن ملك لو إيجار؟",
]
p["endQuestion"] = "ساكن ملك لو إيجار؟"
p["sources"] = [{"name": "رووداو", "domain": "rudawarabia.net"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "مكتب رئيس الوزراء", "domain": "pmo.iq"}]
SLATE[slug] = (p, {
 "kicker": "السكن", "hookHeadline": "ما عندك بيت؟ الأرض صارت مجانية",
 "voText": ("رئيس الوزراء علي الزيدي أطلق السبت العمل بخمسة وتسعين ألف قطعة أرض سكنية ضمن مبادرة وطن، ستين ألفاً في كربلاء وخمسة وثلاثين ألفاً في النجف، "
            "ونينوى هي المحطة التالية. ويقول مكتبه إن القطع مجانية لكل عائلة لا يملك أي من أفرادها سكناً، فيما تحصي وزارة التخطيط نحو مئة وأربعة آلاف وحدة سكنية عشوائية. "
            "وتعهد الزيدي بتوزيع السندات في المرحلة المقبلة والمساعدة في البناء، وقال إن المبادرة لم تكلف الموازنة ديناراً واحداً. ساكن ملك لو إيجار؟"),
 "endQuestion": "ساكن ملك لو إيجار؟",
 "sourcesLine": "المصادر: رووداو · شبكة 964 · شفق نيوز — 10 تشرين الأول 2026",
 "statPops": [{"value": "95,000", "label": "قطعة أرض سكنية في كربلاء والنجف", "matchWord": "وتسعين"},
              {"value": "104,000", "label": "وحدة سكنية عشوائية — وزارة التخطيط", "matchWord": "عشوائية"}],
}, """مبادرة وطن — قطعة أرض مجانية، منو يشملها؟

انطلقت من كربلاء والنجف.. الشرط والوعد والخطوة الجاية بالفيديو.

ساكن ملك لو إيجار؟

المصادر: رووداو، شبكة 964، شفق نيوز (10 تشرين الأول 2026)

#مبادرة_وطن #قطع_الأراضي #السكن #العراق #photonectnews
@photonect.news
""")

# ═══════════ B · 19:45 · P1 dollar anchor — 163,300 Sunday morning, gap over official narrows ═══════════
slug = f"{D}-b-dollar-163300-gap"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار 163,300.. والفرق عن الرسمي يضيق",
  ("BAGHDAD · OCT 11 | SHAFAQ: KIFAH/HARITHIYA 163,300 IQD PER $100 SUNDAY MORNING (VS 163,600 SATURDAY MORNING); BAGHDAD SHOPS SELL 163,750 / BUY 162,750; "
   "ERBIL SELL 163,100 | WED 7 OCT MORNING (DAY 1 OF NEW OFFICIAL 152,000): 168,500 (SHAFAQ) | GAP OVER OFFICIAL 16,500 → 11,300 (COMPUTED, MORNING VS MORNING) | "
   "ECONOMIST NABIL AL-MARSOUMI (FB VIA 964): STABILITY AT 1,600-1,630 PER $ MEANS LOWER GOODS PRICES, TRADERS ALREADY PRICED AT 1,600"))
p["beats"] = [
 beat("البورصة", "الكفاح والحارثية: 163,300 صباح الأحد",
  "شفق نيوز: سجلت بورصتا الكفاح والحارثية 163,300 دينار لكل 100 دولار صباح الأحد، بعد 163,600 صباح السبت. محال بغداد تبيع بـ163,750 وتشتري بـ162,750.",
  "163,300", "IQD per $100 at Kifah/Harithiya on Sunday morning, from 163,600 Saturday morning (Shafaq News)", "دينار لكل 100 دولار — الكفاح صباح الأحد",
  [("السبت صباحاً", "163,600"), ("بيع المحال", "163,750"), ("أربيل بيع", "163,100")], 1, slug,
  ["الكفاح: 163,300 صباح الأحد", "بعد 163,600 السبت", "المحال تبيع بـ163,750"], GEN),
 beat("الفجوة", "من 16,500 إلى 11,300 فوق الرسمي",
  "صباح الأربعاء، أول أيام السعر الرسمي الجديد 152,000، سجلت الكفاح 168,500 (شفق نيوز). الفرق عن الرسمي نزل من 16,500 إلى 11,300 دينار (محتسب).",
  "11,300", "IQD above the official 152,000 per $100 on Sunday morning, down from 16,500 on Wednesday morning (computed from Shafaq figures)", "دينار فوق الرسمي لكل 100 دولار (محتسب)",
  [("الأربعاء صباحاً", "168,500"), ("الرسمي", "152,000"), ("الأحد صباحاً", "163,300")], 2, slug,
  ["الأربعاء: 168,500", "الأحد: 163,300", "الفرق نزل إلى 11,300"], GEN),
 beat("الأسعار", "المرسومي: استقرار 1,600–1,630 يعني تراجع الأسعار",
  "الخبير نبيل المرسومي (فيسبوك، عبر 964): استقرار الدولار بين 1,600 و1,630 ديناراً يعني تراجع أسعار السلع، لأن التجار كانوا يسعّرون أصلاً على 1,600 قبل القرار.",
  "1,600", "IQD per dollar that traders were already pricing goods at before the rate change, per economist Nabil al-Marsoumi (via 964)", "دينار للدولار — تسعيرة التجار قبل القرار (المرسومي)",
  [("نطاق الاستقرار", "1,600–1,630"), ("التوقع", "تراجع الأسعار"), ("المصدر", "المرسومي")], 3, slug,
  ["المرسومي: استقرار 1,600–1,630", "يعني تراجع أسعار السلع", "التجار سعّروا على 1,600"], COMMONS),
]
p["arabicTicker"] = [
 "شفق نيوز: الكفاح والحارثية 163,300 دينار لكل 100 دولار صباح الأحد بعد 163,600 صباح السبت",
 "محال بغداد: بيع 163,750 — شراء 162,750 | أربيل: بيع 163,100",
 "الفرق عن السعر الرسمي 152,000 نزل من 16,500 صباح الأربعاء إلى 11,300 (محتسب)",
 "المرسومي: استقرار الدولار بين 1,600 و1,630 يعني تراجع أسعار السلع",
 "الأسعار نزلت عدكم لو بعدها؟",
]
p["endQuestion"] = "الأسعار نزلت عدكم لو بعدها؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "نبيل المرسومي (فيسبوك عبر 964)", "domain": "964media.com"}, {"name": "البنك المركزي العراقي", "domain": "cbi.iq"}]
SLATE[slug] = (p, {
 "kicker": "الدولار اليوم", "hookHeadline": "الدولار ينزل.. والأسعار؟",
 "voText": ("الدولار يواصل النزول ببطء. سجلت بورصتا الكفاح والحارثية صباح الأحد مئة وثلاثة وستين ألفاً وثلاثمئة دينار لكل مئة دولار بحسب شفق نيوز، "
            "بعد مئة وثمانية وستين ألفاً وخمسمئة صباح الأربعاء، أول أيام السعر الرسمي الجديد. يعني الفرق عن السعر الرسمي نزل من ستة عشر ألفاً وخمسمئة "
            "إلى أحد عشر ألفاً وثلاثمئة دينار بحسب حسابنا. والخبير نبيل المرسومي يرى أن استقرار الدولار بين ألف وستمئة وألف وستمئة وثلاثين ديناراً يعني تراجع أسعار السلع، "
            "لأن التجار سعّروا أصلاً على ألف وستمئة. الأسعار نزلت عدكم لو بعدها؟"),
 "endQuestion": "الأسعار نزلت عدكم لو بعدها؟",
 "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 7 إلى 11 تشرين الأول 2026",
 "statPops": [{"value": "163,300", "label": "دينار لكل 100 دولار — الكفاح صباح الأحد (شفق نيوز)", "matchWord": "وثلاثة"},
              {"value": "11,300", "label": "دينار فوق السعر الرسمي لكل 100 دولار (محتسب)", "matchWord": "حسابنا"}],
}, """سعر الدولار في العراق اليوم — الفرق عن الرسمي يضيق؟

بورصة الكفاح من الأربعاء لليوم، وشنو يعني هذا لأسعار السوق.. بالفيديو.

الأسعار نزلت عدكم لو بعدها؟

المصادر: شفق نيوز، شبكة 964 (7 إلى 11 تشرين الأول 2026)

#سعر_الدولار #الدولار_اليوم #الدينار_العراقي #العراق #photonectnews
@photonect.news
""")

# ═══════════ C · 21:15 · P2 region — Riyadh airport attack, Gulf flights, Baghdad's position + PM trip ═══════════
slug = f"{D}-c-riyadh-airport-flights"
p = base(slug, "mena_geo", "A", "عاجل", "مطار الرياض: 12 قتيلاً.. وبغداد تدين",
  ("RIYADH · OCT 10-11 | SAUDI GACA: ATTACK ON KING KHALID INTERNATIONAL AIRPORT SATURDAY KILLED 12 (4 SAUDIS, 8 RESIDENTS) AND INJURED 309; OPERATIONS TEMPORARILY SUSPENDED | "
   "REUTERS (VIA 964): THIRD ATTACK ON THE AIRPORT IN DAYS AMID HOUTHI MISSILE ESCALATION; ETIHAD + QATAR AIRWAYS CANCELLED RIYADH FLIGHTS | COALITION SPOKESMAN TURKI AL-MALIKI "
   "(VIA RUDAW): PROJECTILE FELL NEAR DAMMAM AIRPORT | US SECRETARY OF STATE RUBIO CONDEMNED HOUTHI ATTACKS | IRAQI GOVT SPOKESMAN SABAH AL-NUMAN: REJECTS TARGETING CIVILIANS, "
   "CALLS FOR A COMPREHENSIVE HALT TO MILITARY ACTION | PM AL-ZAIDI TOURS SAUDI ARABIA + KUWAIT WEDNESDAY (SHAFAQ)"))
p["beats"] = [
 beat("الرياض", "12 قتيلاً و309 مصابين بمطار الملك خالد",
  "هيئة الطيران المدني السعودي: هجوم السبت على مطار الملك خالد قتل 12 بينهم 4 سعوديين وأصاب 309، وعُلّقت العمليات مؤقتاً. روبيو أدان «هجمات الحوثيين» (رووداو، 964).",
  "12", "Killed in Saturday's attack on Riyadh's King Khalid International Airport, per Saudi civil aviation authority (via Rudaw / 964)", "قتيلاً — هيئة الطيران المدني السعودي",
  [("المصابون", "309"), ("سعوديون", "4"), ("المطار", "عمليات معلّقة")], 1, slug,
  ["12 قتيلاً و309 مصابين", "عمليات المطار معلّقة مؤقتاً", "روبيو يدين «هجمات الحوثيين»"], GEN),
 beat("الأجواء", "الهجوم الثالث خلال أيام.. والدمام أيضاً",
  "الهجوم الثالث على المطار خلال أيام (رويترز). وسقط مقذوف قرب مطار الدمام بحسب التحالف، والاتحاد والقطرية ألغتا رحلات إلى الرياض (رووداو، 964).",
  "3", "Attacks on Riyadh's airport within days, per Reuters (via 964) and Shafaq News", "هجمات على مطار الرياض خلال أيام — رويترز",
  [("الدمام", "مقذوف قرب المطار"), ("الاتحاد والقطرية", "رحلات ملغاة"), ("البديل", "جدة والدمام")], 2, slug,
  ["الهجوم الثالث خلال أيام", "مقذوف قرب مطار الدمام", "شركات طيران تلغي رحلاتها"], GEN),
 beat("بغداد", "بغداد تدين.. والزيدي إلى السعودية الأربعاء",
  "بيان صباح النعمان: العراق يرفض استهداف المدنيين ويدعو لوقف شامل للأعمال العسكرية. والزيدي يزور السعودية والكويت الأربعاء، ومصدر حكومي لشفق: أنبوب ينبع على الطاولة.",
  "14", "October (Wednesday): PM Ali al-Zaidi's Gulf tour to Saudi Arabia then Kuwait (Shafaq News)", "تشرين الأول — جولة الزيدي الخليجية (الأربعاء)",
  [("البيان", "وقف شامل"), ("الجولة", "السعودية والكويت"), ("الملف", "أنبوب ينبع")], 3, slug,
  ["بغداد: نرفض استهداف المدنيين", "الزيدي إلى الرياض الأربعاء", "أنبوب ينبع على الطاولة"], GEN),
]
p["arabicTicker"] = [
 "هيئة الطيران المدني السعودي: 12 قتيلاً و309 مصابين في هجوم مطار الملك خالد بالرياض",
 "رويترز: الهجوم الثالث على المطار خلال أيام.. والاتحاد والقطرية تلغيان رحلات",
 "التحالف: سقوط مقذوف قرب مطار الملك فهد بالدمام (رووداو)",
 "بغداد: نرفض استهداف المدنيين وندعو لوقف شامل للأعمال العسكرية",
 "عندك سفرة بالطيارة قريباً؟",
]
p["endQuestion"] = "عندك سفرة بالطيارة قريباً؟"
p["sources"] = [{"name": "رووداو", "domain": "rudawarabia.net"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "رويترز (عبر 964)", "domain": "reuters.com"}]
SLATE[slug] = (p, {
 "kicker": "عاجل", "hookHeadline": "مطار الرياض انضرب.. وبغداد تدين",
 "voText": ("هيئة الطيران المدني السعودي تقول إن هجوم السبت على مطار الملك خالد في الرياض قتل اثني عشر شخصاً، بينهم أربعة سعوديين، وأصاب ثلاثمئة وتسعة، "
            "وعلّق عمليات المطار مؤقتاً. وهو الهجوم الثالث على المطار خلال أيام بحسب رويترز، ووزير الخارجية الأميركي أدان هجمات الحوثيين. "
            "وفي بيان رسمي رفضت بغداد استهداف المدنيين ودعت إلى وقف شامل للأعمال العسكرية، فيما يزور رئيس الوزراء علي الزيدي السعودية ثم الكويت يوم الأربعاء. "
            "عندك سفرة بالطيارة قريباً؟"),
 "endQuestion": "عندك سفرة بالطيارة قريباً؟",
 "sourcesLine": "المصادر: رووداو · شبكة 964 · شفق نيوز · رويترز — 10 و11 تشرين الأول 2026",
 "statPops": [{"value": "12", "label": "قتيلاً في هجوم مطار الرياض — الطيران المدني السعودي", "matchWord": "اثني"},
              {"value": "309", "label": "مصاباً — الطيران المدني السعودي", "matchWord": "وتسعة"}],
}, """هجوم مطار الرياض — شنو صار، وبغداد شنو قالت؟

الضحايا، الطيران بالخليج، وموقف العراق قبل زيارة الزيدي للسعودية.. بالفيديو.

عندك سفرة بالطيارة قريباً؟

المصادر: رووداو، شبكة 964، شفق نيوز، رويترز (10 و11 تشرين الأول 2026)

#مطار_الرياض #السعودية #العراق #أخبار #photonectnews
@photonect.news
""")

# ═══════════ D · 22:30 · P1 corruption — Salahaddin ex-accounts director: 7 more properties ═══════════
slug = f"{D}-d-salahaddin-7-properties"
p = base(slug, "iraq_money", "B", "النزاهة", "7 عقارات جديدة لمدير حسابات موقوف",
  ("SALAHADDIN · OCT 11 | FEDERAL INTEGRITY COMMISSION (VIA SHAFAQ, 964): TEAM SEARCHED THE AL-ALAM HOME OF THE DETAINED FORMER HEAD OF ACCOUNTS AT SALAHADDIN GOVERNORATE; "
   "SEIZED FILES OF 3 HOUSES (2 IN HIS WIFE'S NAME, 1 HIS) + 4 PROPERTY DEEDS IN NAMES OF WIFE, HER BROTHER, A SON | LATE JULY: 2.5BN IQD SEIZED AT HIS HOME + 6 INVESTMENT "
   "PROPERTIES IN WIFE'S NAME | DETAINED UNDER ARTICLE 340 OVER A 425M IQD CHEQUE BASED ON FICTITIOUS DOCUMENTS | UNDER INVESTIGATION, NO CONVICTION"))
p["beats"] = [
 beat("الكشف", "النزاهة: 7 عقارات جديدة باسم الزوجة والأقارب",
  "هيئة النزاهة: فريق فتّش دار مدير الحسابات السابق في ديوان صلاح الدين الموقوف بقضاء العلم، وضبط أضابير 3 دور، اثنتان باسم زوجته (شفق نيوز، 964).",
  "7", "New properties uncovered, per the Federal Integrity Commission (via Shafaq / 964)", "عقارات جديدة — هيئة النزاهة",
  [("دور سكنية", "3"), ("سندات عقارية", "4"), ("المكان", "قضاء العلم")], 1, slug,
  ["7 عقارات جديدة", "تفتيش دار في قضاء العلم", "داران باسم الزوجة"], GEN),
 beat("السندات", "4 سندات بأسماء الزوجة وشقيقها والابن",
  "وضبط أربعة سندات عقارية بأسماء الزوجة وشقيقها وأحد الأبناء. وفي تموز ضبطت الهيئة 2.5 مليار دينار بمنزله وستة عقارات استثمارية باسم زوجته.",
  "2.5", "Billion IQD seized at his home in late July, per the Integrity Commission", "مليار دينار ضُبطت بمنزله في تموز — النزاهة",
  [("تموز", "2.5 مليار دينار"), ("عقارات استثمارية", "6"), ("المجموع", "13 (محتسب)")], 2, slug,
  ["4 سندات بأسماء العائلة", "تموز: 2.5 مليار بالمنزل", "و6 عقارات استثمارية"], GEN),
 beat("التهمة", "صكّ بـ425 مليون دينار على أوليات وهمية",
  "الهيئة تقول إن المتهم موقوف وفق المادة 340 عقوبات بتهمة تنظيم وصرف صكّ بـ425 مليون دينار استناداً إلى أوليات وهمية. القضية بالتحقيق ولم تصدر إدانة.",
  "425M", "IQD cheque he is accused of issuing on fictitious documents, per the Integrity Commission", "دينار قيمة الصك — بحسب النزاهة",
  [("المادة", "340 عقوبات"), ("الحالة", "موقوف"), ("الحكم", "لا إدانة بعد")], 3, slug,
  ["صك بـ425 مليون دينار", "على أوليات وهمية", "القضية بالتحقيق ولا إدانة"], GEN),
]
p["arabicTicker"] = [
 "النزاهة: ضبط 7 عقارات جديدة باسم زوجة وأقارب مدير حسابات صلاح الدين السابق الموقوف (شفق نيوز، 964)",
 "أضابير 3 دور في مجمعات سكنية و4 سندات عقارية بأسماء الزوجة وشقيقها وأحد الأبناء",
 "تموز الماضي: ضبط 2.5 مليار دينار في منزله و6 عقارات استثمارية باسم زوجته",
 "التهمة بحسب الهيئة: صك بـ425 مليون دينار على أوليات وهمية — ولم تصدر إدانة",
 "بلّغت عن فساد قبل؟",
]
p["endQuestion"] = "بلّغت عن فساد قبل؟"
p["sources"] = [{"name": "هيئة النزاهة الاتحادية", "domain": "nazaha.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = (p, {
 "kicker": "النزاهة", "hookHeadline": "مليارا دينار بالبيت.. و7 عقارات جديدة",
 "voText": ("هيئة النزاهة تعلن ضبط سبعة عقارات جديدة مرتبطة بمدير قسم الحسابات السابق في ديوان محافظة صلاح الدين، الموقوف على ذمة التحقيق. "
            "فريق الهيئة فتّش داره في قضاء العلم، وضبط أضابير ثلاث دور، اثنتان منها باسم زوجته، وأربعة سندات بأسماء زوجته وشقيقها وأحد أبنائه. "
            "وكانت الهيئة قد ضبطت في تموز ملياري وخمسمئة مليون دينار في منزله. وتقول الهيئة إنه موقوف بتهمة صرف صك بأربعمئة وخمسة وعشرين مليون دينار "
            "استناداً إلى أوليات وهمية، والقضية ما زالت بالتحقيق ولم تصدر إدانة. بلّغت عن فساد قبل؟"),
 "endQuestion": "بلّغت عن فساد قبل؟",
 "sourcesLine": "المصادر: هيئة النزاهة عبر شفق نيوز · شبكة 964 — 11 تشرين الأول 2026",
 "statPops": [{"value": "7", "label": "عقارات جديدة — هيئة النزاهة", "matchWord": "سبعة"},
              {"value": "2.5 مليار", "label": "دينار ضُبطت في منزله — تموز", "matchWord": "ملياري"}],
}, """هيئة النزاهة صلاح الدين — 7 عقارات جديدة لمدير حسابات موقوف

بيوت وسندات بأسماء العائلة، ومليارات ضُبطت قبل.. والقضية وين وصلت؟ بالفيديو.

بلّغت عن فساد قبل؟

المصادر: هيئة النزاهة الاتحادية عبر شفق نيوز وشبكة 964 (11 تشرين الأول 2026)

#هيئة_النزاهة #صلاح_الدين #الفساد #العراق #photonectnews
@photonect.news
""")

# ═══════════ E · 23:45 · P1 services — a third of Iraqis without waste collection (V10.1 CONTROL) ═══════════
slug = f"{D}-e-waste-third-uncollected"
p = base(slug, "iraq_services", "C", "الخدمات", "ثلث العراقيين بلا خدمة جمع نفايات",
  ("IRAQ · OCT 11 | CENTRAL STATISTICS ORGANISATION ENVIRONMENT REPORT (OBTAINED BY RUDAW): WASTE COLLECTION COVERS 68.6% OF IRAQ'S POPULATION, 31.4% WITHOUT | "
   "CITIES 93.5% VS VILLAGES 16% | PROVINCE CENTRES: KIRKUK 100%, DHI QAR 99.2%, BAGHDAD 98.8% ... DIWANIYA LAST AT 76.6% | ONE OPERATING RECYCLING PLANT (YUSUFIYA) | "
   "55 OF 60 TRANSFER STATIONS LACK ENVIRONMENTAL APPROVAL | DIWANIYA COUNCIL'S ZAINAB AL-ABIDI: NO STANDARD LANDFILL, DUMPS 30-35 KM AWAY"))
p["beats"] = [
 beat("الصورة", "31.4% من السكان بلا جمع نفايات",
  "تقرير الجهاز المركزي للإحصاء (حصلت عليه رووداو): خدمة جمع النفايات تغطي 68.6% من سكان العراق، أي أن 31.4%، قرابة الثلث، محرومون منها.",
  "31.4%", "Share of Iraq's population without waste collection, per the Central Statistics Organisation (via Rudaw)", "من السكان بلا خدمة جمع نفايات",
  [("التغطية", "68.6%"), ("المحرومون", "31.4%"), ("المصدر", "الإحصاء")], 1, slug,
  ["68.6% فقط مشمولون", "31.4% بلا خدمة", "قرابة الثلث"], GEN),
 beat("القرى", "المدن 93.5%.. والقرى 16% فقط",
  "التغطية 93.5% في المدن مقابل 16% في القرى، أي أن 84% من سكان القرى بلا خدمة. ومعمل تدوير واحد فقط يعمل فعلياً، في اليوسفية ببغداد.",
  "16%", "Waste-collection coverage in Iraq's villages vs 93.5% in cities (Central Statistics Organisation via Rudaw)", "تغطية جمع النفايات في القرى",
  [("المدن", "93.5%"), ("القرى", "16%"), ("معامل التدوير", "1 يعمل")], 2, slug,
  ["المدن 93.5%", "القرى 16% فقط", "معمل تدوير واحد يعمل"], GEN),
 beat("المحافظات", "كركوك 100%.. والديوانية الأخيرة 76.6%",
  "كركوك تصدرت المراكز بـ100% بعقد مع شركتين خاصتين، والديوانية أخيرة بـ76.6%. زينب العابدي من مجلسها: لا موقع طمر نموذجي، والمكبات تبعد 30 إلى 35 كم.",
  "76.6%", "Waste-collection coverage in Diwaniya's city centre, last among province centres (CSO via Rudaw)", "تغطية مركز الديوانية — الأخيرة",
  [("كركوك", "100%"), ("ذي قار", "99.2%"), ("الديوانية", "76.6%")], 3, slug,
  ["كركوك 100%", "الديوانية الأخيرة 76.6%", "المكبات تبعد 30–35 كم"], GEN),
]
p["arabicTicker"] = [
 "الجهاز المركزي للإحصاء: جمع النفايات يغطي 68.6% من سكان العراق.. و31.4% بلا خدمة (رووداو)",
 "المدن 93.5% مقابل 16% فقط في القرى",
 "كركوك أولاً بـ100%.. والديوانية أخيرة بـ76.6%",
 "55 من أصل 60 محطة وسيطة لنقل النفايات بلا موافقات بيئية",
 "تجي سيارة النفايات لشارعكم؟",
]
p["endQuestion"] = "تجي سيارة النفايات لشارعكم؟"
p["sources"] = [{"name": "الجهاز المركزي للإحصاء (عبر رووداو)", "domain": "rudawarabia.net"}, {"name": "رووداو", "domain": "rudawarabia.net"},
                {"name": "بلدية كركوك", "domain": "rudawarabia.net"}, {"name": "مجلس محافظة الديوانية", "domain": "rudawarabia.net"}]
SLATE[slug] = (p, None, """النفايات في العراق — منو محروم من الخدمة؟

مدن، قرى، ومحافظة أولى وأخرى أخيرة.. الأرقام بالفيديو.

تجي سيارة النفايات لشارعكم؟

المصادر: الجهاز المركزي للإحصاء عبر رووداو (11 تشرين الأول 2026)

#النفايات #الخدمات #الديوانية #العراق #photonectnews
@photonect.news
""")

def main():
    for slug, (props, brief, caption) in SLATE.items():
        d = POSTS / slug
        (d / ".meta").mkdir(parents=True, exist_ok=True)
        (d / ".meta" / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / "caption.txt").write_text(caption, encoding="utf-8")
        bp = d / ".meta" / "v11-brief.json"
        if brief:
            b = {"slug": slug, "kicker": brief["kicker"], "hookHeadline": brief["hookHeadline"], "voText": brief["voText"],
                 "endQuestion": brief["endQuestion"], "sourcesLine": brief["sourcesLine"],
                 "images": [f"{IMG}/{slug}/hero.jpg"] + [f"{IMG}/{slug}/broll_{i}.jpg" for i in (1, 2, 3)],
                 "audioBed": props["audioBed"], "statPops": brief["statPops"]}
            bp.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
        elif bp.exists():
            bp.unlink()
        print(f"{slug}: props + caption" + (" + v11-brief" if brief else "  (V10.1 CONTROL)"))


if __name__ == "__main__":
    main()
