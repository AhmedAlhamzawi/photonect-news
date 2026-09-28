#!/usr/bin/env python3
"""Author the 2026-09-28 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source published 27-28 Sep 2026. Computed figures carry (محتسب).
All 20 frames are Commons/Pexels real photos (KIE 11.5 credits, Higgsfield 0.38) — see _image_credits_2026_09_28.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-28"
DATE_LABEL = "SEP 28 • 2026"
AR_DATE = "28 أيلول 2026"
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

# ═══════════ A · 18:00 · P1 state banks probe (LEAD) ═══════════
slug = f"{D}-a-state-banks-loans-probe"
p = base(slug, "iraq_money", "A", "المصارف الحكومية", "قروض وسلف المصارف الحكومية تحت التحقيق.. شنو القصة؟",
  ("BAGHDAD · SEP 28 | IRAQ'S FINANCE MINISTRY ORDERED A COMMITTEE TO INVESTIGATE AND AUDIT LOANS, ADVANCES AND "
   "INSURANCE AMOUNTS LINKED TO E-LENDING, FALLING LIQUIDITY, FOREIGN BRANCHES AND INVESTMENT PROJECTS USED TO GRANT "
   "FACILITIES, AND CONTRACTS (MINISTRY DOCUMENT VIA SHAFAQ NEWS) | REPORT GOES TO THE MINISTRY'S OVERSIGHT UNITS, THE "
   "CENTRAL BANK, THE FEDERAL BOARD OF SUPREME AUDIT AND THE INTEGRITY COMMISSION | SOURCES: EARLIER PROBES FOCUSED ON "
   "RAFIDAIN AND RASHEED BANKS (SHAFAQ; AL-MUSTAQILA) | AL-MUSTAQILA: AMOUNTS UNDER AUDIT NOT DETERMINED; NO OFFICIAL "
   "FINDINGS HOLD ANY PERSON OR BODY RESPONSIBLE"))
p["beats"] = [
 beat("اللجنة", "المالية تفتح 5 ملفات بالمصارف",
  "وزارة المالية وجّهت بتشكيل لجنة تحقيق وتدقيق بالقروض والسلف، وأقساط التأمين الخاصة بالتسليف الإلكتروني، وانخفاض السيولة، والفروع الخارجية، والعقود (وثيقة عبر شفق نيوز).",
  "5", "Files before the Finance Ministry's audit committee (ministry document via Shafaq News; count computed)",
  "ملفات أمام لجنة التحقيق (وثيقة المالية — محتسب)",
  [("القروض والسلف", "تحت التدقيق"), ("السيولة", "تحت التدقيق"), ("العقود", "تحت التدقيق")], 1, slug,
  ["لجنة تحقيق بالمالية", "القروض والسلف", "والسيولة والعقود"], STOCK),
 beat("المصارف", "الرافدين والرشيد بصدارة التدقيق",
  "حسب شفق نيوز والمستقلة، تحقيقات سابقة للنزاهة والجهات الرقابية ركّزت على السيولة والقروض والموافقات الاستثنائية، خصوصاً بمصرفي الرافدين والرشيد.",
  "2", "State banks at the centre of earlier probes: Rafidain and Rasheed (Shafaq News; Al-Mustaqila)",
  "مصرفان بصدارة التدقيق: الرافدين والرشيد (شفق نيوز، المستقلة)",
  [("الرافدين", "مشمول"), ("الرشيد", "مشمول"), ("الفروع الخارجية", "مشمولة")], 2, slug,
  ["الرافدين والرشيد", "السيولة والقروض", "والموافقات الاستثنائية"], STOCK),
 beat("النتائج", "التقرير يروح لـ4 جهات رقابية",
  "التقرير يُرفع لرقابة المالية والبنك المركزي وديوان الرقابة المالية والنزاهة. والمستقلة تقول إن المبالغ لم تُحدَّد ولم تصدر نتائج رسمية تُحمّل أحداً المسؤولية.",
  "4", "Oversight bodies that will receive the committee's report (Finance Ministry document)",
  "جهات رقابية يُرفع لها التقرير (وثيقة المالية)",
  [("المبالغ", "غير محددة"), ("النتائج", "لم تصدر"), ("المسؤولية", "لم تُحدَّد")], 3, slug,
  ["التقرير لـ4 جهات", "المبالغ ما انعرفت", "والنتائج ما صدرت"], STOCK),
]
p["arabicTicker"] = [
 "وزارة المالية توجّه بتشكيل لجنة للتحقيق والتدقيق في ملفات القروض والسلف والسيولة والفروع الخارجية للمصارف (وثيقة — شفق نيوز، 28 أيلول)",
 "اللجنة تدقق أقساط التأمين المرتبطة بالتسليف الإلكتروني والمشاريع الاستثمارية التي مُنحت على أساسها التسهيلات",
 "التقرير يُرفع إلى الجهات الرقابية في المالية والبنك المركزي وديوان الرقابة المالية الاتحادي وهيئة النزاهة",
 "مصدر لشفق نيوز: ضغوط للتأثير في عمل لجان التحقيق المشكّلة في المصارف الحكومية",
 "المستقلة: لم يتسنَّ تحديد إجمالي المبالغ محل التدقيق، ولم تصدر نتائج رسمية تحمّل جهات بعينها المسؤولية",
 "أخذت سلفة من مصرف حكومي؟"]
p["endQuestion"] = "أخذت سلفة من مصرف حكومي؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "المستقلة", "domain": "mustaqila.com"}, {"name": "وزارة المالية", "domain": "mof.gov.iq"}]
SLATE[slug] = {"props": p, "caption": """المصارف الحكومية في العراق — ليش لجنة تحقيق بالقروض والسلف؟

الرافدين والرشيد والسيولة والفروع الخارجية.. التفاصيل بالفيديو.

أخذت سلفة من مصرف حكومي؟

المصادر: وثيقة وزارة المالية عبر شفق نيوز، المستقلة (28 أيلول 2026)

#العراق #مصرف_الرافدين #السلف #المصارف_الحكومية #photonectnews
@photonect.news""",
 "brief": {"kicker": "المصارف الحكومية", "hookHeadline": "قروض المصارف الحكومية تحت التحقيق",
  "voText": "وجّهت وزارة المالية، اليوم الاثنين، بتشكيل لجنة للتحقيق والتدقيق في المصارف الحكومية، بحسب وثيقة نشرتها شفق نيوز. وتشمل مهام اللجنة ملفات القروض والسلف، وأقساط التأمين الخاصة بالتسليف الإلكتروني، وانخفاض السيولة، والفروع الخارجية، والعقود. وسيُرفع التقرير إلى البنك المركزي وديوان الرقابة المالية وهيئة النزاهة. وتقول المستقلة إن التدقيق يتركز خصوصاً في مصرفي الرافدين والرشيد، وإن المبالغ لم تُحدَّد، ولم تصدر نتائج رسمية تحمّل أحداً المسؤولية. أخذت سلفة من مصرف حكومي؟",
  "endQuestion": "أخذت سلفة من مصرف حكومي؟",
  "sourcesLine": "المصادر: وثيقة وزارة المالية عبر شفق نيوز · المستقلة — 28 أيلول 2026",
  "statPops": [{"value": "5", "label": "ملفات تحت التدقيق (محتسب)", "matchWord": "والعقود"},
               {"value": "2", "label": "مصرفان بالصدارة: الرافدين والرشيد", "matchWord": "الرافدين"}]}}

# ═══════════ B · 19:45 · P1 dollar anchor ═══════════
slug = f"{D}-b-dollar-156000-back-up"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار رجع يصعد: 156 ألف بالبورصة",
  ("BAGHDAD · SEP 28 | SHAFAQ NEWS: KIFAH & HARITHIYA BOURSES 156,000 IQD PER $100 MONDAY MORNING, UP FROM 155,250 "
   "ON SUNDAY (+750, COMPUTED) | BAGHDAD EXCHANGE SHOPS: SELL 156,500 / BUY 155,500; ERBIL SELL 156,300 / BUY 156,200 "
   "| OFFICIAL CENTRAL BANK RATE: 131,000 IQD PER $100 (964) | BOURSE PREMIUM OVER OFFICIAL RATE: 25,000 IQD (COMPUTED)"))
p["beats"] = [
 beat("البورصة", "156,000 صباح الاثنين",
  "شفق نيوز: بورصتا الكفاح والحارثية سجّلتا صباح اليوم 156,000 دينار لكل 100 دولار، بعد 155,250 أمس الأحد.",
  "156,000", "IQD per $100, Kifah & Harithiya bourses, Monday morning (Shafaq News)",
  "دينار لكل 100 دولار — الكفاح والحارثية صباح الاثنين (شفق نيوز)",
  [("الأحد", "155,250"), ("الفرق", "750+ (محتسب)"), ("الاتجاه", "صعود")], 1, slug,
  ["الدولار رجع يصعد", "156,000 دينار", "أمس كان 155,250"], STOCK),
 beat("الصيرفة", "محلات بغداد تبيع بـ156,500",
  "محال الصيرفة ببغداد: البيع 156,500 والشراء 155,500. وبأربيل: البيع 156,300 والشراء 156,200 (شفق نيوز).",
  "156,500", "IQD per $100, Baghdad exchange-shop selling price, Monday morning (Shafaq News)",
  "دينار سعر البيع لكل 100 دولار بمحلات بغداد (شفق نيوز)",
  [("بغداد شراء", "155,500"), ("أربيل بيع", "156,300"), ("أربيل شراء", "156,200")], 2, slug,
  ["البيع 156,500", "الشراء 155,500", "وأربيل 156,300"], STOCK),
 beat("الرسمي", "الفرق عن الرسمي: 25 ألف",
  "السعر الرسمي للبنك المركزي 131,000 دينار لكل 100 دولار (شبكة 964)، يعني سعر البورصة اليوم أعلى منه بـ25,000 دينار (محتسب).",
  "25,000", "IQD gap per $100 between today's bourse rate and the official central-bank rate (computed)",
  "دينار فرق البورصة عن السعر الرسمي لكل 100 دولار (محتسب)",
  [("الرسمي", "131,000"), ("البورصة", "156,000"), ("الفرق", "25,000 (محتسب)")], 3, slug,
  ["الرسمي 131 ألف", "البورصة 156 ألف", "الفرق 25 ألف"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الدولار في بورصتي الكفاح والحارثية 156,000 دينار لكل 100 دولار صباح الاثنين، بعد 155,250 الأحد",
 "محال الصيرفة ببغداد: البيع 156,500 والشراء 155,500 — أربيل: البيع 156,300 والشراء 156,200",
 "السعر الرسمي المقرر من البنك المركزي: 131,000 دينار لكل 100 دولار (شبكة 964)",
 "سعر الصيرفة بمنطقتك كم اليوم؟"]
p["endQuestion"] = "سعر الصيرفة بمنطقتك كم اليوم؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — رجع يصعد؟

البورصة والصيرفة والفرق عن السعر الرسمي.. التفاصيل بالفيديو.

سعر الصيرفة بمنطقتك كم اليوم؟

المصادر: شفق نيوز، شبكة 964 (28 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "الدولار رجع يصعد اليوم",
  "voText": "عاد سعر الدولار إلى الارتفاع في بغداد صباح اليوم الاثنين. وبحسب شفق نيوز، سجّلت بورصتا الكفاح والحارثية مئة وستة وخمسين ألف دينار لكل مئة دولار، بعد مئة وخمسة وخمسين ألفاً ومئتين وخمسين أمس الأحد. وفي محال الصيرفة ببغداد، بلغ سعر البيع مئة وستة وخمسين ألفاً وخمسمئة دينار. أما السعر الرسمي للبنك المركزي فهو مئة وواحد وثلاثون ألف دينار، أي أن سعر البورصة أعلى منه بخمسة وعشرين ألفاً. سعر الصيرفة بمنطقتك كم اليوم؟",
  "endQuestion": "سعر الصيرفة بمنطقتك كم اليوم؟",
  "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 28 أيلول 2026",
  "statPops": [{"value": "156,000", "label": "بورصة الكفاح — صباح الاثنين", "matchWord": "والحارثية"},
               {"value": "25,000", "label": "فرق البورصة عن الرسمي (محتسب)", "matchWord": "بخمسة"}]}}

# ═══════════ C · 21:15 · P2 Basra crude discount (V10.1 CONTROL) ═══════════
slug = f"{D}-c-basra-crude-28-discount"
p = base(slug, "mena_geo", "A", "النفط", "برنت فوق 105$.. وخام البصرة يُباع بخصم 28$",
  ("NEW DELHI / LONDON · SEP 28 | REUTERS (VIA SHAFAQ NEWS): INDIAN OIL CORP BOUGHT 2 MILLION BARRELS OF BASRAH MEDIUM "
   "AND BASRAH HEAVY FROM MERCURIA AT ABOUT $28/BBL BELOW OCTOBER DUBAI QUOTES, FOB, FOR 21-31 OCT DELIVERY, PER TWO "
   "TRADE SOURCES | BASRAH GRADES FELL MORE THAN $9/BBL IN LAST WEEK'S FINAL SESSION | BRENT +1.27% TO $105.64 AFTER "
   "TRUMP REJECTED AN IRANIAN PEACE PROPOSAL (REUTERS VIA SHAFAQ; 964) | KPLER: MIDEAST CRUDE EXPORTS 12.8M BPD IN "
   "SEPTEMBER, HIGHEST SINCE THE WAR BEGAN IN FEBRUARY, STILL ~6M BPD BELOW FEBRUARY'S 18.8M"))
p["beats"] = [
 beat("الصفقة", "الهند تشتري البصرة بخصم 28$",
  "رويترز عبر شفق نيوز: مؤسسة النفط الهندية اشترت مليوني برميل من خامي البصرة المتوسط والثقيل من شركة ميركوريا بخصم نحو 28 دولاراً عن خام دبي.",
  "$28", "Approx. discount per barrel to Dubai quotes in Indian Oil's purchase of Basrah grades from Mercuria (Reuters)",
  "خصم للبرميل عن سعر دبي بصفقة الهند (رويترز)",
  [("الكمية", "2 مليون برميل"), ("البائع", "ميركوريا"), ("التسليم", "21-31 تشرين الأول")], 1, slug,
  ["خام البصرة", "بخصم 28 دولار", "للبرميل الواحد"], STOCK),
 beat("برنت", "برنت يرجع فوق 105$",
  "رويترز: برنت صعد 1.27% إلى 105.64 دولار للبرميل صباح الاثنين، بعد رفض ترامب مقترح سلام إيرانياً، مع توقعه محادثات جديدة هذا الأسبوع.",
  "$105.64", "Brent crude futures per barrel, early Monday trade (Reuters via Shafaq News, 964)",
  "دولار لبرميل برنت صباح الاثنين (رويترز)",
  [("الارتفاع", "1.27%"), ("غرب تكساس", "93.11$"), ("السبب", "رفض المقترح الإيراني")], 2, slug,
  ["برنت 105 دولار", "بعد رفض ترامب", "للمقترح الإيراني"], STOCK),
 beat("الصادرات", "صادرات المنطقة ترتفع.. لكن أقل",
  "كبلر عبر رويترز: صادرات خام كبار منتجي الشرق الأوسط، ومنهم العراق، بلغت 12.8 مليون برميل يومياً بأيلول، الأعلى منذ شباط، وأقل بنحو 6 ملايين من مستواها وقتها.",
  "12.8M", "Barrels a day of crude exported by major Middle East producers in September (Kpler via Reuters)",
  "برميل يومياً صادرات الشرق الأوسط بأيلول (كبلر)",
  [("شباط", "18.8 مليون"), ("الفرق", "~6 ملايين"), ("عبر هرمز", "~7.4 مليون")], 3, slug,
  ["12.8 مليون برميل", "الأعلى من شباط", "بس أقل من قبل"], STOCK),
]
p["arabicTicker"] = [
 "رويترز: مؤسسة النفط الهندية تشتري مليوني برميل من خامي البصرة المتوسط والثقيل بخصم نحو 28 دولاراً عن دبي (شفق نيوز)",
 "خاما البصرة الثقيل والمتوسط تراجعا بأكثر من 9 دولارات للبرميل في آخر جلسات الأسبوع الماضي",
 "برنت يرتفع 1.27% إلى 105.64 دولار بعد رفض ترامب مقترحاً إيرانياً للسلام (رويترز عبر شبكة 964)",
 "كبلر: صادرات خام الشرق الأوسط 12.8 مليون برميل يومياً بأيلول — الأعلى منذ اندلاع الحرب في شباط",
 "تشتغل بقطاع النفط أو عندك أحد بيه؟"]
p["endQuestion"] = "تشتغل بقطاع النفط أو عندك أحد بيه؟"
p["sources"] = [{"name": "رويترز", "domain": "reuters.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """سعر نفط البصرة اليوم — ليش خصم 28 دولار؟

برنت فوق 105 وخام البصرة بخصم كبير.. التفاصيل بالفيديو.

تشتغل بقطاع النفط أو عندك أحد بيه؟

المصادر: رويترز عبر شفق نيوز وشبكة 964 (28 أيلول 2026)

#العراق #نفط_البصرة #النفط #photonectnews
@photonect.news""",
 "brief": None}

# ═══════════ D · 22:30 · P1 accountability / asset recovery ═══════════
slug = f"{D}-d-nazaha-us-asset-recovery"
p = base(slug, "iraq_corruption", "B", "النزاهة", "الأموال المهربة برّا.. النزاهة تبحث استردادها مع واشنطن",
  ("BAGHDAD / MOSUL · SEP 28 | INTEGRITY COMMISSION HEAD MOHAMMED ALI AL-LAMI MET US CHARGÉ D'AFFAIRES STEVEN FAGIN "
   "ON EXPANDING COOPERATION TO PURSUE CORRUPTION SUSPECTS, RECOVER SMUGGLED FUNDS AND EXTRADITE WANTED PERSONS (INA; "
   "964) | AL-LAMI CITED UNCAC CHAPTER V ON ASSET RECOVERY AND URGED REMOVING OBSTACLES: DUAL NATIONALITY, DIFFERING "
   "LAWS, CLAIMS OF POLITICAL TARGETING | NINEVEH (964): SUSPECT HELD OVER ILLICIT ENRICHMENT, LARGE TRANSFERS AND "
   "COMMERCIAL PROPERTY CONTRACTS FOUND IN HIS TWO HOUSES; 3 EXPENSIVE VEHICLES, ONE ARMOURED, SEIZED FROM A DETAINED "
   "SUSPECT WHO CLAIMED A SECURITY AFFILIATION"))
p["beats"] = [
 beat("اللقاء", "النزاهة وواشنطن: ملاحقة الأموال المهربة",
  "رئيس هيئة النزاهة محمد علي اللامي بحث مع القائم بالأعمال الأمريكي ستيفن فاجن توسيع التعاون لاسترداد الأموال المهربة وتسليم المطلوبين (واع، شبكة 964).",
  "5", "UN Convention against Corruption chapter on asset recovery, cited by the Integrity Commission head (INA)",
  "الفصل الخامس من اتفاقية الأمم المتحدة لمكافحة الفساد: استرداد الموجودات (واع)",
  [("الملف", "استرداد الأموال"), ("والثاني", "تسليم المطلوبين"), ("الطرف", "السفارة الأمريكية")], 1, slug,
  ["النزاهة وواشنطن", "الأموال المهربة", "والمطلوبين برّا"], STOCK),
 beat("العقبة", "العقبة: ازدواج الجنسية",
  "اللامي دعا، حسب بيان الهيئة، لإزالة معوقات الاسترداد، مثل ازدواج الجنسية واختلاف التشريعات ومزاعم الاستهداف السياسي.",
  "3", "Obstacles to asset recovery named by the Integrity Commission head (commission statement)",
  "معوقات استرداد ذكرها رئيس الهيئة (بيان النزاهة)",
  [("الأولى", "ازدواج الجنسية"), ("الثانية", "اختلاف التشريعات"), ("الثالثة", "مزاعم الاستهداف")], 2, slug,
  ["ازدواج الجنسية", "اختلاف القوانين", "ومزاعم الاستهداف"], STOCK),
 beat("نينوى", "نينوى: 3 عجلات فارهة إحداها مصفحة",
  "بنينوى، أعلنت النزاهة ضبط متهم بتضخم أمواله وبداريه حوالات وعقود عقارات، وحجز 3 عجلات باهظة إحداها مصفحة لموقوف ادّعى صفة أمنية (شبكة 964).",
  "3", "Expensive vehicles, one armoured, seized from a detained suspect in Nineveh (Integrity Commission)",
  "عجلات باهظة حُجزت إحداها مصفحة — نينوى (هيئة النزاهة)",
  [("المتهم الأول", "تضخم أموال"), ("المضبوطات", "حوالات وعقود"), ("المتهم الثاني", "ادّعى صفة أمنية")], 3, slug,
  ["3 عجلات باهظة", "وحدة منها مصفحة", "وحوالات وعقود"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة والسفارة الأمريكية تبحثان توسيع التعاون في ملاحقة المتورطين بالفساد واسترداد الأموال المهربة (28 أيلول)",
 "اللامي: أهمية إزالة معوقات الاسترداد كازدواج الجنسية واختلاف التشريعات ومزاعم الاستهداف السياسي (واع)",
 "نينوى: ضبط متهم بتضخم أمواله والعثور بداريه على حوالات مالية وعقود شراء عقارات تجارية (شبكة 964)",
 "حجز 3 عجلات باهظة الثمن إحداها مصفحة لموقوف ادّعى الانتساب لأحد الأجهزة الأمنية",
 "بلّغت عن فساد بدائرة حكومية يوماً؟"]
p["endQuestion"] = "بلّغت عن فساد بدائرة حكومية يوماً؟"
p["sources"] = [{"name": "وكالة الأنباء العراقية", "domain": "ina.iq"}, {"name": "شبكة 964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """استرداد الأموال المهربة من العراق — شنو بحثت النزاهة مع واشنطن؟

ازدواج الجنسية عقبة.. وعجلات مصفحة بنينوى. التفاصيل بالفيديو.

بلّغت عن فساد بدائرة حكومية يوماً؟

المصادر: هيئة النزاهة عبر وكالة الأنباء العراقية وشبكة 964 (28 أيلول 2026)

#العراق #النزاهة #الأموال_المهربة #الفساد #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "الأموال المهربة برّا.. شلون ترجع؟",
  "voText": "بحث رئيس هيئة النزاهة محمد علي اللامي، اليوم الاثنين، مع القائم بأعمال السفارة الأمريكية ستيفن فاجن، توسيع التعاون لملاحقة المتورطين بالفساد، واسترداد الأموال المهربة وتسليم المطلوبين. واستند اللامي إلى الفصل الخامس من اتفاقية الأمم المتحدة لمكافحة الفساد، ودعا إلى إزالة معوقات الاسترداد، ومنها ازدواج الجنسية. وفي نينوى، أعلنت الهيئة ضبط متهم بتضخم أمواله، وحجز ثلاث عجلات باهظة الثمن، إحداها مصفحة، لموقوف ادّعى انتسابه لجهاز أمني. بلّغت عن فساد بدائرة حكومية يوماً؟",
  "endQuestion": "بلّغت عن فساد بدائرة حكومية يوماً؟",
  "sourcesLine": "المصادر: هيئة النزاهة عبر وكالة الأنباء العراقية · شبكة 964 — 28 أيلول 2026",
  "statPops": [{"value": "5", "label": "الفصل الخاص باسترداد الأموال — اتفاقية الأمم المتحدة", "matchWord": "الخامس"},
               {"value": "3", "label": "عجلات باهظة إحداها مصفحة — نينوى", "matchWord": "عجلات"}]}}

# ═══════════ E · 23:45 · P3 Gulf Cup 28 hosting (regional pride) ═══════════
slug = f"{D}-e-gulf-cup-28-iraq"
p = base(slug, "region_sport", "C", "خليجي 28", "رسمياً: خليجي 28 بالعراق.. للمرة الثالثة",
  ("JEDDAH · SEP 28 | THE ARAB GULF CUP FOOTBALL FEDERATION'S EXECUTIVE OFFICE AWARDED IRAQ THE 28TH GULF CUP (SHAFAQ "
   "NEWS; EMARAT AL YOUM) | IRAQ FA VICE-PRESIDENT SARMAD ABDUL-ILAH: 9-22 DECEMBER 2028; IRAQ ALSO HOSTS THE GULF "
   "OLYMPIC TEAMS CHAMPIONSHIP IN BASRA, 21 MARCH - 3 APRIL 2027 (SHAFAQNA) | THIRD TIME IRAQ HOSTS: GULF 5 BAGHDAD 1979, "
   "GULF 25 BASRA 2023 | IRAQ, ON 4 POINTS, FACES SAUDI ARABIA ON TUESDAY IN JEDDAH (SHAFAQ)"))
p["beats"] = [
 beat("القرار", "رسمياً: خليجي 28 بالعراق",
  "اتحاد كأس الخليج العربي أعلن اليوم من جدة إقامة خليجي 28 في العراق، من 9 إلى 22 كانون الأول 2028 (شفق نيوز، شفقنا).",
  "2028", "Year of the 28th Gulf Cup, awarded to Iraq on 28 Sep (Arab Gulf Cup Football Federation)",
  "موعد خليجي 28 بالعراق: 9-22 كانون الأول (اتحاد كأس الخليج)",
  [("من", "9 كانون الأول"), ("إلى", "22 كانون الأول"), ("المدن", "تحددها الحكومة")], 1, slug,
  ["خليجي 28", "رسمياً بالعراق", "كانون الأول 2028"], STOCK),
 beat("التاريخ", "ثالث مرة بتاريخ العراق",
  "بعد خليجي 5 ببغداد عام 1979 وخليجي 25 بالبصرة عام 2023، تكون خليجي 28 ثالث نسخة يستضيفها العراق (شفق نيوز، الإمارات اليوم).",
  "3", "Times Iraq has been awarded the Gulf Cup: Baghdad 1979, Basra 2023, and now 2028",
  "مرات استضافة العراق لكأس الخليج (شفق نيوز)",
  [("خليجي 5", "بغداد 1979"), ("خليجي 25", "البصرة 2023"), ("خليجي 28", "2028")], 2, slug,
  ["خليجي 5 ببغداد", "خليجي 25 بالبصرة", "والثالثة 2028"], STOCK),
 beat("البصرة", "والأولمبي الخليجي بالبصرة 2027",
  "العراق يستضيف أيضاً بطولة المنتخبات الأولمبية الخليجية بالبصرة من 21 آذار إلى 3 نيسان 2027. والمنتخب يواجه السعودية غداً وله 4 نقاط.",
  "2027", "Gulf Olympic teams championship in Basra, 21 March - 3 April 2027 (Iraq FA via Shafaqna)",
  "بطولة المنتخبات الأولمبية الخليجية بالبصرة (الاتحاد العراقي)",
  [("من", "21 آذار"), ("إلى", "3 نيسان"), ("نقاط العراق", "4")], 3, slug,
  ["الأولمبي بالبصرة", "آذار 2027", "وغداً السعودية"], STOCK),
]
p["arabicTicker"] = [
 "اتحاد كأس الخليج العربي يعلن إقامة خليجي 28 في العراق عقب اجتماع مكتبه التنفيذي في جدة (28 أيلول)",
 "سرمد عبد الإله: خليجي 28 للفترة من 9 إلى 22 كانون الأول 2028، والحكومة تحدد المدينة والملاعب (شفقنا)",
 "العراق يستضيف بطولة المنتخبات الأولمبية الخليجية في البصرة من 21 آذار إلى 3 نيسان 2027",
 "المنتخب العراقي يواجه السعودية غداً الثلاثاء في جدة وله 4 نقاط من مباراتين (شفق نيوز)",
 "حضرت خليجي 25 بالبصرة؟"]
p["endQuestion"] = "حضرت خليجي 25 بالبصرة؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "الإمارات اليوم", "domain": "emaratalyoum.com"}, {"name": "شفقنا العراق", "domain": "iraq.shafaqna.com"}]
SLATE[slug] = {"props": p, "caption": """خليجي 28 في العراق — رسمياً وين ومتى؟

ثالث استضافة بتاريخ العراق.. والأولمبي الخليجي بالبصرة قبلها. التفاصيل بالفيديو.

حضرت خليجي 25 بالبصرة؟

المصادر: شفق نيوز، الإمارات اليوم، شفقنا العراق (28 أيلول 2026)

#العراق #خليجي_28 #البصرة #كأس_الخليج #photonectnews
@photonect.news""",
 "brief": {"kicker": "خليجي 28", "hookHeadline": "خليجي 28 بالعراق.. رسمياً",
  "voText": "أعلن اتحاد كأس الخليج العربي، اليوم الاثنين من جدة، إقامة بطولة خليجي ثمانية وعشرين في العراق، من التاسع حتى الثاني والعشرين من كانون الأول عام ألفين وثمانية وعشرين. وهي ثالث نسخة يستضيفها العراق، بعد بغداد عام تسعة وسبعين، والبصرة عام ألفين وثلاثة وعشرين. كما منح الاتحاد البصرة استضافة بطولة المنتخبات الأولمبية الخليجية في آذار ألفين وسبعة وعشرين. ويواجه المنتخب السعودية غداً في جدة، وله أربع نقاط. حضرت خليجي خمسة وعشرين بالبصرة؟",
  "endQuestion": "حضرت خليجي خمسة وعشرين بالبصرة؟",
  "sourcesLine": "المصادر: شفق نيوز · الإمارات اليوم · شفقنا العراق — 28 أيلول 2026",
  "statPops": [{"value": "3", "label": "مرات يستضيف العراق كأس الخليج", "matchWord": "ثالث"},
               {"value": "4", "label": "نقاط للعراق قبل مواجهة السعودية", "matchWord": "نقاط"}]}}

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
