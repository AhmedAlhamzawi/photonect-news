#!/usr/bin/env python3
"""Author the 6 props.json for the 2026-06-29 Photonect NEWS slate.

Slate (6 worlds, energy-topic=1, outside biz+politics=5):
  1 iraq-drought-tombs     iraq_domestic   C  (worst drought since 1933 + exposed tombs)
  2 f1-austria-russell     wildcard        B  (Russell wins Austrian GP)
  3 hormuz-record-flow     mena_geopolitics A (record 20M bbl/day through Hormuz)
  4 asteroid-flyby-1997nc1 wildcard        C  (1-km "hazardous" asteroid safe flyby)
  5 aramco-rastanura-crash gulf_regional   A  (Aramco Ras Tanura helicopter crash)
  6 worldcup-canada-r16    wildcard        B  (Canada's stoppage-time World Cup win)

Arabic authored to spec (heading <=8 words, body <=26 words, 3 stat pills,
real bigStat per beat, Western numerals, every claim source-attributed). An
Opus iraqi-copywriter pass then polishes each file before render.
ONE still per beat (V10.1): beat.broll = the image matching THAT beat's text.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-06-29"
DATE_LABEL = "JUN 29 • 2026"
AR_DATE = "29 يونيو 2026"
ACCENTS = ["#FFC217", "#FF6B3D", "#D72638"]


def beat(label, heading, body, stat, ss, img_n, slug, accent, src):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": stat,
        "supportingStats": ss,
        "broll": f"images/news/{DATE}-{slug}/broll_{img_n}.jpg",
        "brolls": [f"images/news/{DATE}-{slug}/broll_{img_n}.jpg"],
        "brollType": "image",
        "accent": accent,
        "brollSource": src,
    }


def props(slug, bucket, variant, kicker, headline, subhead, beats, sources, ticker):
    return {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": AR_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/news_bed.mp3",
        "topicBucket": bucket,
        "variant": variant,
        "breaking": {
            "arabicKicker": kicker,
            "arabicHeadline": headline,
            "englishSubhead": subhead,
            "heroMedia": f"images/news/{DATE}-{slug}/hero.jpg",
            "heroMediaType": "image",
        },
        "beats": beats,
        "sources": sources,
        "arabicTicker": ticker,
    }


SLATE = {}

# ── 1. IRAQ DROUGHT + EXPOSED TOMBS ──────────────────────────────────────────
slug = "iraq-drought-tombs"
SLATE[slug] = props(
    slug, "iraq_domestic", "C", "بيئة",
    "أسوأ جفاف منذ 1933 يهدّد نهري العراق",
    "IRAQ DROUGHT | WORST SINCE 1933 | RESERVES NEAR 8%",
    [
        beat("ماذا حدث؟",
             "خزين المياه يقترب من 8% فقط",
             "العراق يعيش أسوأ جفاف منذ 1933، ومناسيب دجلة والفرات هبطت نحو 27%، فيما تراجع الخزين الاستراتيجي إلى ما يقارب 8% فقط، وفق آسيا نيوز.",
             {"value": "8%", "label": "water reserves left", "arabicLabel": "ما تبقّى من الخزين"},
             [{"label": "الأسوأ منذ", "value": "1933"},
              {"label": "تراجع المناسيب", "value": "27%"},
              {"label": "المصدر", "value": "AsiaNews"}],
             1, slug, ACCENTS[0], "AI generated · Photonect"),
        beat("لماذا يهم؟",
             "سدود الجوار تخنق الحصة المائية",
             "سدود تركيا وإيران قلّصت التدفّق، والعراق يتلقّى أقل من 35% من حصته النهرية، وشحّ المياه شرّد نحو 180,000 شخص، وفق المنظمة الدولية للهجرة.",
             {"value": "180,000", "label": "displaced by water scarcity", "arabicLabel": "نازح بسبب شحّ المياه"},
             [{"label": "من الحصة", "value": "أقل من 35%"},
              {"label": "السبب", "value": "سدود الجوار"},
              {"label": "المصدر", "value": "IOM"}],
             2, slug, ACCENTS[1], "AI generated · Photonect"),
        beat("ماذا بعد؟",
             "انحسار المياه يكشف 40 مقبرة أثرية",
             "مع تراجع المياه قرب سد الموصل، كشف باحثون نحو 40 مقبرة يعود تاريخها لأكثر من 2,300 عام إلى العصر الهلنستي، وفق سي بي إس وسميثسونيان.",
             {"value": "40", "label": "ancient tombs exposed", "arabicLabel": "مقبرة كشفها الجفاف"},
             [{"label": "عمرها", "value": "2,300+ سنة"},
              {"label": "الموقع", "value": "سد الموصل"},
              {"label": "المصدر", "value": "CBS · Smithsonian"}],
             3, slug, ACCENTS[2], "AI generated · Photonect"),
    ],
    [{"name": "AsiaNews", "domain": "asianews.it"},
     {"name": "CBS News", "domain": "cbsnews.com"},
     {"name": "Smithsonian", "domain": "smithsonianmag.com"},
     {"name": "Asharq Al-Awsat", "domain": "aawsat.com"},
     {"name": "IOM", "domain": "iom.int"}],
    ["العراق يعيش أسوأ جفاف منذ عام 1933 وفق آسيا نيوز",
     "مناسيب دجلة والفرات تهبط نحو 27% والخزين قرب 8% فقط",
     "العراق يتلقّى أقل من 35% من حصته من نهريه التاريخيين",
     "شحّ المياه يشرّد نحو 180,000 شخص وفق المنظمة الدولية للهجرة",
     "سدود تركيا وإيران تقلّص تدفّق المياه إلى العراق",
     "انحسار المياه قرب سد الموصل يكشف نحو 40 مقبرة أثرية",
     "المقابر تعود لأكثر من 2,300 عام إلى العصر الهلنستي"],
)

# ── 2. F1 AUSTRIAN GP — RUSSELL ──────────────────────────────────────────────
slug = "f1-austria-russell"
SLATE[slug] = props(
    slug, "wildcard", "B", "رياضة",
    "راسل يفوز بسباق النمسا متقدّمًا على فيرستابن",
    "F1 AUSTRIAN GP | RUSSELL WINS FROM POLE | VERSTAPPEN 2ND",
    [
        beat("ماذا حدث؟",
             "راسل يقودها من البداية للنهاية",
             "انطلق جورج راسل من المركز الأول وسيطر على سباق النمسا حتى خطّ النهاية، متقدّمًا على ماكس فيرستابن بفارق 1.611 ثانية، وأنتونيلي ثالثًا، وفق فورمولا 1.",
             {"value": "1.611s", "label": "gap over Verstappen", "arabicLabel": "الفارق على فيرستابن"},
             [{"label": "الانطلاق", "value": "المركز الأول"},
              {"label": "الثاني", "value": "فيرستابن"},
              {"label": "المصدر", "value": "Formula 1"}],
             1, slug, ACCENTS[0], "Wikimedia Commons"),
        beat("لماذا يهم؟",
             "فوزه الثاني هذا الموسم والأول منذ مارس",
             "هو الفوز الثاني لراسل في موسم 2026 والسابع في مسيرته، وأول انتصار له منذ أستراليا في مارس، ليؤكد صعود مرسيدس، وفق ESPN.",
             {"value": "2", "label": "wins in 2026", "arabicLabel": "فوزه الثاني هذا الموسم"},
             [{"label": "بمسيرته", "value": "7 انتصارات"},
              {"label": "آخر فوز", "value": "مارس بأستراليا"},
              {"label": "المصدر", "value": "ESPN"}],
             2, slug, ACCENTS[1], "AI generated · Photonect"),
        beat("ماذا بعد؟",
             "سباق اللقب يشتعل ويتقلّص الفارق",
             "بهذا الفوز قلّص راسل الفارق إلى 40 نقطة خلف المتصدّر أنتونيلي بعدما كان 50، ليبقى صراع اللقب مفتوحًا، وفق Yahoo Sports.",
             {"value": "40", "label": "points behind leader", "arabicLabel": "نقطة خلف المتصدّر"},
             [{"label": "المتصدّر", "value": "أنتونيلي"},
              {"label": "كان الفارق", "value": "50 نقطة"},
              {"label": "المصدر", "value": "Yahoo Sports"}],
             3, slug, ACCENTS[2], "AI generated · Photonect"),
    ],
    [{"name": "Formula 1", "domain": "formula1.com"},
     {"name": "ESPN", "domain": "espn.com"},
     {"name": "Yahoo Sports", "domain": "sports.yahoo.com"},
     {"name": "Crash.net", "domain": "crash.net"},
     {"name": "RacingNews365", "domain": "racingnews365.com"}],
    ["جورج راسل يفوز بسباق النمسا للفورمولا 1 من المركز الأول",
     "راسل يتقدّم على فيرستابن بفارق 1.611 ثانية وأنتونيلي ثالثًا",
     "الفوز الثاني لراسل هذا الموسم والسابع في مسيرته",
     "أول انتصار لراسل منذ سباق أستراليا في مارس",
     "راسل يقلّص الفارق إلى 40 نقطة خلف المتصدّر أنتونيلي",
     "صراع لقب الفورمولا 1 يبقى مفتوحًا بعد سباق النمسا",
     "مرسيدس تؤكد صعودها على حلبة ريد بُل رينغ"],
)

# ── 3. STRAIT OF HORMUZ — RECORD FLOW ────────────────────────────────────────
slug = "hormuz-record-flow"
SLATE[slug] = props(
    slug, "mena_geopolitics", "A", "عاجل",
    "تدفّق نفطي قياسي عبر مضيق هرمز خلال 24 ساعة",
    "HORMUZ | RECORD 20M BARRELS IN 24H | ROUTE WIDENED",
    [
        beat("ماذا حدث؟",
             "20 مليون برميل في يوم واحد",
             "أعلن وزير الطاقة الأميركي كريس رايت خروج نحو 20 مليون برميل عبر مضيق هرمز في 24 ساعة، رقم قياسي يتجاوز مستويات ما قبل الحرب، وفق CNBC.",
             {"value": "20 مليون", "label": "barrels in 24h", "arabicLabel": "برميل خلال 24 ساعة"},
             [{"label": "السجلّ", "value": "رقم قياسي"},
              {"label": "مقارنة", "value": "يتجاوز ما قبل الحرب"},
              {"label": "المصدر", "value": "CNBC"}],
             1, slug, ACCENTS[0], "AI generated · Photonect"),
        beat("لماذا يهم؟",
             "ممر موسّع قرب عُمان باتجاهين",
             "في 27 يونيو وسّع مركز المعلومات البحرية ممرًّا قرب عُمان لحركة باتجاهين، لكنّ عدد السفن ما زال نحو ثلث مستوى ما قبل الحرب، وفق NPR.",
             {"value": "1/3", "label": "vessel count vs pre-war", "arabicLabel": "عدد السفن مقابل ما قبل الحرب"},
             [{"label": "التاريخ", "value": "27 يونيو"},
              {"label": "الممر", "value": "باتجاهين قرب عُمان"},
              {"label": "المصدر", "value": "NPR"}],
             2, slug, ACCENTS[1], "AI generated · Photonect"),
        beat("ماذا بعد؟",
             "نافذة 60 يومًا بلا رسوم مرور",
             "ينصّ الاتفاق على سماح إيران بمرور السفن التجارية بلا رسوم لمدة 60 يومًا، تُحدَّد بعدها الرسوم مع عُمان وأطراف أخرى، وفق CNBC وNPR.",
             {"value": "60 يومًا", "label": "no-charge transit window", "arabicLabel": "مرور بلا رسوم"},
             [{"label": "بعدها", "value": "تُحدَّد الرسوم"},
              {"label": "الأطراف", "value": "إيران وعُمان"},
              {"label": "المصدر", "value": "CNBC · NPR"}],
             3, slug, ACCENTS[2], "AI generated · Photonect"),
    ],
    [{"name": "CNBC", "domain": "cnbc.com"},
     {"name": "NPR", "domain": "npr.org"},
     {"name": "US Dept. of Energy", "domain": "energy.gov"},
     {"name": "Reuters", "domain": "reuters.com"},
     {"name": "JMIC", "domain": "jmic.gov"}],
    ["نحو 20 مليون برميل تخرج عبر مضيق هرمز في 24 ساعة",
     "وزير الطاقة الأميركي: رقم قياسي يتجاوز مستويات ما قبل الحرب",
     "مركز المعلومات البحرية يوسّع ممرًّا قرب عُمان لحركة باتجاهين",
     "عدد السفن العابرة ما زال نحو ثلث مستوى ما قبل الحرب",
     "اتفاق يسمح بمرور السفن التجارية بلا رسوم لمدة 60 يومًا",
     "تُحدَّد رسوم المرور لاحقًا مع عُمان وأطراف أخرى",
     "تدفّق النفط يتعافى رغم هشاشة الهدنة في المضيق"],
)

# ── 4. ASTEROID 1997 NC1 FLYBY ───────────────────────────────────────────────
slug = "asteroid-flyby-1997nc1"
SLATE[slug] = props(
    slug, "wildcard", "C", "علوم",
    "كويكب بحجم كيلومتر يمرّ قرب الأرض بأمان",
    "ASTEROID 1997 NC1 | 1 KM WIDE | SAFE CLOSE PASS",
    [
        beat("ماذا حدث؟",
             "كويكب بعرض كيلومتر يعبر بأمان",
             "مرّ كويكب 1997 NC1 بعرض نحو كيلومتر واحد قرب الأرض بأمان يوم 27 يونيو، وهو من نوع آتن العابر لمدار كوكبنا، وفق EarthSky.",
             {"value": "1 كم", "label": "asteroid diameter", "arabicLabel": "قطر الكويكب"},
             [{"label": "المرور", "value": "آمن"},
              {"label": "التاريخ", "value": "27 يونيو"},
              {"label": "المصدر", "value": "EarthSky"}],
             1, slug, ACCENTS[0], "AI generated · Photonect"),
        beat("لماذا يهم؟",
             "مصنّف خطِرًا محتملًا دون خطر فعلي",
             "حجمه الكبير وقربه النسبي جعلاه مصنّفًا «كويكبًا خطِرًا محتملًا» منذ اكتشافه عام 1997، لكنّه لم يشكّل أي خطر فعلي على الأرض، وفق Space.com.",
             {"value": "1997", "label": "year discovered", "arabicLabel": "سنة اكتشافه"},
             [{"label": "التصنيف", "value": "خطِر محتمل"},
              {"label": "الخطر الفعلي", "value": "لا يوجد"},
              {"label": "المصدر", "value": "Space.com"}],
             2, slug, ACCENTS[1], "AI generated · Photonect"),
        beat("ماذا بعد؟",
             "رادار ناسا يرصده لأول مرة",
             "استخدمت ناسا هوائيي غولدستون بقطر 34 مترًا لرصده بالرادار لأول مرة، لتدقيق مداره ودعم أبحاث الدفاع الكوكبي، وفق مختبر الدفع النفّاث.",
             {"value": "34 م", "label": "Goldstone antenna size", "arabicLabel": "قطر هوائي غولدستون"},
             [{"label": "الرصد", "value": "أول مرة راداريًا"},
              {"label": "الهدف", "value": "الدفاع الكوكبي"},
              {"label": "المصدر", "value": "NASA JPL"}],
             3, slug, ACCENTS[2], "AI generated · Photonect"),
    ],
    [{"name": "NASA JPL", "domain": "jpl.nasa.gov"},
     {"name": "EarthSky", "domain": "earthsky.org"},
     {"name": "Space.com", "domain": "space.com"},
     {"name": "NASA", "domain": "nasa.gov"}],
    ["كويكب 1997 NC1 بعرض نحو كيلومتر يمرّ قرب الأرض بأمان",
     "المرور الآمن حدث يوم 27 يونيو وفق EarthSky",
     "الكويكب من نوع آتن العابر لمدار الأرض",
     "مصنّف «كويكبًا خطِرًا محتملًا» منذ اكتشافه عام 1997",
     "لم يشكّل الكويكب أي خطر فعلي على كوكبنا",
     "رادار غولدستون التابع لناسا يرصده لأول مرة",
     "البيانات تدقّق مداره وتدعم أبحاث الدفاع الكوكبي"],
)

# ── 5. ARAMCO RAS TANURA HELICOPTER CRASH ────────────────────────────────────
slug = "aramco-rastanura-crash"
SLATE[slug] = props(
    slug, "gulf_regional", "A", "عاجل",
    "تحطّم مروحية لأرامكو في رأس تنورة ومقتل 14",
    "ARAMCO | RAS TANURA HELICOPTER CRASH | 14 KILLED",
    [
        beat("ماذا حدث؟",
             "تحطّم مروحية فجر الأحد",
             "تحطّمت مروحية تابعة لأرامكو في رأس تنورة فجر الأحد عند نحو السادسة صباحًا، ما أسفر عن مقتل جميع من كانوا على متنها وعددهم 14، وفق واس.",
             {"value": "14", "label": "people killed", "arabicLabel": "قتيلًا على متنها"},
             [{"label": "الموقع", "value": "رأس تنورة"},
              {"label": "التوقيت", "value": "فجر الأحد"},
              {"label": "المصدر", "value": "واس"}],
             1, slug, ACCENTS[0], "AI generated · Photonect"),
        beat("لماذا يهم؟",
             "ضحايا سعوديون قرب مرفأ نفطي رئيسي",
             "أكّدت وزارة الطاقة أنّ الضحايا الـ14 جميعهم سعوديون، والحادث وقع قرب رأس تنورة، أحد أهم مرافئ تصدير النفط على الساحل الشرقي، وفق بلومبرغ.",
             {"value": "6:00 ص", "label": "time of crash", "arabicLabel": "توقيت الحادث"},
             [{"label": "الضحايا", "value": "سعوديون"},
              {"label": "الموقع", "value": "مرفأ نفطي رئيسي"},
              {"label": "المصدر", "value": "Bloomberg"}],
             2, slug, ACCENTS[1], "AI generated · Photonect"),
        beat("ماذا بعد؟",
             "تحقيق مفتوح في أسباب التحطّم",
             "فتحت الجهات المختصة تحقيقًا شاملًا لمعرفة سبب التحطّم، فيما لم تُعلَن الأسباب بعد، وتوالت التعازي الرسمية وتضامن الإمارات، وفق الجزيرة وغلف نيوز.",
             {"value": "تحقيق", "label": "investigation opened", "arabicLabel": "تحقيق في الأسباب"},
             [{"label": "الحالة", "value": "لجنة مختصة"},
              {"label": "الأسباب", "value": "غير معلنة"},
              {"label": "المصدر", "value": "Al Jazeera"}],
             3, slug, ACCENTS[2], "AI generated · Photonect"),
    ],
    [{"name": "Saudi Press Agency", "domain": "spa.gov.sa"},
     {"name": "Saudi Ministry of Energy", "domain": "moenergy.gov.sa"},
     {"name": "Bloomberg", "domain": "bloomberg.com"},
     {"name": "Al Jazeera", "domain": "aljazeera.com"},
     {"name": "Gulf News", "domain": "gulfnews.com"}],
    ["تحطّم مروحية تابعة لأرامكو في رأس تنورة فجر الأحد",
     "مقتل جميع من كانوا على متن المروحية وعددهم 14",
     "وزارة الطاقة: الضحايا الـ14 جميعهم سعوديون",
     "الحادث وقع قرب أحد أهم مرافئ تصدير النفط شرق المملكة",
     "الجهات المختصة تفتح تحقيقًا شاملًا في أسباب التحطّم",
     "لم تُعلَن أسباب الحادث حتى الآن",
     "تعازٍ رسمية وتضامن إماراتي مع السعودية"],
)

# ── 6. WORLD CUP — CANADA INTO R16 ───────────────────────────────────────────
slug = "worldcup-canada-r16"
SLATE[slug] = props(
    slug, "wildcard", "B", "مونديال",
    "كندا تهزم جنوب أفريقيا بهدف في الوقت القاتل",
    "WORLD CUP R32 | CANADA 1-0 | EUSTAQUIO 95'",
    [
        beat("ماذا حدث؟",
             "هدف في الدقيقة 95 يحسم المباراة",
             "سجّل ستيفن أوستاكيو في الدقيقة 95 هدفًا قاتلًا منح كندا فوزًا 1-0 على جنوب أفريقيا في دور الـ32 بلوس أنجلوس، وفق سي بي سي.",
             {"value": "95'", "label": "winning goal minute", "arabicLabel": "دقيقة هدف الفوز"},
             [{"label": "النتيجة", "value": "1-0"},
              {"label": "المسجّل", "value": "أوستاكيو"},
              {"label": "المصدر", "value": "CBC"}],
             1, slug, ACCENTS[0], "AI generated · Photonect"),
        beat("لماذا يهم؟",
             "كندا المضيفة أول المتأهلين للدور الـ16",
             "أصبحت كندا المستضيفة أول منتخب يبلغ دور الـ16، وشارك نجمها ألفونسو ديفيز للمرة الأولى في المونديال بديلًا في الدقيقة 75، وفق NBC.",
             {"value": "16", "label": "round reached", "arabicLabel": "بلغت دور الـ16"},
             [{"label": "الترتيب", "value": "أول المتأهلين"},
              {"label": "ديفيز", "value": "بديلًا د.75"},
              {"label": "المصدر", "value": "NBC"}],
             2, slug, ACCENTS[1], "Wikimedia Commons"),
        beat("ماذا بعد؟",
             "أرقام تؤكد السيطرة رغم قلّة الاستحواذ",
             "رغم استحواذ 42% فقط، تفوّقت كندا بالأهداف المتوقّعة 1.32 مقابل 0.13، وتلاقي المغرب أو هولندا في هيوستن يوم 4 يوليو، وفق ESPN.",
             {"value": "1.32", "label": "expected goals (xG)", "arabicLabel": "الأهداف المتوقّعة"},
             [{"label": "الاستحواذ", "value": "42%"},
              {"label": "الخصم", "value": "0.13 متوقّع"},
              {"label": "المصدر", "value": "ESPN"}],
             3, slug, ACCENTS[2], "AI generated · Photonect"),
    ],
    [{"name": "CBC", "domain": "cbc.ca"},
     {"name": "NBC", "domain": "nbclosangeles.com"},
     {"name": "ESPN", "domain": "espn.com"},
     {"name": "Yahoo Sports", "domain": "sports.yahoo.com"},
     {"name": "Bleacher Report", "domain": "bleacherreport.com"}],
    ["كندا تهزم جنوب أفريقيا 1-0 في دور الـ32 من المونديال",
     "ستيفن أوستاكيو يسجّل هدف الفوز في الدقيقة 95",
     "كندا المستضيفة أول منتخب يبلغ دور الـ16",
     "ألفونسو ديفيز يشارك للمرة الأولى في المونديال بديلًا",
     "كندا تتفوّق بالأهداف المتوقّعة 1.32 مقابل 0.13",
     "الفوز تحقّق رغم استحواذ كندي بنسبة 42% فقط",
     "كندا تلاقي المغرب أو هولندا في هيوستن يوم 4 يوليو"],
)

# ── write all ────────────────────────────────────────────────────────────────
for slug, data in SLATE.items():
    d = POSTS / f"{DATE}-{slug}" / ".meta"
    d.mkdir(parents=True, exist_ok=True)
    (d / "props.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    nbeats = len(data["beats"])
    print(f"  ✓ {DATE}-{slug}  ({data['variant']} · {data['topicBucket']} · {nbeats} beats)")
print(f"\nauthored {len(SLATE)} props.json")
