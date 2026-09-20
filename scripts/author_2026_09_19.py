#!/usr/bin/env python3
"""2026-09-19 slate — 5 slugs. Every figure below is traced to a same-day dated article.
Sources: 964media 718138 (11:36), 718152 (12:32), 718150 (13:26), 718199 (15:42), 718210 (16:32);
Shafaq close report (13:17 UTC); mustaqila (19/9); baghdadtoday 302172 (25/6) for عقاري mechanics.
"""
import json, pathlib

D = "2026-09-19"
ROOT = pathlib.Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
IMG = "images/news"

def img(slug, f):
    return f"{IMG}/{D}-{slug}/{f}"

SLATE = {}

# ---------------------------------------------------------------- A · corruption
s = "a-najaf-electricity-graft"
SLATE[s] = dict(
    topicBucket="iraq_corruption", variant="A", accent="#D72638",
    kicker="نزاهة",
    headline="تدفع فاتورة الكهرباء.. وين تروح فلوسك؟",
    subhead=("NAJAF · SEP 19 | 964 (12:32): FEDERAL INTEGRITY COMMISSION DETAINS TWO AT NAJAF ELECTRICITY "
             "DISTRIBUTION DIRECTORATE — AN EMPLOYEE AND A COLLECTOR (جابٍ) | ACCUSED OF TAKING MONEY FROM "
             "CITIZENS WITHOUT DEPOSITING IT TO THE TREASURY AND USING A FORGED STAMP ON COLLECTION RECEIPTS "
             "| COMMISSION FILED A SEIZURE REPORT; COURT ORDERED DETENTION PENDING INVESTIGATION — "
             "ACCUSATION ONLY, NO CONVICTION ISSUED | NO SUM DISCLOSED"),
    endQuestion="دفعت فلوس لجابي الكهرباء بوصل بدون ختم رسمي؟",
    ticker=[
        "هيئة النزاهة الاتحادية: ضبط موظف وجابٍ في دائرة توزيع كهرباء النجف (شبكة 964 — 19 أيلول)",
        "الاتهام: استحصال أموال من المواطنين دون إيداعها في الخزينة العامة",
        "الهيئة: استُخدم ختم مزوّر على وصولات القبض لإيهام المواطنين بقانونية الاستيفاء",
        "القضاء قرر توقيفهما على ذمة التحقيق — لم تصدر إدانة حتى الآن",
    ],
    beats=[
        dict(label="الضبط",
             heading="النزاهة تطيح بموظف وجابٍ بكهرباء النجف",
             body="هيئة النزاهة الاتحادية أعلنت ضبط موظف في دائرة توزيع كهرباء النجف وجابٍ يعمل معه، بتهمة استحصال أموال من المواطنين دون إيداعها في الخزينة العامة (شبكة 964).",
             stat=("2", "Detained at Najaf electricity distribution directorate, per the Federal Integrity Commission",
                   "موقوفان في دائرة توزيع كهرباء النجف بحسب هيئة النزاهة الاتحادية"),
             sup=[("الموقوفون", "2"), ("الجهة", "النزاهة"), ("الدائرة", "كهرباء النجف")],
             phrases=["النزاهة تطيح بموظفين", "في كهرباء النجف", "أموال ما وصلت الخزينة"]),
        dict(label="الطريقة",
             heading="ختم مزوّر على وصل القبض",
             body="بحسب بيان الهيئة، استُخدم ختم مزوّر على وصولات القبض لإيهام المواطنين بأن الاستيفاء قانوني، وكان الجابي يزوّد الموظف بالوصولات المستخدمة.",
             stat=("1", "Forged stamp used on collection receipts to make the charge look official, per the Commission",
                   "ختم مزوّر واحد استُخدم على وصولات القبض لإيهام المواطنين بقانونية الاستيفاء (بيان الهيئة)"),
             sup=[("الأداة", "ختم مزوّر"), ("المستند", "وصل قبض"), ("الوجهة", "خارج الخزينة")],
             phrases=["ختم مزوّر", "على وصل القبض", "حتى يبين قانوني"]),
        dict(label="القضاء",
             heading="توقيف على ذمة التحقيق.. لا إدانة",
             body="الهيئة نظّمت محضر ضبط أصولياً وعرضته على القضاء الذي قرر توقيفهما على ذمة التحقيق. ولم تصدر إدانة بحق أي منهما حتى الآن، ولم يُعلن المبلغ المستحصل.",
             stat=("0", "Convictions issued so far — the court ordered detention pending investigation only",
                   "إدانة صدرت حتى الآن — القرار توقيف على ذمة التحقيق فقط، والمبلغ لم يُعلن"),
             sup=[("القرار", "توقيف"), ("الإدانات", "0"), ("المبلغ", "لم يُعلن")],
             phrases=["القضاء قرر التوقيف", "على ذمة التحقيق", "بعدها ماكو إدانة"]),
    ],
    sources=[("شبكة 964", "964media.com"), ("هيئة النزاهة الاتحادية", "nazaha.iq")],
    sourcesLine="المصادر: شبكة 964 · هيئة النزاهة الاتحادية — 19 أيلول 2026",
    hookHeadline="فاتورة كهرباء.. بختم مزوّر",
    voText=("أعلنت هيئة النزاهة الاتحادية ضبط موظف وجابٍ في دائرة توزيع كهرباء النجف، بحسب ما نقلته شبكة تسعمئة وأربعة وستين اليوم السبت. "
            "والتهمة أنهما استحصلا أموالاً من المواطنين دون إيداعها في الخزينة العامة، وأن ختماً مزوّراً استُخدم على وصولات القبض لإيهام المواطنين بأن الاستيفاء قانوني. "
            "وتقول الهيئة إنها نظّمت محضر ضبط أصولياً وعرضته على القضاء، الذي قرر توقيفهما على ذمة التحقيق. "
            "ولم تصدر إدانة بحق أي منهما حتى الآن، ولم يُعلن المبلغ. دفعت فلوس لجابي الكهرباء بوصل بدون ختم رسمي؟"),
    pops=[("2", "موقوفان في كهرباء النجف", "ضبط"), ("0", "إدانة صدرت حتى الآن", "إدانة")],
)

# ---------------------------------------------------------------- B · dollar anchor
s = "b-dollar-160250-baghdad"
SLATE[s] = dict(
    topicBucket="iraq_money", variant="B", accent="#FFC217",
    kicker="الدولار اليوم",
    headline="الدولار كسر 160 ألف.. والرسمي بعده 131",
    subhead=("BAGHDAD · SEP 19 | 964 (11:36): BAGHDAD EXCHANGE SHOPS SELL 160,250 / BUY 159,250 PER $100; "
             "ERBIL SELL 159,450 / BUY 159,000; BASRA SELL 159,500 / BUY 159,000; CBI OFFICIAL RATE 131,000 | "
             "SHAFAQ (CLOSE): KIFAH & HARITHIYA BOURSES CLOSED 159,750; BAGHDAD SHOPS SELL 160,250 / BUY 159,250; "
             "ERBIL CLOSE SELL 159,400 / BUY 159,300 | VS OUR SEP 17 POST: BAGHDAD SHOPS SELL WAS 159,250 "
             "(+1,000 SHOP-SELL TO SHOP-SELL, MORNING TO MORNING, COMPUTED) | GAP TO OFFICIAL 29,250 (COMPUTED)"),
    endQuestion="بكم بعت أو اشتريت الدولار اليوم؟",
    ticker=[
        "محال الصيرفة ببغداد: البيع 160,250 والشراء 159,250 لكل 100 دولار (شبكة 964 — 19 أيلول)",
        "أربيل: البيع 159,450 والشراء 159,000 — البصرة: البيع 159,500 والشراء 159,000 (شبكة 964)",
        "إغلاق بورصتي الكفاح والحارثية 159,750 ديناراً لكل 100 دولار (شفق نيوز)",
        "السعر الرسمي المقرر من البنك المركزي 131,000 دينار لكل 100 دولار",
    ],
    beats=[
        dict(label="بغداد",
             heading="محال بغداد تبيع المية بـ160,250",
             body="محال الصيرفة في بغداد باعت 100 دولار بـ160,250 ديناراً واشترت بـ159,250 (شبكة 964). وفي منشورنا يوم الخميس كان سعر البيع 159,250 — أي أعلى بألف دينار.",
             stat=("160,250", "Selling price per $100 at Baghdad exchange shops, Saturday, per 964",
                   "دينار سعر بيع كل 100 دولار في محال الصيرفة ببغداد السبت (شبكة 964)"),
             sup=[("الخميس", "159,250"), ("اليوم", "160,250"), ("الفرق", "+1,000")],
             phrases=["محال بغداد", "تبيع المية بـ160,250", "أعلى بألف عن الخميس"]),
        dict(label="المدن",
             heading="أربيل 159,450 والبصرة 159,500",
             body="في أربيل البيع 159,450 والشراء 159,000، وفي البصرة البيع 159,500 والشراء 159,000 (شبكة 964). وبورصتا الكفاح والحارثية أغلقتا على 159,750 (شفق نيوز).",
             stat=("159,750", "Closing rate at Baghdad's Kifah and Harithiya bourses per $100, per Shafaq",
                   "دينار إغلاق بورصتي الكفاح والحارثية لكل 100 دولار (شفق نيوز)"),
             sup=[("أربيل", "159,450"), ("البصرة", "159,500"), ("الإغلاق", "159,750")],
             phrases=["أربيل 159,450", "والبصرة 159,500", "والإغلاق 159,750"]),
        dict(label="الفجوة",
             heading="الرسمي 131 ألف.. والفرق 29,250",
             body="السعر الرسمي المقرر من البنك المركزي 131,000 دينار لكل 100 دولار. الفرق بينه وبين سعر البيع ببغداد 29,250 ديناراً على كل 100 دولار — محتسب من رقمَي 964.",
             stat=("29,250", "Dinars between the official 131,000 and Baghdad's 160,250 shop-sell per $100 — computed from 964's own two figures",
                   "دينار فرق بين السعر الرسمي 131,000 وسعر البيع ببغداد 160,250 لكل 100 دولار (محتسب من رقمَي شبكة 964)"),
             sup=[("الرسمي", "131,000"), ("السوق", "160,250"), ("الفرق", "29,250")],
             phrases=["الرسمي 131 ألف", "والسوق 160,250", "الفرق 29,250"]),
    ],
    sources=[("شبكة 964", "964media.com"), ("شفق نيوز", "shafaq.com")],
    sourcesLine="المصادر: شبكة 964 · شفق نيوز — 19 أيلول 2026",
    hookHeadline="الدولار كسر المية وستين",
    voText=("كسر الدولار حاجز مئة وستين ألف دينار في بغداد اليوم السبت. "
            "فبحسب شبكة تسعمئة وأربعة وستين، باعت محال الصيرفة في بغداد كل مئة دولار بمئة وستين ألفاً ومئتين وخمسين ديناراً، واشترتها بمئة وتسعة وخمسين ألفاً ومئتين وخمسين. "
            "وفي أربيل بلغ البيع مئة وتسعة وخمسين ألفاً وأربعمئة وخمسين، وفي البصرة مئة وتسعة وخمسين ألفاً وخمسمئة. "
            "أما بورصتا الكفاح والحارثية فأغلقتا عند مئة وتسعة وخمسين ألفاً وسبعمئة وخمسين، بحسب شفق نيوز. "
            "والسعر الرسمي المقرر من البنك المركزي ما زال مئة وواحداً وثلاثين ألفاً. بكم بعت أو اشتريت الدولار اليوم؟"),
    pops=[("160,250", "بيع المية دولار بمحال بغداد", "الصيرفة"), ("131,000", "السعر الرسمي للبنك المركزي", "الرسمي")],
)

# ---------------------------------------------------------------- C · property platform
s = "c-aqari-platform-kirkuk"
SLATE[s] = dict(
    topicBucket="iraq_money", variant="A", accent="#2b2b2b",
    kicker="عقارات",
    headline="تبيع بيتك؟ منو يشوف بياناتك؟",
    subhead=("KIRKUK · SEP 19 | 964 (13:26): REAL-ESTATE OFFICE OWNERS IN KIRKUK PROTESTED SATURDAY AGAINST "
             "THE «عقاري» PROPERTY PLATFORM — THEY SAY IT IS UNSAFE AND LETS COMPANIES REACH BUYERS' AND SELLERS' "
             "PERSONAL DATA, AND THAT THE APP IS TOO COMPLEX: «تطبيق معقد والمواطن هو المتضرر الأول» | NO OFFICIAL "
             "NAMED IN THE REPORT; NO GOVERNMENT RESPONSE PUBLISHED | BAGHDAD TODAY (JUN 25): PLATFORM APPLIES FROM "
             "JUL 1 2026, SALE/PURCHASE NEEDS AN ELECTRONIC LETTER VIA LICENSED OFFICES INCLUDING PROPERTY DETAILS "
             "AND SOURCE OF FUNDS, AHEAD OF TITLE TRANSFER AT REAL-ESTATE REGISTRATION DIRECTORATES"),
    endQuestion="سويت معاملة عقار بعد تموز؟ كم يوم أخذت؟",
    ticker=[
        "أصحاب مكاتب عقارية في كركوك تظاهروا السبت ضد منصة «عقاري» (شبكة 964 — 19 أيلول)",
        "المتظاهرون: المنصة غير آمنة وتتيح للشركات الوصول إلى البيانات الشخصية للمشترين والبائعين",
        "من تصريحاتهم: «تطبيق معقد والمواطن هو المتضرر الأول» — ولم يرد في التقرير رد حكومي",
        "المنصة مطبّقة منذ 1 تموز 2026 وتشترط مكاتبة إلكترونية عبر مكاتب معتمدة تتضمن مصدر الأموال (بغداد اليوم)",
    ],
    beats=[
        dict(label="التظاهرة",
             heading="مكاتب كركوك تتظاهر ضد «عقاري»",
             body="أصحاب مكاتب عقارية في كركوك خرجوا بتظاهرة السبت ضد منصة «عقاري» الإلكترونية المخصصة لمعاملات بيع وشراء العقارات (شبكة 964).",
             stat=("1", "Protest staged Saturday by Kirkuk real-estate office owners against the «عقاري» platform, per 964",
                   "تظاهرة لأصحاب المكاتب العقارية في كركوك السبت ضد منصة «عقاري» (شبكة 964)"),
             sup=[("المكان", "كركوك"), ("اليوم", "السبت"), ("الجهة", "مكاتب عقارية")],
             phrases=["مكاتب كركوك", "تتظاهر ضد عقاري", "منصة بيع العقارات"]),
        dict(label="الاتهام",
             heading="«غير آمنة».. وبيانات المشتري مكشوفة",
             body="المتظاهرون قالوا إن المنصة غير آمنة وتتيح للشركات الوصول إلى البيانات الشخصية للمشترين والبائعين، ووصفوها بأنها «تطبيق معقد والمواطن هو المتضرر الأول». ولم يرد في التقرير رد حكومي على هذه الاتهامات.",
             stat=("2", "Groups whose personal data the protesters say is exposed — buyers and sellers (their claim; no official response in the report)",
                   "طرفان تقول التظاهرة إن بياناتهما مكشوفة: المشتري والبائع — وهو اتهام المتظاهرين، ولم يُنشر رد حكومي"),
             sup=[("الادعاء", "غير آمنة"), ("المكشوف", "بيانات شخصية"), ("رد حكومي", "لم يُنشر")],
             phrases=["يقولون غير آمنة", "بيانات المشتري والبائع", "وماكو رد حكومي"]),
        dict(label="الإلزام",
             heading="إلزامية من 1 تموز.. وتسأل عن مصدر الفلوس",
             body="المنصة مطبّقة منذ الأول من تموز 2026، وإكمال البيع والشراء يتطلب مكاتبة إلكترونية عبر مكاتب معتمدة تتضمن بيانات العقار ومصدر الأموال المستخدمة في الشراء، قبل نقل الملكية في دوائر التسجيل العقاري (بغداد اليوم).",
             stat=("1 تموز", "Date the electronic property platform became the required route for sales, per Baghdad Today",
                   "تموز 2026 تاريخ صيرورة المنصة الإلكترونية الطريق المطلوب لإتمام البيع والشراء (بغداد اليوم)"),
             sup=[("التطبيق", "1 تموز"), ("المطلوب", "مكاتبة إلكترونية"), ("يُسأل عن", "مصدر الأموال")],
             phrases=["إلزامية من تموز", "مكاتبة إلكترونية", "ويسألون مصدر الفلوس"]),
    ],
    sources=[("شبكة 964", "964media.com"), ("بغداد اليوم", "baghdadtoday.news")],
    sourcesLine="المصادر: شبكة 964 · بغداد اليوم — 19 أيلول 2026",
    hookHeadline="بيانات بيتك.. بيد منو؟",
    voText=("تظاهر أصحاب مكاتب عقارية في كركوك اليوم السبت ضد منصة «عقاري» الإلكترونية، بحسب شبكة تسعمئة وأربعة وستين. "
            "ويقول المتظاهرون إن المنصة غير آمنة، وإنها تتيح للشركات الوصول إلى البيانات الشخصية للمشترين والبائعين، ويصفونها بأنها تطبيق معقد وأن المواطن هو المتضرر الأول. "
            "وهذه اتهامات المتظاهرين، ولم يرد في التقرير رد حكومي عليها. "
            "والمنصة مطبّقة منذ الأول من تموز، وإكمال البيع والشراء يتطلب مكاتبة إلكترونية عبر مكاتب معتمدة تتضمن بيانات العقار ومصدر الأموال، قبل نقل الملكية. "
            "سويت معاملة عقار بعد تموز؟ كم يوم أخذت؟"),
    pops=[("1 تموز", "بداية العمل الإلزامي بالمنصة", "تموز"), ("2", "طرفان: المشتري والبائع", "والبائعين")],
)

# ---------------------------------------------------------------- D · CBI answer
s = "d-cbi-reserves-speculation"
SLATE[s] = dict(
    topicBucket="iraq_money", variant="B", accent="#FFC217",
    kicker="المركزي",
    headline="المركزي: الاحتياطي كافٍ.. والسبب مضاربات",
    subhead=("BAGHDAD · SEP 19 | 964 (16:32): CENTRAL BANK OF IRAQ STATEMENT — RESERVES ARE «كفاية» TO MEET FOREIGN-"
             "CURRENCY DEMAND AT THE OFFICIAL RATE FOR FOREIGN-TRADE FINANCE, BANK CARDS AND TRAVELLERS; ATTRIBUTES "
             "THE DOLLAR'S RISE TO «المضاربات في الأسواق والتوقعات وسوء استخدام الظروف الجيوسياسية» | NO RESERVE FIGURE "
             "GIVEN IN THE STATEMENT | MUSTAQILA (SEP 19): «ECO IRAQ» OBSERVATORY SAYS THE RISE IS «مجموعة عوامل متداخلة "
             "لا يمكن اختزالها بسبب واحد» INCLUDING ANXIETY OVER WHAT FOLLOWS SEP 30; PM'S FINANCIAL ADVISER DENIED ANY "
             "ANNOUNCED US PLAN TO HALT DOLLAR SHIPMENTS | 964 (718166): COMMANDER-IN-CHIEF'S SPOKESMAN ON SEP 30 — "
             "«تسقط أي مبرر للتحرك خارج سلطة الدولة»"),
    endQuestion="تصدّق سبب الغلاء مضاربة لو شي ثاني؟",
    ticker=[
        "بيان البنك المركزي العراقي: لدينا كفاية من الاحتياطيات الأجنبية لتلبية الطلب بالسعر الرسمي (شبكة 964 — 19 أيلول)",
        "المركزي يعزو الارتفاع إلى «المضاربات في الأسواق والتوقعات وسوء استخدام الظروف الجيوسياسية»",
        "البيان لم يذكر رقماً للاحتياطيات — والتمويل يشمل التجارة الخارجية وبطاقات المصارف وطلبات المسافرين",
        "مرصد «إيكو عراق»: الارتفاع «مجموعة عوامل متداخلة لا يمكن اختزالها بسبب واحد» (وكالة الصحافة المستقلة)",
    ],
    beats=[
        dict(label="البيان",
             heading="المركزي: الاحتياطي يكفي الطلب",
             body="البنك المركزي العراقي قال في بيان إن لديه كفاية من الاحتياطيات الأجنبية لتلبية الطلبات على العملة بالسعر الرسمي، لتمويل التجارة الخارجية وبطاقات المصارف وطلبات المسافرين (شبكة 964).",
             stat=("3", "Channels the CBI says it covers at the official rate: foreign trade, bank cards, travellers",
                   "قنوات يقول المركزي إنه يغطيها بالسعر الرسمي: التجارة الخارجية وبطاقات المصارف وطلبات المسافرين"),
             sup=[("الجهة", "المركزي"), ("الموقف", "الاحتياطي كافٍ"), ("الرقم", "لم يُذكر")],
             phrases=["المركزي يقول", "الاحتياطي يكفي الطلب", "بالسعر الرسمي"]),
        dict(label="التفسير",
             heading="السبب بنظره: مضاربات وتوقعات",
             body="البيان عزا ارتفاع الدولار إلى «المضاربات في الأسواق والتوقعات وسوء استخدام الظروف الجيوسياسية» من جهات تسعى لإرباك الوضع الاقتصادي. ولم يورد البيان أي رقم للاحتياطيات.",
             stat=("0", "Reserve figures disclosed in the statement — the CBI gave no number",
                   "رقم للاحتياطيات ورد في البيان — المركزي لم يذكر أي مبلغ"),
             sup=[("مضاربات", "نعم"), ("توقعات", "نعم"), ("رقم معلن", "0")],
             phrases=["يقول مضاربات وتوقعات", "وظروف جيوسياسية", "بس بلا رقم"]),
        dict(label="الرواية الثانية",
             heading="مرصد: السبب مو واحد",
             body="مرصد «إيكو عراق» يرى أن التسارع «مجموعة عوامل متداخلة لا يمكن اختزالها بسبب واحد»، منها القلق مما بعد 30 أيلول. والمستشار المالي لرئيس الوزراء نفى وجود خطة أميركية معلنة لوقف شحنات الدولار (وكالة الصحافة المستقلة).",
             stat=("30", "September — the date the market anxiety is pegged to; the PM's financial adviser denies any announced US plan to halt dollar shipments",
                   "أيلول التاريخ الذي يُعلَّق عليه قلق السوق — ومستشار رئيس الوزراء المالي ينفي وجود خطة أميركية معلنة لوقف شحنات الدولار"),
             sup=[("المرصد", "إيكو عراق"), ("التاريخ", "30 أيلول"), ("الخطة", "منفية")],
             phrases=["مرصد يقول أسباب متداخلة", "منها قلق 30 أيلول", "والمستشار ينفي الخطة"]),
    ],
    sources=[("شبكة 964", "964media.com"), ("وكالة الصحافة المستقلة", "mustaqila.com")],
    sourcesLine="المصادر: شبكة 964 · وكالة الصحافة المستقلة — 19 أيلول 2026",
    hookHeadline="المركزي: ما عدنا مشكلة احتياطي",
    voText=("قال البنك المركزي العراقي في بيان اليوم السبت إن لديه كفاية من الاحتياطيات الأجنبية لتلبية الطلبات على العملة بالسعر الرسمي، "
            "لتمويل التجارة الخارجية وبطاقات المصارف وطلبات المسافرين، بحسب شبكة تسعمئة وأربعة وستين. "
            "وعزا البيان ارتفاع الدولار إلى المضاربات في الأسواق والتوقعات وسوء استخدام الظروف الجيوسياسية. ولم يذكر البيان أي رقم للاحتياطيات. "
            "في المقابل، يرى مرصد إيكو عراق أن الارتفاع مجموعة عوامل متداخلة لا يمكن اختزالها بسبب واحد، منها القلق مما بعد الثلاثين من أيلول، "
            "فيما نفى المستشار المالي لرئيس الوزراء وجود خطة أميركية معلنة لوقف شحنات الدولار. تصدّق سبب الغلاء مضاربة لو شي ثاني؟"),
    pops=[("0", "رقم للاحتياطيات ورد في البيان", "رقم"), ("30", "أيلول — موعد يتعلق به قلق السوق", "الثلاثين")],
)

# ---------------------------------------------------------------- E · Anbar petrol (V10.1 CONTROL)
s = "e-anbar-petrol-queues-end"
SLATE[s] = dict(
    topicBucket="iraq_services", variant="C", accent="#D72638",
    kicker="خدمات",
    headline="الأنبار: انفضّت طوابير البنزين",
    subhead=("ANBAR · SEP 19 | 964 (15:42): PROVINCIAL GOVERNMENT SPOKESMAN MUAYYAD AL-DULAIMI ANNOUNCED SATURDAY "
             "THE QUEUES HAVE BROKEN UP AND THE PETROL CRISIS IN THE PROVINCE IS OVER | DAILY FUEL QUOTA RAISED FROM "
             "40 TO 44 TANKER TRUCKS (+4, COMPUTED) | THE SHORTAGE HAD HIT ANBAR ALONGSIDE OTHER PROVINCES, LEAVING "
             "DRIVERS QUEUING FOR HOURS | NO START DATE FOR THE CRISIS GIVEN IN THE REPORT"),
    endQuestion="شكد وكفت بطابور البنزين هالأسبوع؟",
    ticker=[
        "مؤيد الدليمي الناطق الرسمي لحكومة الأنبار المحلية: فض الطوابير وانتهاء أزمة البنزين (شبكة 964 — 19 أيلول)",
        "زيادة الحصة اليومية من الوقود من 40 إلى 44 سيارة حوضية",
        "الشحّ طال الأنبار إلى جانب محافظات عراقية أخرى وأدى إلى طوابير طويلة أمام المحطات",
        "التقرير لم يذكر تاريخ بدء الأزمة",
    ],
    beats=[
        dict(label="الإعلان",
             heading="الأنبار تعلن انتهاء أزمة البنزين",
             body="مؤيد الدليمي، الناطق الرسمي لحكومة الأنبار المحلية، أعلن السبت فضّ الطوابير وانتهاء أزمة البنزين في المحافظة (شبكة 964).",
             stat=("44", "Fuel tanker trucks now reaching Anbar daily, up from 40, per the provincial spokesman",
                   "سيارة حوضية تصل الأنبار يومياً الآن بعد أن كانت 40، بحسب ناطق الحكومة المحلية"),
             sup=[("قبل", "40"), ("بعد", "44"), ("الزيادة", "+4")],
             phrases=["الأنبار تعلن", "انتهت أزمة البنزين", "والطوابير انفضت"]),
        dict(label="الزيادة",
             heading="4 حوضيات زيادة باليوم",
             body="الحصة اليومية من الوقود ارتفعت من 40 إلى 44 سيارة حوضية، أي بزيادة أربع حوضيات يومياً — محتسبة من رقمَي الناطق نفسه.",
             stat=("+4", "Extra tanker trucks per day — computed from the spokesman's own two figures (40 → 44)",
                   "سيارات حوضية إضافية يومياً — محتسبة من رقمَي الناطق نفسه (40 ثم 44)"),
             sup=[("الحصة", "يومية"), ("الفرق", "+4"), ("النسبة", "10%")],
             phrases=["الحصة صارت 44", "بعد ما كانت 40", "أربع حوضيات زيادة"]),
        dict(label="الخلفية",
             heading="الشحّ ما كان بالأنبار بس",
             body="الشحّ طال الأنبار إلى جانب محافظات عراقية أخرى، وترك السائقين بطوابير طويلة وساعات انتظار أمام المحطات. والتقرير لم يذكر تاريخ بدء الأزمة ولا وضع بقية المحافظات اليوم.",
             stat=("0", "Start dates or other-province updates given in the report — only Anbar's own status",
                   "تواريخ لبدء الأزمة أو تحديثات عن بقية المحافظات وردت في التقرير — الإعلان يخص الأنبار وحدها"),
             sup=[("الامتداد", "محافظات أخرى"), ("الانتظار", "ساعات"), ("تفاصيل أخرى", "0")],
             phrases=["الشحّ طال محافظات", "مو بس الأنبار", "وساعات انتظار"]),
    ],
    sources=[("شبكة 964", "964media.com")],
    sourcesLine="المصدر: شبكة 964 — 19 أيلول 2026",
)

MONTH_AR = "أيلول"
for slug, d in SLATE.items():
    full = f"{D}-{slug}"
    props = {
        "dateLabel": "SEP 19 • 2026",
        "arabicDateLabel": f"19 {MONTH_AR} 2026",
        "handle": "@photonect.news",
        "audioBed": "audio/mood_newsroom.mp3",
        "topicBucket": d["topicBucket"],
        "variant": d["variant"],
        "breaking": {
            "arabicKicker": d["kicker"],
            "arabicHeadline": d["headline"],
            "englishSubhead": d["subhead"],
            "heroMedia": img(slug, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [],
        "arabicTicker": d["ticker"],
        "endQuestion": d["endQuestion"],
        "sources": [{"name": n, "domain": dom} for n, dom in d["sources"]],
    }
    for i, b in enumerate(d["beats"], 1):
        v, en, ar = b["stat"]
        props["beats"].append({
            "label": b["label"],
            "arabicHeading": b["heading"],
            "arabicBody": b["body"],
            "bigStat": {"value": v, "label": en, "arabicLabel": ar},
            "supportingStats": [{"label": l, "value": val} for l, val in b["sup"]],
            "broll": img(slug, f"broll_{i}.jpg"),
            "brolls": [img(slug, f"broll_{i}.jpg")],
            "brollType": "image",
            "accent": d["accent"],
            "brollSource": "صورة أرشيفية · Pexels",
            "subtitlePhrases": b["phrases"],
        })
    pdir = POSTS / full / ".meta"
    pdir.mkdir(parents=True, exist_ok=True)
    (pdir / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")

    if "voText" in d:
        brief = {
            "slug": full,
            "kicker": d["kicker"],
            "hookHeadline": d["hookHeadline"],
            "voText": d["voText"],
            "endQuestion": d["endQuestion"],
            "sourcesLine": d["sourcesLine"],
            "images": [img(slug, f) for f in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")],
            "audioBed": "audio/mood_newsroom.mp3",
            "statPops": [{"value": v, "label": l, "matchWord": m} for v, l, m in d["pops"]],
        }
        (pdir / "v11-brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {full}" + ("  [V11]" if "voText" in d else "  [V10.1 control]"))
