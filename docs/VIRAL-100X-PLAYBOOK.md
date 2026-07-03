# PHOTONECT NEWS — 100X VIRAL PLAYBOOK (2026-07-03)

> Multi-agent strategy sprint (9 agents): hostile audit + 5 research lenses + Arabic-format teardowns → playbook → red-team. Baseline: 2–500 views/reel.



---

## A. HOSTILE FORMAT AUDIT

# FORMAT AUDIT: @photonect.news NewsReel V10.1 vs. 2026 TikTok/Reels algorithm

Bottom line up front: this is a slideshow wearing a video costume. The algorithm is pricing it correctly at 2-500 views. The per-video test batch on TikTok is ~200-600 impressions; your typical 10-160 views means most videos are FAILING THE FIRST TEST BATCH and never reaching a second distribution wave. Nothing here is a content-quality problem in the journalistic sense — it is a retention-physics problem.

---

## Signal 1 — First-frame stop-power: "LIVE bar + headline over still" open
**Verdict: KILLER**

- The 0-1s decision is made on motion, novelty, and pattern-interrupt. A static hero image + red LIVE chrome + Arabic headline is the single most saturated template in Arabic news-slop right now. MENA feeds are flooded with identical AI-generated "breaking" cards; users have trained a swipe reflex against the *template*, before reading a word.
- Worse: a 5-second title card is 9.4% of your runtime with zero information payload. On TikTok, ~50-65% of eventual abandons happen inside the first 3s for weak hooks. You spend those 3 seconds on chrome (a LIVE bar that is visibly not live — a credibility own-goal) instead of the story.
- **Fix direction:** kill the title card entirely. Cold-open on the single most concrete, visual, surprising fact of the story — motion in frame within 500ms (b-roll clip, animated map strike, number counting up), the headline landing as kinetic text by frame 15, story content by second 1.5. The "brand intro" belongs at the END, if anywhere.

## Signal 2 — Retention shape of 15s static-image beats
**Verdict: KILLER (the biggest one)**

- One still + slow zoom for 15 seconds means the visual channel delivers new information exactly 3 times in 45 seconds. TikTok-native content changes shot every 1.5-3s. Your visual event rate is ~10-20x too slow.
- Reading-paced content has a built-in cliff: a fast reader finishes your heading + 26-word body + 3 pills in 5-7s, then stares at a slow zoom for 8-10 dead seconds. Every beat manufactures three exit ramps at ~0:12, ~0:27, ~0:42.
- ~40 words on screen per beat with no audio guidance is also cognitive overload for the slow readers. You lose both tails: fast readers bored, slow readers overwhelmed.
- **Fix direction:** one idea per shot, 3-5s per visual, 3-4 visuals per beat (crops, pans between distinct images, animated overlays count). Text appears word-by-word synced to audio, max ~8-10 words on screen at once.

## Signal 3 — No voice-over on TikTok/Reels in Arabic markets
**Verdict: KILLER**

- TikTok is a sound-first platform and MENA has among the highest sound-on rates globally. Silent = you've unilaterally disarmed the strongest retention channel that exists (a human voice telling a story) AND the audio-transcript signal the algorithm uses to classify and search-index your content (TikTok search/SEO in 2026 leans heavily on speech transcription — silent videos are near-invisible in Arabic search).
- The V9 objection ("unsynced / not-Iraqi") was a solvable production bug treated as a format decision. MSA broadcast voice IS the expected register for Arabic news — nobody demands Iraqi dialect from a news anchor; Al Jazeera built an empire on MSA. 2026 Arabic TTS (ElevenLabs v3-class) is broadcast-grade, and sync is trivial when the VO *drives* the timeline instead of being pasted on top (generate VO first, cut visuals to it — which your Essay prototype already does).
- Every Arabic news account that actually clears 100K views (AJ+ عربي clones, معلومة-style explainers, Egyptian/Gulf news TikTokers) is VO-driven. Zero counterexamples at scale in the silent-text-card format.
- **Fix direction:** MSA VO spine on every reel, non-negotiable. Word-level captions synced to it. Your Suno beds become the *bed*, not the show.

## Signal 4 — 53s length vs completion-rate math
**Verdict: HURTING alone, KILLER combined with Signals 2-3**

Do the math. Model: weak hook retains ~60% past 3s; static text-card content then decays ~3%/sec (generous — VO-less slideshows decay faster).

- Completion at 53s ≈ 0.60 × e^(−0.03×50) ≈ **13%**
- Average watch time ≈ 12-16s → average view duration ≈ **25-30%**
- TikTok's distribution gate for a second wave wants roughly ≥35-40% AVD and meaningful completions on this length. You are structurally below the gate on every video. That is your 2-500 ceiling, mechanically explained.

Same content at 28s with a real hook (75% past 3s) and VO-paced cuts (1.5%/sec decay): 0.75 × e^(−0.015×25) ≈ **51% completion, ~60% AVD** → passes the gate, gets wave 2. Length isn't evil — un-earned length is. MrBeast-rule: every second must buy the next second. Your seconds 5-53 buy nothing.
- **Fix direction:** 25-35s until you have retention data proving you've earned more. One story = one tension arc, not three stacked mini-cards.

## Signal 5 — 7-topic scatter vs audience classification
**Verdict: HURTING (KILLER for follow-conversion)**

- 2026 recommendation is embedding-based: the system builds a vector for your channel from content + who watched. Iraq politics → Roland Garros → peanut-allergy patch → Knicks title gives it no stable vector; every video is cold-started against a different stranger pool, and your tiny follower base never compounds because a viewer who came for Iraq corruption gets tennis tomorrow. Follows require a predictable promise; you make seven.
- Your only defensible edge is Iraq/MENA-lens news in Arabic. Europe heatwaves and NBA titles are commodity content where you lose to a thousand bigger accounts.
- **Fix direction:** collapse to 2 buckets max — Iraq domestic + MENA/Gulf geopolitics (economy-through-Iraq-lens counts). Spin everything else off or kill it. Let the classifier learn who you are.

## Signal 6 — Batch-posting 6 within ~2 hours
**Verdict: HURTING**

- Six uploads in one window self-compete: they hit the same follower impressions and the same test pools simultaneously; IG in particular throttles rapid-fire posting from small accounts, and each video's early-velocity window (first 60-90 min) overlaps the next upload's.
- 4-6 PM Baghdad also misses the MENA usage peak (roughly 8 PM-1 AM).
- You have a fully automated pipeline — spacing costs literally nothing. This is a free win being left on the table.
- **Fix direction:** schedule ~2.5-3h apart, weighted 6 PM-midnight Baghdad. Render in a batch, post on a clock.

## Signal 7 — Engagement surface
**Verdict: KILLER**

- Ask the brutal question: after watching, what would a viewer *do*? There is no question posed, no stance to argue with, no stakes framing ("what this means for your salary/fuel/dinar"), no character to attach to, no series to await, no cliffhanger. "Strictly neutral, every claim attributed, numbers over adjectives" is a *sourcing* standard, but you've let it become a *personality* standard — and neutrality-as-personality is engineered un-commentability. Comments/shares/saves are the heaviest ranking weights; you generate ~zero of all three.
- Also: full automation means nobody replies to the few comments that exist and nobody seeds a first comment — the algorithm reads a dead room.
- Faceless is survivable (plenty of faceless channels scale) but faceless + voiceless + stanceless + scattered is a null identity.
- **Fix direction (without breaking neutrality):** (a) end every reel with one sharp open question as the final card + caption first line; (b) auto-post a pinned first comment with a poll-style prompt; (c) frame stories by local consequence, not abstraction — "Chevron pivot" becomes "what changes at Iraqi pumps"; (d) build a named virtual anchor persona (voice + name + catchphrase) so there is *someone* to follow; (e) recurring formats ("رقم اليوم", "خط الزمن") that create appointment behavior. The 3-part Iraq raid special was your best instinct all month — serialization is a follow machine; make it weekly, not one-off.

## Signal 8 — Caption/hashtag strategy
**Verdict: NEUTRAL trending HURTING**

- ~15 hashtags in 2026 is 2019 behavior — hashtags are a minor classification hint at best and read as spam at worst; they will not save a video the retention curve has killed. Numbers-bullets in the caption *duplicate* the video and remove any reason to watch it.
- The caption's real 2026 jobs: TikTok/IG keyword search (Arabic SEO phrases people actually type), and comment-baiting. You do neither.
- **Fix direction:** first line = searchable Arabic keyword phrase + curiosity gap (not a duplicate of the on-screen headline); one question; 3-5 hashtags (1 broad, 2 niche, 1-2 story-specific); sources moved to pinned comment.

---

## The 5 biggest reasons this channel sits at 2-500 views

1. **No voice-over.** A silent read-the-card format on a sound-first platform, in a market where every scaled Arabic news account is VO-driven. This single decision (V9) capped the channel harder than anything else. The fix is a solved TTS problem you already prototyped in the Essay engine.
2. **Retention physics: static 15s beats × 53s runtime ≈ 13% completion.** That fails TikTok's test-batch gate on every single upload, so no video ever reaches distribution wave 2 — which is exactly what a 10-160 view range means. You're not "not going viral"; you're not passing the entrance exam.
3. **Template-slop first impression.** A 5s "Breaking" title card over an AI still with a fake LIVE bar is instantly recognized as automated content and swiped in under a second; 2026 platforms additionally downrank detectable mass-produced/unoriginal AI content, so you're likely eating a quality-suppression penalty on top of the swipes.
4. **Null identity, null engagement surface.** Seven scattered topics, no voice, no character, no question, no series, no local-stakes framing, no comment activity → the algorithm measures near-zero engagement velocity and the follow-conversion rate rounds to zero, so nothing compounds across 6 posts/day.
5. **Distribution malpractice on autopilot.** Six self-competing uploads dumped in one off-peak window, captions that spoil the video, hashtag spam, sources burning caption real estate, nobody home in the comments. Each is individually small; together they tax every upload 20-40% — on a channel that can't afford 1%.

**Strategic note:** the unreleased Essay prototype (VO spine, motion b-roll, counters) is directionally the correct format and the NewsReel is not. The winning move is not shipping the 2-min Essay as-is — it's collapsing its DNA (VO-driven timeline, moving visuals, one narrative arc) into a 28-32s daily news unit, focused on Iraq/MENA only, spaced across the evening, with a question at the end. Everything in the current V10.1 spec except the brand palette and the editorial sourcing standard should be considered disposable.


---

## B. RESEARCH — Algorithm signals 2026

# TikTok + Instagram Reels distribution signals for a news-clips account (2025–2026)

Research synthesis, ranked by expected impact for an Arabic news-clips account posting daily reels. Signals split into **gates** (binary eligibility — get these wrong and ranking signals never fire) and **ranking signals** (continuous — decide how far the test-and-expand loop carries a video).

---

## GATE SIGNALS (eligibility — highest stakes for a news account)

### 1. Originality / transformation of clips — now a hard gate on both platforms
- **TikTok**: from **15 Sept 2025**, stepped-up enforcement against "unoriginal content" — reposts, copied clips, screen recordings of media, and "lazy transformation" (speed changes, watermark blurs) lose recommendations, search ranking, and organic reach. Detection uses perceptual hashing + C2PA metadata at claimed 90%+ accuracy ([BigSeller](https://www.bigseller.com/blog/articleDetails/3778/tiktok-unoriginal-content.htm), [TikTok Originality Policy](https://www.tiktok.com/creator-academy/article/tiktok-originality-policy), [Napolify](https://napolify.com/blogs/news/tiktok-duplicate-penalty)).
- **Instagram (Apr 2026)**: Mosseri announced accounts whose output over a rolling **30-day window** is mostly someone else's content become **ineligible for recommendations entirely** (Explore/Reels to non-followers); follower reach untouched but discovery growth dies. Adding original text overlays, voiceover, commentary, or a distinct editorial take restores originality; adding a credit screenshot or speed change does not ([Tubefilter](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/), [PetaPixel](https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/)). Estimated: original content gets 40–60% more distribution than reposts ([Disrupt](https://disruptmarketing.co/blog/instagram-original-content-update/)).
- **Why #1 for news clips**: raw agency/broadcast footage clips are the canonical target of both policies. Fully-authored renders (Remotion motion graphics, own VO, own text design) sit safely on the original side; screen-recorded TV clips do not.
- Related hard penalty: **third-party watermarks** (TikTok logo, CapCut) suppress IG Reels from Explore/recommendations — own brand logo is explicitly fine, per Mosseri ([Social Media Today](https://www.socialmediatoday.com/news/instagram-clarifies-including-your-own-logo-on-a-reel-is-ok/730852/), [Social Media Today 2](https://www.socialmediatoday.com/news/instagram-will-now-limit-the-reach-of-re-posts-from-tiktok-within-its-reels/594803/)).

### 2. News/political recommendation eligibility
- **Meta**: since Feb 2024, "political content" (governments, elections, "social topics that affect a group of people and/or society at large" — i.e. most hard news) is **not proactively recommended by default**; users must opt in via a Less/Standard/More control ([Instagram Help](https://help.instagram.com/339680465107440/), [TIME](https://time.com/6960587/meta-instagram-political-content-limit-off-setting-default/)). Measured effect: an [Accountable Tech study](https://accountabletech.org/research/metas-political-content-limit-causes-steep-drop-in-reach-for-accounts/) of 5 political/news accounts found a **~65% cumulative reach decline** over 11 weeks ([Fortune](https://fortune.com/2024/08/12/progressive-instagram-accounts-reach-meta-political-content-mark-zuckerberg/)).
- **Partial reversal, Jan 2025**: Zuckerberg announced civic content would be **phased back in**, ranked "like any other content" on personalized explicit/implicit signals, with "More" available in the control ([Meta Newsroom](https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/), [TechCrunch](https://techcrunch.com/2025/01/07/meta-to-phase-back-in-political-content-on-facebook-instagram-and-threads/)). Practical read: the blanket ceiling is lifted but civic content now needs *stronger-than-average* engagement signals to be recommended — it no longer gets a pass, and the user-level control still exists.
- **TikTok**: no blanket news downranking, but **unverified claims about crises or major civic events are FYP-ineligible** while under fact-check review — a direct tax on <24h breaking-news content; content confirmed false is removed or FYP-blocked; political accounts are excluded from monetization ([TikTok Community Guidelines](https://www.tiktok.com/community-guidelines/en/integrity-authenticity), [TikTok election integrity](https://www.tiktok.com/transparency/en/protecting-elections)). Mitigation: attribute every claim to named sources on-screen (matches the existing Editorial Mandate).
- **MENA-specific enforcement risk**: HRW documented **1,050+ takedowns/suppressions** of peaceful Palestine-related content on Meta platforms Oct–Nov 2023, largely via automated Arabic misclassification under the Dangerous Organizations policy ([HRW](https://www.hrw.org/news/2023/12/20/meta-systemic-censorship-palestine-content)); TikTok removed **17.4M videos in MENA in Q3 2025 alone** with 91% automated removal, and deleted Palestinian outlet QNN's account ([Saudishopper](https://saudishopper.com.sa/en/tiktok-mena-safety-report-q3-2025-video-removals/), [MEI](https://mei.edu/publication/content-moderation-trends-mena-region-censorship-discrimination-design-and-linguistic/)). Arabic war/conflict coverage carries elevated false-positive risk; neutral attributed language reduces it.

### 3. AIGC labels — mostly neutral, with one exception
- **TikTok officially states** the AI-generated label does **not** affect distribution if content follows guidelines ([AI label policy guide](https://aiimagetovideo.pro/blog/ai-generated-tiktok-videos/)); an experimental study found small AI labels **do not reduce reach, belief, or share likelihood** ([The Dais](https://dais.ca/reports/human-or-ai/)).
- **Instagram**: the label itself is not an algorithmic ranking input — effects are mediated by audience reaction ([Lookfamed](https://lookfamed.de/en/news/ai-labeling-on-instagram/)) — but **deepfake-style face/body manipulation reportedly draws 60–80% visibility penalties** ([Napolify](https://napolify.com/blogs/news/instagram-ai-label-policy)). For AI-generated *news imagery*, the bigger risk is misinformation enforcement on unlabeled photorealistic scenes of real events; labeling stylized/illustrative AI imagery is cheap insurance, but avoid photoreal depictions of specific real incidents.

---

## RANKING SIGNALS (what decides how far a video travels)

### 4. Watch time — #1 continuous signal on both platforms
- **Mosseri, Jan 2025**: watch time is the top Reels ranking factor, counted both **relative** (% watched) and **absolute** (seconds) ([Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers), [Buffer](https://buffer.com/resources/instagram-algorithms/)).
- **TikTok's own newsroom**: "a strong indicator of interest, such as whether a user finishes watching a longer video from beginning to end, would receive greater weight than a weak indicator" like shared country ([TikTok Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)).
- The hook is where watch time is won: ~50% of viewers drop in the first 3 seconds; industry target ≥60% retention through the 3-second mark ([Fanpage Karma](https://www.fanpagekarma.com/insights/instagram-reels-algorithm/), [Serotonin](https://www.serotonin.co.uk/news/how-instagrams-reels-ranking-works-in-2025-what-creators-need-to-know)). A 15s reel at 80% completion beats a 3-min reel at 20%.

### 5. Completion + rewatch/loop rate (TikTok-weighted)
- Completion ~70%+ is the commonly cited FYP-expansion threshold; **rewatches are described as the single best distribution signal**, with 20–30% rewatch rate on short clips considered strong ([Go-Viral](https://www.go-viral.app/blog/tiktok-algorithm-2026/), [Darkroom](https://www.darkroomagency.com/observatory/how-tiktok%E2%80%99s-algorithm-works-in-2026-and-15-tactics-to-go-viral), [Buffer TikTok](https://buffer.com/resources/tiktok-algorithm/)). Implication for 30s news reels: dense end-cards and loop-engineered closings that feed back into the hook.

### 6. Shares / sends-per-reach — the new-audience multiplier
- **Instagram**: Mosseri named **sends per reach** (DM shares relative to reach) the strongest signal for unconnected (non-follower) reach; commonly cited as weighted **3–5x likes** ([Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers), [Buffer](https://buffer.com/resources/instagram-algorithms/)).
- **TikTok**: shares are the strongest external endorsement signal ([Posteverywhere](https://posteverywhere.ai/blog/how-the-tiktok-algorithm-works), [TikTok Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)).
- News content is structurally advantaged here: "did you see this" forwarding is the native behavior. Design for it explicitly (a stat or map worth forwarding; a one-line takeaway that saves the recipient watching).

### 7. Likes-per-reach + comment rate
- **Likes per reach** is Mosseri's third confirmed signal, weighted more for connected (follower) reach ([Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers)). Mosseri's five feed interactions: likelihood to spend a few seconds, comment, like, share, tap profile ([Buffer](https://buffer.com/resources/instagram-algorithms/)). Comments are a strong TikTok interaction signal too ([Hootsuite](https://blog.hootsuite.com/tiktok-algorithm/)). For news: a debatable-but-factual framing question in the caption reliably drives comment rate.

### 8. Niche consistency / topical authority
- TikTok's FYP is an interest-graph built on **topic clusters from watch histories** — the Washington Post mapped 121,000 videos into these clusters ([Washington Post](https://www.washingtonpost.com/technology/interactive/2025/tiktok-algorithm-video-map-interests/)). Analyses of leaked ranking factors report a **cross-niche penalty (~-45% reach)** for accounts spanning >3 unrelated topics, ~10–15 consistent posts to build an interest profile, and 8–12 weeks to "topical authority" ([Softomate](https://www.softomatesolutions.com/blog/how-to-rank-on-tiktok-2026-algorithm/), [OpusClip](https://www.opus.pro/blog/tiktoks-new-algorithm-2026)). Note: TikTok says follower count and past viral hits are **not direct factors** — every video is tested independently ([TikTok Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)). The 7-bucket topic rotation is safe as long as format/branding keeps everything inside one "Arabic news explainer" cluster.

### 9. Caption SEO / keyword search
- TikTok processes **~140B searches/year**; ~40% of Gen Z start searches on TikTok/IG ([Rise at Seven](https://riseatseven.com/blog/tiktok-seo-statistics-in-2025-/), [SEO Sherpa](https://seosherpa.com/tiktok-seo/)). Search-optimized videos claim 300–500% more search views; keywords in the **first 150 characters** of the caption, spoken keywords in VO (audio is transcribed and indexed), on-screen text, and **3–5 targeted hashtags** beat hashtag spam ([EmbedSocial](https://embedsocial.com/blog/tiktok-seo/), [Boldtake](https://boldtake.io/guides/tiktok-seo-guide-2025)). Instagram removed hashtag-following in Dec 2024 — hashtags are now search metadata, not reach levers ([Buffer](https://buffer.com/resources/instagram-algorithms/)). For Arabic news this is underexploited: searchable Arabic proper nouns (العراق، أوبك، إيران، هدنة) in caption-front + VO give durable search traffic on top of FYP spikes.

### 10. Follows-from-video / profile taps
- Follows triggered by a video are an explicit TikTok interaction signal ([TikTok Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)); profile-photo taps are one of Mosseri's five watched interactions ([Buffer](https://buffer.com/resources/instagram-algorithms/)). Serialized formats ("Part 2 tomorrow", consistent daily slate branding) convert this.

### 11. Posting frequency & timing — real but weakest of the set
- IG data: 3–5 reels/week lifts reach/post ~12% and more than doubles follower growth vs 1–2/week; 6–9/week ≈ 3.7x growth ([Hopper HQ](https://www.hopperhq.com/blog/instagram-posting-frequency-2025/), [SMK](https://smk.co/instagram-growth-in-2025-requires-consistent-posting/)) — the 6/day slate is beyond the measured frontier, so watch for per-post cannibalization on IG (Meta surfaces roughly one reel per account per session to non-followers).
- Timing: TikTok is explicitly **not time-dependent** — a strong video posted at 3 AM can still run ([Buffer TikTok](https://buffer.com/resources/tiktok-algorithm/)); timing only shapes the speed of the initial test pool. Post when the Iraqi/Gulf audience is awake for faster first-hour signals, but don't over-optimize.

### 12. Sound usage
- Sound is video metadata TikTok uses for clustering ([TikTok Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)); trending audio gives a mild discovery assist on IG Reels ([Buffer](https://buffer.com/resources/instagram-algorithms/)). Minor for news; licensed/original music (current rotation) is the right call — the watermark rule matters far more.

---

## MENA/Arabic-specific distribution notes
1. **Arabic content is advantaged, not penalized, in-region**: TikTok penetration is 154% (Saudi), 134% (UAE), **94.5% (Iraq)**; consumption has shifted decisively from Western imports to dialect-driven local content, and Saudi users increasingly prefer Arabic over English ([AGBI](https://www.agbi.com/analysis/media/2026/02/gulfs-love-for-arabic-content-shields-local-tiktok/), [MEA Tech Watch](https://meatechwatch.com/2025/04/21/arab-internet-and-social-media-usage-growth-tiktok-tops-popularity-charts/)). Device language/country are real but **low-weight** clustering signals on TikTok ([TikTok Newsroom](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)) — Arabic caption + Arabic VO + Iraq-relevant keywords is what locks in the geo-cluster.
2. **The downside is moderation, not ranking**: automated Arabic classifiers misfire on dialect and conflict vocabulary (HRW's own anti-Hamas-war-crimes video was auto-removed); MENA sees 11–17M TikTok removals per quarter at 91%+ automation ([HRW](https://www.hrw.org/news/2023/12/20/meta-systemic-censorship-palestine-content), [Saudishopper](https://saudishopper.com.sa/en/tiktok-mena-safety-report-q3-2025-video-removals/)). Attributed, neutral, named-source framing is both editorial policy and an algorithmic survival strategy.

## Practical priority order for @photonect.news
(1) Keep every render unambiguously original (own motion design/VO/text — already true; never screen-record source footage); (2) engineer the 0–3s hook and loop for retention/rewatch; (3) design one forwardable element per reel for sends-per-reach; (4) front-load Arabic keywords in caption + VO for search; (5) attribute every claim on-screen to dodge unverified-claims FYP blocks and Arabic auto-moderation; (6) treat the Meta political-content control as a persistent headwind on IG — expect TikTok to out-distribute IG on hard-news buckets, and let softer buckets (tech/science/sports) carry IG discovery.

Sources: [TikTok Newsroom — How TikTok recommends videos](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you) · [TikTok Community Guidelines — Integrity & Authenticity](https://www.tiktok.com/community-guidelines/en/integrity-authenticity) · [TikTok Originality Policy](https://www.tiktok.com/creator-academy/article/tiktok-originality-policy) · [BigSeller — Sept 2025 unoriginal-content enforcement](https://www.bigseller.com/blog/articleDetails/3778/tiktok-unoriginal-content.htm) · [Buffer — Instagram algorithm](https://buffer.com/resources/instagram-algorithms/) · [Buffer — TikTok algorithm](https://buffer.com/resources/tiktok-algorithm/) · [Dataslayer — Mosseri-confirmed signals](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers) · [Fanpage Karma — Reels ranking](https://www.fanpagekarma.com/insights/instagram-reels-algorithm/) · [Tubefilter — IG aggregator recommendation ban](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/) · [PetaPixel — IG repost policy](https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/) · [Instagram Help — political content control](https://help.instagram.com/339680465107440/) · [Accountable Tech — 65% reach drop study](https://accountabletech.org/research/metas-political-content-limit-causes-steep-drop-in-reach-for-accounts/) · [Fortune — political reach decline](https://fortune.com/2024/08/12/progressive-instagram-accounts-reach-meta-political-content-mark-zuckerberg/) · [Meta Newsroom — More Speech and Fewer Mistakes](https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/) · [TechCrunch — civic content phase-back](https://techcrunch.com/2025/01/07/meta-to-phase-back-in-political-content-on-facebook-instagram-and-threads/) · [TikTok — Protecting elections](https://www.tiktok.com/transparency/en/protecting-elections) · [The Dais — AI label experiment](https://dais.ca/reports/human-or-ai/) · [Lookfamed — AI labeling reach](https://lookfamed.de/en/news/ai-labeling-on-instagram/) · [Napolify — IG AI label policy](https://napolify.com/blogs/news/instagram-ai-label-policy) · [Social Media Today — watermark/logo rules](https://www.socialmediatoday.com/news/instagram-clarifies-including-your-own-logo-on-a-reel-is-ok/730852/) · [Washington Post — TikTok interest map](https://www.washingtonpost.com/technology/interactive/2025/tiktok-algorithm-video-map-interests/) · [Rise at Seven — TikTok SEO stats](https://riseatseven.com/blog/tiktok-seo-statistics-in-2025-/) · [EmbedSocial — TikTok SEO](https://embedsocial.com/blog/tiktok-seo/) · [Hopper HQ — posting frequency](https://www.hopperhq.com/blog/instagram-posting-frequency-2025/) · [AGBI — Gulf Arabic content](https://www.agbi.com/analysis/media/2026/02/gulfs-love-for-arabic-content-shields-local-tiktok/) · [Saudishopper — TikTok MENA Q3 2025 removals](https://saudishopper.com.sa/en/tiktok-mena-safety-report-q3-2025-video-removals/) · [HRW — Meta's Broken Promises](https://www.hrw.org/news/2023/12/20/meta-systemic-censorship-palestine-content) · [MEI — MENA content moderation](https://mei.edu/publication/content-moderation-trends-mena-region-censorship-discrimination-design-and-linguistic/) · [Go-Viral — TikTok completion/rewatch](https://www.go-viral.app/blog/tiktok-algorithm-2026/) · [Softomate — cross-niche penalty](https://www.softomatesolutions.com/blog/how-to-rank-on-tiktok-2026-algorithm/)


---

## C. RESEARCH — Winning Arabic accounts

# Arabic News Short-Form: Who's Winning 2025-2026 & Why

## The Leaderboard (TikTok unless noted, mid-2025/2026 snapshots)

| Account | Followers | Format |
|---|---|---|
| الجزيرة (@aljazeera) | 17.8M TikTok, 458.8M likes | TikTok-native digital newsroom; young anchors, informal set, 1–3 min |
| سكاي نيوز عربية | 7.5M TikTok, 121.5M likes | Breaking clips + presenter shorts, high volume, MSA |
| الشرق للأخبار (Asharq/Bloomberg) | 6.2M TikTok, 107.1M likes; 2M IG | Polished vertical explainers + viral human-interest stories |
| AJ+ عربي | 2.8M TikTok, 49.5M likes; 3M IG | Caption-driven, sound-off-readable social storytelling; issues > headlines |
| العربية | 2.9M on regional @alarabiya.ksa alone (multi-account strategy) | Breaking news clips, MSA |
| أخبار الآن | 21.6M FB, 1M IG | Youth-targeted "القصة ملك الجميع" story-first packages |
| ستيب نيوز (Syrian diaspora) | 10M+ cross-platform, 4M FB | Text-on-video breaking news, raw footage, no presenter |
| المخبر الاقتصادي (YouTube) | 2.6M subs (2025), biggest Arabic econ channel | Narrated econ storytelling, simplified MSA |
| MISTER MONEY (@chebemoney) | TikTok/YT essay creator (Egyptian) | ~100–110s rap-narrated econ essays, glowing captions, animated counters |
| بي بي سي عربي | **only 266K TikTok** | Repurposed TV packages — the cautionary tale |
| Iraq: السومرية 866K TikTok / 10.1M likes; شبكة 964 249K IG (#1 Iraqi news site) | — | No dominant Iraqi short-form news brand exists yet |

## The 8 Winning Patterns

1. **Platform-native beats repurposed TV — the single biggest signal.** Al Jazeera's Shorty-winning TikTok unit rejected TV templates: anchors outside formal sets, spontaneous answers to "the question everyone is asking" about a trending story, 1–3 min, zero paid spend → 17.8M followers. BBC Arabic reposting broadcast packages → 266K. Same language, same news, ~67x gap.

2. **Two viable formats, not one.** (a) *Informal presenter-to-camera* (Al Jazeera, Sky News Arabia) — builds follow loyalty and para-social trust; (b) *faceless kinetic-caption VO edit* (AJ+, Step, your NewsReel lane) — built for sound-off viewing, big Arabic subtitles carrying 100% of the story; wins shares/reach. AJ+ codified this: "short, shareable, viewable with the sound off on a small screen."

3. **The winning length is 60–180s, not 15s.** Al Jazeera explainers 1–3 min; MISTER MONEY essays ~108s; breaking clips <60s. Depth-in-short-form is the growth band — headline-only clips don't build accounts. (Matches your 80/20 depth mandate.)

4. **Hook = the audience's own question, or binary bait, in ≤3s.** Al Jazeera's device: open with the trending question people are already asking. MISTER MONEY's device (from your own teardown): fake-debate bait — "أغبى قرار… أم مشروع عبقري؟" over a striking anchor visual (gold dumped into a chasm, pyramids motif), then argue both sides before landing the thesis.

5. **Register rule: brand = simplified MSA (بيضاء); persona = dialect.** All pan-Arab winners (الجزيرة، الشرق، سكاي، AJ+) use accessible MSA. Dialect wins only in the creator/infotainment lane (Egyptian for chebemoney/المخبر audience feel; Iraqi for Iraq-local pages). Dialect buys intimacy, MSA buys reach.

6. **Industrial cadence, lottery-ticket math.** Al Jazeera published 1,928 TikToks in 2023 (~5–6/day); only 197 (~10%) crossed 1M views, but those carried 806.7M total views. Winners accept that virality is a volume game — daily multiples, never gaps. Sky News Arabia and Asharq run similar always-on volume.

7. **What the most-viral videos share:** trending mega-story + fast turnaround (war, ceasefires, currency crises); human emotion over institutions (Asharq's most-searched TikTok content is a viral human story, "البنت المكسيكية", not geopolitics); big numbers made visual (MISTER MONEY's animated debt counters; المخبر's econ narratives); recurring identity-anchor visuals (pyramids in every chebemoney scene); and sound-off readability.

8. **Demand side is proven, Iraq lane is open.** 79% of Arab youth get news from social media (up 25 pts since 2015); TikTok penetration 94.2% in KSA / 90.1% in UAE; Arab youth TikTok use doubled 2019–2022; Reuters DNR 2025 confirms news creators/influencers are displacing legacy brands with young audiences. In Iraq specifically, 18–34s are ~70% of engaged social users, yet the biggest Iraqi news TikTok (Alsumaria) is <1M — no one has built the Iraqi AJ+ yet.

**Implications for Photonect:** the format you're already running (60s+ caption-driven VO reels, MSA, daily volume) matches winner patterns 2b/3/5/6; the biggest gaps vs. winners are hook-as-audience-question (pattern 4), human-story ratio vs. institutional framing (pattern 7), and the open Iraqi presenter/persona lane (patterns 2a/8) — which the essay engine (chebemoney clone, teardown at `/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/docs/ESSAY-ENGINE-BLUEPRINT.md`) is positioned to fill.

Sources: [Al Jazeera Arabic TikTok — Shorty Awards case study](https://shortyawards.com/16th/aj-dnr-4), [AJ+ عربي TikTok](https://www.tiktok.com/@ajplusarabi), [AJ+ عربي Instagram](https://www.instagram.com/ajplusarabi/), [AJ+ — Wikipedia](https://en.wikipedia.org/wiki/AJ%2B), [AJ+ Arabi launch — Al Jazeera Network](https://network.aljazeera.net/en/events/al-jazeera-officially-launches-aj-arabi), [FIPP on AJ+ millennial strategy](https://fipp.com/news/features/a-look-at-al-jazeeras-unique-approach-millennials), [Sky News Arabia TikTok](https://www.tiktok.com/@skynewsarabia), [Asharq News TikTok](https://www.tiktok.com/@asharqnews), [أخبار الآن Facebook](https://www.facebook.com/akhbaralaan/), [أخبار الآن Instagram](https://www.instagram.com/akhbaralaan/), [BBC News Arabic TikTok](https://www.tiktok.com/@bbcnewsarabic), [وكالة ستيب — Wikipedia](https://ar.wikipedia.org/wiki/%D9%88%D9%83%D8%A7%D9%84%D8%A9_%D8%B3%D8%AA%D9%8A%D8%A8_%D8%A7%D9%84%D8%A5%D8%AE%D8%A8%D8%A7%D8%B1%D9%8A%D8%A9), [Step News IG](https://www.instagram.com/stepnews/), [المخبر الاقتصادي — Wikipedia](https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D9%85%D8%AE%D8%A8%D8%B1_%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A), [Mister Money TikTok](https://www.tiktok.com/@chebemoney), [Mister Money YouTube](https://www.youtube.com/@chebemoney.egofficial), [Alsumaria TikTok](https://www.tiktok.com/@alsumariatv), [شبكة 964](https://964media.com/453961/), [964arabic IG](https://www.instagram.com/964arabic/), [Reuters Institute DNR 2025](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary), [RISJ news creators mapping 2025](https://reutersinstitute.politics.ox.ac.uk/news-creators-influencers/2025/mapping-news-creators-and-influencers-social-and-video-networks), [NW Qatar Media Use survey](https://www.mideastmedia.org/survey/2022/chapter/online-and-social-media/), [World Happiness Report — MENA social media](https://www.worldhappiness.report/ed/2026/social-media-use-and-wellbeing-in-the-middle-east-and-north-africa/), [Sprinklr — Saudi social media 2025](https://www.sprinklr.com/blog/social-media-in-saudi-arabia/), [StarNgage Iraq TikTok ranking](https://starngage.com/app/global/influencer/ranking/tiktok/iraq), [Favikon — Top Iraq influencers](https://www.favikon.com/blog/top-iraq-influencers)


---

## D. RESEARCH — Hook engineering

# Hook Engineering + Retention Structure for News/Explainer Short-Form (2025–2026)
Research synthesis for the Photonect NEWS automated pipeline. All claims cited; formula bank at the end is pipeline-ready.

---

## 1. The data that matters

**3-second gate.** Videos holding 65%+ of viewers at the 3-second mark get 4–7x more impressions; 70–85% intro retention correlates with 2.2x total views; below 60% gets minimal algorithmic promotion. 84.3% of viral TikToks used an explicit psychological hook trigger in the first 3s. The first 3 seconds drive ~80% of completion variance. ([TTS Vibes](https://insights.ttsvibes.com/tiktok-first-3-seconds-hook-retention-rate/), [OpusClip TikTok hooks](https://www.opus.pro/blog/tiktok-hook-formulas))

**Length is bimodal, not linear.** Analysis of 35B YouTube Shorts views: best performance at ~13s OR full 60s — the 30–45s middle underperforms on Shorts. Reels: 15–30s is the viral-reach sweet spot (sub-15s Reels hit ~57% completion; >60s drops to ~36% completion), but 60–90s Reels earn the highest average views/engagement because the algorithm weighs total watch-seconds as well as completion — a 45s reel at 70% retention can beat a 15s reel at 90%. ([Shortimize](https://www.shortimize.com/blog/video-length-sweet-spots-tiktok-reels-shorts), [Bennofilms](https://bennofilms.com/blog/ideal-instagram-tiktok-video-length), [Metricool](https://metricool.com/instagram-reels-length/), [jogg.ai](https://www.jogg.ai/blog/optimal-instagram-reel-length-2025/))

**News-specific.** Publishers on TikTok: complete-watch targets >60%; question-led openings and curiosity gaps outperform; recurring named formats (daily roundups, map explainers, "5 things you need to know") build habit; republishing unadapted TV content fails; "get rewarded for making a TikTok that looks like a TikTok." News clips under 60s deliver ~2.5x higher engagement (Media.net survey). Majority of under-35s now get news from social video. ([Reuters Institute TikTok study](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok), [Reynolds Center](https://businessjournalism.org/2025/10/short-form-video/), [Reuters Institute DNR 2025](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary))

**Implication for the 30s NewsReel format:** 28–35s is the right zone for single-story news on Reels/TikTok (viral-reach band + enough watch-seconds); avoid drifting to 40–50s (dead zone on Shorts). Deep analysis stories can run a second 55–60s variant.

---

## 2. First-second rules (frame 0 to second 3)

1. **Motion in the first 8 frames.** Static openers lose; a zoom, swipe, hand entering frame, or camera push wins. Never open on a still card. ([Coinis thumb-stop](https://coinis.com/glossary/thumb-stop-rate))
2. **Faces beat objects by ~30% thumb-stop** (Meta Creative Hub guidance); face + motion + text overlay together outperform any single element (tested: 39% thumb-stop for motion+text vs 31% face-only). For news without presenters: use a human-scale hero image (crowd, official, close-up) with a slow push-in, not an empty building/wide establishing shot. ([Coinis](https://coinis.com/glossary/thumb-stop-rate), [InfluenceFlow](https://influenceflow.io/resources/creating-compelling-video-thumbnails-and-titles-the-complete-2026-guide/))
3. **Hook must work on mute.** Test the first 3s with no audio; the text hook alone must communicate the stakes. High-contrast text, ≤10–14 words, no frame clutter. ([OpusClip](https://www.opus.pro/blog/tiktok-hook-formulas), [Vexub](https://vexub.com/blog/viral-short-form-video-hooks))
4. **Dual-channel:** spoken hook and text hook should reinforce, not duplicate — text carries the number/stake, voice carries the question. ([OpusClip](https://www.opus.pro/blog/tiktok-hook-formulas))
5. **Pattern interrupt:** an abrupt sound, unusual visual, or bold claim hijacks the orientation response before conscious skip-decision. For news: a hard number, a red BREAKING-style flash, or a jarring juxtaposition frame. ([CreatorsJet](https://www.creatorsjet.com/blog/7-viral-hook-frameworks-for-short-form-video-creators))
6. **First frame = thumbnail** on TikTok/Reels — it must be striking standalone (already aligned with the existing cover-at-3s practice). ([HeyTrendy](https://heytrendy.app/blog/instagram-reels-best-practices))

---

## 3. Spoken + text hook formula bank (Arabic-adapted)

Four cognitive triggers: curiosity gap, pattern interrupt, self-relevance, emotional arousal; strong hooks stack two. ([CreatorsJet](https://www.creatorsjet.com/blog/7-viral-hook-frameworks-for-short-form-video-creators)) The most consistently viral 2026 templates: Contrarian Claim, Mistake Warning, List Tease. Spoken hooks ≤10–14 words. ([Vexub](https://vexub.com/blog/viral-short-form-video-hooks))

Adapted for Arabic news (MSA body, Iraqi-colloquial hook is allowed — it IS the pattern interrupt against formal news feeds). Rotate 5–10 formulas; never repeat one two posts in a row:

| ID | Formula | Arabic template | Use for |
|---|---|---|---|
| H1 | Number shock | «[رقم صادم] — هذا ما حدث في [مكان] خلال [مدة]» | econ, oil, casualties |
| H2 | Curiosity gap (شنو صار؟) | «شنو اللي صار بـ[مكان] الليلة؟» / «ماذا حدث فعلاً في…؟» | breaking |
| H3 | Why/How question | «لماذا [حدث غير متوقع]؟» / «شلون [دولة] سوّت [نتيجة]؟» | explainers |
| H4 | Contrarian claim | «كل ما سمعته عن [قصة] ناقص نصف الحقيقة» | analysis |
| H5 | Stakes-first | «هذا القرار يمسّ [جيبك/راتبك/سعر الدولار] مباشرة» | self-relevance, econ |
| H6 | Countdown tease | «٣ أشياء تغيّرت اليوم — الثالثة هي الأخطر» | roundups |
| H7 | Before/after | «قبل أسبوع كان [س]… اليوم صار [ص]» | escalation stories |
| H8 | Insider/reveal | «الوثائق تكشف ما لم يُقل في المؤتمر الصحفي» | investigations (attribute!) |
| H9 | What-if / scenario | «ماذا لو أُغلق [مضيق هرمز] فعلاً؟» | scenario analysis |
| H10 | Direct call-out | «إذا راتبك بالدينار، هذا الخبر إلك» | audience-specific |

Guardrails (Editorial Mandate compatible): every hook claim must be resolved and attributed inside the video; number shocks must use sourced numbers; no loaded language — the shock is the fact, not the adjective.

---

## 4. Retention structure: hook → body → payoff (the 30s skeleton)

Canonical structure: Hook 1–3s → Body 70–80% → Payoff 10–20% → Post-payoff 1–2s. ([Socialync](https://www.socialync.io/blog/short-form-video-structure-guide-2026))

**Pipeline-ready 30s NewsReel beat sheet:**

| Time | Beat | Rule |
|---|---|---|
| 0–1s | Visual pattern interrupt | motion + face/human-scale hero + brand flash |
| 0–3s | Hook (one formula from bank) | text ≤10 words, voice ≤14 words, works on mute |
| 3–6s | Context snap | one sentence: who/where/when. Open a mini-loop («لكن السبب مختلف تماماً») |
| 6–14s | Escalation 1 | first fact + supporting stat; visual change every 3–5s |
| 14–22s | Escalation 2 | second fact, tension rises; mid-video re-hook: forward-reference what's coming («والأهم بعده») |
| 22–27s | Payoff | resolve the hook's promise with the concrete answer/number |
| 27–30s | Post-payoff | either 2s CTA or loop-back line that reads as the opening's continuation |

Body retention techniques: change visuals every 3–5s, pattern interrupt every 5–8s, speech paragraphs <8s, escalate value linearly (basic → interesting → strongest fact last), remove all filler. ([Socialync](https://www.socialync.io/blog/short-form-video-structure-guide-2026), [Automateed](https://www.automateed.com/content-hooks-for-short-form-videos))

---

## 5. Loop / rewatch engineering

- Rewatch is one of the strongest quality signals: a second watch counts as 200% watch time; seamless loops trigger involuntary replays. ([SMMNut](https://smmnut.com/blog/tiktok-loop-content-strategy-2025/), [Dailyovershare](https://dailyovershare.com/slp-tiktok-algorithm-completion-rate-20250131))
- **Technique:** match final frame to first frame in color/framing/subject position; crossfade audio across the boundary — an audible cut kills the loop even if visuals are clean. ([SMMNut](https://smmnut.com/blog/tiktok-loop-content-strategy-2025/))
- **Script loop:** write the last line so it grammatically completes into the first line («…وهنا نرجع للسؤال —» → loop → «شنو اللي صار؟»), or use "The Loop Back" payoff style. ([Socialync](https://www.socialync.io/blog/short-form-video-structure-guide-2026))
- TikTok distinguishes intentional rewatches from passive loops, so the loop must invite re-reading (e.g., a dense stat card at second 2 the viewer missed first time). ([Fanpage Karma](https://www.fanpagekarma.com/insights/the-2025-tiktok-algorithm-what-you-need-to-know/))

---

## 6. Pacing (cuts per second)

- Short-form baseline: hard cut or visual state-change every **2–4s**; never a static hold >4s. ([OpusClip Shorts](https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention))
- Match pace to energy: breaking/action beats can cut every ~2s; a single powerful face/photo can hold longer if a ken-burns/scan element keeps moving (aligns with existing "every frame has a moving element" rule). ([Visla](https://www.visla.us/blog/guides/video-editing-pacing-what-it-is-and-how-to-control-it/), [AIR Media-Tech](https://air.io/en/youtube-hacks/advanced-retention-editing-cutting-patterns-that-keep-viewers-past-minute-8))
- Sub-1s clips are now standard but only when instantly legible — brains process patterns, not chaos. ([B Square Visuals](https://bsquarevisuals.com/video-editing-trends-hyper-fast-cuts/))
- Pipeline check: for a 30s reel, target **10–14 distinct visual states** (cuts, zoom shifts, stat-card pops).

---

## 7. Captions / subtitle styling

- Word-by-word karaoke captions boost average watch time **12–25%** — dual engagement loop (reading + listening) is harder to abandon; strongest retention of all caption styles. ([AIVidGenie](https://www.aividgenie.com/blog/caption-styles-that-boost-engagement), [OpusClip caption presets](https://www.opus.pro/blog/best-caption-presets-styles-boost-retention))
- Best practice: color-shift highlight (white → brand accent — use #FFC217) rather than boxes/underlines; highlight each word **50–100ms before** it's spoken (reading outpaces listening). ([OpusClip](https://www.opus.pro/blog/best-caption-presets-styles-boost-retention))
- 3–5 words per caption line max on screen; high contrast; keep safe-zone clear of UI. ([VidNo](https://vidno.ai/blog/karaoke-style-word-highlight-captions))
- For Arabic RTL: same rules apply; ensure the highlight animation runs right-to-left with the word order.

---

## 8. CTA + serialization

- Series-driven follow rates are **3–5x higher** than one-off viral posts; series create habitual viewers and are the most reliable follower-growth mechanic on short-form. ([Medium/Episodic series](https://medium.com/@yashasvi_nurdd/episodic-short-form-series-why-creators-are-abandoning-the-one-off-reel-in-2026-bdc6aa03ed9f), [Superdirector](https://superdirector.app/glossary/content-series))
- Mid-tension endings + "follow for part 2" convert passive viewers to followers while maximizing the current video's completion. ([Superdirector](https://superdirector.app/glossary/content-series))
- News publishers' proven recurring formats: named daily roundup, question-led explainer, map-based analysis. Naming the segment builds habit. ([Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok))
- CTA placement: post-payoff only, ≤2s, one ask. Options per Socialync: hard cut (impact), 2s CTA, or loop setup — rotate; never stack CTAs. ([Socialync](https://www.socialync.io/blog/short-form-video-structure-guide-2026))
- **Photonect application:** brand 1–2 named daily segments (e.g., «الملف العراقي» daily deep-dive; «٦٠ ثانية من المنطقة» roundup); multi-part treatment for big running stories with an explicit part-N header and «تابعنا للجزء الثاني» ending on cliffhanger beats.

---

## 9. Machine-checkable ruleset (drop into QA gate)

```
HOOK_TEXT_MAX_WORDS: 10          # on-screen hook
HOOK_SPOKEN_MAX_WORDS: 14
HOOK_FORMULA: one of H1..H10, != previous post's formula
FIRST_8_FRAMES: must contain motion (no static open)
FIRST_FRAME: human-scale subject preferred; doubles as cover
MUTE_TEST: first 3s must convey stakes with audio off
LENGTH_SEC: 28–35 (standard) | 55–60 (deep-dive variant); NEVER 40–50
VISUAL_STATE_CHANGES: >= 10 per 30s (change every 2–4s)
SPEECH_PARAGRAPH_MAX_SEC: 8
MINI_OPEN_LOOP: required at 3–6s beat
MID_REHOOK: forward-reference required at ~50% mark
PAYOFF: must resolve hook claim, attributed source
ENDING: rotate {hard_cut, cta_2s, loop_back}; loop_back = last frame matches first frame + audio crossfade
CAPTIONS: karaoke word-highlight, #FFC217 accent, lead 50–100ms, <=5 words/line
CTA: max 1, post-payoff only
SERIES: multi-part stories end mid-tension + «تابعنا للجزء الثاني»
```

Sources: [TTS Vibes](https://insights.ttsvibes.com/tiktok-first-3-seconds-hook-retention-rate/) · [OpusClip TikTok hook formulas](https://www.opus.pro/blog/tiktok-hook-formulas) · [OpusClip caption presets](https://www.opus.pro/blog/best-caption-presets-styles-boost-retention) · [OpusClip Shorts length](https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention) · [Shortimize length sweet spots](https://www.shortimize.com/blog/video-length-sweet-spots-tiktok-reels-shorts) · [Bennofilms](https://bennofilms.com/blog/ideal-instagram-tiktok-video-length) · [Metricool](https://metricool.com/instagram-reels-length/) · [jogg.ai](https://www.jogg.ai/blog/optimal-instagram-reel-length-2025/) · [Vexub 25 hook formulas](https://vexub.com/blog/viral-short-form-video-hooks) · [CreatorsJet hook frameworks](https://www.creatorsjet.com/blog/7-viral-hook-frameworks-for-short-form-video-creators) · [Socialync structure guide](https://www.socialync.io/blog/short-form-video-structure-guide-2026) · [Automateed](https://www.automateed.com/content-hooks-for-short-form-videos) · [Reuters Institute TikTok publishers](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok) · [Reuters Institute DNR 2025](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary) · [Reynolds Center](https://businessjournalism.org/2025/10/short-form-video/) · [SMMNut loop strategy](https://smmnut.com/blog/tiktok-loop-content-strategy-2025/) · [Dailyovershare completion rate](https://dailyovershare.com/slp-tiktok-algorithm-completion-rate-20250131) · [Fanpage Karma algorithm](https://www.fanpagekarma.com/insights/the-2025-tiktok-algorithm-what-you-need-to-know/) · [AIVidGenie captions](https://www.aividgenie.com/blog/caption-styles-that-boost-engagement) · [VidNo karaoke captions](https://vidno.ai/blog/karaoke-style-word-highlight-captions) · [Coinis thumb-stop rate](https://coinis.com/glossary/thumb-stop-rate) · [InfluenceFlow thumbnails](https://influenceflow.io/resources/creating-compelling-video-thumbnails-and-titles-the-complete-2026-guide/) · [HeyTrendy Reels practices](https://heytrendy.app/blog/instagram-reels-best-practices) · [Episodic series (Medium)](https://medium.com/@yashasvi_nurdd/episodic-short-form-series-why-creators-are-abandoning-the-one-off-reel-in-2026-bdc6aa03ed9f) · [Superdirector content series](https://superdirector.app/glossary/content-series) · [B Square Visuals fast cuts](https://bsquarevisuals.com/video-editing-trends-hyper-fast-cuts/) · [Visla pacing](https://www.visla.us/blog/guides/video-editing-pacing-what-it-is-and-how-to-control-it/) · [AIR Media-Tech retention editing](https://air.io/en/youtube-hacks/advanced-retention-editing-cutting-patterns-that-keep-viewers-past-minute-8)


---

## E. RESEARCH — Arabic voice/VO

# Research: Voice in Arabic Short-Form News (2026)

## (a) Does AI VO work for viral Arabic content?

**Yes for voice-only narration; no for synthetic anchors.** The evidence splits cleanly:

- The [Reuters Institute Generative AI and News Report 2025](https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-how-people-think-about-ais-role-journalism-and-society) found only **12% of audiences are comfortable with fully AI-generated news vs 62% for human-made** — but acceptance rises sharply with human oversight, and resistance concentrates on *front-facing* uses: artificial presenters, synthetic faces, and sensitive/political topics ([DNR 2024 attitudes chapter](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2024/public-attitudes-towards-use-ai-and-journalism)). Voice-only narration over b-roll/graphics sits in the tolerated zone; a fake human anchor does not.
- The "AI news reporter voice" is itself a native TikTok format ([TikTok discover pages](https://www.tiktok.com/discover/how-to-do-the-ai-news-reporter-voice) treat it as a meme/genre, not a stigma). Audiences do not punish TTS per se — they punish *bad* TTS (robotic MSA misreads) and deception. The cautionary tale: [ISIS propaganda networks used AI anchors styled like Al Jazeera/CNN](https://www.hstoday.us/featured/is-iskp-supporters-harness-generative-ai-for-propaganda-dissemination/) — mimicking a real broadcaster's look is now pattern-matched to disinfo. Avoid the fake-anchor aesthetic entirely.
- I could not verify specific named Arabic organic news accounts that openly credit AI VO (search surfaced tools, not accounts) — treat "which accounts use it openly" as unconfirmed.
- **Labeling is now mandatory and safe**: TikTok's 2026 policy requires the AI-content toggle for cloned/AI narrator voices and [states the toggle does not affect distribution](https://storrito.com/resources/tiktoks-2026-ai-labeling-rules-and-what-they-signal-for-platform-governance/) ([4-tier label system](https://www.auditsocials.com/blog/tiktok-ai-content-disclosure-rules-2026)); Meta unified Instagram/Facebook AI disclosure in Feb 2026 with a "Made with AI" advanced setting ([platform-by-platform guide](https://influencermarketinghub.com/ai-disclosure-rules/)). TikTok claims spectral detection of cloned voices, so disclose proactively rather than get flagged.

## (b) Best Arabic TTS options for a news-narrator voice

| Option | Iraqi/Levantine | Quality | Timestamps | Notes |
|---|---|---|---|---|
| **ElevenLabs v3** | No dialect differentiation — "generic Arabic" | Best expressiveness/intonation for MSA; big v3 jump ([JJ Agency review](https://jjagency.co/blog/elevenlabs-v3-alpha-arabic-ai-voiceovers-new-quality-levels/)) | v3 timing endpoint + char-level [convert-with-timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps) | Audio tags = emotion, not dialect. Hits limits on "Levantine cadence" ([Hakim comparison](https://tryhakim.ai/en/alternatives/elevenlabs) — biased source but consistent with other reviews) |
| **ElevenLabs PVC clone of a licensed Iraqi narrator** | Accent carried by source audio + dialect-written text | v3 expressiveness with native phonology | Same as above + [Forced Alignment API](https://elevenlabs.io/docs/overview/capabilities/forced-alignment) (Arabic supported, word-level) | Best quality ceiling; one-time narrator licensing cost |
| **Azure Neural TTS ar-IQ** | **Yes — Bassel/Rana, Baghdadi register** ([voice list](https://json2video.com/ai-voices/azure/voices/ar-iq-rananeural/)); also ar-SY/ar-LB/ar-JO | Correct phonology, flatter prosody than ElevenLabs | **Native WordBoundary events** — cleanest karaoke-caption path ([Azure language support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support)) | Cheap, deterministic, ideal fallback |
| **Hakim (tryhakim.ai)** | 15 Arabic varieties incl. Levantine/Khaleeji | Arabic-first, claims native dialect quality | REST API, Node/Python SDKs | GCC data residency; new/unproven — bake-off candidate |
| **Habibi (open source, Jan 2026)** | **Yes — unified model covers IRQ + LEV among 12 dialects** | [Paper claims it beats Eleven v3 alpha on dialect test sets](https://arxiv.org/html/2601.13802v1) | None built-in — pair with forced alignment | F5-TTS based, weights/code being open-sourced; no code-switching, dialect imbalance. Self-host option |

**Karaoke captions**: three working paths — (1) ElevenLabs `/with-timestamps` (character-level → aggregate to words), (2) ElevenLabs Forced Alignment API on any rendered audio + script (works for Habibi/Hakim output too), (3) Azure WordBoundary natively. All three feed word-timed JSON straight into Remotion.

## (c) MSA vs Iraqi dialect for reach

Evidence points to a **hybrid register, not a binary**:

- Pan-Arab broadcasters (Al Jazeera, BBC Arabic) stay MSA for cross-border reach and authority ([Milestone](https://www.milestoneloc.com/modern-standard-arabic/), [Arabic Language Service](https://arabiclanguageservice.com/choosing-between-gulf-arabic-and-modern-standard-arabic/)); but social-native content across MENA has shifted to dialect for authenticity and emotional connection, and MSA increasingly reads as "distant" in feed contexts ([Fast Trans](https://fast4trans.com/en/choosing-right-arabic-dialect-for-business/)).
- Iraq specifically: TikTok is the dominant platform (~35M users, reach surpassing all other platforms — [Shafaq](https://shafaq.com/en/Report/Iraq-s-TikTok-debate-digital-growth-vs-cultural-norms)), and the winning local creators are dialect-first; dialect-driven content is the strong regional trend ([AGBI](https://www.agbi.com/analysis/media/2026/02/gulfs-love-for-arabic-content-shields-local-tiktok/)).
- **What wins for an Iraq/MENA news channel**: "white Iraqi" (عامية بيضاء) — MSA skeleton with Iraqi rhythm and selective dialect markers. MSA-leaning read for hard geopolitics (credibility + pan-Arab reach into Gulf/Levant), Iraqi-leaning read for hooks, CTAs, and Iraq-local stories. This is a *text-register* decision, not a voice swap — same narrator, the copywriter shifts register.

## (d) Trending-sound strategy

- News publishers succeed on TikTok/Reels **without riding trending audio** — the Reuters Institute's publisher study found news works via explainers and formats, "not having to resort to news presenters dancing" ([Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok)); in the AI-slop era, trusted/consistent presentation is the appreciating asset ([2026 trends](https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026)).
- Verdict: **ride trend *formats* (structures, caption memes, editing patterns), never trend *music* on hard news.** Trending pop under a Sudan-genocide or ceasefire story wrecks credibility, and business accounts face commercial-music licensing limits anyway. Narrow exception: soft buckets (sports, culture, tech) can use a trending sound at low bed volume under VO. The bigger win: a consistent narrator voice makes every post "original audio" — repeated original audio becomes a sonic brand that TikTok/IG users recognize in-feed, which compounds in a way borrowed sounds never do.

## Recommended voice architecture (fully-automated pipeline)

1. **One fixed channel narrator ("صوت القناة")** — ElevenLabs Professional Voice Clone of a licensed native Iraqi male narrator (warm-authoritative, late-30s). One voice, every NEWS reel, forever: the voice *is* the brand. Separate distinct voice for HEKAYA.
2. **Register switching in text, not voice**: `iraqi-copywriter` outputs two registers — MSA-leaning for geopolitics/economy, white-Iraqi for local/sports/culture hooks. Persian-char guard (U+06CC/06A9) still applies before TTS.
3. **Model routing**: `eleven_multilingual_v2` via `/with-timestamps` as default (stable + timing in one call); `v3` for high-emotion essay-engine pieces, then Forced Alignment API for word timing.
4. **Fallback chain** (mirrors the KIE-402 pattern): ElevenLabs → Azure ar-IQ Bassel (WordBoundary timestamps, near-zero cost) → flag in DELIVERY. Never ship silent.
5. **Bake-off track**: pilot Hakim API and Habibi weights (Iraqi dialect) on 2 non-critical reels/week; promote if they beat the clone on Ahmed's ear test.
6. **Governance**: enable TikTok AI toggle + Meta "Made with AI" on every VO post (no distribution penalty, avoids detection strikes); voice-only narration + kinetic karaoke captions; never a synthetic human anchor face.
7. **Audio mix**: VO at -3dB over the existing 4-mood music rotation ducked to -18dB; no trending music on hard news.

Sources: [Reuters Institute GenAI & News 2025](https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-how-people-think-about-ais-role-journalism-and-society) · [Reuters Institute DNR 2024 AI attitudes](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2024/public-attitudes-towards-use-ai-and-journalism) · [Reuters Institute publishers on TikTok](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok) · [Reuters Institute 2026 predictions](https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026) · [Habibi paper (arXiv 2601.13802)](https://arxiv.org/html/2601.13802v1) · [JJ Agency ElevenLabs v3 Arabic](https://jjagency.co/blog/elevenlabs-v3-alpha-arabic-ai-voiceovers-new-quality-levels/) · [Hakim vs ElevenLabs](https://tryhakim.ai/en/alternatives/elevenlabs) · [ElevenLabs timestamps API](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps) · [ElevenLabs Forced Alignment](https://elevenlabs.io/docs/overview/capabilities/forced-alignment) · [Azure Speech language support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support) · [Azure ar-IQ Rana](https://json2video.com/ai-voices/azure/voices/ar-iq-rananeural/) · [SpeechGen ar-IQ](https://speechgen.io/en/tts-arabic-iraq/) · [TikTok AI policy 2026](https://www.auditsocials.com/blog/tiktok-ai-content-disclosure-rules-2026) · [Storrito TikTok labeling](https://storrito.com/resources/tiktoks-2026-ai-labeling-rules-and-what-they-signal-for-platform-governance/) · [Influencer Marketing Hub AI disclosure](https://influencermarketinghub.com/ai-disclosure-rules/) · [Shafaq Iraq TikTok](https://shafaq.com/en/Report/Iraq-s-TikTok-debate-digital-growth-vs-cultural-norms) · [AGBI Arabic content TikTok](https://www.agbi.com/analysis/media/2026/02/gulfs-love-for-arabic-content-shields-local-tiktok/) · [Fast Trans dialect choice](https://fast4trans.com/en/choosing-right-arabic-dialect-for-business/) · [Milestone MSA](https://www.milestoneloc.com/modern-standard-arabic/) · [HSToday ISIS AI propaganda](https://www.hstoday.us/featured/is-iskp-supporters-harness-generative-ai-for-propaganda-dissemination/)


---

## F. RESEARCH — Growth mechanics

RANKED GROWTH LEVERS — new/small news account, 2026 (evidence-cited, mapped to Photonect NEWS where relevant)

## 1. Niche authority: one clear beat, not general news (highest-leverage, free)
TikTok in 2026 operates as a topical-authority engine; accounts publishing across 3+ unrelated topics see roughly -45% reach vs single-niche accounts, and Instagram's Explore now evaluates the *whole account's* content history and gives "topical authority" boosts for consistent topics ([Truescho](https://truescho.com/en/blog/instagram-tiktok-algorithm-consistency-2026), [LeeSEOHits](https://leeseohits.com/blog/industry-news/instagram-algorithm-update-2026-new-ranking-factors), [DigitalApplied](https://www.digitalapplied.com/blog/how-social-media-algorithms-work-2026)). Nuance: IG rewards format diversity within one niche; TikTok rewards single-niche obsession with no drift. Implication for @photonect.news: the current 7-bucket topic-diversity rotation (Iraq politics + NBA + tennis + ancient DNA + AI) is exactly the pattern the 2026 algorithms punish on a small account. The evidence favors collapsing to one ownable beat — "Iraq/MENA money & power, explained in Iraqi Arabic" — and treating sports/science as rare exceptions, not slate slots. Both successful news-creator case studies (below) were single-lane.

## 2. Cold-start case studies: personality + one franchise beat volume
- **Dylan Page / News Daddy**: 0 → 7M in under 2 years, 4B+ views; grew by picking one repeatable format (fast conversational news brief, "friend delivering news over coffee"), one recognizable persona/name, targeting stories legacy news undercovers for Gen Z ([Yoof](https://www.yoof.news/dylan-page-another-tiktok-news-start/), [Screenshot Media](https://screenshot-media.com/gen-z-news/dylan-page-news-tiktok-creator/), [Uppercent](https://www.tiktok.com/@uppercent/video/7243733510446517531?lang=en)).
- **V Spehar / Under the Desk News**: ~5M followers across TikTok+IG (3.5M TikTok — nearly 2x NYT); growth built on a fixed visual gimmick (under the desk), daily recap ritual, and a breakout moment (explaining the 25th Amendment during Jan 6) — i.e., a recognizable *show*, not a feed of clips ([Nieman Lab](https://www.niemanlab.org/2026/04/how-v-spehar-built-a-news-business-from-under-a-desk/), [WhatsTrending](https://whatstrending.com/how-v-spehar-and-under-the-desk-news-became-tiktoks-most-trusted-gen-z-news-source/)).
- Generic organic timelines: 10K typically takes 30-90 days, 100K takes 9-18 months; single well-structured videos can hit day-one because TikTok ignores follower count in ranking ([Viryze](https://viryze.com/blog/tiktok-follower-strategy), [Havok Journal](https://havokjournal.com/internet-technology/tiktok-growth-guide-from-0-to-10k-followers-step-by-step/)).
Common thread: every 0→100k news case is a *person or persona* with one format. Faceless polished motion-graphics news has no cited 0→100k case in these results — a strategic gap to note for the essay-engine/voiceover direction.

## 3. Posting cadence: 6/day in one batch is the wrong shape (high-leverage fix, zero cost)
Two separate findings both cut against the current pipeline:
- **Volume**: 2026 consensus for small accounts is 3-5 quality, search-optimized posts *per week* on TikTok and roughly 1/day max on IG Reels; more than 1/day on IG splits engagement and can reduce per-post performance; "topic authority matters more than quantity" ([Ampfluence](https://www.ampfluence.com/how-the-tiktok-algorithm-works-in-2026-and-how-to-beat-it-for-more-reach/), [Hopper HQ](https://www.hopperhq.com/blog/instagram-posting-frequency-2026/), [360uniquizer](https://360uniquizer.com/en/news/instagram-reels-posting-frequency-2026), [FlowShorts](https://flowshorts.app/blog/how-often-to-post-on-tiktok)). Daily 1-3x on TikTok is defensible for speed ([Viryze](https://viryze.com/blog/tiktok-follower-strategy)) but 6/day is above every recommendation found.
- **Spacing**: posting videos back-to-back cannibalizes — the second video competes with the first for the same initial test batch; TikTok takes ~2h to push a video to its first cold audience; recommended gap is 3-5 hours minimum ([Koro](https://getkoro.app/blog/how-long-should-i-wait-to-post-another-tiktok), [CLIMB](https://climbtheladder.com/how-many-tiktoks-can-i-post-a-day-for-best-results/), [JoinBrands](https://joinbrands.com/blog/how-often-to-post-on-tiktok/)).
Concrete change: if 6/day stays, schedule uploads ~3h apart across the day (upload-post scheduling), never batch-fire. Evidence-optimal would be 2-3/day spaced, with the saved render budget moved into depth/engagement. Also: consistency compounds — 20+ active weeks = 5.3x growth multiplier vs casual posting; one silent week costs a sub-10K account 2-6 weeks of recovery ([Truescho](https://truescho.com/en/blog/instagram-tiktok-algorithm-consistency-2026)).

## 4. Caption/search SEO: TikTok and IG are search engines now (cheap, automatable)
TikTok processes ~3B searches/day; it indexes captions, *spoken audio*, on-screen text, and filenames. Caption is the strongest on-page element: front-load the primary keyword in the first 50 characters, write natural search phrases, use 3-5 targeted hashtags (20-30 generic ones now hurt signal clarity) ([EmbedSocial](https://embedsocial.com/blog/tiktok-seo/), [SEO Sherpa](https://seosherpa.com/tiktok-seo/), [Dive Media](https://www.divemedia.com.au/marketing-tips-and-insights/social-seo-keywords-vs-hashtags), [Metricool](https://metricool.com/social-media-seo/)). IG likewise prioritizes real-language captions over hashtag clusters ([ALM Corp](https://almcorp.com/blog/youtube-tiktok-instagram-social-seo-2026/)). Pipeline change: add an Arabic-search-keyword step to caption generation — the exact phrases Iraqis type ("سعر الدولار اليوم", "رواتب الموظفين", "أخبار العراق اليوم") in the first line, and make sure the on-screen headline text carries the keyword too (it's indexed). Rename video files to keyworded slugs before upload.

## 5. Comment-engagement loops (biggest untapped lever for an auto-posting pipeline)
Comment activity is one of TikTok's strongest distribution signals; videos with active discussion get extended FYP distribution vs like-only videos. Tactics with evidence: reply to comments within the first hour (feeds the algorithm's Phase-1 test), pin up to 3 comments (pin a question + your answer to seed more questions; pin a context/follow-up comment to extend the story), and use *video replies* to comments — each reply is a new indexed video with its own distribution, repeatedly called the fastest organic tactic ([ReelForge](https://reelforgeai.io/blog/how-tiktok-algorithm-works-2026-complete-guide), [SocialzAI](https://socialz.ai/blog/how-to-pin-a-comment-on-tiktok), [Conbersa](https://www.conbersa.ai/learn/what-is-tiktok-comments), [StackInfluence](https://stackinfluence.com/blog/tiktok-comment-memes-the-creators-2026-guide)). Right now the pipeline posts and walks away — that discards roughly half the algorithmic value. Concrete: end every reel with one debatable question in the outro; auto-pin a first comment with a question or a "the detail we cut" fact; a daily 30-min pass (or agent) replying in Iraqi Arabic within the first hour; turn the best comment of the week into a video-reply reel (fits the engine — it's just another render).

## 6. Series/franchise naming ("الرقم اليوم", "صار وانت نايم") — validated
A recurring series = fixed name + predictable cadence + recognizable visual cue; each post becomes an episode. Evidence: series packaging measurably lifts retention and follows; IG's 2026 ranking weights multiple-watches-per-session; best names are two words, typeable in a comment, visible in the first 2 seconds of the cover; commit to at least 4 episodes before judging; label "Part 1 of 3" style entries — episode 1 pulls new audiences in ([CreatorFlow](https://creatorflow.so/blog/instagram-content-series-strategy/), [Later](https://later.com/blog/how-to-build-a-signature-content-series/), [SocialPilot](https://www.socialpilot.co/blog/social-media-content-series-guide), [TLO](https://www.tloproduction.com/post/serialized-content-strategy-turning-your-social-feed-into-appointment-viewing)). Both proposed names fit the two-word/ownable pattern. Implementation: 2-3 named daily franchises with fixed intro sting + cover badge + fixed time slot ("صار وانت نايم" = the 7am slot), rendered from dedicated Remotion templates so the visual cue is automatic.

## 7. Follower conversion: give a reason to follow (fixes views-without-follows)
The metric that predicts growth is profile visits per post; if visits rise but follows don't, it's a profile problem — bio must state a specific promise ("your 60-second Iraq briefing, every day at 7") not a vague one; pin 1-3 posts matching the ideal follower's biggest need; end videos with a scheduled-value CTA ("follow — every evening at 7, one minute on Iraq") rather than "follow for more"; open loops ("part 2 tomorrow") convert best ([Mander Marketing](https://mandermarketing.com/blog/how-to-convert-instagram-views-into-followers), [Buffer](https://buffer.com/resources/how-to-get-followers-on-tiktok/), [CloudixDigital](https://cloudixdigital.com/the-hook-body-cta-blueprint-10-short-form-video-scripts-to-master-social-search-and-conversions/)). Series (#6) and fixed time slots are the mechanical way to create this "appointment" promise.

## 8. Cross-platform repurposing: fine, but only clean native uploads
No penalty for cross-posting itself; three things tank reach: watermarks (TikTok logo on IG/Shorts = 40-70% reach drop; both platforms + YouTube run watermark-detection AI that also flags blur/crop removal artifacts), copy-pasted identical captions, and TikTok audio on IG ([Socialync](https://www.socialync.io/blog/avoid-content-duplication-penalties-cross-posting-2026), [SocialKit](https://socialk.it/en/blog/tiktok-watermark-reach-guide), [Joyspace](https://joyspace.ai/stop-reposting-tiktoks-watermark-detection)). IG 2026 also explicitly de-ranks reposted/watermarked and "mass-produced-looking" content ([HeroPost](https://heropost.io/instagram-algorithm-changes-2026/)). The Remotion clean-master pipeline already complies; the gap is captions — generate per-platform caption variants (keyword-led for TikTok search, shorter for IG, thread/plain-text for X). Consider adding YouTube Shorts as a fourth free surface from the same master. On X specifically: links get 50-90% reach suppression, replies are ~13.5x a like's weight, and small-account strategy is reply-driven (10 target accounts, first 15 min) with Premium near-required for reach ([SocialPilot](https://www.socialpilot.co/blog/twitter-algorithm), [Postory](https://postory.io/blog/twitter-reply-strategy), [Graham Mann](https://grahammann.net/blog/how-to-grow-on-x-twitter-2026)) — X is the lowest-ROI leg for a video pipeline; treat as archive unless someone works replies.

## 9. Trial Reels on IG (free A/B for a small account)
Trial Reels show only to non-followers for ~72h, are ranked separately (a flop doesn't drag the account), auto-share to followers if they clear the threshold; Instagram reports 80% of adopters who post more see increased non-follower reach; needs a professional account and ~1K followers ([Instagram Creators](https://creators.instagram.com/blog/instagram-trial-reels), [Fliki](https://fliki.ai/blog/trial-reels-instagram), [Publer](https://blog.publer.com/instagram-trial-reels-guide/)). Perfect fit for testing new formats (essay-engine pilots, new franchises) without burning the main feed.

## 10. Duet/stitch-able content (real but weaker fit)
Stitched/duetted content reaches 30-50% larger audiences per TikTok's Creator Portal; stitches suit commentary/education (~4.8% ER) and brands stitching 2x/week grew followers ~28% faster ([Amra & Elma](https://www.amraandelma.com/duet-and-stitch-tiktok-stats/), [Conbersa](https://www.conbersa.ai/learn/tiktok-stitch-duet-brand-strategy), [ContentMation](https://contentmation.com/marketing/tiktok/tiktok-duet-stitch-strategy)). Two directions: (a) stitch trending Arabic clips with a fact-check/context reel ("الحقيقة وراء المقطع") — strong for a news brand; (b) make reels stitch-able by opening with a bold claim in the first 5s and leaving duet/stitch enabled. Ranked last because it requires human/editorial reactivity the current automated pipeline lacks — but it pairs naturally with lever 5.

MENA context notes: TikTok reach in KSA/UAE is at population saturation and TikTok accounts moved up follower tiers at ~2x Instagram's rate 2025→2026 (16.5% vs 8.9%) — TikTok is the priority growth surface for a new Arabic account; 68% of MENA consumers use social as their main news source, 90% mobile-first; Arabic-first local content is the stated regional trend ([Statista](https://www.statista.com/statistics/1299829/tiktok-penetration-worldwide-by-country/), [SQ Magazine](https://sqmagazine.co.uk/tiktok-statistics/), [GlobalCom PR](https://gcpr.net/blog/how-social-media-transforming-pr-middle-east/), [VeraContent](https://veracontent.com/mix/social-media-middle-east/)).

Caveats: most numeric claims above (e.g., -45% multi-topic penalty, 2.9x duet FYP likelihood, 13.5x reply weight) come from SMM-industry blogs interpreting platform behavior, not platform-published data — treat exact figures as directional; the directional consensus across independent sources is however strong on all ten levers. The three highest-confidence, highest-impact changes for this pipeline: (1) collapse to one beat, (3) space the 6-slate 3h apart or cut to 2-3/day, (5) add a comment-loop layer to auto-posting.

Sources: [Truescho](https://truescho.com/en/blog/instagram-tiktok-algorithm-consistency-2026), [Ampfluence](https://www.ampfluence.com/how-the-tiktok-algorithm-works-in-2026-and-how-to-beat-it-for-more-reach/), [LeeSEOHits](https://leeseohits.com/blog/industry-news/instagram-algorithm-update-2026-new-ranking-factors), [DigitalApplied](https://www.digitalapplied.com/blog/how-social-media-algorithms-work-2026), [HeroPost](https://heropost.io/instagram-algorithm-changes-2026/), [Hopper HQ](https://www.hopperhq.com/blog/instagram-posting-frequency-2026/), [360uniquizer](https://360uniquizer.com/en/news/instagram-reels-posting-frequency-2026), [FlowShorts](https://flowshorts.app/blog/how-often-to-post-on-tiktok), [JoinBrands](https://joinbrands.com/blog/how-often-to-post-on-tiktok/), [Koro](https://getkoro.app/blog/how-long-should-i-wait-to-post-another-tiktok), [CLIMB](https://climbtheladder.com/how-many-tiktoks-can-i-post-a-day-for-best-results/), [EmbedSocial](https://embedsocial.com/blog/tiktok-seo/), [SEO Sherpa](https://seosherpa.com/tiktok-seo/), [ALM Corp](https://almcorp.com/blog/youtube-tiktok-instagram-social-seo-2026/), [Dive Media](https://www.divemedia.com.au/marketing-tips-and-insights/social-seo-keywords-vs-hashtags), [Metricool](https://metricool.com/social-media-seo/), [ReelForge](https://reelforgeai.io/blog/how-tiktok-algorithm-works-2026-complete-guide), [SocialzAI](https://socialz.ai/blog/how-to-pin-a-comment-on-tiktok), [Conbersa comments](https://www.conbersa.ai/learn/what-is-tiktok-comments), [StackInfluence](https://stackinfluence.com/blog/tiktok-comment-memes-the-creators-2026-guide), [Amra & Elma](https://www.amraandelma.com/duet-and-stitch-tiktok-stats/), [Conbersa duet/stitch](https://www.conbersa.ai/learn/tiktok-stitch-duet-brand-strategy), [ContentMation](https://contentmation.com/marketing/tiktok/tiktok-duet-stitch-strategy), [CreatorFlow series](https://creatorflow.so/blog/instagram-content-series-strategy/), [Later](https://later.com/blog/how-to-build-a-signature-content-series/), [SocialPilot series](https://www.socialpilot.co/blog/social-media-content-series-guide), [TLO Production](https://www.tloproduction.com/post/serialized-content-strategy-turning-your-social-feed-into-appointment-viewing), [Socialync cross-posting](https://www.socialync.io/blog/avoid-content-duplication-penalties-cross-posting-2026), [SocialKit](https://socialk.it/en/blog/tiktok-watermark-reach-guide), [Joyspace](https://joyspace.ai/stop-reposting-tiktoks-watermark-detection), [Instagram Creators — Trial Reels](https://creators.instagram.com/blog/instagram-trial-reels), [Fliki](https://fliki.ai/blog/trial-reels-instagram), [Publer](https://blog.publer.com/instagram-trial-reels-guide/), [Nieman Lab — V Spehar](https://www.niemanlab.org/2026/04/how-v-spehar-built-a-news-business-from-under-a-desk/), [WhatsTrending](https://whatstrending.com/how-v-spehar-and-under-the-desk-news-became-tiktoks-most-trusted-gen-z-news-source/), [Yoof — Dylan Page](https://www.yoof.news/dylan-page-another-tiktok-news-start/), [Screenshot Media](https://screenshot-media.com/gen-z-news/dylan-page-news-tiktok-creator/), [Viryze](https://viryze.com/blog/tiktok-follower-strategy), [Havok Journal](https://havokjournal.com/internet-technology/tiktok-growth-guide-from-0-to-10k-followers-step-by-step/), [Mander Marketing](https://mandermarketing.com/blog/how-to-convert-instagram-views-into-followers), [Buffer](https://buffer.com/resources/how-to-get-followers-on-tiktok/), [CloudixDigital](https://cloudixdigital.com/the-hook-body-cta-blueprint-10-short-form-video-scripts-to-master-social-search-and-conversions/), [SocialPilot X](https://www.socialpilot.co/blog/twitter-algorithm), [Postory](https://postory.io/blog/twitter-reply-strategy), [Graham Mann](https://grahammann.net/blog/how-to-grow-on-x-twitter-2026), [Statista](https://www.statista.com/statistics/1299829/tiktok-penetration-worldwide-by-country/), [SQ Magazine](https://sqmagazine.co.uk/tiktok-statistics/), [GlobalCom PR](https://gcpr.net/blog/how-social-media-transforming-pr-middle-east/), [VeraContent](https://veracontent.com/mix/social-media-middle-east/), [Socialync new accounts](https://www.socialync.io/blog/tiktok-algorithm-tips-new-accounts-2026), [Metricool TikTok strategy](https://metricool.com/tiktok-strategy/)


---

## G. TEARDOWNS — Top Arabic formats

# Deep Teardown: The 4 Most Successful Arabic Short-Form News/Explainer Formats

Evidence base: Al Jazeera Media Institute's own video playbook (PDF, the codified AJ+ method), Digiday/Nieman coverage of AJ+, a 2026 Journal of Science Communication study of Arabic explainer channels, Arabic Wikipedia + Playboard analytics for المخبر الاقتصادي, Al Jazeera's own case study of the Da7ee7 audience migration, and Reuters Institute's TikTok-publisher and news-influencer reports. Items marked [documented] are cited; items marked [reconstructed] are anatomy inferred from the documented rules + top-video titles/metadata.

---

## FORMAT 1 — AJ+ عربي: the subtitle-first "emotional news card" video

The archetype every Arabic social-news page copied. AJ+ was the #2 news video producer on all of Facebook by 2015, crossed 1B views across platforms by Oct 2015, and generated 2.2B Facebook video views in 2015 alone, producing ~50 videos/week, most ~1 minute long ([Digiday](https://digiday.com/media/al-jazeeras-distributed-content-unit-generated-2-2-bil-facebook-video-views-2015/), [Wikipedia](https://en.wikipedia.org/wiki/AJ+)). AJ+ عربي launched Nov 30, 2015 with format tiers: "Real Time" breaking (30s–3min), "In Depth", "Short Docs" (6–10min) ([Wikipedia](https://en.wikipedia.org/wiki/AJ+)).

**Anatomy of a top video:**
- **Second 0–1** [documented rule]: the single strongest visual of the story fills the frame — a human face in distress or an astonishing action shot — with a short bold Arabic text overlay stating the emotional core. No VO needed: Al Jazeera's institute playbook mandates "قاعدة الثواني الخمس" (the 5-second rule: what you show first decides whether they stay), "استخدم أقوى العناصر البصرية الممكنة، أثر اهتمام المشاهد عبر نص أو جملة افتتاحية" ([AJ Media Institute guide](https://institute.aljazeera.net/sites/default/files/2018/إنتاج%20الفيديو%20لشبكات%20التواصل%20الاجتماعي.pdf)).
- **What you hear**: often nothing that matters — the playbook designs for sound-off ("صمّم قصتك لتكون ذات مغزى من دون صوت... 85% من الفيديوهات على فيسبوك تشاهد من دون صوت"), music starting where pacing dips, natural sound kept under A-roll [documented].
- **Structure/timeline** [documented]: hook (0–5s) → escalating fact cards synced to footage → emotional peak (victim quote / astonishing stat) → resolution card. Golden rule: "إخبار قصة كاملة بأقل وقت ممكن"; breaking clips ≤120 seconds.
- **VO + dialect**: mostly NO VO; when present, MSA in a deliberately informal register — the playbook orders "التحدث إلى الجمهور مباشرة... بأسلوب متحرر من القيود الرسمية" [documented].
- **Captions**: burned-in large-font Arabic text IS the narration; playbook: watch the final cut at 25% size and ensure text is comfortable — mobile-first [documented].
- **Cuts**: clean, purposeful; playbook explicitly bans decorative transitions/wipes/blurs and screen clutter [documented].
- **Ending/CTA**: a question or a "share this" framing to drive comments/debate [reconstructed from the playbook's engagement-as-success-metric framing].
- **Emotional job**: indignation + empathy + solidarity. The playbook literally instructs "استمِل عواطف الجمهور"; France's INA found three-quarters of AJ+ posts concerned the Israeli–Palestinian conflict or racism/police violence ([Wikipedia](https://en.wikipedia.org/wiki/AJ+)) — outrage/justice is the engine.

**Faceless-AI replicability: HIGH (the highest).** This format is already faceless — it's text-on-footage. An automated channel replicates 100% of the mechanics (hook card, burned text, sound-off design, ≤120s). The two real barriers are non-format barriers: rights-cleared authentic footage of the actual event (AI-generated b-roll weakens the "witness" claim that powers the outrage), and editorial verification speed. This is essentially the format Photonect NEWS already runs.

---

## FORMAT 2 — المخبر الاقتصادي: the faceless MSA voice-over investigation

The largest Arabic economics channel: founded 2018 by Ashraf Ibrahim (PhD economist), ~2.83M subs, ~270M views, 500 episodes at ~2/week, plus an AJ+ co-branded spinoff المخبر الاقتصادي+ ([Arabic Wikipedia](https://ar.wikipedia.org/wiki/المخبر_الاقتصادي), [Playboard](https://playboard.co/en/channel/UC4kRorAXuIkyIX6vwXKaLWg)). Proof that a pure voice, with no face ever shown on camera, can build one of the biggest trust brands in Arabic media.

**Anatomy of a top video** (top recent: "كيف حققت الصين معجزة مبهرة في أخطر مجال طاقة في العالم؟" 508K views; "أخطر تطبيق في روسيا" — [Playboard](https://playboard.co/en/channel/UC4kRorAXuIkyIX6vwXKaLWg)):
- **Second 0–1** [reconstructed]: fast archive/stock montage of the subject + the VO posing the title's question verbatim — a curiosity-gap question with a superlative ("أخطر", "معجزة", "أغنى"). You hear the narrator immediately; the voice IS the brand.
- **Structure/timeline** [documented + reconstructed]: question cold-open → "how did we get here" chronological build with data waypoints → the twist/mechanism reveal → implications for "you/the Arab viewer" → open question ending. Wikipedia describes it as investigative/documentary reports with "data-dependent narratives" — numbers over adjectives.
- **VO + dialect** [documented]: Modern Standard Arabic (فصحى), warm-authoritative single narrator, near-continuous narration (10–30 min episodes).
- **Captions**: minimal subtitles; instead on-screen numbers, maps, charts, highlighted source screenshots [reconstructed].
- **Cuts**: b-roll changes every 2–4s under continuous VO; motion-graphics inserts for every statistic [reconstructed].
- **Ending/CTA**: summary judgment + subscribe prompt + tease of related episode [reconstructed].
- **Emotional job**: curiosity + usefulness + geopolitical intrigue ("what they don't tell you about the economy"), with pride/anxiety about Arab economic standing. Titles are engineered dread/awe ("أخطر مجال طاقة في العالم").

**Faceless-AI replicability: HIGH — this is the closest blueprint for an automated channel.** Everything is pipeline-able: research → question-hook script → TTS/VO → stock+archive assembly → data graphics. The credibility bar is (a) a consistent, high-quality Arabic voice (the audience bonds to the voice the way they bond to a face — voice consistency is non-negotiable), and (b) genuine research depth: the moat is script substance, not visuals. Weakness to exploit: he publishes 2/week in long-form; a daily short-form "mini-Mokhbir" (60–90s, one mechanism per video) is an open lane.

---

## FORMAT 3 — الدحيح (El Da7ee7): the host-persona comedy explainer

The most successful Arabic explainer property ever: Ahmed El-Ghandour, started on YouTube 2014, AJ+ 2017–2020, then New Media Academy; the current channel passed 7.5M subscribers and 1B+ views by May 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Ahmed_El-Ghandour), [iHouse](https://ihouse.ps/blog/472)). A peer-reviewed 2026 JCOM study classifies it as the "humorous" style and finds it produces the strongest positive emotions AND strongest cognitive activation of all Arabic science channels studied — humor did not reduce learning engagement ([JCOM](https://jcom.sissa.it/article/pubid/JCOM_2502_2026_A04/)).

**Anatomy of a top video:**
- **Second 0–1** [reconstructed from documented style]: El-Ghandour mid-energy, direct-to-camera in Egyptian عامية, usually already inside a joke or an absurd question ("يبدأ بطرح تساؤل جذاب" — [Harper's Bazaar Arabia](https://ar.harpersbazaararabia.com/أخبار/أخبار-بازار/كل-ما-تريدون-معرفته-عن-برنامج-الدحيح-2026)); you hear his voice instantly at high tempo. No slow branding.
- **Structure/timeline** [documented]: seductive question → escalating explanation through real examples, historical stories, simplified experiments → recurring comic bits and pop-culture cutaways as breathers → emotional/philosophical landing. Episodes 10–20 min built on "المونتاج السريع والمقاطع التوضيحية والمقارنات الذكية" (fast montage, illustrative clips, clever comparisons).
- **VO + dialect** [documented]: Egyptian colloquial, "rapid narration + cultural references" (JCOM); the dialect intimacy is a core trust device.
- **Captions**: stylized keyword pop-ups and meme inserts rather than full subtitles; the editing template is so distinctive it's sold/cloned on Arab freelance markets ([doros-media](https://doros-media.com/additions-to-the-al-duha-program/)).
- **Cuts**: the fastest in Arabic media — zoom punches, image inserts every sentence, sound-effect punctuation [documented as "fast montage" style].
- **Ending/CTA**: a reflective twist that reframes the whole episode, then outro [reconstructed].
- **Emotional job**: amusement + intellectual pride + social currency ("I learned something and laughed"). JCOM: approval, amusement, caring, admiration.

**Faceless-AI replicability: LOW.** The hardest possible evidence: when Da7ee7 switched host channels in June 2021, New Media Academy's channel went from 9K subs to 650K in one week with 6M added views ([Al Jazeera](https://www.aljazeera.net/ebusiness/2021/6/20/الدحيح-نموذجا-كيف-يمكن-لمؤثر-واحد-أن)) — the audience follows the PERSON, not the format or the brand. The value is the performance: timing, face, dialect improvisation, parasocial trust. An AI can clone the script architecture (question-open, story-ladder, comic breathers — worth stealing for pacing) but a synthetic host attempting this register reads uncanny and gets punished on authenticity. Requires a human.

---

## FORMAT 4 — Sky News Arabia TikTok: the broadcaster breaking-clip machine

The biggest pure-news success in Arabic vertical short-form: 7.5M TikTok followers, 121M likes ([TikTok](https://www.tiktok.com/@skynewsarabia)). The Sky News network strategy rests on four pillars: eyewitness/access footage, being first on breaking moments, explainers, and lives ([Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok)). Notably, per DW's audience-development lead in the same report: "serious news seems to perform more strongly in the Middle East" — Arabic TikTok rewards hard news more than Western markets do.

**Anatomy of a top clip:**
- **Second 0–1** [documented rule + reconstructed]: raw eyewitness or agency footage of the event itself — explosion, flood, official mid-sentence — with a large Arabic headline strip overlay; natural sound up. Reuters Institute: "the first three seconds on TikTok is literally the most crucial — it functions as a modern headline"; people or compelling images must be in frame one.
- **Structure/timeline** [reconstructed]: 15–45s single-event clip: footage → headline overlay → 1–2 context lines → logo end-card. Explainers "start with a question" [documented], run 45–90s, often anchor-fronted.
- **VO + dialect**: frequently none (natural sound + text); when voiced, MSA news register; anchors appear for explainers [reconstructed].
- **Captions**: persistent branded headline bar + short text overlays; MSA [reconstructed from account observation].
- **Cuts**: minimal in breaking clips (the authenticity IS the uncut footage); fast-paced with "minimal pauses between statements" in explainers [documented].
- **Ending/CTA**: none beyond branding — the feed algorithm is the CTA; volume + speed is the strategy.
- **Emotional job**: urgency, fear, shock, being-first. Secondary: trust-through-witnessing (raw footage = proof).

**Faceless-AI replicability: HIGH on format, MEDIUM in practice.** The clip anatomy (footage + headline strip + context lines, no presenter) is trivially automatable and already close to Photonect's reel format. The binding constraint is the input: credible breaking video requires licensed agency/eyewitness footage within minutes — an automated channel without a wire subscription can't win the "first + witnessed" game and shouldn't pretend to (AI-generated "event footage" here is a credibility landmine). Automate the explainer pillar, not the eyewitness pillar.

---

## VERDICT: what a faceless, fully-automated AI channel can credibly own

Frame from Reuters Institute's creator typology (commentary / news+investigation / explanation / specialism): TikTok+IG favor short-form **explanation**, YouTube favors personality **commentary** ([Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/news-creators-influencers/2025/mapping-news-creators-and-influencers-social-and-video-networks)).

**Fully replicable by faceless AI:**
1. **AJ+ anatomy** (text-on-footage emotional news card) — already faceless by design; the format's own playbook (5-second rule, sound-off, ≤120s, emotion-first, clean frames) is a machine-checkable spec.
2. **المخبر anatomy** (MSA voice-over data explainer) — proven that a voice alone builds a top-tier Arabic trust brand; the moat is research depth + a consistent premium voice, both automatable. Biggest open lane: daily 60–90s versions of this anatomy, which nobody dominates.
3. **Sky News Arabia's explainer pillar** (question-open, 45–90s, overlay-driven) — replicable; its breaking/eyewitness pillar is NOT (footage licensing + speed, not format, is the barrier).

**Requires a human:**
4. **الدحيح anatomy** — persona-comedy explainer. The 9K→650K-in-a-week channel migration proves loyalty attaches to the human, not the format. Steal its script architecture (seductive question → story ladder → comic breathers → reframing ending) and its editing tempo, but do not attempt a synthetic host in dialect comedy.

**Synthesis for an automated Arabic channel:** the credible hybrid is المخبر's question-hook + numbers-spine + MSA voice, delivered in AJ+'s sound-off, burned-text, ≤120s emotional packaging, at Sky News Arabia's daily cadence — while explicitly avoiding the two human-only zones: eyewitness-breaking claims and persona comedy.

Sources: [AJ Media Institute video guide (PDF)](https://institute.aljazeera.net/sites/default/files/2018/إنتاج%20الفيديو%20لشبكات%20التواصل%20الاجتماعي.pdf) · [Digiday 2.2B views](https://digiday.com/media/al-jazeeras-distributed-content-unit-generated-2-2-bil-facebook-video-views-2015/) · [Digiday AJ+ YouTube pivot](https://digiday.com/media/early-facebook-video-adopter-aj-is-spending-more-time-on-youtube/) · [AJ+ Wikipedia](https://en.wikipedia.org/wiki/AJ+) · [المخبر الاقتصادي Arabic Wikipedia](https://ar.wikipedia.org/wiki/المخبر_الاقتصادي) · [Playboard analytics](https://playboard.co/en/channel/UC4kRorAXuIkyIX6vwXKaLWg) · [JCOM study on Arabic explainer channels](https://jcom.sissa.it/article/pubid/JCOM_2502_2026_A04/) · [Ahmed El-Ghandour Wikipedia](https://en.wikipedia.org/wiki/Ahmed_El-Ghandour) · [Al Jazeera on Da7ee7 migration](https://www.aljazeera.net/ebusiness/2021/6/20/الدحيح-نموذجا-كيف-يمكن-لمؤثر-واحد-أن) · [Harper's Bazaar Arabia on Da7ee7 format](https://ar.harpersbazaararabia.com/أخبار/أخبار-بازار/كل-ما-تريدون-معرفته-عن-برنامج-الدحيح-2026) · [Da7ee7 editing templates](https://doros-media.com/additions-to-the-al-duha-program/) · [Sky News Arabia TikTok](https://www.tiktok.com/@skynewsarabia) · [Reuters Institute: publishers on TikTok](https://reutersinstitute.politics.ox.ac.uk/how-publishers-are-learning-create-and-distribute-news-tiktok) · [Reuters Institute: mapping news creators 2025](https://reutersinstitute.politics.ox.ac.uk/news-creators-influencers/2025/mapping-news-creators-and-influencers-social-and-video-networks) · [iHouse Da7ee7 stats](https://ihouse.ps/blog/472)


---

## H. THE 100X PLAYBOOK

# THE 100X PLAYBOOK — @photonect.news
### From 2–500 views to viral-capable, without breaking automation or neutrality
*Head of Growth memo · 2026-07-03 · binding for V11 and beyond*

---

## 1. THE DIAGNOSIS

We built a beautiful factory that mass-produces the one product the 2026 algorithm is engineered to reject: a silent, 53-second, seven-topic slideshow that fails TikTok's entrance exam (~13% modeled completion vs a ~35–40% AVD gate) on every single upload, then dumps six of them into one off-peak window where they cannibalize each other, with captions that spoil the video and a comment section nobody staffs. The channel has no voice (killed in V9 over a solvable sync bug), no niche vector (Iraq corruption today, Roland Garros tomorrow — the classifier never learns who we are), no reason to follow (no persona, no series, no question, no local-stakes framing), and no engagement surface — so zero videos ever reach distribution wave 2, which is exactly what "10–160 views" means mechanically. The bitter irony: our own unreleased Essay prototype (VO spine → visuals cut to voice, one narrative arc, moving b-roll) is the correct architecture, and every scaled Arabic winner (الجزيرة 17.8M، المخبر الاقتصادي، AJ+) proves the lane — while the open lane itself ("the Iraqi المخبر: daily 30–60s money-and-power explainers in Arabic") sits unclaimed because the biggest Iraqi news TikTok is still under 1M. Nothing is wrong with our sourcing, brand, or automation; everything is wrong with the retention physics and identity of the unit we automate. We don't need a better factory. We need a different product.

---

## 2. FORMAT V11 SPEC — «الموجز» (The Brief)

**One story. One voice. One question. 30 seconds.** Buildable in Remotion today (`my-video/src/compositions/NewsReel` forked to `NewsReelV11`; Essay comp donates the VO-timeline and counter components).

### Hard parameters
- **Length: 28–34s** (never 40–50s — dead zone). Deep-dive variant 55–60s allowed max 1x/day.
- **FPS/canvas unchanged** (1080x1920, 9:16). Same brand palette (#FFC217 / #D72638 / dark), Tajawal.
- **VO-first pipeline**: script → TTS with word timestamps → `durationInFrames` and every visual cut derived FROM the VO timing JSON. Visuals serve the voice, never the reverse. (This is the Essay engine's architecture, ported.)

### Second-by-second skeleton

| Time | Beat | Spec |
|---|---|---|
| **0.0–1.0s** | Pattern interrupt | NO title card, NO LIVE bar, NO logo. Frame 1 = the story's strongest human-scale image already in motion (fast 8% push-in or lateral pan starts at frame 0) + the hook's key number/word SLAMMING in as kinetic text by frame 10. First frame doubles as cover. |
| **0–3s** | Spoken hook | VO line ≤14 words from the formula bank (below). On-screen text ≤8 words carrying the NUMBER; voice carries the QUESTION. Must pass the mute test. |
| **3–6s** | Context snap + mini-loop | One sentence who/where/when. VO opens a loop: «لكن السبب مو اللي تتوقعه». Visual state change at ~3s. |
| **6–14s** | Escalation 1 | First fact + one stat counter animating up (Essay-style counter component). 2–3 visual states (image swap, crop punch-in, map wipe). |
| **14–15s** | Mid re-hook | VO forward-reference: «والرقم الجاي أخطر». Hard visual cut. |
| **15–23s** | Escalation 2 | Strongest fact LAST. 2–3 more visual states. Attribution burned on-screen (small source chip per claim — this is also our FYP fact-check armor). |
| **23–28s** | Payoff | Resolve the hook's promise with the concrete number/answer. Biggest type moment of the video. |
| **28–31s** | Question card + loop | ONE open question on screen + spoken («برأيك؟ اكتبها بتعليق») over a final frame that color/composition-matches frame 1; music crossfades the boundary for loop. Sources = 1-line micro-strip at bottom (full list moves to pinned comment). |

**Visual state target: ≥10 changes per 30s. No static hold >4s. Ever.** Machine-check this in the QA gate.

### The hook system (rotate, never repeat consecutively)
First-1s VISUAL formulas: (V1) face/crowd push-in + number slam; (V2) animated map strike (Iraq/Hormuz/pipeline route draws itself); (V3) counter already spinning (dinar rate, barrels, casualties); (V4) before/after wipe between two stills.
First-3s SPOKEN formulas (Arabic, ≤14 words):
- H1 رقم صادم: «١٢ مليار دولار طلعت من العراق بشهر واحد — وين راحت؟»
- H2 شنو صار: «شنو اللي صار بأنبوب البصرة الليلة؟»
- H3 السبب المخفي: «ليش أمريكا رجعت شيفرون للعراق هسه بالذات؟»
- H5 جيبك أولاً: «هذا القرار يوصل لسعر البنزين بمحطتك خلال أسبوعين»
- H7 قبل/بعد: «قبل سنة كان الدولار ١٣٢... اليوم القصة تغيرت»
- H10 نداء مباشر: «إذا راتبك بالدينار العراقي، هذا الخبر إلك»
Guardrail: the shock is always the sourced fact, never an adjective. Hook claim MUST resolve inside the video (editorial mandate intact).

### VO architecture
- **One fixed channel narrator — «صوت الموجز»** — the voice IS the brand and makes every upload "original audio" that compounds.
- **Default: ElevenLabs `eleven_multilingual_v2` via `/convert-with-timestamps`** (audio + char-level timing in one call → aggregate to words → feeds Remotion + karaoke). Target: warm-authoritative male, Iraqi-accented. Upgrade path: license an Iraqi narrator for a Professional Voice Clone (one-time cost, do it in month 2 if V11 metrics confirm).
- **Fallback chain** (mirrors KIE-402 pattern): ElevenLabs → Azure `ar-IQ` Bassel (native WordBoundary timestamps, near-free) → HOLD the post and flag in DELIVERY. **Never ship silent again.**
- **Register: عامية بيضاء** — MSA skeleton, Iraqi rhythm. iraqi-copywriter outputs two registers: MSA-leaning body for geopolitics/economy, Iraqi-leaning for hooks/CTAs/local stories. Persian-char guard runs BEFORE TTS.
- **Governance**: TikTok AI toggle + Meta "Made with AI" ON every post (zero distribution penalty, avoids spectral-detection strikes). Voice-only narration — never a synthetic anchor face.

### Captions
Word-by-word karaoke (worth +12–25% AVD alone): white → #FFC217 highlight, RTL-ordered, highlight leads audio by 50–100ms, max 4 words/line, lower-third safe zone. Built once as `<KaraokeCaptions/>` component consuming the timestamp JSON.

### Motion / b-roll (budget: stays ~$5–15/day)
- **Tier 1 (every reel):** stills made kinetic — punch-in crops of the SAME KIE image (3 shots from 1 credit), pan-between-stills, animated maps/counters/charts (free, Remotion-native). This alone hits the 10-state target.
- **Tier 2 (1–2 reels/day, the "hero slots"):** one 4–6s AI video clip (Veo via the Essay pipeline) for the 0–3s hook only — spend motion budget where retention is decided.
- **Tier 3:** real Wikimedia faces for named people (unchanged), archival Commons/Pexels footage where rights-clear (KIE-402 fallback already does this).
- **Never:** AI-photoreal depictions of specific real violent events (moderation landmine). Stylized/illustrative only.

### Music/sound
Suno 4-mood rotation stays but becomes the BED: ducked to −18dB under VO at −3dB. Sidechain duck in the ffmpeg mux step. Whoosh/tick SFX on stat counters (tiny static library, free). No trending audio on hard news, ever.

### Ending/CTA + brand
Rotate three endings: (a) loop-back (last frame ≈ first frame), (b) one question card «برأيك؟», (c) series cliffhanger «الجزء الثاني باچر — تابعنا». One ask max, ≤2s. Brand = small persistent corner logo (Mosseri-confirmed safe) + the narrator's fixed sign-off line: «هذا الموجز. الأرقام تحچي.» — the catchphrase is the anchor a faceless channel gets instead of a face.

---

## 3. NICHE + PROGRAMMING STRATEGY

**We STOP covering:** standalone global sports (Knicks, Wimbledon, Roland Garros), Western human-interest/science one-offs (peanut patch, ancient DNA, Alzheimer's tests), Europe-only stories (heatwaves), generic tech_ai with no MENA angle. These are commodity content where we lose to a thousand bigger accounts, and they scramble our embedding. The 7-bucket rotation is formally dead. Exception rule: any topic earns a slot ONLY via an Iraq/MENA money-power lens (World Cup = Qatar/Iraqi fans economics; chips = Gulf sovereign AI bets).

**The beat we own:** «فلوس وقوة العراق والمنطقة» — Iraq/MENA money & power, explained in 30 seconds, in Arabic that respects your intelligence. This is the open lane: no Iraqi AJ+ exists; biggest Iraqi news TikTok <1M.

**Pillars:**
- **50% Iraq domestic** — oil, dinar, salaries, electricity, corruption, elections, services. Self-relevance is the strongest retention trigger we have.
- **30% MENA/Gulf geopolitics** — Iran, Saudi/UAE, Hormuz, OPEC, US posture — always cabled back to "what it means in Baghdad/Basra."
- **15% economy-through-the-lens** — global moves (chips, oil majors, sanctions) translated to Iraqi stakes.
- **5% wildcard** — one earned curiosity story/week max, still MENA-angled.

**Named franchises (fixed cover badge + intro sting + fixed slot, each its own Remotion prop-preset):**
1. **«الموجز»** — the daily flagship V11 unit (3–4x/day).
2. **«رقم اليوم»** — one number, 30s, why it matters to your pocket. Daily, 8 PM slot. Most shareable unit we'll own.
3. **«صار وانت نايم»** — overnight roundup, 45s, 3 items, 7 AM slot. Appointment viewing; the bio promise.
4. **«الملف»** — weekly 3-part serialized investigation (the corruption-raid instinct, industrialized). Parts labeled ١/٣, cliffhanger endings, fires Sun–Tue.
5. **«الحقيقة ورا المقطع»** — fact-check/context stitch of a viral Arabic clip. 1–2x/week, our only reactive format.

**Cadence: 5/day, SPACED — batch-render at 4 PM, post on a clock.** 7:00 صباحاً («صار وانت نايم») → 12:00 → 17:00 → 20:00 («رقم اليوم») → 22:30. Every slot ≥2.5h apart; weight 5 PM–11 PM Baghdad (MENA usage peak 8 PM–1 AM). Render pipeline unchanged (one `/produce-today` batch); only `upload-post` gains scheduled times. IG gets the best 2–3 of the day only (Meta throttles >1–2/day from small accounts + political-content headwind); TikTok gets all 5; X gets all as archive; add YouTube Shorts as a free 4th surface.

---

## 4. ENGAGEMENT ENGINE

**Comment-bait patterns by story type (final card + caption line 1 — always factual, never partisan):**
- Economy/salaries: «راتبك يتأثر بهذا القرار؟ اكتب محافظتك» (writes geography into comments → geo-signal + volume)
- Corruption/graft: «برأيك، هالمرة القضية توصل للمحكمة لو تنسى مثل كل مرة؟» (binary, debatable, no stance taken by us)
- Geopolitics: «سيناريو أ: تهدئة. سيناريو ب: تصعيد. أنت شنو تتوقع؟» (A/B forecasting bait — opinion is the viewer's, not ours)
- Oil/OPEC: «تعتقد سعر البنزين ينزل فعلاً؟ نرجع نحاسب بعد أسبوع» (creates a callback appointment AND a part-2)
- Services/infrastructure: «عندك كهرباء هسه؟ گللي منطقتك» (lived-experience prompt — highest reply rates in Iraq)

**Pinned-comment strategy (automate in poster):** auto-post comment #1 within 60s of upload containing (a) «التفصيلة اللي ما لحگنا نحطها بالفيديو:» + one extra sourced fact, (b) the full sources list (moved OUT of caption), (c) the question restated. Pin it. This seeds the room, hosts sources without burning caption SEO space, and gives repliers something to argue with.

**Caption SEO rules:** first 50 chars = the exact Arabic search phrase Iraqis type («سعر الدولار اليوم في العراق», «رواتب الموظفين ٢٠٢٦», «أخبار العراق اليوم») + curiosity gap that does NOT duplicate the on-screen headline and does NOT spoil the payoff. No numbers-bullets (they replace the video). 3–5 hashtags total: 1 broad (#العراق), 2 niche (#اقتصاد_العراق #أخبار_المنطقة), 1–2 story-specific. Per-platform variants (TikTok keyword-led / IG shorter / X plain). Rename video files to Arabic-keyword slugs pre-upload (filenames are indexed).

**Share-trigger checklist (QA gate — every reel must tick ≥2):**
☐ One forwardable artifact (a stat card / map / before-after a viewer sends to say "did you see this")
☐ Self-relevance line («يمس راتبك/بنزينك/الدولار بجيبك»)
☐ One "argue-with-me" question
☐ A save trigger (dense payoff card worth re-reading = also a rewatch trigger)
☐ Series hook («الجزء ٢ باچر»)

**The dead-room fix:** a 20-min daily reply pass (or a scheduled reply-agent) in Iraqi Arabic within hour 1 of each post — replies in the first hour feed Phase-1 testing. Best comment of the week becomes a video-reply reel (it's just another render — fits the engine). Bio rewritten to a promise: «موجز العراق والمنطقة — كل يوم ٥ مرات. الأرقام تحچي.»

---

## 5. THE VIRAL SWINGS

**Swing 1 — «المخبر مصغّر»: the Essay engine, weaponized weekly.** Finish the Essay pipeline but change the audio spine: drop the rap (intelligibility risk, register mismatch for news) → the fixed «صوت الموجز» narrator over Veo b-roll + counters, 75–110s, one mechanism per video («ليش الدينار ما ينهار رغم كل شي؟»، «منو يملك نفط العراق فعلاً؟»). Fire 1x/week (Thursday 8 PM), test as IG Trial Reel first. This is the 100K-view ceiling format — المخبر proved the anatomy builds the biggest Arabic trust brands, and he only ships 2 long-forms/week; the daily-short lane is empty. Keep rap as a rare stylistic stunt for soft topics only, pending Ahmed's ear verdict.

**Swing 2 — «عاجل بصوت» speed play.** When a structural MENA event breaks (ceasefire, OPEC decision, dinar move, assassination-scale news), a stripped 20s unit ships within 90 minutes: animated map/flag motion background (no footage claims — we can't win the eyewitness game and mustn't fake it), VO + karaoke + 3 facts + question. Requires the `breaking` CLI path (research → 1 story → render → post, skipping slate). Speed on mega-stories is the single highest-variance lever we possess; every teardown says trending mega-story + fast turnaround is what the most-viral Arabic clips share. Cap: only for events meeting the editorial mandate (≥2 named sources) — attribution on-screen protects us from the unverified-claims FYP block.

**Swing 3 — «الملف» serialized investigations.** The 3-part corruption-raid special was our best instinct all month — industrialize it. One file/week, 3 parts, each ends mid-tension «الجزء الثاني باچر». Series convert follows 3–5x better than one-offs, and part-1 keeps recruiting new viewers for months. Iraqi corruption/money files are an endless, ownable well nobody covers in this format.

Fire order: Swing 2 opportunistically (target: ≥1/week), Swing 3 weekly from week 2, Swing 1 weekly from week 3.

---

## 6. WHAT WE CHANGE IN THE PIPELINE (ordered)

1. **VO module** — `scripts/tts_vo.py`: ElevenLabs `/with-timestamps` → `vo.mp3` + `words.json` per post; Azure ar-IQ fallback; hard-fail = HOLD not silent-ship. Wire into `/produce-today` after copywriter, before render. **EFFORT M · IMPACT 10**
2. **`NewsReelV11` comp** — fork `compositions/NewsReel`; timeline driven by `words.json`; `<KaraokeCaptions/>`; kill the 5s title card; cold-open beat; question end-card; loop-frame matching; ≥10-visual-state layout. Reuse Essay's counter/EQ components. **EFFORT L · IMPACT 10**
3. **Spaced scheduler** — poster reads a slot table (07:00/12:00/17:00/20:00/22:30 Baghdad) and schedules via upload-post instead of batch-firing; also fixes the 429 problem for free. **EFFORT S · IMPACT 8**
4. **Slate collapse** — `/produce-today` research prompt: 7 buckets → 50/30/15/5 pillars, 6→5 posts, every story must pass the "Iraq/MENA money-power lens" test. **EFFORT S · IMPACT 8**
5. **Caption rewrite + pinned comment** — captions module: Arabic-SEO first line, no spoiler bullets, 3–5 hashtags, per-platform variants; poster auto-posts+pins comment #1 (extra fact + sources + question); keyword-slug filenames. **EFFORT S · IMPACT 7**
6. **Hook bank + QA ruleset** — encode the machine-checkable spec (HOOK_FORMULA rotation, MUTE_TEST, LENGTH 28–34, VISUAL_STATES ≥10, MID_REHOOK, share-trigger checklist) into the triple-QA gate in generate-daily. **EFFORT M · IMPACT 7**
7. **Franchise presets** — prop-presets + intro stings + cover badges for الموجز/رقم اليوم/صار وانت نايم/الملف; slate assigns franchise per slot. **EFFORT M · IMPACT 6**
8. **Multi-crop image step** — 3 punch-in crops per KIE image at fetch time (3 shots per credit); AI-label toggles on in poster. **EFFORT S · IMPACT 5**
9. **Audio mix v2** — VO −3dB over bed −18dB sidechain duck + SFX library on counters. **EFFORT S · IMPACT 5**
10. **Reply agent** — scheduled task: fetch hour-1 comments, draft/post Iraqi-Arabic replies within guardrails; weekly best-comment → video-reply render. **EFFORT M · IMPACT 6**
11. **`breaking` CLI path** — single-story fast lane for Swing 2. **EFFORT M · IMPACT 6**
12. **Essay v2 (narrator spine)** — swap rap→narrator VO, cut to 75–110s, weekly cadence + IG Trial Reel flag. **EFFORT L · IMPACT 7**
13. **Metrics harvester** — daily pull of retention/AVD/completion/shares per post into `data/metrics/`, joined to hook-formula + franchise tags, so the Evolution Mandate runs on data, not vibes. **EFFORT M · IMPACT 8 (compounding)**
14. **YouTube Shorts leg** in poster. **EFFORT S · IMPACT 4**

---

## 7. 30-DAY ROLLOUT

**Week 1 — Stop the bleeding (changes 3, 4, 5, 8-partial).** Spaced posting, collapsed slate, SEO captions + pinned comments — all on the CURRENT engine while V11 is built (items 1–2 in parallel). *Metric: median views/post.* Target: 2×-3× baseline → median ≥300, zero <50-view posts. Also watch: profile visits (bio rewritten day 1).

**Week 2 — V11 ships.** VO + karaoke + cold-open + question cards live on all 5 daily slots; QA ruleset enforced; franchises رقم اليوم + صار وانت نايم launch. First «الملف» 3-parter fires Sun–Tue. *Metric: 3-second retention + completion rate (TikTok analytics).* Target: ≥60% past 3s, ≥40% completion on the 30s unit. If completion <30%, the hook bank rotates harder before anything else changes.

**Week 3 — Engagement layer + first swings.** Reply agent live, pinned-comment questions tuned to what's actually getting answered, first «عاجل بصوت» on the week's biggest story, Essay v2 pilot as IG Trial Reel. *Metric: comments+shares per 1K views.* Target: ≥8 engagements/1K views; ≥1 video with 50+ comments; follower growth turns visibly nonzero (≥300 net adds/week).

**Week 4 — Double down on data.** Metrics harvester joins hook formulas × franchises × slots to retention; kill the worst-performing franchise slot, double the best; second «الملف»; Essay v2 goes weekly if Trial Reel cleared threshold. *Metric: outlier count.* Target: ≥2 videos >10K views in the month, ≥1 >25K; median ≥1,000; ≥1,500 total followers. Those numbers = the flywheel has caught; miss them and the retention data tells us exactly which beat of the 30s skeleton is leaking — we fix the component, not the output.

**The bet, in one line:** VO spine + 30s single-story units + one owned beat + spaced posting + a question at the end — the five fixes that turn a factory the algorithm ignores into the Iraqi المخبر nobody has built yet, with zero new manual work for Ahmed.


---

## I. RED-TEAM + FINAL TOP-10

# RED-TEAM: THE 100X PLAYBOOK — @photonect.news

## A. ATTACK FINDINGS

### 1. Breaks automation / hidden daily human labor
- **"20-min daily reply pass"** — explicit daily human labor. Violates the zero-manual-work constraint on its face. The "or a scheduled reply-agent" escape hatch is hand-waved: upload-post is a publish API; reading and replying to comments needs IG Graph API (business token + app review), TikTok's comment API (restricted developer approval), and X API (paid tier). None of that exists in the pipeline today.
- **Auto-pinned comment #1** — pinning comments is not exposed via IG Graph API or TikTok's open API. The whole pinned-comment strategy (sources moved OUT of captions into a comment that may silently fail to post or pin) creates an *attribution regression* against the editorial mandate. If the comment fails, the video ships with a 1-line micro-strip as its only sourcing.
- **Swing 2 "ship within 90 minutes"** — requires a 24/7 event-detection daemon plus autonomous verification of assassination-scale news with zero human review. The pipeline is a once-daily manually-triggered `/produce-today`. The slow step in "≥2 named sources" is verification, which is exactly what a 90-minute SLA compresses. This is the highest-variance lever *and* the highest-probability channel-killer.
- **Metrics harvester** — TikTok retention/AVD/completion is not available via public API without an approved developer app; IG insights need Graph API onboarding. The playbook scores this "M"; realistically it's M-L with an external approval dependency, or it degrades to views/likes/comments only. The Week-2 gate ("≥60% past 3s, ≥40% completion") depends on data the pipeline cannot yet fetch.
- **Voice clone in month 2** — "license an Iraqi narrator" = sourcing, negotiating, recording, and paying a human. That is a project, not a line item.

### 2. Faceless-AI credibility limits
- **The Iraqi-dialect VO is the weakest load-bearing assumption.** VO was killed in V9 as "not Iraqi." The playbook's fix is to *target* "warm-authoritative Iraqi-accented" from ElevenLabs multilingual — but the hooks are written in dialect («شنو», «هسه», «باچر», «تحچي» with چ/گ), which is precisely where TTS mangles pronunciation. A near-Iraqi voice that misses is worse for trust than clean MSA newscast register, which Iraqi audiences fully accept for hard news (it's what الجزيرة and المخبر use). The playbook conflates "Iraqi identity" with "Iraqi-dialect TTS" — the first is achievable via framing and stakes; the second is unproven with current tools. Note the Persian-char guard memory exists because Arabic text handling already bites this pipeline.
- **«الحقيقة ورا المقطع» (fact-check stitch)** — stitching is a native in-app TikTok feature, not available through upload-post; re-using a third-party viral clip raises rights issues; and a faceless AI channel fact-checking humans invites exactly the pile-on the brand can't survive. Infeasible and risky.
- **AI-drafted Iraqi-Arabic auto-replies** — Iraqis clock robotic dialect fast. A visibly-bot reply account under every video is worse than a quiet one.

### 3. Claims not supported by evidence
- "~13% modeled completion vs ~35–40% AVD gate", "karaoke worth +12–25% AVD", "series convert 3–5x better", "biggest Iraqi news TikTok <1M", "zero distribution penalty for AI labels" — all uncited or modeled. The AI-label claim is actively contested: labeled synthetic *political/news* content on Meta faces political-content reach limits regardless; keep the labels (mandatory anyway) but budget for a reach tax, don't promise zero.
- **Week-4 targets are fantasy pacing**: from median ~30 views to median ≥1,000, ≥2 videos >10K, +1,500 followers in 30 days, on a new voice format. Setting these as "the flywheel has caught" thresholds guarantees a declared failure and an Evolution-Mandate thrash cycle. Realistic 30-day success: median 300–500, one 3–5K outlier, retention data flowing.

### 4. Brand / neutrality violations *inside the playbook itself*
- Comment-bait template «...لو تنسى مثل كل مرة؟» ("or forgotten like every time?") embeds a cynical editorial claim about Iraqi courts — that's a stance, and it violates the mandate the playbook swears it preserves. Hook «وين راحت؟» over $12B is insinuation-by-question. Each template needs the same copywriter/QA pass as body copy.
- Fixed-slot "appointment" franchises (7 AM «صار وانت نايم») make a public promise; one failed overnight render breaks it visibly. The pipeline's own history (KIE 402s, upload-post 429s) says renders fail.

### 5. Cost check ($5–15/day)
- ElevenLabs: ~5 × 450 chars/day ≈ 70K chars/month → Creator tier ~$22/mo. Fine.
- Veo hero clips 1–2/day: fine only on fast tier and only if capped — 2/day quality-tier plus a weekly 75–110s Essay (15–20 clips) blows the ceiling. Budget forces: 1 hero clip/day max OR the weekly Essay, not both at quality tier.
- Multi-crop (3 shots/credit) is the single best cost move in the doc. Keep.

### 6. Pipeline reliability
- 14 changes + 5 franchises + 3 swings in 30 days onto a pipeline that stabilized auto-posting six days ago. The riskiest coupling is the new spine itself: TTS timestamp JSON drives `durationInFrames` and every cut — one malformed timestamp breaks *every* render. The HOLD-not-silent fallback is correct; it needs golden-sample tests before it gates 5 posts/day.
- Five franchise presets = 5x prop schemas, 5x QA surface, week 2. Launch two.
- "Mute test" is not machine-checkable and will rubber-stamp; keep only enforceable rules (length, visual-state count from props, hook-formula rotation, char guards, source count).

## B. KILL / DOWNGRADE LIST
- **KILL**: reply agent + video-reply reels (API-gated, bot-smell); «الحقيقة ورا المقطع» (infeasible stitch); pinned-comment *pinning* (keep sources in caption tail; attempt plain comment #1 best-effort); voice-clone licensing (defer indefinitely); loaded comment-bait templates (rewrite through iraqi-copywriter).
- **DEFER**: Swing 2 breaking lane until ≥4 weeks of stable V11 metrics AND a verification gate design (this is the channel-death vector); 5-franchise rollout → 2 franchises.
- **REWRITE**: dialect VO → MSA newscast VO default, dialect limited to on-screen hook text; Week-4 targets → median 300–500, 1 outlier >3K; AI-label claim → "mandatory, expect a reach tax on political content."

## C. FINAL TOP-10 (prioritized)

| # | What | Why top-10 | Effort | Views impact | Ship |
|---|---|---|---|---|---|
| 1 | **V11 VO spine** (playbook 1+2+9 merged): `tts_vo.py` ElevenLabs-with-timestamps → Azure ar-IQ fallback → HOLD; `NewsReelV11` comp driven by `words.json`; karaoke captions; cold open; question end-card; sidechain-ducked bed. **MSA newscast register** for VO; dialect only in on-screen text. Golden-sample render test before it gates production. | The only change that attacks retention physics directly; everything else is multiplicative on it | L | High — this is the completion-rate fix | W1–2 |
| 2 | **Slate collapse to Iraq/MENA money-power pillars** (50/30/15/5), 6→5 posts, lens test in research prompt | Fixes classifier identity + self-relevance retention; pure prompt change, zero pipeline risk | S | Med-High | W1 |
| 3 | **Spaced scheduler** — 5 slots via upload-post scheduling if supported, else local cron per slot; kills self-cannibalization and the 429 problem | Cheapest distribution fix; current single-window batch is provably self-harming | S | Med | W1 |
| 4 | **Caption rewrite** — Arabic-SEO first line, no spoiler bullets, 3–5 hashtags, per-platform variants, keyword-slug filenames. **Sources stay in caption** (attribution must not depend on a comment API). Best-effort unpinned comment #1 only. | Current captions replace the video; fix is script-only | S | Med | W1 |
| 5 | **Machine-checkable QA v2** — length 28–34s, ≥10 visual states (from props), hook-formula rotation log, Persian-char guard pre-TTS, ≥2 share-triggers, source count. Drop unenforceable "mute test" as a gate. **Neutrality lint extended to hooks/CTAs/comment templates** | Protects the mandate from the playbook's own bait patterns; prevents silent format drift | M | Med (defensive) | W2 |
| 6 | **Multi-crop kinetic stills** — 3 punch-in crops per KIE credit + pan-between-stills + Remotion-native maps/counters; **Veo capped at 1 fast-tier hero clip/day** | Hits the 10-state target at ~zero marginal cost; enforces the budget ceiling | S | Med | W2 |
| 7 | **Two franchises only** — «الموجز» (flagship) + «رقم اليوم» (20:00). «صار وانت نايم» and its 7 AM promise wait until slot reliability is proven | Series identity without 5x QA surface or a breakable public appointment | M | Med | W3 |
| 8 | **Metrics harvester, honest scope** — pull whatever upload-post/IG Graph expose (views, likes, comments); start TikTok developer-app application now for retention data later; join to hook-formula tags | Evolution Mandate needs data, but W2 retention gates must not block on unavailable APIs | M | Compounding | W2–3 |
| 9 | **«الملف» weekly 3-parter** — industrialize the corruption-special instinct; parts ١/٣ with cliffhangers, Sun–Tue | Proven internal signal (best experiment to date), pure content-config on the V11 engine | M | Med-High | W3 |
| 10 | **Essay v2, narrator spine, weekly** — rap dropped for the fixed narrator; 75–110s; Thursday slot; budget-gated (skip a daily hero clip that week) | The 100K-ceiling format, but only after the daily unit and voice are proven | L | High-variance | W4 |

Explicitly cut from the original 14: reply agent (#10), breaking CLI (#11 — deferred behind a verification-gate design), fact-check franchise, 5-franchise rollout, pinning, voice clone. YouTube Shorts leg (#14): do it whenever, it's an afternoon — not a top-10 slot.

## D. THE ONE THING
**Ship the VO spine (item 1): a 28–34s single-story unit where a timestamped MSA narrator drives every cut, with karaoke captions and a cold open.** Every credible mechanism in the playbook — completion rate, mute-proof retention, original-audio identity, franchise stings, the Essay upgrade, even the breaking lane — is a multiplier on that one unit. Nothing else in the document works while the product is a silent 53-second slideshow, and almost everything else still works if it's the *only* thing that ships this month. The one modification to the playbook's version: MSA newscast voice first, Iraqi dialect only on screen — the channel died once already on a voice that wasn't Iraqi enough, and an almost-Iraqi TTS voice repeats that mistake; a clean broadcast MSA voice does not.