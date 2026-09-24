#!/usr/bin/env python3
"""Author the 2026-09-24 slate: props.json + caption.txt (+ v11-brief.json on a-d).

Every figure traces to a named source published 23-24 Sep 2026. Computed figures carry (محتسب).
Heroes are KIE nano-banana-pro; brolls are Commons/Pexels (real photos) — see _image_credits_2026_09_24.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-24"
DATE_LABEL = "SEP 24 • 2026"
AR_DATE = "24 أيلول 2026"
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

# ═══════════ A · 18:00 · P1 corruption / asset recovery (LEAD) ═══════════
slug = f"{D}-a-france-13-million"
p = base(slug, "iraq_corruption", "A", "عاجل", "13 مليون دولار رجعت للخزينة من بنوك فرنسا",
  ("BAGHDAD · SEP 24 | IRAQ'S ASSET RECOVERY FUND SAID ON THURSDAY 24 SEP IT RETURNED $13M OF IRAQI FUNDS "
   "FROZEN IN FRENCH BANKS UNDER JUDICIAL RULINGS TO THE STATE TREASURY (SHAFAQ NEWS; 964) | DEPOSITED IN "
   "FINANCE MINISTRY ACCOUNTS IN COORDINATION WITH ARAB SWISS BANK, SAID FUND CHAIR MOHAMMED ALI AL-LAMI, WHO "
   "ALSO HEADS THE INTEGRITY COMMISSION | 964: THE RETURN FOLLOWED UNDERSTANDINGS IN PARIS WITH THE FRENCH "
   "ANTI-CORRUPTION AGENCY AND JUSTICE MINISTRY DURING PM ALI AL-ZAIDI'S DELEGATION VISIT; TALKS COVERED "
   "EXTRADITION OF WANTED PERSONS AND FREEZING IRAQI ASSETS SMUGGLED ABROAD | THE OWNER/CASE BEHIND THE FUNDS "
   "WAS NOT DISCLOSED"))
p["beats"] = [
 beat("المبلغ", "13 مليون دولار كانت محجوزة بفرنسا",
  "صندوق استرداد أموال العراق أعلن اليوم الخميس استعادة 13 مليون دولار من أموال عراقية محجوزة في بنوك فرنسية بموجب قرارات قضائية (شفق نيوز، شبكة 964).",
  "13", "Million US dollars of frozen Iraqi funds returned from French banks, 24 Sep",
  "مليون دولار أموال عراقية محجوزة ببنوك فرنسا رجعت للخزينة (شفق نيوز، شبكة 964)",
  [("المصدر", "بنوك فرنسية"), ("السند", "قرارات قضائية"), ("التاريخ", "24 أيلول")], 1, slug,
  ["13 مليون دولار", "كانت محجوزة ببنوك فرنسا", "ورجعت بقرارات قضائية"], STOCK),
 beat("وين راحت", "المبلغ دخل حسابات وزارة المالية",
  "رئيس الصندوق محمد علي اللامي قال إن المبلغ أُودع في حسابات وزارة المالية بالتنسيق مع البنك العربي السويسري، ولم يُعلَن صاحب الأموال أو القضية (شبكة 964).",
  "24", "September — date the fund announced the deposit into Finance Ministry accounts",
  "أيلول: إعلان إيداع المبلغ بحسابات وزارة المالية (شبكة 964)",
  [("الجهة", "وزارة المالية"), ("بالتنسيق", "العربي السويسري"), ("القضية", "لم تُعلن")], 2, slug,
  ["المبلغ دخل وزارة المالية", "بالتنسيق مع مصرف سويسري", "وصاحب الأموال ما انعلن"], STOCK),
 beat("باريس", "تفاهمات بباريس.. وملف الأموال المهرّبة",
  "حسب شبكة 964، الخطوة جاءت بعد تفاهمات في باريس مع الوكالة الفرنسية لمكافحة الفساد ووزارة العدل، بحثت تسليم المطلوبين وتجميد الأصول العراقية المهرّبة.",
  "3", "French bodies al-Lami met in Paris: anti-corruption agency, asset-recovery agency, justice ministry",
  "جهات فرنسية بحث معها اللامي بباريس: مكافحة الفساد واسترداد الموجودات والعدل (شبكة 964)",
  [("الملف", "تسليم المطلوبين"), ("والأصول", "تجميد المهرّب"), ("الهدف", "اتفاق رسمي")], 3, slug,
  ["تفاهمات في باريس", "تسليم المطلوبين", "وتجميد الأصول المهرّبة"], STOCK),
]
p["arabicTicker"] = [
 "صندوق استرداد أموال العراق: استعادة 13 مليون دولار من أموال عراقية محجوزة في بنوك فرنسية بموجب قرارات قضائية (شفق نيوز — 24 أيلول)",
 "المبلغ أُودع في حسابات وزارة المالية بالتنسيق مع البنك العربي السويسري (رئيس الصندوق محمد علي اللامي — شبكة 964)",
 "الاسترداد جاء بعد تفاهمات في باريس مع الوكالة الفرنسية لمكافحة الفساد ووزارة العدل على هامش زيارة الوفد الحكومي برئاسة علي الزيدي (شبكة 964)",
 "المباحثات شملت تسليم المطلوبين وتجميد الأصول العراقية المهرّبة للخارج، وبغداد تتطلع لاتفاق رسمي مع الوكالة الفرنسية (شبكة 964)",
 "لم يُكشف عن صاحب الأموال المستردة أو القضية المرتبطة بها",
 "سمعت بصندوق استرداد الأموال قبل اليوم؟"]
p["endQuestion"] = "سمعت بصندوق استرداد الأموال قبل اليوم؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """فلوس العراق المحجوزة بفرنسا — شكد رجع منها؟

صندوق استرداد الأموال يعلن رجوع مبلغ للخزينة.. والقصة ما خلصت بباريس.

سمعت بصندوق استرداد الأموال قبل اليوم؟

المصادر: شفق نيوز، شبكة 964 (24 أيلول 2026)

#العراق #استرداد_الأموال #مكافحة_الفساد #فرنسا #photonectnews
@photonect.news""",
 "brief": {"kicker": "عاجل", "hookHeadline": "13 مليون دولار رجعت من فرنسا",
  "voText": "أعلن صندوق استرداد أموال العراق، اليوم الخميس، استعادة ثلاثة عشر مليون دولار من أموال عراقية كانت محجوزة في بنوك فرنسية بموجب قرارات قضائية. وقال رئيس الصندوق محمد علي اللامي إن المبلغ أودع في حسابات وزارة المالية بالتنسيق مع البنك العربي السويسري، من دون الكشف عن صاحب الأموال. ونقلت شبكة تسعة ستة أربعة أن الخطوة جاءت بعد تفاهمات في باريس مع الوكالة الفرنسية لمكافحة الفساد ووزارة العدل، شملت تسليم المطلوبين وتجميد الأصول المهربة. سمعت بصندوق استرداد الأموال قبل اليوم؟",
  "endQuestion": "سمعت بصندوق استرداد الأموال قبل اليوم؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 24 أيلول 2026",
  "statPops": [{"value": "$13M", "label": "رجعت من بنوك فرنسا", "matchWord": "فرنسية"},
               {"value": "المالية", "label": "المبلغ أُودع بحسابات الوزارة", "matchWord": "المالية"}]}}

# ═══════════ B · 19:45 · P1 dollar anchor ═══════════
slug = f"{D}-b-dollar-week-2000"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "بأسبوع.. الدولار نزل 2,000 دينار ببغداد",
  ("BAGHDAD · SEP 24 | 964 MORNING LIST (10:53, THU 24 SEP), PER $100: BAGHDAD SELL 157,000 / BUY 156,750; ERBIL "
   "SELL 157,000 / BUY 156,250; BASRA SELL 157,000 / BUY 156,500; CBI OFFICIAL 131,000 | 964'S MORNING LIST A WEEK "
   "EARLIER (10:51, THU 17 SEP): BAGHDAD SELL 159,000 — 2,000 LOWER THURSDAY-TO-THURSDAY (COMPUTED FROM 964'S TWO "
   "LISTS) | SHAFAQ (THU MORNING): KIFAH & HARITHIYA 156,800; BAGHDAD SHOPS SELL 157,250 / BUY 156,250; ERBIL SELL "
   "156,800 / BUY 156,750 | GOLD, SHAFAQ THU: NAHR ST WHOLESALE 21K GULF/TURKISH/EUROPEAN MITHQAL SELL 945,000 / BUY "
   "941,000; IRAQI 21K SELL 915,000"))
p["beats"] = [
 beat("اليوم", "قائمة 964: بغداد 157,000",
  "قائمة شبكة 964 صباح الخميس: بيع 100 دولار ببغداد وأربيل والبصرة 157,000 دينار، والسعر الرسمي عند البنك المركزي 131,000.",
  "157,000", "Dinars, sell price per $100 in Baghdad, 964 morning list, Thursday 24 Sep",
  "دينار بيع 100 دولار ببغداد بقائمة شبكة 964 صباح الخميس",
  [("أربيل", "157,000"), ("البصرة", "157,000"), ("الرسمي", "131,000")], 1, slug,
  ["بغداد 157,000", "أربيل والبصرة نفس الرقم", "والرسمي 131,000"], STOCK),
 beat("الأسبوع", "الخميس الماضي كان 159,000",
  "نفس القائمة يوم الخميس 17 أيلول سجّلت 159,000 لبيع بغداد — يعني نزل 2,000 دينار بأسبوع (محتسب من قائمتَي 964). وشفق نيوز سجّلت الكفاح والحارثية 156,800.",
  "2,000", "Dinars lower: 964 Baghdad morning sell, Thu 17 Sep vs Thu 24 Sep (computed)",
  "دينار نزول بيع بغداد بين قائمتَي 964 ليومي الخميس 17 و24 أيلول (محتسب)",
  [("17 أيلول", "159,000"), ("24 أيلول", "157,000"), ("البورصة", "156,800")], 2, slug,
  ["الخميس الماضي 159,000", "واليوم 157,000", "نزول 2,000 (محتسب)"], STOCK),
 beat("الذهب", "مثقال الذهب بشارع النهر 945,000",
  "شفق نيوز: مثقال الذهب الخليجي والتركي والأوروبي عيار 21 بجملة شارع النهر بيع 945,000 دينار، والعراقي عيار 21 بيع 915,000.",
  "945,000", "Dinars, sell price per mithqal of 21K foreign gold, Nahr St wholesale, Thursday (Shafaq)",
  "دينار مثقال الذهب الأجنبي عيار 21 بجملة شارع النهر صباح الخميس (شفق نيوز)",
  [("الشراء", "941,000"), ("العراقي", "915,000"), ("عيار", "21")], 3, slug,
  ["الذهب الأجنبي 945,000", "والعراقي 915,000", "بجملة شارع النهر"], STOCK),
]
p["arabicTicker"] = [
 "قائمة شبكة 964 صباح الخميس 24 أيلول: بيع 100 دولار ببغداد 157,000 دينار والشراء 156,750",
 "أربيل: البيع 157,000 والشراء 156,250 — البصرة: البيع 157,000 والشراء 156,500 (شبكة 964)",
 "قائمة 964 يوم الخميس 17 أيلول سجّلت 159,000 لبيع بغداد — نزول 2,000 دينار بأسبوع (محتسب من قائمتَي الشبكة)",
 "شفق نيوز صباح الخميس: بورصتا الكفاح والحارثية 156,800، ومحال بغداد بيع 157,250 وشراء 156,250",
 "السعر الرسمي للبنك المركزي 131,000 دينار لكل 100 دولار",
 "الذهب: مثقال الأجنبي عيار 21 بشارع النهر بيع 945,000 والعراقي 915,000 (شفق نيوز)",
 "بدّلت دولار هالأسبوع؟"]
p["endQuestion"] = "بدّلت دولار هالأسبوع؟"
p["sources"] = [{"name": "شبكة 964", "domain": "964media.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — شكد نزل بأسبوع؟

قارنّا قائمة الخميس بقائمة الخميس الماضي.. والذهب هم إله رقم اليوم.

بدّلت دولار هالأسبوع؟

المصادر: شبكة 964، شفق نيوز (24 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #الذهب #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "بأسبوع.. الدولار نزل 2,000 دينار",
  "voText": "سجّلت القائمة الصباحية لشبكة تسعة ستة أربعة، اليوم الخميس، سعر بيع مئة دولار في بغداد عند مئة وسبعة وخمسين ألف دينار، بعد أن كان مئة وتسعة وخمسين ألفاً في قائمتها صباح الخميس الماضي، أي أقل بألفي دينار خلال أسبوع. وفي بورصتي الكفاح والحارثية سجّلت شفق نيوز مئة وستة وخمسين ألفاً وثمانمئة، فيما بقي السعر الرسمي عند مئة وواحد وثلاثين ألفاً. أما مثقال الذهب الأجنبي عيار واحد وعشرين في جملة شارع النهر فبلغ تسعمئة وخمسة وأربعين ألف دينار. بدّلت دولار هالأسبوع؟",
  "endQuestion": "بدّلت دولار هالأسبوع؟",
  "sourcesLine": "المصادر: شبكة 964 · شفق نيوز — 24 أيلول 2026",
  "statPops": [{"value": "157,000", "label": "بيع 100 دولار ببغداد (قائمة 964)", "matchWord": "بغداد"},
               {"value": "-2,000", "label": "فرق أسبوع بقائمة 964 (محتسب)", "matchWord": "بألفي"}]}}

# ═══════════ C · 21:15 · P2 Hormuz → Iraq economy ═══════════
slug = f"{D}-c-ebrd-minus-12"
p = base(slug, "mena_geo", "B", "اقتصاد", "البنك الأوروبي: اقتصاد العراق ينكمش 12% هذا العام",
  ("LONDON/BAGHDAD · SEP 24 | EBRD REGIONAL ECONOMIC PROSPECTS, 24 SEP 2026: IRAQ'S ECONOMY IS EXPECTED TO "
   "CONTRACT BY 12.0% IN 2026 BEFORE REBOUNDING BY 14.0% IN 2027 | THE DOWNTURN REFLECTS SEVERE DISRUPTIONS TO OIL "
   "EXPORTS THROUGH THE STRAIT OF HORMUZ; ALTERNATIVE ROUTES CARRIED LESS THAN A QUARTER OF IRAQ'S NORMAL EXPORT "
   "VOLUMES, WITH A SUBSTANTIAL IMPACT ON GROWTH, PUBLIC FINANCES AND FX RESERVES | THE 2027 REBOUND ASSUMES "
   "OIL EXPORTS NORMALISE | SHAFAQ: THE LARGEST DOWNGRADE AMONG ECONOMIES COVERED; LEBANON -5% | SEMED REGION "
   "-0.7% IN 2026 (EBRD)"))
p["beats"] = [
 beat("التوقع", "ناقص 12%.. أكبر خفض بالتقرير",
  "البنك الأوروبي لإعادة الإعمار والتنمية توقّع بتقرير صدر الخميس انكماش اقتصاد العراق 12% خلال 2026، وهو أكبر خفض بين الاقتصادات التي يغطيها التقرير (شفق نيوز).",
  "-12%", "EBRD forecast for Iraq's economy in 2026, published 24 Sep",
  "توقع البنك الأوروبي لاقتصاد العراق في 2026 (تقرير 24 أيلول)",
  [("لبنان", "-5%"), ("المنطقة", "-0.7%"), ("التقرير", "24 أيلول")], 1, slug,
  ["انكماش 12%", "أكبر خفض بالتقرير", "ولبنان ناقص 5%"], STOCK),
 beat("السبب", "هرمز: أقل من ربع الصادرات تطلع",
  "البنك قال إن السبب اضطراب صادرات النفط عبر مضيق هرمز، والطرق البديلة نقلت أقل من ربع الكميات المعتادة، فتأثرت المالية العامة واحتياطيات العملة الأجنبية.",
  "<25%", "Share of Iraq's normal export volumes carried by alternative routes (EBRD)",
  "من صادرات العراق المعتادة نقلتها الطرق البديلة (البنك الأوروبي)",
  [("المضيق", "هرمز"), ("تأثر", "المالية العامة"), ("وأيضاً", "الاحتياطيات")], 2, slug,
  ["المشكلة بمضيق هرمز", "البدائل أقل من الربع", "والمالية العامة تأثرت"], STOCK),
 beat("2027", "والتعافي؟ مشروط برجوع الصادرات",
  "البنك يتوقع نمو 14% في 2027، ويقول إن هذا التوقع يفترض عودة صادرات النفط إلى طبيعتها (البنك الأوروبي لإعادة الإعمار والتنمية).",
  "+14%", "EBRD forecast for Iraq's economy in 2027, assuming oil exports normalise",
  "توقع البنك لنمو اقتصاد العراق في 2027 بشرط عودة الصادرات",
  [("الشرط", "عودة الصادرات"), ("2026", "-12%"), ("2027", "+14%")], 3, slug,
  ["2027 نمو 14%", "بشرط رجوع الصادرات", "لطبيعتها"], STOCK),
]
p["arabicTicker"] = [
 "البنك الأوروبي لإعادة الإعمار والتنمية يتوقع انكماش اقتصاد العراق 12% في 2026 (تقرير الآفاق الاقتصادية الإقليمية — 24 أيلول)",
 "السبب بحسب البنك: اضطراب صادرات النفط عبر مضيق هرمز، والطرق البديلة نقلت أقل من ربع الكميات المعتادة",
 "البنك: الاضطراب أثّر بشكل كبير في النمو والمالية العامة واحتياطيات العملة الأجنبية",
 "توقع نمو 14% في 2027 بافتراض عودة صادرات النفط إلى طبيعتها (البنك الأوروبي)",
 "شفق نيوز: خفض العراق هو الأكبر بين الاقتصادات التي يغطيها التقرير، ولبنان -5%",
 "راتبك وصل بموعده هالشهر؟"]
p["endQuestion"] = "راتبك وصل بموعده هالشهر؟"
p["sources"] = [{"name": "البنك الأوروبي لإعادة الإعمار والتنمية", "domain": "ebrd.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """اقتصاد العراق 2026 — شنو قال البنك الأوروبي؟

تقرير جديد يربط رقم صادم بمضيق هرمز.. وشرط واحد للتعافي.

راتبك وصل بموعده هالشهر؟

المصادر: البنك الأوروبي لإعادة الإعمار والتنمية، شفق نيوز (24 أيلول 2026)

#العراق #اقتصاد_العراق #مضيق_هرمز #النفط #photonectnews
@photonect.news""",
 "brief": {"kicker": "اقتصاد", "hookHeadline": "اقتصاد العراق ينكمش 12%.. ليش؟",
  "voText": "توقّع البنك الأوروبي لإعادة الإعمار والتنمية، في تقرير صدر اليوم الخميس، أن ينكمش اقتصاد العراق بنسبة اثني عشر بالمئة خلال هذا العام، وهو أكبر خفض بين الاقتصادات التي يغطيها التقرير بحسب شفق نيوز. وعزا البنك ذلك إلى اضطراب صادرات النفط عبر مضيق هرمز، قائلاً إن الطرق البديلة نقلت أقل من ربع الكميات المعتادة، ما أثّر في المالية العامة واحتياطيات العملة الأجنبية. ويتوقع البنك تعافياً بنسبة أربعة عشر بالمئة في العام المقبل إذا عادت الصادرات إلى طبيعتها. راتبك وصل بموعده هالشهر؟",
  "endQuestion": "راتبك وصل بموعده هالشهر؟",
  "sourcesLine": "المصادر: البنك الأوروبي لإعادة الإعمار والتنمية · شفق نيوز — 24 أيلول 2026",
  "statPops": [{"value": "-12%", "label": "توقع اقتصاد العراق 2026", "matchWord": "ينكمش"},
               {"value": "+14%", "label": "توقع 2027 بشرط عودة الصادرات", "matchWord": "تعافياً"}]}}

# ═══════════ D · 22:30 · P3 sport / pride ═══════════
slug = f"{D}-d-gulf-cup-oman-draw"
p = base(slug, "region_sport", "A", "خليجي 27", "هدف بالدقيقة 6.. والعراق يتعادل مع عُمان",
  ("JEDDAH · SEP 23 | 27TH GULF CUP, GROUP A OPENER AT PRINCE ABDULLAH AL-FAISAL STADIUM: IRAQ 1-1 OMAN | "
   "MOHAMMED QASIM 6' (FROM AYMEN HUSSEIN'S HEADER), NASSER AL-RAWAHI 67' (AL-KHALEEJ; AL-MASHHAD) | SAUDI ARABIA "
   "BEAT KUWAIT 1-0 AND TOP GROUP A (SHAFAQ; BBC ARABIC) | TOP TWO IN EACH GROUP REACH THE SEMI-FINALS; FINAL 6 OCT "
   "(SHAFAQ) | IRAQ NEXT PLAY KUWAIT ON SATURDAY 26 SEP AT 18:55 BAGHDAD (AL-MASHHAD) | IRAQ COACH: GRAHAM ARNOLD"))
p["beats"] = [
 beat("النتيجة", "1-1 بافتتاح المشوار بجدة",
  "المنتخب العراقي بقيادة المدرب غراهام أرنولد تعادل مع عُمان 1-1 مساء الأربعاء على ملعب الأمير عبد الله الفيصل بجدة، بافتتاح مشواره في خليجي 27 (الخليج، المشهد).",
  "1-1", "Iraq vs Oman, Gulf Cup 27 Group A opener, Jeddah, Wednesday 23 Sep",
  "العراق وعُمان بافتتاح المجموعة الأولى من خليجي 27 في جدة (الخليج، المشهد)",
  [("الملعب", "الأمير عبد الله الفيصل"), ("المدرب", "غراهام أرنولد"), ("المجموعة", "الأولى")], 1, slug,
  ["العراق وعُمان 1-1", "ملعب الأمير عبد الله الفيصل", "بقيادة غراهام أرنولد"], "صورة أرشيفية · ويكيميديا"),
 beat("الأهداف", "محمد قاسم بالدقيقة 6.. والرواحي بالـ67",
  "محمد قاسم سجّل هدف التقدم بالدقيقة السادسة بعد كرة برأسية من أيمن حسين، وناصر الرواحي عادل لعُمان بالدقيقة 67 (صحيفة الخليج).",
  "6'", "Minute Mohammed Qasim scored Iraq's goal; Oman equalised in the 67th",
  "دقيقة هدف محمد قاسم للعراق، وعُمان عادلت بالدقيقة 67 (صحيفة الخليج)",
  [("هدفنا", "محمد قاسم"), ("التعادل", "الدقيقة 67"), ("الصناعة", "أيمن حسين")], 2, slug,
  ["محمد قاسم بالدقيقة 6", "بعد رأسية أيمن حسين", "والرواحي عادل بالـ67"], STOCK),
 beat("الجاية", "السبت مع الكويت.. والسعودية بالصدارة",
  "السعودية فازت على الكويت 1-0 وتصدرت المجموعة، والعراق يلاقي الكويت السبت 26 أيلول الساعة 18:55 بتوقيت بغداد، ويتأهل الأول والثاني لنصف النهائي (شفق نيوز، المشهد).",
  "26", "September — Iraq vs Kuwait, Saturday, 18:55 Baghdad time",
  "أيلول: العراق والكويت يوم السبت الساعة 18:55 بتوقيت بغداد (المشهد)",
  [("الخصم", "الكويت"), ("الموعد", "18:55"), ("المتأهلون", "الأول والثاني")], 3, slug,
  ["السبت مع الكويت", "الساعة 18:55", "والأول والثاني يتأهلون"], STOCK),
]
p["arabicTicker"] = [
 "خليجي 27: العراق يتعادل مع عُمان 1-1 في افتتاح مشواره على ملعب الأمير عبد الله الفيصل بجدة (صحيفة الخليج — 23 أيلول)",
 "محمد قاسم سجّل للعراق بالدقيقة 6، وناصر الرواحي عادل لعُمان بالدقيقة 67 (صحيفة الخليج، المشهد)",
 "السعودية تفوز على الكويت 1-0 وتتصدر المجموعة الأولى (شفق نيوز)",
 "العراق يلاقي الكويت السبت 26 أيلول الساعة 18:55 بتوقيت بغداد (المشهد)",
 "البطولة في جدة من 23 أيلول إلى 6 تشرين الأول، ويتأهل الأول والثاني من كل مجموعة لنصف النهائي (شفق نيوز)",
 "راح تتابع مباراة الكويت السبت؟"]
p["endQuestion"] = "راح تتابع مباراة الكويت السبت؟"
p["sources"] = [{"name": "صحيفة الخليج", "domain": "alkhaleej.ae"}, {"name": "المشهد", "domain": "almashhad.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """العراق وعُمان خليجي 27 — شنو صار بجدة؟

بداية مشوار أسود الرافدين.. وموعد السبت صار مصيري.

راح تتابع مباراة الكويت السبت؟

المصادر: صحيفة الخليج، المشهد، شفق نيوز (23-24 أيلول 2026)

#خليجي_27 #المنتخب_العراقي #العراق #أسود_الرافدين #photonectnews
@photonect.news""",
 "brief": {"kicker": "خليجي 27", "hookHeadline": "هدف بالدقيقة 6.. وتعادل مع عُمان",
  "voText": "افتتح المنتخب العراقي، بقيادة مدربه غراهام أرنولد، مشواره في بطولة كأس الخليج السابعة والعشرين بالتعادل مع عُمان بهدف لمثله، مساء الأربعاء على ملعب الأمير عبد الله الفيصل في جدة. وسجّل محمد قاسم هدف التقدم في الدقيقة السادسة، قبل أن يعادل ناصر الرواحي في الدقيقة السابعة والستين. وفي المجموعة نفسها فازت السعودية على الكويت بهدف دون رد وتصدرت، ويتأهل الأول والثاني إلى نصف النهائي. ويلتقي العراق الكويت يوم السبت. راح تتابع مباراة الكويت السبت؟",
  "endQuestion": "راح تتابع مباراة الكويت السبت؟",
  "sourcesLine": "المصادر: صحيفة الخليج · المشهد · شفق نيوز — 24 أيلول 2026",
  "statPops": [{"value": "1-1", "label": "العراق وعُمان — خليجي 27", "matchWord": "بالتعادل"},
               {"value": "6'", "label": "هدف محمد قاسم", "matchWord": "السادسة"}]}}

# ═══════════ E · 23:45 · P2 Iran→Iraq trade (V10.1 control) ═══════════
slug = f"{D}-e-mehran-453-million"
p = base(slug, "mena_geo", "C", "تجارة", "453 مليون دولار بضاعة عبرت منفذ مهران بـ6 أشهر",
  ("ILAM, IRAN · SEP 24 | ILAM PROVINCE CUSTOMS DIRECTOR-GENERAL SOHRAB KAMARI TOLD IRAN'S OFFICIAL AGENCY IRNA "
   "THAT GOODS EXPORTED THROUGH THE MEHRAN INTERNATIONAL BORDER CROSSING IN THE PAST SIX MONTHS WERE WORTH $453M, "
   "TOTAL WEIGHT 1,046,579 TONNES, SHIPPED TO IRAQ AND OTHER REGIONAL COUNTRIES (REPORTED BY SHAFAQ NEWS) | MAIN "
   "GOODS: FARM PRODUCE, TILES AND CERAMICS, PLASTIC HOUSEWARE AND SINGLE-USE PRODUCTS, GLASS, REBAR, LIVE FISH, "
   "IRON ORE, PVC PIPES, BUILDING STONE | FIGURES ARE IRAN'S; NO IRAQI BREAKDOWN WAS PUBLISHED"))
p["beats"] = [
 beat("الرقم", "منفذ واحد.. 453 مليون دولار",
  "مدير جمارك إيلام سهراب كمري قال لوكالة إرنا الإيرانية إن قيمة البضائع المصدّرة عبر منفذ مهران بآخر 6 أشهر بلغت 453 مليون دولار، معظمها للعراق (شفق نيوز).",
  "453", "Million US dollars of goods exported via Mehran in six months, per Ilam customs (IRNA)",
  "مليون دولار بضائع صُدّرت عبر مهران بـ6 أشهر حسب جمارك إيلام (إرنا)",
  [("المنفذ", "مهران"), ("المدة", "6 أشهر"), ("الوجهة", "العراق والمنطقة")], 1, slug,
  ["منفذ مهران", "453 مليون دولار", "بستة أشهر"], STOCK),
 beat("الوزن", "أكثر من مليون طن",
  "حسب نفس التصريح، الوزن الإجمالي للبضائع 1,046,579 طناً، والأرقام إيرانية ولم يُنشر تفصيل عراقي مقابل لها (إرنا، شفق نيوز).",
  "1,046,579", "Tonnes of goods exported via Mehran in six months (IRNA)",
  "طن وزن البضائع المصدّرة عبر مهران بستة أشهر (إرنا)",
  [("المصدر", "جمارك إيلام"), ("الوكالة", "إرنا"), ("الرقم العراقي", "غير منشور")], 2, slug,
  ["مليون و46 ألف طن", "أرقام جمارك إيلام", "بدون رقم عراقي مقابل"], STOCK),
 beat("شنو يدخل", "كاشي وحديد وسمك حي",
  "أبرز السلع حسب جمارك إيلام: محاصيل زراعية، بلاط وسيراميك، أوانٍ بلاستيكية، زجاج، حديد تسليح، أسماك حية، أنابيب PVC وأحجار بناء (شفق نيوز).",
  "6", "Months covered by the Ilam customs figure for Mehran exports",
  "أشهر يغطيها رقم جمارك إيلام لصادرات منفذ مهران",
  [("بناء", "بلاط وحديد"), ("غذاء", "محاصيل وسمك"), ("بيت", "بلاستيك وزجاج")], 3, slug,
  ["بلاط وسيراميك", "حديد تسليح وزجاج", "ومحاصيل وأسماك حية"], STOCK),
]
p["arabicTicker"] = [
 "جمارك إيلام الإيرانية: 453 مليون دولار قيمة البضائع المصدّرة عبر منفذ مهران خلال الأشهر الستة الأخيرة (إرنا عبر شفق نيوز — 24 أيلول)",
 "الوزن الإجمالي 1,046,579 طناً صُدّرت إلى العراق وباقي دول المنطقة (مدير جمارك إيلام سهراب كمري)",
 "أبرز السلع: محاصيل زراعية، بلاط وسيراميك، أوانٍ بلاستيكية، زجاج، حديد تسليح، أسماك حية، خام الحديد، أنابيب PVC، أحجار بناء",
 "الأرقام صادرة عن الجانب الإيراني ولم يُنشر تفصيل عراقي مقابل لها",
 "كاشي بيتك إيراني لو محلي؟"]
p["endQuestion"] = "كاشي بيتك إيراني لو محلي؟"
p["sources"] = [{"name": "وكالة إرنا", "domain": "irna.ir"}, {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """البضاعة الإيرانية بالعراق — شكد عبر من منفذ مهران؟

رقم جديد من جمارك إيلام.. وقائمة سلع تلقاها ببيتك.

كاشي بيتك إيراني لو محلي؟

المصادر: وكالة إرنا، شفق نيوز (24 أيلول 2026)

#العراق #إيران #منفذ_مهران #تجارة #photonectnews
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
                 "audioBed": data["props"]["audioBed"], "statPops": b.pop("statPops")}
            order = ["slug", "kicker", "hookHeadline", "voText", "endQuestion", "sourcesLine", "images", "audioBed", "statPops"]
            (d / "v11-brief.json").write_text(json.dumps({k: b[k] for k in order}, ensure_ascii=False, indent=1))
        print(f"  ✓ {slug}  (brief={'yes' if data['brief'] else 'NO — V10.1 control'})")
    print(f"\n== authored {len(SLATE)} slugs ==")

if __name__ == "__main__":
    main()
