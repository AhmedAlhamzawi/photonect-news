import fs from "node:fs/promises";
import path from "node:path";
import { isPosted, lastPostedBucket } from "./state.js";

const POSTS_DIR = path.resolve(
  new URL("..", import.meta.url).pathname,
  process.env.POSTS_DIR || "../data/posts"
);

/**
 * Heuristic bucket assignment from story.json.
 * Priority order matches feedback_topic_diversity.md:
 *   1 MENA geopolitics, 2 global economy, 3 tech/AI, 4 Iraq domestic,
 *   5 Gulf regional, 6 Europe/west, 7 wildcard.
 */
const BUCKET_RULES = [
  { bucket: "mena_geopolitics", patterns: [/iran|hezbollah|lebanon|hormuz|israel|gaza|syria|yemen|houthi|netanyahu|aoun|truce|ceasefire|blockade/i] },
  { bucket: "iraq_domestic", patterns: [/iraq|baghdad|erbil|kurdistan|kdp|puk|kittleson|maliki/i] },
  { bucket: "gulf_regional", patterns: [/saudi|uae|qatar|bahrain|kuwait|oman|gcc|mbs|doha|riyadh/i] },
  { bucket: "europe", patterns: [/europe|eu|nato|germany|france|uk|london|brussels|jet fuel|flight|airline/i] },
  { bucket: "global_economy", patterns: [/brent|opec|oil price|imf|fed|inflation|market|stocks|dollar|yuan|recession/i] },
  { bucket: "tech_ai", patterns: [/openai|anthropic|google|microsoft|nvidia|llm|gpu|chip|ai regulation/i] },
];

function pickBucket(story) {
  const haystack = [story?.title, story?.subtitle, story?.englishSubhead, story?.beats?.map(b => b.arabicHeading).join(" ")]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
  for (const rule of BUCKET_RULES) {
    if (rule.patterns.some(p => p.test(haystack))) return rule.bucket;
  }
  return "wildcard";
}

async function loadPost(slug) {
  const dir = path.join(POSTS_DIR, slug);
  const [caption, storyRaw, propsRaw] = await Promise.all([
    fs.readFile(path.join(dir, "caption.txt"), "utf8").catch(() => ""),
    fs.readFile(path.join(dir, "story.json"), "utf8").catch(() => "null"),
    fs.readFile(path.join(dir, "props.json"), "utf8").catch(() => "null"),
  ]);
  const story = JSON.parse(storyRaw);
  const props = JSON.parse(propsRaw);
  const mergedForBucket = { ...(story || {}), ...(props?.breaking || {}), beats: props?.beats };

  // Prefer v2 if present.
  const files = await fs.readdir(dir);
  const video = files.find(f => f === "newsreel_v2.mp4") ?? files.find(f => f === "newsreel.mp4");
  if (!video) return null;

  return {
    slug,
    dir,
    videoPath: path.join(dir, video),
    videoVariant: video,
    caption: caption.trim(),
    bucket: pickBucket(mergedForBucket),
    props,
  };
}

export async function listAllPosts() {
  const entries = await fs.readdir(POSTS_DIR, { withFileTypes: true });
  const slugs = entries.filter(e => e.isDirectory()).map(e => e.name).sort();
  const loaded = await Promise.all(slugs.map(loadPost));
  return loaded.filter(Boolean);
}

/**
 * Pick the next post to publish, respecting:
 *   - not already posted to target platform,
 *   - bucket differs from the last posted bucket (diversity mandate),
 *   - newest slug first (slugs begin with ISO date).
 * If no post satisfies the bucket rule, relax it but log a warning.
 */
export async function pickNext(platform) {
  const posts = await listAllPosts();
  const unposted = [];
  for (const post of posts) {
    if (!(await isPosted(post.slug, platform))) unposted.push(post);
  }
  if (unposted.length === 0) return null;

  const lastBucket = await lastPostedBucket();
  const preferred = unposted.filter(p => p.bucket !== lastBucket);
  const pool = preferred.length > 0 ? preferred : unposted;

  // Newest first. Slugs are YYYY-MM-DD-*.
  pool.sort((a, b) => b.slug.localeCompare(a.slug));
  const pick = pool[0];
  if (preferred.length === 0) {
    console.warn(`[queue] no bucket-diverse post available; reusing bucket=${pick.bucket}`);
  }
  return pick;
}

export async function printQueue() {
  const posts = await listAllPosts();
  console.log(`Queue (${posts.length} posts):`);
  for (const p of posts) {
    const igPosted = await isPosted(p.slug, "instagram");
    const ttPosted = await isPosted(p.slug, "tiktok");
    console.log(
      `  ${p.slug.padEnd(40)} bucket=${p.bucket.padEnd(18)} ig=${igPosted ? "✓" : "·"} tt=${ttPosted ? "✓" : "·"} variant=${p.videoVariant}`
    );
  }
}
