#!/usr/bin/env python3
"""Author the 2026-10-03 slate: props.json + caption.txt (+ v11-brief.json on a, b, c, d; e = V10.1 control).

Every figure traces to a named source (Baghdad Today, Al-Rasheed, Shafaq, Ultra Iraq, INA, NINA, Al-Fallujah TV). Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + two gate passes (apply_gate*_2026_10_03.py)
then edited the files on disk — do NOT re-run this script, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_10_03.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-03"
DATE_LABEL = "OCT 03 • 2026"
AR_DATE = "3 تشرين الأول 2026"
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




# ═══════════ A · 18:00 · P1 electricity (LEAD) — Baghdad generator ampere tariff for October ═══════════
slug = f"{D}-a-ampere-15000-october"
p = base(slug, "iraq_services", "A", "الكهرباء", "أمبير المولدة بتشرين: 15 ألف للذهبي.. و10 لليلي",
  ("BAGHDAD · OCT 2 | BAGHDAD PROVINCIAL COUNCIL SETS THE OCTOBER 2026 GENERATOR TARIFF: 15,000 IQD PER AMP FOR THE 24-HOUR "
   "'GOLDEN' LINE (ALTERNATING WITH THE NATIONAL GRID), 10,000 IQD FOR THE NIGHT LINE (12 NOON-6 AM), WITH CONTROLS AGAINST "
   "EXTRA CHARGES (GOVERNORATE DOCUMENT VIA BAGHDAD TODAY; AL-RASHEED TV) | SEPTEMBER 2026: 15,000 GOLDEN / 9,000 NIGHT "
   "(AL-FALLUJAH TV, AL-RASHEED) | OCTOBER 2025: 9,000 GOLDEN / 7,000 NIGHT (NINA)"))
p["beats"] = [
 beat("التسعيرة", "15 ألف للأمبير الذهبي",
  "مجلس محافظة بغداد حدّد تسعيرة تشرين الأول: 15 ألف دينار للأمبير الذهبي بالتناوب مع الوطنية، و10 آلاف لليلي من 12 ظهراً حتى 6 صباحاً.",
  "15,000", "IQD per amp, 24h 'golden' line, October 2026 (Baghdad council document via Baghdad Today)",
  "دينار للأمبير الذهبي — تشرين الأول (مجلس بغداد)",
  [("الليلي", "10,000 دينار"), ("ساعات الليلي", "12 ظهراً - 6 صباحاً"), ("الذهبي", "24 ساعة بالتناوب")], 1, slug,
  ["تسعيرة تشرين", "15 ألف للذهبي", "10 آلاف لليلي"], STOCK),
 beat("مقارنة بأيلول", "الليلي زاد ألف دينار عن أيلول",
  "تسعيرة أيلول كانت 15 ألفاً للذهبي و9 آلاف لليلي (قناة الفلوجة، الرشيد). يعني الذهبي ثابت، والليلي زاد ألف دينار.",
  "1,000", "IQD rise in the night-line amp price vs September (computed from Al-Fallujah TV / Al-Rasheed)",
  "دينار زيادة الأمبير الليلي عن أيلول (محتسب)",
  [("ليلي أيلول", "9,000"), ("ليلي تشرين", "10,000"), ("الذهبي", "ثابت 15,000")], 2, slug,
  ["أيلول 9 آلاف", "تشرين 10 آلاف", "الذهبي ثابت"], STOCK),
 beat("قبل سنة", "تشرين الماضي: الذهبي 9 آلاف",
  "في تشرين الأول 2025 حدّد مجلس بغداد الأمبير الذهبي بـ9 آلاف دينار والليلي بـ7 آلاف (وكالة نينا). اليوم الذهبي أغلى بـ6 آلاف.",
  "6,000", "IQD more per golden amp than October 2025 (computed: 15,000 vs 9,000 per NINA)",
  "دينار زيادة الأمبير الذهبي عن العام الماضي (محتسب)",
  [("ذهبي 2025", "9,000"), ("ليلي 2025", "7,000"), ("5 أمبير ذهبي اليوم", "75,000 (محتسب)")], 3, slug,
  ["قبل سنة", "9 آلاف بس", "اليوم 15 ألف"], STOCK),
]
p["arabicTicker"] = [
 "مجلس محافظة بغداد: تسعيرة تشرين الأول 15 ألف دينار للأمبير الذهبي و10 آلاف لليلي (وثيقة عبر بغداد اليوم)",
 "التشغيل الليلي من الساعة 12 ظهراً حتى 6 صباحاً، والذهبي 24 ساعة بالتناوب مع الكهرباء الوطنية",
 "تسعيرة أيلول: 15 ألفاً للذهبي و9 آلاف لليلي (قناة الفلوجة، الرشيد)",
 "تشرين الأول 2025: 9 آلاف للذهبي و7 آلاف لليلي (وكالة نينا)",
 "شكد تدفع للمولدة هالشهر؟"]
p["endQuestion"] = "شكد تدفع للمولدة هالشهر؟"
p["sources"] = [{"name": "بغداد اليوم", "domain": "baghdadtoday.news"}, {"name": "قناة الرشيد", "domain": "alrasheedmedia.com"}, {"name": "قناة الفلوجة", "domain": "alfallujah.tv"}, {"name": "وكالة نينا", "domain": "ninanews.com"}]
SLATE[slug] = {"props": p, "caption": """تسعيرة أمبير المولدات في بغداد لشهر تشرين الأول — شكد صارت؟

الليلي زاد عن أيلول.. وقارنّاها بالسنة الماضية بالفيديو.

شكد تدفع للمولدة هالشهر؟

المصادر: مجلس محافظة بغداد عبر بغداد اليوم، الرشيد، الفلوجة، نينا

#المولدات #الأمبير #بغداد #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "المولدات", "hookHeadline": "أمبيرك بتشرين: شكد صار؟",
  "voText": "حدّد مجلس محافظة بغداد تسعيرة أمبير المولدات لشهر تشرين الأول: خمسة عشر ألف دينار للأمبير الذهبي على مدار الساعة بالتناوب مع الكهرباء الوطنية، وعشرة آلاف دينار للتشغيل الليلي من الظهر حتى السادسة صباحاً، بحسب وثيقة نشرتها بغداد اليوم. ووضع المجلس ضوابط لمنع استيفاء أي مبالغ إضافية من المواطنين. وكان سعر الليلي في أيلول تسعة آلاف دينار. وفي تشرين الأول من العام الماضي، حُدّد الذهبي بتسعة آلاف دينار فقط، بحسب وكالة نينا. شكد تدفع للمولدة هالشهر؟",
  "endQuestion": "شكد تدفع للمولدة هالشهر؟",
  "sourcesLine": "المصادر: مجلس محافظة بغداد عبر بغداد اليوم · الرشيد · الفلوجة · نينا",
  "statPops": [{"value": "15,000", "label": "دينار للأمبير الذهبي — تشرين الأول", "matchWord": "خمسة"},
               {"value": "9,000", "label": "الذهبي قبل عام (نينا)", "matchWord": "فقط"}]}}


# ═══════════ B · 19:45 · P1 dollar anchor — flat at 157,300; Erbil vs Baghdad shops; toman next door ═══════════
slug = f"{D}-b-dollar-157300-flat"
p = base(slug, "iraq_money", "B", "سعر الدولار", "الدولار واقف على 157,300.. والتومان لوين؟",
  ("BAGHDAD/ERBIL · OCT 3 | SHAFAQ NEWS: KIFAH & HARITHIYA OPENED THE WEEK AT 157,250 IQD PER $100 AND CLOSED SATURDAY AT "
   "157,300 — THE SAME AS THURSDAY'S CLOSE (SHAFAQ, OCT 1) | BAGHDAD EXCHANGE SHOPS: SELL 157,750 / BUY 156,750 | ERBIL "
   "SHOPS AT CLOSE: SELL 157,550 / BUY 157,500 | IRAN: DOLLAR SELLS AT ~265,050 TOMAN, UP 1,150 (0.44%) FROM 263,900 "
   "(IRANIAN MARKET DATA VIA SHAFAQ NEWS)"))
p["beats"] = [
 beat("إغلاق السبت", "157,300.. نفس إغلاق الخميس",
  "شفق نيوز: بورصتا الكفاح والحارثية افتتحتا الأسبوع على 157,250 وأغلقتا السبت على 157,300 لكل 100 دولار، وهو سعر إغلاق الخميس نفسه.",
  "157,300", "IQD per $100, Kifah & Harithiya, Saturday close — unchanged from Thursday close (Shafaq News)",
  "دينار لكل 100 دولار — إغلاق السبت (شفق نيوز)",
  [("افتتاح السبت", "157,250"), ("إغلاق الخميس", "157,300"), ("التغيّر", "صفر (محتسب)")], 1, slug,
  ["إغلاق السبت", "157,300", "مثل الخميس"], STOCK),
 beat("محال الصيرفة", "بالمحلات: أربيل أرخص من بغداد",
  "عند الإغلاق: البيع بمحال صيرفة بغداد 157,750 والشراء 156,750، وفي أربيل البيع 157,550 والشراء 157,500 (شفق نيوز).",
  "157,550", "IQD per $100, Erbil exchange-shop selling price at Saturday close (Shafaq News)",
  "دينار سعر البيع بمحال أربيل (شفق نيوز)",
  [("بيع بغداد", "157,750"), ("بيع أربيل", "157,550"), ("الفرق", "200 دينار (محتسب)")], 2, slug,
  ["محال بغداد", "محال أربيل", "فرق 200 دينار"], STOCK),
 beat("الجارة إيران", "التومان: 265 ألف للدولار",
  "في إيران بلغ سعر بيع الدولار نحو 265,050 توماناً، بارتفاع 1,150 توماناً (0.44%) عن اليوم السابق، وفق بيانات السوق الإيرانية عبر شفق نيوز.",
  "265,050", "Toman per US dollar, Iranian free-market selling price (Iranian market data via Shafaq News)",
  "تومان للدولار في السوق الإيرانية (شفق نيوز)",
  [("أمس", "263,900"), ("الزيادة", "1,150 تومان"), ("النسبة", "0.44%")], 3, slug,
  ["التومان الإيراني", "265 ألف", "مستوى جديد"], "صورة أرشيفية — الريال الإيراني"),
]
p["arabicTicker"] = [
 "شفق نيوز: الدولار في بورصتي الكفاح والحارثية 157,300 دينار لكل 100 دولار عند إغلاق السبت، بعد 157,250 صباحاً",
 "إغلاق الخميس كان 157,300 أيضاً — لا تغيّر (محتسب)",
 "محال صيرفة بغداد: البيع 157,750 والشراء 156,750 — أربيل: البيع 157,550 والشراء 157,500",
 "إيران: الدولار بنحو 265,050 توماناً، بارتفاع 0.44% عن اليوم السابق",
 "بيش صرفت الدولار آخر مرة؟"]
p["endQuestion"] = "بيش صرفت الدولار آخر مرة؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — بغداد وأربيل بإغلاق السبت

وين أرخص تصرف؟ والتومان الإيراني لوين وصل؟ بالفيديو.

بيش صرفت الدولار آخر مرة؟

المصادر: شفق نيوز (1 و3 تشرين الأول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #أربيل #photonectnews
@photonect.news""",
 "brief": {"kicker": "سعر الدولار", "hookHeadline": "الدولار واقف.. وين أرخص تصرف؟",
  "voText": "افتتحت بورصتا الكفاح والحارثية في بغداد تعاملات الأسبوع على مئة وسبعة وخمسين ألفاً ومئتين وخمسين ديناراً لكل مئة دولار، ثم أغلقت السبت على مئة وسبعة وخمسين ألفاً وثلاثمئة، وهو سعر إغلاق الخميس نفسه، بحسب شفق نيوز. وفي محال الصيرفة، بلغ سعر البيع في بغداد مئة وسبعة وخمسين ألفاً وسبعمئة وخمسين ديناراً، مقابل مئة وسبعة وخمسين ألفاً وخمسمئة وخمسين في أربيل. أما في إيران المجاورة، فتراجع التومان إلى نحو مئتين وخمسة وستين ألفاً للدولار. بيش صرفت الدولار آخر مرة؟",
  "endQuestion": "بيش صرفت الدولار آخر مرة؟",
  "sourcesLine": "المصادر: شفق نيوز — 3 تشرين الأول 2026",
  "statPops": [{"value": "157,300", "label": "إغلاق السبت — مثل الخميس", "matchWord": "أغلقت"},
               {"value": "265,050", "label": "تومان للدولار في إيران", "matchWord": "التومان"}]}}


# ═══════════ C · 21:15 · P2 Iraq–Turkey — extend Kirkuk–Ceyhan to Basra as a Hormuz bypass ═══════════
slug = f"{D}-c-ceyhan-basra-pipeline"
p = base(slug, "mena_geo", "A", "نفط العراق", "خط جيهان للبصرة؟ تركيا تطرح بديل هرمز",
  ("ANKARA · OCT 2-3 | IRAQI OIL MINISTER BASIM MOHAMMED KHUDAIR AL-ABADI AND TURKISH ENERGY MINISTER ALPARSLAN BAYRAKTAR "
   "OPENED TALKS ON AN OIL-GAS FRAMEWORK AGREEMENT (IRAQI OIL MINISTRY VIA SHAFAQ NEWS, ULTRA IRAQ) | BAYRAKTAR: EXTENDING "
   "THE KIRKUK-CEYHAN PIPELINE TO BASRA AND RAISING ITS CAPACITY IS STRATEGIC, A STRONG ALTERNATIVE TO THE GULF AND THE "
   "STRAIT OF HORMUZ (ULTRA IRAQ, AL-RASHEED) | PIPELINE ~970 KM; AUGUST ONE-YEAR DEAL TO MOVE 750,000 BPD; BAYRAKTAR CITES "
   "PM ALI AL-ZAIDI'S ONE-MILLION-BARREL SUPPLY TARGET (ULTRA IRAQ)"))
p["beats"] = [
 beat("المقترح", "تركيا: مدّوا خط جيهان للبصرة",
  "وزير الطاقة التركي ألب أرسلان بيرقدار: تمديد خط كركوك–جيهان إلى البصرة وزيادة طاقته يوفّران بديلاً قوياً للخليج ومضيق هرمز.",
  "970", "Km — approximate length of the Kirkuk–Ceyhan pipeline today (Ultra Iraq)",
  "كم طول خط كركوك–جيهان حالياً (الترا عراق)",
  [("البداية", "كركوك"), ("النهاية", "ميناء جيهان"), ("المقترح", "حتى البصرة")], 1, slug,
  ["خط كركوك–جيهان", "يمتد للبصرة؟", "بديل هرمز"], STOCK),
 beat("المفاوضات", "مفاوضات أنقرة بدأت الجمعة",
  "وزارة النفط: الوزير باسم محمد خضير العبادي ترأس وفد العراق في افتتاح مفاوضات الاتفاقية الإطارية للنفط والغاز مع تركيا في أنقرة.",
  "2", "October — framework-agreement talks opened in Ankara (Iraqi Oil Ministry via Shafaq News)",
  "تشرين الأول — افتتاح المفاوضات في أنقرة (وزارة النفط)",
  [("الوفد العراقي", "باسم العبادي"), ("الجانب التركي", "ألب أرسلان بيرقدار"), ("الملفات", "نفط وغاز وبتروكيماويات")], 2, slug,
  ["أنقرة", "وزير النفط", "اتفاقية إطارية"], STOCK),
 beat("الأرقام", "750 ألف برميل.. والهدف مليون",
  "اتفاق آب لمدة عام يقضي بنقل 750 ألف برميل يومياً (الترا عراق). وبيرقدار تحدث عن هدف توريد مليون برميل أشار إليه رئيس الوزراء علي الزيدي.",
  "750,000", "Barrels per day under the one-year August Iraq–Turkey transport deal (Ultra Iraq)",
  "برميل يومياً — اتفاق آب لمدة عام (الترا عراق)",
  [("مدة اتفاق آب", "سنة"), ("الهدف", "مليون برميل"), ("الجديد", "اتفاقية أشمل")], 3, slug,
  ["750 ألف برميل", "الهدف مليون", "اتفاقية أطول"], STOCK),
]
p["arabicTicker"] = [
 "وزارة النفط: انطلاق مفاوضات الاتفاقية الإطارية للنفط والغاز بين العراق وتركيا في أنقرة (الجمعة 2 تشرين الأول)",
 "بيرقدار: تمديد خط كركوك–جيهان إلى البصرة وزيادة طاقته بديل قوي للخليج ومضيق هرمز",
 "الترا عراق: طول الخط نحو 970 كم — واتفاق آب لعام واحد لنقل 750 ألف برميل يومياً",
 "بيرقدار: هدف توريد مليون برميل أشار إليه رئيس الوزراء علي الزيدي",
 "سمعت بخط كركوك–جيهان قبل؟"]
p["endQuestion"] = "سمعت بخط كركوك–جيهان قبل؟"
p["sources"] = [{"name": "وزارة النفط", "domain": "oil.gov.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "الترا عراق", "domain": "ultrairaq.ultrasawt.com"}, {"name": "قناة الرشيد", "domain": "alrasheedmedia.com"}]
SLATE[slug] = {"props": p, "caption": """خط نفط كركوك جيهان إلى البصرة — تركيا تطرح بديلاً لهرمز

شنو اتفقوا بأنقرة؟ الأرقام بالفيديو.

سمعت بخط كركوك–جيهان قبل؟

المصادر: وزارة النفط عبر شفق نيوز، الترا عراق، الرشيد (2-3 تشرين الأول 2026)

#نفط_العراق #جيهان #البصرة #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "نفط العراق", "hookHeadline": "نفط البصرة يطلع من تركيا؟",
  "voText": "في أنقرة، بدأ العراق وتركيا يوم الجمعة مفاوضات اتفاقية إطارية للنفط والغاز، بحسب وزارة النفط العراقية. وقال وزير الطاقة التركي ألب أرسلان بيرقدار إن تمديد خط كركوك جيهان إلى البصرة وزيادة طاقته يوفّران بديلاً قوياً لمضيق هرمز. ويبلغ طول الخط حالياً نحو تسعمئة وسبعين كيلومتراً، ويقضي اتفاق وُقّع في آب بنقل سبعمئة وخمسين ألف برميل يومياً، فيما تحدث بيرقدار عن هدف مليون برميل أشار إليه رئيس الوزراء علي الزيدي. سمعت بخط كركوك جيهان قبل؟",
  "endQuestion": "سمعت بخط كركوك جيهان قبل؟",
  "sourcesLine": "المصادر: وزارة النفط عبر شفق نيوز · الترا عراق · الرشيد",
  "statPops": [{"value": "970 كم", "label": "طول خط كركوك–جيهان", "matchWord": "كيلومتراً"},
               {"value": "750,000", "label": "برميل يومياً — اتفاق آب", "matchWord": "وخمسين"}]}}


# ═══════════ D · 22:30 · P1 accountability — MoI September tally (V10.1 CONTROL) ═══════════
slug = f"{D}-d-moi-september-308"
p = base(slug, "iraq_corruption", "B", "حصيلة أيلول", "مليون دولار و308 متهمين.. حصيلة شهر واحد",
  ("BAGHDAD · OCT 3 | INTERIOR MINISTRY MEDIA CHIEF MAJ. GEN. MIQDAD MIRI: THE RAPID RESPONSE DIVISION ARRESTED 308 SUSPECTS "
   "IN SEPTEMBER — 31 IN INTEGRITY (CORRUPTION) CASES, 55 DRUGS, 16 UNDER ART. 4 TERRORISM, 206 ON WARRANTS — IN 124 "
   "OPERATIONS | SEIZED: $1,000,000 + 6,047,000 IQD, 21 WEAPONS, 1,425 G CRYSTAL METH, 305 G HASHISH, 92 PILLS (SHAFAQ NEWS, "
   "INA, 964)"))
p["beats"] = [
 beat("الاعتقالات", "308 متهمين بشهر واحد",
  "اللواء مقداد ميري: قيادة فرقة الرد السريع قبضت خلال أيلول على 308 متهمين، بينهم 31 بقضايا نزاهة و55 بقضايا مخدرات.",
  "308", "Suspects arrested by the Rapid Response Division in September (Interior Ministry via Shafaq News)",
  "متهماً قُبض عليهم خلال أيلول (وزارة الداخلية)",
  [("قضايا نزاهة", "31"), ("قضايا مخدرات", "55"), ("مذكرات قبض", "206")], 1, slug,
  ["308 متهمين", "31 بقضايا نزاهة", "55 مخدرات"], STOCK),
 beat("المضبوطات", "مليون دولار مصادرة",
  "حسب بيان الداخلية: صودر 1,000,000 دولار و6,047,000 دينار، إضافة إلى 21 قطعة سلاح و18 هاتفاً محمولاً.",
  "1,000,000", "US dollars seized in September operations (Interior Ministry via Shafaq News)",
  "دولار مصادرة خلال أيلول (وزارة الداخلية)",
  [("بالدينار", "6,047,000"), ("أسلحة", "21 قطعة"), ("هواتف", "18")], 2, slug,
  ["مليون دولار", "6 ملايين دينار", "21 قطعة سلاح"], STOCK),
 beat("المخدرات", "كيلو و425 غراماً كريستال",
  "وضُبط 1,425 غراماً من الكريستال و305 غرامات من الحشيشة و92 حبة مخدرة، عبر 124 واجباً أمنياً خلال الشهر.",
  "1,425", "Grams of crystal meth seized in September (Interior Ministry via Shafaq News)",
  "غراماً من الكريستال المضبوط (وزارة الداخلية)",
  [("حشيشة", "305 غرامات"), ("حبوب مخدرة", "92"), ("واجبات أمنية", "124")], 3, slug,
  ["1,425 غرام كريستال", "305 حشيشة", "124 واجباً"], STOCK),
]
p["arabicTicker"] = [
 "وزارة الداخلية: فرقة الرد السريع تقبض على 308 متهمين خلال أيلول (شفق نيوز، واع)",
 "بينهم 31 بقضايا نزاهة و55 بقضايا مخدرات و16 وفق المادة 4 إرهاب و206 بمذكرات قبض",
 "المضبوطات: 1,000,000 دولار و6,047,000 دينار و21 قطعة سلاح",
 "ضبط 1,425 غراماً من الكريستال و305 غرامات من الحشيشة و92 حبة مخدرة",
 "مرّيت بسيطرة اليوم؟"]
p["endQuestion"] = "مرّيت بسيطرة اليوم؟"
p["sources"] = [{"name": "وزارة الداخلية", "domain": "moi.gov.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "واع", "domain": "ina.iq"}, {"name": "964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """حصيلة وزارة الداخلية لشهر أيلول — مليون دولار و308 متهمين

31 منهم بقضايا نزاهة.. التفاصيل بالفيديو.

مرّيت بسيطرة اليوم؟

المصادر: وزارة الداخلية عبر شفق نيوز، واع، 964 (3 تشرين الأول 2026)

#وزارة_الداخلية #النزاهة #العراق #بغداد #photonectnews
@photonect.news""",
 "brief": None}


# ═══════════ E · 23:45 · P3 health — Kirkuk: 150+ diarrhoea/vomiting cases, drinking water tested ═══════════
slug = f"{D}-e-kirkuk-water-150-cases"
p = base(slug, "region_health", "C", "صحة كركوك", "150 إصابة إسهال بيومين.. والفحص على مي الشرب",
  ("KIRKUK · OCT 3 | JASSIM YASSIN HUSSEIN, HEAD OF KIRKUK HEALTH'S SECOND SECTOR: AL-RIYADH SUBDISTRICT (HAWIJA) RECORDED "
   "MORE THAN 150 CASES OF DIARRHOEA AND VOMITING ON TUESDAY-WEDNESDAY, ~70 ON THE FIRST DAY | TEAMS VISITED THE AL-RIYADH "
   "WATER PROJECT, TOOK SAMPLES FOR LAB TESTS AND DISTRIBUTED CHLORINE TABLETS; RESULTS PENDING | HE SAYS MOST KIRKUK WATER "
   "DIRECTORATE PROJECTS LACK REQUIRED STERILISATION CONDITIONS (SHAFAQ NEWS)"))
p["beats"] = [
 beat("الإصابات", "أكثر من 150 حالة خلال يومين",
  "جاسم ياسين حسين من صحة كركوك لشفق نيوز: ناحية الرياض سجلت أكثر من 150 حالة إسهال وتقيؤ يومي الثلاثاء والأربعاء الماضيين.",
  "150", "Diarrhoea and vomiting cases in al-Riyadh, Kirkuk, over two days (Kirkuk Health via Shafaq News)",
  "حالة إسهال وتقيؤ خلال يومين (صحة كركوك)",
  [("اليوم الأول", "نحو 70"), ("الناحية", "الرياض"), ("القضاء", "الحويجة")], 1, slug,
  ["ناحية الرياض", "150 إصابة", "بيومين"], STOCK),
 beat("الفحص", "عينات من مي الشرب.. والنتائج بعدها",
  "فرق الأمراض الانتقالية زارت مشروع ماء الرياض، وأخذت نماذج للفحص المختبري ووزعت حبوب الكلور على المواطنين، بانتظار النتائج لتحديد السبب.",
  "70", "Cases received by the health centre on the first day (Kirkuk Health via Shafaq News)",
  "حالة باليوم الأول في المركز الصحي (صحة كركوك)",
  [("العينات", "للمختبر"), ("حبوب الكلور", "توزيع"), ("السبب", "بانتظار النتائج")], 2, slug,
  ["مشروع ماء الرياض", "عينات للمختبر", "حبوب كلور"], STOCK),
 beat("التعقيم", "مشاريع ماء بلا شروط التعقيم",
  "حسب المسؤول نفسه: أغلب مشاريع دائرة ماء كركوك لا تتوفر فيها شروط التعقيم الصحية، وهذا يتطلب تعزيز التعقيم والرقابة على مصادر الشرب.",
  "2", "Days over which the 150+ cases were recorded — Tuesday and Wednesday (Kirkuk Health via Shafaq News)",
  "يومان سُجّلت خلالهما الإصابات (صحة كركوك)",
  [("المشاريع", "أغلبها بلا شروط التعقيم"), ("المطلوب", "تعزيز الرقابة"), ("المصدر", "صحة كركوك")], 3, slug,
  ["شروط التعقيم", "مشاريع الماء", "تعزيز الرقابة"], "صورة أرشيفية — كركوك"),
]
p["arabicTicker"] = [
 "صحة كركوك: أكثر من 150 حالة إسهال وتقيؤ في ناحية الرياض خلال يومي الثلاثاء والأربعاء (شفق نيوز)",
 "المركز الصحي استقبل نحو 70 حالة في اليوم الأول",
 "الفرق الصحية أخذت عينات من مشروع ماء الرياض ووزعت حبوب الكلور — النتائج بانتظار المختبر",
 "المسؤول الصحي: أغلب مشاريع ماء كركوك لا تتوفر فيها شروط التعقيم",
 "تشرب مي الحنفية لو تشتري؟"]
p["endQuestion"] = "تشرب مي الحنفية لو تشتري؟"
p["sources"] = [{"name": "دائرة صحة كركوك", "domain": "moh.gov.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """إسهال وتقيؤ في كركوك — 150 إصابة والفحص على مياه الشرب

شنو قالت صحة كركوك عن مشاريع الماء؟ بالفيديو.

تشرب مي الحنفية لو تشتري؟

المصادر: دائرة صحة كركوك عبر شفق نيوز (3 تشرين الأول 2026)

#كركوك #مياه_الشرب #الحويجة #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "صحة كركوك", "hookHeadline": "150 إصابة بيومين.. والسبب؟",
  "voText": "سجلت ناحية الرياض في قضاء الحويجة بمحافظة كركوك أكثر من مئة وخمسين حالة إسهال وتقيؤ خلال يومي الثلاثاء والأربعاء الماضيين، بحسب جاسم ياسين حسين، مسؤول القطاع الصحي الثاني في صحة كركوك، لشفق نيوز. وأوضح أن الفرق الصحية أخذت عينات من مشروع ماء الرياض للفحص، ووزعت حبوب الكلور على السكان، بانتظار النتائج لتحديد السبب. وأضاف أن أغلب مشاريع ماء كركوك لا تتوفر فيها شروط التعقيم المطلوبة. تشرب مي الحنفية لو تشتري؟",
  "endQuestion": "تشرب مي الحنفية لو تشتري؟",
  "sourcesLine": "المصادر: دائرة صحة كركوك عبر شفق نيوز — 3 تشرين الأول 2026",
  "statPops": [{"value": "150+", "label": "حالة إسهال وتقيؤ خلال يومين", "matchWord": "وتقيؤ"},
               {"value": "الكلور", "label": "حبوب كلور توزّع على السكان", "matchWord": "الكلور"}]}}


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
