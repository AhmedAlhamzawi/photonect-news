#!/usr/bin/env python3
"""Author the 2026-09-25 slate: props.json + caption.txt (+ v11-brief.json on a-d).

Every figure traces to a named source published 23-25 Sep 2026. Computed figures carry (محتسب).
All 20 frames are Commons/Pexels real photos (KIE 11.5 credits, Higgsfield 0.38) — see _image_credits_2026_09_25.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-25"
DATE_LABEL = "SEP 25 • 2026"
AR_DATE = "25 أيلول 2026"
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

# ═══════════ A · 18:00 · P1 accountability / oil theft (LEAD) ═══════════
slug = f"{D}-a-oil-theft-500-million"
p = base(slug, "iraq_corruption", "A", "عاجل", "500 مليون دينار بالشهر من أنبوب نفط بالمثنى",
  ("MUTHANNA · SEP 25 | IRAQ'S NATIONAL SECURITY SERVICE SAID ON FRIDAY IT DISMANTLED A NETWORK STEALING CRUDE "
   "FROM A STRATEGIC PIPELINE RUNNING FROM SOUTHERN IRAQ TOWARD HADITHA; 4 SUSPECTS ARRESTED UNDER JUDICIAL "
   "WARRANTS (AL-MADA; SHAFAQ NEWS; 964) | TWO TAPS ON THE PIPE AND ~270 M OF HIDDEN BURIED PIPING INTO A FARM "
   "USED AS A DEN; CEMENT TRUCKS CONVERTED TO CARRY CRUDE AS CAMOUFLAGE | PRELIMINARY INVESTIGATION PER THE "
   "SERVICE: PROCEEDS REACHED ~500M IQD A MONTH; CORROSION SHOWS THE TAP WAS LONG-STANDING | TAPS SEALED; "
   "SUSPECTS REFERRED TO JUDICIARY"))
p["beats"] = [
 beat("الشبكة", "خرقان بأنبوب نفط استراتيجي",
  "جهاز الأمن الوطني أعلن اليوم الجمعة تفكيك شبكة لسرقة النفط الخام من أنبوب استراتيجي بالمثنى، واعتقال 4 متهمين بموافقات قضائية (المدى، شفق نيوز).",
  "4", "Suspects arrested by Iraq's National Security Service, Muthanna, 25 Sep",
  "متهمين اعتُقلوا بموافقات قضائية (جهاز الأمن الوطني)",
  [("المحافظة", "المثنى"), ("الخروقات", "2"), ("الأنبوب", "الجنوب ← حديثة")], 1, slug,
  ["شبكة لسرقة النفط الخام", "خرقان بأنبوب استراتيجي", "و4 متهمين بقبضة الأمن"], STOCK),
 beat("التمويه", "270 متراً أنابيب مدفونة لمزرعة",
  "حسب البيان، أنابيب مخفية تحت الأرض بطول نحو 270 متراً توصل الخرق لمزرعة، وشاحنات إسمنت حُوّرت لنقل الخام للتمويه (شبكة 964، المدى).",
  "270", "Metres of hidden buried piping from the tap into a farm (National Security Service)",
  "متراً من الأنابيب المدفونة من الخرق للمزرعة (جهاز الأمن الوطني)",
  [("الوكر", "مزرعة"), ("النقل", "شاحنات إسمنت"), ("الأنابيب", "مدفونة")], 2, slug,
  ["أنابيب مدفونة 270 متراً", "توصل لمزرعة", "وشاحنات إسمنت للتمويه"], STOCK),
 beat("العائدات", "500 مليون دينار بالشهر",
  "الجهاز قال إن التحقيقات الأولية أظهرت أن عائدات السرقة وصلت نحو 500 مليون دينار شهرياً، وإن الخرق قديم حسب آثار التآكل (المدى).",
  "500", "Million IQD a month in proceeds, per the service's preliminary investigation",
  "مليون دينار شهرياً حسب التحقيقات الأولية (جهاز الأمن الوطني)",
  [("الخرق", "قديم"), ("الأنبوب", "أُغلق"), ("المتهمون", "أُحيلوا للقضاء")], 3, slug,
  ["500 مليون دينار بالشهر", "حسب التحقيقات الأولية", "والخرق قديم"], STOCK),
]
p["arabicTicker"] = [
 "جهاز الأمن الوطني: تفكيك شبكة لسرقة وتهريب النفط الخام من أنبوب استراتيجي في المثنى واعتقال 4 متهمين (25 أيلول)",
 "الأنبوب يمتد من جنوب العراق باتجاه حديثة ومرتبط بمنظومة نقل النفط نحو شمال البلاد (المدى، شفق نيوز)",
 "كشف خرقين في الأنبوب وأنابيب مدفونة بطول نحو 270 متراً وصولاً إلى مزرعة اتُّخذت وكراً (شبكة 964)",
 "شاحنات مخصصة لنقل الإسمنت حُوّرت لنقل النفط الخام للتمويه (بيان الجهاز)",
 "التحقيقات الأولية: العائدات نحو 500 مليون دينار شهرياً — الخرقان أُغلقا والمتهمون أُحيلوا للقضاء",
 "سمعت بخرق أنبوب نفط بمنطقتك قبل؟"]
p["endQuestion"] = "سمعت بخرق أنبوب نفط بمنطقتك قبل؟"
p["sources"] = [{"name": "المدى", "domain": "almadapaper.net"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """سرقة النفط في المثنى — شكد كانت تجيب بالشهر؟

أنابيب مدفونة ومزرعة وشاحنات مموّهة.. التفاصيل بالفيديو.

سمعت بخرق أنبوب نفط بمنطقتك قبل؟

المصادر: المدى، شفق نيوز، شبكة 964 (25 أيلول 2026)

#العراق #المثنى #سرقة_النفط #النفط #photonectnews
@photonect.news""",
 "brief": {"kicker": "عاجل", "hookHeadline": "نص مليار دينار بالشهر من أنبوب",
  "voText": "أعلن جهاز الأمن الوطني، اليوم الجمعة، تفكيك شبكة لسرقة النفط الخام من أنبوب استراتيجي في محافظة المثنى، واعتقال أربعة متهمين بموافقات قضائية. وبحسب بيان الجهاز، كشفت العملية خرقين في الأنبوب، وأنابيب مدفونة بطول نحو مئتين وسبعين متراً تصل إلى مزرعة، وشاحنات إسمنت حُوّرت لنقل الخام. وقال الجهاز إن التحقيقات الأولية أظهرت أن العائدات بلغت نحو خمسمئة مليون دينار شهرياً، وإن الخرق قديم. سمعت بخرق أنبوب نفط بمنطقتك قبل؟",
  "endQuestion": "سمعت بخرق أنبوب نفط بمنطقتك قبل؟",
  "sourcesLine": "المصادر: المدى · شفق نيوز · شبكة 964 — 25 أيلول 2026",
  "statPops": [{"value": "270م", "label": "أنابيب مدفونة حتى المزرعة", "matchWord": "مدفونة"},
               {"value": "500M", "label": "دينار شهرياً — حسب التحقيقات الأولية", "matchWord": "شهرياً"}]}}

# ═══════════ B · 19:45 · P1 dollar anchor ═══════════
slug = f"{D}-b-dollar-friday-spread"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "تبدّل 100 دولار وترجعها؟ تخسر 1,000 دينار",
  ("BAGHDAD · SEP 25 | LAST PRICES BEFORE THE WEEKEND (SHAFAQ NEWS, THU 24 SEP EVENING CLOSE): KIFAH & HARITHIYA "
   "BOURSES 157,100 IQD PER $100, UP FROM 156,800 THAT MORNING | BAGHDAD EXCHANGE SHOPS: SELL 157,500 / BUY 156,500 "
   "— A 1,000 IQD ROUND-TRIP SPREAD PER $100 (COMPUTED) | ERBIL SELL 157,150 / BUY 157,100 | KALIMA (THU MORNING): "
   "BOURSES 156,850; EXCHANGE OFFICES BUY FROM CITIZENS 156,850 / SELL 157,900 — 1,050 SPREAD (COMPUTED)"))
p["beats"] = [
 beat("الإغلاق", "آخر سعر قبل العطلة: 157,100",
  "شفق نيوز: بورصتا الكفاح والحارثية أغلقتا الخميس، نهاية أسبوع التداول، على 157,100 دينار لكل 100 دولار، بعد 156,800 صباح اليوم نفسه.",
  "157,100", "IQD per $100, Kifah & Harithiya bourses, Thursday evening close (Shafaq News)",
  "دينار لكل 100 دولار — إغلاق الخميس بالكفاح والحارثية (شفق نيوز)",
  [("الصباح", "156,800"), ("أربيل بيع", "157,150"), ("أربيل شراء", "157,100")], 1, slug,
  ["آخر سعر قبل العطلة", "157,100 دينار", "الصبح كان 156,800"], STOCK),
 beat("الفرق", "بين البيع والشراء: 1,000 دينار",
  "بمحلات الصيرفة ببغداد سجّلت شفق نيوز مساء الخميس البيع 157,500 والشراء 156,500 — تشتري 100 دولار وتبيعها، تخسر 1,000 دينار (محتسب).",
  "1,000", "IQD lost buying then selling $100 at Baghdad exchange shops, Thursday close (computed from Shafaq)",
  "دينار فرق البيع والشراء لكل 100 دولار بمحلات بغداد (محتسب)",
  [("البيع", "157,500"), ("الشراء", "156,500"), ("الفرق", "1,000 (محتسب)")], 2, slug,
  ["البيع 157,500", "الشراء 156,500", "الفرق 1,000 دينار"], STOCK),
 beat("الصبح", "صباحاً كان الفرق 1,050",
  "موقع كلمة: مكاتب الصيرفة صباح الخميس اشترت من المواطنين بـ156,850 وباعت لهم بـ157,900 لكل 100 دولار — فرق 1,050 دينار (محتسب).",
  "1,050", "IQD spread at exchange offices, Thursday morning (computed from Kalima)",
  "دينار فرق البيع والشراء بمكاتب الصيرفة صباح الخميس (محتسب من موقع كلمة)",
  [("شراء", "156,850"), ("بيع", "157,900"), ("البورصة", "156,850")], 3, slug,
  ["الشراء 156,850", "البيع 157,900", "فرق 1,050 دينار"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: إغلاق الخميس في بورصتي الكفاح والحارثية 157,100 دينار لكل 100 دولار، بعد 156,800 صباحاً",
 "محلات الصيرفة ببغداد مساء الخميس: البيع 157,500 والشراء 156,500 دينار (شفق نيوز)",
 "أربيل: البيع 157,150 والشراء 157,100 دينار لكل 100 دولار (شفق نيوز)",
 "موقع كلمة صباح الخميس: مكاتب الصيرفة تشتري بـ156,850 وتبيع بـ157,900",
 "فرق البيع والشراء بمحلات بغداد 1,000 دينار لكل 100 دولار (محتسب)",
 "تشتري دولار لو تبيع هالأسبوع؟"]
p["endQuestion"] = "تشتري دولار لو تبيع هالأسبوع؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "موقع كلمة", "domain": "kalimaiq.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — ليش تخسر لمن تبدّل؟

آخر سعر قبل العطلة.. وفرق صغير بين البيع والشراء يطلع من جيبك.

تشتري دولار لو تبيع هالأسبوع؟

المصادر: شفق نيوز، موقع كلمة (24 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "تبدّل 100 دولار وترجعها؟ تخسر",
  "voText": "مع عطلة نهاية الأسبوع، سجّلت شفق نيوز آخر سعر للدولار عند إغلاق الخميس في بورصتي الكفاح والحارثية، مئة وسبعة وخمسين ألفاً ومئة دينار لكل مئة دولار، بعد مئة وستة وخمسين ألفاً وثمانمئة صباحاً. وفي محال الصيرفة ببغداد بلغ البيع مئة وسبعة وخمسين ألفاً وخمسمئة، والشراء مئة وستة وخمسين ألفاً وخمسمئة، أي أن من يشتري مئة دولار ثم يبيعها يخسر ألف دينار بحسابنا. تشتري دولار لو تبيع هالأسبوع؟",
  "endQuestion": "تشتري دولار لو تبيع هالأسبوع؟",
  "sourcesLine": "المصادر: شفق نيوز · موقع كلمة — 24 أيلول 2026",
  "statPops": [{"value": "157,100", "label": "إغلاق الخميس — الكفاح والحارثية", "matchWord": "ومئة"},
               {"value": "1,000", "label": "فرق البيع والشراء لكل 100$ (محتسب)", "matchWord": "يخسر"}]}}

# ═══════════ C · 21:15 · P2 Iran flight ban → Iraqi travellers ═══════════
slug = f"{D}-c-najaf-iran-flights"
p = base(slug, "mena_geo", "A", "عاجل", "رحلات إيران توقفت.. والبديل 25 ساعة بالباص",
  ("NAJAF · SEP 25 | NAJAF INTERNATIONAL AIRPORT HALTED ALL FLIGHTS TO AND FROM IRAN FROM 02:00 FRIDAY 25 SEP "
   "UNTIL FURTHER NOTICE (ALSUMARIA; SHAFAQ NEWS); ERBIL AND SULAYMANIYAH ALSO SUSPENDED IRAN FLIGHTS (SHAFAQ) | "
   "964: DOZENS OF STRANDED TRAVELLERS AT NAJAF'S GATES; ONE SAID THEY WOULD PAY TWICE — THE CANCELLED FLIGHT AND "
   "LAND TRANSPORT VIA SHALAMCHEH | FM FUAD HUSSEIN (TO AL ARABIYA, VIA SHAFAQ): BAGHDAD INFORMED TEHRAN OF THE BAN "
   "IN FORCE SINCE WEDNESDAY AND WILL DISCUSS SERVICING IRANIAN AVIATION WITH WASHINGTON | US TREASURY 8 SEP: "
   "SANCTIONS ON 36 ENTITIES INCL. 27 IRANIAN AIRLINES | TRAVEL AGENTS TO SHAFAQ (23 SEP): ~75% OF BOOKINGS ON "
   "IRANIAN CARRIERS; ~50 IRANIAN FLIGHTS A DAY TO IRAQ; LAND TRIP 20-25 HOURS TO SOME IRANIAN CITIES"))
p["beats"] = [
 beat("المطار", "عالقون ببوابة النجف: «ندفع مرتين»",
  "مطار النجف أوقف رحلات إيران من الثانية فجر الجمعة حتى إشعار آخر. مسافرون عالقون قالوا لشبكة 964 إنهم سيدفعون مرتين: للطيران الملغى وللنقل البري.",
  "02:00", "Friday 25 Sep — time Najaf airport halted all Iran flights, until further notice",
  "فجر الجمعة: توقف كل رحلات إيران بمطار النجف حتى إشعار آخر (السومرية، شفق نيوز)",
  [("النجف", "متوقف"), ("أربيل", "معلّق"), ("السليمانية", "معلّق")], 1, slug,
  ["رحلات إيران توقفت", "من الثانية فجراً", "والمسافر يدفع مرتين"], STOCK),
 beat("الخارجية", "بغداد أبلغت طهران.. وتفاتح واشنطن",
  "وزير الخارجية فؤاد حسين قال للعربية إن بغداد أبلغت إيران بالحظر النافذ منذ الأربعاء، وستناقش مع واشنطن تقديم الخدمات للطيران الإيراني (شفق نيوز).",
  "27", "Iranian airlines among 36 entities sanctioned by the US Treasury on 8 Sep",
  "شركة طيران إيرانية ضمن 36 جهة عاقبتها الخزانة الأمريكية في 8 أيلول (شفق نيوز)",
  [("العقوبات", "8 أيلول"), ("الجهات", "36"), ("الحظر", "منذ الأربعاء")], 2, slug,
  ["أبلغنا إيران بالحظر", "وراح نناقش واشنطن", "27 شركة طيران معاقبة"], STOCK),
 beat("البديل", "75% من الحجوزات كانت عالطيران الإيراني",
  "شركات سفر قالت لشفق نيوز إن نحو 75% من حجوزاتها على الطيران الإيراني، والطريق البري يستغرق 20 إلى 25 ساعة لبعض المدن الإيرانية.",
  "75%", "Share of Iraqi travel-agency bookings on Iranian carriers (agents to Shafaq News)",
  "من حجوزات شركات السفر العراقية كانت على الطيران الإيراني (شفق نيوز)",
  [("براً", "20-25 ساعة"), ("رحلات يومية", "~50"), ("المتضررون", "مرضى وطلاب وزوار")], 3, slug,
  ["75% من الحجوزات", "كانت عالطيران الإيراني", "والبر 25 ساعة"], STOCK),
]
p["arabicTicker"] = [
 "مطار النجف الدولي يوقف جميع الرحلات من وإلى إيران اعتباراً من الساعة 2 فجر الجمعة 25 أيلول وحتى إشعار آخر (السومرية، شفق نيوز)",
 "إقليم كوردستان يعلّق الرحلات من وإلى إيران في مطاري أربيل والسليمانية (شفق نيوز)",
 "مسافرون عالقون عند بوابات مطار النجف: سندفع مرتين، للحجز الملغى وللنقل البري عبر الشلامجة (شبكة 964)",
 "فؤاد حسين: أبلغنا إيران بالحظر النافذ منذ الأربعاء وسنناقش مع الجانب الأمريكي تقديم الخدمات للطيران الإيراني (شفق نيوز)",
 "الخزانة الأمريكية عاقبت في 8 أيلول 36 جهة مرتبطة بالطيران الإيراني بينها 27 شركة طيران",
 "عندك سفرة لإيران هالشهر؟"]
p["endQuestion"] = "عندك سفرة لإيران هالشهر؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}, {"name": "السومرية نيوز", "domain": "alsumaria.tv"}]
SLATE[slug] = {"props": p, "caption": """السفر من العراق إلى إيران — شنو صار بالرحلات؟

مطارات توقف الرحلات ومسافرون عالقين.. والبديل طريق طويل.

عندك سفرة لإيران هالشهر؟

المصادر: شفق نيوز، شبكة 964، السومرية نيوز (23-25 أيلول 2026)

#العراق #إيران #مطار_النجف #السفر #photonectnews
@photonect.news""",
 "brief": {"kicker": "عاجل", "hookHeadline": "رحلات إيران توقفت.. والبديل الباص",
  "voText": "أوقف مطار النجف الدولي جميع الرحلات من إيران وإليها، اعتباراً من الثانية فجر اليوم الجمعة وحتى إشعار آخر، كما علّق مطارا أربيل والسليمانية رحلاتهما. وتجمّع عشرات المسافرين عند بوابات مطار النجف، وقال أحدهم لشبكة تسعة ستة أربعة إنهم سيدفعون مرتين، للرحلة الملغاة وللنقل البري. ووزير الخارجية فؤاد حسين قال إن بغداد أبلغت طهران بالحظر، وستناقشه مع واشنطن. وتقول شركات سفر إن الطريق البري يستغرق حتى خمس وعشرين ساعة. عندك سفرة لإيران هالشهر؟",
  "endQuestion": "عندك سفرة لإيران هالشهر؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 · السومرية نيوز — 25 أيلول 2026",
  "statPops": [{"value": "02:00", "label": "توقف رحلات إيران بمطار النجف", "matchWord": "الثانية"},
               {"value": "25 ساعة", "label": "السفر براً لبعض المدن الإيرانية", "matchWord": "ساعة"}]}}

# ═══════════ D · 22:30 · P1 oil revenue — SOMO hunting buyers (V10.1 CONTROL) ═══════════
slug = f"{D}-d-somo-oil-buyers"
p = base(slug, "iraq_money", "B", "نفط", "نفط العراق يدوّر مشترين.. و20 دولار شحن عالبرميل",
  ("BAGHDAD · SEP 25 | BLOOMBERG (VIA SHAFAQ NEWS), CITING PEOPLE FAMILIAR: SOMO OFFERED LATE-SEPTEMBER-LOADING "
   "CRUDE TO AT LEAST TWO COMPANIES AFTER SOME TRADERS PULLED OUT | BLOOMBERG CALCULATION (BALTIC EXCHANGE DATA): "
   "VLCC FREIGHT GULF OF OMAN → EAST ASIA ADDS ~$20/BBL, ~ONE-FIFTH OF A CRUDE PRICE ABOVE $100 AT LOADING | "
   "REUTERS (VIA SHAFAQ, 24 SEP): VITOL BOUGHT AT LEAST 25M BARRELS OF IRAQI CRUDE IN SEPTEMBER, AT STEEP "
   "DISCOUNTS | SOMO TENDER (REUTERS, 25 SEP): 2M BBL BASRAH HEAVY FOR 1-7 OCT LOADING"))
p["beats"] = [
 beat("العرض", "سومو تعرض شحنات باللحظة الأخيرة",
  "بلومبرغ نقلت عن مصادر أن سومو عرضت شحنات خام للتحميل أواخر أيلول على شركتين على الأقل، بعد انسحاب بعض التجار (شفق نيوز).",
  "2", "Companies at least that SOMO offered late-September cargoes to (Bloomberg)",
  "شركتان على الأقل عُرضت عليهما شحنات أواخر أيلول (بلومبرغ)",
  [("المسوّق", "سومو"), ("التحميل", "أواخر أيلول"), ("السبب", "انسحاب تجار")], 1, slug,
  ["سومو تعرض شحنات", "باللحظة الأخيرة", "بعد انسحاب تجار"], STOCK),
 beat("الشحن", "20 دولار شحن على كل برميل",
  "حسب حسابات بلومبرغ، شحن الخام بناقلات عملاقة من خليج عُمان لشرق آسيا يضيف نحو 20 دولاراً للبرميل، نحو خُمس قيمته.",
  "$20", "Added per barrel by VLCC freight, Gulf of Oman to East Asia (Bloomberg calculation)",
  "دولار تقريباً يضيفها الشحن لكل برميل نحو شرق آسيا (بلومبرغ)",
  [("النسبة", "نحو الخُمس"), ("سعر التحميل", "+100$"), ("الوجهة", "شرق آسيا")], 2, slug,
  ["20 دولار شحن", "على كل برميل", "نحو خُمس قيمته"], STOCK),
 beat("المشترون", "فيتول اشترت 25 مليون برميل",
  "رويترز: فيتول اشترت ما لا يقل عن 25 مليون برميل عراقي خلال أيلول بخصومات كبيرة، وسومو طرحت عطاءً لمليوني برميل من البصرة الثقيل (شفق نيوز).",
  "25M", "Barrels of Iraqi crude Vitol bought in September, at least (Reuters)",
  "مليون برميل عراقي على الأقل اشترتها فيتول بأيلول (رويترز)",
  [("العطاء", "2 مليون برميل"), ("الخام", "البصرة الثقيل"), ("التحميل", "1-7 تشرين الأول")], 3, slug,
  ["فيتول اشترت 25 مليون برميل", "بخصومات كبيرة", "وعطاء جديد لمليونين"], STOCK),
]
p["arabicTicker"] = [
 "بلومبرغ: سومو عرضت شحنات خام في اللحظات الأخيرة للتحميل أواخر أيلول على شركتين على الأقل (شفق نيوز — 25 أيلول)",
 "حسابات بلومبرغ: شحن الخام من خليج عمان إلى شرق آسيا يضيف نحو 20 دولاراً للبرميل، نحو خُمس قيمته",
 "رويترز: فيتول اشترت ما لا يقل عن 25 مليون برميل من الخام العراقي خلال أيلول بخصومات كبيرة",
 "سومو تطرح عطاءً لبيع مليوني برميل من خام البصرة الثقيل للتحميل من 1 إلى 7 تشرين الأول (رويترز)",
 "تتابع سعر النفط كل يوم؟"]
p["endQuestion"] = "تتابع سعر النفط كل يوم؟"
p["sources"] = [{"name": "بلومبرغ", "domain": "bloomberg.com"}, {"name": "رويترز", "domain": "reuters.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """نفط العراق وهرمز — ليش صعب نبيع البرميل؟

شحن غالي ومشترين ينسحبون.. شوف شلون يتحرك نفطنا.

تتابع سعر النفط كل يوم؟

المصادر: بلومبرغ، رويترز عبر شفق نيوز (24-25 أيلول 2026)

#العراق #النفط #سومو #photonectnews
@photonect.news""",
 "brief": None}

# ═══════════ E · 23:45 · P2 Syria corridor → petrol at your pump ═══════════
slug = f"{D}-e-syria-petrol-baniyas"
p = base(slug, "mena_geo", "C", "عاجل", "أول بنزين للعراق يعبر من سوريا",
  ("BANIYAS · SEP 25 | SYRIAN PETROLEUM COMPANY (STATEMENT TO SHAFAQ NEWS; ALMODON/SANA) ANNOUNCED ON FRIDAY THE "
   "FIRST PETROL SHIPMENTS FROM SYRIAN PORTS TOWARD THE IRAQI BORDER CROSSINGS | 3 TANKERS ARRIVED; FIRST UNLOADED "
   "~32,000 T OF PETROL | LOADING BEGAN 22 SEP: CONVOYS OF 10 THEN 55 ROAD TANKERS; PORTS READY FOR 150 ROAD "
   "TANKERS A DAY | AL-RASHEED TV, CITING ATTAQA PLATFORM: FIRST TANKER CAME FROM HOUSTON, ~13,000 KM ROUTE | "
   "BAGHDAD AND OTHER PROVINCES HAVE FACED A PETROL SUPPLY CRISIS FOR WEEKS (SHAFAQ)"))
p["beats"] = [
 beat("بانياس", "أول ناقلة فرّغت 32 ألف طن",
  "الشركة السورية للبترول أعلنت اليوم انطلاق أولى شحنات البنزين من موانئها باتجاه العراق، وأول ناقلة فرّغت نحو 32 ألف طن (شفق نيوز، المدن).",
  "32,000", "Tonnes of petrol unloaded from the first tanker at Syrian ports (Syrian Petroleum Company)",
  "طن بنزين فرّغتها أول ناقلة بالموانئ السورية (الشركة السورية للبترول)",
  [("الميناء", "بانياس"), ("الوجهة", "المعابر العراقية"), ("الإعلان", "25 أيلول")], 1, slug,
  ["أول شحنة بنزين", "عبر موانئ سوريا", "32 ألف طن"], STOCK),
 beat("الناقلات", "3 ناقلات وصلت.. واثنتان تنتظران",
  "الشركة قالت إن 3 ناقلات وصلت، ونقلت قناة الرشيد عن منصة الطاقة أن الأولى جاءت من هيوستن الأمريكية بمسار نحو 13 ألف كيلومتر.",
  "3", "Tankers of petroleum products arrived at Syrian ports; two await unloading",
  "ناقلات وصلت للموانئ السورية واثنتان تنتظران التفريغ (الشركة السورية للبترول)",
  [("فُرّغت", "1"), ("تنتظر", "2"), ("المسار", "~13,000 كم")], 2, slug,
  ["3 ناقلات وصلت", "وحدة فرّغت", "واثنتين تنتظر"], STOCK),
 beat("الصهاريج", "150 صهريج باليوم نحو العراق",
  "التحميل بدأ 22 أيلول بقافلتين: 10 صهاريج ثم 55، والموانئ جاهزة لـ150 صهريجاً يومياً، وسط أزمة بنزين ببغداد ومحافظات منذ أسابيع (شفق نيوز).",
  "150", "Road tankers a day — loading capacity Syrian ports say they are ready for",
  "صهريجاً يومياً الطاقة التحميلية الجاهزة (الشركة السورية للبترول)",
  [("القافلة 1", "10"), ("القافلة 2", "55"), ("بدء التحميل", "22 أيلول")], 3, slug,
  ["قافلتين: 10 ثم 55", "والجاهزية 150 باليوم", "والأزمة بمحطاتنا"], STOCK),
]
p["arabicTicker"] = [
 "الشركة السورية للبترول: انطلاق أولى شحنات البنزين عبر الموانئ السورية باتجاه المعابر الحدودية مع العراق (25 أيلول)",
 "3 ناقلات وصلت الموانئ السورية وتفريغ الأولى انتهى بحمولة نحو 32 ألف طن من البنزين (صفوان شيخ أحمد — شفق نيوز)",
 "التحميل بدأ في 22 أيلول: قافلة من 10 صهاريج ثم قافلة من 55 صهريجاً",
 "الموانئ جاهزة لرفع الطاقة التحميلية إلى 150 صهريجاً يومياً",
 "قناة الرشيد عن منصة الطاقة: الناقلة الأولى قادمة من هيوستن بمسار نحو 13 ألف كيلومتر",
 "لقيت بنزين بمحطتك هالأسبوع؟"]
p["endQuestion"] = "لقيت بنزين بمحطتك هالأسبوع؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "المدن", "domain": "almodon.com"}, {"name": "قناة الرشيد", "domain": "alrasheedmedia.com"}]
SLATE[slug] = {"props": p, "caption": """أزمة البنزين في العراق — شحنة جديدة جاية من سوريا

ناقلات وصلت بانياس وصهاريج بالطريق.. شكد تكفي؟

لقيت بنزين بمحطتك هالأسبوع؟

المصادر: شفق نيوز، المدن، قناة الرشيد (25 أيلول 2026)

#العراق #البنزين #سوريا #أزمة_الوقود #photonectnews
@photonect.news""",
 "brief": {"kicker": "عاجل", "hookHeadline": "أول بنزين للعراق يعبر من سوريا",
  "voText": "أعلنت الشركة السورية للبترول، اليوم الجمعة، انطلاق أولى شحنات البنزين من الموانئ السورية باتجاه المعابر الحدودية مع العراق. وقالت الشركة إن ثلاث ناقلات وصلت، وإن تفريغ الأولى انتهى بحمولة نحو اثنين وثلاثين ألف طن. وبدأ التحميل في الثاني والعشرين من أيلول بقافلتين من عشرة صهاريج ثم خمسة وخمسين، والموانئ جاهزة لمئة وخمسين صهريجاً يومياً. ويأتي ذلك وسط أزمة بنزين في بغداد ومحافظات أخرى منذ أسابيع. لقيت بنزين بمحطتك هالأسبوع؟",
  "endQuestion": "لقيت بنزين بمحطتك هالأسبوع؟",
  "sourcesLine": "المصادر: الشركة السورية للبترول عبر شفق نيوز · المدن — 25 أيلول 2026",
  "statPops": [{"value": "32,000", "label": "طن بنزين بأول ناقلة", "matchWord": "طن"},
               {"value": "150", "label": "صهريج يومياً — الجاهزية", "matchWord": "يومياً"}]}}


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
