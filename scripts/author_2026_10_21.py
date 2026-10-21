#!/usr/bin/env python3
"""Author the 2026-10-21 slate: props.json + caption.txt (+ v11-brief.json for a-d). e = silent V10.1 control."""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
D = "2026-10-21"
DL, ADL = "OCT 21 • 2026", "21 تشرين الأول 2026"

def beat(slug, n, label, h, body, bs_v, bs_en, bs_ar, pills, subs):
    img = f"images/news/{D}-{slug}/broll_{n}.jpg"
    return {"label": label, "arabicHeading": h, "arabicBody": body,
            "bigStat": {"value": bs_v, "label": bs_en, "arabicLabel": bs_ar},
            "supportingStats": [{"label": l, "value": v} for l, v in pills],
            "broll": img, "brolls": [img], "brollType": "image", "accent": "#FFC217",
            "brollSource": "صورة توضيحية", "subtitlePhrases": subs}

S = {}
S = {}
# ---------------- A · Anbar education: resigned employee's back pay (accused, not convicted) ----------------
S["a-anbar-resigned-salary-6-years"] = dict(
 bucket="iraq_corruption", variant="A", kicker="النزاهة",
 headline="مستقيل من 6 سنين.. ورواتبه انصرفت بأثر رجعي",
 sub="ANBAR · OCT 21 (WED) | FEDERAL INTEGRITY COMMISSION EXECUTES 4 ARREST WARRANTS AGAINST EMPLOYEES OF THE ANBAR EDUCATION DIRECTORATE (COMMISSION STATEMENT VIA SHAFAQ, BAGHDAD TODAY) | PER THE COMMISSION: THE FILE OF AN EMPLOYEE WHO RESIGNED 6 YEARS AGO WAS HIDDEN; A FORGED 'RESUMPTION OF WORK' LETTER AND A 'CONTINUITY OF SERVICE' LETTER SHOWED HIM BACK ON THE JOB, TO OBTAIN HIS SALARY AND DUES RETROACTIVELY | ARREARS PAID FOR 2020-2026; THE COMMISSION SAYS THE MONEY WAS RECOVERED (NO AMOUNT DISCLOSED) | RAMADI INTEGRITY INVESTIGATION JUDGE ORDERED THE SUSPECTS DETAINED UNDER PENAL CODE ARTICLES 289 AND 298 — ACCUSED, NOT CONVICTED",
 beats=[
  ("القبض", "النزاهة: 4 أوامر قبض بتربية الأنبار",
   "نفّذت هيئة النزاهة الاتحادية، الأربعاء، أربعة أوامر قبض بحق موظفين في مديرية تربية الأنبار (بيان الهيئة عبر شفق نيوز وبغداد اليوم).",
   "4", "Arrest warrants executed against Anbar Education employees, Wed (Integrity Commission)", "أوامر قبض",
   [("المديرية", "تربية الأنبار"), ("اليوم", "الأربعاء"), ("الصفة", "متهمون")],
   ["أربعة أوامر قبض", "مديرية تربية الأنبار", "بيان هيئة النزاهة"]),
  ("الوثائق", "مستقيل.. وعلى الورق رجع للدوام",
   "بحسب الهيئة، أُخفيت أوليات استقالة موظف مستقيل منذ 6 سنوات، وزُوّر كتاب مباشرة وكتاب استمرارية لإظهار عودته إلى الوظيفة.",
   "6", "Years since the employee resigned (Integrity Commission)", "سنوات على استقالته",
   [("الاستقالة", "قبل 6 سنوات"), ("الوثيقة", "كتاب مباشرة"), ("ومعه", "كتاب استمرارية")],
   ["مستقيل منذ ست سنوات", "كتاب مباشرة", "عودة على الورق"]),
  ("الفلوس", "فروقات 2020 - 2026.. والمبالغ استُعيدت",
   "تقول الهيئة إن فروقات مالية صُرفت عن المدة 2020 - 2026 واستُعيدت. وقاضي تحقيق النزاهة بالرمادي أوقف المتهمين وفق المادتين 289 و298.",
   "289", "Penal Code article cited for the detention, with article 298 (Integrity Commission)", "المادة من قانون العقوبات",
   [("المدة", "2020 - 2026"), ("المبالغ", "استُعيدت"), ("المواد", "289 و298")],
   ["فروقات من 2020", "المبالغ استُعيدت", "توقيف على ذمة التحقيق"]),
 ],
 ticker=["النزاهة: أربعة أوامر قبض بحق موظفين في تربية الأنبار (شفق نيوز، بغداد اليوم)",
         "بحسب الهيئة: وثائق مزوّرة أظهرت عودة موظف مستقيل منذ 6 سنوات",
         "الهيئة: استعادة المبالغ.. والمتهمون موقوفون على ذمة التحقيق"],
 q="تشتغل بدائرة حكومية؟",
 sources=[("هيئة النزاهة الاتحادية", "nazaha.iq"), ("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news")],
 brief=dict(kicker="النزاهة", hook="مستقيل من 6 سنين.. ورواتبه انصرفت",
  vo="نفّذت هيئة النزاهة الاتحادية، يوم الأربعاء، أربعة أوامر قبض بحق موظفين في مديرية تربية الأنبار. وبحسب بيان الهيئة، كشف مكتب تحقيق الأنبار إخفاء أوليات استقالة موظف مستقيل منذ ست سنوات، وتزوير كتاب مباشرة بالعمل وكتاب استمرارية في الخدمة لإظهار عودته إلى الوظيفة، بهدف الاستحواذ على رواتبه ومستحقاته بأثر رجعي لمصلحة المتهمين. وتقول الهيئة إن فروقات مالية صُرفت عن السنوات من ألفين وعشرين حتى ألفين وستة وعشرين، وإنها استعادت المبالغ، فيما قرر قاضي تحقيق النزاهة في الرمادي توقيف المتهمين. تشتغل بدائرة حكومية؟",
  pops=[{"value": "4", "label": "أوامر قبض — تربية الأنبار", "matchWord": "أربعة"},
        {"value": "6 سنوات", "label": "على استقالة الموظف", "matchWord": "مستقيل"}],
  srcline="المصادر: هيئة النزاهة الاتحادية · شفق نيوز · بغداد اليوم — 21 تشرين الأول 2026"),
 caption=["رواتب موظف مستقيل بتربية الأنبار.. شنو كشفت النزاهة؟",
          "وثائق، وست سنين، وأربعة أوامر قبض. القصة بالفيديو.",
          "تشتغل بدائرة حكومية؟",
          "المصادر: هيئة النزاهة عبر شفق نيوز وبغداد اليوم (21 تشرين الأول 2026)",
          "#العراق #الأنبار #هيئة_النزاهة #photonectnews"])

# ---------------- B · dollar ----------------
S["b-dollar-168900-near-170"] = dict(
 bucket="iraq_money", variant="B", kicker="الدولار اليوم",
 headline="المية دولار بالبورصة 168,900.. تقرب من 170 ألف",
 sub="BAGHDAD · OCT 21 (WED) | KIFAH AND HARITHIYA BOURSES 168,900 IQD PER $100 WEDNESDAY MORNING VS 168,250 TUESDAY MORNING (SHAFAQ); BAGHDAD TODAY: BOURSE OPENED AT 169,100 | BAGHDAD SHOPS SELL 169,500 / BUY 168,500; ERBIL SELL 168,900 / BUY 168,800 (SHAFAQ) | RAMADI: A TRADER TELLS SHAFAQ IMPORTERS WHO BOUGHT ON DEFERRED DOLLARS LOST UP TO 16% OF THEIR MONEY AFTER THE RATE CHANGE; SHOPS OFFERED FOR RENT | OFFICIAL RATE 152,000 SINCE OCT 7",
 beats=[
  ("البورصة", "البورصة: 168,900 صباح الأربعاء",
   "بورصتا الكفاح والحارثية سجلتا 168,900 دينار لكل 100 دولار صباح الأربعاء، مقابل 168,250 صباح الثلاثاء (شفق نيوز). وبغداد اليوم: الافتتاح على 169,100.",
   "168,900", "IQD per $100 at Kifah/Harithiya bourses, Wednesday morning (Shafaq)", "دينار لكل 100$ — البورصة",
   [("الثلاثاء", "168,250"), ("الأربعاء", "168,900"), ("الفرق (محتسب)", "650")],
   ["البورصة 168,900", "الثلاثاء 168,250", "لكل 100 دولار"]),
  ("الصيرفة", "بالصيرفة: البيع 169,500",
   "محال الصيرفة ببغداد باعت الـ100 دولار بـ169,500 دينار واشترتها بـ168,500. وفي أربيل البيع 168,900 والشراء 168,800 (شفق نيوز).",
   "169,500", "IQD — Baghdad exchange-shop selling price per $100 (Shafaq)", "دينار — سعر البيع بالصيرفة",
   [("البيع", "169,500"), ("الشراء", "168,500"), ("أربيل بيع", "168,900")],
   ["الصيرفة تبيع بـ169,500", "وتشتري بـ168,500", "أربيل 168,900"]),
  ("الرمادي", "بالرمادي: خسائر تجار لحد 16%",
   "صاحب مشروع تجاري بالرمادي قال لشفق نيوز إن مستوردين اشتروا بالدولار الآجل خسروا حتى 16% من أموالهم بعد تغيّر الصرف.",
   "16%", "Losses of up to 16% for importers who bought on deferred dollars — a Ramadi trader to Shafaq", "خسائر تجار بالرمادي",
   [("إيجار محل", "700 ألف"), ("المولدة", "150 ألف"), ("الرسمي", "152,000")],
   ["خسائر لحد 16%", "الدولار الآجل", "محال للإيجار"]),
 ],
 ticker=["بورصتا الكفاح والحارثية: 168,900 دينار لكل 100 دولار صباح الأربعاء (شفق نيوز)",
         "الصيرفة ببغداد: بيع 169,500 وشراء 168,500 (شفق نيوز)",
         "تاجر بالرمادي لشفق نيوز: خسائر لحد 16% بعد تغيّر الصرف"],
 q="شكد صرف المية دولار عندكم اليوم؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news")],
 brief=dict(kicker="الدولار اليوم", hook="المية دولار تقرب من 170 ألف",
  vo="سجّلت بورصتا الكفاح والحارثية في بغداد، صباح الأربعاء، مئة وثمانية وستين ألفاً وتسعمئة دينار لكل مئة دولار، مقارنة مع مئة وثمانية وستين ألفاً ومئتين وخمسين صباح الثلاثاء، بحسب شفق نيوز. وفي محال الصيرفة ببغداد بلغ سعر البيع مئة وتسعة وستين ألفاً وخمسمئة دينار، والسعر الرسمي للجمهور، بحسب البنك المركزي، ألف وخمسمئة وعشرون ديناراً للدولار. وفي الرمادي، قال صاحب مشروع تجاري لشفق نيوز إن مستوردين اشتروا بالدولار الآجل خسروا حتى ستة عشر في المئة من أموالهم بعد تغيّر الصرف. شكد صرف المية دولار عندكم اليوم؟",
  pops=[{"value": "168,900", "label": "دينار لكل 100$ — البورصة", "matchWord": "الكفاح"},
        {"value": "16%", "label": "خسائر تجار بالرمادي (تاجر لشفق)", "matchWord": "الآجل"}],
  srcline="المصادر: شفق نيوز · بغداد اليوم — 21 تشرين الأول 2026"),
 caption=["سعر الدولار اليوم في بغداد.. وتاجر بالرمادي يتحدث عن خسائر",
          "البورصة صباح الأربعاء مقارنة بصباح الثلاثاء، وسعر الصيرفة. الأرقام بالفيديو.",
          "شكد صرف المية دولار عندكم اليوم؟",
          "المصادر: شفق نيوز، بغداد اليوم (21 تشرين الأول 2026)",
          "#سعر_الدولار #الدينار_العراقي #العراق #photonectnews"])

# ---------------- C · Iran crossings ----------------
S["c-shib-closed-iran-crossings"] = dict(
 bucket="mena_economy", variant="A", kicker="العراق وإيران",
 headline="منفذ الشيب انغلق.. وفرانس برس: معابر إيران تنغلق تباعاً",
 sub="MAYSAN · OCT 21 (WED) | SHIB BORDER CROSSING WITH IRAN CLOSED FROM 6AM WEDNESDAY UNTIL FURTHER NOTICE ON FEDERAL GOVERNMENT ORDERS, PER A MAYSAN COUNCIL SOURCE (SHAFAQ) | IRAN INTERIOR MINISTRY SPOKESMAN ZEINIVAND: NO PRIOR NOTICE; UNDER THE BILATERAL AGREEMENT CLOSURES LONGER THAN ONE DAY MUST BE NOTIFIED (SHAFAQ) | BAGHDAD TODAY, CITING AFP: IRAQI GOVERNMENT SOURCES SAY CROSSINGS WILL CLOSE ONE BY ONE EXCEPT TWO; SOURCES TOLD REUTERS OF DIRECT US PRESSURE; TRADE ACROSS THE 7 CROSSINGS EXCEEDED $10BN LAST YEAR",
 beats=[
  ("الشيب", "الشيب مغلق حتى إشعار آخر",
   "أُغلق منفذ الشيب مع إيران في ميسان من السادسة صباح الأربعاء وحتى إشعار آخر، بأوامر الحكومة الاتحادية، بحسب مصدر في مجلس ميسان (شفق نيوز).",
   "6", "AM Wednesday — Shib crossing closed until further notice (Maysan council source via Shafaq)", "صباح الأربعاء — بدء الإغلاق",
   [("المنفذ", "الشيب"), ("المحافظة", "ميسان"), ("المدة", "حتى إشعار آخر")],
   ["منفذ الشيب", "حتى إشعار آخر", "بأوامر اتحادية"]),
  ("طهران", "طهران: ما بلّغونا مسبقاً",
   "المتحدث باسم الداخلية الإيرانية قال إن الإغلاق جرى بلا إشعار مسبق، وإن الاتفاق المشترك يوجب الإبلاغ إذا تجاوز الإغلاق يوماً واحداً (شفق نيوز).",
   "1", "Day — closures longer than this must be notified under the bilateral agreement, per Iran's interior ministry (Shafaq)", "يوم — حد الإبلاغ المسبق",
   [("المتحدث", "زيني وند"), ("الموقف", "استياء"), ("الملف", "قيد الدراسة")],
   ["بلا إشعار مسبق", "الداخلية الإيرانية", "أكثر من يوم"]),
  ("المعابر", "فرانس برس: معبران فقط يبقيان",
   "نقلت بغداد اليوم عن فرانس برس أن المعابر تُغلق تباعاً عدا اثنين، وعن مصادر لرويترز: بضغط أمريكي. وتبادل المعابر السبعة تجاوز 10 مليارات دولار العام الماضي.",
   "10", "Billion USD — Iraq-Iran trade across the 7 crossings last year (AFP via Baghdad Today)", "مليارات دولار تبادل العام الماضي",
   [("المعابر", "7"), ("تبقى مفتوحة", "2"), ("المصدر", "فرانس برس")],
   ["عدا معبرين", "ضغوط أمريكية بحسب مصادر", "10 مليارات دولار"]),
 ],
 ticker=["أُغلق منفذ الشيب مع إيران حتى إشعار آخر (شفق نيوز)",
         "الداخلية الإيرانية: لم نتلقَّ إشعاراً مسبقاً (شفق نيوز)",
         "بغداد اليوم عن فرانس برس: المعابر تُغلق تباعاً عدا اثنين"],
 q="تسافر لإيران براً؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("فرانس برس", "afp.com")],
 brief=dict(kicker="العراق وإيران", hook="منفذ الشيب مع إيران انغلق.. لحد متى؟",
  vo="أُغلق منفذ الشيب مع إيران في محافظة ميسان صباح الأربعاء حتى إشعار آخر. وكان مصدر في مجلس المحافظة قال لشفق نيوز مساء الثلاثاء إن أوامر اتحادية صدرت بالإغلاق لأمور فنية. وقال المتحدث باسم وزارة الداخلية الإيرانية إن طهران لم تتلقَّ إشعاراً مسبقاً بالقرار. ونقلت بغداد اليوم عن فرانس برس أن مصادر حكومية عراقية تحدثت عن إغلاق المعابر تباعاً باستثناء معبرين، ونقلت عن مصادر لرويترز أن الإغلاق جاء بضغوط أمريكية. وبحسب فرانس برس، تجاوز التبادل عبر المعابر السبعة، العام الماضي، عشرة مليارات دولار. تسافر لإيران براً؟",
  pops=[{"value": "2", "label": "معبران فقط يبقيان (فرانس برس)", "matchWord": "معبرين"},
        {"value": "+$10B", "label": "تبادل عبر المعابر العام الماضي (فرانس برس)", "matchWord": "مليارات"}],
  srcline="المصادر: شفق نيوز · بغداد اليوم · فرانس برس — 21 تشرين الأول 2026"),
 caption=["منفذ الشيب مع إيران مغلق.. شنو صار اليوم؟",
          "منفذ مغلق حتى إشعار آخر، وطهران تقول ما بلّغوها، وفرانس برس تتحدث عن معابر أخرى. التفاصيل بالفيديو.",
          "تسافر لإيران براً؟",
          "المصادر: شفق نيوز، بغداد اليوم، فرانس برس (21 تشرين الأول 2026)",
          "#العراق #إيران #منفذ_الشيب #photonectnews"])

# ---------------- D · solar customs zero + net metering ----------------
S["d-solar-zero-customs-bills"] = dict(
 bucket="iraq_economy", variant="B", kicker="الكهرباء",
 headline="صفر كمرك على المنظومات الشمسية.. وفاتورتك تنتظر تعليمات الربط",
 sub="BAGHDAD · OCT 21 (WED) | CABINET (TUE EVENING) ZEROES CUSTOMS DUTIES ON IMPORTED SOLAR ENERGY SYSTEMS TO SUPPORT THE PRIVATE SECTOR AND ENCOURAGE CITIZENS TO BUY THEM (SHAFAQ, BAGHDAD TODAY) | ELECTRICITY MINISTRY: DECISION FOLLOWS MINISTER ALI SAADI WAHEEB'S PROPOSAL OF 23 SEPT; A 40-ARTICLE DRAFT REGULATION WOULD LET CITIZENS CONNECT SOLAR SYSTEMS TO THE NATIONAL GRID WITH SMART METERS, CUTTING BILLS BY THE ENERGY EXCHANGED, ONCE APPROVED; DRAFT IS WITH THE STATE COUNCIL (BAGHDAD TODAY) | CABINET ALSO APPROVED A 600-1,000 MW POWER SUPPLY CONTRACT FOR THE NORTHERN REGION (SHAFAQ)",
 beats=[
  ("القرار", "صفر كمرك على منظومتك الشمسية",
   "مجلس الوزراء وافق مساء الثلاثاء على تصفير الرسوم الكمركية على منظومات الطاقة الشمسية المستوردة، دعماً للقطاع الخاص وتشجيعاً للمواطنين على اقتنائها (شفق نيوز، بغداد اليوم).",
   "0", "Customs duty on imported solar systems after Tuesday's cabinet decision (Shafaq, Baghdad Today)", "رسوم كمركية على المنظومات",
   [("القرار", "مجلس الوزراء"), ("اليوم", "الثلاثاء"), ("الهدف", "تشجيع الاقتناء")],
   ["تصفير الكمرك", "منظومات الطاقة الشمسية", "قرار مجلس الوزراء"]),
  ("الربط", "40 مادة لربط منظومتك بالشبكة الوطنية",
   "وزارة الكهرباء قالت إنها أعدّت مسودة تعليمات من 40 مادة تنظّم ربط المنظومات الشمسية بالشبكة الوطنية وتبادل الطاقة بين المواطن والشبكة (بغداد اليوم).",
   "40", "Articles in the draft grid-connection regulation (Electricity Ministry via Baghdad Today)", "مادة بمسودة التعليمات",
   [("المسودة", "40 مادة"), ("الجهة", "وزارة الكهرباء"), ("الآن", "لدى مجلس الدولة")],
   ["مسودة من 40 مادة", "ربط بالشبكة الوطنية", "تبادل الطاقة"]),
  ("الفاتورة", "فاتورة أقل؟ بعد إقرار التعليمات فقط",
   "بحسب الوزارة، ستتيح التعليمات بعد إقرارها الربط بمقاييس ذكية وخفض الفواتير وفق الطاقة المتبادلة، وإنها خاطبت مجلس الدولة لاستكمال صياغتها قبل رفعها لمجلس الوزراء.",
   "23", "September — date of the electricity minister's proposal behind the decision (ministry via Baghdad Today)", "أيلول — تاريخ مقترح الوزير",
   [("المقياس", "ذكي"), ("الفاتورة", "حسب التبادل"), ("المرحلة", "قبل الإقرار")],
   ["مقاييس ذكية", "فاتورة أقل بعد الإقرار", "مجلس الدولة"]),
 ],
 ticker=["مجلس الوزراء يصفّر الرسوم الكمركية على منظومات الطاقة الشمسية المستوردة (شفق نيوز، بغداد اليوم)",
         "الكهرباء: مسودة من 40 مادة لربط المنظومات بالشبكة الوطنية (بغداد اليوم)",
         "الوزارة: خفض الفواتير وفق الطاقة المتبادلة بعد إقرار التعليمات"],
 q="عندك منظومة شمسية بالبيت؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("وزارة الكهرباء", "moelc.gov.iq")],
 brief=dict(kicker="الكهرباء", hook="صفر كمرك على المنظومة الشمسية.. وفاتورتك تنتظر",
  vo="وافق مجلس الوزراء، مساء الثلاثاء، على تصفير الرسوم الكمركية المفروضة على منظومات الطاقة الشمسية المستوردة، دعماً للقطاع الخاص وتشجيعاً للمواطنين على اقتنائها، بحسب شفق نيوز وبغداد اليوم. وقالت وزارة الكهرباء إن القرار جاء بعد مقترح قدّمه الوزير علي سعدي وهيب في أيلول، وإنها أعدّت مسودة تعليمات من أربعين مادة لربط المنظومات بالشبكة الوطنية عبر مقاييس ذكية. وبحسب الوزارة، ستسهم التعليمات بعد إقرارها في خفض الفواتير وفق كميات الطاقة المتبادلة، وإنها خاطبت مجلس الدولة لاستكمال صياغتها القانونية قبل رفعها إلى مجلس الوزراء. عندك منظومة شمسية بالبيت؟",
  pops=[{"value": "صفر", "label": "كمرك على المنظومات الشمسية المستوردة", "matchWord": "تصفير"},
        {"value": "40", "label": "مادة بمسودة تعليمات الربط", "matchWord": "أربعين"}],
  srcline="المصادر: شفق نيوز · بغداد اليوم · وزارة الكهرباء — 21 تشرين الأول 2026"),
 caption=["الطاقة الشمسية في العراق بلا رسوم كمركية.. شنو يعني لفاتورتك؟",
          "قرار مجلس الوزراء، وخطة الكهرباء لربط البيوت بالشبكة، وشرط إقرار التعليمات قبل أي خفض بالفاتورة. بالفيديو.",
          "عندك منظومة شمسية بالبيت؟",
          "المصادر: شفق نيوز، بغداد اليوم (21 تشرين الأول 2026)",
          "#العراق #الطاقة_الشمسية #الكهرباء #photonectnews"])

# ---------------- E · domestic debt + reserves (V10.1 control, no brief) ----------------
S["e-debt-113-trillion-reserves"] = dict(
 bucket="iraq_money", variant="C", kicker="فلوس الدولة",
 headline="دين الدولة الداخلي زاد 25.4% بثمانية أشهر.. وصار 113.485 تريليون",
 sub="BAGHDAD · OCT 21 (WED) | CBI DATA (VIA SHAFAQ): DOMESTIC PUBLIC DEBT 113.485 TRILLION IQD AT END-AUGUST 2026 VS 109.516 AT END-JULY, +3.969 TRILLION IN ONE MONTH | +22.97 TRILLION (+25.4%) SINCE END-2025 (90.515) | COMPONENTS: FINANCE MINISTRY CLAIMS HELD BY THE CBI 76.499, LOANS 18.945, BONDS 9.330, TREASURY BILLS 8.711 | FOREIGN RESERVES $81.538BN END-AUGUST, UP $905M ON JULY ($80.633BN) BUT $15.894BN BELOW END-2025 ($97.432BN)",
 beats=[
  ("الدين", "دين الدولة الداخلي: 113.485 تريليون دينار",
   "بيانات البنك المركزي: الدين العام الداخلي بلغ 113.485 تريليون دينار بنهاية آب 2026، مقابل 109.516 تريليوناً بنهاية تموز (شفق نيوز).",
   "113.485", "Trillion IQD — domestic public debt, end-August 2026 (CBI data via Shafaq)", "تريليون دينار — الدين الداخلي",
   [("تموز", "109.516"), ("آب", "113.485"), ("بشهر واحد", "3.969")],
   ["113.485 تريليون", "نهاية آب", "زيادة بشهر واحد"]),
  ("الزيادة", "25.4% أكثر من نهاية 2025",
   "بنهاية 2025 كان الدين 90.515 تريليون دينار، أي زيادة 22.97 تريليوناً بنسبة 25.4% خلال ثمانية أشهر. ومطالبات البنك المركزي على وزارة المالية 76.499 تريليوناً (شفق نيوز).",
   "25.4", "Percent growth in domestic debt since end-2025 (CBI data via Shafaq)", "% زيادة خلال 8 أشهر",
   [("نهاية 2025", "90.515"), ("قروض", "18.945"), ("سندات", "9.330")],
   ["نهاية 2025", "+22.97 تريليون", "مطالبات المركزي"]),
  ("الاحتياطي", "الاحتياطي يرتفع بآب.. لكنه دون نهاية 2025",
   "الاحتياطيات الأجنبية ارتفعت بآب 905 ملايين دولار إلى 81.538 مليار، لكنها أقل بـ15.894 مليار من نهاية 2025 حين بلغت 97.432 مليار (شفق نيوز).",
   "81.538", "Billion USD — CBI foreign reserves, end-August 2026 (CBI data via Shafaq)", "مليار دولار — الاحتياطي الأجنبي",
   [("تموز", "80.633"), ("نهاية 2025", "97.432"), ("زيادة آب", "905 ملايين")],
   ["81.538 مليار", "+905 ملايين", "دون نهاية 2025"]),
 ],
 ticker=["البنك المركزي: الدين العام الداخلي 113.485 تريليون دينار بنهاية آب (شفق نيوز)",
         "زيادة 3.969 تريليون دينار خلال شهر واحد",
         "الاحتياطيات الأجنبية 81.538 مليار دولار بنهاية آب"],
 q="تعرف شكد دين العراق الداخلي قبل هالفيديو؟",
 sources=[("البنك المركزي العراقي", "cbi.iq"), ("شفق نيوز", "shafaq.com")],
 brief=None,
 caption=["الدين الداخلي للعراق.. شكد صار وشكد زاد بشهر واحد؟",
          "رقم آب الجديد من البنك المركزي، ووين وصل الاحتياطي الأجنبي. بالفيديو.",
          "تعرف شكد دين العراق الداخلي قبل هالفيديو؟",
          "المصادر: البنك المركزي العراقي عبر شفق نيوز (21 تشرين الأول 2026)",
          "#العراق #الدين_العام #البنك_المركزي_العراقي #photonectnews"])

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
