#!/usr/bin/env python3
"""Author the 6 props.json for the 2026-06-22 slate (V10.1 engine, one still per beat).

Six different worlds: Iraq at the World Cup (sport) / US-Iran Switzerland talks (diplomacy)
/ Iraq militia disarmament (governance) / GCC unified visa + rail (integration) /
pancreatic-cancer oral drug (medicine) / climate-resilient coral reefs (nature).
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/data/posts")
DATE = "2026-06-22"
DATE_LABEL = "JUN 22 • 2026"
AR_DATE = "22 يونيو 2026"
HANDLE = "@photonect.news"

Y = "#FFC217"
B = "#2EA6FF"
R = "#D72638"


def img(slug, name):
    return f"images/news/{DATE}-{slug}/{name}"


def beat(label, heading, body, val, ar_label, en_label, stats, slug, broll_name, accent):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": val, "label": en_label, "arabicLabel": ar_label},
        "supportingStats": [{"label": s[0], "value": s[1]} for s in stats],
        "broll": img(slug, broll_name),
        "brolls": [img(slug, broll_name)],
        "brollType": "image",
        "accent": accent,
        "brollSource": "Photonect · 2026",
    }


SLATE = {}

# ── 1. IRAQ AT THE WORLD CUP ─────────────────────────────────────────────
s = "iraq-worldcup-france"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
    "audioBed": "audio/music_01.mp3", "topicBucket": "wildcard", "variant": "C",
    "breaking": {
        "arabicKicker": "كأس العالم",
        "arabicHeadline": "العراق يواجه فرنسا في مونديال 2026",
        "englishSubhead": "IRAQ FACES FRANCE — FIRST WORLD CUP SINCE 1986",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "أسود الرافدين يعودون للمونديال",
             "يخوض منتخب العراق أولى مبارياته في كأس العالم 2026 أمام فرنسا ضمن المجموعة التاسعة، في أول ظهور مونديالي منذ 1986، وفق فيفا وإسبن.",
             "1986", "آخر ظهور مونديالي للعراق", "Iraq's last World Cup",
             [("المجموعة", "التاسعة"), ("الخصوم", "فرنسا والسنغال والنرويج"), ("المصدر", "FIFA")],
             s, "broll_1.jpg", Y),
        beat("كيف تأهل؟", "تأهل عبر ملحق أمام بوليفيا",
             "حسم العراق بطاقته الأخيرة بفوزه على بوليفيا في الملحق العالمي بمدينة مونتيري المكسيكية، مكمّلاً عقد الـ48 منتخباً، وفق إنسايد فيفا.",
             "48", "عدد منتخبات المونديال", "teams at the World Cup",
             [("الملحق", "مونتيري، المكسيك"), ("الخصم", "بوليفيا"), ("المصدر", "inside.fifa")],
             s, "broll_2.jpg", B),
        beat("ماذا بعد؟", "اختبار ثقيل ثم أمل التأهل",
             "بعد فرنسا يلاقي العراق السنغال والنرويج، وحلمه بلوغ الدور الثاني الذي تتأهل إليه أفضل المنتخبات في النسخة الموسّعة، وفق إسبن.",
             "3 مباريات", "مباريات دور المجموعات", "group-stage matches",
             [("المنافسون", "فرنسا/السنغال/النرويج"), ("الهدف", "دور الـ32"), ("المصدر", "ESPN")],
             s, "broll_3.jpg", R),
    ],
    "sources": [
        {"name": "FIFA", "domain": "fifa.com"},
        {"name": "Inside FIFA", "domain": "inside.fifa.com"},
        {"name": "ESPN", "domain": "espn.com"},
        {"name": "Wikipedia", "domain": "en.wikipedia.org"},
        {"name": "Tribuna", "domain": "tribuna.com"},
    ],
    "arabicTicker": [
        "منتخب العراق يعود إلى كأس العالم بعد غياب 40 عاماً منذ نسخة 1986، وفق فيفا",
        "العراق في المجموعة التاسعة إلى جانب فرنسا والسنغال والنرويج",
        "تأهل العراق بفوزه على بوليفيا في الملحق العالمي بمدينة مونتيري المكسيكية، وفق إنسايد فيفا",
        "نسخة 2026 الموسّعة تضم 48 منتخباً وتُقام في كندا والمكسيك والولايات المتحدة",
        "أفضل المنتخبات من المركز الثالث تبلغ دور الـ32 في النظام الجديد، وفق إسبن",
        "مباراة العراق وفرنسا أول اختبار مونديالي لأسود الرافدين",
    ],
}

# ── 2. US–IRAN SWITZERLAND TALKS ─────────────────────────────────────────
s = "iran-us-switzerland-talks"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
    "audioBed": "audio/music_02.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
    "breaking": {
        "arabicKicker": "دبلوماسية",
        "arabicHeadline": "واشنطن وطهران تبحثان إنهاء حرب لبنان",
        "englishSubhead": "US–IRAN TALKS IN SWITZERLAND TARGET LEBANON WAR",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "مفاوضات سويسرا تحقق تقدماً",
             "أعلن وزير خارجية إيران عباس عراقجي «تقدماً كبيراً» في محادثات سويسرا مع واشنطن التي وصلها نائب الرئيس جي دي فانس في 21 يونيو، لإنهاء حرب لبنان، وفق رويترز.",
             "21 يونيو", "انطلاق محادثات سويسرا", "talks begin",
             [("الوسطاء", "قطر وباكستان"), ("الملف", "حرب لبنان"), ("المصدر", "Reuters")],
             s, "broll_1.jpg", Y),
        beat("ما الذي اتُّفق؟", "خلية لمنع التصعيد في لبنان",
             "اتفق الجانبان على إنشاء «خلية منع تصادم» مع لبنان لوقف العمليات العسكرية، مع رفع حظر صادرات النفط والإفراج عن أصول مجمّدة، وفق وساطة قطر وباكستان.",
             "2", "عدد الدول الوسيطة", "mediator states",
             [("الخلية", "منع تصادم"), ("النفط", "رفع الحظر"), ("المصدر", "قطر وباكستان")],
             s, "broll_2.jpg", B),
        beat("ماذا يعني للعراق؟", "هدوء إقليمي يطمئن بغداد",
             "يقول الرئيس السوري أحمد الشرع إن دمشق لن تقاتل حزب الله لكنها قد تساعد بطرق أخرى، فيما يخفّض الاتفاق مخاطر حرب تهدد استقرار العراق، وفق رويترز.",
             "تهدئة", "خفض مخاطر الحرب الإقليمية", "regional de-escalation",
             [("سوريا", "لن تقاتل حزب الله"), ("الأثر", "استقرار العراق"), ("المصدر", "Reuters")],
             s, "broll_3.jpg", R),
    ],
    "sources": [
        {"name": "Reuters", "domain": "reuters.com"},
        {"name": "Times of Israel", "domain": "timesofisrael.com"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "CNN", "domain": "cnn.com"},
        {"name": "Profile News", "domain": "profilenews.com"},
    ],
    "arabicTicker": [
        "نائب الرئيس الأمريكي جي دي فانس يصل سويسرا في 21 يونيو لمحادثات مع إيران، وفق رويترز",
        "وزير خارجية إيران عباس عراقجي يعلن «تقدماً كبيراً» نحو إنهاء حرب لبنان",
        "اتفاق على «خلية منع تصادم» مع لبنان لوقف العمليات العسكرية بوساطة قطر وباكستان",
        "رفع حظر صادرات النفط الإيرانية والإفراج عن بعض الأصول المجمّدة ضمن التفاهمات",
        "الرئيس السوري أحمد الشرع: دمشق لن تقاتل حزب الله لكنها قد تساعد بطرق أخرى",
        "تهدئة إقليمية تخفّض مخاطر حرب تهدد استقرار العراق والمنطقة",
    ],
}

# ── 3. IRAQ MILITIA DISARMAMENT ──────────────────────────────────────────
s = "iraq-militia-disarmament"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
    "audioBed": "audio/music_03.mp3", "topicBucket": "iraq_domestic", "variant": "A",
    "breaking": {
        "arabicKicker": "العراق",
        "arabicHeadline": "فصائل عراقية تقبل حصر السلاح بالدولة",
        "englishSubhead": "IRAQI FACTIONS PLEDGE ARMS TO STATE CONTROL",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "فصائل تعلن تسليم سلاحها",
             "أعلنت عصائب أهل الحق وكتائب الإمام علي في 2 يونيو قبول حصر السلاح بيد الدولة وفك ارتباطها بالحشد الشعبي، وفق لونغ وور جورنال.",
             "2 يونيو", "إعلان قبول حصر السلاح", "pledge announced",
             [("الفصائل", "عصائب وكتائب الإمام علي"), ("الإطار", "التنسيقي"), ("المصدر", "LWJ")],
             s, "broll_1.jpg", Y),
        beat("لماذا يهم؟", "ضغط أمريكي ومهلة سبتمبر",
             "حدّدت بغداد نهاية سبتمبر موعداً لحصر السلاح وسط ضغط أمريكي على حكومة رئيس الوزراء علي الزيدي الذي التقى وفود الفصائل في 3 يونيو، وفق آراب نيوز.",
             "سبتمبر", "مهلة حصر السلاح", "disarmament deadline",
             [("الضغط", "أمريكي"), ("اللقاء", "3 يونيو"), ("المصدر", "Arab News")],
             s, "broll_2.jpg", B),
        beat("ماذا بعد؟", "فصائل متشددة ترفض المبادرة",
             "رفضت حركة حزب الله النجباء المبادرة، وربطت بغداد حصر السلاح بانسحاب التحالف الدولي بحلول سبتمبر، ما يبقي تطبيقها غير مؤكد، وفق ذا ناشيونال.",
             "رفض", "موقف الفصائل المتشددة", "hardliners refuse",
             [("الرافض", "النجباء"), ("الربط", "انسحاب التحالف"), ("المصدر", "The National")],
             s, "broll_3.jpg", R),
    ],
    "sources": [
        {"name": "Long War Journal", "domain": "longwarjournal.org"},
        {"name": "FDD", "domain": "fdd.org"},
        {"name": "Arab News", "domain": "arabnews.com"},
        {"name": "The National", "domain": "thenationalnews.com"},
        {"name": "Amwaj", "domain": "amwaj.media"},
    ],
    "arabicTicker": [
        "عصائب أهل الحق وكتائب الإمام علي تعلنان في 2 يونيو قبول حصر السلاح بيد الدولة، وفق لونغ وور جورنال",
        "الفصائل تعلن فك ارتباطها بالحشد الشعبي وتشكيل لجنة لآليات التنفيذ",
        "رئيس الوزراء علي الزيدي يلتقي وفود الفصائل في بغداد في 3 يونيو، وفق آراب نيوز",
        "بغداد تحدد نهاية سبتمبر موعداً نهائياً لحصر السلاح وسط ضغط أمريكي",
        "حركة حزب الله النجباء ترفض مبادرة حصر السلاح، وفق ذا ناشيونال",
        "بغداد تربط حصر السلاح بانسحاب التحالف الدولي بحلول سبتمبر",
    ],
}

# ── 4. GCC UNIFIED VISA + RAIL ───────────────────────────────────────────
s = "gcc-grand-tours-visa"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
    "audioBed": "audio/music_04.mp3", "topicBucket": "gulf_regional", "variant": "B",
    "breaking": {
        "arabicKicker": "الخليج",
        "arabicHeadline": "تأشيرة خليجية موحّدة تقترب من الإطلاق",
        "englishSubhead": "GULF LAUNCHES SCHENGEN-STYLE UNIFIED VISA",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "تأشيرة سياحية تجمع ست دول",
             "تطلق دول مجلس التعاون الست تجريبياً «تأشيرة الجولات الكبرى» الموحّدة أواخر 2026، تتيح دخولاً متعدداً برسم 100 إلى 150 دولاراً، وفق ترافل آند تور وورلد.",
             "6", "دول التأشيرة الموحّدة", "states in the visa",
             [("الرسم", "100–150 دولاراً"), ("المدة", "30–90 يوماً"), ("المصدر", "GCC")],
             s, "broll_1.jpg", Y),
        beat("البنية التحتية", "سكة الخليج تتجاوز نصف الإنجاز",
             "بلغ مشروع سكة حديد الخليج بطول 2117 كيلومتراً نحو 50% من الإنجاز، فيما دشّن قطار الاتحاد الإماراتي خدمة الركاب على 900 كيلومتر، وفق تقارير خليجية.",
             "2117 كم", "طول سكة حديد الخليج", "Gulf railway length",
             [("الإنجاز", "نحو 50%"), ("قطار الاتحاد", "900 كم"), ("المصدر", "Etihad Rail")],
             s, "broll_2.jpg", B),
        beat("لماذا يهم؟", "تكامل خليجي يعزّز السياحة",
             "يعيد الطيران الخليجي نحو 85 إلى 90% من طاقته بعد الحرب، وتسعى التأشيرة والسكة لرفع التنقل والسياحة البينية بين دول المجلس، وفق تقارير القطاع.",
             "85–90%", "تعافي طاقة الطيران الخليجي", "aviation recovery",
             [("الهدف", "سياحة بينية"), ("الإطلاق", "أواخر 2026"), ("المصدر", "Gulf News")],
             s, "broll_3.jpg", R),
    ],
    "sources": [
        {"name": "Travel And Tour World", "domain": "travelandtourworld.com"},
        {"name": "Gulf News", "domain": "gulfnews.com"},
        {"name": "Etihad Rail", "domain": "etihadrail.ae"},
        {"name": "Gulf Nashra", "domain": "gulfnashra.com"},
        {"name": "GCC", "domain": "gcc-sg.org"},
    ],
    "arabicTicker": [
        "دول مجلس التعاون الست تطلق تجريبياً «تأشيرة الجولات الكبرى» الموحّدة أواخر 2026، وفق ترافل آند تور وورلد",
        "التأشيرة تتيح دخولاً متعدداً لكل الأعضاء برسم 100 إلى 150 دولاراً ولمدة 30 إلى 90 يوماً",
        "مشروع سكة حديد الخليج بطول 2117 كيلومتراً يبلغ نحو 50% من الإنجاز",
        "قطار الاتحاد الإماراتي يدشّن خدمة الركاب على 900 كيلومتر تربط 11 مدينة",
        "الطيران الخليجي يستعيد نحو 85 إلى 90% من طاقته بعد اضطرابات الحرب",
        "التأشيرة الموحّدة والسكة يعزّزان التنقل والسياحة البينية بين دول المجلس",
    ],
}

# ── 5. PANCREATIC-CANCER ORAL DRUG ───────────────────────────────────────
s = "pancreas-cancer-pill"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
    "audioBed": "audio/music_05.mp3", "topicBucket": "tech_ai", "variant": "B",
    "breaking": {
        "arabicKicker": "صحة",
        "arabicHeadline": "دواء فموي يضاعف بقاء مرضى البنكرياس",
        "englishSubhead": "ORAL RAS DRUG DOUBLES PANCREATIC CANCER SURVIVAL",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "داراكسونراسيب يضاعف البقاء",
             "أظهرت تجربة المرحلة الثالثة «راسوليوت 302» أن دواء داراكسونراسيب الفموي رفع متوسط البقاء إلى 13.2 شهراً مقابل 6.7 للعلاج الكيميائي، وفق نيو إنغلاند جورنال.",
             "13.2 شهراً", "متوسط البقاء مع الدواء", "median survival on drug",
             [("الكيميائي", "6.7 شهراً"), ("نسبة الخطر", "0.40"), ("المصدر", "NEJM")],
             s, "broll_1.jpg", Y),
        beat("لماذا يهم؟", "أول مثبّط راس في تجربة كبرى",
             "هو أول مثبّط لبروتين «راس» يُختبر في تجربة عشوائية واسعة لسرطان البنكرياس، أحد أشرس السرطانات، ويؤخذ حبّة فموية مرة يومياً، وفق معهد دانا-فاربر.",
             "p<0.0001", "الدلالة الإحصائية للنتيجة", "statistical significance",
             [("النوع", "غدّي مع طفرة راس"), ("الجرعة", "حبة يومياً"), ("المصدر", "Dana-Farber")],
             s, "broll_2.jpg", B),
        beat("ماذا بعد؟", "أمل جديد لسرطان عصيّ",
             "نُشرت النتائج في مؤتمر «آسكو» 31 مايو وفي نيو إنغلاند جورنال، وتفتح الباب لعلاجات راس الفموية في سرطانات أخرى، وفق ريفولوشن ميديسنز.",
             "31 مايو 2026", "إعلان نتائج مؤتمر آسكو", "ASCO presentation",
             [("النشر", "NEJM"), ("الأفق", "سرطانات أخرى"), ("المصدر", "Rev Medicines")],
             s, "broll_3.jpg", R),
    ],
    "sources": [
        {"name": "NEJM", "domain": "nejm.org"},
        {"name": "Dana-Farber", "domain": "dana-farber.org"},
        {"name": "Revolution Medicines", "domain": "revmed.com"},
        {"name": "OncLive", "domain": "onclive.com"},
        {"name": "ASCO", "domain": "asco.org"},
    ],
    "arabicTicker": [
        "تجربة المرحلة الثالثة «راسوليوت 302» تظهر مضاعفة البقاء مع داراكسونراسيب الفموي، وفق نيو إنغلاند جورنال",
        "متوسط البقاء 13.2 شهراً مع الدواء مقابل 6.7 شهراً للعلاج الكيميائي ونسبة خطر 0.40",
        "أول مثبّط لبروتين «راس» يُختبر في تجربة عشوائية واسعة لسرطان البنكرياس، وفق دانا-فاربر",
        "الدواء يؤخذ حبّة فموية مرة واحدة يومياً في سرطان غدّي حامل لطفرة راس",
        "النتائج عُرضت في مؤتمر آسكو 31 مايو ونُشرت في نيو إنغلاند جورنال",
        "النتائج تفتح الباب لعلاجات راس الفموية في سرطانات أخرى، وفق ريفولوشن ميديسنز",
    ],
}

# ── 6. CLIMATE-RESILIENT CORAL REEFS ─────────────────────────────────────
s = "coral-resilient-reefs"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
    "audioBed": "audio/music_06.mp3", "topicBucket": "wildcard", "variant": "C",
    "breaking": {
        "arabicKicker": "بيئة",
        "arabicHeadline": "خريطة عالمية للشعاب المرجانية الصامدة",
        "englishSubhead": "SCIENTISTS MAP CLIMATE-RESILIENT CORAL REEFS",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "علماء يرسمون الشعاب الصامدة",
             "حدّد باحثون من جمعية حفظ الحياة البرية وجامعة ماكواري شعاباً قادرة على التعافي من الاحترار تمتد على 165,922 كيلومتراً مربعاً في 71 دولة، وفق دراسة جديدة.",
             "165,922 كم²", "مساحة الشعاب الصامدة", "resilient reef area",
             [("الدول", "71"), ("التقدير", "3 أضعاف السابق"), ("المصدر", "WCS")],
             s, "broll_1.jpg", Y),
        beat("لماذا يهم؟", "ابيضاض ضرب 84% من الشعاب",
             "بين 2023 و2025 ضرب الإجهاد الحراري نحو 84% من مساحة الشعاب في 83 دولة، في رابع ابيضاض جماعي مسجَّل، ما يجعل الملاذات الصامدة بالغة الأهمية، وفق الدراسة.",
             "84%", "نسبة الشعاب المتضررة", "reefs hit by bleaching",
             [("الفترة", "2023–2025"), ("الدول", "83"), ("الترتيب", "رابع ابيضاض")],
             s, "broll_2.jpg", B),
        beat("ماذا بعد؟", "ملاذات للحفظ ونينيو يلوح",
             "تتركّز 61% من الملاذات الصامدة في خمس دول، وتقترح الدراسة توجيه الحماية إليها مع تطوّر ظاهرة النينيو المتوقع، وفق الإدارة الوطنية للمحيطات.",
             "61%", "تركّز الملاذات بخمس دول", "refuges in five states",
             [("الحماية", "موجَّهة"), ("النينيو", "متوقع يشتد"), ("المصدر", "NOAA")],
             s, "broll_3.jpg", R),
    ],
    "sources": [
        {"name": "Wildlife Conservation Society", "domain": "wcs.org"},
        {"name": "Macquarie University", "domain": "mq.edu.au"},
        {"name": "CBC", "domain": "cbc.ca"},
        {"name": "NOAA", "domain": "noaa.gov"},
        {"name": "Earth.org", "domain": "earth.org"},
    ],
    "arabicTicker": [
        "باحثون من جمعية حفظ الحياة البرية وجامعة ماكواري يرسمون خريطة الشعاب المرجانية الصامدة للحرارة، وفق دراسة جديدة",
        "الشعاب القادرة على التعافي تمتد على 165,922 كيلومتراً مربعاً في 71 دولة، ثلاثة أضعاف التقديرات السابقة",
        "بين 2023 و2025 ضرب الإجهاد الحراري نحو 84% من مساحة الشعاب في 83 دولة",
        "هذا رابع ابيضاض جماعي مسجَّل للشعاب المرجانية في العالم",
        "61% من الملاذات الصامدة تتركّز في خمس دول وتقترح الدراسة توجيه الحماية إليها",
        "الإدارة الوطنية للمحيطات تتوقع اشتداد ظاهرة النينيو ما يزيد الإجهاد الحراري",
    ],
}

# ── WRITE ────────────────────────────────────────────────────────────────
def wc(t):
    return len(t.split())


for slug, props in SLATE.items():
    d = ROOT / f"{DATE}-{slug}" / ".meta"
    d.mkdir(parents=True, exist_ok=True)
    (d / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
    # quick length audit
    hw = wc(props["breaking"]["arabicHeadline"])
    flags = []
    if hw > 8:
        flags.append(f"HEADLINE {hw}w")
    for i, b in enumerate(props["beats"]):
        if wc(b["arabicHeading"]) > 8:
            flags.append(f"beat{i} heading {wc(b['arabicHeading'])}w")
        if wc(b["arabicBody"]) > 26:
            flags.append(f"beat{i} body {wc(b['arabicBody'])}w")
    print(f"✓ {DATE}-{slug}  bucket={props['topicBucket']} var={props['variant']}  {'⚠ '+'; '.join(flags) if flags else 'ok'}")

print(f"\n{len(SLATE)} props written")
