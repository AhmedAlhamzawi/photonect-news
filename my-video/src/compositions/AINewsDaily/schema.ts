import { z } from "zod";
import { zColor } from "@remotion/zod-types";

const Stat = z.object({
  label: z.string(),
  value: z.string(), // string so we can include units + formatting
});

// Shared extras each story variant inherits
const StoryCommon = {
  // Image URLs — Wikimedia, Unsplash, or staticFile(). Each scene uses 1+.
  images: z.array(z.string()).min(1).max(4),
  // Arabic density — bilingual-first treatment
  arabicKicker: z.string(),
  arabicContext: z.string(),
};

// Variant-specific payloads for each story beat
const StoryBigNumber = z.object({
  variant: z.literal("bigNumber"),
  kicker: z.string(),
  prefix: z.string().default(""),
  value: z.number(),
  suffix: z.string().default(""),
  decimals: z.number().default(0),
  label: z.string(),
  context: z.string(), // "why this matters" sentence
  supportingStats: z.array(Stat).min(2).max(4),
  arabic: z.string(),
  ...StoryCommon,
});

const StoryRace = z.object({
  variant: z.literal("race"),
  kicker: z.string(),
  context: z.string(),
  arabic: z.string(),
  unit: z.string(),
  items: z
    .array(
      z.object({
        label: z.string(),
        value: z.number(),
        color: zColor(),
        growth: z.string().optional(), // "10x / yr"
        initials: z.string().optional(), // BrandMark initials (e.g. "A", "OAI")
      }),
    )
    .min(2)
    .max(4),
  ...StoryCommon,
});

const StoryReveal = z.object({
  variant: z.literal("reveal"),
  kicker: z.string(),
  title: z.string(),
  quote: z.string(),
  context: z.string(),
  supportingStats: z.array(Stat).min(2).max(4),
  arabic: z.string(),
  ...StoryCommon,
});

const StoryAlliance = z.object({
  variant: z.literal("alliance"),
  kicker: z.string(),
  nodes: z
    .array(
      z.object({
        label: z.string(),
        initials: z.string().optional(), // BrandMark initials
        brandColor: z.string().optional(), // brand color for the mark
      }),
    )
    .min(2)
    .max(4),
  verdict: z.string(),
  context: z.string(),
  arabic: z.string(),
  ...StoryCommon,
});

const StoryCompute = z.object({
  variant: z.literal("compute"),
  kicker: z.string(),
  value: z.number(),
  unit: z.string(),
  label: z.string(),
  partners: z.array(z.string()),
  context: z.string(),
  supportingStats: z.array(Stat).min(2).max(4),
  arabic: z.string(),
  ...StoryCommon,
});

const Story = z.discriminatedUnion("variant", [
  StoryBigNumber,
  StoryRace,
  StoryReveal,
  StoryAlliance,
  StoryCompute,
]);

export const AINewsDailySchema = z.object({
  dateLabel: z.string(),
  arabicDateLabel: z.string(),
  stories: z.array(Story).min(3).max(6),
  tickerHeadlines: z.array(z.string()).min(3).max(10), // EN ticker
  arabicTickerHeadlines: z.array(z.string()).min(3).max(10), // AR ticker
  handle: z.string().default("@photonect.news"),
});

export type AINewsDailyProps = z.infer<typeof AINewsDailySchema>;
export type StoryProps = z.infer<typeof Story>;
export type StatProps = z.infer<typeof Stat>;
