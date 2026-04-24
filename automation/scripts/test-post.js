#!/usr/bin/env node
/**
 * Manual test harness — post a specific slug to a specific platform.
 *
 *   node scripts/test-post.js instagram 2026-04-17-hormuz-week2
 *   node scripts/test-post.js tiktok    2026-04-17-hormuz-week2
 *   node scripts/test-post.js both      2026-04-17-hormuz-week2
 */
import "dotenv/config";
import { listAllPosts } from "../src/queue.js";
import { uploadVideo } from "../src/uploader.js";
import { postReel } from "../src/posters/instagram.js";
import { postVideo as postTikTok } from "../src/posters/tiktok.js";
import { markPosted } from "../src/state.js";

const [, , platform, slug] = process.argv;
if (!platform || !slug) {
  console.error("usage: test-post.js <instagram|tiktok|both> <slug>");
  process.exit(2);
}

const posts = await listAllPosts();
const post = posts.find(p => p.slug === slug);
if (!post) {
  console.error(`no post found for slug=${slug}. Available:`);
  posts.forEach(p => console.error(`  ${p.slug}`));
  process.exit(2);
}

console.log(`uploading ${post.videoVariant} to Cloudinary...`);
const videoUrl = await uploadVideo({ slug: post.slug, localPath: post.videoPath });
console.log(`cloudinary: ${videoUrl}`);

if (platform === "instagram" || platform === "both") {
  const r = await postReel({ videoUrl, caption: post.caption, slug: post.slug });
  await markPosted(post.slug, "instagram", { ...r, bucket: post.bucket, videoUrl });
  console.log("IG:", r);
}
if (platform === "tiktok" || platform === "both") {
  const r = await postTikTok({ videoUrl, caption: post.caption, slug: post.slug });
  await markPosted(post.slug, "tiktok", { ...r, bucket: post.bucket, videoUrl });
  console.log("TikTok:", r);
}

console.log("done.");
