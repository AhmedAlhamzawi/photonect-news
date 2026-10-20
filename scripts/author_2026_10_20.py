#!/usr/bin/env python3
"""Author the 2026-10-20 slate: props.json + caption.txt (+ v11-brief.json for a-d). e = silent V10.1 control."""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
D = "2026-10-20"
DL, ADL = "OCT 20 • 2026", "20 تشرين الأول 2026"

def beat(slug, n, label, h, body, bs_v, bs_en, bs_ar, pills, subs):
    img = f"images/news/{D}-{slug}/broll_{n}.jpg"
    return {"label": label, "arabicHeading": h, "arabicBody": body,
            "bigStat": {"value": bs_v, "label": bs_en, "arabicLabel": bs_ar},
            "supportingStats": [{"label": l, "value": v} for l, v in pills],
            "broll": img, "brolls": [img], "brollType": "image", "accent": "#FFC217",
            "brollSource": "صورة توضيحية", "subtitlePhrases": subs}

S = {}
# ---------------- A · Maysan agricultural bank ex-director ----------------
S["a-maysan-bank-director-5-years"] = dict(
 bucket="iraq_money", variant="A", kicker="القضاء",
 headline="قروض خارج الضوابط.. 5 سنوات سجن لمدير مصرف سابق",
 sub="MAYSAN · OCT 20 (TUE) | MAYSAN CRIMINAL COURT SENTENCES THE FORMER DIRECTOR OF THE COOPERATIVE AGRICULTURAL BANK IN MAYSAN TO 5 YEARS AND 1 MONTH | PER THE SUPREME JUDICIAL COUNCIL: HE DISBURSED LOANS TO CITIZENS IN BREACH OF RULES, CAUSING WASTE OF PUBLIC MONEY; ARTICLE 315 PENAL CODE WITH COMPLICITY ARTICLES 47-49 (SHAFAQ, BAGHDAD TODAY) | SHAFAQ: IN AUG 2021 THE SAME COURT GAVE HIM 3 YEARS; HIS SENTENCES THEN TOTALLED 33 YEARS ACROSS 6 RULINGS FOR FORGERY AND EMBEZZLEMENT",
 beats=[
  ("الحكم", "جنايات ميسان: 5 سنوات وشهر",
   "حكمت محكمة جنايات ميسان، الثلاثاء، بالسجن خمس سنوات وشهراً على المدير الأسبق للمصرف الزراعي التعاوني في المحافظة (مجلس القضاء الأعلى).",
   "5", "Years (plus 1 month) in prison — Maysan Criminal Court, Tue (Supreme Judicial Council)", "سنوات وشهر سجن",
   [("المدة", "5 سنوات وشهر"), ("المحكمة", "جنايات ميسان"), ("اليوم", "الثلاثاء")],
   ["خمس سنوات وشهر", "مدير المصرف الزراعي الأسبق", "جنايات ميسان"]),
  ("التهمة", "قروض للمواطنين خلافاً للضوابط",
   "بحسب بيان القضاء، صرف المدان قروضاً للمواطنين خلافاً للضوابط والتعليمات، ما سبّب هدراً وضرراً بالمال العام (شفق نيوز، بغداد اليوم).",
   "315", "Penal Code article the ruling cites, with complicity articles 47-49 (judiciary statement)", "المادة من قانون العقوبات",
   [("المادة", "315"), ("الاشتراك", "47 - 49"), ("الضرر", "المال العام")],
   ["قروض خلافاً للضوابط", "هدر بالمال العام", "المادة 315"]),
  ("السوابق", "ليس الحكم الأول بحقه",
   "وفق شفق نيوز، حكمت المحكمة نفسها عليه في آب 2021 بالسجن 3 سنوات، وبلغت أحكامه حينها 6 مجموعها 33 سنة، بتهم تزوير واختلاس.",
   "33", "Years — total of his 6 earlier sentences as of Aug 2021, forgery and embezzlement (Shafaq)", "سنة مجموع أحكامه حتى 2021",
   [("آب 2021", "3 سنوات"), ("الأحكام", "6"), ("المجموع", "33 سنة")],
   ["آب 2021", "ستة أحكام", "33 سنة"]),
 ],
 ticker=["جنايات ميسان: السجن 5 سنوات وشهر للمدير الأسبق للمصرف الزراعي (مجلس القضاء الأعلى)",
         "التهمة: صرف قروض للمواطنين خلافاً للضوابط (شفق نيوز، بغداد اليوم)",
         "شفق نيوز: أحكامه حتى 2021 بلغت 33 سنة"],
 q="أخذت قرض من مصرف حكومي؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("مجلس القضاء الأعلى", "sjc.iq")],
 brief=dict(kicker="القضاء", hook="قروض خارج الضوابط.. 5 سنوات سجن لمدير مصرف سابق",
  vo="أصدرت محكمة جنايات ميسان، يوم الثلاثاء، حكماً بالسجن خمس سنوات وشهراً بحق المدير الأسبق للمصرف الزراعي التعاوني في المحافظة. وبحسب مجلس القضاء الأعلى، صرف المدان قروضاً مالية للمواطنين خلافاً للضوابط والتعليمات، ما تسبب بهدر وضرر بالمال العام، وصدر الحكم وفق المادة ثلاثمئة وخمس عشرة من قانون العقوبات. وتذكر شفق نيوز أن أحكامه السابقة بلغت، حتى عام ألفين وواحد وعشرين، ستة أحكام مجموعها ثلاث وثلاثون سنة، بتهم تزوير واختلاس. أخذت قرض من مصرف حكومي؟",
  pops=[{"value": "5 سنوات", "label": "وشهر — جنايات ميسان", "matchWord": "وشهراً"},
        {"value": "33", "label": "سنة — أحكامه حتى 2021 (شفق)", "matchWord": "وثلاثون"}],
  srcline="المصادر: مجلس القضاء الأعلى · شفق نيوز · بغداد اليوم — 20 تشرين الأول 2026"),
 caption=["محكمة ميسان تسجن مدير مصرف حكومي سابق.. شنو القصة؟",
          "قروض للمواطنين خارج الضوابط وحكم جديد اليوم. التفاصيل بالفيديو.",
          "أخذت قرض من مصرف حكومي؟",
          "المصادر: مجلس القضاء الأعلى، شفق نيوز، بغداد اليوم (20 تشرين الأول 2026)",
          "#العراق #ميسان #مكافحة_الفساد #photonectnews"])

# ---------------- B · dollar ----------------
S["b-dollar-168250-dip"] = dict(
 bucket="iraq_money", variant="B", kicker="الدولار اليوم",
 headline="الدولار ينزل شوية: المية بـ168,250 بالبورصة",
 sub="BAGHDAD · OCT 20 (TUE) | KIFAH AND HARITHIYA BOURSES 168,250 IQD PER $100 TUESDAY MORNING VS 168,600 MONDAY (SHAFAQ) | BAGHDAD SHOPS SELL 168,750 / BUY 167,750 (SHAFAQ, BAGHDAD TODAY); ERBIL SELL 168,050 / BUY 167,950 (SHAFAQ) | CBI (TUE): IMPORT TRANSFER REQUESTS HALTED BEFORE THE RATE CHANGE HAVE BEEN COMPLETED; TRADERS ASKED FOR EXTRA AMOUNTS SHOULD FILE A COMPLAINT | OFFICIAL RATE 152,000 (PUBLIC), 151,000 (BANKS)",
 beats=[
  ("البورصة", "البورصة: 168,250 صباح الثلاثاء",
   "بورصتا الكفاح والحارثية سجلتا 168,250 ديناراً لكل 100 دولار صباح الثلاثاء، مقابل 168,600 صباح الاثنين (شفق نيوز).",
   "168,250", "IQD per $100 at Kifah/Harithiya bourses, Tuesday morning (Shafaq)", "دينار لكل 100$ — البورصة",
   [("الاثنين", "168,600"), ("الثلاثاء", "168,250"), ("الفرق (محتسب)", "350")],
   ["البورصة 168,250", "الاثنين 168,600", "لكل 100 دولار"]),
  ("الصيرفة", "بالصيرفة: البيع 168,750",
   "محال الصيرفة ببغداد باعت الـ100 دولار بـ168,750 ديناراً واشترتها بـ167,750 (شفق نيوز، بغداد اليوم). وفي أربيل البيع 168,050.",
   "168,750", "IQD — Baghdad exchange-shop selling price per $100 (Shafaq, Baghdad Today)", "دينار — سعر البيع بالصيرفة",
   [("البيع", "168,750"), ("الشراء", "167,750"), ("أربيل بيع", "168,050")],
   ["الصيرفة تبيع بـ168,750", "وتشتري بـ167,750", "أربيل 168,050"]),
  ("المركزي", "المركزي: حوالات الاستيراد المتوقفة اكتملت",
   "البنك المركزي قال الثلاثاء إنه أكمل طلبات تحويل الاستيرادات المتوقفة قبل تعديل الصرف، ودعا التجار للشكوى إذا طولبوا بمبالغ إضافية (شفق نيوز).",
   "152,000", "IQD per $100 — official public selling rate since 7 Oct (CBI via Shafaq)", "دينار — السعر الرسمي لكل 100$",
   [("الرسمي", "152,000"), ("للمصارف", "151,000"), ("الصيرفة", "168,750")],
   ["حوالات الاستيراد اكتملت", "اشتكِ إذا طالبوك بالزيادة", "الرسمي 152 ألف"]),
 ],
 ticker=["بورصتا الكفاح والحارثية: 168,250 ديناراً لكل 100 دولار صباح الثلاثاء (شفق نيوز)",
         "الصيرفة ببغداد: بيع 168,750 وشراء 167,750 (شفق نيوز، بغداد اليوم)",
         "المركزي: اكتمال طلبات تحويل الاستيرادات المتوقفة (شفق نيوز)"],
 q="تشتري دولار هالأسبوع؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("البنك المركزي العراقي", "cbi.iq")],
 brief=dict(kicker="الدولار اليوم", hook="الدولار ينزل شوية.. المية بكم اليوم؟",
  vo="سجّلت بورصتا الكفاح والحارثية في بغداد، صباح الثلاثاء، مئة وثمانية وستين ألفاً ومئتين وخمسين ديناراً لكل مئة دولار، مقارنة بمئة وثمانية وستين ألفاً وستمئة صباح الاثنين، بحسب شفق نيوز. وفي محال الصيرفة بلغ سعر البيع مئة وثمانية وستين ألفاً وسبعمئة وخمسين، وفق شفق نيوز وبغداد اليوم. وفي اليوم نفسه، قال البنك المركزي إنه أكمل طلبات تحويل الاستيرادات المتوقفة، ودعا التجار إلى تقديم شكوى إذا طولبوا بمبالغ إضافية. تشتري دولار هالأسبوع؟",
  pops=[{"value": "168,250", "label": "دينار لكل 100$ — البورصة", "matchWord": "الكفاح"},
        {"value": "168,750", "label": "دينار — البيع بالصيرفة", "matchWord": "الصيرفة"}],
  srcline="المصادر: شفق نيوز · بغداد اليوم · البنك المركزي العراقي — 20 تشرين الأول 2026"),
 caption=["سعر الدولار في بغداد اليوم.. نزل لو صعد؟",
          "البورصة والصيرفة اليوم، وشنو قال البنك المركزي للتجار. بالفيديو.",
          "تشتري دولار هالأسبوع؟",
          "المصادر: شفق نيوز، بغداد اليوم (20 تشرين الأول 2026)",
          "#سعر_الدولار #الدينار_العراقي #العراق #photonectnews"])

# ---------------- C · Houthi claims + Brent ----------------
S["c-houthi-claims-brent-110"] = dict(
 bucket="mena_economy", variant="A", kicker="النفط والخليج",
 headline="الحوثيون يعلنون ضرب منشآت سعودية.. وبرنت فوق 110",
 sub="GULF · OCT 20 (TUE) | HOUTHIS SAY (MON) THEY STRUCK AN ARAMCO SITE IN YANBU, THE SHAYBAH OILFIELD, KING KHALID INTERNATIONAL AIRPORT (RIYADH) AND ABHA AIRPORT; NO SAUDI CONFIRMATION, REUTERS COULD NOT INDEPENDENTLY VERIFY (SHAFAQ, CITING REUTERS) | BRENT FUTURES +55C TO $110.10 TUESDAY AFTER $110.70 IN THE PREVIOUS SESSION, HIGHEST SINCE MAY 20; WTI NOV $103.91 (SHAFAQ, BAGHDAD TODAY) | KPLER: AT LEAST 18 SHIPS ATTACKED IN TWO WEEKS",
 beats=[
  ("الإعلان", "الحوثيون: استهدفنا منشآت طاقة ومطارين",
   "أعلنت جماعة الحوثي الاثنين استهداف موقع لأرامكو في ينبع وحقل الشيبة ومطاري الرياض وأبها. لا تأكيد سعودياً، ورويترز لم تتحقق (شفق نيوز).",
   "4", "Sites the Houthis say they struck: Yanbu (Aramco), Shaybah, King Khalid airport, Abha airport — unconfirmed (Shafaq/Reuters)", "مواقع بحسب إعلان الحوثيين",
   [("ينبع", "أرامكو"), ("الشيبة", "حقل نفط"), ("مطاران", "الرياض وأبها")],
   ["ينبع والشيبة", "مطارا الرياض وأبها", "لا تأكيد سعودياً"]),
  ("برنت", "برنت: 110.10 دولارات للبرميل",
   "صعد برنت الثلاثاء إلى 110.10 دولارات للبرميل، بعدما بلغ 110.70 في الجلسة السابقة، وهو الأعلى منذ 20 أيار (شفق نيوز، بغداد اليوم).",
   "110.10", "USD per barrel — Brent futures, Tuesday (Shafaq, Baghdad Today)", "دولار — برميل برنت",
   [("الجلسة السابقة", "110.70"), ("غرب تكساس", "103.91"), ("الأعلى منذ", "20 أيار")],
   ["برنت 110.10", "الأعلى منذ أيار", "غرب تكساس 103.91"]),
  ("السفن", "18 سفينة تعرضت لهجمات بأسبوعين",
   "بحسب شركة كبلر لتتبع السفن، تعرضت 18 سفينة على الأقل لهجمات خلال أسبوعين، ما أبقى علاوة المخاطر مرتفعة في أسواق النفط (شفق نيوز).",
   "18", "Ships attacked in two weeks, at least (Kpler, via Shafaq)", "سفينة تعرضت لهجمات خلال أسبوعين",
   [("المدة", "أسبوعان"), ("المصدر", "كبلر"), ("برنت", "110.10")],
   ["18 سفينة", "خلال أسبوعين", "بحسب كبلر"]),
 ],
 ticker=["الحوثيون يعلنون استهداف منشآت طاقة ومطارين في السعودية.. ولا تأكيد سعودياً (شفق نيوز)",
         "برنت 110.10 دولارات للبرميل الثلاثاء (شفق نيوز، بغداد اليوم)",
         "كبلر: 18 سفينة على الأقل تعرضت لهجمات خلال أسبوعين"],
 q="عندك عمرة أو سفرة للسعودية قريباً؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("رويترز", "reuters.com")],
 brief=dict(kicker="النفط والخليج", hook="منشآت سعودية بمرمى الحوثيين.. وبرنت فوق 110",
  vo="أعلنت جماعة الحوثي، يوم الاثنين، أنها استهدفت موقعاً لشركة أرامكو في ينبع، وحقل الشيبة النفطي، ومطار الملك خالد في الرياض، ومطار أبها. ولم يصدر تأكيد سعودي، ولم تتمكن رويترز من التحقق من ذلك، بحسب شفق نيوز. وصعد خام برنت يوم الثلاثاء إلى مئة وعشرة دولارات وعشرة سنتات للبرميل، بعدما سجل في الجلسة السابقة أعلى مستوى له منذ العشرين من أيار. وتقول شركة كبلر إن ثماني عشرة سفينة على الأقل تعرضت لهجمات خلال أسبوعين. عندك عمرة أو سفرة للسعودية قريباً؟",
  pops=[{"value": "$110.10", "label": "برميل برنت — الثلاثاء", "matchWord": "برنت"},
        {"value": "18", "label": "سفينة تعرضت لهجمات خلال أسبوعين", "matchWord": "كبلر"}],
  srcline="المصادر: شفق نيوز · بغداد اليوم · رويترز — 20 تشرين الأول 2026"),
 caption=["هجمات الحوثيين على السعودية وسعر النفط اليوم.. شنو صار؟",
          "منشآت ومطارات سعودية بإعلان الحوثيين، وبرنت عند أعلى مستوى من أيار. بالفيديو.",
          "عندك عمرة أو سفرة للسعودية قريباً؟",
          "المصادر: شفق نيوز، بغداد اليوم، رويترز (20 تشرين الأول 2026)",
          "#النفط #السعودية #الحوثيين #العراق #photonectnews"])

# ---------------- D · Rasheed loans ----------------
S["d-rasheed-loans-25-million"] = dict(
 bucket="iraq_money", variant="B", kicker="سلف الموظفين",
 headline="مصرف الرشيد: سلفة لحد 25 مليون وبدون كفيل",
 sub="BAGHDAD · OCT 20 (TUE) | STATE-OWNED RASHEED BANK ANNOUNCES LOANS AND ADVANCES PER AN OFFICIAL LETTER DATED OCT 19 (SHAFAQ, BAGHDAD TODAY) | EMPLOYEE ADVANCES IQD 5M-25M, 5 YEARS, 8% DECLINING ANNUAL INTEREST, NO GUARANTOR; CONTRACT STAFF UP TO 5M | RETIREES 5M-15M, SAME TERMS | MARRIAGE ADVANCE UP TO 10M; HOME-REPAIR LOANS UP TO 75M; VISA CREDIT CARD LIMIT UP TO 5M; UNIVERSITY ADVANCES 25M-50M | FINANCE MINISTER FALEH SARI (MON) DIRECTED RAFIDAIN TO LAUNCH EMPLOYEE LOANS",
 beats=[
  ("الموظفون", "موظف؟ من 5 إلى 25 مليون",
   "بحسب كتاب لمصرف الرشيد بتاريخ 19 تشرين الأول: سلف الموظفين من 5 إلى 25 مليون دينار، لخمس سنوات، بفائدة 8% متناقصة وبدون كفيل.",
   "25", "Million IQD — top employee advance, 5 years, 8% declining, no guarantor (Rasheed letter via Shafaq, Baghdad Today)", "مليون دينار — سقف سلف الموظفين",
   [("الفائدة", "8% متناقصة"), ("المدة", "5 سنوات"), ("العقود", "لحد 5 ملايين")],
   ["من 5 إلى 25 مليون", "فائدة 8% متناقصة", "بدون كفيل"]),
  ("المتقاعدون", "متقاعد؟ من 5 إلى 15 مليون",
   "سلف المتقاعدين من 5 إلى 15 مليون دينار بالشروط نفسها: خمس سنوات، وفائدة 8% متناقصة، وبدون كفيل (شفق نيوز، بغداد اليوم).",
   "15", "Million IQD — top retiree advance, same terms (Rasheed letter via Shafaq, Baghdad Today)", "مليون دينار — سقف سلف المتقاعدين",
   [("الحد الأدنى", "5 ملايين"), ("الفائدة", "8%"), ("الكفيل", "بدون")],
   ["المتقاعد من 5 إلى 15 مليون", "خمس سنوات", "بدون كفيل"]),
  ("غيرها", "سلفة زواج وقرض لترميم البيت",
   "القائمة تشمل سلفة زواج تصل إلى 10 ملايين، وقرض ترميم سكن حتى 75 مليوناً، وبطاقة فيزا بسقف 5 ملايين دينار (شفق نيوز، بغداد اليوم).",
   "75", "Million IQD — ceiling for home-repair loans (Rasheed letter via Shafaq, Baghdad Today)", "مليون دينار — سقف قرض الترميم",
   [("الزواج", "10 ملايين"), ("الفيزا", "5 ملايين"), ("الجامعية", "25 - 50 مليون")],
   ["سلفة زواج 10 ملايين", "ترميم لحد 75 مليون", "فيزا بسقف 5 ملايين"]),
 ],
 ticker=["مصرف الرشيد: سلف الموظفين من 5 إلى 25 مليون دينار بفائدة 8% متناقصة (شفق نيوز، بغداد اليوم)",
         "المتقاعدون من 5 إلى 15 مليوناً لخمس سنوات وبدون كفيل",
         "سلفة زواج لحد 10 ملايين وقرض ترميم لحد 75 مليوناً"],
 q="راح تقدّم على سلفة؟",
 sources=[("شفق نيوز", "shafaq.com"), ("بغداد اليوم", "baghdadtoday.news"), ("مصرف الرشيد", "rasheedbank.gov.iq")],
 brief=dict(kicker="سلف الموظفين", hook="سلفة لحد 25 مليون.. وبدون كفيل",
  vo="أعلن مصرف الرشيد الحكومي، يوم الثلاثاء، حزمة سلف وقروض، بحسب كتاب رسمي تلقته شفق نيوز وبغداد اليوم. سلف الموظفين تبدأ من خمسة ملايين وتصل إلى خمسة وعشرين مليون دينار، لمدة خمس سنوات، بفائدة ثمانية بالمئة متناقصة، ومن دون كفيل. وللمتقاعدين من خمسة إلى خمسة عشر مليوناً بالشروط نفسها. وتشمل القائمة أيضاً سلفة زواج تصل إلى عشرة ملايين، وقروضاً لترميم السكن حتى خمسة وسبعين مليوناً. راح تقدّم على سلفة؟",
  pops=[{"value": "25 مليون", "label": "دينار — سقف سلف الموظفين", "matchWord": "وعشرين"},
        {"value": "15 مليون", "label": "دينار — سقف سلف المتقاعدين", "matchWord": "وللمتقاعدين"}],
  srcline="المصادر: شفق نيوز · بغداد اليوم · مصرف الرشيد — 20 تشرين الأول 2026"),
 caption=["سلف مصرف الرشيد للموظفين والمتقاعدين 2026.. شكد المبلغ؟",
          "المبالغ والفائدة والمدة، وشلون الشروط للمتقاعد. كلها بالفيديو.",
          "راح تقدّم على سلفة؟",
          "المصادر: شفق نيوز، بغداد اليوم (20 تشرين الأول 2026)",
          "#سلف_الموظفين #مصرف_الرشيد #العراق #photonectnews"])

# ---------------- E · Global Hunger Index (V10.1 control, no brief) ----------------
S["e-hunger-index-iraq-61"] = dict(
 bucket="region_society", variant="C", kicker="مؤشر الجوع العالمي",
 headline="مؤشر الجوع 2026: العراق بالمرتبة 61 عالمياً",
 sub="GLOBAL · OCT 20 (TUE) | GLOBAL HUNGER INDEX 2026: IRAQ RANKS 61ST WITH A SCORE OF 11.9 ('MODERATE'), BETWEEN UKRAINE (60TH, 11.6) AND HONDURAS (62ND, 12.3) | IRAQ'S SCORE: 22.9 (2000), 17.2 (2012), 13.5 (2018), 11.9 (2026) | CHILD STUNTING DOWN FROM 28.0% (2000) TO 9.4% | REGION (WEST ASIA & NORTH AFRICA) 12.5, WORLD 18.1 | SAUDI 33RD, JORDAN & LEBANON 48TH, EGYPT 55TH; KUWAIT AND UAE BELOW 5 (GHI, SHAFAQ)",
 beats=[
  ("المرتبة", "العراق 61 عالمياً بـ11.9 نقطة",
   "حلّ العراق بالمرتبة 61 في مؤشر الجوع العالمي 2026 بـ11.9 نقطة، ضمن مستوى «معتدل»، بين أوكرانيا وهندوراس (موقع المؤشر، شفق نيوز).",
   "61", "Iraq's rank in the Global Hunger Index 2026, score 11.9, 'moderate' (GHI, Shafaq)", "مرتبة العراق عالمياً",
   [("النقاط", "11.9"), ("المستوى", "معتدل"), ("الدول المصنفة", "122")],
   ["المرتبة 61", "11.9 نقطة", "مستوى معتدل"]),
  ("التحسن", "من 22.9 نقطة إلى 11.9",
   "سجّل العراق 22.9 نقطة عام 2000، و17.2 عام 2012، و13.5 عام 2018. وتقزّم الأطفال دون الخامسة نزل من 28% إلى 9.4% (موقع المؤشر).",
   "9.4%", "Child stunting, under-fives, now — down from 28.0% in 2000 (GHI)", "تقزّم الأطفال دون الخامسة",
   [("2000", "22.9"), ("2018", "13.5"), ("2026", "11.9")],
   ["22.9 عام 2000", "11.9 عام 2026", "التقزم 9.4%"]),
  ("الجيران", "وين العراق من جيرانه؟",
   "السعودية بالمرتبة 33، والأردن ولبنان 48، ومصر 55، والكويت والإمارات دون 5 نقاط. ومعدل غرب آسيا وشمال أفريقيا 12.5 (المؤشر، شفق نيوز).",
   "12.5", "GHI score for West Asia & North Africa; world 18.1 (GHI)", "معدل المنطقة بالنقاط",
   [("السعودية", "33"), ("الأردن", "48"), ("مصر", "55")],
   ["السعودية 33", "الأردن 48 ومصر 55", "معدل المنطقة 12.5"]),
 ],
 ticker=["مؤشر الجوع العالمي 2026: العراق بالمرتبة 61 بـ11.9 نقطة (موقع المؤشر، شفق نيوز)",
         "نتيجة العراق: 22.9 عام 2000 و11.9 عام 2026",
         "تقزّم الأطفال دون الخامسة: من 28% إلى 9.4%"],
 q="بيتكم يستلم الحصة التموينية؟",
 sources=[("مؤشر الجوع العالمي", "globalhungerindex.org"), ("شفق نيوز", "shafaq.com")],
 brief=None,
 caption=["مؤشر الجوع العالمي 2026.. ترتيب العراق والدول العربية",
          "وين وصل العراق من عام 2000، ووين جيرانه. بالفيديو.",
          "بيتكم يستلم الحصة التموينية؟",
          "المصادر: مؤشر الجوع العالمي، شفق نيوز (20 تشرين الأول 2026)",
          "#العراق #مؤشر_الجوع_العالمي #الأمن_الغذائي #photonectnews"])

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
