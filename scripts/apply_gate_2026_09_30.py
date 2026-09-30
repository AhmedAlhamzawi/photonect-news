#!/usr/bin/env python3
"""Apply Opus gate pass-1 findings (2026-09-30): 3 blockers (b computed gap airing, c 2nd caption question,
e one-sided dispute pairing) + warnings. Exact-string replacements; asserts each target exists."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
FIX = [
 ("a-gold-5kg-land-registry", [".meta/v11-brief.json"], "إذ نقلته شقيقتها", "الذي نقلته شقيقتها"),
 ("a-gold-5kg-land-registry", [".meta/v11-brief.json"], "سند عقار ضُبط في آب", "عقاراً ضُبطت سنداته في آب"),
 ("a-gold-5kg-land-registry", [".meta/v11-brief.json"], "والقضية ما زالت قيد التحقيق.", "والقضية قيد التحقيق، والكلمة الأخيرة للقضاء."),
 ("b-dollar-157250-third-rise", [".meta/v11-brief.json"], "والشراء أقل بألف دينار.", "وسجّل الشراء مئة وستة وخمسين ألفاً وسبعمئة وخمسين."),
 ("b-dollar-157250-third-rise", [".meta/v11-brief.json"], "فقفز مثقال عيار واحد وعشرين الخليجي والتركي والأوروبي في جملة شارع النهر", "فارتفع مثقال الذهب الخليجي والتركي والأوروبي عيار واحد وعشرين في جملة شارع النهر"),
 ("b-dollar-157250-third-rise", [".meta/v11-brief.json"], "الدولار يواصل.. والذهب يقفز", "الدولار يواصل.. والذهب يرتفع"),
 ("b-dollar-157250-third-rise", [".meta/v11-brief.json", ".meta/props.json", "caption.txt"], "عندك ذهب محفوظ بالبيت؟", "تحفظ فلوسك ذهب لو دولار؟"),
 ("c-coalition-mission-ends", ["caption.txt"], "انتهاء مهمة التحالف الدولي في العراق رسمياً — شنو يتغير بعد اليوم؟", "انتهاء مهمة التحالف الدولي في العراق رسمياً — والصدر يحل «اليوم الموعود»"),
 ("c-coalition-mission-ends", [".meta/v11-brief.json"], "على اكتمال تسليم السلاح بحلول نهاية حزيران", "على اكتمال تسليم سلاح الفصائل بحلول نهاية حزيران"),
 ("c-coalition-mission-ends", ["caption.txt"], "البنتاغون حدد أربيل كآخر محطة", "البنتاغون: الانسحاب من قاعدة أربيل يختم المهمة"),
 ("d-watan-275000-plots", [".meta/v11-brief.json"], "قطعة أرض؟ التسجيل الشهر الجاي", "الزيدي يوجّه: رابط الأراضي الشهر الجاي"),
 ("d-watan-275000-plots", ["caption.txt"], "مبادرة وطن لقطع الأراضي السكنية: رابط التسجيل خلال الشهر المقبل", "مبادرة وطن لقطع الأراضي السكنية: توجيه بإطلاق رابط التسجيل الشهر المقبل"),
 ("d-watan-275000-plots", [".meta/v11-brief.json"], "مع حجر أساس في أول محافظة خلال الأيام المقبلة.", "على أن يوضع حجر الأساس في أول محافظة خلال الأيام المقبلة."),
 ("e-ali-ammar-219kg", [".meta/props.json"], "بحسب اللجنة الأولمبية العراقية، عرض المنظمون العلم الإيراني وشغّلوا العدّ ثم بدّلوه بالعراقي، فلم يكفِ الوقت لمحاولته الأخيرة. وعمار لرويترز: «لو عندي 10 ثوانٍ إضافية».", "بحسب اللجنة الأولمبية العراقية، بدأ العدّ تحت العلم الإيراني ثم تبدّل. وقال عمار لرويترز إنه ظنّ أن لديه دقيقتين: «لو عندي 10 ثوانٍ إضافية»."),
 ("e-ali-ammar-219kg", [".meta/props.json"], "البرونزية للبحريني غور ميناسيان (رويترز، شفق نيوز).", "البرونزية للبحريني غور ميناسيان بحسب شفق نيوز."),
 ("e-ali-ammar-219kg", [".meta/props.json", "caption.txt"], "علي عمار يكسر الرقم العالمي بالخطف.. والذهب يفلت بكيلو واحد", "علي عمار يسجّل رقماً عالمياً بالخطف.. والذهب يفلت بكيلو واحد"),
]
bad = 0
for slug, files, old, new in FIX:
    hit = 0
    for f in files:
        p = P / f"2026-09-30-{slug}" / f
        s = p.read_text(encoding="utf-8")
        if old in s:
            p.write_text(s.replace(old, new), encoding="utf-8"); hit += 1
    print(("OK  " if hit else "MISS"), slug, old[:50]); bad += (hit == 0)
raise SystemExit(bad)
