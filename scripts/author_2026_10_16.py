#!/usr/bin/env python3
"""Author the 2026-10-16 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source saved in the session scratchpad (Shafaq full-text RSS, 964, Baghdad Today, SJC pages; raw copies in scratchpad/art/).
Computed figures carry (محتسب). PRE-copywriter draft: do NOT re-run after the Opus copywriter/gate edits.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-16"
DATE_LABEL = "OCT 16 • 2026"
AR_DATE = "16 تشرين الأول 2026"
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


# ═══════════ A · 18:00 · P1 fees (LEAD) — passport fee raised to 101k in the morning, reversed to 91k by evening ═══════════
slug = f"{D}-a-passport-101k-reversed"
p = base(slug, "iraq_money", "A", "رسوم الدولة", "جوازك صار بـ101 ألف.. وبالمساء رجع 91",
  ("BAGHDAD · OCT 15 | CITIZENS AT PASSPORT OFFICES FOUND THE E-PASSPORT FEE RAISED TO 101,000 IQD FROM 91,000 (BAGHDAD TODAY; SHAFAQ SECURITY SOURCE) — "
   "PER BAGHDAD TODAY AT THE REQUEST OF THE CONTRACTED COMPANY, CITING THE EXCHANGE RATE | THURSDAY EVENING: INTERIOR SENIOR UNDERSECRETARY HUSSEIN AL-AWADI ORDERED THE FEE KEPT AT 91,000 "
   "WITH NO INCREASE, ON THE COMMANDER-IN-CHIEF'S DIRECTION (INTERIOR STATEMENT VIA SHAFAQ, 964) | MP MIQDAD AL-KHAFAJI SAYS HEPIQ PLATFORM FEES RISE FROM 66,000 TO 76,000; "
   "THE HIGHER EDUCATION MINISTRY HAD NOT CONFIRMED (SHAFAQ)"))
p["beats"] = [
 beat("الصبح", "الخميس الصبح: الجواز بـ101 ألف",
  "مواطنون تفاجأوا الخميس في دوائر الجوازات بأن رسم الجواز الإلكتروني صار 101,000 دينار بدل 91,000 (بغداد اليوم، شفق نيوز)، بذريعة ارتفاع سعر صرف الدولار.",
  "101,000", "IQD e-passport fee citizens were charged on Thursday morning, up from 91,000 (Baghdad Today / Shafaq)", "دينار — رسم الجواز صباح الخميس",
  [("قبلها", "91,000"), ("الزيادة", "10,000"), ("السبب المتداول", "سعر الصرف")], 1, slug,
  ["الجواز صار 101 ألف", "بدل 91 ألف", "بذريعة سعر الصرف"], GEN),
 beat("المساء", "المساء: الداخلية تتراجع.. 91 ألف",
  "الوكيل الأقدم لوزارة الداخلية حسين العوادي وجّه باستمرار استيفاء 91,000 دينار دون أي زيادة، تنفيذاً لتوجيهات القائد العام للقوات المسلحة (شفق نيوز، 964).",
  "91,000", "IQD — the passport fee the Interior Ministry says stays in force with no increase (statement via Shafaq / 964)", "دينار — رسم الجواز بعد التراجع",
  [("الرسم المعتمد", "91,000"), ("الزيادة", "أُلغيت"), ("الدفع", "إلكتروني")], 2, slug,
  ["الداخلية: 91 ألف", "دون أي زيادة", "بتوجيه القائد العام"], GEN),
 beat("بعدها", "و«هيبك»؟ نائب: من 66 إلى 76 ألف",
  "النائب مقداد الخفاجي يقول إن رسوم منصة «هيبك» للطلبة ترتفع من 66,000 إلى 76,000 دينار، ولم تؤكد وزارة التعليم العالي ذلك (شفق نيوز).",
  "76,000", "IQD HEPIQ platform fee per MP Miqdad al-Khafaji, up from 66,000 — not confirmed by the Higher Education Ministry (Shafaq)", "دينار رسوم «هيبك» بحسب النائب — لم تؤكدها الوزارة",
  [("قبلها", "66,000"), ("بحسب", "النائب الخفاجي"), ("الوزارة", "لم تؤكد")], 3, slug,
  ["هيبك: من 66 إلى 76 ألف", "بحسب النائب الخفاجي", "والوزارة لم تؤكد"], GEN),
]
p["arabicTicker"] = [
 "صباح الخميس: رسم الجواز الإلكتروني 101,000 دينار بدل 91,000 (بغداد اليوم، شفق نيوز)",
 "مساء الخميس: الداخلية تعيد الرسم إلى 91,000 دينار دون زيادة (شفق نيوز، 964)",
 "النائب مقداد الخفاجي: رسوم منصة «هيبك» من 66,000 إلى 76,000 — والوزارة لم تؤكد",
 "تحتاج تجدد جوازك هالسنة؟",
]
p["endQuestion"] = "تحتاج تجدد جوازك هالسنة؟"
p["sources"] = [{"name": "وزارة الداخلية", "domain": "moi.gov.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"},
                {"name": "شبكة 964", "domain": "964media.com"}, {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}]
SLATE[slug] = (p, {
 "kicker": "رسوم الدولة", "hookHeadline": "جوازك صار بـ101 ألف.. ورجع",
 "voText": ("صباح الخميس تفاجأ مواطنون في دوائر الجوازات بأن رسم الجواز الإلكتروني صار مئة وألف دينار بدل واحد وتسعين ألفاً، بحسب بغداد اليوم وشفق نيوز، بذريعة ارتفاع سعر صرف الدولار. "
            "وفي المساء أعلنت وزارة الداخلية أن الوكيل الأقدم حسين العوادي وجّه باستمرار استيفاء واحد وتسعين ألف دينار دون أي زيادة. "
            "وفي اليوم نفسه قال النائب مقداد الخفاجي إن رسوم منصة هيبك للطلبة ترتفع إلى ستة وسبعين ألفاً، ولم تؤكد الوزارة ذلك. "
            "تحتاج تجدد جوازك هالسنة؟"),
 "endQuestion": "تحتاج تجدد جوازك هالسنة؟",
 "sourcesLine": "المصادر: وزارة الداخلية · شفق نيوز · شبكة 964 · بغداد اليوم — 15 تشرين الأول 2026",
 "statPops": [{"value": "101,000", "label": "دينار — رسم الجواز صباح الخميس", "matchWord": "الإلكتروني"},
              {"value": "91,000", "label": "دينار — بعد تراجع الداخلية", "matchWord": "استيفاء"}],
}, """رسوم الجواز في العراق — صارت 101 ألف ورجعت؟

شنو صار الصبح، وشنو قررت الداخلية بالمساء.. بالفيديو.

تحتاج تجدد جوازك هالسنة؟

المصادر: وزارة الداخلية عبر شفق نيوز وشبكة 964، بغداد اليوم (15 تشرين الأول 2026)

#الجواز_العراقي #رسوم #العراق #photonectnews
@photonect.news
""")

# ═══════════ B · 19:45 · P1 dollar anchor — travel dollar: $2,000 every two months from Sunday ═══════════
slug = f"{D}-b-travel-dollar-2-months"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "دولار السفر: 2,000 كل شهرين بس",
  ("BAGHDAD · OCT 15 | CENTRAL BANK OF IRAQ (STATEMENT VIA 964, SHAFAQ): TRAVELLERS' DOLLAR ALLOCATION AT THE OFFICIAL RATE SET AT $2,000 EVERY TWO MONTHS, MAX 6 TIMES A YEAR, "
   "EFFECTIVE SUNDAY 18 OCTOBER 2026 | IN JULY THE CAP WAS CUT TO $2,000 A MONTH FROM $3,000 (SHAFAQ, AL JAZEERA) | MAX $12,000/YEAR VS UP TO $24,000 (COMPUTED) | "
   "THURSDAY CLOSE KIFAH/HARITHIYA 166,550 IQD PER $100 (SHAFAQ); OFFICIAL 1,520 IQD/$ — $2,000 = 3,040,000 OFFICIAL VS 3,331,000 MARKET, GAP 291,000 (COMPUTED)"))
p["beats"] = [
 beat("القرار", "من الأحد: 2,000 دولار كل شهرين",
  "البنك المركزي: حصة المسافر 2,000 دولار بالسعر الرسمي كل شهرين، وبحد أقصى 6 مرات بالسنة، اعتباراً من الأحد 18 تشرين الأول (964، شفق نيوز).",
  "2,000", "US dollars per traveller every two months at the official rate, from 18 October (CBI statement via 964 / Shafaq)", "دولار للمسافر كل شهرين",
  [("الدورية", "كل شهرين"), ("الحد الأقصى", "6 مرات بالسنة"), ("يبدأ", "الأحد 18 تشرين الأول")], 1, slug,
  ["2,000 دولار للمسافر", "كل شهرين", "من الأحد 18 تشرين الأول"], GEN),
 beat("بالسنة", "12 ألف دولار بالسنة.. بدل 24 ألف",
  "في تموز خُفّض السقف إلى 2,000 دولار شهرياً بدل 3,000 (شفق نيوز، الجزيرة). بالآلية الجديدة الحد الأقصى 12,000 دولار بالسنة بدل 24,000 (محتسب).",
  "12,000", "US dollars a year maximum per traveller under the new rule (6 × $2,000), vs up to $24,000 under the monthly cap (computed)", "دولار بالسنة حداً أقصى (محتسب)",
  [("تموز", "2,000 شهرياً"), ("الآن", "2,000 كل شهرين"), ("السنة", "12,000 (محتسب)")], 2, slug,
  ["تموز: 2,000 كل شهر", "الآن: كل شهرين", "12 ألف بالسنة بدل 24"], GEN),
 beat("الفرق", "الفرق عن السوق: 291 ألف دينار",
  "بورصة الكفاح أغلقت الخميس على 166,550 لكل 100 دولار (شفق نيوز). الـ2,000 دولار بالسعر الرسمي 3,040,000 دينار، وبالسوق 3,331,000: فرق 291,000 (محتسب).",
  "291,000", "IQD difference on $2,000 between the official rate (1,520) and Thursday's Kifah close (166,550 per $100) — computed", "دينار فرق الحصة بين الرسمي والسوق (محتسب)",
  [("الرسمي", "3,040,000"), ("السوق", "3,331,000"), ("إغلاق الخميس", "166,550")], 3, slug,
  ["الكفاح: 166,550 إغلاق الخميس", "الحصة بالرسمي 3,040,000", "فرق 291 ألف دينار"], GEN),
]
p["arabicTicker"] = [
 "البنك المركزي: 2,000 دولار للمسافر كل شهرين وبحد أقصى 6 مرات سنوياً — من الأحد 18 تشرين الأول (964، شفق نيوز)",
 "الحد الأقصى بالسنة 12,000 دولار بدل 24,000 بالسقف الشهري (محتسب)",
 "إغلاق الخميس: الكفاح والحارثية 166,550 دينار لكل 100 دولار (شفق نيوز)",
 "مسافر خلال الشهرين الجايين؟",
]
p["endQuestion"] = "مسافر خلال الشهرين الجايين؟"
p["sources"] = [{"name": "البنك المركزي العراقي", "domain": "cbi.iq"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "الجزيرة نت", "domain": "aljazeera.net"}]
SLATE[slug] = (p, {
 "kicker": "الدولار اليوم", "hookHeadline": "دولار السفر: كل شهرين بس",
 "voText": ("أعلن البنك المركزي آلية جديدة لدولار المسافرين: ألفا دولار بالسعر الرسمي كل شهرين، وبحد أقصى ست مرات في السنة، اعتباراً من الأحد الثامن عشر من تشرين الأول. "
            "وكان السقف منذ تموز ألفي دولار شهرياً، أي أن الحد الأقصى السنوي ينخفض إلى اثني عشر ألف دولار. "
            "وأغلقت بورصة الكفاح الخميس على مئة وستة وستين ألفاً وخمسمئة وخمسين ديناراً لكل مئة دولار، فيصبح فرق الحصة عن السوق نحو مئتين وواحد وتسعين ألف دينار. "
            "مسافر خلال الشهرين الجايين؟"),
 "endQuestion": "مسافر خلال الشهرين الجايين؟",
 "sourcesLine": "المصادر: البنك المركزي عبر شبكة 964 وشفق نيوز · الجزيرة نت — 15 تشرين الأول 2026",
 "statPops": [{"value": "$2,000", "label": "للمسافر كل شهرين", "matchWord": "المسافرين"},
              {"value": "291,000", "label": "دينار فرق الحصة عن السوق (محتسب)", "matchWord": "الحصة"}],
}, """دولار المسافرين في العراق — شنو تغيّر من الأحد؟

الحصة الجديدة، وكم تساوي بالسوق.. بالفيديو.

مسافر خلال الشهرين الجايين؟

المصادر: البنك المركزي العراقي عبر شبكة 964 وشفق نيوز (15 تشرين الأول 2026)

#دولار_المسافرين #سعر_الدولار #البنك_المركزي #العراق #photonectnews
@photonect.news
""")

# ═══════════ C · 21:15 · P2 US–Iran sanctions on an Iraqi bank (V10.1 CONTROL) ═══════════
slug = f"{D}-c-us-sanctions-iraqi-bank"
p = base(slug, "mena_economy", "A", "عقوبات", "عقوبات أميركية على مصرف عراقي.. ليش؟",
  ("WASHINGTON / BAGHDAD · OCT 15 | US TREASURY (STATEMENT VIA 964, BAGHDAD TODAY) DESIGNATED IRAQ-BASED INTERNATIONAL DEVELOPMENT BANK FOR INVESTMENT AND FINANCE (IDB) UNDER EO 13902 | "
   "TREASURY ALLEGES IDB GAVE IRAN ACCESS TO US DOLLARS, MISUSED ITS ACCESS TO THE NOW-DISSOLVED DOLLAR AUCTION AND KEEPS TIES WITH IRANIAN GOVERNMENT ENTITIES AND IRAN-ALIGNED ARMED GROUPS | "
   "CONSEQUENCES PER TREASURY: US-LINKED PROPERTY BLOCKED, ENTITIES 50%+ OWNED BY DESIGNATED PERSONS ALSO BLOCKED, FOREIGN BANKS RISK SECONDARY SANCTIONS"))
p["beats"] = [
 beat("القرار", "الخزانة الأميركية تعاقب «مصرف التنمية الدولي»",
  "وزارة الخزانة الأميركية أدرجت الخميس «مصرف التنمية الدولي للاستثمار والتمويل» ومقره العراق على قائمة العقوبات، بموجب الأمر التنفيذي 13902 (964، بغداد اليوم).",
  "13902", "US executive order under which Treasury designated Iraq-based IDB on 15 October (Treasury statement via 964)", "رقم الأمر التنفيذي الأميركي",
  [("الجهة", "الخزانة الأميركية"), ("المصرف", "مقره العراق"), ("التاريخ", "15 تشرين الأول")], 1, slug,
  ["الخزانة الأميركية تعاقب مصرفاً عراقياً", "مصرف التنمية الدولي", "بموجب الأمر 13902"], GEN),
 beat("الاتهام", "بحسب واشنطن: دولار لإيران",
  "بحسب بيان الخزانة: المصرف وفّر لإيران وصولاً إلى الدولار، وأساء استخدام مزاد العملة المنحلّ، وله علاقات بكيانات حكومية إيرانية وفصائل مسلحة. ولم نجد رداً منشوراً للمصرف.",
  "1", "Iraq-based bank designated in this package, per the Treasury statement (via 964 / Baghdad Today)", "مصرف عراقي ضمن حزمة الخميس",
  [("الاتهام 1", "دولار لإيران"), ("الاتهام 2", "مزاد العملة"), ("المصدر", "بيان الخزانة")], 2, slug,
  ["الخزانة: دولار لإيران", "وإساءة استخدام مزاد العملة", "اتهامات بحسب واشنطن"], GEN),
 beat("الأثر", "شنو يعني؟ تجميد.. وتحذير للمصارف",
  "بحسب الخزانة: تُجمّد أصول المصرف المرتبطة بأميركا، وكذلك أي كيان يملكه المُدرَجون بنسبة 50% فأكثر، والمصارف الأجنبية المتعاملة معه تخاطر بعقوبات ثانوية.",
  "50%", "Ownership threshold: entities 50%+ owned by designated persons are also blocked (Treasury statement via 964)", "ملكية تكفي لتجميد الكيان التابع",
  [("الأصول", "تُجمّد"), ("الكيانات التابعة", "50% فأكثر"), ("المصارف الأجنبية", "عقوبات ثانوية")], 3, slug,
  ["تجميد الأصول", "وكل كيان مملوك 50% فأكثر", "وتحذير للمصارف المتعاملة"], GEN),
]
p["arabicTicker"] = [
 "الخزانة الأميركية تدرج «مصرف التنمية الدولي للاستثمار والتمويل» ومقره العراق على قائمة العقوبات (964، بغداد اليوم)",
 "بحسب بيان الخزانة: المصرف وفّر لإيران وصولاً إلى الدولار وأساء استخدام مزاد العملة المنحلّ",
 "الأثر بحسب الخزانة: تجميد الأصول المرتبطة بأميركا وخطر عقوبات ثانوية على المصارف المتعاملة",
 "عندك حساب بمصرف أهلي؟",
]
p["endQuestion"] = "عندك حساب بمصرف أهلي؟"
p["sources"] = [{"name": "وزارة الخزانة الأميركية", "domain": "treasury.gov"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}]
SLATE[slug] = (p, None, """عقوبات أميركية على مصرف عراقي — شنو القصة؟

الاتهام بحسب واشنطن، وشنو يعني القرار.. بالفيديو.

عندك حساب بمصرف أهلي؟

المصادر: بيان وزارة الخزانة الأميركية عبر شبكة 964 وبغداد اليوم (15 تشرين الأول 2026)

#عقوبات #المصارف #العراق #photonectnews
@photonect.news
""")

# ═══════════ D · 22:30 · P1 accountability — Rafidain cashier jailed 6 years for customers' savings ═══════════
slug = f"{D}-d-rafidain-cashier-6-years"
p = base(slug, "iraq_money", "B", "النزاهة", "فلوس الزبائن بالرافدين.. 6 سنين سجن",
  ("BAGHDAD · OCT 15 | RUSAFA CRIMINAL COURT FOR INTEGRITY CASES SENTENCED A RAFIDAIN BANK CASHIER TO 6 YEARS AFTER CONVICTING HIM OF EMBEZZLING FROM INDIVIDUAL SAVINGS CUSTOMERS' ACCOUNTS "
   "BY MANIPULATING THEM; ORDERED TO RETURN THE FUNDS; ARTICLE 315 OF THE PENAL CODE (SUPREME JUDICIAL COUNCIL MEDIA, 964) | KIRKUK: INTEGRITY COMMISSION CAUGHT THE HEAD OF THE 4TH MUNICIPAL SECTOR "
   "RECEIVING PART OF A BRIBE — $6,000 + AN IPHONE 18 PRO MAX DEMANDED TO ALLOW A COMMERCIAL BUILDING ON AL-QUDS STREET; DETAINED PENDING INVESTIGATION, NOT CONVICTED (SHAFAQ, BAGHDAD TODAY)"))
p["beats"] = [
 beat("الحكم", "أمين صندوق بالرافدين: 6 سنين سجن",
  "محكمة جنايات الرصافة المختصة بقضايا النزاهة حكمت بالسجن 6 سنوات على أمين صندوق في مصرف الرافدين، بعد إدانته باختلاس أموال من حسابات زبائن التوفير (إعلام القضاء، 964).",
  "6", "Years in prison for a Rafidain Bank cashier convicted of embezzling customers' savings (Supreme Judicial Council media / 964)", "سنوات سجن — حكم جنايات الرصافة",
  [("المحكمة", "جنايات الرصافة"), ("المدان", "أمين صندوق"), ("الضحايا", "زبائن التوفير")], 1, slug,
  ["6 سنين سجن", "لأمين صندوق بالرافدين", "اختلس من حسابات التوفير"], GEN),
 beat("الطريقة", "تلاعب بأرصدة الزبائن",
  "بحسب إعلام القضاء: استغل وظيفته أميناً للصندوق وتلاعب بحسابات الزبائن واستحوذ على مبالغ من أرصدتهم. والمحكمة ألزمته بإعادة الأموال المختلسة، وفق المادة 315.",
  "315", "Article of the Iraqi Penal Code under which the cashier was sentenced (Supreme Judicial Council media)", "المادة من قانون العقوبات",
  [("الأسلوب", "تلاعب بالحسابات"), ("الأموال", "يعيدها"), ("المادة", "315")], 2, slug,
  ["تلاعب بالحسابات", "واستحوذ على الأرصدة", "وملزم بإعادة الأموال"], GEN),
 beat("كركوك", "وبكركوك: 6 آلاف دولار وآيفون",
  "هيئة النزاهة: ضُبط مسؤول القاطع البلدي الرابع في كركوك متلبساً بتسلّم جزء من رشوة، 6,000 دولار وآيفون، مقابل السماح ببناء عمارة. موقوف على ذمة التحقيق ولم يُحكم (شفق، بغداد اليوم).",
  "6,000", "US dollars plus an iPhone allegedly demanded by a Kirkuk municipal official, per the Integrity Commission (via Shafaq / Baghdad Today) — detained, not convicted", "دولار + آيفون — المطلوب بحسب النزاهة",
  [("المكان", "شارع القدس"), ("المقابل", "بناء عمارة"), ("الحالة", "موقوف، لم يُحكم")], 3, slug,
  ["كركوك: 6 آلاف دولار وآيفون", "مقابل رخصة عمارة", "موقوف على ذمة التحقيق"], GEN),
]
p["arabicTicker"] = [
 "جنايات الرصافة: السجن 6 سنوات لأمين صندوق في مصرف الرافدين بعد إدانته باختلاس أموال زبائن التوفير (إعلام القضاء، 964)",
 "المحكمة ألزمت المدان بإعادة الأموال المختلسة",
 "النزاهة: ضبط مسؤول القاطع البلدي الرابع في كركوك متلبساً بتسلم جزء من رشوة — موقوف على ذمة التحقيق",
 "تتابع رصيد حسابك كل شهر؟",
]
p["endQuestion"] = "تتابع رصيد حسابك كل شهر؟"
p["sources"] = [{"name": "مجلس القضاء الأعلى", "domain": "sjc.iq"}, {"name": "هيئة النزاهة الاتحادية", "domain": "nazaha.iq"},
                {"name": "شبكة 964", "domain": "964media.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}]
SLATE[slug] = (p, {
 "kicker": "النزاهة", "hookHeadline": "فلوس الزبائن بالرافدين.. وين راحت؟",
 "voText": ("أصدرت محكمة جنايات الرصافة المختصة بقضايا النزاهة حكماً بالسجن ست سنوات على أمين صندوق في مصرف الرافدين، بعد إدانته باختلاس أموال من حسابات زبائن التوفير عبر التلاعب بأرصدتهم، وألزمته بإعادة الأموال، بحسب إعلام القضاء. "
            "وفي كركوك أعلنت هيئة النزاهة ضبط مسؤول القاطع البلدي الرابع متلبساً بتسلم جزء من رشوة، ستة آلاف دولار وهاتف آيفون، مقابل السماح ببناء عمارة، وهو موقوف على ذمة التحقيق. "
            "تتابع رصيد حسابك كل شهر؟"),
 "endQuestion": "تتابع رصيد حسابك كل شهر؟",
 "sourcesLine": "المصادر: مجلس القضاء الأعلى · هيئة النزاهة · شبكة 964 · شفق نيوز · بغداد اليوم — 15 تشرين الأول 2026",
 "statPops": [{"value": "6", "label": "سنوات سجن لأمين الصندوق", "matchWord": "الرصافة"},
              {"value": "$6,000", "label": "+ آيفون — المطلوب بحسب النزاهة", "matchWord": "آيفون"}],
}, """اختلاس من حسابات زبائن مصرف الرافدين — شنو كان الحكم؟

والرشوة اللي انضبطت بكركوك.. بالفيديو.

تتابع رصيد حسابك كل شهر؟

المصادر: مجلس القضاء الأعلى عبر شبكة 964، هيئة النزاهة عبر شفق نيوز وبغداد اليوم (15 تشرين الأول 2026)

#مصرف_الرافدين #النزاهة #كركوك #العراق #photonectnews
@photonect.news
""")

# ═══════════ E · 23:45 · P3 weather — rain and lightning in the north, 40°C in the south, cooler from Monday ═══════════
slug = f"{D}-e-rain-north-40-south"
p = base(slug, "iraq_society", "C", "الطقس", "مطر بالشمال.. و40 درجة بالجنوب",
  ("BAGHDAD · OCT 16 | IRAQI METEOROLOGICAL AUTHORITY (VIA 964): FRIDAY CLOUDY WITH LIGHT-TO-MODERATE THUNDERY RAIN IN THE CENTRE AND NORTH; SOUTH CLEAR | MAX 28°C IN DUHOK, 40°C IN BASRA, MAYSAN, DHI QAR, MUTHANNA | "
   "TEMPERATURES DROP SEVERAL DEGREES FROM MONDAY WITH NW WINDS UP TO 40 KM/H; INTERMITTENT RAIN UNTIL MID-WEEK | FORECASTER SADIQ ATTIYA (VIA SHAFAQ): RAIN WITH LIGHTNING IN NINEVEH, ERBIL, DUHOK, SULAYMANIYAH; "
   "HEAVY POCKETS FRIDAY NIGHT/SATURDAY IN PARTS OF ANBAR; CAUTION FOR DOWNDRAFT WINDS AND LIGHTNING"))
p["beats"] = [
 beat("اليوم", "الشمال والوسط: مطر ورعد",
  "الأنواء الجوية: أجواء غائمة مع مطر خفيف إلى معتدل ورعد متفرق في المنطقتين الوسطى والشمالية، والجنوب صحو مع بعض الغيوم (964).",
  "28", "°C — Friday's lowest maximum, in Duhok (Meteorological Authority via 964)", "درجة — العظمى في دهوك",
  [("الشمال", "مطر ورعد"), ("الوسط", "مطر متفرق"), ("الجنوب", "صحو")], 1, slug,
  ["مطر ورعد بالشمال والوسط", "والجنوب صحو", "دهوك: 28 درجة"], GEN),
 beat("البؤر", "وين المطر أغزر؟",
  "الراصد صادق عطية: أمطار مع برق ورعد في نينوى وأربيل ودهوك والسليمانية، وبؤر غزارة ليل الجمعة/السبت في مناطق من الأنبار، مع الحذر من الرياح الهابطة والصواعق (شفق نيوز).",
  "4", "Northern provinces named for rain with lightning: Nineveh, Erbil, Duhok, Sulaymaniyah (forecaster Sadiq Attiya via Shafaq)", "محافظات شمالية بمطر وبرق",
  [("الشمال", "4 محافظات"), ("الأنبار", "بؤر غزارة"), ("الحذر", "الصواعق")], 2, slug,
  ["نينوى وأربيل ودهوك والسليمانية", "بؤر غزارة بالأنبار", "احذر الصواعق"], GEN),
 beat("الجنوب", "البصرة 40.. ومن الإثنين تنزل",
  "العظمى 40 درجة في البصرة وميسان وذي قار والمثنى. ومن الإثنين تنخفض الحرارة عدة درجات مع رياح شمالية غربية حتى 40 كم/ساعة، والمطر متقطع حتى منتصف الأسبوع (964).",
  "40", "°C maximum in Basra, Maysan, Dhi Qar and Muthanna on Friday (Meteorological Authority via 964)", "درجة — العظمى بالجنوب",
  [("الجنوب", "40°"), ("من الإثنين", "انخفاض"), ("الرياح", "40 كم/ساعة")], 3, slug,
  ["البصرة 40 درجة", "ومن الإثنين تنخفض", "والمطر لمنتصف الأسبوع"], GEN),
]
p["arabicTicker"] = [
 "الأنواء الجوية: مطر خفيف إلى معتدل ورعد متفرق في الوسط والشمال (964)",
 "العظمى من 28 درجة في دهوك إلى 40 في البصرة وميسان وذي قار والمثنى",
 "من الإثنين: انخفاض الحرارة عدة درجات ورياح حتى 40 كم/ساعة",
 "نزل مطر عندكم اليوم؟",
]
p["endQuestion"] = "نزل مطر عندكم اليوم؟"
p["sources"] = [{"name": "الهيئة العامة للأنواء الجوية", "domain": "meteoseism.gov.iq"}, {"name": "شبكة 964", "domain": "964media.com"},
                {"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = (p, {
 "kicker": "الطقس", "hookHeadline": "مطر بالشمال.. و40 بالجنوب",
 "voText": ("بحسب الهيئة العامة للأنواء الجوية، تشهد المنطقتان الوسطى والشمالية اليوم أجواء غائمة مع مطر خفيف إلى معتدل ورعد متفرق، بينما يبقى الجنوب صحواً، والعظمى تصل إلى أربعين درجة في البصرة وميسان وذي قار والمثنى. "
            "ويتوقع الراصد صادق عطية برقاً ورعداً في نينوى وأربيل ودهوك والسليمانية، وبؤر غزارة في مناطق من الأنبار، مع الحذر من الصواعق. "
            "ومن الإثنين تنخفض الحرارة عدة درجات. نزل مطر عندكم اليوم؟"),
 "endQuestion": "نزل مطر عندكم اليوم؟",
 "sourcesLine": "المصادر: الهيئة العامة للأنواء الجوية عبر شبكة 964 · شفق نيوز — 15 و16 تشرين الأول 2026",
 "statPops": [{"value": "40°", "label": "العظمى بالبصرة وميسان وذي قار والمثنى", "matchWord": "أربعين"},
              {"value": "4", "label": "محافظات شمالية بمطر وبرق", "matchWord": "السليمانية"}],
}, """طقس العراق اليوم — مطر بالشمال وحر بالجنوب؟

وين المطر أغزر، ومتى تنزل الحرارة.. بالفيديو.

نزل مطر عندكم اليوم؟

المصادر: الهيئة العامة للأنواء الجوية عبر شبكة 964، شفق نيوز (15 و16 تشرين الأول 2026)

#طقس_العراق #أمطار #العراق #photonectnews
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
