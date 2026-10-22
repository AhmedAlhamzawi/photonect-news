#!/usr/bin/env python3
"""Author the 2026-10-22 slate: props.json + caption.txt (+ v11-brief.json for a-d). e = silent V10.1 control."""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
D = "2026-10-22"
DL, ADL = "OCT 22 • 2026", "22 تشرين الأول 2026"

def beat(slug, n, label, h, body, bs_v, bs_en, bs_ar, pills, subs):
    img = f"images/news/{D}-{slug}/broll_{n}.jpg"
    return {"label": label, "arabicHeading": h, "arabicBody": body,
            "bigStat": {"value": bs_v, "label": bs_en, "arabicLabel": bs_ar},
            "supportingStats": [{"label": l, "value": v} for l, v in pills],
            "broll": img, "brolls": [img], "brollType": "image", "accent": "#FFC217",
            "brollSource": "صورة توضيحية", "subtitlePhrases": subs}

S = {}
# ---------------- A · Dhi Qar governorate accounts director caught taking a bribe (accused, not convicted) ----------------
S["a-dhiqar-accounts-bribe-caught"] = dict(
 bucket="iraq_corruption", variant="A", kicker="النزاهة",
 headline="مدير حسابات ديوان ذي قار.. بالجرم المشهود",
 sub="DHI QAR · OCT 22 (THU) | FEDERAL INTEGRITY COMMISSION: HEAD OF THE ACCOUNTS DEPARTMENT AT THE DHI QAR GOVERNORATE OFFICE AND ONE OF HIS STAFF CAUGHT RED-HANDED RECEIVING A BRIBE FROM A CONTRACTOR (STATEMENT VIA BAGHDAD TODAY, 964, AL-MADA) | PER THE COMMISSION: THE TWO OBSTRUCTED PAYMENT OF THE CONTRACTOR'S DUES FOR A PROJECT IN AL-NASR DISTRICT DESPITE HIM COMPLETING ALL PROCEDURES AND FOLLOWING UP REPEATEDLY | DHI QAR INTEGRITY INVESTIGATION JUDGE ORDERED BOTH DETAINED UNDER PENAL CODE ARTICLE 308 — ACCUSED, NOT CONVICTED",
 beats=[
  ("الضبط", "النزاهة تضبط مدير حسابات ديوان ذي قار",
   "أعلنت هيئة النزاهة الاتحادية، الخميس، ضبط مدير قسم الحسابات في ديوان محافظة ذي قار وموظف في القسم بالجرم المشهود (بيان الهيئة).",
   "2", "Officials caught red-handed at the Dhi Qar governorate office, Thu (Integrity Commission)", "متهمان",
   [("المكان", "ديوان ذي قار"), ("اليوم", "الخميس"), ("الصفة", "متهمان")],
   ["ديوان محافظة ذي قار", "مدير قسم الحسابات", "بالجرم المشهود"]),
  ("المقاول", "مقاول أكمل معاملته.. ومستحقاته متعطلة",
   "بحسب الهيئة، عرقل المتهمان صرف مستحقات مقاول نفّذ مشروعاً في قضاء النصر، رغم إكماله الإجراءات كافة وتكرار مراجعته.",
   "النصر", "District where the contractor's project is located (Integrity Commission)", "قضاء المشروع",
   [("القضاء", "النصر"), ("الإجراءات", "مكتملة"), ("المراجعات", "متكررة")],
   ["مستحقات مقاول", "الإجراءات مكتملة", "مراجعات متكررة"]),
  ("التوقيف", "توقيف المتهمَين وفق المادة 308",
   "قاضي محكمة التحقيق المختصة بقضايا النزاهة في ذي قار قرر توقيف المتهمَين وفق المادة 308 من قانون العقوبات (بغداد اليوم، 964، المدى).",
   "308", "Penal Code article cited for the detention (Integrity Commission)", "المادة من قانون العقوبات",
   [("القرار", "توقيف"), ("المادة", "308"), ("الصفة", "متهمان")],
   ["قاضي تحقيق النزاهة", "المادة 308", "توقيف المتهمَين"]),
 ],
 ticker=["النزاهة: ضبط مدير حسابات ديوان ذي قار وموظف بالجرم المشهود (بغداد اليوم، 964، المدى)",
         "بحسب الهيئة: عرقلا صرف مستحقات مقاول رغم إكماله الإجراءات",
         "توقيف المتهمَين وفق المادة 308 من قانون العقوبات"],
 q="راجعت دائرة أكثر من مرة لمعاملة وحدة؟",
 sources=[("هيئة النزاهة الاتحادية", "nazaha.iq"), ("بغداد اليوم", "baghdadtoday.news"), ("شبكة 964", "964media.com"), ("المدى", "almadapaper.net")],
 brief=dict(kicker="النزاهة", hook="ضبط مدير حسابات بالجرم المشهود",
  vo="أعلنت هيئة النزاهة الاتحادية، يوم الخميس، ضبط مدير قسم الحسابات في ديوان محافظة ذي قار وأحد موظفي القسم، بالجرم المشهود أثناء تسلّمهما مبلغ رشوة من أحد المقاولين. وبحسب بيان الهيئة، عرقل المتهمان صرف مستحقات المقاول عن مشروع ينفذه في قضاء النصر، رغم إكماله الإجراءات كافة وتكرار مراجعته. وقرر قاضي التحقيق المختص بقضايا النزاهة في ذي قار توقيفهما وفق المادة ثلاثمئة وثمانية من قانون العقوبات. راجعت دائرة أكثر من مرة لمعاملة وحدة؟",
  pops=[{"value": "2", "label": "متهمان — ديوان ذي قار", "matchWord": "الحسابات"},
        {"value": "المادة 308", "label": "توقيف وفق قانون العقوبات", "matchWord": "ثلاثمئة"}],
  srcline="المصادر: هيئة النزاهة الاتحادية · بغداد اليوم · شبكة 964 · المدى — 22 تشرين الأول 2026"),
 caption=["رشوة بديوان محافظة ذي قار؟ شنو كشفت النزاهة",
          "مقاول، ومعاملة متعطلة، وضبط بالجرم المشهود. التفاصيل بالفيديو.",
          "راجعت دائرة أكثر من مرة لمعاملة وحدة؟",
          "المصادر: هيئة النزاهة عبر بغداد اليوم، شبكة 964، المدى (22 تشرين الأول 2026)",
          "#العراق #ذي_قار #هيئة_النزاهة #photonectnews"])

# ---------------- B · dollar ----------------
S["b-dollar-170000-shops"] = dict(
 bucket="iraq_money", variant="B", kicker="الدولار اليوم",
 headline="المية دولار بالصيرفة وصلت 170 ألف",
 sub="BAGHDAD · OCT 22 (THU) | KIFAH AND HARITHIYA BOURSES 169,500 IQD PER $100 THURSDAY MORNING VS 168,900 WEDNESDAY (SHAFAQ) | BAGHDAD SHOPS SELL 170,000 / BUY 169,000 (SHAFAQ); 964: BAGHDAD SELL 170,000, ERBIL 169,700, BASRA 169,500; AL-MADA: PRICES CROSS THE 170,000 THRESHOLD | BLOOMBERG DATA (VIA SHAFAQ): IRAQI DINAR DOWN 14.2% VS THE DOLLAR SINCE START-2026, 2ND WORST GLOBALLY AFTER THE LIBYAN DINAR (15.6%), AHEAD OF THE TURKISH LIRA (13.3%) | OFFICIAL RATE 152,000 SINCE OCT 7",
 beats=[
  ("البورصة", "البورصة: 169,500 صباح الخميس",
   "بورصتا الكفاح والحارثية سجلتا 169,500 دينار لكل 100 دولار صباح الخميس، مقابل 168,900 صباح الأربعاء (شفق نيوز).",
   "169,500", "IQD per $100 at Kifah/Harithiya bourses, Thursday morning (Shafaq)", "دينار لكل 100$ — البورصة",
   [("الأربعاء", "168,900"), ("الخميس", "169,500"), ("الفرق (محتسب)", "600")],
   ["البورصة 169,500", "الأربعاء 168,900", "لكل 100 دولار"]),
  ("الصيرفة", "الصيرفة ببغداد: البيع 170,000",
   "محال الصيرفة ببغداد باعت الـ100 دولار بـ170,000 دينار واشترتها بـ169,000 (شفق نيوز). وبحسب شبكة 964: البصرة 169,500 وأربيل 169,700.",
   "170,000", "IQD — Baghdad exchange-shop selling price per $100 (Shafaq, 964)", "دينار — البيع بالصيرفة",
   [("البيع", "170,000"), ("الشراء", "169,000"), ("الرسمي", "152,000")],
   ["الصيرفة 170,000", "الشراء 169,000", "الرسمي 152,000"]),
  ("بلومبرغ", "الدينار ثاني أكثر عملة تراجعاً بـ2026",
   "بيانات بلومبرغ عبر شفق نيوز: الدينار تراجع 14.2% أمام الدولار منذ مطلع 2026، بعد الدينار الليبي 15.6% وقبل الليرة التركية 13.3%.",
   "14.2%", "Iraqi dinar's fall vs the dollar since start-2026, 2nd worst globally (Bloomberg data via Shafaq)", "تراجع الدينار منذ مطلع 2026",
   [("الليبي", "15.6%"), ("العراقي", "14.2%"), ("التركية", "13.3%")],
   ["تراجع 14.2%", "الثاني عالمياً", "بيانات بلومبرغ"]),
 ],
 ticker=["بورصتا الكفاح والحارثية: 169,500 دينار لكل 100 دولار صباح الخميس (شفق نيوز)",
         "الصيرفة ببغداد: بيع 170,000 وشراء 169,000 (شفق نيوز)",
         "بلومبرغ: الدينار ثاني أكثر العملات تراجعاً أمام الدولار منذ مطلع 2026"],
 q="بكم اشتريت المية دولار آخر مرة؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بلومبرغ", "bloomberg.com"), ("شبكة 964", "964media.com"), ("المدى", "almadapaper.net")],
 brief=dict(kicker="الدولار اليوم", hook="المية دولار وصلت 170 ألف",
  vo="سجّلت بورصتا الكفاح والحارثية في بغداد، صباح الخميس، مئة وتسعة وستين ألفاً وخمسمئة دينار لكل مئة دولار، مقارنة مع مئة وثمانية وستين ألفاً وتسعمئة صباح الأربعاء، بحسب شفق نيوز. وفي محال الصيرفة ببغداد بلغ سعر البيع مئة وسبعين ألف دينار. وبحسب بيانات بلومبرغ التي أوردتها شفق نيوز، تراجع الدينار العراقي أربعة عشر فاصلة اثنين في المئة أمام الدولار منذ مطلع العام، ليحلّ ثانياً بين أكثر العملات تراجعاً، بعد تعديل السعر الرسمي إلى ألف وخمسمئة وعشرين ديناراً. بكم اشتريت المية دولار آخر مرة؟",
  pops=[{"value": "170,000", "label": "دينار لكل 100$ — بيع الصيرفة ببغداد", "matchWord": "الصيرفة"},
        {"value": "14.2%", "label": "تراجع الدينار منذ مطلع 2026 (بلومبرغ)", "matchWord": "بلومبرغ"}],
  srcline="المصادر: شفق نيوز · بلومبرغ · شبكة 964 · المدى — 22 تشرين الأول 2026"),
 caption=["سعر الدولار اليوم في بغداد.. الصيرفة تعبر حاجزاً جديداً",
          "البورصة، والصيرفة، وترتيب الدينار عالمياً حسب بلومبرغ. بالفيديو.",
          "بكم اشتريت المية دولار آخر مرة؟",
          "المصادر: شفق نيوز، بلومبرغ عبر شفق نيوز، شبكة 964، المدى (22 تشرين الأول 2026)",
          "#سعر_الدولار #الدينار_العراقي #العراق #photonectnews"])

# ---------------- C · Iran toman ----------------
S["c-toman-273700-iran"] = dict(
 bucket="mena_geo", variant="A", kicker="إيران",
 headline="الدولار بإيران يتجاوز 273 ألف تومان",
 sub="TEHRAN · OCT 22 (THU) | FREE-MARKET DOLLAR ~273,700 TOMAN, +3,900 (+1.45%) ON THE DAY (SHAFAQ); IRAN INTERNATIONAL: ABOVE 273,000, EURO ~307,000, GBP >366,000 | IRAN STATISTICAL CENTRE (VIA SHAFAQ): ANNUAL INFLATION 73.6% IN SEPTEMBER; CONSUMER PRICES +89.8% Y/Y | CENTRAL BANK OF IRAN SAID IN EARLY OCTOBER IT WOULD INJECT UP TO $2BN | IRAQ: ECONOMIST NABIL AL-MARSOUMI TELLS BAGHDAD TODAY DOLLAR DEMAND TO FINANCE TRADE WITH IRAN OUTSIDE OFFICIAL BANKING CHANNELS PRESSURES THE IRAQI MARKET; AFP (VIA BAGHDAD TODAY): IRAQ-IRAN TRADE VIA 7 CROSSINGS TOPPED $10BN LAST YEAR",
 beats=[
  ("السوق الحرة", "الدولار بإيران: نحو 273,700 تومان",
   "سعر بيع الدولار بالسوق الحرة في إيران بلغ نحو 273,700 تومان الخميس، بارتفاع 3,900 عن اليوم السابق (شفق نيوز). وإيران إنترناشيونال: فوق 273 ألفاً.",
   "273,700", "Toman per US dollar, Iran free market, Thursday (Shafaq)", "تومان لكل دولار",
   [("الارتفاع", "3,900"), ("النسبة", "1.45%"), ("اليورو", "307 ألف")],
   ["273,700 تومان", "+3,900 بيوم", "السوق الحرة"]),
  ("التضخم", "التضخم السنوي بإيران: 73.6%",
   "بيانات مركز الإحصاء الإيراني عبر شفق نيوز: التضخم السنوي 73.6% خلال أيلول، وأسعار المستهلكين أعلى بـ89.8% عن أيلول الماضي.",
   "73.6%", "Iran annual inflation, September (Iran Statistical Centre via Shafaq)", "التضخم السنوي — أيلول",
   [("التضخم", "73.6%"), ("الأسعار سنوياً", "89.8%"), ("ضخ المركزي", "ملياري $")],
   ["تضخم 73.6%", "الأسعار +89.8%", "مركز الإحصاء"]),
  ("العراق", "وبالعراق: دولار التجارة مع إيران",
   "الخبير نبيل المرسومي لبغداد اليوم: الطلب على الدولار لتمويل التجارة مع إيران خارج القنوات المصرفية الرسمية يضغط على السوق العراقية.",
   "$10B", "Iraq-Iran trade via 7 crossings last year (AFP via Baghdad Today)", "تبادل عبر 7 معابر العام الماضي",
   [("المعابر", "7"), ("التبادل", "+$10B"), ("المصدر", "فرانس برس")],
   ["دولار التجارة", "خارج المصارف", "ضغط على السوق"]),
 ],
 ticker=["الدولار في السوق الحرة الإيرانية نحو 273,700 تومان (شفق نيوز)",
         "إيران إنترناشيونال: الدولار يتجاوز 273 ألف تومان",
         "مركز الإحصاء الإيراني: تضخم سنوي 73.6% في أيلول"],
 q="سافرت لإيران هالسنة؟",
 sources=[("شفق نيوز", "shafaq.com"), ("إيران إنترناشيونال", "iranintl.com"), ("بغداد اليوم", "baghdadtoday.news")],
 brief=dict(kicker="إيران", hook="الدولار بإيران فوق 273 ألف تومان",
  vo="ارتفع سعر الدولار في السوق الحرة الإيرانية، يوم الخميس، إلى نحو مئتين وثلاثة وسبعين ألفاً وسبعمئة تومان، بزيادة ثلاثة آلاف وتسعمئة تومان عن اليوم السابق، بحسب شفق نيوز، فيما أفادت إيران إنترناشيونال بتجاوزه مئتين وثلاثة وسبعين ألفاً. وتُظهر بيانات مركز الإحصاء الإيراني تضخماً سنوياً بلغ ثلاثة وسبعين فاصلة ستة في المئة خلال أيلول. وفي العراق، يرى الخبير الاقتصادي نبيل المرسومي، بحسب بغداد اليوم، أن الطلب على الدولار لتمويل التجارة مع إيران خارج القنوات الرسمية يضغط على السوق المحلية. سافرت لإيران هالسنة؟",
  pops=[{"value": "273,700", "label": "تومان للدولار — السوق الحرة", "matchWord": "الإيرانية"},
        {"value": "73.6%", "label": "التضخم السنوي بإيران — أيلول", "matchWord": "تضخماً"}],
  srcline="المصادر: شفق نيوز · إيران إنترناشيونال · بغداد اليوم — 22 تشرين الأول 2026"),
 caption=["سعر الدولار في إيران اليوم بالتومان.. شنو صار؟",
          "رقم جديد، والتضخم، وشنو علاقة السوق العراقية. بالفيديو.",
          "سافرت لإيران هالسنة؟",
          "المصادر: شفق نيوز، إيران إنترناشيونال، بغداد اليوم (22 تشرين الأول 2026)",
          "#إيران #التومان #العراق #photonectnews"])

# ---------------- D · education: third round + no-fail year ----------------
S["d-no-fail-year-third-round"] = dict(
 bucket="iraq_services", variant="B", kicker="التربية",
 headline="دور ثالث للراسبين.. وسنة بلا رسوب",
 sub="BAGHDAD · OCT 22 (THU) | EDUCATION MINISTRY'S OPINION BOARD (STATEMENT VIA SHAFAQ, BAGHDAD TODAY, 964, AL-MADA): A THIRD EXAM ROUND FOR 6TH PRIMARY, 3RD INTERMEDIATE AND 6TH PREPARATORY (ALL BRANCHES), COVERING STUDENTS WHO FAILED ALL SUBJECTS — THE RECOMMENDATION GOES TO THE COUNCIL OF MINISTERS FOR FORMAL APPROVAL | SCHOOL YEAR 2025-2026 DECLARED A 'NO-FAIL YEAR' FOR ALL STAGES",
 beats=[
  ("الدور الثالث", "دور ثالث للمراحل المنتهية",
   "أقرت هيئة الرأي في وزارة التربية، الخميس، دوراً ثالثاً لطلبة السادس الابتدائي والثالث المتوسط والسادس الإعدادي، يشمل الراسبين في جميع المواد.",
   "3", "Graduating stages covered by the third exam round (Education Ministry)", "مراحل منتهية",
   [("الابتدائية", "السادس"), ("المتوسطة", "الثالث"), ("الإعدادية", "السادس")],
   ["الدور الثالث", "المراحل المنتهية", "الراسبون بكل المواد"]),
  ("الشرط", "بانتظار موافقة مجلس الوزراء",
   "بحسب بيان الوزارة، تُرفع توصية هيئة الرأي إلى مجلس الوزراء لاستحصال الموافقة الأصولية على إجراء الدور الثالث.",
   "مجلس الوزراء", "Third round still needs formal cabinet approval (Education Ministry)", "الموافقة الأصولية",
   [("القرار", "توصية"), ("الجهة", "مجلس الوزراء"), ("الحالة", "بانتظار")],
   ["توصية لمجلس الوزراء", "موافقة أصولية", "بعدها الدور الثالث"]),
  ("عدم الرسوب", "2025–2026 سنة عدم رسوب",
   "القرار الثاني: اعتبار العام الدراسي 2025–2026 سنة عدم رسوب لجميع المراحل الدراسية (شفق نيوز، بغداد اليوم، 964، المدى).",
   "2025–2026", "School year declared a no-fail year for all stages (Education Ministry)", "سنة عدم رسوب",
   [("العام", "2025–2026"), ("يشمل", "كل المراحل"), ("القرار", "عدم رسوب")],
   ["سنة عدم رسوب", "كل المراحل", "العام 2025–2026"]),
 ],
 ticker=["التربية: دور ثالث للسادس الابتدائي والثالث المتوسط والسادس الإعدادي (شفق نيوز، بغداد اليوم)",
         "الدور الثالث بانتظار موافقة مجلس الوزراء",
         "العام الدراسي 2025–2026 سنة عدم رسوب لجميع المراحل"],
 q="عندك طالب بمرحلة منتهية بالبيت؟",
 sources=[("وزارة التربية", "moedu.gov.iq"), ("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("شبكة 964", "964media.com"), ("المدى", "almadapaper.net")],
 brief=dict(kicker="التربية", hook="دور ثالث للراسبين.. وسنة بلا رسوب",
  vo="أقرّت هيئة الرأي في وزارة التربية، يوم الخميس، قرارين يخصان الطلبة، بحسب بيان الوزارة. الأول إجراء دور ثالث لطلبة السادس الابتدائي والثالث المتوسط والسادس الإعدادي بفروعه كافة، يشمل الراسبين في جميع المواد، على أن تُرفع التوصية إلى مجلس الوزراء لاستحصال الموافقة الأصولية على إجرائه. والثاني اعتبار العام الدراسي ألفين وخمسة وعشرين، ألفين وستة وعشرين، سنة عدم رسوب لجميع المراحل الدراسية. عندك طالب بمرحلة منتهية بالبيت؟",
  pops=[{"value": "الدور الثالث", "label": "للراسبين بجميع المواد", "matchWord": "الراسبين"},
        {"value": "2025–2026", "label": "سنة عدم رسوب لكل المراحل", "matchWord": "رسوب"}],
  srcline="المصادر: وزارة التربية · شفق نيوز · بغداد اليوم · شبكة 964 · المدى — 22 تشرين الأول 2026"),
 caption=["الدور الثالث وسنة عدم رسوب.. شنو قررت التربية العراقية؟",
          "منو يشمله القرار، وشنو الخطوة الباقية. بالفيديو.",
          "عندك طالب بمرحلة منتهية بالبيت؟",
          "المصادر: وزارة التربية عبر شفق نيوز، بغداد اليوم، شبكة 964، المدى (22 تشرين الأول 2026)",
          "#العراق #وزارة_التربية #الدور_الثالث #photonectnews"])

# ---------------- E · Artawi gas (V10.1 control, no brief) ----------------
S["e-artawi-gas-96-percent"] = dict(
 bucket="iraq_energy", variant="C", kicker="الكهرباء والغاز",
 headline="غاز أرطاوي وصل 96%.. وقود لمحطات الكهرباء",
 sub="BASRA · OCT 22 (THU) | OIL MINISTRY UNDERSECRETARY FOR GAS EZZAT SABER ISMAIL (VIA SHAFAQ, ECONOMY NEWS): ARTAWI FIELD EARLY GAS PROJECT (AG25) 96% COMPLETE; TARGETS 50 MILLION STANDARD CUBIC FEET OF RAW GAS TO PRODUCE OVER 40 MILLION OF DRY GAS, PRODUCTION 'SOON' | GAS MANAGEMENT PROJECT (GMP) 36% COMPLETE; PHASE 1 TARGETS 300 MILLION SCF OF RAW GAS FROM MAJNOON, WEST QURNA 2 AND ARTAWI, PHASE 2 OF SIMILAR SIZE | GOAL: CUT FLARING, BOOST FUEL FOR POWER STATIONS",
 beats=[
  ("أرطاوي", "مشروع غاز أرطاوي: إنجاز 96%",
   "وكيل وزارة النفط لشؤون الغاز عزت صابر إسماعيل أعلن الخميس وصول إنجاز مشروع غاز حقل أرطاوي المعجّل إلى 96% (شفق نيوز، الاقتصاد نيوز).",
   "96", "Percent complete — Artawi early gas project AG25 (Oil Ministry)", "% نسبة الإنجاز",
   [("الحقل", "أرطاوي"), ("الإنجاز", "96%"), ("الإنتاج", "قريباً")],
   ["أرطاوي 96%", "الغاز المصاحب", "الإنتاج قريباً"]),
  ("الكميات", "50 مليون قدم مكعب غاز خام",
   "بحسب الوكيل، يستهدف المشروع استثمار 50 مليون قدم مكعب قياسي من الغاز الخام لإنتاج أكثر من 40 مليوناً من الغاز الجاف.",
   "50", "Million standard cubic feet of raw gas targeted (Oil Ministry)", "مليون قدم مكعب — غاز خام",
   [("خام", "50 مليون"), ("جاف", "+40 مليون"), ("الهدف", "محطات الكهرباء")],
   ["50 مليون خام", "40 مليون جاف", "وقود المحطات"]),
  ("المعالجة", "مشروع معالجة الغاز: إنجاز 36%",
   "مشروع معالجة الغاز (GMP) بلغ إنجازه 36%، ويستهدف بمرحلته الأولى 300 مليون قدم مكعب قياسي من حقول مجنون وغرب القرنة 2 وأرطاوي.",
   "36", "Percent complete — Gas Management Project GMP (Oil Ministry)", "% إنجاز مشروع المعالجة",
   [("الإنجاز", "36%"), ("المرحلة 1", "300 مليون"), ("الحقول", "3")],
   ["معالجة الغاز 36%", "300 مليون قدم", "مجنون وغرب القرنة"]),
 ],
 ticker=["وزارة النفط: مشروع غاز حقل أرطاوي بلغ 96% (شفق نيوز، الاقتصاد نيوز)",
         "المشروع يستهدف 50 مليون قدم مكعب قياسي من الغاز الخام",
         "مشروع معالجة الغاز GMP بلغ 36%"],
 q="كم ساعة كهرباء توصلك اليوم؟",
 sources=[("وزارة النفط", "oil.gov.iq"), ("شفق نيوز", "shafaq.com"), ("الاقتصاد نيوز", "economy-news.net")],
 brief=None,
 caption=["غاز حقل أرطاوي بالبصرة.. شكد باقي على الإنتاج؟",
          "نسب الإنجاز، وكميات الغاز، وليش تهم محطات الكهرباء. بالفيديو.",
          "كم ساعة كهرباء توصلك اليوم؟",
          "المصادر: وزارة النفط عبر شفق نيوز والاقتصاد نيوز (22 تشرين الأول 2026)",
          "#العراق #الكهرباء #الغاز #photonectnews"])

for slug, s in S.items():
    full = f"{D}-{slug}"
    d = R / "data" / "posts" / full / ".meta"; d.mkdir(parents=True, exist_ok=True)
    props = {"dateLabel": DL, "arabicDateLabel": ADL, "handle": "@photonect.news",
             "audioBed": "audio/mood_newsroom.mp3", "topicBucket": s["bucket"], "variant": s["variant"],
             "breaking": {"arabicKicker": s["kicker"], "arabicHeadline": s["headline"], "englishSubhead": s["sub"],
                          "heroMedia": f"images/news/{full}/hero.jpg", "heroMediaType": "image"},
             "beats": [beat(slug, i + 1, *b) for i, b in enumerate(s["beats"])],
             "arabicTicker": s["ticker"] + [s["q"]], "endQuestion": s["q"],
             "sources": [{"name": n, "domain": dm} for n, dm in s["sources"]]}
    (d / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
    cap = s["caption"]
    (R / "data" / "posts" / full / "caption.txt").write_text(
        f"{cap[0]}\n\n{cap[1]}\n\n{cap[2]}\n\n{cap[3]}\n\n{cap[4]}\n@photonect.news\n", encoding="utf-8")
    if s["brief"]:
        b = s["brief"]
        brief = {"slug": full, "kicker": b["kicker"], "hookHeadline": b["hook"], "voText": b["vo"],
                 "endQuestion": s["q"], "sourcesLine": b["srcline"],
                 "images": [f"images/news/{full}/{f}" for f in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")],
                 "audioBed": "audio/mood_newsroom.mp3", "statPops": b["pops"]}
        (d / "v11-brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", full)
