#!/usr/bin/env python3
"""Author the 2026-09-30 slate: props.json + caption.txt (+ v11-brief.json on a, b, c, d; e = V10.1 control).

Every figure traces to a named source published 29-30 Sep 2026. Computed figures carry (محتسب).
NOTE: this is the PRE-copywriter draft. The Opus copywriter + two gate passes (apply_gate*_2026_09_30.py)
then edited the files on disk — do NOT re-run this script, it would revert those fixes.
All 20 frames are Commons/Pexels real photos (KIE -0.5 credits, Higgsfield 0.38) — see _image_credits_2026_09_30.json.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-30"
DATE_LABEL = "SEP 30 • 2026"
AR_DATE = "30 أيلول 2026"
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


# ═══════════ A · 18:00 · P1 corruption — 5.25 kg gold, Salahuddin land registry (LEAD) ═══════════
slug = f"{D}-a-gold-5kg-land-registry"
p = base(slug, "iraq_corruption", "A", "النزاهة", "5 كيلو ذهب.. بقضية معاونة مدير التسجيل العقاري",
  ("SALAHUDDIN · SEP 30 | FEDERAL INTEGRITY COMMISSION: INVESTIGATORS SEIZED 5.250 KG OF GOLD JEWELLERY BELONGING TO A "
   "DETAINED ACCUSED — THE ASSISTANT DIRECTOR OF THE SALAHUDDIN REAL-ESTATE REGISTRATION DIRECTORATE — IN AN ILLICIT-ENRICHMENT "
   "CASE | PER THE COMMISSION, AFTER THE CONFESSIONS OF HER HUSBAND (ALSO ACCUSED) THE TEAM TRACED JEWELLERY HER SISTER HAD MOVED "
   "FROM HER HOME TO ANOTHER PERSON'S HOUSE; SEIZED UNDER AN INVESTIGATIVE JUDGE'S ORDER | ON 30 AUG THE COMMISSION SEIZED "
   "DEEDS FOR 95 PROPERTIES (BAGHDAD, DIYALA, SALAHUDDIN) AND 31 BLANK THUMB-PRINTED FORMS | CASE UNDER INVESTIGATION — NO "
   "VERDICT (INTEGRITY COMMISSION VIA SHAFAQ NEWS, AL-MUSTAQILLA, KALIMA)"))
p["beats"] = [
 beat("الضبط", "5 كيلو و250 غرام ذهب",
  "هيئة النزاهة: ضبط 5.250 كغم مصوغات ذهبية تعود لمتهمة موقوفة، معاونة مدير التسجيل العقاري في صلاح الدين، بقضية كسب غير مشروع.",
  "5.25", "KG of gold jewellery seized, Salahuddin land-registry case (Integrity Commission)",
  "كغم مصوغات ذهبية مضبوطة (هيئة النزاهة)",
  [("المتهمة", "موقوفة"), ("القضية", "كسب غير مشروع"), ("المحافظة", "صلاح الدين")], 1, slug,
  ["خمسة كيلو ذهب", "معاونة مدير", "التسجيل العقاري"], STOCK),
 beat("الطريق للذهب", "نُقل من البيت.. واعترافات قادت إليه",
  "حسب الهيئة: بعد تدوين اعترافات زوجها المتهم، وصل الفريق إلى الذهب الذي نقلته شقيقتها من منزلها إلى دار شخص آخر، بقرار قاضي التحقيق.",
  "95", "Property deeds seized from the same accused on 30 Aug (Integrity Commission)",
  "سند عقار ضُبط في 30 آب بنفس القضية (النزاهة)",
  [("الزوج", "متهم"), ("الضبط", "بقرار قضائي"), ("عقارات آب", "95")], 2, slug,
  ["اعترافات الزوج", "الذهب نُقل من البيت", "بقرار قاضي التحقيق"], STOCK),
 beat("قبل شهر", "95 عقاراً و31 بياناً على بياض",
  "في 30 آب أعلنت الهيئة ضبط سندات 95 عقاراً ببغداد وديالى وصلاح الدين، و31 بياناً مبصوماً على بياض. القضية ما زالت قيد التحقيق.",
  "31", "Blank thumb-printed forms seized on 30 Aug (Integrity Commission)",
  "بياناً مبصوماً على بياض ضُبط في آب (النزاهة)",
  [("العقارات", "95"), ("المحافظات", "3"), ("الحالة", "قيد التحقيق")], 3, slug,
  ["95 عقاراً", "31 بياناً على بياض", "القضية قيد التحقيق"], STOCK),
]
p["arabicTicker"] = [
 "هيئة النزاهة: ضبط 5.250 كغم مصوغات ذهبية تعود لمتهمة موقوفة — معاونة مدير التسجيل العقاري في صلاح الدين (30 أيلول)",
 "الهيئة: الذهب نُقل من منزل المتهمة بواسطة شقيقتها إلى دار أحد الأشخاص، ووصل إليه الفريق بعد اعترافات زوجها المتهم",
 "في 30 آب: ضبط سندات 95 عقاراً ببغداد وديالى وصلاح الدين و31 بياناً مبصوماً على بياض",
 "القضية ما زالت قيد التحقيق — لم يصدر حكم",
 "راجعت دائرة التسجيل العقاري هالسنة؟"]
p["endQuestion"] = "راجعت دائرة التسجيل العقاري هالسنة؟"
p["sources"] = [{"name": "هيئة النزاهة", "domain": "nazaha.iq"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "المستقلة", "domain": "mustaqila.com"}, {"name": "كلمة", "domain": "kalimaiq.com"}]
SLATE[slug] = {"props": p, "caption": """النزاهة تضبط ذهب بقضية التسجيل العقاري في صلاح الدين — شنو القصة؟

من اعترافات الزوج إلى ذهب منقول لبيت ثاني.. التفاصيل بالفيديو.

راجعت دائرة التسجيل العقاري هالسنة؟

المصادر: هيئة النزاهة عبر شفق نيوز، المستقلة، كلمة (30 أيلول 2026)

#هيئة_النزاهة #العراق #صلاح_الدين #مكافحة_الفساد #photonectnews
@photonect.news""",
 "brief": {"kicker": "النزاهة", "hookHeadline": "5 كيلو ذهب.. بقضية موظفة عقاري",
  "voText": "أعلنت هيئة النزاهة الاتحادية، اليوم الأربعاء، ضبط خمسة كيلوغرامات ومئتين وخمسين غراماً من المصوغات الذهبية، تعود لمتهمة موقوفة تعمل معاونةً لمدير التسجيل العقاري في صلاح الدين، بقضية كسب غير مشروع. وبحسب الهيئة، قادت اعترافات زوجها، وهو متهم أيضاً، إلى ذهب نقلته شقيقتها من منزلها إلى دار شخص آخر. وكانت الهيئة قد ضبطت في آب الماضي سندات خمسة وتسعين عقاراً، وواحداً وثلاثين بياناً مبصوماً على بياض. والقضية ما زالت قيد التحقيق. راجعت دائرة التسجيل العقاري هالسنة؟",
  "endQuestion": "راجعت دائرة التسجيل العقاري هالسنة؟",
  "sourcesLine": "المصادر: هيئة النزاهة عبر شفق نيوز · المستقلة · كلمة — 30 أيلول 2026",
  "statPops": [{"value": "5.25 كغم", "label": "مصوغات ذهبية مضبوطة (النزاهة)", "matchWord": "كيلوغرامات"},
               {"value": "95", "label": "سند عقار ضُبط في آب", "matchWord": "عقاراً"}]}}


# ═══════════ B · 19:45 · P1 dollar anchor — 157,250 + gold jump ═══════════
slug = f"{D}-b-dollar-157250-third-rise"
p = base(slug, "iraq_money", "B", "الدولار اليوم", "الدولار 157,250.. ومثقال الذهب يقفز 15 ألفاً",
  ("BAGHDAD · SEP 30 | SHAFAQ NEWS: KIFAH & HARITHIYA BOURSES 157,250 IQD PER $100 WEDNESDAY MORNING, UP FROM 157,000 "
   "TUESDAY MORNING (+250, COMPUTED) AND 156,000 MONDAY MORNING | BAGHDAD EXCHANGE SHOPS: SELL 157,750 / BUY 156,750 "
   "(1,000 GAP, COMPUTED); ERBIL SELL 157,450 / BUY 157,400 | GOLD, AL-NAHR ST WHOLESALE: 21K GULF/TURKISH/EUROPEAN MITHQAL "
   "SELLS AT 930,000 IQD (BUY 926,000), UP FROM 915,000 TUESDAY (+15,000, COMPUTED); IRAQI 21K 900,000 (SHAFAQ NEWS)"))
p["beats"] = [
 beat("البورصة", "157,250 صباح الأربعاء",
  "شفق نيوز: بورصتا الكفاح والحارثية سجّلتا صباح الأربعاء 157,250 ديناراً لكل 100 دولار، بعد 157,000 صباح الثلاثاء.",
  "157,250", "IQD per $100, Kifah & Harithiya bourses, Wednesday morning (Shafaq News)",
  "دينار لكل 100 دولار — الكفاح والحارثية صباح الأربعاء (شفق نيوز)",
  [("الثلاثاء", "157,000"), ("الاثنين", "156,000"), ("الفرق", "250+ (محتسب)")], 1, slug,
  ["الدولار يواصل", "157,250 دينار", "الثلاثاء كان 157,000"], STOCK),
 beat("الصيرفة", "بين البيع والشراء.. ألف دينار",
  "محال الصيرفة ببغداد: البيع 157,750 والشراء 156,750 لكل 100 دولار. وبأربيل: البيع 157,450 والشراء 157,400 (شفق نيوز).",
  "157,750", "IQD per $100, Baghdad exchange-shop selling price, Wednesday morning (Shafaq News)",
  "دينار سعر البيع لكل 100 دولار بمحال بغداد (شفق نيوز)",
  [("بغداد شراء", "156,750"), ("الفرق", "1,000 (محتسب)"), ("أربيل بيع", "157,450")], 2, slug,
  ["البيع 157,750", "الشراء 156,750", "الفرق ألف دينار"], STOCK),
 beat("الذهب", "مثقال شارع النهر 930 ألفاً",
  "شفق نيوز: مثقال عيار 21 الخليجي والتركي والأوروبي بجملة شارع النهر 930,000 دينار بيعاً، بعد 915,000 الثلاثاء. والعراقي 900,000.",
  "930,000", "IQD per mithqal, 21K Gulf/Turkish/European gold, Al-Nahr St wholesale sell price (Shafaq News)",
  "دينار مثقال عيار 21 — جملة شارع النهر (شفق نيوز)",
  [("الثلاثاء", "915,000"), ("الفرق", "15,000+ (محتسب)"), ("العراقي 21", "900,000")], 3, slug,
  ["الذهب يقفز", "المثقال 930 ألف", "أمس 915 ألف"], STOCK),
]
p["arabicTicker"] = [
 "شفق نيوز: الدولار في بورصتي الكفاح والحارثية 157,250 ديناراً لكل 100 دولار صباح الأربعاء، بعد 157,000 صباح الثلاثاء",
 "محال الصيرفة ببغداد: البيع 157,750 والشراء 156,750 — أربيل: البيع 157,450 والشراء 157,400",
 "الذهب بجملة شارع النهر: مثقال عيار 21 الخليجي 930,000 دينار بيعاً و926,000 شراءً، بعد 915,000 الثلاثاء",
 "مثقال الذهب العراقي عيار 21: 900,000 دينار بيعاً (شفق نيوز)",
 "عندك ذهب محفوظ بالبيت؟"]
p["endQuestion"] = "عندك ذهب محفوظ بالبيت؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}]
SLATE[slug] = {"props": p, "caption": """سعر الدولار في العراق اليوم — ومثقال الذهب بشارع النهر يقفز

البورصة والصيرفة والذهب.. أرقام الأربعاء بالفيديو.

عندك ذهب محفوظ بالبيت؟

المصادر: شفق نيوز (30 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #سعر_الذهب #العراق #photonectnews
@photonect.news""",
 "brief": {"kicker": "الدولار اليوم", "hookHeadline": "الدولار يواصل.. والذهب يقفز",
  "voText": "واصل الدولار ارتفاعه في بغداد صباح الأربعاء. فبحسب شفق نيوز، سجّلت بورصتا الكفاح والحارثية مئة وسبعة وخمسين ألفاً ومئتين وخمسين ديناراً لكل مئة دولار، بعد مئة وسبعة وخمسين ألفاً صباح الثلاثاء. وفي محال الصيرفة ببغداد، بلغ سعر البيع مئة وسبعة وخمسين ألفاً وسبعمئة وخمسين، والشراء أقل بألف دينار. أما الذهب، فقفز مثقال عيار واحد وعشرين الخليجي في جملة شارع النهر إلى تسعمئة وثلاثين ألف دينار، بعد تسعمئة وخمسة عشر ألفاً يوم الثلاثاء. عندك ذهب محفوظ بالبيت؟",
  "endQuestion": "عندك ذهب محفوظ بالبيت؟",
  "sourcesLine": "المصادر: شفق نيوز — 30 أيلول 2026",
  "statPops": [{"value": "157,250", "label": "الكفاح والحارثية — صباح الأربعاء", "matchWord": "والحارثية"},
               {"value": "930,000", "label": "دينار مثقال عيار 21 — شارع النهر", "matchWord": "النهر"}]}}


# ═══════════ C · 21:15 · P2 Iraq–US — coalition mission ends, Sadr dissolves brigade ═══════════
slug = f"{D}-c-coalition-mission-ends"
p = base(slug, "mena_geopolitics", "A", "يوم السيادة", "انتهت مهمة التحالف.. والصدر يحل «اليوم الموعود»",
  ("BAGHDAD · SEP 30 | PM ALI AL-ZAIDI, AT AN OFFICIAL 'SOVEREIGNTY DAY' CEREMONY ATTENDED BY THE COALITION COMMANDER, "
   "ANNOUNCED THE OFFICIAL END OF THE INTERNATIONAL COALITION'S ANTI-ISIS MISSION IN IRAQ: 'NO WEAPONS OUTSIDE THE UMBRELLA OF "
   "THE LAW' (PM OFFICE VIA SHAFAQ NEWS, SHAFAQNA, INA) | PENTAGON: ORDERLY WITHDRAWAL OF COALITION FORCES AND EQUIPMENT FROM "
   "ERBIL AIR BASE CONCLUDES OPERATION INHERENT RESOLVE IN IRAQ; TARGETED TRAINING AND INTELLIGENCE SUPPORT CONTINUE | "
   "GOVT PLAN (ANNOUNCED 21 SEP): 90-DAY DE-ESCALATION, THEN WEAPONS HANDOVER COMPLETE BY 30 JUNE 2027 (SHAFAQ NEWS) | "
   "MUQTADA AL-SADR DISSOLVES 'PROMISED DAY BRIGADE', DEMANDS US COMPENSATION (SADR ON X VIA SHAFAQ NEWS, ARABI21)"))
p["beats"] = [
 beat("الإعلان", "الزيدي: مهمة التحالف انتهت رسمياً",
  "في حفل يوم السيادة وبحضور قائد التحالف، أعلن الزيدي الانتهاء الرسمي لمهمة التحالف الدولي ضد داعش: «لا سلاح خارج مظلة القانون».",
  "30", "September 2026 — 'Sovereignty Day', official end of the coalition mission (PM office)",
  "أيلول — يوم السيادة وانتهاء مهمة التحالف (مكتب رئيس الوزراء)",
  [("المهمة", "محاربة داعش"), ("الحضور", "قائد التحالف"), ("الشعار", "لا سلاح خارج القانون")], 1, slug,
  ["يوم السيادة", "انتهت مهمة التحالف", "لا سلاح خارج القانون"], "صورة أرشيفية — علي الزيدي"),
 beat("البنتاغون", "البنتاغون: الانسحاب من أربيل يختم المهمة",
  "البنتاغون: الانسحاب من قاعدة أربيل الجوية يختتم «العزم الصلب»، مع تدريب ودعم استخباري. وخطة الحكومة: تهدئة 90 يوماً ثم تسليم السلاح (شفق نيوز).",
  "90", "Day de-escalation phase in the government's weapons plan announced 21 Sep (Shafaq News)",
  "يوماً مرحلة تهدئة بخطة الحكومة لحصر السلاح (شفق نيوز)",
  [("القاعدة", "أربيل الجوية"), ("يستمر", "تدريب واستخبارات"), ("اكتمال التسليم", "30 حزيران 2027")], 2, slug,
  ["الانسحاب من أربيل", "العزم الصلب انتهت", "تدريب ودعم استخباري"], "صورة أرشيفية — مطار أربيل"),
 beat("الصدر", "الصدر يحل «لواء اليوم الموعود»",
  "الصدر أعلن حل «لواء اليوم الموعود» وتحويل «جيش الإمام» إلى مؤسسة، وطالب الجيش الأميركي بتعويضات، ودعا لحصر السلاح بيد الدولة (شفق نيوز، عربي21).",
  "2027", "30 June 2027 — deadline for completing the weapons handover in the government plan (Shafaq News)",
  "حزيران — موعد اكتمال تسليم السلاح بخطة الحكومة (شفق نيوز)",
  [("اللواء", "حُلّ فوراً"), ("جيش الإمام", "صار مؤسسة"), ("طالب", "تعويضات أميركية")], 3, slug,
  ["الصدر يحل اللواء", "ويطالب بتعويضات", "وحصر السلاح بيد الدولة"], "صورة أرشيفية — مقتدى الصدر 2019"),
]
p["arabicTicker"] = [
 "الزيدي يعلن الانتهاء الرسمي لمهمة التحالف الدولي لمحاربة داعش في العراق — حفل يوم السيادة 30 أيلول",
 "البنتاغون: الانسحاب المنظم من قاعدة أربيل الجوية يمثل ختام المهمة العسكرية للتحالف في العراق",
 "خطة الحكومة لحصر السلاح: تهدئة 90 يوماً ثم تسليم يكتمل بحلول 30 حزيران 2027 (شفق نيوز)",
 "مقتدى الصدر يعلن حل لواء اليوم الموعود ويطالب الجيش الأميركي بتعويضات",
 "كم كان عمرك لما بدأت الحرب على داعش؟"]
p["endQuestion"] = "كم كان عمرك لما بدأت الحرب على داعش؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "شفقنا العراق", "domain": "iraq.shafaqna.com"}, {"name": "عربي21", "domain": "arabi21.com"}]
SLATE[slug] = {"props": p, "caption": """انتهاء مهمة التحالف الدولي في العراق — شنو يتغير بعد اليوم؟

إعلان الزيدي، بيان البنتاغون، وقرار الصدر.. بالفيديو.

كم كان عمرك لما بدأت الحرب على داعش؟

المصادر: مكتب رئيس الوزراء عبر شفق نيوز وشفقنا، البنتاغون، عربي21 (30 أيلول 2026)

#العراق #يوم_السيادة #التحالف_الدولي #حصر_السلاح #photonectnews
@photonect.news""",
 "brief": {"kicker": "يوم السيادة", "hookHeadline": "انتهت مهمة التحالف.. شنو بعد؟",
  "voText": "أعلن رئيس الوزراء علي الزيدي، اليوم الأربعاء، الانتهاء الرسمي لمهمة التحالف الدولي لمحاربة داعش في العراق، خلال حفل بمناسبة يوم السيادة، مؤكداً أن لا سلاح خارج مظلة القانون. وقالت وزارة الدفاع الأميركية إن الانسحاب من قاعدة أربيل الجوية يختتم المهمة، مع استمرار التدريب والدعم الاستخباري. وبالتزامن، أعلن مقتدى الصدر حل لواء اليوم الموعود، وطالب الجيش الأميركي بتعويضات. وتنص خطة الحكومة على اكتمال تسليم سلاح الفصائل بحلول حزيران ألفين وسبعة وعشرين. كم كان عمرك لما بدأت الحرب على داعش؟",
  "endQuestion": "كم كان عمرك لما بدأت الحرب على داعش؟",
  "sourcesLine": "المصادر: مكتب رئيس الوزراء عبر شفق نيوز · البنتاغون · عربي21 — 30 أيلول 2026",
  "statPops": [{"value": "30 أيلول", "label": "يوم السيادة — انتهاء مهمة التحالف", "matchWord": "السيادة"},
               {"value": "2027", "label": "حزيران — موعد اكتمال تسليم سلاح الفصائل", "matchWord": "حزيران"}]}}


# ═══════════ D · 22:30 · P1 housing — Watan: 275,000 plots ready ═══════════
slug = f"{D}-d-watan-275000-plots"
p = base(slug, "iraq_money", "B", "مبادرة وطن", "275 ألف قطعة أرض جاهزة.. والتسجيل الشهر المقبل",
  ("BAGHDAD · SEP 29 | PM OFFICE: AT THE HIGH COMMITTEE OF THE ONE-MILLION RESIDENTIAL PLOTS PROJECT ('WATAN INITIATIVE'), "
   "PM CHIEF OF STAFF IHSAN AL-AWADI SAID PROCEDURES FOR 275,000 PLOTS ARE COMPLETE AND READY FOR REAL-ESTATE DEVELOPMENT; "
   "THE PROJECT SPANS 121 CITIES IN 15 GOVERNORATES; INFRASTRUCTURE CONTRACTING HAS BEGUN, FIRST FOUNDATION STONE 'IN THE "
   "COMING DAYS' | PM AL-ZAIDI: LAUNCH THE CITIZEN REGISTRATION LINK AS SOON AS POSSIBLE NEXT MONTH; DISTRIBUTION BY PLACE OF "
   "RESIDENCE AT GOVERNORATE AND DISTRICT LEVEL, COVERING ELIGIBLE AND POOR FAMILIES | JUSTICE MINISTRY TO SPEED STATE-PROPERTY "
   "DATABASE; PROPOSALS TO SPEED TITLES FOR HOMES BUILT ON FARMLAND (DECISION 320/2022) (SHAFAQ NEWS, KALIMA, SHAFAQNA)"))
p["beats"] = [
 beat("الجاهز", "275 ألف قطعة من مليون",
  "مكتب رئيس الوزراء: اكتملت إجراءات 275 ألف قطعة أرض سكنية ضمن «مبادرة وطن» لمشروع المليون قطعة، وهُيّئت للتطوير العقاري.",
  "275,000", "Residential plots with completed procedures under the Watan one-million-plots project (PM office)",
  "قطعة أرض اكتملت إجراءاتها (مكتب رئيس الوزراء)",
  [("الهدف", "مليون قطعة"), ("المدن", "121"), ("المحافظات", "15")], 1, slug,
  ["مبادرة وطن", "275 ألف قطعة", "من أصل مليون"], STOCK),
 beat("التسجيل", "رابط التسجيل خلال الشهر المقبل",
  "الزيدي وجّه بإطلاق رابط تسجيل المواطنين خلال الشهر المقبل، والتوزيع حسب محل السكن بالمحافظة والقضاء، بما يشمل العوائل المستحقة والفقيرة.",
  "15", "Governorates covered by the Watan project, across 121 cities (PM office)",
  "محافظة يشملها المشروع في 121 مدينة (مكتب رئيس الوزراء)",
  [("التسجيل", "الشهر المقبل"), ("التوزيع", "حسب محل السكن"), ("المستوى", "المحافظة والقضاء")], 2, slug,
  ["رابط التسجيل", "الشهر المقبل", "حسب محل السكن"], STOCK),
 beat("الخدمات", "بنى تحتية.. وحجر أساس قريباً",
  "إحسان العوادي: بدأت إجراءات التعاقد على البنى التحتية للأراضي الجاهزة، وحجر الأساس بأول محافظة خلال الأيام المقبلة (شفق نيوز، كلمة).",
  "121", "Cities in the Watan one-million-plots project (PM office)",
  "مدينة ضمن المشروع (مكتب رئيس الوزراء)",
  [("التعاقد", "بدأ"), ("حجر الأساس", "الأيام المقبلة"), ("قرار التمليك", "320 لسنة 2022")], 3, slug,
  ["البنى التحتية", "التعاقد بدأ", "حجر أساس قريباً"], STOCK),
]
p["arabicTicker"] = [
 "مكتب رئيس الوزراء: اكتمال إجراءات 275 ألف قطعة أرض سكنية ضمن مبادرة وطن — مشروع المليون قطعة (29 أيلول)",
 "المشروع يتوزع على 121 مدينة في 15 محافظة",
 "الزيدي: إطلاق رابط التسجيل للمواطنين خلال الشهر المقبل، والتوزيع حسب محل السكن بالمحافظة والقضاء",
 "بدء إجراءات التعاقد على البنى التحتية، وحجر الأساس بأول محافظة خلال الأيام المقبلة (إحسان العوادي)",
 "ساكن بملك لو إيجار؟"]
p["endQuestion"] = "ساكن بملك لو إيجار؟"
p["sources"] = [{"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "كلمة", "domain": "kalimaiq.com"}, {"name": "شفقنا العراق", "domain": "iraq.shafaqna.com"}]
SLATE[slug] = {"props": p, "caption": """مبادرة وطن قطع الأراضي السكنية — متى رابط التسجيل؟

كم قطعة جاهزة، وين، وشلون التوزيع.. بالفيديو.

ساكن بملك لو إيجار؟

المصادر: مكتب رئيس الوزراء عبر شفق نيوز، كلمة، شفقنا (29 أيلول 2026)

#مبادرة_وطن #قطع_الأراضي #العراق #السكن #photonectnews
@photonect.news""",
 "brief": {"kicker": "مبادرة وطن", "hookHeadline": "قطعة أرض؟ التسجيل الشهر الجاي",
  "voText": "قال مكتب رئيس الوزراء، يوم الثلاثاء، إن إجراءات مئتين وخمسة وسبعين ألف قطعة أرض سكنية اكتملت ضمن مبادرة وطن، مشروع المليون قطعة. ويتوزع المشروع على مئة وإحدى وعشرين مدينة في خمس عشرة محافظة. ووجّه رئيس الوزراء علي الزيدي بإطلاق رابط تسجيل المواطنين خلال الشهر المقبل، وبأن يكون التوزيع حسب محل السكن، بما يضمن شمول العوائل المستحقة والفقيرة. كما بدأت إجراءات التعاقد على البنى التحتية، مع حجر أساس مرتقب في أول محافظة. ساكن بملك لو إيجار؟",
  "endQuestion": "ساكن بملك لو إيجار؟",
  "sourcesLine": "المصادر: مكتب رئيس الوزراء عبر شفق نيوز · كلمة · شفقنا — 29 أيلول 2026",
  "statPops": [{"value": "275,000", "label": "قطعة أرض اكتملت إجراءاتها", "matchWord": "وسبعين"},
               {"value": "121", "label": "مدينة في 15 محافظة", "matchWord": "مدينة"}]}}


# ═══════════ E · 23:45 · P3 sport/pride — Ali Ammar 219 kg snatch WR (V10.1 CONTROL) ═══════════
slug = f"{D}-e-ali-ammar-219kg"
p = base(slug, "region_sport", "C", "آسياد ناغويا", "رقم عالمي بالخطف.. وفضية بفارق كيلو واحد",
  ("AICHI-NAGOYA · SEP 29 | REUTERS: IRAQ'S ALI AMMAR SET A SNATCH WORLD RECORD OF 219 KG IN THE MEN'S +110 KG AT THE ASIAN "
   "GAMES, ABOVE THE IWF 218 KG WORLD STANDARD | TOTAL 465 KG (219 + 246) — ONE KG SHORT OF IRAN'S ALI DAVOUDI, 466 KG "
   "(204 + 262); SILVER FOR IRAQ, BRONZE BAHRAIN'S GOR MINASYAN (SHAFAQ NEWS) | IRAQI OLYMPIC COMMITTEE: ORGANISERS SHOWED THE "
   "IRANIAN FLAG AND STARTED THE TIMER BEFORE SWITCHING TO THE IRAQI FLAG, LEAVING TOO LITTLE TIME FOR HIS LAST ATTEMPT "
   "(VIA AL-MASHHAD) | AMMAR TO REUTERS: 'IF I HAD 10 MORE SECONDS THAT WOULD HAVE BEEN GREAT'"))
p["beats"] = [
 beat("الرقم", "219 كغم.. رقم عالمي بالخطف",
  "الرباع علي عمار رفع 219 كغم بالخطف في وزن +110 كغم بآسياد ناغويا، متجاوزاً المعيار العالمي 218 كغم (رويترز).",
  "219", "KG snatch by Iraq's Ali Ammar, a world record above the IWF 218 kg standard (Reuters)",
  "كغم رفعة خطف — رقم عالمي (رويترز)",
  [("المعيار السابق", "218"), ("الوزن", "+110 كغم"), ("الدورة", "آسياد ناغويا")], 1, slug,
  ["علي عمار", "219 كيلو بالخطف", "رقم عالمي"], "صورة توضيحية"),
 beat("الفارق", "الفضية بفارق كيلو واحد",
  "مجموع علي عمار 465 كغم (219 خطف و246 نتر)، والإيراني علي داوودي 466 كغم أخذ الذهبية. البرونزية للبحريني غور ميناسيان (رويترز، شفق نيوز).",
  "465", "KG total for Ali Ammar — silver, one kg behind Iran's Ali Davoudi on 466 (Reuters)",
  "كغم مجموع علي عمار — الفضية (رويترز)",
  [("داوودي", "466"), ("الفارق", "1 كغم"), ("النتر", "246")], 2, slug,
  ["المجموع 465", "داوودي 466", "بفارق كيلو واحد"], "صورة توضيحية"),
 beat("الاعتراض", "اعتراض عراقي على التوقيت",
  "اللجنة الأولمبية العراقية: المنظمون عرضوا العلم الإيراني وشغّلوا العدّ ثم بدّلوه بالعراقي، فلم يكفِ الوقت لمحاولته الأخيرة. وعمار لرويترز: «لو عندي 10 ثوانٍ إضافية».",
  "10", "Extra seconds Ali Ammar told Reuters he needed for his last attempt",
  "ثوانٍ قال علي عمار إنه احتاجها (رويترز)",
  [("المحاولة", "الأخيرة بالنتر"), ("الموقف", "اعتراض رسمي"), ("النتيجة", "فضية")], 3, slug,
  ["اعتراض عراقي", "العلم والتوقيت", "عشر ثوانٍ"], "صورة توضيحية"),
]
p["arabicTicker"] = [
 "رويترز: العراقي علي عمار يسجل رقماً عالمياً في الخطف 219 كغم بوزن +110 كغم في دورة الألعاب الآسيوية",
 "المجموع: علي عمار 465 كغم (فضية) — الإيراني علي داوودي 466 كغم (ذهبية) — البحريني غور ميناسيان (برونزية)",
 "اللجنة الأولمبية العراقية تعترض: العلم الإيراني عُرض والتوقيت شُغّل قبل تبديله بالعلم العراقي",
 "علي عمار لرويترز: لو كان عندي 10 ثوانٍ إضافية لكان الأمر رائعاً",
 "كم كيلو تكدر ترفع؟"]
p["endQuestion"] = "كم كيلو تكدر ترفع؟"
p["sources"] = [{"name": "رويترز", "domain": "reuters.com"}, {"name": "شفق نيوز", "domain": "shafaq.com"}, {"name": "المشهد", "domain": "almashhad.com"}]
SLATE[slug] = {"props": p, "caption": """علي عمار رباع العراق — رقم عالمي بآسياد ناغويا والفضية بفارق كيلو

شنو صار بالمحاولة الأخيرة؟ بالفيديو.

كم كيلو تكدر ترفع؟

المصادر: رويترز، شفق نيوز، المشهد (29-30 أيلول 2026)

#علي_عمار #رفع_الأثقال #العراق #آسياد_ناغويا #photonectnews
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
