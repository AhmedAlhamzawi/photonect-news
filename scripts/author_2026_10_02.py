#!/usr/bin/env python3
"""Author the 2026-10-02 slate: props.json + caption.txt (+ v11-brief.json on a, b, c, d; e = V10.1 control).

Every figure traces to a named source published 29 Sep-2 Oct 2026. Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + two gate passes (apply_gate*_2026_10_02.py)
then edited the files on disk — do NOT re-run this script, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_10_02.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-10-02"
DATE_LABEL = "OCT 02 • 2026"
AR_DATE = "2 تشرين الأول 2026"
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


# ═══════════ A · 18:00 · P1 corruption — Wasit health embezzler returned from Lebanon (LEAD) ═══════════
slug = f"{D}-a-wasit-health-3-7-billion"
p = base(slug, "iraq_corruption", "A", "النزاهة", "3.7 مليار من صحة واسط.. والمدانة ترجع من لبنان",
  ("WASIT · OCT 1 | FEDERAL INTEGRITY COMMISSION: A FUGITIVE FORMER EMPLOYEE OF THE WASIT HEALTH DIRECTORATE, CONVICTED IN "
   "ABSENTIA OF TAKING PART IN EMBEZZLING 2,855,313,401 + 923,719,423 = 3,779,032,824 IQD (~$2.6M PER AL-MODON) OF THE "
   "DIRECTORATE'S FUNDS, WAS ARRESTED IN LEBANON AND HANDED TO IRAQ VIA INTERPOL | WASIT CRIMINAL COURT HAD SENTENCED HER IN "
   "ABSENTIA TO LIFE IMPRISONMENT (PENAL CODE ART. 315) AND ORDERED FULL REPAYMENT (INTEGRITY COMMISSION VIA SHAFAQ NEWS, "
   "AL-MODON, ALSUMARIA)"))
p["beats"] = [
 beat("المبلغ", "3.779 مليار دينار من صحة واسط",
  "هيئة النزاهة: موظفة سابقة في دائرة صحة واسط أُدينت بالاشتراك باختلاس مبلغين مجموعهما 3,779,032,824 ديناراً من أموال الدائرة.",
  "3.779", "Billion IQD embezzled from Wasit Health Directorate in two amounts (Integrity Commission)",
  "مليار دينار مختلسة من صحة واسط (هيئة النزاهة)",
  [("المبلغ الأول", "2.855 مليار"), ("المبلغ الثاني", "923 مليون"), ("بالدولار", "2.6 مليون (المدن)")], 1, slug,
  ["صحة واسط", "3.7 مليار دينار", "مبلغين مختلسين"], STOCK),
 beat("الاسترداد", "هربت إلى لبنان.. ورجعت عبر الإنتربول",
  "حسب الهيئة: أُعدّ ملف استردادها وأُرسل إلى السلطات اللبنانية، فقُبض عليها وسُلّمت للعراق عبر مديرية الشرطة العربية والدولية (الإنتربول).",
  "2.6", "Million USD equivalent of the embezzled sum (Al-Modon)",
  "مليون دولار ما يعادل المبلغ المختلس (المدن)",
  [("البلد", "لبنان"), ("التسليم", "الإنتربول"), ("الإعلان", "الخميس 1 تشرين الأول")], 2, slug,
  ["هربت إلى لبنان", "الإنتربول", "رجعت للعراق"], STOCK),
 beat("الحكم", "مؤبد غيابي.. وإلزام بإعادة المبلغ",
  "محكمة جنايات واسط أصدرت بحقها غيابياً حكماً بالسجن المؤبد وفق المادة 315، وألزمتها بإعادة المبلغ كاملاً للدائرة.",
  "315", "Article of the Iraqi Penal Code under which the life sentence was issued (Integrity Commission)",
  "المادة القانونية التي صدر بموجبها الحكم (النزاهة)",
  [("الحكم", "المؤبد غيابياً"), ("المحكمة", "جنايات واسط"), ("الإلزام", "إعادة المبلغ")], 3, slug,
  ["حكم غيابي", "السجن المؤبد", "إعادة المبلغ كاملاً"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة: استرداد مدانة هاربة من لبنان — موظفة سابقة في دائرة صحة واسط (الخميس 1 تشرين الأول)",
 "المبلغ المختلس: 2,855,313,401 دينار و923,719,423 ديناراً — المجموع 3,779,032,824 ديناراً",
 "التسليم تم عبر مديرية الشرطة العربية والدولية (الإنتربول) بالتنسيق مع الادعاء العام والسفارة العراقية في لبنان",
 "محكمة جنايات واسط: السجن المؤبد غيابياً وإلزامها بإعادة المبلغ كاملاً",
 "تراجع مستشفى حكومي لو أهلي؟"]
p["endQuestion"] = "تراجع مستشفى حكومي لو أهلي؟"
p["sources"] = [{"name": "هيئة النزاهة", "domain": "nazaha.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "المدن", "domain": "almodon.com"}, {"name": "السومرية", "domain": "alsumaria.tv"}]
SLATE[slug] = {"props": p, "caption": """اختلاس من صحة واسط — المدانة ترجع من لبنان

3.7 مليار دينار وحكم مؤبد.. شلون رجعت؟ بالفيديو.

تراجع مستشفى حكومي لو أهلي؟

المصادر: هيئة النزاهة عبر شفق نيوز، المدن، السومرية (1 تشرين الأول 2026)

#هيئة_النزاهة #العراق #واسط #المال_العام #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "3.7 مليار من صحة واسط.. ورجعت",
  "voText": "أعلنت هيئة النزاهة الاتحادية استرداد موظفة سابقة في دائرة صحة واسط من لبنان، بعد إدانتها بالاشتراك باختلاس نحو ثلاثة مليارات وسبعمئة وتسعة وسبعين مليون دينار من أموال الدائرة. وبحسب الهيئة، أُرسل ملف استردادها إلى السلطات اللبنانية، فقُبض عليها وسُلّمت إلى العراق عبر الإنتربول. وكانت محكمة جنايات واسط قد حكمت عليها غيابياً بالسجن المؤبد، وألزمتها بإعادة المبلغ كاملاً إلى الدائرة. وتقدّر صحيفة المدن المبلغ بنحو مليونين وستمئة ألف دولار. تراجع مستشفى حكومي لو أهلي؟",
  "endQuestion": "تراجع مستشفى حكومي لو أهلي؟",
  "sourcesLine": "المصادر: هيئة النزاهة عبر شفق نيوز · المدن · السومرية — 1 تشرين الأول 2026",
  "statPops": [{"value": "3.779 مليار", "label": "دينار مختلسة من صحة واسط (النزاهة)", "matchWord": "وسبعمئة"},
               {"value": "مؤبد", "label": "حكم غيابي — جنايات واسط", "matchWord": "بالسجن"}]}}


# ═══════════ B · 19:45 · P1 dollar anchor — the official/parallel gap: who pays ═══════════
slug = f"{D}-b-dollar-gap-who-pays"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "موبايلك وهدومك.. ليش تتسعّر بدولار السوق؟",
  ("BAGHDAD · OCT 1-2 | SHAFAQ NEWS: KIFAH & HARITHIYA BOURSES CLOSED THURSDAY AT 157,300 IQD PER $100, UP FROM 156,850 "
   "THURSDAY MORNING; BAGHDAD SHOPS SELL 157,750 / BUY 156,750 | SHAFAQ REPORT (OCT 2): ECONOMIST ALI DAADOUSH — THE "
   "OFFICIAL/PARALLEL GAP RAISES THE COST OF IMPORTS OUTSIDE OFFICIAL CHANNELS AND PRESSES PRICES; BENEFICIARIES ARE "
   "BROKERS, SPECULATORS, INFORMAL TRADE | MONEY CHANGER OSAMA AL-MASHRAFAWI: CLOTHING AND MOBILE-PHONE SHOPS DON'T GET "
   "DOLLARS AT THE OFFICIAL RATE, SO BUY ON THE BLACK MARKET | MUSTAFA HANTOUSH: THE PLATFORM DOES NOT COVER SMALL TRADERS"))
p["beats"] = [
 beat("إغلاق الخميس", "157,300 بإغلاق الخميس",
  "شفق نيوز: بورصتا الكفاح والحارثية أغلقتا الخميس على 157,300 دينار لكل 100 دولار، بعد 156,850 صباح اليوم نفسه.",
  "157,300", "IQD per $100, Kifah & Harithiya bourses, Thursday close (Shafaq News)",
  "دينار لكل 100 دولار — إغلاق الخميس (شفق نيوز)",
  [("صباح الخميس", "156,850"), ("بيع الصيرفة", "157,750"), ("شراء الصيرفة", "156,750")], 1, slug,
  ["إغلاق الخميس", "157,300 دينار", "صباحاً 156,850"], STOCK),
 beat("منو يدفع؟", "محل الموبايلات يشتري من السوق السوداء",
  "الصيرفي أسامة المشرفاوي لشفق نيوز: أصحاب محال الملابس والهواتف وبعض المستوردين لا يحصلون على الدولار بالسعر الرسمي، فيشترونه من السوق السوداء.",
  "157,750", "IQD per $100, Baghdad exchange-shop selling price, Thursday close (Shafaq News)",
  "دينار سعر البيع بمحال صيرفة بغداد (شفق نيوز)",
  [("الملابس", "دولار السوق"), ("الهواتف", "دولار السوق"), ("المنصة", "لا تغطي الصغار")], 2, slug,
  ["محال الملابس", "محال الهواتف", "السوق السوداء"], STOCK),
 beat("الأثر", "الفجوة ترفع الأسعار عليك",
  "الخبير علي دعدوش: الفجوة ترفع كلفة المستوردات خارج القنوات الرسمية وتضغط على الأسعار، والمستفيدون الوسطاء والمضاربون والتجارة غير الرسمية.",
  "156,750", "IQD per $100, Baghdad exchange-shop buying price, Thursday close (Shafaq News)",
  "دينار سعر الشراء بمحال صيرفة بغداد (شفق نيوز)",
  [("الخاسر", "المستهلك والتاجر الصغير"), ("المستفيد", "الوسطاء والمضاربون"), ("الحل المقترح", "توسيع التعامل بالدينار")], 3, slug,
  ["الفجوة ترفع الكلفة", "تضغط على الأسعار", "منو المستفيد؟"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الدولار في بورصتي الكفاح والحارثية 157,300 دينار لكل 100 دولار عند إغلاق الخميس، بعد 156,850 صباحاً",
 "محال الصيرفة ببغداد عند الإغلاق: البيع 157,750 والشراء 156,750 لكل 100 دولار",
 "الصيرفي أسامة المشرفاوي: محال الملابس والهواتف لا تحصل على الدولار بالسعر الرسمي",
 "الخبير علي دعدوش: الفجوة بين الرسمي والموازي ترفع كلفة المستوردات وتضغط على الأسعار",
 "الخبير مصطفى حنتوش: المنصة لا تغطي التجار الصغار",
 "اشتريت شي بالدولار هالأسبوع؟"]
p["endQuestion"] = "اشتريت شي بالدولار هالأسبوع؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — ليش السوق غير الرسمي؟

صيرفي وخبيران يشرحون منو يدفع الفرق.. بالفيديو.

اشتريت شي بالدولار هالأسبوع؟

المصادر: شفق نيوز (1-2 تشرين الأول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #السوق_الموازي #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "ليش موبايلك يتسعّر بدولار السوق؟",
  "voText": "أغلقت بورصتا الكفاح والحارثية في بغداد تعاملات الخميس على مئة وسبعة وخمسين ألفاً وثلاثمئة دينار لكل مئة دولار، بحسب شفق نيوز. لكن لماذا يبقى سعر السوق أعلى من الرسمي؟ الصيرفي أسامة المشرفاوي يقول إن أصحاب محال الملابس والهواتف لا يحصلون على الدولار بالسعر الرسمي، فيشترونه من السوق السوداء. ويرى الخبير الاقتصادي علي دعدوش أن هذه الفجوة ترفع كلفة المستوردات وتضغط على الأسعار، وأن المستفيدين هم الوسطاء والمضاربون. اشتريت شي بالدولار هالأسبوع؟",
  "endQuestion": "اشتريت شي بالدولار هالأسبوع؟",
  "sourcesLine": "المصادر: شفق نيوز — 1-2 تشرين الأول 2026",
  "statPops": [{"value": "157,300", "label": "إغلاق الكفاح والحارثية — الخميس", "matchWord": "والحارثية"},
               {"value": "دولار السوق", "label": "محال الملابس والهواتف (المشرفاوي)", "matchWord": "السوداء"}]}}


# ═══════════ C · 21:15 · P2 Iraq–Iran–US — Najaf/Mashhad flights: licence, ban, pressure ═══════════
slug = f"{D}-c-najaf-mashhad-flights"
p = base(slug, "mena_geo", "A", "حظر الطيران", "3 ملايين عراقي يزورون مشهد.. شنو صار بالرحلات؟",
  ("NAJAF · SEP 29-OCT 2 | US TREASURY (OFAC) LICENCE LETS IRAQI AIRWAYS ALONE FLY IRAQ-IRAN VIA NAJAF AIRPORT ONLY, FOR "
   "RELIGIOUS VISITORS, ONE MONTH ENDING 28 OCT (AL-ARABY TV, RUDAW) | SENIOR SOURCE: BAN ON IRANIAN AIRLINES STILL IN "
   "FORCE (SHAFAQ NEWS) | FM FUAD HUSSEIN IN WASHINGTON: IRAQ RECEIVES ~5M IRANIAN VISITORS A YEAR, ~3M IRAQIS VISIT MASHHAD "
   "(SHAFAQ NEWS) | IRANIAN EMBASSY CALLS FOR AN 'IMMEDIATE DECISION' (SHAFAQ NEWS) | NAJAF FRIDAY PREACHER SADR AL-DIN "
   "AL-QABANCHI CALLS FOR THE DECISION TO BE REVIEWED (964)"))
p["beats"] = [
 beat("الاستثناء", "ترخيص أميركي: العراقية فقط ومن النجف فقط",
  "ترخيص الخزانة الأميركية يسمح للخطوط الجوية العراقية وحدها برحلات إلى إيران عبر مطار النجف، للزوار الدينيين فقط، لمدة شهر ينتهي 28 تشرين الأول.",
  "28", "October 2026 — expiry of the one-month US Treasury licence (Al-Araby TV)",
  "تشرين الأول — نهاية الترخيص الأميركي (التلفزيون العربي)",
  [("الشركة", "العراقية فقط"), ("المطار", "النجف فقط"), ("المسافرون", "زوار دينيون")], 1, slug,
  ["ترخيص أميركي", "العراقية فقط", "من النجف فقط"], "صورة أرشيفية — الخطوط الجوية العراقية"),
 beat("الأرقام", "3 ملايين عراقي يزورون مشهد",
  "وزير الخارجية فؤاد حسين من واشنطن: العراق يستقبل سنوياً نحو 5 ملايين زائر إيراني، ونحو 3 ملايين عراقي يزورون مشهد (شفق نيوز).",
  "3", "Million Iraqis visit Mashhad yearly (FM Fuad Hussein via Shafaq News)",
  "ملايين عراقي يزورون مشهد سنوياً (فؤاد حسين)",
  [("زوار إيرانيون", "5 ملايين سنوياً"), ("الطيران الإيراني", "الحظر سارٍ"), ("المصدر", "شفق نيوز")], 2, slug,
  ["فؤاد حسين", "3 ملايين عراقي", "5 ملايين زائر إيراني"], "صورة أرشيفية — مرقد الإمام الرضا"),
 beat("الضغط", "طهران تطالب.. وخطيب النجف يدعو للمراجعة",
  "السفارة الإيرانية دعت بغداد إلى «قرار فوري». وخطيب جمعة النجف صدر الدين القبانجي دعا اليوم إلى مراجعة القرار (964). والحكومة تحاور واشنطن لاستثناءات.",
  "5", "Million Iranian visitors to Iraq yearly (FM Fuad Hussein via Shafaq News)",
  "ملايين زائر إيراني للعراق سنوياً (فؤاد حسين)",
  [("السفارة الإيرانية", "قرار فوري"), ("خطيب النجف", "مراجعة القرار"), ("الحكومة", "حوار مع واشنطن")], 3, slug,
  ["السفارة الإيرانية", "خطيب جمعة النجف", "حوار مع واشنطن"], "صورة أرشيفية — مرقد الإمام علي"),
]
p["arabicTicker"] = [
 "التلفزيون العربي: ترخيص الخزانة الأميركية للخطوط الجوية العراقية — رحلات إيران عبر النجف فقط وللزوار الدينيين، حتى 28 تشرين الأول",
 "مصدر رفيع لشفق نيوز: الحظر المفروض على شركات الطيران الإيرانية ما يزال سارياً",
 "فؤاد حسين: نحو 5 ملايين زائر إيراني سنوياً ونحو 3 ملايين عراقي يزورون مشهد",
 "السفارة الإيرانية في بغداد تدعو إلى «قرار فوري» بشأن قيود الطيران",
 "خطيب جمعة النجف صدر الدين القبانجي يدعو إلى مراجعة القرار (964)",
 "زرت مشهد قبل؟"]
p["endQuestion"] = "زرت مشهد قبل؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "التلفزيون العربي", "domain": "alaraby.com"}, {"name": "روداو", "domain": "rudawarabia.net"}, {"name": "964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """رحلات مشهد من النجف — شنو صار بعد الترخيص الأميركي؟

ترخيص لشهر واحد بشروط.. والتفاصيل بالفيديو.

زرت مشهد قبل؟

المصادر: شفق نيوز، التلفزيون العربي، روداو، 964 (29 أيلول - 2 تشرين الأول 2026)

#مطار_النجف #مشهد #العراق #الخطوط_الجوية_العراقية #photonectnews
@photonect.news""",
 "brief": {"kicker": "حظر الطيران", "hookHeadline": "رايح مشهد؟ هذا اللي تغيّر",
  "voText": "منحت وزارة الخزانة الأميركية الخطوط الجوية العراقية ترخيصاً لتسيير رحلات إلى إيران عبر مطار النجف وحده، للزوار الدينيين فقط، ولمدة شهر ينتهي في الثامن والعشرين من تشرين الأول، بحسب التلفزيون العربي. أما شركات الطيران الإيرانية فالحظر عليها ما يزال سارياً، وفق مصدر رفيع لشفق نيوز. وقال وزير الخارجية فؤاد حسين إن نحو ثلاثة ملايين عراقي يزورون مشهد سنوياً. وفي النجف، دعا خطيب الجمعة اليوم إلى مراجعة القرار. زرت مشهد قبل؟",
  "endQuestion": "زرت مشهد قبل؟",
  "sourcesLine": "المصادر: شفق نيوز · التلفزيون العربي · روداو · 964",
  "statPops": [{"value": "28 تشرين الأول", "label": "نهاية الترخيص الأميركي", "matchWord": "والعشرين"},
               {"value": "3 ملايين", "label": "عراقي يزورون مشهد سنوياً (فؤاد حسين)", "matchWord": "سنوياً"}]}}


# ═══════════ D · 22:30 · P1 electricity — Kurdistan power hours cut for a month (Khor Mor maintenance) ═══════════
slug = f"{D}-d-kurdistan-power-khormor"
p = base(slug, "iraq_services", "B", "الكهرباء", "كهرباء كوردستان تقل شهراً كاملاً.. ليش؟",
  ("ERBIL · OCT 1-2 | KRG MINISTRY OF ELECTRICITY: DANA GAS MAINTENANCE AT KHOR MOR FIELD FROM 2 OCT TO 2 NOV WILL REDUCE "
   "POWER SUPPLY BY SEVERAL HOURS THROUGHOUT; MINISTRY TO COORDINATE TO MINIMISE IMPACT ON THE 24-HOUR 'RUNAKI' PROJECT "
   "(SHAFAQ NEWS) | KRG MINISTRY OF NATURAL RESOURCES: OUTPUT 640 MMSCF/D FALLS TO 520 DURING MAINTENANCE; HOUSEHOLD GAS NOT "
   "AFFECTED (964) | SULAYMANIYAH GAS COMMITTEE: STOCKS BUILT OVER TWO MONTHS, NO HOUSEHOLD GAS CRISIS EXPECTED (SHAFAQ NEWS)"))
p["beats"] = [
 beat("الإعلان", "من 2 تشرين الأول لـ2 تشرين الثاني",
  "وزارة كهرباء الإقليم: صيانة «دانة غاز» لحقل كورمور تبدأ اليوم وتستمر حتى 2 تشرين الثاني، وستخفض تجهيز الكهرباء لعدة ساعات طوال المدة.",
  "31", "Days of Khor Mor maintenance, 2 Oct–2 Nov (KRG Ministry of Electricity)",
  "يوماً مدة صيانة كورمور (كهرباء الإقليم)",
  [("البداية", "2 تشرين الأول"), ("النهاية", "2 تشرين الثاني"), ("الحقل", "كورمور")], 1, slug,
  ["صيانة كورمور", "من اليوم", "لمدة شهر"], STOCK),
 beat("الغاز", "640 ينزل إلى 520 مليون قدم مكعب",
  "وزارة الثروات الطبيعية في الإقليم: إنتاج الحقل 640 مليون قدم مكعب يومياً، وسينخفض خلال الصيانة إلى 520 مليوناً (964).",
  "520", "Million cubic feet/day Khor Mor output during maintenance, down from 640 (KRG Natural Resources via 964)",
  "مليون قدم مكعب يومياً خلال الصيانة (الثروات الطبيعية)",
  [("الإنتاج الحالي", "640"), ("خلال الصيانة", "520"), ("الفرق", "120 (محتسب)")], 2, slug,
  ["640 مليون قدم", "ينزل إلى 520", "الكهرباء تتأثر"], STOCK),
 beat("غاز البيوت", "غاز المنازل: لا أزمة متوقعة",
  "الثروات الطبيعية: غاز المنازل لن يتأثر. ومشرف لجنة غاز السليمانية عمر عبد الله لشفق نيوز: خزّنّا كميات كافية خلال الشهرين الماضيين.",
  "640", "Million cubic feet/day current Khor Mor output (KRG Natural Resources via 964)",
  "مليون قدم مكعب يومياً الإنتاج الحالي (الثروات الطبيعية)",
  [("غاز المنازل", "لن يتأثر"), ("الخزين", "شهرين"), ("الصيانة", "سنوية كل تشرين الأول")], 3, slug,
  ["غاز البيوت", "لا أزمة متوقعة", "خزين شهرين"], "صورة أرشيفية — السليمانية"),
]
p["arabicTicker"] = [
 "وزارة الكهرباء في إقليم كوردستان: صيانة حقل كورمور من 2 تشرين الأول إلى 2 تشرين الثاني تخفض التجهيز لعدة ساعات",
 "الوزارة: التنسيق مع الثروات الطبيعية لتقليل الأثر على مشروع «رووناكي» للكهرباء 24 ساعة",
 "وزارة الثروات الطبيعية: الإنتاج 640 مليون قدم مكعب يومياً وينخفض إلى 520 خلال الصيانة (964)",
 "لجنة غاز السليمانية: لا مؤشرات على أزمة بغاز المنازل (شفق نيوز)",
 "كم ساعة كهرباء توصلك اليوم؟"]
p["endQuestion"] = "كم ساعة كهرباء توصلك اليوم؟"
p["sources"] = [{"name": "كهرباء إقليم كوردستان", "domain": "gov.krd"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "964", "domain": "964media.com"}]
SLATE[slug] = {"props": p, "caption": """كهرباء إقليم كوردستان — ساعات أقل لمدة شهر بسبب صيانة كورمور

وغاز البيوت؟ الجواب بالفيديو.

كم ساعة كهرباء توصلك اليوم؟

المصادر: كهرباء الإقليم عبر شفق نيوز، 964 (1-2 تشرين الأول 2026)

#الكهرباء #كوردستان #كورمور #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الكهرباء", "hookHeadline": "كهرباء أقل.. شهر كامل",
  "voText": "أعلنت وزارة الكهرباء في إقليم كوردستان أن شركة دانة غاز تبدأ اليوم صيانة حقل كورمور في السليمانية، وتستمر حتى الثاني من تشرين الثاني، ما سيخفض تجهيز الكهرباء لعدة ساعات طوال هذه المدة. وبحسب وزارة الثروات الطبيعية، ينخفض إنتاج الحقل خلال الصيانة من ستمئة وأربعين إلى خمسمئة وعشرين مليون قدم مكعب يومياً، من دون أن يتأثر غاز المنازل. وتقول لجنة الغاز في السليمانية إنها خزّنت كميات كافية مسبقاً. كم ساعة كهرباء توصلك اليوم؟",
  "endQuestion": "كم ساعة كهرباء توصلك اليوم؟",
  "sourcesLine": "المصادر: كهرباء إقليم كوردستان عبر شفق نيوز · 964 — 1 تشرين الأول 2026",
  "statPops": [{"value": "شهر كامل", "label": "صيانة كورمور حتى 2 تشرين الثاني", "matchWord": "وتستمر"},
               {"value": "520", "label": "مليون قدم مكعب يومياً خلال الصيانة", "matchWord": "وعشرين"}]}}


# ═══════════ E · 23:45 · P3 sport/pride — Sajjad Ali Muksir wrestling bronze (V10.1 CONTROL) ═══════════
slug = f"{D}-e-wrestling-bronze-16-years"
p = base(slug, "region_sport", "C", "آسياد ناغويا", "برونزية تنهي 16 سنة بلا ميدالية للمصارعة العراقية",
  ("NAGOYA · OCT 1 | IRAQI WRESTLER SAJJAD ALI MUKSIR WON BRONZE IN 60 KG GRECO-ROMAN AT THE AICHI-NAGOYA ASIAN GAMES, "
   "BEATING A SOUTH KOREAN IN THE BRONZE BOUT (SHAFAQ NEWS, INA, ALSUMARIA) | ROUTE: BEAT A TAJIK IN THE LAST 16 AND "
   "VIETNAM'S NGUYEN HUY IN THE QUARTER-FINAL, LOST THE SEMI TO KYRGYZSTAN'S SHARSHENBEKOV | IRAQI WRESTLING FEDERATION "
   "SECRETARY HADI HASSAN: IRAQ'S FIRST ASIAN GAMES WRESTLING MEDAL IN 16 YEARS"))
p["beats"] = [
 beat("الميدالية", "سجاد علي مكسر.. برونزية 60 كغم",
  "المصارع العراقي سجاد علي مكسر أحرز الخميس برونزية وزن 60 كغم بالمصارعة الرومانية في آسياد ناغويا، بفوزه على مصارع كوري جنوبي.",
  "60", "KG Greco-Roman category, Asian Games bronze (Shafaq News, INA)",
  "كغم وزن المنافسة — المصارعة الرومانية (شفق نيوز، واع)",
  [("الميدالية", "برونزية"), ("الأسلوب", "الروماني"), ("الدورة", "آسياد ناغويا")], 1, slug,
  ["سجاد علي مكسر", "برونزية", "وزن 60 كغم"], "صورة توضيحية"),
 beat("المشوار", "طاجكستان ثم فيتنام.. وتعثر أمام قرغيزستان",
  "حسب أمين سر اتحاد المصارعة هادي حسن: فاز على طاجيكي بدور الـ16 ثم على الفيتنامي نغوين هوي، وخسر نصف النهائي أمام القرغيزي شارشينبيكوف.",
  "16", "Round of 16 — first bout, against a Tajik wrestler (Wrestling Federation via Shafaq News)",
  "دور الـ16 — أول نزالاته (اتحاد المصارعة)",
  [("دور الـ16", "فوز"), ("ربع النهائي", "فوز"), ("نصف النهائي", "خسارة")], 2, slug,
  ["فوز على طاجيكستان", "فوز على فيتنام", "خسارة بنصف النهائي"], "صورة توضيحية"),
 beat("الإنجاز", "أول ميدالية آسيوية للمصارعة منذ 16 عاماً",
  "هادي حسن لشفق نيوز: العراق لم يحرز أي وسام في المصارعة بدورة الألعاب الآسيوية خلال 16 عاماً، ومكسر كسر هذا الصيام.",
  "16", "Years without an Iraqi Asian Games wrestling medal (Wrestling Federation via Shafaq News)",
  "عاماً بلا وسام آسيوي للمصارعة العراقية (اتحاد المصارعة)",
  [("آخر ميدالية", "قبل 16 عاماً"), ("المصدر", "اتحاد المصارعة"), ("اليوم", "الخميس")], 3, slug,
  ["16 سنة", "بلا ميدالية", "مكسر كسر الصيام"], "صورة توضيحية"),
]
p["arabicTicker"] = [
 "المصارع العراقي سجاد علي مكسر يحرز برونزية 60 كغم بالمصارعة الرومانية في آسياد ناغويا (شفق نيوز، واع، السومرية)",
 "فاز على طاجيكي وفيتنامي، وخسر نصف النهائي أمام القرغيزي شارشينبيكوف، ثم فاز بنزال البرونزية على كوري جنوبي",
 "اتحاد المصارعة: أول وسام آسيوي للمصارعة العراقية منذ 16 عاماً",
 "مارست المصارعة يوم؟"]
p["endQuestion"] = "مارست المصارعة يوم؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "واع", "domain": "ina.iq"}, {"name": "السومرية", "domain": "alsumaria.tv"}]
SLATE[slug] = {"props": p, "caption": """سجاد علي مكسر — برونزية المصارعة للعراق في آسياد ناغويا

أول ميدالية آسيوية للمصارعة العراقية من 16 سنة.. بالفيديو.

مارست المصارعة يوم؟

المصادر: شفق نيوز، واع، السومرية (1 تشرين الأول 2026)

#سجاد_علي_مكسر #المصارعة #العراق #آسياد_ناغويا #photonectnews
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
