#!/usr/bin/env python3
"""Author the 2026-10-14 slate: props.json + caption.txt (+ v11-brief.json on a, b, c, d; e = V10.1 control).

Every figure traces to a named source saved in the session scratchpad (Shafaq full-text RSS, 964 + Rudaw article pages; raw copies in scratchpad/art/).
Computed figures carry (محتسب). PRE-copywriter draft: do NOT re-run after the Opus copywriter/gate edits.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-14"
DATE_LABEL = "OCT 14 • 2026"
AR_DATE = "14 تشرين الأول 2026"
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


# ═══════════ A · 18:00 · P1 prices (LEAD) — customs duties lifted on imported food + medicine ═══════════
slug = f"{D}-a-customs-food-medicine"
p = base(slug, "iraq_money", "A", "الأسعار", "أكلك ودواك المستورد.. صار بلا كمرك",
  ("BAGHDAD · OCT 13 | IRAQ'S CABINET (23RD REGULAR SESSION, CHAIRED BY PM ALI AL-ZAIDI) EXEMPTED IMPORTED FOOD AND MEDICINES FROM CUSTOMS DUTIES, "
   "EFFECTIVE RETROACTIVELY FROM 7 OCTOBER 2026 (PM MEDIA OFFICE VIA SHAFAQ, 964, RUDAW) | STATED AIM: PROTECT FOOD AND HEALTH SECURITY | "
   "LAST THURSDAY ZAIDI ORDERED CUSTOMS + TAX ON IMPORTED EGGS, CHICKEN AND LIVE MEAT POSTPONED | SHAFAQ: FOOD PRICES ROSE NOTICEABLY AFTER THE OFFICIAL RATE WAS RAISED TO 1,520 IQD/$"))
p["beats"] = [
 beat("القرار", "مجلس الوزراء: لا رسوم كمركية على الأغذية والأدوية",
  "قرر مجلس الوزراء مساء الثلاثاء، برئاسة علي الزيدي، إعفاء المواد الغذائية والأدوية المستوردة من الرسوم الكمركية، «لحماية الأمن الغذائي والصحي» (شفق نيوز، 964، رووداو).",
  "0", "Customs duty on imported food and medicines after the cabinet decision of 13 October (PM media office via Shafaq / 964 / Rudaw)", "رسوم كمركية على الأغذية والأدوية المستوردة",
  [("يشمل", "الأغذية"), ("ويشمل", "الأدوية"), ("الجلسة", "23")], 1, slug,
  ["إعفاء من الرسوم الكمركية", "الأغذية والأدوية المستوردة", "«لحماية الأمن الغذائي والصحي»"], GEN),
 beat("التوقيت", "بأثر رجعي.. من 7 تشرين الأول",
  "الإعفاء يسري ابتداءً من 7 تشرين الأول، اليوم الذي بدأ فيه السعر الرسمي الجديد 1,520 ديناراً للدولار. وشفق نيوز رصدت ارتفاعاً ملحوظاً بأسعار مواد غذائية بعده.",
  "7", "October — the exemption applies retroactively from 7 October 2026, the first day of the new official rate (PM media office)", "تشرين الأول — بداية الإعفاء بأثر رجعي",
  [("يبدأ من", "7 تشرين الأول"), ("السعر الرسمي", "1,520"), ("الأسعار", "ارتفعت")], 2, slug,
  ["يسري من 7 تشرين الأول", "يوم بدء السعر الرسمي 1,520", "والأسعار ارتفعت بعده"], GEN),
 beat("قبلها", "الخميس الماضي: البيض والدجاج أولاً",
  "وكان الزيدي وجّه الخميس الماضي بتأجيل الرسوم الكمركية والضريبة على البيض والدجاج واللحوم الحية المستوردة، لتوفيرها «بأسعار مناسبة» (شفق نيوز).",
  "1,520", "IQD per dollar — the new official rate in force since 7 October (CBI)", "دينار للدولار — السعر الرسمي الجديد",
  [("البيض", "تأجيل الرسوم"), ("الدجاج", "تأجيل الرسوم"), ("اللحوم الحية", "تأجيل الرسوم")], 3, slug,
  ["الخميس: تأجيل رسوم البيض والدجاج", "واللحوم الحية المستوردة", "والثلاثاء: كل الأغذية والأدوية"], COMMONS),
]
p["arabicTicker"] = [
 "مجلس الوزراء يعفي المواد الغذائية والأدوية المستوردة من الرسوم الكمركية (شفق نيوز، 964، رووداو)",
 "الإعفاء يسري بأثر رجعي ابتداءً من 7 تشرين الأول 2026",
 "الهدف بحسب البيان الحكومي: حماية الأمن الغذائي والصحي",
 "الخميس الماضي: تأجيل الرسوم والضريبة على البيض والدجاج واللحوم الحية المستوردة",
 "تشتري دواء مستورد كل شهر؟",
]
p["endQuestion"] = "تشتري دواء مستورد كل شهر؟"
p["sources"] = [{"name": "مكتب رئيس الوزراء", "domain": "pmo.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "شبكة 964", "domain": "964media.com"}, {"name": "رووداو", "domain": "rudawarabia.net"}]
SLATE[slug] = (p, {
 "kicker": "الأسعار", "hookHeadline": "أكلك ودواك المستورد.. بلا كمرك",
 "voText": ("قرر مجلس الوزراء مساء الثلاثاء، في جلسة برئاسة علي الزيدي، إعفاء المواد الغذائية والأدوية المستوردة من الرسوم الكمركية، بهدف حماية الأمن الغذائي والصحي بحسب البيان الحكومي. "
            "ويسري الإعفاء بأثر رجعي من السابع من تشرين الأول، وهو اليوم الذي بدأ فيه السعر الرسمي الجديد، ألف وخمسمئة وعشرون ديناراً للدولار، "
            "بعدما رصدت شفق نيوز ارتفاعاً ملحوظاً في أسعار مواد غذائية. وكان الزيدي قد وجّه الخميس الماضي بتأجيل الرسوم على البيض والدجاج واللحوم الحية المستوردة. "
            "تشتري دواء مستورد كل شهر؟"),
 "endQuestion": "تشتري دواء مستورد كل شهر؟",
 "sourcesLine": "المصادر: مكتب رئيس الوزراء · شفق نيوز · شبكة 964 · رووداو — 13 و14 تشرين الأول 2026",
 "statPops": [{"value": "0%", "label": "رسوم كمركية على الأغذية والأدوية المستوردة", "matchWord": "الكمركية"},
              {"value": "1,520", "label": "دينار للدولار — السعر الرسمي الجديد", "matchWord": "وعشرون"}],
}, """إعفاء الأغذية والأدوية من الكمرك في العراق — شنو يعني لجيبك؟

القرار، تاريخه، وشنو صار قبله بأسبوع.. بالفيديو.

تشتري دواء مستورد كل شهر؟

المصادر: مكتب رئيس الوزراء عبر شفق نيوز، شبكة 964، رووداو (13 و14 تشرين الأول 2026)

#الرسوم_الكمركية #الأسعار #الأدوية #العراق #photonectnews
@photonect.news
""")

# ═══════════ B · 19:45 · P1 dollar anchor — back up to 167,000, gap over official widens to 15,000 ═══════════
slug = f"{D}-b-dollar-167000-rebound"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار رجع يصعد: 167 ألف",
  ("BAGHDAD · OCT 14 | SHAFAQ: KIFAH/HARITHIYA 167,000 IQD PER $100 WEDNESDAY MORNING (VS 165,600 TUESDAY MORNING, 166,250 TUESDAY CLOSE); "
   "BAGHDAD SHOPS SELL 167,500 / BUY 166,500; ERBIL SELL 166,500 | 964: BAGHDAD SELL 167,500, ERBIL SELL 166,500, BASRA SELL 166,500; OFFICIAL RATE 152,000 | "
   "SUNDAY MORNING (SHAFAQ, OUR OCT 11 REEL): 163,300 | GAP OVER OFFICIAL 11,300 → 15,000 (COMPUTED, MORNING VS MORNING)"))
p["beats"] = [
 beat("البورصة", "الكفاح والحارثية: 167,000 صباح الأربعاء",
  "شفق نيوز: سجلت بورصتا الكفاح والحارثية 167,000 دينار لكل 100 دولار صباح الأربعاء، بعد 165,600 صباح الثلاثاء. محال بغداد تبيع بـ167,500 (شفق، 964).",
  "167,000", "IQD per $100 at Kifah/Harithiya on Wednesday morning, from 165,600 Tuesday morning (Shafaq News)", "دينار لكل 100 دولار — الكفاح صباح الأربعاء",
  [("الثلاثاء صباحاً", "165,600"), ("بيع المحال", "167,500"), ("أربيل بيع", "166,500")], 1, slug,
  ["الكفاح: 167,000 صباح الأربعاء", "بعد 165,600 الثلاثاء", "المحال تبيع بـ167,500"], GEN),
 beat("الارتداد", "الأحد 163,300.. والأربعاء 167,000",
  "صباح الأحد سجلت الكفاح 163,300 (شفق نيوز). خلال ثلاثة أيام صعد السعر 3,700 دينار لكل 100 دولار (محتسب، صباح مقابل صباح).",
  "3,700", "IQD per $100 rise from Sunday morning (163,300) to Wednesday morning (167,000) — computed from Shafaq figures", "دينار ارتفاع منذ صباح الأحد (محتسب)",
  [("الأحد صباحاً", "163,300"), ("الأربعاء صباحاً", "167,000"), ("المدة", "3 أيام")], 2, slug,
  ["الأحد: 163,300", "الأربعاء: 167,000", "+3,700 بثلاثة أيام"], GEN),
 beat("الفجوة", "15 ألف دينار فوق السعر الرسمي",
  "السعر الرسمي للبنك المركزي 152,000 دينار لكل 100 دولار (964). الفرق عن السوق صار 15,000 دينار، بعد 11,300 صباح الأحد (محتسب).",
  "15,000", "IQD above the official 152,000 per $100 on Wednesday morning, up from 11,300 on Sunday morning (computed from Shafaq / 964 figures)", "دينار فوق الرسمي لكل 100 دولار (محتسب)",
  [("الرسمي", "152,000"), ("السوق", "167,000"), ("الأحد", "11,300")], 3, slug,
  ["الرسمي: 152,000", "الفرق صار 15,000", "بعد 11,300 الأحد"], COMMONS),
]
p["arabicTicker"] = [
 "شفق نيوز: الكفاح والحارثية 167,000 دينار لكل 100 دولار صباح الأربعاء بعد 165,600 صباح الثلاثاء",
 "محال بغداد: بيع 167,500 | أربيل: بيع 166,500 | البصرة: بيع 166,500 (964)",
 "السعر الرسمي: 152,000 دينار لكل 100 دولار — الفرق 15,000 (محتسب)",
 "صباح الأحد كان 163,300 — ارتفاع 3,700 خلال ثلاثة أيام (محتسب)",
 "بكم صرفت الدولار آخر مرة؟",
]
p["endQuestion"] = "بكم صرفت الدولار آخر مرة؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "البنك المركزي العراقي", "domain": "cbi.iq"}]
SLATE[slug] = (p, {
 "kicker": "الدولار اليوم", "hookHeadline": "الدولار رجع يصعد.. 167 ألف",
 "voText": ("سجلت بورصتا الكفاح والحارثية في بغداد صباح الأربعاء مئة وسبعة وستين ألف دينار لكل مئة دولار، بحسب شفق نيوز، بعد مئة وخمسة وستين ألفاً وستمئة صباح الثلاثاء، "
            "ومحال الصيرفة تبيع بمئة وسبعة وستين ألفاً وخمسمئة. وصباح الأحد كان السعر مئة وثلاثة وستين ألفاً وثلاثمئة، أي أن الدولار صعد ثلاثة آلاف وسبعمئة دينار خلال ثلاثة أيام. "
            "وبذلك اتسع الفرق عن السعر الرسمي، مئة واثنين وخمسين ألفاً، إلى خمسة عشر ألف دينار. بكم صرفت الدولار آخر مرة؟"),
 "endQuestion": "بكم صرفت الدولار آخر مرة؟",
 "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 11 و14 تشرين الأول 2026",
 "statPops": [{"value": "167,000", "label": "دينار لكل 100 دولار — الكفاح صباح الأربعاء", "matchWord": "الكفاح"},
              {"value": "15,000", "label": "دينار فوق السعر الرسمي (محتسب)", "matchWord": "اتسع"}],
}, """سعر الدولار في العراق اليوم — رجع يصعد؟

البورصة، المحال، والفرق عن السعر الرسمي.. بالفيديو.

بكم صرفت الدولار آخر مرة؟

المصادر: شفق نيوز، شبكة 964 (14 تشرين الأول 2026)

#سعر_الدولار #الدينار_العراقي #العراق #photonectnews
@photonect.news
""")

# ═══════════ C · 21:15 · P2 Iraq–Jordan oil — Jordan lost Kirkuk crude while barrels go to Ceyhan ═══════════
slug = f"{D}-c-jordan-kirkuk-oil"
p = base(slug, "mena_economy", "A", "العراق والأردن", "نفط كركوك ما يوصل الأردن.. ليش؟",
  ("BAGHDAD · OCT 14 | 964: IRAQI KIRKUK CRUDE SUPPLY TO JORDAN HALTED SINCE EARLY THIS YEAR; OIL MINISTRY CITES INSUFFICIENT KIRKUK LIGHT AND BASRA MEDIUM UNSUITED TO JORDANIAN REFINERIES | "
   "SOMO DATA (VIA 964): ~1.76M BARRELS OF KIRKUK CRUDE TO TURKEY'S CEYHAN IN AUGUST (~56K BPD) + 2.17M BARRELS OF KURDISTAN OIL | JORDAN USED TO GET 10-15K BPD AT BRENT MINUS $16: "
   "$7.75 TRANSPORT, $3.40 QUALITY, $4.76 JORDANIAN TREASURY SAVING (964; SHAFAQ CITING JORDANIAN OFFICIAL FIGURES) | EXPERT SADIQ AL-RIKABI (964): DEEP DISCOUNT QUESTIONS THE DEAL'S FEASIBILITY"))
p["beats"] = [
 beat("التوقف", "تجهيز الأردن متوقف منذ بداية السنة",
  "شبكة 964: نفط كركوك للأردن متوقف منذ مطلع العام. وزارة النفط تقول إن خام كركوك الخفيف غير متوفر بالكميات المطلوبة، وخام البصرة لا يناسب المصافي الأردنية.",
  "15,000", "Barrels per day of Kirkuk crude Jordan used to receive (upper bound of 10,000-15,000, via 964 / Shafaq)", "برميل يومياً كان يصل الأردن (الحد الأعلى)",
  [("الكمية", "10–15 ألف ب/ي"), ("التوقف", "مطلع 2026"), ("السبب الرسمي", "نقص الخام")], 1, slug,
  ["نفط كركوك للأردن متوقف", "وزارة النفط: الكميات غير متوفرة", "وخام البصرة لا يناسب مصافيه"], GEN),
 beat("جيهان", "بينما 1.76 مليون برميل من كركوك راحت لتركيا",
  "بيانات «سومو» عبر 964: نحو 1.76 مليون برميل من خام كركوك صُدّرت إلى جيهان التركي في آب، بمعدل يقارب 56 ألف برميل يومياً.",
  "1.76M", "Barrels of Kirkuk crude exported to Turkey's Ceyhan in August, per SOMO data (via 964)", "برميل من خام كركوك إلى جيهان في آب — سومو",
  [("آب", "1.76 مليون برميل"), ("المعدل", "~56 ألف ب/ي"), ("نفط الإقليم", "2.17 مليون")], 2, slug,
  ["1.76 مليون برميل لجيهان", "بآب وحده", "نحو 56 ألف برميل يومياً"], GEN),
 beat("المعادلة", "برنت ناقص 16 دولاراً.. وين يروح الخصم؟",
  "العقد الأردني: برنت ناقص 16 دولاراً، منها 7.75 نقل و3.40 فرق نوعية و4.76 وفر للخزينة الأردنية (964، شفق). الخبير صادق الركابي يرى أن الخصم يطرح تساؤلاً عن جدواه.",
  "$16", "Per-barrel discount below Brent in the Iraq–Jordan crude formula (964 / Shafaq, citing Jordanian official figures)", "دولاراً خصم للبرميل عن برنت",
  [("النقل", "7.75$"), ("فرق النوعية", "3.40$"), ("وفر الأردن", "4.76$")], 3, slug,
  ["برنت ناقص 16 دولاراً", "7.75 نقل و3.40 نوعية", "و4.76 وفر للخزينة الأردنية"], GEN),
]
p["arabicTicker"] = [
 "شبكة 964: تجهيز الأردن بنفط كركوك متوقف منذ مطلع العام",
 "وزارة النفط: خام كركوك الخفيف غير متوفر بالكميات المطلوبة وخام البصرة لا يناسب المصافي الأردنية",
 "سومو: نحو 1.76 مليون برميل من خام كركوك إلى جيهان التركي في آب",
 "معادلة الأردن: برنت ناقص 16 دولاراً — 7.75 نقل، 3.40 نوعية، 4.76 وفر للخزينة الأردنية",
 "كنت تعرف بخصم الـ16 دولار؟",
]
p["endQuestion"] = "كنت تعرف بخصم الـ16 دولار؟"
p["sources"] = [{"name": "شبكة 964", "domain": "964media.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "سومو (عبر 964)", "domain": "somooil.gov.iq"}, {"name": "وزارة النفط", "domain": "oil.gov.iq"}]
SLATE[slug] = (p, {
 "kicker": "العراق والأردن", "hookHeadline": "نفط كركوك ما يوصل الأردن.. ليش؟",
 "voText": ("بحسب شبكة تسعمئة وأربعة وستين، توقف تجهيز الأردن بنفط كركوك منذ مطلع العام، ووزارة النفط تقول إن الخام الخفيف غير متوفر بالكميات المطلوبة وإن خام البصرة لا يناسب المصافي الأردنية. "
            "لكن بيانات سومو تظهر تصدير نحو مليون وسبعمئة وستين ألف برميل من خام كركوك إلى جيهان التركي في آب. "
            "وكان الأردن يحصل على ما بين عشرة وخمسة عشر ألف برميل يومياً بسعر برنت ناقص ستة عشر دولاراً، منها أربعة دولارات وستة وسبعون سنتاً وفر للخزينة الأردنية. "
            "كنت تعرف بخصم الستة عشر دولار؟"),
 "endQuestion": "كنت تعرف بخصم الستة عشر دولار؟",
 "sourcesLine": "المصادر: شبكة 964 · شفق نيوز · بيانات سومو — 13 و14 تشرين الأول 2026",
 "statPops": [{"value": "1.76M", "label": "برميل من خام كركوك إلى جيهان في آب — سومو", "matchWord": "جيهان"},
              {"value": "$16", "label": "خصم البرميل عن برنت في عقد الأردن", "matchWord": "ناقص"}],
}, """نفط العراق للأردن — ليش توقف، ووين راح خام كركوك؟

الكميات، تركيا، ومعادلة الخصم.. بالفيديو.

كنت تعرف بخصم الـ16 دولار؟

المصادر: شبكة 964، شفق نيوز، بيانات سومو (13 و14 تشرين الأول 2026)

#نفط_كركوك #الأردن #النفط_العراقي #العراق #photonectnews
@photonect.news
""")

# ═══════════ D · 22:30 · P1 accountability — loans taken in retirees' names without their knowledge ═══════════
slug = f"{D}-d-retirees-loans-fraud"
p = base(slug, "iraq_money", "B", "احذر", "قرض باسمك وانت ما تدري؟",
  ("BAGHDAD · OCT 13 | FEDERAL INTELLIGENCE AND INVESTIGATIONS AGENCY (STATEMENT VIA 964, SHAFAQ): A 4-MEMBER NETWORK TARGETING RETIREES DISMANTLED | "
   "METHOD PER THE AGENCY: LURED RETIREES WITH INSTALMENT PURCHASES OF ELECTRICAL AND ELECTRONIC GOODS, THEN USED THEIR PERSONAL DATA TO TAKE LOANS AND ADVANCES IN THEIR NAMES WITHOUT THEIR KNOWLEDGE OR CONSENT | "
   "ALL 4 ARRESTED, STATEMENTS JUDICIALLY CERTIFIED; ACCUSED, NOT CONVICTED | TIPS: FREE NUMBER 911"))
p["beats"] = [
 beat("الشبكة", "4 متهمين استهدفوا المتقاعدين",
  "وكالة الاستخبارات والتحقيقات الاتحادية أعلنت تفكيك شبكة من أربعة متهمين تمارس احتيالاً مالياً إلكترونياً يستهدف المتقاعدين (بيان عبر 964 وشفق نيوز).",
  "4", "Accused members of the network, all arrested, per the Federal Intelligence and Investigations Agency (via 964 / Shafaq)", "متهمين — قُبض على جميعهم",
  [("المستهدفون", "المتقاعدون"), ("النوع", "احتيال إلكتروني"), ("الحالة", "متهمون")], 1, slug,
  ["شبكة من 4 متهمين", "احتيال مالي إلكتروني", "يستهدف المتقاعدين"], GEN),
 beat("الطريقة", "«أجهزة بالتقسيط».. ثم قروض بأسمائهم",
  "بحسب البيان: يوهمون المتقاعد بشراء أجهزة كهربائية وإلكترونية بالتقسيط، ثم يستغلون بياناته الشخصية لسحب قروض وسلف باسمه دون علمه أو موافقته.",
  "0", "Retiree consent: loans and advances were taken in their names without their knowledge or approval, per the agency statement", "علم أو موافقة من المتقاعد — بحسب البيان",
  [("الطُّعم", "أجهزة بالتقسيط"), ("المسروق", "البيانات الشخصية"), ("النتيجة", "قروض وسلف")], 2, slug,
  ["الطُّعم: أجهزة بالتقسيط", "ثم بياناتك الشخصية", "وقروض باسمك دون علمك"], GEN),
 beat("الآن", "قبض على الجميع.. والتبليغ على 911",
  "الوكالة: قُبض على أفراد الشبكة جميعاً وصُدّقت أقوالهم قضائياً تمهيداً لاستكمال الإجراءات، ولم تصدر أحكام بعد. وللتبليغ: الرقم المجاني 911.",
  "911", "Free number the agency asks citizens to call with information", "الرقم المجاني للتبليغ",
  [("المقبوض عليهم", "4 من 4"), ("الأقوال", "صُدّقت قضائياً"), ("الحكم", "لم يصدر")], 3, slug,
  ["قُبض على الأربعة", "وصُدّقت أقوالهم قضائياً", "التبليغ على 911"], GEN),
]
p["arabicTicker"] = [
 "الاستخبارات الاتحادية: تفكيك شبكة من 4 متهمين تستهدف المتقاعدين بالاحتيال الإلكتروني (964، شفق نيوز)",
 "الطريقة بحسب البيان: إغراء بشراء أجهزة بالتقسيط ثم قروض وسلف بأسماء المتقاعدين دون علمهم",
 "القبض على جميع أفراد الشبكة وتصديق أقوالهم قضائياً — ولم تصدر أحكام",
 "للتبليغ: الرقم المجاني 911",
 "وصلك اتصال يطلب بياناتك؟",
]
p["endQuestion"] = "وصلك اتصال يطلب بياناتك؟"
p["sources"] = [{"name": "وكالة الاستخبارات والتحقيقات الاتحادية", "domain": "moi.gov.iq"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = (p, {
 "kicker": "احذر", "hookHeadline": "قرض باسمك.. وانت ما تدري؟",
 "voText": ("أعلنت وكالة الاستخبارات والتحقيقات الاتحادية تفكيك شبكة من أربعة متهمين تمارس الاحتيال المالي الإلكتروني ضد المتقاعدين. "
            "وبحسب بيان الوكالة، كان المتهمون يوهمون المتقاعد بإمكانية شراء أجهزة كهربائية وإلكترونية بالتقسيط، ثم يستغلون بياناته الشخصية لسحب قروض وسلف مالية باسمه من دون علمه أو موافقته. "
            "وتقول الوكالة إنها قبضت على جميع أفراد الشبكة وصدّقت أقوالهم قضائياً، ولم تصدر أحكام بعد، وتدعو للتبليغ على الرقم المجاني. "
            "وصلك اتصال يطلب بياناتك؟"),
 "endQuestion": "وصلك اتصال يطلب بياناتك؟",
 "sourcesLine": "المصادر: وكالة الاستخبارات والتحقيقات الاتحادية عبر شبكة 964 · شفق نيوز — 13 تشرين الأول 2026",
 "statPops": [{"value": "4", "label": "متهمين — قُبض على جميعهم", "matchWord": "أربعة"},
              {"value": "911", "label": "الرقم المجاني للتبليغ", "matchWord": "المجاني"}],
}, """احتيال على المتقاعدين في العراق — قرض باسمك وانت ما تدري؟

الطُّعم كان «أجهزة بالتقسيط».. شلون صارت، وين تبلّغ؟ بالفيديو.

وصلك اتصال يطلب بياناتك؟

المصادر: وكالة الاستخبارات والتحقيقات الاتحادية عبر شبكة 964 وشفق نيوز (13 تشرين الأول 2026)

#المتقاعدين #احتيال #العراق #أخبار #photonectnews
@photonect.news
""")

# ═══════════ E · 23:45 · P3 society — September marriages vs divorces (V10.1 control) ═══════════
slug = f"{D}-e-marriage-35440-divorce"
p = base(slug, "iraq_society", "C", "المجتمع", "35 ألف عرس.. و6,741 طلاق بشهر",
  ("BAGHDAD · OCT 14 | SUPREME JUDICIAL COUNCIL (VIA SHAFAQ, 964): FEDERAL COURTS (15 PROVINCES, EXCLUDING KURDISTAN REGION) REGISTERED 35,440 MARRIAGE CONTRACTS AND 6,741 DIVORCES "
   "(INCL. RATIFIED EXTERNAL DIVORCES) IN SEPTEMBER — 42,181 IN TOTAL VS ~27,000 IN AUGUST (SHAFAQ) | BAGHDAD (KARKH + RUSAFA): 8,938 MARRIAGES, 2,515 DIVORCES | NINEVEH: 4,055 MARRIAGES, 678 DIVORCES | "
   "~19 DIVORCES PER 100 MARRIAGES NATIONALLY, ~28 IN BAGHDAD (COMPUTED)"))
p["beats"] = [
 beat("أيلول", "35,440 عقد زواج بشهر واحد",
  "مجلس القضاء الأعلى: محاكم 15 محافظة، عدا إقليم كوردستان، سجلت 35,440 عقد زواج و6,741 حالة طلاق خلال أيلول (شفق نيوز، 964).",
  "35,440", "Marriage contracts registered by federal courts in September, excluding the Kurdistan Region (Supreme Judicial Council via Shafaq / 964)", "عقد زواج في أيلول — مجلس القضاء الأعلى",
  [("الزواج", "35,440"), ("الطلاق", "6,741"), ("المحافظات", "15")], 1, slug,
  ["35,440 عقد زواج", "و6,741 حالة طلاق", "في أيلول وحده"], GEN),
 beat("النسبة", "19 طلاقاً لكل 100 زواج",
  "يعني نحو 19 حالة طلاق مقابل كل 100 عقد زواج (محتسب). ومجموع الحالتين 42,181، بعد نحو 27 ألفاً في آب بحسب شفق نيوز.",
  "19", "Divorces per 100 marriage contracts in September (computed from Supreme Judicial Council figures)", "طلاقاً لكل 100 زواج (محتسب)",
  [("المجموع", "42,181"), ("آب", "~27 ألف"), ("النسبة", "19% (محتسب)")], 2, slug,
  ["19 طلاقاً لكل 100 زواج", "المجموع 42,181", "بعد نحو 27 ألفاً بآب"], GEN),
 beat("بغداد", "بغداد الأولى.. 8,938 زواج و2,515 طلاق",
  "بغداد بجانبيها تصدرت بـ8,938 زواجاً و2,515 طلاقاً، أي نحو 28 طلاقاً لكل 100 زواج (محتسب). تلتها نينوى بـ4,055 زواجاً و678 طلاقاً.",
  "2,515", "Divorces registered in Baghdad (Karkh + Rusafa) in September, the highest of any province (Supreme Judicial Council)", "حالة طلاق في بغداد خلال أيلول",
  [("بغداد زواج", "8,938"), ("نينوى زواج", "4,055"), ("نينوى طلاق", "678")], 3, slug,
  ["بغداد: 8,938 زواج", "و2,515 طلاق", "نينوى ثانياً: 4,055"], GEN),
]
p["arabicTicker"] = [
 "مجلس القضاء الأعلى: 35,440 عقد زواج و6,741 حالة طلاق في أيلول — عدا إقليم كوردستان (شفق نيوز، 964)",
 "بغداد بجانبيها الأولى: 8,938 زواجاً و2,515 طلاقاً",
 "نينوى ثانياً: 4,055 زواجاً و678 طلاقاً",
 "نحو 19 طلاقاً مقابل كل 100 زواج (محتسب)",
 "كم عرس حضرت هالشهر؟",
]
p["endQuestion"] = "كم عرس حضرت هالشهر؟"
p["sources"] = [{"name": "مجلس القضاء الأعلى", "domain": "sjc.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = (p, None, """الزواج والطلاق في العراق — أرقام أيلول

كم عرس، كم طلاق، ومنو المحافظة الأولى.. بالفيديو.

كم عرس حضرت هالشهر؟

المصادر: مجلس القضاء الأعلى عبر شفق نيوز وشبكة 964 (14 تشرين الأول 2026)

#الزواج #الطلاق #بغداد #العراق #photonectnews
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
