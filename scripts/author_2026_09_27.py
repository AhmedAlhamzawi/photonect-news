#!/usr/bin/env python3
"""Author the 2026-09-27 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source published 26-27 Sep 2026. Computed figures carry (محتسب).
All 20 frames are Commons/Pexels real photos (KIE 11.5 credits, Higgsfield 0.38) — see _image_credits_2026_09_27.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-27"
DATE_LABEL = "SEP 27 • 2026"
AR_DATE = "27 أيلول 2026"
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

# ═══════════ A · 18:00 · P1 corruption / accountability (LEAD) ═══════════
slug = f"{D}-a-pension-bribes-nazaha"
p = base(slug, "iraq_corruption", "A", "النزاهة", "رواتبك المتراكمة مقابل رشوة؟ النزاهة تضبط متهمين",
  ("BAGHDAD / ANBAR · SEP 27 | IRAQ'S FEDERAL INTEGRITY COMMISSION SAID ON SUNDAY IT CAUGHT TWO SUSPECTS IN BAGHDAD "
   "RED-HANDED RECEIVING BRIBES, IN TWO SEPARATE OPERATIONS (964; SHAFAQ NEWS; ALSUMARIA) | 1: LEGAL DEPARTMENT "
   "DIRECTOR AT THE NATIONAL INSURANCE COMPANY, OVER RENEWING THE LEASE OF TWO PLOTS IN DIWANIYAH | 2: EMPLOYEE AT "
   "THE NATIONAL RETIREMENT AUTHORITY (POLITICAL PRISONERS SECTION) RECEIVING 2M IQD FROM A WOMAN APPLICANT TO "
   "RELEASE HER ACCUMULATED SALARIES; HER MASTERCARD FOUND ON HIM | RUSAFA INVESTIGATIVE JUDGE ORDERED BOTH DETAINED "
   "| ANBAR: SUSPECT CAUGHT RECEIVING 3M IQD TO LIFT A SEIZURE ON A PENSION SHARE, CLAIMING STAFF WOULD GET THE MONEY"))
p["beats"] = [
 beat("التأمين", "مدير قانوني متلبساً بالرشوة",
  "هيئة النزاهة: ضبط مدير القسم القانوني بشركة التأمين الوطنية متلبساً بتسلّم رشوة مقابل تجديد عقد إيجار قطعتي أرض بالديوانية (شبكة 964، شفق نيوز).",
  "2", "Separate sting operations in Baghdad, per the Integrity Commission, 27 Sep",
  "عمليتا ضبط منفصلتان ببغداد (هيئة النزاهة)",
  [("الشركة", "التأمين الوطنية"), ("العقد", "قطعتا أرض"), ("المكان", "الديوانية")], 1, slug,
  ["مدير قانوني", "متلبساً بالرشوة", "مقابل تجديد عقد"], STOCK),
 beat("التقاعد", "مليونا دينار مقابل رواتب متراكمة",
  "حسب الهيئة، موظف بقسم السجناء السياسيين في هيئة التقاعد تسلّم مليوني دينار من مراجِعة مقابل صرف رواتبها المتراكمة، وضُبطت بطاقتها المصرفية بحوزته.",
  "2 مليون", "IQD allegedly taken from a woman applicant to release her accumulated salaries (Integrity Commission)",
  "دينار مقابل صرف رواتب متراكمة لمراجِعة (هيئة النزاهة)",
  [("القسم", "السجناء السياسيين"), ("المضبوط", "بطاقتها المصرفية"), ("القرار", "توقيف")], 2, slug,
  ["مليونا دينار", "مقابل رواتبها المتراكمة", "وبطاقتها بجيبه"], STOCK),
 beat("الأنبار", "3 ملايين لرفع حجز عن تقاعد",
  "بالأنبار، ضبطت النزاهة متهماً تسلّم 3 ملايين دينار من مراجع لرفع الحجز عن حصة تقاعدية لوالدته وشقيقته، مدعياً أن المال لموظفين (السومرية نيوز).",
  "3 مليون", "IQD a suspect allegedly received to lift a seizure on a pension share, Anbar (Integrity Commission)",
  "دينار لرفع الحجز عن حصة تقاعدية بالأنبار (هيئة النزاهة)",
  [("الدائرة", "تقاعد الأنبار"), ("الحصة", "والدته وشقيقته"), ("القرار", "توقيف")], 3, slug,
  ["3 ملايين دينار", "لرفع حجز التقاعد", "والمتهم موقوف"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة: ضبط متهمَين اثنين أحدهما مدير متلبسَين بتسلّم الرشوة في عمليتين منفصلتين ببغداد (27 أيلول)",
 "ضبط مدير القسم القانوني في شركة التأمين الوطنية مقابل تجديد عقد تأجير قطعتي أرض في الديوانية",
 "ضبط موظف في هيئة التقاعد الوطنية - قسم السجناء السياسيين أثناء تسلّمه مليوني دينار من مراجِعة (شبكة 964)",
 "قاضي تحقيق الرصافة المختص بقضايا النزاهة قرر توقيف المتهمَين (شفق نيوز)",
 "الأنبار: ضبط متهم بالجرم المشهود أثناء تسلّمه 3 ملايين دينار لقاء رفع الحجز عن حصة تقاعدية (السومرية نيوز)",
 "معاملتك بالتقاعد خلصت بموعدها؟"]
p["endQuestion"] = "معاملتك بالتقاعد خلصت بموعدها؟"
p["sources"] = [{"name": "شبكة 964", "domain": "964media.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "السومرية نيوز", "domain": "alsumaria.tv"}]
SLATE[slug] = {"props": p, "caption": """رشوة بدوائر التقاعد — شنو كشفت النزاهة اليوم؟

رواتب متراكمة وبطاقة مصرفية وحصة تقاعد محجوزة.. التفاصيل بالفيديو.

معاملتك بالتقاعد خلصت بموعدها؟

المصادر: هيئة النزاهة عبر شبكة 964، شفق نيوز، السومرية نيوز (27 أيلول 2026)

#العراق #النزاهة #التقاعد #الفساد #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "رواتبك المتراكمة مقابل رشوة؟",
  "voText": "أعلنت هيئة النزاهة، اليوم الأحد، ضبط متهمَين في بغداد بالجرم المشهود أثناء تسلّم رشوة. الأول مدير القسم القانوني في شركة التأمين الوطنية، مقابل تجديد عقد إيجار قطعتي أرض في الديوانية. والثاني موظف في هيئة التقاعد، قسم السجناء السياسيين، تسلّم مليوني دينار من مراجِعة مقابل صرف رواتبها المتراكمة، وضُبطت بطاقتها المصرفية بحوزته، وقرر القضاء توقيفهما. وفي الأنبار، ضُبط متهم تسلّم ثلاثة ملايين دينار لرفع الحجز عن حصة تقاعدية. معاملتك بالتقاعد خلصت بموعدها؟",
  "endQuestion": "معاملتك بالتقاعد خلصت بموعدها؟",
  "sourcesLine": "المصادر: هيئة النزاهة عبر شبكة 964 · شفق نيوز · السومرية نيوز — 27 أيلول 2026",
  "statPops": [{"value": "2 مليون", "label": "دينار مقابل رواتب متراكمة", "matchWord": "مليوني"},
               {"value": "3 مليون", "label": "دينار لرفع حجز تقاعد — الأنبار", "matchWord": "ثلاثة"}]}}

# ═══════════ B · 19:45 · P1 dollar anchor ═══════════
slug = f"{D}-b-dollar-155250-shipment"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار نزل تحت 156 ألف.. شنو السبب؟",
  ("BAGHDAD · SEP 27 | SHAFAQ NEWS: KIFAH & HARITHIYA BOURSES 155,250 IQD PER $100 SUNDAY MORNING, DOWN FROM "
   "156,800 ON SATURDAY (−1,550, COMPUTED) | BAGHDAD EXCHANGE SHOPS: SELL 155,750 / BUY 154,750; ERBIL SELL "
   "155,350 / BUY 155,250 | GOVERNMENT SPOKESMAN HAIDAR AL-ABOUDI (964, 26 SEP): PM ALI AL-ZAIDI REACHED AN "
   "UNDERSTANDING IN THE US ON CONTINUED CASH-DOLLAR SHIPMENTS; A NEW SHIPMENT DUE IN THE COMING DAYS, VALUE NOT "
   "DISCLOSED | ECONOMIST MOHAMMED AL-HUSNI (SHAFAQ): NEWS OF THE SHIPMENT EASED FEARS AND PRECAUTIONARY DEMAND"))
p["beats"] = [
 beat("البورصة", "155,250 صباح الأحد",
  "شفق نيوز: بورصتا الكفاح والحارثية سجّلتا صباح اليوم 155,250 ديناراً لكل 100 دولار، بعد 156,800 أمس السبت.",
  "155,250", "IQD per $100, Kifah & Harithiya bourses, Sunday morning (Shafaq News)",
  "دينار لكل 100 دولار — الكفاح والحارثية صباح الأحد (شفق نيوز)",
  [("السبت", "156,800"), ("الفرق", "1,550- (محتسب)"), ("أربيل بيع", "155,350")], 1, slug,
  ["الدولار نزل", "155,250 دينار", "أمس كان 156,800"], STOCK),
 beat("الشحنة", "شحنة دولار جاية خلال أيام",
  "المتحدث باسم الحكومة حيدر العبودي قال إن الزيدي توصّل بواشنطن لتفاهم على استمرار شحنات الدولار النقدي، وشحنة جديدة تصل قريباً دون تحديد قيمتها (شبكة 964).",
  "160,000+", "IQD per $100 — level the rate passed in recent days, before the drop (Shafaq News)",
  "دينار لكل 100 دولار — السعر تجاوزها خلال الأيام الماضية (شفق نيوز)",
  [("المصدر", "المتحدث الحكومي"), ("القيمة", "غير محددة"), ("الموعد", "الأيام المقبلة")], 2, slug,
  ["شحنة دولار نقدي", "جاية خلال أيام", "وقيمتها ما انعلنت"], STOCK),
 beat("الصيرفة", "بمحلات بغداد: تبيع 155,750",
  "محلات الصيرفة ببغداد: البيع 155,750 والشراء 154,750. الخبير محمد الحسني قال لشفق نيوز إن السوق تفاعل مع خبر الشحنة قبل وصولها.",
  "155,750", "IQD per $100, Baghdad exchange-shop selling price, Sunday morning (Shafaq News)",
  "دينار سعر البيع لكل 100 دولار بمحلات بغداد (شفق نيوز)",
  [("البيع", "155,750"), ("الشراء", "154,750"), ("أربيل شراء", "155,250")], 3, slug,
  ["البيع 155,750", "الشراء 154,750", "السوق سبق الشحنة"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الدولار في بورصتي الكفاح والحارثية 155,250 ديناراً لكل 100 دولار صباح الأحد، بعد 156,800 السبت",
 "محال الصيرفة ببغداد: البيع 155,750 والشراء 154,750 — أربيل: البيع 155,350 والشراء 155,250",
 "المتحدث باسم الحكومة حيدر العبودي: شحنة جديدة من الدولار النقدي تصل خلال الأيام المقبلة (شبكة 964)",
 "الخبير الاقتصادي محمد الحسني: خبر الشحنة هدّأ مخاوف المتعاملين وقلّل الطلب الاحتياطي (شفق نيوز)",
 "راح تشتري دولار هالأسبوع؟"]
p["endQuestion"] = "راح تشتري دولار هالأسبوع؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — ليش نزل؟

خبر شحنة دولار جديدة سبق وصولها للسوق.. التفاصيل بالفيديو.

راح تشتري دولار هالأسبوع؟

المصادر: شفق نيوز، شبكة 964 (26-27 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "الدولار نزل.. شنو السبب؟",
  "voText": "انخفض سعر الدولار في بغداد صباح اليوم الأحد. وبحسب شفق نيوز، سجّلت بورصتا الكفاح والحارثية مئة وخمسة وخمسين ألفاً ومئتين وخمسين ديناراً لكل مئة دولار، بعد مئة وستة وخمسين ألفاً وثمانمئة أمس السبت. ويأتي ذلك بعدما قال المتحدث باسم الحكومة حيدر العبودي إن شحنة جديدة من الدولار النقدي ستصل خلال الأيام المقبلة، إثر تفاهم مع واشنطن، من دون تحديد قيمتها. ويرى خبير اقتصادي أن السوق تفاعل مع الخبر قبل وصول الشحنة. راح تشتري دولار هالأسبوع؟",
  "endQuestion": "راح تشتري دولار هالأسبوع؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 26-27 أيلول 2026",
  "statPops": [{"value": "155,250", "label": "بورصة الكفاح — صباح الأحد", "matchWord": "ومئتين"},
               {"value": "1,550-", "label": "أقل من سعر السبت (محتسب)", "matchWord": "وثمانمئة"}]}}

# ═══════════ C · 21:15 · P2 US warning on Iraqi airports (V10.1 CONTROL) ═══════════
slug = f"{D}-c-us-warning-iraq-airports"
p = base(slug, "mena_geo", "A", "عاجل", "تحذير أمريكي: عقوبات على أي مطار يستقبل طائرات إيران",
  ("BAGHDAD · SEP 27 | A SENIOR GOVERNMENT SOURCE TO SHAFAQ NEWS: WASHINGTON WARNED BAGHDAD THAT SANCTIONS COULD HIT "
   "ANY IRAQI AIRPORT OR FIRM PROVIDING LANDING, GROUND HANDLING OR FUEL TO SANCTIONED IRANIAN AIRLINES | BAGHDAD IS "
   "NEGOTIATING EXEMPTIONS FOR MEDICAL, EDUCATIONAL AND RELIGIOUS TRIPS (SHAFAQ; 964) | BASRA MPS (964, 26 SEP): 48-HOUR "
   "ULTIMATUM; MP FALIH AL-KHAZALI: ~50 FLIGHTS A DAY HALTED, ~$242M A YEAR IN GROUND-SERVICE LOSSES | MPS: MORE THAN "
   "100,000 IRAQI STUDENTS STUDY IN IRAN"))
p["beats"] = [
 beat("التحذير", "واشنطن: العقوبات تطال المطار نفسه",
  "مصدر حكومي لشفق نيوز: واشنطن حذّرت بغداد أن أي مطار أو شركة تقدّم الهبوط أو المناولة أو الوقود لطيران إيراني معاقب قد تُعاقب.",
  "3", "Airports that stopped receiving Iranian carriers: Baghdad, Basra, Najaf (964)",
  "مطارات أوقفت استقبال الطائرات الإيرانية: بغداد والبصرة والنجف (شبكة 964)",
  [("الهبوط", "مشمول"), ("المناولة", "مشمولة"), ("الوقود", "مشمول")], 1, slug,
  ["تحذير أمريكي لبغداد", "العقوبات تطال المطار", "مو بس شركة الطيران"], STOCK),
 beat("الكلفة", "50 رحلة يومياً متوقفة",
  "النائب فالح الخزعلي قال لشبكة 964 إن الحظر يوقف نحو 50 رحلة يومياً، بخسائر خدمات أرضية تُقدّر بنحو 242 مليون دولار سنوياً.",
  "$242M", "Estimated yearly ground-service losses, per Basra MP Falih al-Khazali (964)",
  "دولار خسائر سنوية بالخدمات الأرضية حسب تقدير النائب فالح الخزعلي (شبكة 964)",
  [("الرحلات", "~50 يومياً"), ("مهلة النواب", "48 ساعة"), ("المطلب", "رفع الحظر")], 2, slug,
  ["50 رحلة يومياً", "242 مليون دولار", "ومهلة 48 ساعة"], STOCK),
 beat("الاستثناء", "بغداد تفاوض على استثناءات إنسانية",
  "المصدر الحكومي قال إن بغداد تفاوض واشنطن على استثناءات لرحلات علاجية وتعليمية ودينية. ونواب قالوا إن أكثر من 100 ألف طالب عراقي يدرسون بإيران.",
  "100,000+", "Iraqi students in Iran, per MPs (964)",
  "طالب عراقي يدرسون في إيران حسب نواب (شبكة 964)",
  [("علاج", "استثناء مطلوب"), ("دراسة", "استثناء مطلوب"), ("زيارة", "استثناء مطلوب")], 3, slug,
  ["استثناءات للعلاج", "والدراسة والزيارة", "والمفاوضات مستمرة"], STOCK),
]
p["arabicTicker"] = [
 "مصدر حكومي لشفق نيوز: تحذير أمريكي مباشر لبغداد من معاقبة أي مطار يقدم خدمات لشركات الطيران الإيرانية المشمولة بالعقوبات",
 "العقوبات قد تشمل خدمات الهبوط والمناولة الأرضية والتزود بالوقود (شفق نيوز — 27 أيلول)",
 "الحكومة تفاوض الجانب الأمريكي على استثناءات لرحلات علاجية وتعليمية ودينية",
 "نواب البصرة يمهلون الحكومة 48 ساعة لرفع الحظر ويجمعون تواقيع لاستضافة رئيس الوزراء (شبكة 964)",
 "عندك قريب يدرس أو يتعالج بإيران؟"]
p["endQuestion"] = "عندك قريب يدرس أو يتعالج بإيران؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """رحلات العراق وإيران — ليش توقفت المطارات؟

تحذير أمريكي ومهلة نيابية ومفاوضات على استثناءات.. التفاصيل بالفيديو.

عندك قريب يدرس أو يتعالج بإيران؟

المصادر: شفق نيوز، شبكة 964 (26-27 أيلول 2026)

#العراق #إيران #الطيران #العقوبات #photonectnews
@photonect.news""",
 "brief": None}

# ═══════════ D · 22:30 · P1 electricity ═══════════
slug = f"{D}-d-electricity-52-percent-lost"
p = base(slug, "iraq_services", "A", "الكهرباء", "52% من كهرباء العراق ضاعت بـ2025",
  ("BAGHDAD · SEP 27 | IRAQ MINISTRY OF ELECTRICITY 2025 ANNUAL STATISTICAL REPORT (VIA SHAFAQ NEWS; AL-MUSTAQILA): "
   "153,975,051 MWH RECEIVED BY DISTRIBUTION FROM TRANSMISSION; 73,361,651 MWH SOLD TO CONSUMERS; LOSSES 80,613,400 "
   "MWH = 52% | LOSS RATES: KARBALA 67%, BAGHDAD/SADR 65%, MAYSAN 62%, SALAHUDDIN 61%, KIRKUK 58%, DIWANIYAH 58%, "
   "BABYLON 56%, BASRA 52%, NAJAF 41% | BY REGION: BAGHDAD 56%, SOUTH 54%, NORTH 54%, MID-EUPHRATES 55%, CENTRE 36%"))
p["beats"] = [
 beat("التقرير", "أكثر من نص الكهرباء ضاعت",
  "التقرير الإحصائي السنوي لوزارة الكهرباء لعام 2025: الضائعات بلغت 80,613,400 ميغاواط ساعة، أي 52% من الطاقة المستلمة (شفق نيوز).",
  "52%", "Share of electricity received by distribution that was lost in 2025 (Ministry of Electricity report)",
  "من الكهرباء المستلمة ضاعت خلال 2025 (تقرير وزارة الكهرباء)",
  [("المستلمة", "153,975,051"), ("الضائعة", "80,613,400"), ("الوحدة", "ميغاواط ساعة")], 1, slug,
  ["52% ضاعت", "80 مليون ميغاواط ساعة", "خلال سنة وحدة"], STOCK),
 beat("المباع", "الضايع أكثر من اللي انباع",
  "حسب التقرير، الطاقة المباعة للمستهلكين كانت 73,361,651 ميغاواط ساعة فقط، أقل من الطاقة الضائعة البالغة 80,613,400 (المستقلة، شفق نيوز).",
  "73,361,651", "MWh sold to consumers in 2025 — less than the energy lost (Ministry of Electricity report)",
  "ميغاواط ساعة بيعت للمستهلكين بـ2025 — أقل من الضائعة (تقرير الوزارة)",
  [("المباعة", "73,361,651"), ("الضائعة", "80,613,400"), ("السنة", "2025")], 2, slug,
  ["المباع 73 مليون", "والضايع 80 مليون", "الضايع أكثر"], STOCK),
 beat("المحافظات", "كربلاء الأعلى: 67% ضائعات",
  "كربلاء سجّلت أعلى نسبة ضائعات بـ67%، تلتها بغداد/الصدر 65%، ميسان 62%، صلاح الدين 61%، والنجف الأقل بين المذكورة 41%.",
  "67%", "Loss rate in Karbala, highest by province in 2025 (Ministry of Electricity report)",
  "نسبة ضائعات كربلاء — الأعلى بين المحافظات (تقرير الوزارة)",
  [("بغداد/الصدر", "65%"), ("ميسان", "62%"), ("النجف", "41%")], 3, slug,
  ["كربلاء 67%", "بغداد الصدر 65%", "ميسان 62%"], STOCK),
]
p["arabicTicker"] = [
 "تقرير وزارة الكهرباء السنوي 2025: الضائعات 80,613,400 ميغاواط ساعة بنسبة 52% من الطاقة المستلمة (شفق نيوز)",
 "الطاقة المستلمة من شركات النقل 153,975,051 ميغاواط ساعة، والمباعة للمستهلكين 73,361,651",
 "أعلى نسب الضائعات: كربلاء 67% — بغداد/الصدر 65% — ميسان 62% — صلاح الدين 61%",
 "كركوك 58% — الديوانية 58% — بابل 56% — البصرة 52% — النجف 41%",
 "كم ساعة كهرباء وطنية توصلك اليوم؟"]
p["endQuestion"] = "كم ساعة كهرباء وطنية توصلك اليوم؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "المستقلة", "domain": "mustaqila.com"}, {"name": "وزارة الكهرباء", "domain": "moelc.gov.iq"}]
SLATE[slug] = {"props": p, "caption": """الكهرباء في العراق — وين تروح نص الطاقة؟

تقرير الوزارة لـ2025 يكشف شكد ضاع.. ومحافظتك وين بالترتيب؟

كم ساعة كهرباء وطنية توصلك اليوم؟

المصادر: تقرير وزارة الكهرباء السنوي عبر شفق نيوز، المستقلة (27 أيلول 2026)

#العراق #الكهرباء #الضائعات #photonectnews
@photonect.news""",
 "brief": {"kicker": "الكهرباء", "hookHeadline": "نص الكهرباء ضاعت بسنة وحدة",
  "voText": "كشف التقرير الإحصائي السنوي لوزارة الكهرباء لعام ألفين وخمسة وعشرين، أن أكثر من نصف الطاقة المستلمة ضاع. فمن نحو مئة وأربعة وخمسين مليون ميغاواط ساعة استلمتها شبكات التوزيع، بيع للمستهلكين نحو ثلاثة وسبعين مليوناً فقط، وبلغت الضائعات نحو ثمانين مليوناً، أي اثنين وخمسين بالمئة. وسجّلت كربلاء أعلى نسبة ضائعات بسبعة وستين بالمئة، تلتها بغداد الصدر بخمسة وستين، ثم ميسان باثنين وستين. كم ساعة كهرباء وطنية توصلك اليوم؟",
  "endQuestion": "كم ساعة كهرباء وطنية توصلك اليوم؟",
  "sourcesLine": "المصادر: تقرير وزارة الكهرباء السنوي عبر شفق نيوز · المستقلة — 27 أيلول 2026",
  "statPops": [{"value": "52%", "label": "من الكهرباء ضاعت بـ2025", "matchWord": "الضائعات"},
               {"value": "67%", "label": "ضائعات كربلاء — الأعلى", "matchWord": "كربلاء"}]}}

# ═══════════ E · 23:45 · P3 Hajj lottery (region-relevant, personal) ═══════════
slug = f"{D}-e-hajj-lottery-2030"
p = base(slug, "iraq_society", "C", "قرعة الحج", "طلع اسمك؟ نتائج قرعة الحج لأربع مواسم",
  ("BAGHDAD · SEP 27 | IRAQ'S SUPREME AUTHORITY FOR HAJJ AND UMRAH ANNOUNCED THE ELECTRONIC HAJJ LOTTERY RESULTS FOR "
   "2027 (SUPPLEMENTARY), 2028, 2029 AND 2030 (SHAFAQ NEWS; INA; 964) | HEAD SAMI AL-MASOUDI: THIS ROUND IS DEDICATED "
   "TO THE ELDERLY; IRAQ'S LIMITED QUOTA VERSUS APPLICANTS MAKES SELECTION HARD | 7 GOVERNMENT BODIES SUPERVISED; "
   "SOFTWARE TESTED BY AL-MUSTANSIRIYA UNIVERSITY AND THE UNIVERSITY OF TECHNOLOGY; JUDGES FROM THE SUPREME JUDICIAL "
   "COUNCIL ATTENDED | FAKE NAMES REMOVED, PER THE AUTHORITY"))
p["beats"] = [
 beat("النتائج", "القرعة انعلنت: من 2027 لـ2030",
  "الهيئة العليا للحج والعمرة أعلنت اليوم نتائج القرعة الإلكترونية لمواسم 2027 التكميلي و2028 و2029 و2030 (شفق نيوز، واع).",
  "4", "Hajj seasons covered by the electronic lottery: 2027 (supplementary) to 2030",
  "مواسم حج شملتها القرعة الإلكترونية (هيئة الحج والعمرة)",
  [("من", "2027 تكميلي"), ("إلى", "2030"), ("الطريقة", "إلكترونية")], 1, slug,
  ["نتائج قرعة الحج", "لأربع مواسم", "من 2027 لـ2030"], STOCK),
 beat("الأولوية", "كبار السن أولاً",
  "رئيس الهيئة سامي المسعودي قال إن قرعة هذه الأعوام مخصصة لكبار السن، وإن محدودية حصة العراق مقابل أعداد المتقدمين تصعّب الاختيار (واع).",
  "2027", "First season in this lottery round — a supplementary season (Hajj and Umrah Authority)",
  "أول موسم بالقرعة — موسم تكميلي (هيئة الحج والعمرة)",
  [("الفئة", "كبار السن"), ("الحصة", "محدودة"), ("المتقدمون", "أكثر منها")], 2, slug,
  ["الأولوية لكبار السن", "والحصة محدودة", "والمتقدمين كثار"], STOCK),
 beat("الرقابة", "7 جهات وقضاة يراقبون القرعة",
  "حسب الهيئة، أشرفت 7 جهات حكومية وقضاة من مجلس القضاء الأعلى، وفحصت الجامعة المستنصرية والتكنولوجية برنامج القرعة، واستُبعدت أسماء وهمية.",
  "7", "Government bodies that supervised the lottery (Hajj and Umrah Authority)",
  "جهات حكومية أشرفت على القرعة (هيئة الحج والعمرة)",
  [("الفحص", "جامعتان"), ("الإشراف", "قضاة"), ("الأسماء الوهمية", "استُبعدت")], 3, slug,
  ["7 جهات حكومية", "وقضاة يراقبون", "والأسماء الوهمية برّا"], STOCK),
]
p["arabicTicker"] = [
 "الهيئة العليا للحج والعمرة تعلن نتائج القرعة الإلكترونية للأعوام 2027 التكميلية و2028 و2029 و2030 (27 أيلول)",
 "سامي المسعودي: قرعة هذه الأعوام مخصصة لكبار السن ومحدودية حصة العراق تجعل الاختيار صعباً (واع)",
 "7 جهات حكومية وقضاة من مجلس القضاء الأعلى أشرفوا على القرعة (شفق نيوز)",
 "برنامج القرعة خضع للفحص في الجامعة المستنصرية والجامعة التكنولوجية",
 "طلع اسمك أو اسم أحد من أهلك بالقرعة؟"]
p["endQuestion"] = "طلع اسمك أو اسم أحد من أهلك بالقرعة؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "وكالة الأنباء العراقية", "domain": "ina.iq"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """نتائج قرعة الحج في العراق — طلع اسمك؟

أربع مواسم والأولوية لكبار السن.. تأكد من الرابط الرسمي للهيئة فقط.

طلع اسمك أو اسم أحد من أهلك بالقرعة؟

المصادر: شفق نيوز، وكالة الأنباء العراقية، شبكة 964 (27 أيلول 2026)

#العراق #قرعة_الحج #الحج #photonectnews
@photonect.news""",
 "brief": {"kicker": "قرعة الحج", "hookHeadline": "طلع اسمك بقرعة الحج؟",
  "voText": "أعلنت الهيئة العليا للحج والعمرة، اليوم الأحد، نتائج القرعة الإلكترونية للحج لأربعة مواسم، من ألفين وسبعة وعشرين التكميلي حتى ألفين وثلاثين. وقال رئيس الهيئة سامي المسعودي إن قرعة هذه الأعوام مخصصة لكبار السن، وإن محدودية حصة العراق مقارنة بأعداد المتقدمين تجعل الاختيار صعباً. وبحسب الهيئة، أشرفت سبع جهات حكومية وقضاة من مجلس القضاء الأعلى على القرعة، وفُحص برنامجها في جامعتين. طلع اسمك أو اسم أحد من أهلك بالقرعة؟",
  "endQuestion": "طلع اسمك أو اسم أحد من أهلك بالقرعة؟",
  "sourcesLine": "المصادر: شفق نيوز · وكالة الأنباء العراقية · شبكة 964 — 27 أيلول 2026",
  "statPops": [{"value": "4", "label": "مواسم حج بالقرعة", "matchWord": "مواسم"},
               {"value": "7", "label": "جهات حكومية أشرفت", "matchWord": "سبع"}]}}

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
