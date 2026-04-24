import { z } from "zod";
import { zColor } from "@remotion/zod-types";

export const BrandReelSchema = z.object({
  brandName: z.string(),
  brandSlug: z.string(),

  primary: zColor(),
  secondary: zColor(),
  accent: zColor(),
  background: zColor(),
  paper: zColor(),

  taglineLatin: z.string(),
  taglineArabic: z.string().optional(),

  benefits: z
    .array(
      z.object({
        headline: z.string(),
        body: z.string().optional(),
      }),
    )
    .min(3)
    .max(3),

  cta: z.object({
    text: z.string(),
    url: z.string(),
  }),

  durationInSeconds: z.number().min(10).max(30),
});

export type BrandReelProps = z.infer<typeof BrandReelSchema>;
