# Setup: TikTok Content Posting API

**Why:** Lets us POST a video to TikTok from Node via PULL_FROM_URL (Cloudinary). Unlike IG, TikTok requires app audit/review before you can post to production — expect **3–10 business days** of waiting before live publishing works. Until then, you can test in Sandbox mode with a bound TikTok account.

**Time:** ~30 min of setup + days of waiting on audit.

**Pre-reqs:**
- @photonect.news TikTok account exists and is logged in on your browser.
- Account is a **TikTok Business** (or at minimum a public, non-private account). Switch under Settings → Account → Switch to Business Account.

## Step 1 — Register as a TikTok developer

1. Go to **[developers.tiktok.com](https://developers.tiktok.com)** → "Log in" → sign in with the photonect.news TikTok account.
2. If asked, complete the developer profile (name, email, country). Accept the TikTok Developer TOS.

## Step 2 — Create an app

1. **Manage apps** → **Connect an app**.
2. App name: `Photonect News Publisher`. Description: "Automated cross-posting of short Arabic news clips to @photonect.news."
3. Category: **News & Information**.
4. Website: `https://photonect.net` (or any domain you control — TikTok will send test traffic here during audit).
5. Terms of service URL + Privacy policy URL: required. If you don't have one, use a generator like [termsfeed.com](https://www.termsfeed.com) and host the pages anywhere public (e.g. a GitHub Pages site). TikTok audits these pages.
6. Platform: **Web**. Redirect URI: `https://photonect.net/tiktok/callback` (can be a placeholder page for now — you'll only hit it once during OAuth).

Save. Copy:
- **Client Key** → `TIKTOK_CLIENT_KEY` in `.env`
- **Client Secret** → `TIKTOK_CLIENT_SECRET` in `.env`

## Step 3 — Add Content Posting API product

1. In the app dashboard: **Add products** → **Content Posting API** → Add.
2. Under scopes, request:
   - `user.info.basic` (required)
   - `video.publish` (this is the one that needs audit)
   - `video.upload` (for direct upload path — we don't need it, PULL_FROM_URL is enough, but request it anyway as a fallback)

## Step 4 — Bind the target account (Sandbox mode)

Before audit, TikTok only lets you post from the app to a **bound** TikTok account (yours as the developer, plus up to ~5 testers).

1. App dashboard → **Sandbox** → **Add sandbox tester**.
2. Add `photonect.news` TikTok username. It will send an in-app invite; accept it from the TikTok app.

## Step 5 — Get the user access token

TikTok requires OAuth 2.0. Simplest path:

1. Build the authorization URL:
   ```
   https://www.tiktok.com/v2/auth/authorize/?client_key=CLIENT_KEY&scope=user.info.basic,video.publish,video.upload&response_type=code&redirect_uri=https://photonect.net/tiktok/callback&state=photonect
   ```
2. Paste it into your browser. Log in as @photonect.news. Approve the requested scopes.
3. TikTok redirects to `https://photonect.net/tiktok/callback?code=AUTH_CODE_HERE&state=photonect`. Copy `AUTH_CODE_HERE` from the URL bar (even if the page 404s — the code is already in the URL).
4. Exchange the code for tokens:
   ```bash
   curl -X POST https://open.tiktokapis.com/v2/oauth/token/ \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "client_key=CLIENT_KEY&client_secret=CLIENT_SECRET&code=AUTH_CODE&grant_type=authorization_code&redirect_uri=https://photonect.net/tiktok/callback"
   ```
5. Response:
   ```json
   {
     "access_token": "act.xxx",
     "expires_in": 86400,
     "refresh_token": "rft.yyy",
     "refresh_expires_in": 31536000,
     "open_id": "abc123...",
     "scope": "user.info.basic,video.publish,video.upload"
   }
   ```

Paste into `.env`:
- `TIKTOK_USER_ACCESS_TOKEN=act.xxx`
- `TIKTOK_USER_REFRESH_TOKEN=rft.yyy`
- `TIKTOK_USER_OPEN_ID=abc123...`

## Step 6 — Test in sandbox

```bash
cd automation
npm run test:tiktok 2026-04-17-hormuz-week2
```

Expected in sandbox mode:
- Post succeeds BUT the video is marked as **private** regardless of the `privacy_level` you pass. This is TikTok's sandbox safety.
- Check the TikTok app → your profile → Drafts/Private. The video should be there.

If that works, the plumbing is correct — you just can't go public until audit.

## Step 7 — Submit for audit (to go live)

1. App dashboard → **Audit** → **Submit**.
2. TikTok requires:
   - A **demo video** (screencap of the automation running or similar) showing how you use `video.publish`.
   - A written description of use case, frequency, and content type.
   - Confirmation your ToS + Privacy URLs are live.
3. Submit. Wait 3–10 business days.
4. When approved, you can set `privacy_level=PUBLIC_TO_EVERYONE` and the video will go live to @photonect.news.

## Token rotation

`access_token` expires in 24 hours. The scheduler uses `refreshToken()` in `src/posters/tiktok.js` — but for now, refresh manually to confirm:

```bash
curl -X POST https://open.tiktokapis.com/v2/oauth/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_key=CLIENT_KEY&client_secret=CLIENT_SECRET&grant_type=refresh_token&refresh_token=CURRENT_REFRESH_TOKEN"
```

Response contains a new `access_token` + new `refresh_token` — update `.env`. The refresh_token rotates every use, so keep the latest one.

I'll wire auto-refresh into `state.js` once we're out of sandbox.

## Troubleshooting

- **`access_token_invalid`** → token expired. Run the refresh curl above.
- **`unaudited_client_can_only_post_to_private_accounts`** → expected in sandbox. Won't go away until audit passes.
- **`video_pull_failed`** → Cloudinary URL returned non-200 or wrong content-type. Confirm the URL opens in a browser and returns `video/mp4`.
- **`spam_risk_user_banned_from_posting`** → rare; TikTok's anti-spam flagged the account. Wait 24h, try again, and slow down posting cadence if it recurs.
- **Redirect URI mismatch** → exact match required. `https://photonect.net/tiktok/callback` in both the app config AND the authorize URL. No trailing slash differences.
