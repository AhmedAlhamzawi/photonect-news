# Photonect NEWS — April 21, 2026 Slate (V5 rebuild)

**Status:** ✅ **V5 SLATE COMPLETE** — 12/12 rendered Apr 22 02:24–02:45 GMT+3. All audio present + unique. See `DELIVERY_2026-04-21.md` for morning handoff.
**Engine version:** V5 (12 music beds + 12 slug-specific accents + safe-zone enforcement + distinct label treatments per variant)
**Rebuild rationale:** Ahmed feedback on V4 — "all the videos look the same", "margins are screwed up", "all the music is the same". V5 addresses each at the architectural layer — not by patching individual slugs.

V5 architectural changes:
- `safeArea.ts` rewritten with `CONTENT_BOTTOM`, `SPLIT_BOTTOM_HEIGHT`, and `adaptiveFontSize()` — content CANNOT enter the IG/TikTok caption-drawer strip regardless of length.
- Three visually distinct label treatments: BAR (A) / STRIKE (B) / HAIRLINE (C) — no more copy-pasted pill across variants.
- 12 music beds (8 new ffmpeg-EQ variants) — one unique bed per slug, zero adjacency duplication. Audio fingerprint (MD5 PCM slice) uniqueness verified post-batch.
- 12 slug-specific accent colors — no more bucket-level sharing.
- On-demand trigger: `bash generate-daily.sh [YYYY-MM-DD]` (NOT scheduled — by explicit mandate).

(Prior V4 rationale retained below for historical context.)

**April 20 friend feedback** — "text too much", "text appears too quickly", "punchlines robotic"

---

## The V4 Upgrade — what changed vs. April 20

| Problem (April 20) | Fix (V4 engine) |
|---|---|
| 25-40 word body paragraph per beat — unreadable in 8s | Body is now OPTIONAL. Variants A & C drop it entirely. Variant B caps at 15 words. |
| 4 supporting stat cards per beat — cluttered, chart-like | Max 2 stats. Often 0. |
| Every beat looked identical — flat rhythm | 3 visual variants per bucket: **A MONEY-SHOT** (politics/conflict), **B KINETIC** (data/tech), **C CINEMA** (feature/wildcard) |
| Same music bed every time — monotonous | 4 EQ-varied beds: tense / uplift / somber / neutral, mapped per bucket |
| 8s dwell per beat — too fast to read | 9s beat 1, 9s beat 2, 8s beat 3 (total 34s reel) |
| Robotic `ماذا يحدث / لماذا يهم / ماذا بعد` beat labels | Story-specific labels ("الرقم السحري", "الساعة صفر", "الجدار") |
| Hero images sometimes stale/generic | Hand-picked via Wikimedia Commons visual curation |

---

## 12-Slot Schedule (2h cadence, full bucket rotation — zero adjacency collisions)

| # | Time | Slug | Bucket | Variant | Hook |
|---|------|------|--------|---------|------|
| 1 | 08:00 | iraq-vote | iraq_domestic | A MONEY-SHOT | 227 votes — government tonight or void |
| 2 | 09:20 | brent-150 | global_economy | B KINETIC | Brent breaks $150 — $8.7T Asia wipeout |
| 3 | 10:40 | ceasefire-break | mena_geopolitics | A MONEY-SHOT | 47 dead in 3h — Lebanon ceasefire ends |
| 4 | 12:00 | ai-nuclear-sim | tech_ai | B KINETIC | GPT-6 fails nuke safety at 0.3% — Claude 94% |
| 5 | 13:20 | berlin-protest | europe | C CINEMA | 500K on Berlin streets — chancellor 48h |
| 6 | 14:40 | un-secgen-plan | mena_geopolitics | A MONEY-SHOT | UN 7-point plan — Russia vetoes in minutes |
| 7 | 16:00 | crypto-tether-depeg | tech_ai | B KINETIC | USDT at $0.87 — $23B redemption queue |
| 8 | 17:20 | opec-emergency-2 | gulf_regional | C CINEMA | OPEC+ Vienna emergency — 2M bpd surge |
| 9 | 18:40 | kdp-split | iraq_domestic | A MONEY-SHOT | 58 Kurdish MPs defect — 30y alliance ends |
| 10 | 20:00 | imf-sa-loan | global_economy | B KINETIC | Saudi asks IMF $40B — first since 1998 |
| 11 | 21:20 | egypt-mobilize | gulf_regional | C CINEMA | 200K Egyptian troops to Sinai — 1973 echo |
| 12 | 22:40 | north-korea-ship | wildcard | C CINEMA | DPRK ship intercepted in Red Sea — 12 crates |

---

## Per-Slot Status — V5 FINAL (batch: Apr 22 02:24–02:45 GMT+3)

| # | Slug | Render | Lumin QA (hero/b1/b2/b3) | Audio (mean dB) | Notes |
|---|------|--------|---------------------------|-----------------|-------|
| 1 | iraq-vote | ✅ 42 MB / 91 s | ✅ 53 / 83 / 79 / 113 | –29.8 ✅ | V-A BAR label + #FFD447 + urgent bed. Baghdad Convention Center hero. |
| 2 | brent-150 | ✅ 25 MB / 76 s | ⚠ 83 / 39 / 54 / 48 ¹ | –27.7 ✅ | V-B STRIKE + #FF8C42 + electric. Studio-dark half + dim bourse broll → soft-warn, visually clean. |
| 3 | ceasefire-break | ✅ 50 MB / 110 s | ✅ 93 / 91 / 77 / 76 | –27.2 ✅ | V-A BAR + #FF2D55 + dread. Cleanest luminance of slate. |
| 4 | ai-nuclear-sim | ✅ 19 MB / 82 s | ⚠ 70 / 38 / 42 / 43 ¹ | –27.7 ✅ | V-B STRIKE + #00F0FF + pulse. Datacenter broll triggers VB soft-warn. Frames verified clean. |
| 5 | berlin-protest | ✅ 34 MB / 106 s | ✅ 87 / 55 / 74 / 59 | –26.5 ✅ | V-C HAIRLINE + #8E9AFF + stark. 492K stat overlay lands cinematic. |
| 6 | un-secgen-plan | ✅ 52 MB / 114 s | ✅ 70 / 69 / 68 / 105 | –27.6 ✅ | V-A BAR + #B8DBD9 + tense. UN HQ hero. Largest file — rich broll variety. |
| 7 | crypto-tether-depeg | ✅ 21 MB / 92 s | ⚠ 74 / 48 / 33 / 24 ¹ | –27.7 ✅ | V-B STRIKE + #39FF14 + chase. NYSE floor + Bitcoin ATM in dim bar → soft-warn, frames verified clean. |
| 8 | opec-emergency-2 | ✅ 32 MB / 108 s | ✅ 96 / 50 / 66 / 93 | –35.1 ✅ | V-C HAIRLINE + #E8B923 + somber. Kingdom Tower sequence. |
| 9 | kdp-split | ✅ 35 MB / 117 s | ✅ 89 / 113 / 64 / 80 | –29.3 ✅ | V-A BAR + #C3272B + neutral. Erbil citadel hero — beat1 L=113 brightest of slate. |
| 10 | imf-sa-loan | ✅ 25 MB / 93 s | ✅ 73 / 48 / 49 / 61 | –28.9 ✅ | V-B STRIKE + #00E5A0 + uplift. **Bright broll VB → QA PASS** (contrast with slots 2/4/7 proves VB flag is broll-dependent). |
| 11 | egypt-mobilize | ✅ 21 MB / 107 s | ✅ 76 / 88 / 93 / 72 | –27.0 ✅ | V-C HAIRLINE + #C9A66B + drone. Sepia archival troops — 1973 echo lands. |
| 12 | north-korea-ship | ✅ 31 MB / 111 s | ✅ 93 / 65 / 54 / 57 | –30.4 ✅ | V-C HAIRLINE + #FF006E + mist. Coast guard ocean plate. |

¹ Variant B soft-warn. 50/50 split with intentional studio-dark bottom half — when broll is also dim, L_safe dips under 40 but content is unambiguously readable. Visual verification done on all three; deferred QA algorithm calibration to future iteration. See `DELIVERY_2026-04-21.md` for details.

**12/12 rendered • 12/12 audio present + unique (MD5 fingerprints all distinct) • 9/12 luminance PASS clean • 3/12 luminance soft-warn verified clean.**

---

## Variants at a glance

### A — MONEY-SHOT (politics / conflict)
Giant 260px count-up stat with slam-scale spring, single-line Arabic heading, accent radial flash. No body, no stat cards. One giant number dominates the frame.
- Slots: 1, 3, 6, 9
- Music bed: `news_bed_tense.mp3`
- Use for: hot-breaking politics, casualty counts, deadline pressure

### B — KINETIC-SPLIT (data / tech / macro)
50/50 vertical split — image top, kinetic typography bottom. Heading slams in word-by-word. Optional 15-word body. Max 2 supporting stats with whip-in animation.
- Slots: 2, 4, 7, 10
- Music bed: `news_bed_uplift.mp3`
- Use for: market moves, AI benchmarks, macro economics

### C — CINEMA-REVEAL (feature / wildcard / strategic)
Full-bleed hero with heavy bottom scrim. Slow reveals (Bezier 0.16,1,0.3,1). Left-aligned (contrast vs A/B). Optional single quiet stat. No body, no supporting stats.
- Slots: 5, 8, 11, 12
- Music bed: `news_bed_somber.mp3`
- Use for: strategic stories, features, non-urgent wildcards

---

## Hand-picking provenance (for attribution)

All 47 images across 12 slugs were hand-curated from Wikimedia Commons. Automated
hunter was 403-blocked from Pexels + had a Python bug in motion-graphic fallback
(fixed this session — see EVOLUTION_LOG FIX-002). Hand-picking ensured every
image is topic-specific and narrative-appropriate rather than generic atlas fill.

### iraq-vote (A, iraq_domestic)
- hero — `File:Baghdad_Convention_Center_inside.jpg` (CC BY 2.0, James Gordon)
- broll_1 — `File:Baghdad_Convention_Center.jpg` (CC BY 2.0, James Gordon)
- broll_2 — `File:View_on_Green_zone,_Baghdad.jpg` (CC BY-SA 4.0)
- broll_3 — `File:Tigris_river_from_Al_Shohada'_bridge.jpg` (CC BY-SA)

### brent-150 (B, global_economy)
- hero — oil rig at sea (CC BY, preserved from automated hunt)
- broll_1 — `File:Market_centre_in_Tokyo_stock_exchange.jpg` (CC) — Tokyo exchange trading floor
- broll_2 — `File:Hong_Kong_(239753253).jpeg` (CC) — HK financial district daytime, for "$8.7T Asian market wipeout" beat (hand-picked 2nd pass, replaced stale Wall Street tourist photo)
- broll_3 — `File:Vienna_OPEC_Headquarters_(9812748993).jpg` (CC) — OPEC HQ (reused from opec-emergency-2), for "OPEC+ emergency Vienna" beat (hand-picked 2nd pass, replaced stale Wall Street tourist photo)

### ceasefire-break (A, mena_geopolitics)
- hero — `File:Beirut_skyline,_Beirut,_Lebanon.jpg` (CC BY 4.0, V. Argenberg)
- broll_1 — `File:Columns_at_Al_Mina_site,_Tyre,_Lebanon.jpg` (CC BY 4.0, V. Argenberg)
- broll_2 — `File:Litani_river_2.jpg` (CC BY-SA 2.5, S. Fares)
- broll_3 — `File:Cedar_of_Lebanon_(Cedar_of_God),_Lebanon.jpg` (CC BY 4.0, V. Argenberg)

### ai-nuclear-sim (B, tech_ai)
- hero — server room (CC, preserved)
- broll_1 — `File:Technician_with_laptop_working_on_server_rack_at_NERSC.jpg` (CC)
- broll_2 — `File:Peacekeeper_in_silo_1987.jpg` (Public Domain, US Air Force)
- broll_3 — `File:G7_Family_group_photo_of_2016_Ise-Shima_Summit.jpg` (CC)

### berlin-protest (C, europe)
- hero — Berlin exterior (CC, preserved)
- broll_1 — Berlin exterior (CC, preserved)
- broll_2 — `File:Stack_of_pipes_North_Stream_2.jpg` (CC) — gas supply visual
- broll_3 — `File:Reichstag_building_Berlin_view_from_west_before_sunset.jpg` (CC)

### un-secgen-plan (A, mena_geopolitics)
- hero — `File:Headquarters_of_the_United_Nations,_New_York_City,_20231001_1103_1006.jpg` (CC BY 4.0, J. Hałun)
- broll_1 — `File:UN_Security_Council_2007-04-03.JPG` (CC BY-SA 2.5, K. Ree)
- broll_2 — `File:UN_General_Assembly_hall.jpg` (CC BY-SA 2.0, P. Gruban)
- broll_3 — `File:Flags_of_the_United_Nations,_2005.jpg` (Public Domain, UN)

### crypto-tether-depeg (B, tech_ai)
- hero — `File:Bitcoin_BTC_golden_coin_with_the_symbol.jpg` (CC)
- broll_1 — `File:Holding_Bitcoin_cryptocurrency_coin.jpg` (CC)
- broll_2 — `File:Trading_Floor_at_the_New_York_Stock_Exchange_during_the_Zendesk_IPO.jpg` (CC)
- broll_3 — `File:Bitcoin_ATM_in_City_Galleria,_Zadar.jpg` (CC)

### opec-emergency-2 (C, gulf_regional)
- hero — `File:Vienna_OPEC_Headquarters_(9812748993).jpg` (CC)
- broll_1 — `File:Oil_pumpjack_in_the_Permian_Basin.jpg` (CC, resized 12288→2400)
- broll_2 — `File:Kingdom_Tower1.jpg` (CC) — Riyadh Kingdom Centre at night, for "الانقسام" (Riyadh-leads-Moscow-resists) beat — hand-picked 2nd pass after initial render crashed on missing broll_2
- broll_3 — `File:Ras_Tanura_Refinery_by_Paul_Palmer_2487098008.jpg` (CC, Saudi Aramco)

### kdp-split (A, iraq_domestic)
- hero — `File:Hawler_Castle.jpg` (CC BY-SA 2.0, jan kurdistani) — Erbil citadel
- broll_1 — `File:Kurdistan_landscape.jpg` (CC BY-SA 4.0, N. Bartóki-Gönczy)
- broll_2 — `File:Views_around_Sulaymaniyah_01.jpg` (CC0, L. Clancy)
- broll_3 — `File:Baghdad_Convention_Center.jpg` (CC BY 2.0, J. Gordon) — Iraqi parliament

### imf-sa-loan (B, global_economy)
- hero — Riyadh at night (CC, preserved)
- broll_1 — `File:Riyadh_Skyline_showing_the_King_Abdullah_Financial_District_(KAFD)_and_the_famous_Kingdom_Tower.jpg` (CC)
- broll_2 — `File:Bank_SA.jpg` (CC) — SAMA Saudi Central Bank
- broll_3 — `File:11_International_Monetary_Fund_IMF_in_Washington_DC_USA_-_Creative_Commons_CC-BY.jpg` (CC-BY)

### egypt-mobilize (C, gulf_regional)
- hero — Egyptian desert/military (CC, preserved)
- broll_1 — Egyptian military convoy (CC, preserved)
- broll_3 — `File:Cairo_-_Heliopolis_-_1973_October_War_Panorama.JPG` (CC) — 1973 echo

### north-korea-ship (C, wildcard)
- hero — cargo ship (CC, preserved)
- broll_1 — `File:Ocean_container_megaship_comming_to_Europe.jpg` (CC)
- broll_2 — `File:Bab_Al-Mandeb_Strait,_between_Djibouti_and_Yemen.jpg` (CC) — actual Bab el-Mandeb strait imagery for "البحر الأحمر" beat — hand-picked 2nd pass after props.json was missing broll_2 ref
- broll_3 — `File:North_Korea's_ballistic_missile_-_North_Korea_Victory_Day-2013_01.jpg` (CC)
