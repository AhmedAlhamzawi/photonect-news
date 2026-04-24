# Setup: Instagram Graph API (Content Publishing)

**Why:** Lets us POST a Reel from Node with just an API call. The Chrome browser automation path is blocked by IG's security — the API path is the supported way.

**Time:** ~15–20 minutes if you already have a Facebook account. Add ~5 min if you need to create a FB Page.

**Pre-reqs:**
- `@photonect.news` is already an **Instagram Business or Creator** account. ✅ (we confirmed this — the "Switch" button in the IG sidebar showed the Photonect NEWS business profile).
- A **Facebook Page** connected to that IG account. If you don't have one, create a blank one called "Photonect News" — nobody needs to see it, it's just the OAuth anchor.

## Step 1 — Create a Facebook App

1. Go to **[developers.facebook.com/apps](https://developers.facebook.com/apps)** → "Create App".
2. Choose **Other** → **Business** as use case.
3. Name: `Photonect News Publisher`. Contact email: your email. Business Account: skip (optional).
4. Once created, the app dashboard opens. Copy:
   - **App ID** → `META_APP_ID` in `.env`
   - **App Secret** (App Settings → Basic → show) → `META_APP_SECRET` in `.env`

## Step 2 — Add Instagram product

1. In app dashboard left sidebar: **Add products** → **Instagram** → Set up.
2. Under **Instagram Graph API**, click **Add instagram_content_publish permission** (if present) or note that the permission will be requested below.

## Step 3 — Link your FB Page to the IG Business account

1. Go to **facebook.com/photonect.news-page** (or whatever your FB Page is called).
2. Page Settings → **Linked accounts** → Instagram → Connect → log in with @photonect.news credentials → approve.
3. Verify: in the app dashboard → Instagram → "Accounts" should now list photonect.news.

## Step 4 — Generate a user access token

1. Go to **[developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer)**.
2. In the top-right, select your app ("Photonect News Publisher").
3. Click **Generate Access Token**. Grant these scopes:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_show_list`
   - `pages_read_engagement`
   - `business_management` (if available)
4. Copy the token. This is a **short-lived** token (~1h).

## Step 5 — Exchange for a long-lived token

Run this curl (replace `SHORT_TOKEN`, `APP_ID`, `APP_SECRET`):

```bash
curl "https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=SHORT_TOKEN"
```

You get back `{ "access_token": "EAAB...", "expires_in": 5184000 }` — that's 60 days.

Paste as `META_LONG_LIVED_USER_TOKEN` in `.env`.

## Step 6 — Find your IG Business Account ID

```bash
curl "https://graph.facebook.com/v21.0/me/accounts?access_token=LONG_TOKEN"
# find the entry for your Page, copy its "id"

curl "https://graph.facebook.com/v21.0/PAGE_ID?fields=instagram_business_account&access_token=LONG_TOKEN"
# response has "instagram_business_account":{"id":"1784..."}  <-- THIS is what you want
```

Paste as `IG_BUSINESS_ACCOUNT_ID` in `.env`.

## Step 7 — Test

```bash
cd automation
npm run test:ig 2026-04-17-hormuz-week2
```

Expected output:
```
cloudinary: https://res.cloudinary.com/...
[ig] container=17841... slug=... — waiting for FINISHED
[ig] published mediaId=17841...
IG: { mediaId: '...', permalink: 'https://www.instagram.com/reel/...' }
done.
```

Check instagram.com/photonect.news — the reel should be live.

## Token rotation

The 60-day token will expire. A month from now, refresh it:

```bash
curl "https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=CURRENT_LONG_TOKEN"
```

Update `.env` with the new token. I'll add a reminder cron later.

## Troubleshooting

- **"(#10) Application does not have permission for this action"** → your app needs App Review for `instagram_content_publish`. In dev mode you can still post to accounts that are "testers" of the app (app dashboard → roles → add @photonect.news as tester).
- **Container stuck in IN_PROGRESS** → Cloudinary URL wrong format. IG requires h264+AAC mp4. Our render output already is.
- **"The user is not an Instagram Business Account"** → re-verify step 3 linking.
