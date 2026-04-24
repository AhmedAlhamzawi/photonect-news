import fs from "node:fs/promises";
import path from "node:path";

const STATE_FILE = process.env.STATE_FILE || new URL("../state/posted.json", import.meta.url).pathname;

export async function loadState() {
  try {
    const raw = await fs.readFile(STATE_FILE, "utf8");
    return JSON.parse(raw);
  } catch (err) {
    if (err.code === "ENOENT") return { posts: {} };
    throw err;
  }
}

export async function saveState(state) {
  await fs.mkdir(path.dirname(STATE_FILE), { recursive: true });
  await fs.writeFile(STATE_FILE, JSON.stringify(state, null, 2));
}

export async function markPosted(slug, platform, meta) {
  const state = await loadState();
  state.posts[slug] ??= {};
  state.posts[slug][platform] = {
    postedAt: new Date().toISOString(),
    ...meta,
  };
  await saveState(state);
}

export async function isPosted(slug, platform) {
  const state = await loadState();
  return Boolean(state.posts[slug]?.[platform]);
}

export async function lastPostedBucket() {
  const state = await loadState();
  const entries = Object.entries(state.posts)
    .flatMap(([slug, platforms]) =>
      Object.values(platforms).map(p => ({ slug, bucket: p.bucket, at: p.postedAt }))
    )
    .filter(e => e.bucket)
    .sort((a, b) => b.at.localeCompare(a.at));
  return entries[0]?.bucket ?? null;
}
