#!/usr/bin/env python3
"""Author the 6 props.json for the 2026-06-18 slate (V10.1 engine: ONE still per beat).
Zero-energy, discovery-led slate — six different worlds:
  1 iraq-mosul-museum   (iraq_domestic, C)  culture/heritage
  2 iran-us-deal-signing(mena_geopolitics,A) diplomacy/peace
  3 mammal-regeneration (wildcard, B)        biomedical science
  4 saudi-seha-hospital (gulf_regional, A)   health-tech
  5 jwst-exoplanet-roasted (wildcard, B)     space/astronomy
  6 superconductor-leap (tech_ai, C)         physics/tech
Western numerals throughout; decimals never rounded. audioBed set later by
assign-mood-rotation.py — left as placeholder here."""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-06-18"
DLABEL = "JUN 18 • 2026"
ADLABEL = "18 يونيو 2026"
IMG = "images/news"

A1, A2, A3 = "#FFC217", "#2EA6FF", "#D72638"


def beat(label, heading, body, bv, bl, bal, s1, s2, s3, accent, broll):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": bv, "label": bl, "arabicLabel": bal},
        "supportingStats": [
            {"label": s1[0], "value": s1[1]},
            {"label": s2[0], "value": s2[1]},
            {"label": s3[0], "value": s3[1]},
        ],
        "broll": broll,
        "brolls": [broll],
        "brollType": "image",
        "accent": accent,
        "brollSource": "Photonect · 2026",
    }


def img(slug, f):
    return f"{IMG}/{slug}/{f}"


SLUGS = {}

# ---------------------------------------------------------------- 1. MOSUL MUSEUM
s = f"{DATE}-iraq-mosul-museum"
SLUGS[s] = {
    "dateLabel": DLABEL, "arabicDateLabel": ADLABEL, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "iraq_domestic", "variant": "C",
    "breaking": {
        "arabicKicker": "تراث",
        "arabicHeadline": "متحف الموصل يستعد لإعادة الافتتاح",
        "englishSubhead": "MOSUL CULTURAL MUSEUM TO REOPEN IN 2026",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "متحف الموصل يفتح أبوابه خريف 2026",
             "يستعد متحف الموصل الثقافي، ثاني أكبر متاحف العراق، لإعادة الافتتاح خريف 2026 بعد نحو 20 عاماً من الإغلاق ودمار تنظيم داعش، وفق سميثسونيان.",
             "خريف 2026", "Planned reopening of the Mosul Cultural Museum", "موعد إعادة الافتتاح المرتقب",
             ("مغلق منذ", "~20 عاماً"), ("دمار التنظيم", "2015"), ("المصدر", "Smithsonian"),
             A1, img(s, "broll_1.jpg")),
        beat("لماذا يهم؟", "تحالف دولي يعيد الحياة للمتحف",
             "يقود الترميم تحالف من 5 جهات يضم متحف اللوفر وصندوق آليف ومؤسسة سميثسونيان وصندوق الآثار العالمي مع هيئة الآثار العراقية، وفق اللوفر.",
             "5 شركاء", "International institutions restoring the museum", "جهات دولية تشارك في الترميم",
             ("ترميم القطع", "اللوفر"), ("العمارة", "WMF"), ("التمويل", "ALIPH"),
             A2, img(s, "broll_2.jpg")),
        beat("ماذا بعد؟", "رمز لتعافي الموصل بعد الحرب",
             "بعد تحرير المدينة عام 2017، يصبح المتحف رمزاً لعودة الموصل، فيما تُرمَّم القطع الآشورية والحَضرية التي حطمها التنظيم، وفق تايمز أوف إسرائيل.",
             "2017", "Year Mosul was liberated from ISIS", "عام تحرير الموصل",
             ("القطع", "آشورية وحَضرية"), ("المدينة", "الموصل"), ("المصدر", "The Art Newspaper"),
             A3, img(s, "broll_3.jpg")),
    ],
    "sources": [
        {"name": "Smithsonian Magazine", "domain": "smithsonianmag.com"},
        {"name": "Musée du Louvre", "domain": "louvre.fr"},
        {"name": "ALIPH Foundation", "domain": "aliph-foundation.org"},
        {"name": "The Times of Israel", "domain": "timesofisrael.com"},
        {"name": "The Art Newspaper", "domain": "theartnewspaper.com"},
    ],
    "arabicTicker": [
        "متحف الموصل الثقافي يستعد لإعادة الافتتاح خريف 2026 بعد ~20 عاماً، وفق سميثسونيان",
        "دمّر تنظيم داعش مقتنيات المتحف عام 2015 وحطّم قطعاً آشورية وحَضرية",
        "تحالف من 5 جهات يقود الترميم: اللوفر وآليف وسميثسونيان وصندوق الآثار العالمي وهيئة الآثار العراقية",
        "اللوفر يتولّى ترميم القطع وصندوق الآثار العالمي يتولّى العمارة، وفق اللوفر",
        "بعد تحرير الموصل عام 2017 يعود المتحف رمزاً للتعافي الثقافي",
        "هل يعيد المتحف الموصل إلى خريطة السياحة الثقافية؟",
    ],
}

# ---------------------------------------------------------------- 2. IRAN-US DEAL SIGNING
s = f"{DATE}-iran-us-deal-signing"
SLUGS[s] = {
    "dateLabel": DLABEL, "arabicDateLabel": ADLABEL, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
    "breaking": {
        "arabicKicker": "عاجل",
        "arabicHeadline": "واشنطن وطهران نحو توقيع اتفاق في سويسرا",
        "englishSubhead": "US AND IRAN TO SIGN INTERIM DEAL FRIDAY IN SWITZERLAND",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "توقيع مذكرة تفاهم الجمعة في سويسرا",
             "تعتزم الولايات المتحدة وإيران توقيع مذكرة تفاهم مرحلية الجمعة في سويسرا تفتح الطريق لإنهاء الحرب المندلعة منذ 28 فبراير، وفق بلومبرغ وفرانس 24.",
             "الجمعة", "Planned signing of the US-Iran interim memorandum", "موعد توقيع المذكرة المرتقب",
             ("بدء الحرب", "28 فبراير"), ("مكان التوقيع", "سويسرا"), ("المصدر", "Bloomberg"),
             A1, img(s, "broll_1.jpg")),
        beat("لماذا يهم؟", "مسار اقتصادي وتجميد للتصعيد",
             "يفتح الاتفاق الباب أمام برنامج تنمية اقتصادية بقيمة 300 مليار دولار بعد محادثات السلام، مقابل تعهّد واشنطن بعدم فرض عقوبات جديدة، وفق بلومبرغ.",
             "300 مليار $", "Economic development program Iran could access", "حجم البرنامج الاقتصادي المتاح",
             ("عقوبات جديدة", "مُجمّدة"), ("قوات إضافية", "مُجمّدة"), ("المصدر", "Bloomberg"),
             A2, img(s, "broll_2.jpg")),
        beat("ماذا بعد؟", "60 يوماً من المحادثات حول الملف النووي",
             "يمنح الاتفاق 60 يوماً من المحادثات لإنهاء الحرب وضبط البرنامج النووي، مع تأكيد طهران عدم سعيها لسلاح نووي وتثبيت وضعه الراهن، وفق فرانس 24.",
             "60 يوماً", "Negotiation window to end the war", "مهلة المحادثات لإنهاء الحرب",
             ("الملف النووي", "تثبيت الوضع"), ("سلاح نووي", "لا"), ("المصدر", "France 24"),
             A3, img(s, "broll_3.jpg")),
    ],
    "sources": [
        {"name": "Bloomberg", "domain": "bloomberg.com"},
        {"name": "France 24", "domain": "france24.com"},
        {"name": "Council on Foreign Relations", "domain": "cfr.org"},
        {"name": "Associated Press", "domain": "apnews.com"},
    ],
    "arabicTicker": [
        "واشنطن وطهران تعتزمان توقيع مذكرة تفاهم مرحلية الجمعة في سويسرا، وفق بلومبرغ",
        "الاتفاق يفتح الطريق لإنهاء الحرب المندلعة منذ 28 فبراير 2026",
        "برنامج تنمية اقتصادية بقيمة 300 مليار دولار يُتاح لإيران بعد محادثات السلام",
        "واشنطن تتعهّد بعدم فرض عقوبات جديدة أو نشر قوات إضافية، وفق بلومبرغ",
        "60 يوماً من المحادثات لإنهاء الحرب وضبط البرنامج النووي، وفق فرانس 24",
        "طهران تؤكد عدم سعيها لسلاح نووي وتثبيت وضع برنامجها الراهن",
        "هل يصمد الاتفاق المرحلي حتى سلام دائم؟",
    ],
}

# ---------------------------------------------------------------- 3. MAMMAL REGENERATION
s = f"{DATE}-mammal-regeneration"
SLUGS[s] = {
    "dateLabel": DLABEL, "arabicDateLabel": ADLABEL, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "wildcard", "variant": "B",
    "breaking": {
        "arabicKicker": "علوم",
        "arabicHeadline": "قدرة الثدييات على التجدّد ليست مفقودة بل مُعطّلة",
        "englishSubhead": "MAMMAL REGENERATION MAY BE SWITCHED OFF, NOT LOST",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "مفتاح جيني مُعطّل وراء فقدان التجدّد",
             "كشفت دراستان في مجلة ساينس أن قدرة الثدييات على إعادة بناء أنسجة معقّدة ليست مفقودة بل مُعطّلة، بقيادة فريق من جامعة تكساس إيه آند إم، وفق ساينس ديلي.",
             "2 دراستان", "New studies published in the journal Science", "دراستان جديدتان في مجلة ساينس",
             ("الجهة", "تكساس إيه آند إم"), ("النشر", "مجلة Science"), ("المصدر", "ScienceDaily"),
             A1, img(s, "broll_1.jpg")),
        beat("لماذا يهم؟", "الأكسجين وفيتامين A يتحكّمان بالتجدّد",
             "وجد الباحثون أن استشعار الأكسجين وجين Aldh1a2 المنتج لحمض الريتينويك يكبحان التجدّد لدى الثدييات بينما تحتفظ به البرمائيات، وفق ساينس ديلي.",
             "Aldh1a2", "Gene mammals fail to fully activate after injury", "الجين الذي تعجز الثدييات عن تفعيله",
             ("المُحفّز", "حمض الريتينويك"), ("المقارنة", "البرمائيات"), ("المصدر", "Science"),
             A2, img(s, "broll_2.jpg")),
        beat("ماذا بعد؟", "فئران تُعيد بناء أنسجة أذنها",
             "بعد إعادة تفعيل المفتاح أو حقن حمض الريتينويك، أعادت الفئران بناء أنسجة في ثقوب أذنها، ما يفتح آفاقاً لعلاج الجروح، مع حاجة لتجارب لاحقة، وفق ساينس أليرت.",
             "أنسجة جديدة", "Tissue regrown in mice ear holes", "أنسجة أعادت الفئران بناءها",
             ("التطبيق", "التئام الجروح"), ("المرحلة", "تجارب على الفئران"), ("المصدر", "ScienceAlert"),
             A3, img(s, "broll_3.jpg")),
    ],
    "sources": [
        {"name": "Science (AAAS)", "domain": "science.org"},
        {"name": "ScienceDaily", "domain": "sciencedaily.com"},
        {"name": "Texas A&M University", "domain": "tamu.edu"},
        {"name": "ScienceAlert", "domain": "sciencealert.com"},
        {"name": "Nature", "domain": "nature.com"},
    ],
    "arabicTicker": [
        "دراستان في مجلة ساينس: قدرة الثدييات على التجدّد مُعطّلة لا مفقودة، وفق ساينس ديلي",
        "فريق من جامعة تكساس إيه آند إم يكشف آليتين تتحكّمان بالتجدّد",
        "استشعار الأكسجين يكبح تجدّد الأطراف لدى الثدييات بعكس البرمائيات",
        "جين Aldh1a2 المنتج لحمض الريتينويك لا يُفعّل بالكامل بعد الإصابة",
        "فئران أعادت بناء أنسجة ثقوب أذنها بعد إعادة تفعيل المفتاح، وفق ساينس أليرت",
        "النتائج على الفئران فقط ولا تزال بحاجة إلى تجارب بشرية",
        "هل يتعلّم الإنسان يوماً إعادة بناء أنسجته؟",
    ],
}

# ---------------------------------------------------------------- 4. SAUDI SEHA VIRTUAL HOSPITAL
s = f"{DATE}-saudi-seha-hospital"
SLUGS[s] = {
    "dateLabel": DLABEL, "arabicDateLabel": ADLABEL, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "gulf_regional", "variant": "A",
    "breaking": {
        "arabicKicker": "الخليج",
        "arabicHeadline": "مستشفى صحة الافتراضي الأكبر عالمياً يتوسّع",
        "englishSubhead": "SAUDI SEHA VIRTUAL HOSPITAL, WORLD'S LARGEST, EXPANDS",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "242 مستشفى مرتبطة بمنصّة واحدة",
             "يربط مستشفى صحة الافتراضي السعودي، الأكبر عالمياً، 242 مستشفى عبر منصّة موحّدة للطب عن بُعد ضمن برنامج تحوّل القطاع الصحي، وفق رؤية 2030.",
             "242 مستشفى", "Hospitals linked to Seha Virtual Hospital", "عدد المستشفيات المرتبطة بالمنصّة",
             ("التصنيف", "الأكبر عالمياً"), ("الإطلاق", "2022"), ("المصدر", "رؤية 2030"),
             A1, img(s, "broll_1.jpg")),
        beat("لماذا يهم؟", "16 مليون موعد افتراضي في عام واحد",
             "قدّم المستشفى أكثر من 16 مليون موعد واستشارة افتراضية خلال 2025 بنموّ 56% عن العام السابق، مع تغطية خدمية بلغت 97.4% للمملكة، وفق وزارة الصحة.",
             "16 مليون+", "Virtual appointments delivered in 2025", "المواعيد الافتراضية خلال 2025",
             ("النموّ", "56%"), ("التغطية", "97.4%"), ("المصدر", "وزارة الصحة"),
             A2, img(s, "broll_2.jpg")),
        beat("ماذا بعد؟", "الصحة الرقمية ركيزة اقتصادية",
             "يسهم القطاع الصحي بنحو 5% من الناتج المحلي، فيما تتجه المملكة لتصدير نموذج الصحة الرقمية والذكاء الاصطناعي الطبي، وفق العربية ووزير الصحة الجلاجل.",
             "~5%", "Healthcare's contribution to Saudi GDP", "إسهام القطاع الصحي في الناتج المحلي",
             ("الاتجاه", "تصدير النموذج"), ("الخدمات", "30+ تخصصاً"), ("المصدر", "Arab News"),
             A3, img(s, "broll_3.jpg")),
    ],
    "sources": [
        {"name": "Saudi MOH", "domain": "moh.gov.sa"},
        {"name": "Saudi Vision 2030", "domain": "vision2030.gov.sa"},
        {"name": "Arab News", "domain": "arabnews.com"},
        {"name": "Fast Company Middle East", "domain": "fastcompanyme.com"},
        {"name": "ITIJ", "domain": "itij.com"},
    ],
    "arabicTicker": [
        "مستشفى صحة الافتراضي السعودي الأكبر عالمياً يربط 242 مستشفى عبر منصّة موحّدة، وفق رؤية 2030",
        "أكثر من 16 مليون موعد واستشارة افتراضية خلال 2025 بنموّ 56%، وفق وزارة الصحة",
        "التغطية الخدمية الصحية بلغت 97.4% من المملكة",
        "القطاع الصحي يسهم بنحو 5% من الناتج المحلي السعودي",
        "المنصّة تقدّم أكثر من 30 تخصصاً ضمن برنامج تحوّل القطاع الصحي",
        "المملكة تتجه لتصدير نموذج الصحة الرقمية والذكاء الاصطناعي الطبي",
        "هل يصبح الطب عن بُعد مستقبل الرعاية في المنطقة؟",
    ],
}

# ---------------------------------------------------------------- 5. JWST EXOPLANET ROASTED
s = f"{DATE}-jwst-exoplanet-roasted"
SLUGS[s] = {
    "dateLabel": DLABEL, "arabicDateLabel": ADLABEL, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "wildcard", "variant": "B",
    "breaking": {
        "arabicKicker": "فضاء",
        "arabicHeadline": "ويب يرصد كوكباً تشويه نجمه عند اقترابه",
        "englishSubhead": "WEBB CATCHES AN EXOPLANET ROASTED BY ITS STAR",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "تلسكوب ويب يرصد كوكباً يُشوى دورياً",
             "رصد تلسكوب جيمس ويب الكوكب الخارجي HD 80606 b، وكتلته 4 أضعاف المشتري، وهو يُشوى عند اقترابه من نجمه الشبيه بالشمس في مدار شديد الاستطالة، وفق ناسا.",
             "×4 المشتري", "Mass of exoplanet HD 80606 b vs Jupiter", "كتلة الكوكب مقارنةً بالمشتري",
             ("الكوكب", "HD 80606 b"), ("النجم", "شبيه بالشمس"), ("المصدر", "NASA"),
             A1, img(s, "broll_1.jpg")),
        beat("لماذا يهم؟", "حرارته ترتفع 1100 درجة عند الاقتراب",
             "خلال مداره البالغ 111 يوماً ترتفع حرارة الكوكب نحو 1100 درجة فهرنهايت عند أقرب نقطة من نجمه، ما يوفّر مختبراً طبيعياً لدراسة الغلاف الجوي، وفق ناسا.",
             "+1100°F", "Temperature surge at closest approach", "ارتفاع الحرارة عند أقرب نقطة",
             ("مدّة المدار", "111 يوماً"), ("الأداة", "MIRI"), ("المصدر", "NASA"),
             A2, img(s, "broll_2.jpg")),
        beat("ماذا بعد؟", "بصمات الميثان وثاني أكسيد الكربون",
             "قاس فريق مختبر الدفع النفّاث بقيادة تيفاني كاتاريا التركيب الكيميائي ورصد بصمات الميثان وثاني أكسيد الكربون، ما يعمّق فهم الأجواء الحارّة، وفق ناسا.",
             "CH₄ + CO₂", "Chemical signatures Webb detected", "البصمات الكيميائية التي رصدها ويب",
             ("المختبر", "JPL/NASA"), ("القياس", "الطيف الحراري"), ("المصدر", "NASA"),
             A3, img(s, "broll_3.jpg")),
    ],
    "sources": [
        {"name": "NASA", "domain": "science.nasa.gov"},
        {"name": "NASA JPL", "domain": "jpl.nasa.gov"},
        {"name": "Space.com", "domain": "space.com"},
        {"name": "Johns Hopkins APL", "domain": "jhuapl.edu"},
    ],
    "arabicTicker": [
        "تلسكوب ويب يرصد الكوكب الخارجي HD 80606 b وكتلته 4 أضعاف المشتري، وفق ناسا",
        "الكوكب يدور في مدار شديد الاستطالة مدّته 111 يوماً حول نجم شبيه بالشمس",
        "حرارة الكوكب ترتفع نحو 1100 درجة فهرنهايت عند أقرب نقطة من نجمه",
        "أداة MIRI رصدت بصمات الميثان وثاني أكسيد الكربون في غلافه الجوي",
        "فريق مختبر الدفع النفّاث بقيادة تيفاني كاتاريا قاد الرصد، وفق ناسا",
        "مدارات شديدة الاستطالة تمنح مختبراً طبيعياً لدراسة الأجواء الحارّة",
    ],
}

# ---------------------------------------------------------------- 6. SUPERCONDUCTOR LEAP
s = f"{DATE}-superconductor-leap"
SLUGS[s] = {
    "dateLabel": DLABEL, "arabicDateLabel": ADLABEL, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "tech_ai", "variant": "C",
    "breaking": {
        "arabicKicker": "تكنولوجيا",
        "arabicHeadline": "باحثون سويديون يعزّزون التوصيل الفائق",
        "englishSubhead": "SWEDISH TEAM BOOSTS SUPERCONDUCTIVITY BY SCULPTING THE SUBSTRATE",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "نحت السطح يرفع أداء التوصيل الفائق",
             "أظهر باحثون في جامعة تشالمرز السويدية أن نحت السطح الحامل لطبقة فائقة التوصيل بالغة الرقّة يبقيها موصِّلة عند حرارة أعلى ومجالات مغناطيسية أقوى، وفق ساينس ديلي.",
             "Nature Comms", "Journal publishing the study, June 2026", "مجلة نشر الدراسة في يونيو 2026",
             ("الجامعة", "تشالمرز"), ("النشر", "17 يونيو 2026"), ("المصدر", "ScienceDaily"),
             A1, img(s, "broll_1.jpg")),
        beat("لماذا يهم؟", "طبقة أرقّ من جزء من مليون من الشعرة",
             "تبلغ سماكة الطبقة بضعة نانومترات، أي أقل من جزء من مليون من سُمك شعرة الإنسان، وتُهندَس عبر نحت القاعدة بدل البحث عن مواد جديدة، وفق بايو إنجينير.",
             "بضعة نانومترات", "Thickness of the superconducting film", "سماكة الطبقة فائقة التوصيل",
             ("المادة", "YBCO"), ("القاعدة", "أكسيد المغنيسيوم"), ("المصدر", "Bioengineer"),
             A2, img(s, "broll_2.jpg")),
        beat("ماذا بعد؟", "إلكترونيات أوفر للطاقة وحوسبة كمومية",
             "يَعِد النهج بإلكترونيات أوفر للطاقة وتقنيات كمومية، في وقت تستهلك تقنيات المعلومات 6 إلى 12% من كهرباء العالم، بقيادة فلوريانا لومباردي، وفق ساينس ديلي.",
             "6–12%", "Share of global electricity used by ICT", "حصة تقنيات المعلومات من كهرباء العالم",
             ("الباحثة", "فلوريانا لومباردي"), ("التطبيق", "حوسبة كمومية"), ("المصدر", "ScienceDaily"),
             A3, img(s, "broll_3.jpg")),
    ],
    "sources": [
        {"name": "ScienceDaily", "domain": "sciencedaily.com"},
        {"name": "Chalmers University of Technology", "domain": "chalmers.se"},
        {"name": "Bioengineer", "domain": "bioengineer.org"},
        {"name": "EurekAlert", "domain": "eurekalert.org"},
        {"name": "Nature Communications", "domain": "nature.com"},
    ],
    "arabicTicker": [
        "باحثو جامعة تشالمرز السويدية يعزّزون التوصيل الفائق عبر نحت السطح الحامل، وفق ساينس ديلي",
        "الطبقة فائقة التوصيل تبقى فاعلة عند حرارة أعلى ومجالات مغناطيسية أقوى",
        "سماكة الطبقة بضعة نانومترات، أقل من جزء من مليون من سُمك شعرة الإنسان",
        "النهج يهندس القاعدة (أكسيد المغنيسيوم) بدل البحث عن مواد جديدة",
        "الدراسة نُشرت في Nature Communications في 17 يونيو 2026",
        "تقنيات المعلومات تستهلك 6 إلى 12% من كهرباء العالم اليوم",
        "هل تقرّبنا الهندسة الدقيقة من توصيل فائق بحرارة الغرفة؟",
    ],
}

# ---------------------------------------------------------------- write
for slug, props in SLUGS.items():
    meta = POSTS / slug / ".meta"
    meta.mkdir(parents=True, exist_ok=True)
    (meta / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
    (meta / "media-stamp.json").write_text(
        json.dumps({"manual": True, "source": "nano-banana-pro", "date": DATE}, ensure_ascii=False),
        encoding="utf-8")
    print(f"props + stamp: {slug} ({len(props['beats'])} beats, {props['variant']}/{props['topicBucket']})")
print(f"\n{len(SLUGS)}/6 props written")
