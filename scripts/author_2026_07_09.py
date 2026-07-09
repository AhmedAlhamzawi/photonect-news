#!/usr/bin/env python3
"""Author the 5 props.json for the 2026-07-09 Photonect NEWS slate (V10.1 engine).

Pillar mix 2 P1 / 2 P2 / 1 P3 (فلوس وسلطة العراق والمنطقة). Posting order = alphabetical
by slug → P3 · P1 · P2 · P1 · P2 (no two consecutive same pillar).

  american-hospital     P3  wildcard (health+money)   var C
  electricity-graft     P1  iraq_domestic             var A
  iran-deal-collapse    P2  mena_geopolitics          var A
  land-plots-million    P1  iraq_domestic             var B
  washington-dollar     P2  mena_geopolitics          var B

Every number attributed, Western numerals, no Persian yeh/kaf. Drafts here get an
Opus iraqi-copywriter polish pass before render.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-09"
DL, ADL, HANDLE = "JUL 9 • 2026", "9 يوليو 2026", "@photonect.news"
ACC = ["#FFC217", "#FF6B3D", "#D72638"]


def img(slug, f):
    return f"images/news/{DATE}-{slug}/{f}"


def beat(label, heading, body, bigv, bigl, bigal, stats, slug, bfile, acc, src):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": bigv, "label": bigl, "arabicLabel": bigal},
        "supportingStats": [{"label": l, "value": v} for l, v in stats],
        "broll": img(slug, bfile),
        "brolls": [img(slug, bfile)],
        "brollType": "image",
        "accent": acc,
        "brollSource": src,
    }


SLATE = {}

# ── 1 · american-hospital (P3 · wildcard · C) ──────────────────────────────
s = "american-hospital"
SLATE[s] = {
    "dateLabel": DL, "arabicDateLabel": ADL, "handle": HANDLE,
    "audioBed": "audio/music_05.mp3", "topicBucket": "wildcard", "variant": "C",
    "breaking": {
        "arabicKicker": "صحة · فلوس",
        "arabicHeadline": "تدفع لعلاجك برّه العراق؟",
        "englishSubhead": "200,000+ IRAQIS TREATED ABROAD YEARLY • UP TO $1B SPENT • A U.S.-BACKED HOSPITAL TO KEEP IT HOME",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "مستشفى أمريكي داخل العراق",
             "وزارة التجارة تبحث مع شركة American Medical Services نموذج استثمار لبناء مستشفى أمريكي متطور داخل العراق، وفق العراق نيوز.",
             "200,000+", "Iraqis treated abroad / yr", "عراقي يسافر للعلاج خارج البلد سنوياً (شفق)",
             [("يغادرون سنوياً", "200 ألف+"), ("الوجهة الأولى", "الهند"), ("الكلفة", "~مليار$")],
             s, "broll_1.jpg", ACC[0], "Iraqi News · Shafaq · 2026"),
        beat("لماذا يهم؟", "مليار دولار يخرج للعلاج",
             "لجنة الصحة النيابية تقدّر إنفاق العراقيين على العلاج بالخارج بين 750 مليوناً ومليار دولار سنوياً، تذهب للهند والأردن وتركيا، وفق المونيتور.",
             "$750م–1مليار", "Spent on medical travel / yr", "ما ينفقه العراقيون سنوياً على العلاج خارج البلد (لجنة الصحة النيابية)",
             [("سنوياً", "750م–1مليار$"), ("الأردن", "10,000$ للركبة"), ("الثقة", "متدنية")],
             s, "broll_2.jpg", ACC[1], "Al-Monitor · لجنة الصحة النيابية · 2026"),
        beat("ماذا بعد؟", "هل يعود المال إلى الداخل؟",
             "الحكومة تدفع لإنهاء رحلات العلاج بالخارج عبر استثمار أجنبي ومستشفيات متقدمة توفّر المال وتخلق وظائف طبية، وفق شفق.",
             "الهدف", "Keep spend + jobs home", "إبقاء إنفاق العلاج داخل العراق وخلق وظائف طبية (شفق)",
             [("الاستثمار", "أمريكي"), ("المستشفى", "متطور"), ("المكسب", "مال ووظائف")],
             s, "broll_3.jpg", ACC[2], "Shafaq · Iraqi News · 2026"),
    ],
    "sources": [
        {"name": "Iraqi News", "domain": "iraqinews.com"},
        {"name": "Al-Monitor", "domain": "al-monitor.com"},
        {"name": "Shafaq News", "domain": "shafaq.com"},
        {"name": "Parliament Health Committee", "domain": "parliament.iq"},
    ],
    "arabicTicker": [
        "تدفع لعلاجك برّه العراق؟",
        "أكثر من 200 ألف عراقي يسافرون للعلاج خارج البلد سنوياً (شفق)",
        "إنفاق العراقيين على العلاج بالخارج 750 مليوناً إلى مليار دولار (لجنة الصحة النيابية)",
        "وزارة التجارة تبحث استثماراً أمريكياً لبناء مستشفى متطور داخل العراق (العراق نيوز)",
        "الحكومة تسعى لإنهاء رحلات العلاج بالخارج وإبقاء المال داخل البلد (شفق)",
        "هل يكفي مستشفى واحد لإعادة الثقة بالطب العراقي؟",
    ],
}

# ── 2 · electricity-graft (P1 · iraq_domestic · A) ─────────────────────────
s = "electricity-graft"
SLATE[s] = {
    "dateLabel": DL, "arabicDateLabel": ADL, "handle": HANDLE,
    "audioBed": "audio/music_01.mp3", "topicBucket": "iraq_domestic", "variant": "A",
    "breaking": {
        "arabicKicker": "كهرباء · فساد",
        "arabicHeadline": "كهرباؤك تنطفي وفلوسها تروح؟",
        "englishSubhead": "28 ELECTRICITY OFFICIALS SACKED • ~19B DINAR MISSING FROM COLLECTIONS • DAWN CRACKDOWN HITS THE GRID",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "إقالة 28 مسؤولاً بالكهرباء",
             "الحكومة تقيل 28 مسؤولاً كبيراً في وزارة الكهرباء بينهم مدراء عامون في البصرة وذي قار على خلفية شبهات فساد، وفق شفق.",
             "28", "Officials dismissed", "مسؤولاً كبيراً أُقيلوا من وزارة الكهرباء (شفق)",
             [("المحافظات", "البصرة وذي قار"), ("الرتب", "مدراء عامون"), ("الحملة", "صولة الفجر")],
             s, "broll_1.jpg", ACC[0], "Shafaq · Middle East Online · 2026"),
        beat("لماذا يهم؟", "19 ملياراً اختفت من الجباية",
             "لجان تحقيق كشفت جباية كهرباء تفوق 67 مليار دينار وفجوة نحو 19 ملياراً بين الإيراد المسجّل والمُحصّل فعلاً، وفق شفق.",
             "~19 مليار", "Dinar missing", "فجوة بين الإيراد المسجّل والمُحصّل في جباية الكهرباء (شفق)",
             [("الجباية", "67 مليار+ دينار"), ("الفجوة", "~19 مليار"), ("القطاع", "جنوب العراق")],
             s, "broll_2.jpg", ACC[1], "Shafaq · 2026"),
        beat("ماذا بعد؟", "صولة الفجر تصل للشبكة",
             "منذ 28 حزيران أوقفت الحملة عشرات المسؤولين ويُتوقع أن تطال أكثر من 200 شخصية، والطاقة بين القطاعات ذات الأولوية للتحقيق، وفق الجزيرة.",
             "200+", "Figures targeted", "شخصية يُتوقع أن تطالها حملة صولة الفجر (الجزيرة)",
             [("انطلقت", "28 حزيران"), ("أُوقِف", "عشرات"), ("الأولوية", "الطاقة")],
             s, "broll_3.jpg", ACC[2], "Al Jazeera · Shafaq · 2026"),
    ],
    "sources": [
        {"name": "Shafaq News", "domain": "shafaq.com"},
        {"name": "Middle East Online", "domain": "middle-east-online.com"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "Government of Iraq", "domain": "pmo.iq"},
    ],
    "arabicTicker": [
        "كهرباؤك تنطفي وفلوسها تروح؟",
        "إقالة 28 مسؤولاً كبيراً في وزارة الكهرباء على خلفية شبهات فساد (شفق)",
        "فجوة نحو 19 مليار دينار بين الإيراد المسجّل والمُحصّل في جباية الكهرباء (شفق)",
        "حملة صولة الفجر انطلقت في 28 حزيران وتطال قطاع الطاقة (الجزيرة)",
        "يُتوقع أن تصل الحملة إلى أكثر من 200 شخصية في الدولة (الجزيرة)",
        "هل يصلح ملاحقة الفساد ساعات الكهرباء في بيتك؟",
    ],
}

# ── 3 · iran-deal-collapse (P2 · mena_geopolitics · A) ─────────────────────
s = "iran-deal-collapse"
SLATE[s] = {
    "dateLabel": DL, "arabicDateLabel": ADL, "handle": HANDLE,
    "audioBed": "audio/music_03.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
    "breaking": {
        "arabicKicker": "نفط · مضيق هرمز",
        "arabicHeadline": "الاتفاق انتهى... نفط العراق يمرّ؟",
        "englishSubhead": "TRUMP ENDS IRAN TRUCE • OIL WAIVER REVOKED • HORMUZ UNDER FIRE — IRAQ'S EXPORT LIFELINE AT RISK",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "ترامب يعلن انتهاء الاتفاق",
             "بعد ضربات متبادلة أعلن ترامب أن الاتفاق المؤقت مع إيران «انتهى»، وواشنطن ألغت إعفاءً كان يسمح ببيع النفط الإيراني، وفق ذا هيل.",
             "«انتهى»", "Trump on the truce", "ترامب: الاتفاق المؤقت مع إيران انتهى بعد الضربات (ذا هيل)",
             [("الإعفاء", "أُلغي"), ("بعد", "7 تموز"), ("الضربات", "متبادلة")],
             s, "broll_1.jpg", ACC[0], "The Hill · 2026"),
        beat("لماذا يهم؟", "هرمز تحت النار",
             "طهران متّهمة بمهاجمة ثلاث سفن تجارية قرب مضيق هرمز، ونحو 6,000 بحّار عالقون في الخليج، والمنظمة البحرية الدولية تدين، وفق الجزيرة.",
             "~6,000", "Seafarers stranded", "بحّار عالقون في الخليج مع تصاعد الهجمات على السفن (الجزيرة · IMO)",
             [("السفن", "3 تجارية"), ("هرمز", "مهدَّد"), ("IMO", "يدين")],
             s, "broll_2.jpg", ACC[1], "Al Jazeera · IMO · 2026"),
        beat("لماذا يهم العراق؟", "90% من إيرادك عبر البصرة",
             "نحو 90% من إيراد العراق نفط يخرج غالبه من البصرة قرب هرمز، فأي تعطّل شحن يهدد الرواتب، ويبقى خطّا جيهان وسوريا بديلاً، وفق بلومبرغ.",
             "~90%", "Iraq revenue from oil", "حصة النفط من إيراد الدولة العراقية المعرّض لممر هرمز (بلومبرغ)",
             [("المنفذ", "البصرة"), ("البديل", "جيهان/سوريا"), ("الخطر", "الرواتب")],
             s, "broll_3.jpg", ACC[2], "Bloomberg · CNN · 2026"),
    ],
    "sources": [
        {"name": "The Hill", "domain": "thehill.com"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "Bloomberg", "domain": "bloomberg.com"},
        {"name": "CNN", "domain": "cnn.com"},
    ],
    "arabicTicker": [
        "الاتفاق انتهى... نفط العراق يمرّ؟",
        "ترامب يعلن أن الاتفاق المؤقت مع إيران انتهى بعد ضربات متبادلة (ذا هيل)",
        "واشنطن تلغي إعفاءً كان يسمح ببيع النفط الإيراني اعتباراً من 7 تموز (ذا هيل)",
        "نحو 6,000 بحّار عالقون مع هجمات على السفن قرب مضيق هرمز (الجزيرة · IMO)",
        "نحو 90% من إيراد العراق نفط يخرج غالبه عبر البصرة قرب هرمز (بلومبرغ)",
        "هل يصمد ممر نفطك إذا اشتعل مضيق هرمز؟",
    ],
}

# ── 4 · land-plots-million (P1 · iraq_domestic · B) ────────────────────────
s = "land-plots-million"
SLATE[s] = {
    "dateLabel": DL, "arabicDateLabel": ADL, "handle": HANDLE,
    "audioBed": "audio/music_04.mp3", "topicBucket": "iraq_domestic", "variant": "B",
    "breaking": {
        "arabicKicker": "سكن · أراضٍ",
        "arabicHeadline": "مليون قطعة أرض... حصتك وين؟",
        "englishSubhead": "1M SERVICED PLOTS NATIONWIDE • SHARED BY POPULATION + POVERTY • KURDISTAN EXCLUDED",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "مليون قطعة أرض سكنية",
             "مجلس الوزراء يقرّ مشروع مليون قطعة أرض مخدومة بالبنى التحتية توزَّع على المحافظات عدا الإقليم للمواطنين المستحقين، وفق العراق نيوز.",
             "1,000,000", "Serviced plots", "قطعة أرض سكنية مخدومة ضمن المشروع الوطني (العراق نيوز)",
             [("مخدومة", "ببنى تحتية"), ("تشمل", "كل المحافظات"), ("تستثني", "الإقليم")],
             s, "broll_1.jpg", ACC[0], "Iraqi News · 2026"),
        beat("لماذا يهم؟", "التوزيع بالسكان والفقر",
             "الزيدي يقرّ 11 قراراً في جلسة 6 تموز، والتوزيع يُحدَّد بحجم السكان ونسب الفقر لضمان أوسع استفادة ممكنة، وفق وكالة الأنباء العراقية.",
             "11", "Decrees approved", "قراراً تنموياً أقرّها الزيدي في جلسة التنسيق بين المحافظات (INA)",
             [("المعيار", "عدد السكان"), ("ثم", "نسب الفقر"), ("التاريخ", "6 تموز")],
             s, "broll_2.jpg", ACC[1], "INA · 2026"),
        beat("ماذا بعد؟", "الأولوية للسجناء السياسيين",
             "الجلسة خصّصت أراضي لمشمولي مؤسسة السجناء السياسيين وربما نازحين إيزيديين، وسط جدل حول عدالة توزيع الأرض، وفق شفق.",
             "الأولوية", "Political-prisoner families", "تخصيص أراضٍ لمشمولي مؤسسة السجناء السياسيين ضمن الأولويات (شفق)",
             [("مشمولون", "السجناء السياسيون"), ("وربما", "نازحون إيزيديون"), ("المطلب", "عدالة التوزيع")],
             s, "broll_3.jpg", ACC[2], "Shafaq · 2026"),
    ],
    "sources": [
        {"name": "Iraqi News", "domain": "iraqinews.com"},
        {"name": "Iraqi News Agency", "domain": "ina.iq"},
        {"name": "Shafaq News", "domain": "shafaq.com"},
        {"name": "Council of Ministers", "domain": "cabinet.iq"},
    ],
    "arabicTicker": [
        "مليون قطعة أرض... حصتك وين؟",
        "مجلس الوزراء يقرّ مشروع مليون قطعة أرض سكنية مخدومة (العراق نيوز)",
        "التوزيع بين المحافظات بحجم السكان ونسب الفقر عدا الإقليم (INA)",
        "الزيدي يقرّ 11 قراراً تنموياً في جلسة 6 تموز (وكالة الأنباء العراقية)",
        "أولوية أراضٍ لمشمولي مؤسسة السجناء السياسيين وربما نازحين إيزيديين (شفق)",
        "هل تصل الأرض لمن يستحقها فعلاً؟",
    ],
}

# ── 5 · washington-dollar (P2 · mena_geopolitics · B) ──────────────────────
s = "washington-dollar"
SLATE[s] = {
    "dateLabel": DL, "arabicDateLabel": ADL, "handle": HANDLE,
    "audioBed": "audio/music_06.mp3", "topicBucket": "mena_geopolitics", "variant": "B",
    "breaking": {
        "arabicKicker": "العراق · واشنطن",
        "arabicHeadline": "الزيدي عند ترامب... فلوس ووظائف؟",
        "englishSubhead": "FIRST U.S. TRIP • ENERGY + INFRA INVESTMENT • $10B PRIVATE-SECTOR FUND • WEAPONS UNDER STATE CONTROL",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat("ماذا يحدث؟", "أول زيارة رسمية لواشنطن",
             "رئيس الوزراء علي الزيدي يزور واشنطن في تموز يرافقه وفد أعمال عراقي، سعياً لاستثمار أمريكي في الطاقة والبنى التحتية، وفق ذا ناشيونال.",
             "أول", "High-level U.S. visit", "أول زيارة رفيعة لرئيس وزراء عراقي إلى واشنطن (ذا ناشيونال)",
             [("الوفد", "رجال أعمال"), ("الهدف", "استثمار"), ("القطاع", "طاقة وبنى تحتية")],
             s, "broll_1.jpg", ACC[0], "The National · 2026"),
        beat("لماذا يهم؟", "10 مليارات لصندوق القطاع الخاص",
             "التركيز على التعاون الاقتصادي، وصندوق تنمية للقطاع الخاص يضخّ فيه البنك المركزي 10 مليارات دولار لخلق وظائف وتقليل الاعتماد على النفط، وفق ذا ناشيونال.",
             "10 مليار$", "CBI private-sector fund", "مساهمة البنك المركزي في صندوق تنمية القطاع الخاص (ذا ناشيونال)",
             [("المصدر", "البنك المركزي"), ("الهدف", "وظائف"), ("يقلّل", "الاعتماد على النفط")],
             s, "broll_2.jpg", ACC[1], "The National · Jerusalem Post · 2026"),
        beat("ماذا بعد؟", "السلاح بيد الدولة شرط",
             "ملف حصر السلاح بيد الدولة على طاولة البيت الأبيض، والزيدي يستكمل حكومته قبل القمة ثم يزور تركيا وإيران والسعودية، وفق الأسبوع العربي.",
             "حصر السلاح", "On the White House table", "حصر السلاح بيد الدولة أحد ملفّي قمة البيت الأبيض (الأسبوع العربي)",
             [("الملف الثاني", "اقتصاد"), ("بعدها", "تركيا/إيران/السعودية"), ("قبل القمة", "استكمال الحكومة")],
             s, "broll_3.jpg", ACC[2], "The Arab Weekly · 2026"),
    ],
    "sources": [
        {"name": "The National", "domain": "thenationalnews.com"},
        {"name": "Jerusalem Post", "domain": "jpost.com"},
        {"name": "The Arab Weekly", "domain": "thearabweekly.com"},
        {"name": "Iraqi News", "domain": "iraqinews.com"},
    ],
    "arabicTicker": [
        "الزيدي عند ترامب... فلوس ووظائف؟",
        "أول زيارة رفيعة لرئيس وزراء عراقي إلى واشنطن مع وفد أعمال (ذا ناشيونال)",
        "صندوق تنمية للقطاع الخاص يضخّ فيه البنك المركزي 10 مليارات دولار (ذا ناشيونال)",
        "التركيز على استثمار أمريكي في الطاقة والبنى التحتية وخلق وظائف (ذا ناشيونال)",
        "حصر السلاح بيد الدولة أحد ملفّي قمة البيت الأبيض (الأسبوع العربي)",
        "هل تتحوّل الزيارة إلى وظائف واستثمار على الأرض؟",
    ],
}


def main():
    for slug, props in SLATE.items():
        d = POSTS / f"{DATE}-{slug}" / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  wrote {DATE}-{slug}/.meta/props.json  ({len(props['beats'])} beats)")
    print(f"\n== authored {len(SLATE)} slugs ==")


if __name__ == "__main__":
    main()
