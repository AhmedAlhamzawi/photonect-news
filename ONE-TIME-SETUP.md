# Photonect NEWS — One-Time Cloud Setup

Do this once. After that, rendering a day = one tap on your phone.

There are three moving parts:

1. **GitHub repo** — holds the code + triggers the workflow
2. **Google Drive service account** — lets the runner write videos to your Drive
3. **GitHub secrets** — store the Drive credentials so the workflow can use them

---

## 1. Google Cloud — create a service account (5 min)

A service account is a robot Google user that can upload to Drive without you
having to log in. The `drive.file` scope we use means it can only touch files
it creates — it cannot read or modify anything else in your Drive.

**Steps (on a laptop, one-time):**

1. Open https://console.cloud.google.com/
2. Create a new project called `photonect-news` (or pick an existing one)
3. In the search bar, go to **APIs & Services → Library → Google Drive API → Enable**
4. Go to **IAM & Admin → Service Accounts → + Create service account**
   - Name: `photonect-news-uploader`
   - Role: leave empty (we don't need IAM roles — the Drive scope is enough)
5. Once created, open the service account → **Keys → Add key → Create new key → JSON**
6. A `.json` file downloads. **This is the credential. Keep it secret.**
7. Note the service account's email (looks like `photonect-news-uploader@<project>.iam.gserviceaccount.com`)

## 2. Google Drive — create a destination folder (1 min)

1. Open Drive on the web: https://drive.google.com/
2. Create a folder: **Photonect NEWS**
3. Right-click the folder → **Share** → paste the service account's email from step 1.7 → **Editor** access → Send
4. Open the folder. The URL looks like `https://drive.google.com/drive/folders/<LONG_ID>`. **Copy `<LONG_ID>`** — that's the `DRIVE_PARENT_FOLDER_ID`.

## 3. GitHub — create the private repo + push the code (1 command)

Ask me (Claude) to run this once you've done steps 1–2:

```
gh repo create photonect-news --private --source . --remote origin --push
```

(I need you to say go — I won't create a public repo or push without explicit approval.)

## 4. GitHub secrets — wire the credentials to the workflow (2 min)

On the repo page on github.com:

1. **Settings → Secrets and variables → Actions → New repository secret**
2. Add `DRIVE_PARENT_FOLDER_ID` → paste the long ID from step 2.4
3. Add `DRIVE_SERVICE_ACCOUNT_JSON` → paste the **entire contents** of the JSON file from step 1.6

Both secrets are encrypted. Only workflows in this repo can use them.

## 5. First run

1. Open the **GitHub** app on your phone
2. `photonect-news` → **Actions** → **Render day** → **Run workflow**
3. Leave the date blank (uses today) or type `YYYY-MM-DD`
4. ~30 minutes later, you get a push notification
5. Open **Drive** app → **Photonect NEWS → 2026-04-24 →** 12 folders, one per reel

Each folder contains `video.mp4` and `caption.txt`. Long-press to share/copy.

---

## Troubleshooting

**The workflow failed at "Write Drive service-account JSON to disk".**
→ Your `DRIVE_SERVICE_ACCOUNT_JSON` secret is malformed. Re-paste the file contents exactly.

**The workflow succeeded but Drive is empty.**
→ Your `DRIVE_PARENT_FOLDER_ID` is wrong, or the folder isn't shared with the service account email. Re-check step 2.3.

**"No slugs found for date YYYY-MM-DD"**
→ No post folders exist for that date under `data/posts/`. Run `build-slate.py` (or manually create the props) and commit them before triggering the workflow.

**The runner takes longer than 60 minutes.**
→ Increase `timeout-minutes:` in `.github/workflows/render-day.yml`. GitHub Actions free tier gives you 2000 minutes/month — one full slate is ~30 min so you have headroom for ~60+ runs/month.

---

## Staying under the GitHub Actions free tier

- 1 full slate render = ~30 min runner time
- Free tier = 2000 min/month
- Comfortable ceiling: ~30 full renders/month (one every ~1 day)
- Evolver runs (Part 2) ≈ 15 min each

If you ever bump the ceiling, you see an email from GitHub. Billing never surprises you.
