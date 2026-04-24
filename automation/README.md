# Photonect News — Tier 3 Automation

Autonomous every-2h posting to Instagram (@photonect.news) and TikTok. Reads `data/posts/<slug>/newsreel*.mp4` + `caption.txt`, uploads to Cloudinary CDN, then publishes via the official Graph / Content Posting APIs.

## Status legend
- `data/posts/<slug>/newsreel_v2.mp4` — preferred, used if present
- `data/posts/<slug>/newsreel.mp4` — fallback

## Install

```bash
cd automation
npm install
cp .env.example .env
# fill .env per SETUP guides below
```

## Quick commands

```bash
npm run queue:show                 # print what's in the queue + posted state
npm run test:ig 2026-04-17-hormuz-week2     # post a specific slug to IG only
npm run test:tiktok 2026-04-17-hormuz-week2 # same to TikTok only
npm run post:one                   # one full cycle (IG + TikTok, pick next post)
npm start                          # start scheduler (runs forever; default every 2h)
```

Set `DRY_RUN=true` in `.env` to go through every step except the final publish call.

## Topic diversity

`src/queue.js` tags each post to a bucket (mena_geopolitics / iraq_domestic / gulf_regional / europe / global_economy / tech_ai / wildcard) based on title+body keyword rules. `pickNext` prefers a bucket different from the last-posted one. No two consecutive posts from the same bucket unless the queue has no alternative.

## Setup guides

1. [setup-cloudinary.md](scripts/setup-cloudinary.md) — 5 min, free
2. [setup-ig.md](scripts/setup-ig.md) — 15 min, needs FB page linked to IG Business
3. [setup-tiktok.md](scripts/setup-tiktok.md) — days (app review)

Do them in order. After Cloudinary + IG you can already autopost to IG today. TikTok comes online once TikTok approves the app.

## State

`state/posted.json` tracks per-slug per-platform post history — so re-running the scheduler never double-posts. Delete a slug's entry to repost it.
