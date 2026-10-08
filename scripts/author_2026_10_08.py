#!/usr/bin/env python3
"""Author the 2026-10-08 slate: props.json + caption.txt (+ v11-brief.json on a, b, c, d; e = V10.1 control).

Every figure traces to a named source (Shafaq market check; PM office + MoF via Shafaq/964/Rudaw; Pharmacists Syndicate;
CBI media director via 964; Iraqi Airways via Rudaw; Fars via 964; Al-Araby TV via our 10-02 archive; Integrity Commission via 964;
EUAA via Rudaw). Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + gate passes then edit the files on disk —
do NOT re-run this script after that, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_10_08.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-08"
DATE_LABEL = "OCT 08 • 2026"
AR_DATE = "8 تشرين الأول 2026"
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

# ═══════════ A · 18:00 · P1 money (LEAD) — food prices jump, PM defers customs on eggs/chicken/live meat ═══════════
slug = f"{D}-a-food-eggs-93k"
p = base(slug, "iraq_money", "A", "الأسعار", "سلّة بيتك غلت.. والحكومة تؤجل الكمارك",
  ("BAGHDAD · OCT 8 | SHAFAQ NEWS MARKET CHECK: EGG CARTON (12 TRAYS) 84,000 -> 93,000 IQD, 'MAHMOUD' RICE 65,000 -> 72,000, "
   "SUGAR 26,000 -> 30,000 | PM ALI AL-ZAIDI'S OFFICE + MoF (VIA SHAFAQ, 964, RUDAW): CUSTOMS + TAX ON IMPORTED EGGS, CHICKEN, "
   "LIVE MEAT POSTPONED | IRAQ PHARMACISTS SYNDICATE: DRUG PRICING BUILT ON 1,320 IQD/$, ASKS TO KEEP IT FOR MEDICINE IMPORTS"))
p["beats"] = [
 beat("السوق", "صندوق البيض: من 84 إلى 93 ألفاً",
  "بحسب شفق نيوز، ارتفع صندوق البيض (12 طبقة) الخميس من 84 ألف دينار إلى 93 ألفاً، والرز «محمود» من 65 إلى 72 ألفاً، والسكر من 26 إلى 30 ألفاً.",
  "93,000", "IQD per 12-tray egg carton on Thursday, up from 84,000 (Shafaq News market check)", "دينار لصندوق البيض",
  [("الرز «محمود»", "65 ← 72 ألف"), ("السكر", "26 ← 30 ألف"), ("البيض", "+10.7%")], 1, slug,
  ["البيض 93 ألف", "الرز 72 ألف", "السكر 30 ألف"], STOCK),
 beat("قرار الحكومة", "تأجيل الكمارك على البيض والدجاج",
  "وجّه رئيس الوزراء علي الزيدي بتأجيل استيفاء الرسوم الكمركية والضريبة على البيض والدجاج واللحوم الحية المستوردة، ووجهت المالية هيئة الكمارك بالتنفيذ.",
  "3", "Imported staples whose customs + tax are postponed: eggs, chicken, live meat (PM office + MoF via Shafaq / 964 / Rudaw)",
  "مواد أُجّلت كماركها",
  [("البيض", "تأجيل"), ("الدجاج", "تأجيل"), ("اللحوم الحية", "تأجيل")], 2, slug,
  ["الزيدي: تأجيل الكمارك", "بيض ودجاج ولحوم حية", "المالية تبلغ الكمارك"], STOCK),
 beat("الدواء", "الصيادلة: تسعيرة الدواء على 1,320",
  "نقابة صيادلة العراق تقول إن تسعيرة الأدوية مبنية على 1,320 ديناراً للدولار، وتطالب بإبقاء هذا السعر لحوالات استيراد الأدوية ومستلزماتها.",
  "1,320", "IQD per dollar on which Iraq's drug-pricing system is built, per the Pharmacists Syndicate (via Shafaq)",
  "دينار للدولار — أساس تسعيرة الأدوية",
  [("السعر الرسمي الجديد", "1,520"), ("الأكثر تضرراً", "المرضى المزمنون"), ("المطلب", "سعر خاص للأدوية")], 3, slug,
  ["الصيادلة يحذرون", "تسعيرة الدواء على 1,320", "طلب سعر خاص للأدوية"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: صندوق البيض من 84 ألفاً إلى 93 ألف دينار الخميس",
 "الرز «محمود» من 65 إلى 72 ألفاً والسكر من 26 إلى 30 ألفاً",
 "الزيدي يوجه بتأجيل الكمارك والضريبة على البيض والدجاج واللحوم الحية المستوردة",
 "نقابة الصيادلة تطالب بإبقاء سعر الصرف السابق لحوالات استيراد الأدوية",
 "شكد صار صندوق البيض عدكم؟"]
p["endQuestion"] = "شكد صار صندوق البيض عدكم؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "رووداو", "domain": "rudawarabia.net"}, {"name": "نقابة صيادلة العراق", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """أسعار البيض والرز في العراق بعد رفع الدولار — شكد صارت؟

الأسعار تحركت بالسوق، والحكومة ردّت بقرار.. التفاصيل بالفيديو.

شكد صار صندوق البيض عدكم؟

المصادر: شفق نيوز، شبكة 964، رووداو، نقابة صيادلة العراق (8 تشرين الأول 2026)

#أسعار_البيض #الأسعار_في_العراق #سعر_الصرف #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الأسعار", "hookHeadline": "صندوق البيض صار بـ93 ألف",
  "voText": "بعد يوم من تطبيق السعر الرسمي الجديد للدولار، رصدت شفق نيوز ارتفاع صندوق البيض من أربعة وثمانين ألف دينار إلى ثلاثة وتسعين ألفاً، والرز من خمسة وستين ألفاً إلى اثنين وسبعين. وقال تاجر إن بعض شركات المشروبات أوقفت البيع مؤقتاً. ووجّه رئيس الوزراء علي الزيدي اليوم بتأجيل استيفاء الرسوم الكمركية والضريبة على البيض والدجاج واللحوم الحية المستوردة. أما نقابة الصيادلة فحذّرت من أثر سعر الصرف على أسعار الأدوية، وطالبت بإبقاء السعر السابق لحوالات استيرادها. شكد صار صندوق البيض عدكم؟",
  "endQuestion": "شكد صار صندوق البيض عدكم؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 · رووداو · نقابة صيادلة العراق — 8 تشرين الأول 2026",
  "statPops": [{"value": "93,000", "label": "دينار لصندوق البيض (12 طبقة) — شفق نيوز", "matchWord": "وتسعين"},
               {"value": "72,000", "label": "دينار للرز «محمود» بعد 65 ألفاً", "matchWord": "والرز"}]}}


# ═══════════ B · 19:45 · P1 dollar anchor — bourse eases to 166,800; CBI says 1,900 was on the table ═══════════
slug = f"{D}-b-dollar-166800-1900"
p = base(slug, "iraq_money", "B", "سعر الدولار", "الدولار نزل شوية.. والمركزي: الأرقام وصلت 1,900",
  ("BAGHDAD · OCT 8 | SHAFAQ: KIFAH & HARITHIYA THU AM 166,800 IQD/$100 (WED AM 168,500); BAGHDAD SHOPS SELL 167,250, ERBIL SELL 166,350 | "
   "964 LIST 13:25: BAGHDAD SELL 168,000, ERBIL 165,850, BASRA 166,000 | OFFICIAL 152,000 | CBI MEDIA DIRECTOR HAIDAR GHAZI (DIJLA TV VIA 964): "
   "RESERVES DRAWN TO PAY 9M+ EMPLOYEES; FIGURES PROPOSED REACHED 1,900, CBI HELD 1,500"))
p["beats"] = [
 beat("صباح الخميس", "الكفاح: 166,800 صباح الخميس",
  "بحسب شفق نيوز، سجلت بورصتا الكفاح والحارثية صباح الخميس 166,800 دينار لكل 100 دولار، بعد 168,500 صباح الأربعاء.",
  "166,800", "IQD per $100, Kifah & Harithiya, Thursday morning (Shafaq News)", "دينار لكل 100 دولار",
  [("صباح الأربعاء", "168,500"), ("محال بغداد بيع", "167,250"), ("أربيل بيع", "166,350")], 1, slug,
  ["الكفاح 166,800", "صباح الأربعاء 168,500", "أربيل 166,350"], STOCK),
 beat("الفجوة", "فوق الرسمي بـ14,800 دينار",
  "السعر الرسمي 152 ألفاً لكل 100 دولار، أي أن سعر الكفاح الصباحي أعلى بـ14,800 (محتسب). وفي قائمة شبكة 964 ظهراً: أربيل 165,850 والبصرة 166,000.",
  "14,800", "IQD per $100 above the official 152,000 (Kifah 166,800 − 152,000, computed)", "دينار فوق الرسمي (محتسب)",
  [("الرسمي", "152,000"), ("أربيل ظهراً", "165,850"), ("البصرة ظهراً", "166,000")], 2, slug,
  ["الرسمي 152 ألف", "الفرق 14,800 (محتسب)", "البصرة 166 ألف"], STOCK),
 beat("كواليس القرار", "المركزي: مقترحات وصلت 1,900",
  "مدير إعلام البنك المركزي حيدر غازي: الحكومة استهلكت جزءاً من الاحتياطي لتأمين رواتب أكثر من 9 ملايين موظف، وأرقام طُرحت وصلت إلى 1,900 دينار للدولار.",
  "1,900", "IQD per dollar — highest figure proposed before the CBI held 1,500 (CBI media director on Dijla TV, via 964)",
  "دينار للدولار — أعلى رقم طُرح",
  [("ما اعتمده المركزي", "1,500"), ("الموظفون", "+9 ملايين"), ("المصدر", "قناة دجلة")], 3, slug,
  ["مقترحات حتى 1,900", "المركزي ثبّت 1,500", "رواتب 9 ملايين موظف"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الكفاح والحارثية صباح الخميس 166,800 دينار لكل 100 دولار",
 "صباح الأربعاء كان 168,500 (شفق نيوز)",
 "شبكة 964 ظهراً: أربيل 165,850 والبصرة 166,000",
 "المركزي: أرقام طُرحت وصلت إلى 1,900 دينار للدولار",
 "عندك دولار مخزون بالبيت؟"]
p["endQuestion"] = "عندك دولار مخزون بالبيت؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "البنك المركزي العراقي", "domain": "cbi.iq"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار اليوم في بغداد — نزل لو بعده؟

البورصة تحركت ثاني يوم، والمركزي كشف رقم ما توقعه أحد.. التفاصيل بالفيديو.

عندك دولار مخزون بالبيت؟

المصادر: شفق نيوز، شبكة 964، البنك المركزي العراقي عبر قناة دجلة (7 و8 تشرين الأول 2026)

#سعر_الدولار_اليوم #بورصة_الكفاح #الدينار_العراقي #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "سعر الدولار", "hookHeadline": "الدولار نزل.. بس شوية",
  "voText": "سجلت بورصتا الكفاح والحارثية صباح الخميس مئة وستة وستين ألفاً وثمانمئة دينار لكل مئة دولار، بحسب شفق نيوز، بعد مئة وثمانية وستين ألفاً وخمسمئة صباح الأربعاء. وفي قائمة شبكة تسعة ستة أربعة، سجلت أربيل والبصرة نحو مئة وستة وستين ألفاً. وبذلك يبقى سعر الكفاح أعلى من السعر الرسمي بأربعة عشر ألفاً وثمانمئة دينار. وقال مدير إعلام البنك المركزي حيدر غازي إن الحكومة استهلكت جزءاً من الاحتياطي لتأمين رواتب أكثر من تسعة ملايين موظف، وإن أرقاماً طُرحت وصلت إلى ألف وتسعمئة دينار للدولار. عندك دولار مخزون بالبيت؟",
  "endQuestion": "عندك دولار مخزون بالبيت؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 · البنك المركزي عبر قناة دجلة — 7 و8 تشرين الأول 2026",
  "statPops": [{"value": "166,800", "label": "دينار لكل 100 دولار — الكفاح صباح الخميس", "matchWord": "والحارثية"},
               {"value": "1,900", "label": "دينار للدولار — أعلى رقم طُرح (البنك المركزي)", "matchWord": "وتسعمئة"}]}}


# ═══════════ C · 21:15 · P2 Iran travel — Iraqi Airways resumes daily Najaf flights to Iran ═══════════
slug = f"{D}-c-iraqi-airways-iran-daily"
p = base(slug, "mena_geo", "A", "السفر", "رحلات يومية من النجف لطهران ومشهد وأصفهان",
  ("NAJAF · OCT 8 | IRAQI AIRWAYS STATEMENT (VIA RUDAW): IRAN FLIGHTS RESUME — DAILY SCHEDULED FLIGHTS NAJAF -> TEHRAN, MASHHAD, ISFAHAN; "
   "IRAN FLIGHTS HALTED SINCE EARLY MARCH | FARS (VIA 964): FIRST FLIGHT FROM NAJAF LANDED AT IMAM KHOMEINI AIRPORT THU MORNING, ROUND-TRIP SERVICE | "
   "AL-ARABY TV (OCT 2): US TREASURY LICENSE FOR IRAQI AIRWAYS VIA NAJAF ONLY, EXPIRES OCT 28"))
p["beats"] = [
 beat("الوجهات", "النجف ← طهران ومشهد وأصفهان",
  "بيان الخطوط الجوية العراقية، بحسب رووداو: رحلات يومية منتظمة من مطار النجف الدولي إلى طهران ومشهد وأصفهان، بعد توقف رحلاتها إلى إيران منذ مطلع آذار.",
  "3", "Iranian destinations served daily from Najaf: Tehran, Mashhad, Isfahan (Iraqi Airways via Rudaw)", "وجهات يومية من النجف",
  [("طهران", "يومياً"), ("مشهد", "يومياً"), ("أصفهان", "يومياً")], 1, slug,
  ["الخطوط العراقية ترجع لإيران", "طهران · مشهد · أصفهان", "من مطار النجف"], STOCK),
 beat("أول رحلة", "هبطت صباح اليوم في مطار الخميني",
  "وكالة فارس الإيرانية، عبر شبكة 964: أول رحلة دولية من النجف هبطت صباح الخميس في مطار الإمام الخميني بطهران، بنظام الذهاب والعودة.",
  "7", "Months since Iraqi Airways halted Iran flights (early March -> October, computed from the airline statement via Rudaw)",
  "أشهر من التوقف (محتسب)",
  [("التوقف", "منذ مطلع آذار"), ("الاستئناف", "8 تشرين الأول"), ("النظام", "ذهاب وعودة")], 2, slug,
  ["أول رحلة هبطت بطهران", "ذهاب وعودة", "بعد توقف منذ آذار"], STOCK),
 beat("لمن؟", "زيارة وعلاج ودراسة",
  "تقول الشركة إن الرحلات لخدمة السفر الديني والعلاجي والدراسي. وكان التلفزيون العربي أفاد في 2 تشرين الأول بأن الترخيص الأميركي لهذه الرحلات ينتهي في 28 تشرين الأول.",
  "28", "October — expiry of the US Treasury license for Iraqi Airways' Najaf-Iran flights (Al-Araby TV, Oct 2)",
  "تشرين الأول — نهاية الترخيص الأميركي",
  [("ديني", "زيارة"), ("علاجي", "مستشفيات"), ("دراسي", "جامعات")], 3, slug,
  ["زيارة · علاج · دراسة", "ترخيص أميركي لشهر", "ينتهي 28 تشرين الأول"], STOCK),
]
p["arabicTicker"] = [
 "الخطوط الجوية العراقية تستأنف رحلاتها إلى إيران من مطار النجف (رووداو)",
 "رحلات يومية منتظمة إلى طهران ومشهد وأصفهان",
 "فارس عبر 964: أول رحلة من النجف هبطت في مطار الإمام الخميني صباح الخميس",
 "التلفزيون العربي (2 تشرين الأول): الترخيص الأميركي ينتهي في 28 تشرين الأول",
 "سافرت لمشهد بالطيارة قبل؟"]
p["endQuestion"] = "سافرت لمشهد بالطيارة قبل؟"
p["sources"] = [{"name": "رووداو", "domain": "rudawarabia.net"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "التلفزيون العربي", "domain": "alaraby.com"}]
SLATE[slug] = {"props": p, "caption": """رحلات العراق إلى إيران رجعت — من وين وإلى وين؟

الخطوط العراقية رجعت تطير يومياً من النجف.. الوجهات والتفاصيل بالفيديو.

سافرت لمشهد بالطيارة قبل؟

المصادر: الخطوط الجوية العراقية عبر رووداو، وكالة فارس عبر شبكة 964، التلفزيون العربي (2 و8 تشرين الأول 2026)

#الخطوط_الجوية_العراقية #مطار_النجف #مشهد #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "السفر", "hookHeadline": "النجف ← طهران ومشهد.. يومياً",
  "voText": "أعلنت الخطوط الجوية العراقية اليوم الخميس استئناف رحلاتها إلى إيران، وقالت في بيان نقلته رووداو إنها ستسيّر رحلات يومية منتظمة من مطار النجف إلى طهران ومشهد وأصفهان، بعد توقف منذ مطلع آذار. وذكرت وكالة فارس الإيرانية أن أول رحلة من النجف هبطت صباح اليوم في مطار الإمام الخميني، بنظام الذهاب والعودة. وبحسب الشركة، تخدم الرحلات السفر الديني والعلاجي والدراسي. وكان التلفزيون العربي قد أفاد بأن الترخيص الأميركي لهذه الرحلات ينتهي في الثامن والعشرين من تشرين الأول. سافرت لمشهد بالطيارة قبل؟",
  "endQuestion": "سافرت لمشهد بالطيارة قبل؟",
  "sourcesLine": "المصادر: الخطوط الجوية العراقية عبر رووداو · وكالة فارس عبر شبكة 964 · التلفزيون العربي — 2 و8 تشرين الأول 2026",
  "statPops": [{"value": "3", "label": "وجهات يومية: طهران · مشهد · أصفهان", "matchWord": "وأصفهان"},
               {"value": "28", "label": "تشرين الأول — نهاية الترخيص الأميركي (التلفزيون العربي)", "matchWord": "والعشرين"}]}}


# ═══════════ D · 22:30 · P1 corruption × electricity — Karbala meter bribe ═══════════
slug = f"{D}-d-karbala-meter-bribe"
p = base(slug, "iraq_money", "B", "النزاهة", "رشوة لتفادي غرامة كهرباء بـ10 ملايين",
  ("KARBALA · OCT 7 | FEDERAL INTEGRITY COMMISSION STATEMENT (VIA 964): KARBALA INVESTIGATION OFFICE AMBUSH — TWO ELECTRICITY-DIRECTORATE "
   "EMPLOYEES CAUGHT RECEIVING A BRIBE FROM A CITIZEN TO HELP HIM AVOID A 10M IQD FINE; DEAL WAS TO TAMPER WITH HIS HOME METER; "
   "THIRD PARTNER ARRESTED LATER | KARBALA INTEGRITY INVESTIGATION JUDGE ORDERED ALL 3 DETAINED UNDER RCC RESOLUTION 160/1983 | NO CONVICTION"))
p["beats"] = [
 beat("الكمين", "غرامة 10 ملايين.. ورشوة لتفاديها",
  "هيئة النزاهة: مكتب تحقيق كربلاء ضبط موظفَين في دائرة كهرباء المحافظة، بحسب الهيئة، متلبسَين بتسلّم رشوة من مواطن مقابل تفادي غرامة قيمتها 10 ملايين دينار.",
  "10", "Million IQD — the electricity fine the citizen was allegedly helped to avoid (Integrity Commission via 964)",
  "ملايين دينار — قيمة الغرامة",
  [("المكان", "كهرباء كربلاء"), ("العملية", "كمين"), ("المتهمون", "موظفون")], 1, slug,
  ["كهرباء كربلاء", "غرامة 10 ملايين", "رشوة لتفاديها"], STOCK),
 beat("المقياس", "الاتفاق: التلاعب بمقياس البيت",
  "تقول الهيئة إن الاتفاق كان على التلاعب بمقياس الكهرباء في منزل المواطن، وإن الموظفَين أقرّا خلال التحقيق بوجود شريك ثالث ضُبط لاحقاً.",
  "3", "Electricity employees detained: two caught in the ambush + a third partner arrested later (Integrity Commission via 964)",
  "موظفين متهمين",
  [("ضُبطوا بالكمين", "2"), ("ضُبط لاحقاً", "1"), ("الأداة", "مقياس الكهرباء")], 2, slug,
  ["التلاعب بالمقياس", "موظفان بالكمين", "وشريك ثالث"], STOCK),
 beat("القضاء", "توقيف الثلاثة.. ولا إدانة بعد",
  "عُرض المتهمون الثلاثة على قاضي محكمة التحقيق المختصة بقضايا النزاهة في كربلاء، فقرر توقيفهم وفق القرار 160 لسنة 1983. ولم تصدر إدانة.",
  "160", "RCC Resolution 160 of 1983 — legal basis for the detention order (Integrity Commission via 964)", "رقم القرار — لسنة 1983",
  [("القرار", "160 لسنة 1983"), ("الإجراء", "توقيف"), ("الحكم", "لم يصدر")], 3, slug,
  ["قاضي التحقيق يوقفهم", "القرار 160 لسنة 1983", "ولا إدانة بعد"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة: ضبط موظفَين في كهرباء كربلاء بحالة تسلّم رشوة",
 "الرشوة مقابل تفادي غرامة 10 ملايين دينار عبر التلاعب بمقياس منزل",
 "شريك ثالث ضُبط لاحقاً — والقاضي قرر توقيف الثلاثة",
 "التوقيف وفق القرار 160 لسنة 1983 — ولم تصدر إدانة",
 "شكد تدفع فاتورة الوطنية بالشهر؟"]
p["endQuestion"] = "شكد تدفع فاتورة الوطنية بالشهر؟"
p["sources"] = [{"name": "هيئة النزاهة الاتحادية", "domain": "nazaha.iq"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """غرامة الكهرباء في كربلاء — شنو كشفت هيئة النزاهة؟

كمين، مقياس كهرباء، وغرامة بالملايين.. والمتهمون موقوفون. التفاصيل بالفيديو.

شكد تدفع فاتورة الوطنية بالشهر؟

المصادر: هيئة النزاهة الاتحادية عبر شبكة 964 (7 تشرين الأول 2026)

#هيئة_النزاهة #كربلاء #الكهرباء #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "رشوة لتفادي غرامة 10 ملايين",
  "voText": "أعلنت هيئة النزاهة الاتحادية أن مكتب تحقيق كربلاء ضبط موظفَين في دائرة كهرباء المحافظة، بحسب الهيئة، متلبسَين بتسلّم رشوة من مواطن، مقابل تفادي غرامة قيمتها عشرة ملايين دينار. وتقول الهيئة إن الاتفاق كان على التلاعب بمقياس الكهرباء في منزله، وإن الموظفَين أقرّا بشريك ثالث ضُبط لاحقاً. وقرر قاضي محكمة تحقيق النزاهة في كربلاء توقيف المتهمين الثلاثة، وفق القرار مئة وستين لسنة ألف وتسعمئة وثلاثة وثمانين، ولم تصدر إدانة بعد. شكد تدفع فاتورة الوطنية بالشهر؟",
  "endQuestion": "شكد تدفع فاتورة الوطنية بالشهر؟",
  "sourcesLine": "المصادر: هيئة النزاهة الاتحادية عبر شبكة 964 — 7 تشرين الأول 2026",
  "statPops": [{"value": "10M", "label": "مليون دينار — قيمة الغرامة", "matchWord": "ملايين"},
               {"value": "3", "label": "موظفين موقوفين على ذمة التحقيق", "matchWord": "الثلاثة"}]}}


# ═══════════ E · 23:45 · P3 migration (V10.1 CONTROL) — EU rejects two-thirds of Iraqi asylum claims ═══════════
slug = f"{D}-e-eu-asylum-66-percent"
p = base(slug, "region_life", "C", "اللجوء", "أوروبا رفضت ثلثي طلبات لجوء العراقيين",
  ("EUAA DATA TO RUDAW (OCT 8): H1 2026 — 7,610 IRAQI ASYLUM DECISIONS IN EU+ (EU, NORWAY, SWITZERLAND); 5,069 FULLY REJECTED (66.61%) | "
   "REFUGEE STATUS 1,586 (20.84%), HUMANITARIAN/NATIONAL 548 (7.20%), SUBSIDIARY 407 (5.35%) | 4,670 NEW IRAQI APPLICATIONS, -19% Y/Y | "
   "NO SEPARATE TREATMENT FOR KURDISTAN REGION APPLICANTS"))
p["beats"] = [
 beat("القرارات", "5,069 رفضاً من 7,610 قرارات",
  "وكالة اللجوء الأوروبية لرووداو: في النصف الأول من 2026، بُتّ في 7,610 طلبات لعراقيين في الاتحاد الأوروبي والنرويج وسويسرا، رُفض منها 5,069 بالكامل.",
  "66.61%", "Share of Iraqi asylum decisions fully rejected in EU+ in H1 2026 (EUAA via Rudaw)", "من الطلبات رُفضت بالكامل",
  [("قرارات", "7,610"), ("رفض كامل", "5,069"), ("الفترة", "النصف الأول 2026")], 1, slug,
  ["وكالة اللجوء الأوروبية", "7,610 قرار", "66.61% رفض"], STOCK),
 beat("الطلبات الجديدة", "4,670 عراقياً قدّموا.. بانخفاض 19%",
  "بحسب الوكالة، قدّم 4,670 عراقياً طلبات لجوء في الدول الأوروبية خلال الأشهر الستة الأولى من العام، بانخفاض 19% عن الفترة نفسها من العام الماضي.",
  "4,670", "New Iraqi asylum applications in EU+ in H1 2026, down 19% year on year (EUAA via Rudaw)", "طلب لجوء جديد",
  [("التغير السنوي", "-19%"), ("الدول", "الاتحاد + النرويج + سويسرا"), ("الفترة", "6 أشهر")], 2, slug,
  ["4,670 طلب جديد", "انخفاض 19%", "خلال 6 أشهر"], STOCK),
 beat("من قُبل؟", "1,586 حصلوا على صفة لاجئ",
  "حصل 1,586 على صفة اللاجئ (20.84%)، و548 على حماية إنسانية ووطنية، و407 على حماية ثانوية. وتقول الوكالة إن طلبات إقليم كوردستان لا تُعامل بشكل منفصل.",
  "1,586", "Iraqis granted full refugee status in EU+ in H1 2026, 20.84% of decisions (EUAA via Rudaw)", "حصلوا على صفة اللاجئ",
  [("صفة لاجئ", "20.84%"), ("حماية إنسانية", "548"), ("حماية ثانوية", "407")], 3, slug,
  ["1,586 صفة لاجئ", "548 حماية إنسانية", "407 حماية ثانوية"], STOCK),
]
p["arabicTicker"] = [
 "وكالة اللجوء الأوروبية لرووداو: رفض 66.61% من طلبات لجوء العراقيين في النصف الأول من 2026",
 "7,610 قراراً بينها 5,069 رفضاً كاملاً",
 "4,670 طلباً جديداً بانخفاض 19% عن العام الماضي",
 "1,586 حصلوا على صفة اللاجئ و548 حماية إنسانية و407 حماية ثانوية",
 "عندك أحد من أهلك قدّم لجوء بأوروبا؟"]
p["endQuestion"] = "عندك أحد من أهلك قدّم لجوء بأوروبا؟"
p["sources"] = [{"name": "وكالة الاتحاد الأوروبي للجوء", "domain": "euaa.europa.eu"}, {"name": "رووداو", "domain": "rudawarabia.net"}]
SLATE[slug] = {"props": p, "caption": """اللجوء إلى أوروبا للعراقيين 2026 — كم طلب انقبل؟

أرقام جديدة من وكالة اللجوء الأوروبية.. النسبة بالفيديو.

عندك أحد من أهلك قدّم لجوء بأوروبا؟

المصادر: وكالة الاتحاد الأوروبي للجوء عبر رووداو (8 تشرين الأول 2026)

#اللجوء #أوروبا #العراقيين_في_الخارج #العراق #photonectnews
@photonect.news""", "brief": None}


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
