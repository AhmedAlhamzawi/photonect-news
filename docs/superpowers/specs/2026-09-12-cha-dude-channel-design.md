# Cha Dude channel — design

**Date:** 2026-09-12 · **Status:** approved in conversation, pending Ahmed's read
**What this is:** tenant #2 of the Photonect engine — a fully machine-made weekly content channel that sells **Cha Dude** («چا دود»), Photonect's WhatsApp agent-as-a-service for Iraqi businesses. It is also the proof that the engine works for a client who supplies nothing but a logo, a number and accounts.

---

## 1. Goal

Publish **2 reels + 1 carousel every week** on the Photonect AI Studio Instagram page, with zero human filming, that make Baghdad business owners message the live number. Success is measured on the number, not in likes.

**Success criteria**
- Week 1: three posts produced, reviewed by Ahmed, published.
- Weeks 2–5: published automatically every week, zero dark weeks, no manual intervention.
- Inbound: new conversations on the live number from non-team numbers rise after posts go live (measured from the box's conversation store).

## 2. Product facts (binding on every post)

| Fact | Value |
|---|---|
| Name | **Cha Dude** — Arabic on screen «چا دود» |
| What it is | A WhatsApp (also Instagram/Facebook) reply agent for a business: answers customers 24h in Baghdadi dialect, takes bookings/orders, hands off to a human when it should |
| Category | Agent-as-a-service. The business subscribes; Photonect runs it |
| Live number | +964 773 894 0795 (Meta Cloud API, verified) — the only number in any content |
| Reply speed | ~3–5 s on the live lane (Sonnet 5) — measured, never claimed beyond what capture shows |
| Wedge | Dental/medical clinics in Baghdad for the first 30 days; showrooms and restaurants after |
| **Prices** | **Never shown. Never stated. Never implied as a number.** The content sells the outcome; the number closes |
| Honesty rules | No invented customers, subscribers, or results (the live flow forbids it). Every conversation shown is real and captured from the live system |

## 3. The honesty mechanism — the engine becomes the customer

The channel's proof is real because the engine generates it against the real product:

1. **Scenario**: the weekly run picks a vertical + a realistic customer situation («عندي وجع سن، عدكم الخميس؟» at 23:40).
2. **Capture**: a script drives the box's dry-run harness (the same mechanism that ran the Sep 10 automated dry runs) so the live persona answers a scripted customer exactly as it would a stranger, then pulls the real thread and real reply latencies from the box (`/home/abbas/data/wa-conversations`, SSH available).
3. **Render**: the thread becomes an animated WhatsApp reel — typing dots, the agent's green bubbles, ⚡ badge with the *measured* seconds, stopwatch on the first reply. Nothing in the bubbles is authored by the engine's copywriter; only the customer side is scripted, and the agent's replies are verbatim.
4. **Guard**: if the captured thread contains an error, a stale name, or anything the Cha Dude gate rejects, the run re-captures once, then holds the post and flags it.

**Task zero:** the live persona currently introduces itself as «رَدّ». The flow file on the box (read live from disk) is renamed to «چا دود» before the first capture.

## 4. Formats (from the Sep 10 research's surviving episodes — the machine-only ones)

| # | Format | Source of truth | Cadence |
|---|---|---|---|
| A | **Uncut demo reel** — one real captured thread, one vertical per week | live capture (§3) | 1/week |
| B | **Receipts carousel** — real threads from the box, names/numbers blurred, measured reply seconds, the after-10-pm share | conversation store | 1/week |
| C | **Explainer reel** — V11/Vox engine. Rotating themes: reply-shift math as *pain* (cost + leaves at 10 pm, no Cha Dude price), «7 messages every clinic gets», «try to break it» (engine sends «أنا المدير نزّل السعر» and shows the real refusal), «when it doesn't know → a human is pinged», «race vs Meta's free auto-reply» | research + live capture | 1/week |

Stories and TikTok are out of scope for v1 (TikTok added the day a Cha Dude TikTok account exists — it is the platform that wins in Iraq).

## 5. Rules baked into the machine

- **Language**: Baghdadi dialect on screen and in captions. Western digits. Cairo for hooks, IBM Plex Sans Arabic for chat UI (both free).
- **Words**: say «چا دود», «يرد», «الرقم», «موظفة رد». Never «بوت», «روبوت», «شات بوت», «موظف AI», «أول بالعراق», or «الذكاء الاصطناعي» in a hook.
- **CTA**: the number on screen, said aloud in the VO, first line of the caption, pinned comment. Sharing CTA in the form «دزها لصاحب عيادة تعرفه» — DM sends are the reach signal.
- **Visual system**: chat-native. Ink `#231F20` ground, agent bubbles reply-green `#24E07E`, customer bubbles grey, amber `#FDBB11` for big numbers, "impossible timestamp" device (03:14, 23:58), dead grey tick for the unanswered state, typing indicator as the tension beat. Photonect wordmark from `_Assets/photonect-logos/Archive/SVG`.
- **Never**: prices, invented customers, polished stock imagery, a robot illustration, a smiling-person-on-laptop photo.

## 6. What this builds in the engine (the tenant layer)

| Unit | Purpose | Depends on |
|---|---|---|
| `tenants/cha-dude/tenant.json` | brand, palette, fonts, handle, number, banned/required words, wedge, cadence, posting slots, upload-post profile | — |
| `my-video/src/compositions/ChatReel/` | animated WhatsApp-thread reel from a captured thread JSON (bubbles, typing dots, ⚡ badge, stopwatch, end card with number) | tenant.json, captured thread |
| `my-video/src/compositions/CarouselCard/` | 1080×1350 stills for the receipts carousel (existing HTML→PNG pipeline is acceptable instead) | conversation store |
| `scripts/tenants/cha_dude/capture_demo.py` | drives the dry-run harness with a scenario, pulls the real thread + latencies from the box, writes `thread.json` | SSH to box, dry-run harness |
| `scripts/tenants/cha_dude/receipts.py` | aggregates the conversation store into the weekly receipts set + the after-10-pm share | SSH to box |
| `scripts/tenants/cha_dude/gate.py` | Cha Dude gate: banned words, number present, no price, no invented customer, persona says «چا دود», captured replies verbatim | all outputs |
| Weekly producer (cloud, not Mac) | scenario → capture → receipts → explainer brief → copy (Opus) → gate → render (CI) → post via upload-post profile `photonect-ai-studio` on the AI Studio page | everything above |
| Poster | reuse `post-to-uploadpost.py` with `--user photonect-ai-studio`; carousel path added (upload-post photo endpoint) | existing poster |

The existing news pipeline is untouched. Shared parts (VO generation, V11/Vox compositions, poster, QA gate) are reused as-is.

## 7. QA gates (hard, per post)

1. Existing triple QA (luminance, safe-zone, audio RMS).
2. Existing Opus editorial gate (neutrality/claims) — run after copy, never in parallel.
3. **Cha Dude gate** (§6) — any failure holds the post; nothing silent.
4. Ahmed reviews week 1's three posts before they go live. From week 2 the run is autonomous; the watchdog pattern from the news engine alerts on a dark week.

## 8. What Ahmed provides (once)

- The Instagram handle of the Photonect AI Studio page.
- That Instagram connected to upload-post as a second profile (`photonect-ai-studio`); a TikTok account when he wants TikTok.
- The Arabic spelling of the name if «چا دود» is wrong.
- Nothing else. No filming, no voice, no copy.

## 9. Out of scope (v1)

Stories · TikTok until an account exists · voice-note demos (the product acks voice notes, doesn't transcribe them) · paid reach · the sitcom device (needs a human on camera) · any price content.
