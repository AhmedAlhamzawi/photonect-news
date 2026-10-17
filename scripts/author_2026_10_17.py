#!/usr/bin/env python3
"""Author the 2026-10-17 slate: props.json + caption.txt (+ v11-brief.json on a, b, d, e; c = V10.1 control).

Every figure traces to a named source saved in the session scratchpad (Shafaq full-text RSS, 964, Baghdad Today, SJC pages; raw copies in scratchpad/art/).
Computed figures carry (محتسب). PRE-copywriter draft: do NOT re-run after the Opus copywriter/gate edits.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-17"
DATE_LABEL = "OCT 17 • 2026"
AR_DATE = "17 تشرين الأول 2026"
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
PEX = "Pexels"
SRC = lambda *pairs: [{"name": n, "domain": d} for n, d in pairs]


def finish(p, ticker, eq, sources):
    p["arabicTicker"] = ticker + [eq]
    p["endQuestion"] = eq
    p["sources"] = sources
    return p


# ═══════════ A · 18:00 · P1 IMF loan request (LEAD) ═══════════
slug = f"{D}-a-imf-loan-request"
p = base(slug, "iraq_money", "A", "صندوق النقد", "العراق طلب قرض.. شنو يعني لجيبك؟",
  ("BANGKOK · OCT 17 | IMF MANAGING DIRECTOR KRISTALINA GEORGIEVA SAID IRAQ HAS REQUESTED A LENDING PROGRAMME AND THE FUND WILL SUPPORT IT \"WITH MONEY AND POLICIES\"; "
   "AMOUNT AND CONDITIONS NOT DISCLOSED (AL JAZEERA, SHAFAQ) | OIL EXPORTS, ~90% OF REVENUE, FELL SHARPLY FOR MONTHS; RESERVES DOWN ABOUT $20BN (AFP VIA AL JAZEERA) | "
   "ECONOMIST ZIAD AL-HASHEMI (SHAFAQ) WARNS CONDITIONS COULD INCLUDE CUTTING FUEL AND ELECTRICITY SUBSIDIES"))
p["beats"] = [
 beat("الطلب", "جورجيفا: العراق طلب برنامج إقراض",
  "رئيسة صندوق النقد كريستالينا جورجيفا قالت السبت إن العراق طلب برنامج إقراض، والصندوق سيدعمه «بالمال والسياسات». المبلغ والشروط لم تُعلن (الجزيرة، شفق نيوز).",
  "1", "lending programme Iraq has requested, per IMF chief Georgieva (Al Jazeera / Shafaq)", "برنامج إقراض طلبه العراق",
  [("المتحدثة", "جورجيفا"), ("المبلغ", "لم يُعلن"), ("الشروط", "لم تُعلن")], 1, slug,
  ["العراق طلب برنامج إقراض", "الدعم بالمال والسياسات", "المبلغ ما انعلن"], GEN),
 beat("ليش", "النفط 90% من الإيرادات.. وتراجع",
  "صادرات النفط التي تؤمّن 90% من إيرادات العراق تراجعت بحدة لأشهر، والاحتياطي النقدي نزل بقرابة 20 مليار دولار (فرانس برس عبر الجزيرة).",
  "$20B", "approximate fall in Iraq's foreign reserves (AFP via Al Jazeera)", "تراجع الاحتياطي (تقريباً)",
  [("حصة النفط", "90%"), ("الاحتياطي", "−20 مليار $ تقريباً"), ("الصادرات", "تراجع لأشهر")], 2, slug,
  ["النفط 90% من الإيرادات", "صادراته تراجعت لأشهر", "الاحتياطي نزل 20 مليار"], GEN),
 beat("الشروط", "خبير: الشروط قد تمسّ دعم الوقود",
  "الخبير زياد الهاشمي (شفق نيوز) يحذّر من شروط قد تشمل تقليص دعم الوقود والكهرباء، ويقول إن الاقتراض يناقض تبرير خفض قيمة الدينار.",
  "152,000", "IQD per $100 — Iraq's official exchange rate since 7 Oct 2026 (CBI)", "دينار لكل 100$ — السعر الرسمي",
  [("الدعم المهدد", "الوقود والكهرباء"), ("الرأي", "خبير اقتصادي"), ("الحكومة", "لم تعلّق")], 3, slug,
  ["شروط القرض؟", "تقليص دعم الوقود والكهرباء", "بحسب خبير اقتصادي"], PEX),
]
finish(p, ["جورجيفا: العراق طلب برنامج إقراض والصندوق سيدعمه بالمال والسياسات (الجزيرة، شفق نيوز)",
           "صادرات النفط تؤمّن 90% من الإيرادات والاحتياطي تراجع بقرابة 20 مليار دولار (فرانس برس)",
           "الخبير زياد الهاشمي: الشروط قد تشمل تقليص دعم الوقود والكهرباء (شفق نيوز)"],
       "شكد تدفع بانزين بالأسبوع؟",
       SRC(("الجزيرة نت", "aljazeera.net"), ("شفق نيوز", "shafaq.com"), ("فرانس برس", "afp.com")))
SLATE[slug] = (p, {
 "kicker": "صندوق النقد", "hookHeadline": "العراق يطلب قرض.. شنو يعني لجيبك؟",
 "voText": ("قالت رئيسة صندوق النقد الدولي كريستالينا جورجيفا، يوم السبت، إن العراق طلب برنامج إقراض، وإن الصندوق سيقدم له الدعم بالمال والسياسات، من دون الإعلان عن المبلغ أو الشروط. "
            "ويأتي الطلب بعد تراجع حاد لصادرات النفط التي تؤمّن تسعين بالمئة من الإيرادات، وانخفاض الاحتياطي النقدي بقرابة عشرين مليار دولار، بحسب فرانس برس. "
            "ويحذّر الخبير الاقتصادي زياد الهاشمي من أن شروط القرض قد تشمل تقليص دعم الوقود والكهرباء. شكد تدفع بانزين بالأسبوع؟"),
 "endQuestion": "شكد تدفع بانزين بالأسبوع؟",
 "sourcesLine": "المصادر: الجزيرة نت · شفق نيوز · فرانس برس — 17 تشرين الأول 2026",
 "statPops": [{"value": "90%", "label": "من إيرادات العراق من النفط", "matchWord": "تسعين"},
              {"value": "$20B", "label": "تراجع الاحتياطي — تقريباً", "matchWord": "عشرين"}],
}, """قرض صندوق النقد للعراق — شنو يعني للمواطن؟

جورجيفا كشفت الطلب.. وخبير يحذّر من شرط يمس جيبك. بالفيديو.

شكد تدفع بانزين بالأسبوع؟

المصادر: الجزيرة نت، شفق نيوز، فرانس برس (17 تشرين الأول 2026)

#صندوق_النقد_الدولي #اقتصاد_العراق #العراق #photonectnews
@photonect.news
""")


# ═══════════ B · 19:45 · P1 dollar anchor — dollar up as bourses reopen + gold mithqal 976k ═══════════
slug = f"{D}-b-dollar-166850-gold-976"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار رجع يصعد.. والمثقال قرب المليون",
  ("BAGHDAD · OCT 17 (SAT) | AS THE BOURSES REOPENED, KIFAH AND HARITHIYA BOURSES QUOTED 166,850 IQD PER $100, UP FROM THURSDAY (SHAFAQ) | "
   "BAGHDAD EXCHANGE SHOPS SOLD AT 167,250 AND BOUGHT AT 166,250 (SHAFAQ, BAGHDAD TODAY); OFFICIAL RATE 152,000 | "
   "NAHR STREET WHOLESALE: GULF/TURKISH/EUROPEAN 21K GOLD 976,000 IQD PER MITHQAL SELL VS 970,000 ON THURSDAY; IRAQI 21K 946,000 (SHAFAQ, BAGHDAD TODAY)"))
p["beats"] = [
 beat("البورصة", "الكفاح والحارثية: 166,850",
  "مع عودة البورصات السبت، ارتفع الدولار في بورصتي الكفاح والحارثية ببغداد إلى 166,850 ديناراً لكل 100 دولار، مقارنة بيوم الخميس (شفق نيوز).",
  "166,850", "IQD per $100 at Baghdad's Kifah and Harithiya bourses, Saturday morning (Shafaq)", "دينار لكل 100$ — البورصة",
  [("الاتجاه", "ارتفاع"), ("البورصات", "الكفاح والحارثية"), ("اليوم", "السبت")], 1, slug,
  ["رجعت البورصات", "والدولار ارتفع", "166,850 لكل 100 دولار"], GEN),
 beat("الصيرفة", "بالصيرفة: تشتري بـ167,250",
  "محال الصيرفة ببغداد باعت الـ100 دولار بـ167,250 ديناراً واشترتها بـ166,250 (شفق نيوز، بغداد اليوم). والسعر الرسمي 152,000.",
  "167,250", "IQD — exchange-shop selling price per $100 in Baghdad (Shafaq / Baghdad Today)", "دينار — سعر البيع بالصيرفة",
  [("البيع", "167,250"), ("الشراء", "166,250"), ("الرسمي", "152,000")], 2, slug,
  ["الصيرفة تبيع بـ167,250", "وتشتري بـ166,250", "والرسمي 152,000"], GEN),
 beat("الذهب", "مثقال الخليجي: 976 ألف دينار",
  "بسوق الجملة في شارع النهر، سجّل مثقال الذهب الخليجي عيار 21 سعر بيع 976 ألف دينار مقابل 970 ألفاً الخميس، والعراقي 946 ألفاً (شفق نيوز، بغداد اليوم).",
  "976,000", "IQD per mithqal of Gulf/Turkish/European 21K gold, Nahr Street wholesale sell price (Shafaq / Baghdad Today)", "دينار — مثقال الخليجي عيار 21",
  [("الخميس", "970 ألف"), ("العراقي", "946 ألف"), ("السوق", "شارع النهر")], 3, slug,
  ["المثقال الخليجي 976 ألف", "الخميس كان 970 ألف", "والعراقي 946 ألف"], GEN),
]
finish(p, ["الدولار في بورصتي الكفاح والحارثية: 166,850 ديناراً لكل 100 دولار (شفق نيوز)",
           "الصيرفة ببغداد: بيع 167,250 وشراء 166,250 (شفق نيوز، بغداد اليوم)",
           "مثقال الذهب الخليجي عيار 21 بشارع النهر: 976 ألف دينار (شفق نيوز، بغداد اليوم)"],
       "ناوي تشتري ذهب قريباً؟",
       SRC(("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news")))
SLATE[slug] = (p, {
 "kicker": "الدولار اليوم", "hookHeadline": "الدولار يصعد.. والمثقال قرب المليون",
 "voText": ("مع عودة البورصات يوم السبت، ارتفع سعر صرف الدولار في بورصتي الكفاح والحارثية ببغداد إلى مئة وستة وستين ألفاً وثمانمئة وخمسين ديناراً لكل مئة دولار، بحسب شفق نيوز. "
            "وفي محال الصيرفة بلغ سعر البيع مئة وسبعة وستين ألفاً ومئتين وخمسين ديناراً. "
            "أما الذهب، فسجّل مثقال الذهب الخليجي عيار واحد وعشرين في شارع النهر تسعمئة وستة وسبعين ألف دينار، مقارنة بتسعمئة وسبعين ألفاً يوم الخميس. ناوي تشتري ذهب قريباً؟"),
 "endQuestion": "ناوي تشتري ذهب قريباً؟",
 "sourcesLine": "المصادر: شفق نيوز · بغداد اليوم — 17 تشرين الأول 2026",
 "statPops": [{"value": "166,850", "label": "دينار لكل 100$ — البورصة", "matchWord": "الحارثية"},
              {"value": "976,000", "label": "دينار — مثقال الخليجي عيار 21", "matchWord": "النهر"}],
}, """سعر الدولار والذهب في بغداد اليوم — شكد صار؟

البورصات رجعت السبت.. والمثقال يقترب من رقم كبير. بالفيديو.

ناوي تشتري ذهب قريباً؟

المصادر: شفق نيوز، بغداد اليوم (17 تشرين الأول 2026)

#سعر_الدولار #الذهب #العراق #photonectnews
@photonect.news
""")


# ═══════════ C · 21:15 · P2 oil output recovery through the war (V10.1 CONTROL) ═══════════
slug = f"{D}-c-oil-4399-recovery"
p = base(slug, "iraq_money", "A", "نفط العراق", "إنتاج النفط بأيلول: الأعلى هالسنة",
  ("BAGHDAD · OCT 17 | ECO IRAQ OBSERVATORY, CITING OPEC DIRECT-COMMUNICATION DATA: IRAQ'S CRUDE OUTPUT AVERAGED 4.399 MILLION B/D IN SEPTEMBER, THE HIGHEST OF 2026 | "
   "OUTPUT FELL SHARPLY FROM MARCH WITH THE REGIONAL WAR TO A LOW OF 1.406 MILLION B/D IN MAY, THEN 1.525 JUNE, 2.901 JULY, 3.746 AUGUST | "
   "834.7 MILLION BARRELS IN JAN-SEP (SHAFAQ, BAGHDAD TODAY, AL-MADA) | BRENT FUTURES ROSE ABOVE $109 ON FRIDAY (SHAFAQ)"))
p["beats"] = [
 beat("أيلول", "أيلول: 4.399 مليون برميل يومياً",
  "مرصد «إيكو عراق»: متوسط إنتاج العراق النفطي في أيلول بلغ 4.399 ملايين برميل يومياً، الأعلى منذ بداية 2026، وفق بيانات أوبك (شفق نيوز، بغداد اليوم).",
  "4.399", "million barrels per day — Iraq's average crude output in September 2026, highest this year (Eco Iraq via Shafaq / Baghdad Today)", "مليون برميل يومياً — أيلول",
  [("المصدر", "إيكو عراق"), ("البيانات", "أوبك"), ("الترتيب", "الأعلى بـ2026")], 1, slug,
  ["أيلول: 4.399 مليون برميل", "الأعلى هالسنة", "بحسب إيكو عراق"], GEN),
 beat("أيار", "أيار: القاع بـ1.406 مليون",
  "بحسب المرصد، تراجع الإنتاج بحدة من آذار مع الحرب في المنطقة حتى 1.406 مليون برميل يومياً في أيار، ثم تعافى: تموز 2.901 وآب 3.746.",
  "1.406", "million b/d — Iraq's crude output low in May 2026 (Eco Iraq)", "مليون برميل يومياً — أيار",
  [("حزيران", "1.525"), ("تموز", "2.901"), ("آب", "3.746")], 2, slug,
  ["من آذار تراجع حاد", "أيار: 1.406 مليون", "وبعدها تعافى"], GEN),
 beat("الحصيلة", "9 أشهر: 834.7 مليون برميل",
  "العراق استخرج نحو 834.7 مليون برميل خلال الأشهر التسعة الأولى من 2026 (إيكو عراق عبر بغداد اليوم والمدى). وبرنت تجاوز الجمعة 109 دولارات (شفق نيوز).",
  "834.7", "million barrels of crude Iraq produced in Jan–Sep 2026 (Eco Iraq via Baghdad Today / Al-Mada)", "مليون برميل — 9 أشهر",
  [("برنت الجمعة", "$109.58"), ("كانون الثاني", "4.097"), ("شباط", "4.140")], 3, slug,
  ["834.7 مليون برميل", "بتسعة أشهر", "وبرنت فوق 109 دولار"], GEN),
]
finish(p, ["إيكو عراق: إنتاج النفط في أيلول 4.399 ملايين برميل يومياً، الأعلى منذ بداية 2026 (شفق نيوز، بغداد اليوم)",
           "أدنى مستوى كان في أيار: 1.406 مليون برميل يومياً (إيكو عراق)",
           "834.7 مليون برميل خلال 9 أشهر (بغداد اليوم، المدى) — وبرنت تجاوز 109 دولارات الجمعة (شفق نيوز)"],
       "راتبك وصل بموعده هالشهر؟",
       SRC(("مرصد إيكو عراق", "ecoiraq"), ("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("المدى", "almadapaper.net")))
SLATE[slug] = (p, None, """إنتاج النفط العراقي — رجع لمستواه قبل الحرب؟

من قاع أيار إلى أعلى رقم هالسنة.. بالفيديو.

راتبك وصل بموعده هالشهر؟

المصادر: مرصد إيكو عراق عبر شفق نيوز وبغداد اليوم والمدى (17 تشرين الأول 2026)

#نفط_العراق #اقتصاد_العراق #العراق #photonectnews
@photonect.news
""")


# ═══════════ D · 22:30 · P1 accountability — new Interior minister orders fee review + suspect-contracts decision ═══════════
slug = f"{D}-d-interior-fees-review"
p = base(slug, "iraq_money", "B", "رسوم الدولة", "وزير الداخلية الجديد: الرسوم تحت المراجعة",
  ("BAGHDAD · OCT 17 | NEW INTERIOR MINISTER YASSER AL-MALIKI TOOK OFFICE AND ORDERED A REVIEW OF THE FEES AND LEVIES COLLECTED FROM CITIZENS, "
   "AND ACTIVATION OF THE CABINET DECISION ON CONTRACTS SURROUNDED BY SUSPICIONS OF CORRUPTION (MINISTER'S MEDIA OFFICE VIA BAGHDAD TODAY); NO SPECIFIC FEES OR CONTRACTS NAMED | "
   "CONTEXT: ON OCT 15 CITIZENS WERE CHARGED 101,000 IQD FOR THE E-PASSPORT; THE MINISTRY THEN SAID THE FEE STAYS AT 91,000 (BAGHDAD TODAY, SHAFAQ, 964)"))
p["beats"] = [
 beat("أول يوم", "أول يوم: مراجعة رسوم المواطنين",
  "وزير الداخلية ياسر المالكي باشر مهامه السبت، ووجّه بإعادة النظر في الرسوم والاستيفاءات المستحصلة من المواطنين (مكتبه الإعلامي عبر بغداد اليوم).",
  "17", "October — Interior Minister Yasser al-Maliki's first day in office, when he ordered a review of citizen fees (minister's office via Baghdad Today)", "تشرين الأول — أول يوم للوزير",
  [("الوزير", "ياسر المالكي"), ("التوجيه", "مراجعة الرسوم"), ("التفاصيل", "لم تُحدَّد")], 1, slug,
  ["وزير الداخلية الجديد", "يوجّه بمراجعة الرسوم", "اللي يدفعها المواطن"], GEN),
 beat("العقود", "والعقود المشبوهة: تفعيل قرار الوزراء",
  "ووجّه أيضاً بتفعيل قرار مجلس الوزراء بشأن العقود التي تدور حولها شبهات فساد، بحسب البيان. ولم يذكر البيان رسوماً أو عقوداً بعينها.",
  "2", "directives in the minister's first-day statement: review fees, activate the cabinet decision on suspect contracts", "توجيهان: الرسوم والعقود",
  [("القرار", "مجلس الوزراء"), ("العقود", "شبهات فساد"), ("الأسماء", "لم تُذكر")], 2, slug,
  ["تفعيل قرار مجلس الوزراء", "بشأن العقود المشبوهة", "بدون أسماء"], GEN),
 beat("الجواز", "الخميس: الجواز بين 101 و91 ألف",
  "وكان مواطنون تفاجأوا الخميس برسم جواز 101,000 دينار، ثم أعلنت الداخلية الإبقاء على 91,000 دون زيادة (بغداد اليوم، شفق نيوز، 964).",
  "101,000", "IQD e-passport fee citizens were charged on Thursday before the ministry kept it at 91,000 (Baghdad Today / Shafaq / 964)", "دينار — رسم الجواز صباح الخميس",
  [("المعتمد", "91,000"), ("الفرق", "10,000"), ("الدفع", "إلكتروني")], 3, slug,
  ["الخميس: 101 ألف للجواز", "وبالمساء رجع 91 ألف", "بدون زيادة"], GEN),
]
finish(p, ["وزير الداخلية ياسر المالكي يوجّه بإعادة النظر في الرسوم والاستيفاءات المستحصلة من المواطنين (بغداد اليوم)",
           "وتفعيل قرار مجلس الوزراء بشأن العقود التي تدور حولها شبهات فساد",
           "رسم الجواز الإلكتروني باقٍ عند 91,000 دينار بحسب الداخلية (شفق نيوز، 964)"],
       "دفعت رسوم بدائرة حكومية هالشهر؟",
       SRC(("بغداد اليوم", "baghdadtoday.news"), ("وزارة الداخلية", "moi.gov.iq"), ("شفق نيوز", "shafaq.com"), ("شبكة 964", "964media.com")))
SLATE[slug] = (p, {
 "kicker": "رسوم الدولة", "hookHeadline": "رسومك بالداخلية.. تحت المراجعة",
 "voText": ("باشر وزير الداخلية الجديد ياسر المالكي مهامه يوم السبت، ووجّه بإعادة النظر في الرسوم والاستيفاءات التي تُستحصل من المواطنين، "
            "وبتفعيل قرار مجلس الوزراء بشأن العقود التي تدور حولها شبهات فساد، بحسب بيان مكتبه الإعلامي، من دون تحديد رسوم أو عقود بعينها. "
            "وكان مواطنون قد تفاجأوا يوم الخميس برسم جواز سفر بلغ مئة وألف دينار، قبل أن تعلن الوزارة الإبقاء على واحد وتسعين ألفاً. دفعت رسوم بدائرة حكومية هالشهر؟"),
 "endQuestion": "دفعت رسوم بدائرة حكومية هالشهر؟",
 "sourcesLine": "المصادر: المكتب الإعلامي لوزير الداخلية عبر بغداد اليوم · شفق نيوز · شبكة 964 — 15 و17 تشرين الأول 2026",
 "statPops": [{"value": "101,000", "label": "دينار — رسم الجواز صباح الخميس", "matchWord": "تفاجأوا"},
              {"value": "91,000", "label": "الرسم المعتمد بحسب الداخلية", "matchWord": "الإبقاء"}],
}, """رسوم وزارة الداخلية — راح تتغير؟

الوزير الجديد بأول يوم.. توجيهان يخصّون جيبك. بالفيديو.

دفعت رسوم بدائرة حكومية هالشهر؟

المصادر: المكتب الإعلامي لوزير الداخلية عبر بغداد اليوم، شفق نيوز، شبكة 964 (15 و17 تشرين الأول 2026)

#وزارة_الداخلية #رسوم_الجواز #العراق #photonectnews
@photonect.news
""")


# ═══════════ E · 23:45 · P3 Iraqis = 2nd-biggest foreign homebuyers in Turkey ═══════════
slug = f"{D}-e-iraqis-turkey-homes-166"
p = base(slug, "region_money", "C", "عقارات", "العراقيين ثاني أكبر مشتري بيوت بتركيا",
  ("ANKARA · OCT 17 | TURKSTAT: IRAQI CITIZENS BOUGHT 166 HOMES IN TURKEY IN SEPTEMBER 2026, SECOND AMONG FOREIGNERS AFTER RUSSIANS (388); GERMANS 162, IRANIANS 159, UKRAINIANS 158, CHINESE 124 (SHAFAQ; BAZAAR TIMES) | "
   "HOME SALES TO FOREIGNERS ROSE 9.9% YEAR ON YEAR TO 2,167, 1.5% OF ALL SALES (TURKSTAT VIA SHAFAQ, BAZAAR TIMES)"))
p["beats"] = [
 beat("أيلول", "أيلول: 166 بيت لعراقيين",
  "بيانات معهد الإحصاء التركي: العراقيون اشتروا 166 منزلاً في تركيا خلال أيلول، ثانياً بين الأجانب بعد الروس بـ388 منزلاً (شفق نيوز، بازار تايمز).",
  "166", "homes bought by Iraqi citizens in Turkey in September 2026 — 2nd among foreign nationalities (TurkStat via Shafaq / Bazaar Times)", "منزلاً — للعراقيين بأيلول",
  [("المرتبة", "الثانية"), ("الأول", "الروس 388"), ("الشهر", "أيلول")], 1, slug,
  ["166 بيت بتركيا", "اشتراها عراقيون بأيلول", "ثانياً بعد الروس"], PEX),
 beat("الترتيب", "قبل الألمان والإيرانيين",
  "بعد العراقيين جاء الألمان بـ162 منزلاً، ثم الإيرانيون بـ159، والأوكرانيون بـ158، والصينيون بـ124، بحسب البيانات نفسها (شفق نيوز).",
  "162", "homes bought by Germans in Turkey in September — 3rd, behind Iraqis (TurkStat via Shafaq)", "منزلاً — للألمان (الثالث)",
  [("الإيرانيون", "159"), ("الأوكرانيون", "158"), ("الصينيون", "124")], 2, slug,
  ["الألمان: 162", "الإيرانيون: 159", "العراقيون قبلهم"], PEX),
 beat("الصورة", "مبيعات الأجانب: 2,167 منزلاً",
  "مبيعات المنازل للأجانب في تركيا ارتفعت 9.9% عن أيلول الماضي إلى 2,167 منزلاً، أي 1.5% فقط من مجمل المبيعات (معهد الإحصاء التركي).",
  "2,167", "homes sold to foreigners in Turkey in September 2026, up 9.9% y/y, 1.5% of all sales (TurkStat via Shafaq / Bazaar Times)", "منزلاً — مبيعات الأجانب بأيلول",
  [("سنوياً", "+9.9%"), ("الحصة", "1.5%"), ("العراقيون", "166")], 3, slug,
  ["الأجانب: 2,167 بيت", "ارتفاع 9.9%", "بس 1.5% من السوق"], PEX),
]
finish(p, ["معهد الإحصاء التركي: العراقيون ثاني أكبر مشترٍ أجنبي للمنازل في تركيا خلال أيلول بـ166 منزلاً (شفق نيوز)",
           "الروس أولاً بـ388 منزلاً، والألمان ثالثاً بـ162",
           "مبيعات المنازل للأجانب ارتفعت 9.9% إلى 2,167 منزلاً"],
       "عندك قريب اشترى بيت بتركيا؟",
       SRC(("معهد الإحصاء التركي", "tuik.gov.tr"), ("شفق نيوز", "shafaq.com"), ("بازار تايمز", "bazaartimes.com")))
SLATE[slug] = (p, {
 "kicker": "عقارات", "hookHeadline": "العراقيين ثاني أكبر مشتري بيوت بتركيا",
 "voText": ("أظهرت بيانات معهد الإحصاء التركي أن العراقيين اشتروا مئة وستة وستين منزلاً في تركيا خلال شهر أيلول، ليحلّوا في المرتبة الثانية بين الأجانب بعد الروس الذين اشتروا ثلاثمئة وثمانية وثمانين منزلاً، "
            "وقبل الألمان والإيرانيين، بحسب شفق نيوز. وارتفعت مبيعات المنازل للأجانب بنسبة تسعة فاصلة تسعة بالمئة مقارنة بأيلول من العام الماضي، "
            "لكنها لا تشكّل سوى واحد ونصف بالمئة من مجمل المبيعات في تركيا. عندك قريب اشترى بيت بتركيا؟"),
 "endQuestion": "عندك قريب اشترى بيت بتركيا؟",
 "sourcesLine": "المصادر: معهد الإحصاء التركي عبر شفق نيوز · بازار تايمز — 16 و17 تشرين الأول 2026",
 "statPops": [{"value": "166", "label": "منزلاً اشتراها عراقيون بأيلول", "matchWord": "العراقيين"},
              {"value": "388", "label": "منزلاً للروس — المرتبة الأولى", "matchWord": "الروس"}],
}, """شراء بيت في تركيا للعراقيين — شكد اشترينا بأيلول؟

ترتيبنا بين الأجانب يفاجئ.. بالفيديو.

عندك قريب اشترى بيت بتركيا؟

المصادر: معهد الإحصاء التركي عبر شفق نيوز، بازار تايمز (16 و17 تشرين الأول 2026)

#عقارات_تركيا #العراقيين_في_تركيا #العراق #photonectnews
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
