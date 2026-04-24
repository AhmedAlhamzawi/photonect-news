# Photonect NEWS — Posting Queue for 2026-04-17

**6 production-ready NewsReel videos** across **3 topic buckets** (mena_geopolitics × 4, tech_ai × 1, iraq_domestic × 1). All 30s vertical (1080×1920), Arabic-first, with 6+ real sources each. Ready to post.

**Latest autonomous session (23:30 GMT+3):**
- Hormuz re-rendered as `newsreel_v3.mp4` with map LTR fix (IRAN on left, OMAN-UAE on right — architectural fix in `Beat.tsx:111`)
- Lebanon + Flight props now include `mapOverlay` → new `LebanonMap` + `FlightEuropeMap` components unlocked (previously only hormuz supported). Fix lives in [HormuzMap.tsx](../Claude%20%3C%3E%20Ahmed%20-%202nd%20Brain/Photonect/my-video/src/compositions/NewsReel/scenes/maps/HormuzMap.tsx) — all future reels can reference these overlays.
- **New reels produced:** `2026-04-17-ai-hundred-billion` (AI's $100B Week — Anthropic/CoreWeave/ASML/Gemini) and `2026-04-17-iraq-blackout` (Iranian gas collapse / electricity crisis)
- Helper scripts added: [data/_template/new-reel.sh](data/_template/new-reel.sh), [queue-status.sh](data/_template/queue-status.sh), [render-reel.sh](data/_template/render-reel.sh)

---

## Suggested Posting Cadence (2h intervals — 6 slots across the prime Arabic audience window)

The six videos form a deliberate arc that respects the **topic-diversity mandate** (no two consecutive posts from the same bucket) and the **escalation-then-relief** rhythm:

| Slot | GMT+3 | Video | Bucket | Angle |
|------|-------|-------|--------|-------|
| 1 | 12:00 | **Hormuz Week 2** | mena_geopolitics | Ship spoofing — the hook that started it all |
| 2 | 14:00 | **Iraq Blackout** | iraq_domestic | Iranian gas collapse — the home-front consequence |
| 3 | 16:00 | **Iran-US Talks** | mena_geopolitics | 100 hours to deadline — the clock |
| 4 | 18:00 | **AI $100B Week** | tech_ai | Palate cleanser — zoom out to Silicon Valley |
| 5 | 20:00 | **Lebanon Ceasefire** | mena_geopolitics | Netanyahu-Aoun Thursday call — human cost |
| 6 | 22:00 | **Flight Aftermath** | mena_geopolitics | How the war cancels your vacation — consumer angle |

Rationale: slots 1/3/5/6 carry the Iran-war throughline; slots 2 and 4 are deliberate breaks (domestic Iraq / global tech) so the feed never feels like a single-topic drumbeat. If you prefer tighter thematic flow, drop slot 4 (AI) and post slots 1-2-3-5-6 on the old 2h grid.

---

## 1. Hormuz Week 2 — Ship Spoofing

**Video:** `data/posts/2026-04-17-hormuz-week2/newsreel_v3.mp4` (38 MB) — v3 has Hormuz map LTR fix (IRAN on left, OMAN-UAE on right)
**Caption:** `data/posts/2026-04-17-hormuz-week2/caption.txt`
**Arabic headline:** سفن تُزيّف هويتها لاختراق الحصار الأمريكي في هرمز
**English subhead:** HORMUZ BLOCKADE • WEEK 2
**Big stats:** Day 4 of blockade • +34% jet fuel • 72h decisive window
**Sources:** NPR, Al Jazeera, BBC, CBS, ABC, Fortune
**Why it leads:** Concrete, visual story ("12+ vessels spoofing AIS") with USS Tripoli footage. Sets geopolitical stage for the three follow-ups.

---

## 2. Iran-US Talks — 100 Hours to Deadline

**Video:** `data/posts/2026-04-17-iran-talks/newsreel.mp4` (28 MB)
**Caption:** `data/posts/2026-04-17-iran-talks/caption.txt`
**Arabic headline:** ١٠٠ ساعة تفصل واشنطن وطهران عن نقطة اللاعودة
**English subhead:** US–IRAN TALKS • 100h TO DEADLINE
**Big stats:** APR 21 (deadline) • +34% jet fuel • 100h (clock)
**Sources:** Al Jazeera, CNN, Foreign Policy, Insurance Journal, NY Post, The Atlantic
**Why it follows Hormuz:** The blockade creates the pressure; this is the diplomatic countdown. Pakistani mediation angle is fresh.

---

## 3. Lebanon Ceasefire Push — Thursday Call

**Video:** `data/posts/2026-04-17-lebanon-ceasefire/newsreel.mp4` (50 MB)
**Caption:** `data/posts/2026-04-17-lebanon-ceasefire/caption.txt`
**Arabic headline:** الخميس الحاسم: نتنياهو يتّصل بعون بعد قصف عنيف لبنت جبيل
**English subhead:** LEBANON–ISRAEL • CEASEFIRE WEEK
**Big stats:** 70 Hezbollah sites hit • 1,953 Lebanese killed • This week (decisive)
**Sources:** AP, Al Jazeera, NY Post, Reuters, BBC, Israel National News
**Why it follows Iran-talks:** Human-cost angle (4 medics killed, buffer zone dispute). Gives the geopolitical story a face.

---

## 4. Flight Aftermath — How the War Cancels Your Vacation

**Video:** `data/posts/2026-04-17-flight-aftermath/newsreel_v3.mp4` — v3 includes new FlightEuropeMap overlay on beat 3 (6 airports × jet-fuel arrow)
**Caption:** `data/posts/2026-04-17-flight-aftermath/caption.txt`
**Arabic headline:** الحرب تُلغي رحلتك: أوروبا على حافة شلل طيران كامل
**English subhead:** AFTERMATH • FLIGHT CHAOS AHEAD
**Big stats:** +34% jet fuel spike • $140+ Brent • 7 days decisive
**Sources:** The American Prospect, Times of India, Foreign Policy, Fortune, Insurance Journal, Reuters
**Why it closes:** "What does this mean for YOU?" — highest-converting angle. Tourists, flights, ticket prices. Universal relatability.

---

## 5. AI's $100B Week — Anthropic / Meta / ASML / Gemini

**Topic bucket:** `tech_ai` (breaks out of MENA rotation — satisfies topic-diversity mandate)
**Video:** `data/posts/2026-04-17-ai-hundred-billion/newsreel.mp4` (26 MB)
**Caption:** `data/posts/2026-04-17-ai-hundred-billion/caption.txt`
**Arabic headline:** أسبوع الـ ١٠٠ مليار دولار في الذكاء الاصطناعي
**English subhead:** AI'S HUNDRED-BILLION WEEK
**Kicker:** تحليل (analysis — deliberately not عاجل; this is a zoom-out piece)
**Big stats:** Anthropic $30B ARR • Meta×CoreWeave $35B • ASML €32.7B backlog • Gemini Robotics 93%
**Accent palette:** #D97757 Anthropic brick • #0071C5 ASML blue • #4285F4 Google blue
**Sources:** The Information, Bloomberg, Reuters, FT, WSJ, TechCrunch
**Why it matters to the feed:** Ahmed's audience leans MENA geopolitics — this is the reset-the-palate post. Arabic-first explainer of what the Silicon Valley money moves actually buy.

---

## 6. Iraq Blackout — Iranian Gas Collapses 74%

**Topic bucket:** `iraq_domestic` (explicit Iraq angle — complements war trifecta)
**Video:** `data/posts/2026-04-17-iraq-blackout/newsreel.mp4`
**Caption:** `data/posts/2026-04-17-iraq-blackout/caption.txt`
**Arabic headline:** العراق في الظلام: الغاز الإيراني ينهار من ١٩ إلى ٥ مليون متر مكعب
**English subhead:** IRAQ BLACKOUT • GAS COLLAPSE
**Kicker:** أزمة (crisis)
**Big stats:** -74% Iran gas imports • 8,000 MW grid deficit • 2× diesel price • 3 government options
**Accent palette:** #FFC217 yellow • #E74C3C alert red • #D72638 Photonect red (brand-tight)
**Sources:** Rudaw, Al Sharq Al Awsat, Iraq Oil Report, Reuters, AP, Al Jazeera
**Why it matters to the feed:** Iraq readers are the loyal core. This takes the Hormuz blockade and asks "what does this do to my electricity bill?" — same universal-relatability play as Flight Aftermath but for the Baghdad/Basra viewer.

---

## Quality Rubric (Approved Format — do not regress)

- 30 seconds, vertical 1080×1920 @ 30fps
- Arabic-first; English used only for subhead and big-stat labels
- 3 beats labeled ماذا يحدث؟ / لماذا يهم؟ / ماذا بعد؟
- ≥6 real sources on sources screen
- Big stat per beat (accent-colored, dominant)
- 4 supporting stats per beat in bilingual grid
- Persistent chrome: WORLD NEWS top strip + Arabic ticker + LIVE badge
- B-roll from real Pexels footage (no stock-photo clichés)
- Overlay gradients capped — b-roll must remain visible (see `feedback_newsreel_approved.md` in memory)

## QA Evidence

Each post folder has a `qa/` subdir with 5 still frames (t=2s, 10s, 18s, 25s, 29s) confirming:
- Arabic RTL rendering correct
- Big stat + supporting stats legible
- B-roll visible through overlay
- Brand chrome intact

## Posting Mechanics (deferred)

Instagram and TikTok credentials have NOT been connected. All 4 videos are render-complete and caption-ready — when you add `IG_ACCESS_TOKEN` and `TIKTOK_ACCESS_TOKEN` to `.env.local`, a publish script can schedule them on the cadence above. Nothing was auto-posted while you were away.

## Cleanup Performed

- NEWS CODE root cleaned: all legacy static-HTML pipeline files (iran_*.html, iraq_v*.html, render_*.py, slides_*/, v[2-4]_*.html, fonts, old images/) moved to `archive/pre-newsreel-legacy-html-pipeline/`.
- Root now contains only: `.env.local`, `.gitignore`, `.claude/`, `data/` (active posts), `archive/` (preserved history), `SHOWCASE.md` (this file).

## Next Session Ideas

- Add royalty-free audio bed (Remotion `<Audio>` component) — currently videos are silent, which is fine for IG autoplay-muted but flat on TikTok.
- Add Story 5: Iraq PM race (Amedi elected, Sudani blocked) — researched, not yet produced.
- Wire up NewsAPI scheduled task to auto-spin fresh NewsReel at 8:00, 14:00, 20:00 daily.
