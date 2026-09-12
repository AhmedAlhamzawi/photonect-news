import { z } from "zod";

// ── CHAT REEL — chat-native product reel for a WhatsApp reply agent ─────────
// The conversation is the hero. Every bubble is real: captured from the live
// system with measured reply latencies. The engine only scripts the customer
// side; the agent side is verbatim. Tenant #2 of the engine (Cha Dude).

export const chatTurnSchema = z.object({
  who: z.enum(["customer", "agent", "divider"]),
  text: z.string(),
  time: z.string().default(""),          // on-bubble timestamp, e.g. "23:41" (the "impossible timestamp")
  startF: z.number(),                    // frame the bubble lands
  typingF: z.number().default(0),        // agent only: typing-indicator frames before landing (= real latency)
  latencyS: z.number().optional(),       // agent only: measured seconds shown on the ⚡ badge
  unanswered: z.boolean().default(false),// customer only: dead grey single tick, never answered
});

export const chatReelSchema = z.object({
  hook: z.string(),
  hookFrames: z.number().default(80),
  contactName: z.string().default("چا دود"),
  avatarLetter: z.string().default("چ"),
  statusLine: z.string().default("متصل الآن"),
  clockLabel: z.string().default("23:41"),     // phone status-bar time
  turns: z.array(chatTurnSchema),
  stopwatchOnFirst: z.boolean().default(true),  // big counter during the first agent typing window
  endcard: z.object({
    title: z.string(), sub: z.string().default(""), number: z.string(), cta: z.string().default(""),
    small: z.string().default(""),
  }),
  endcardStartF: z.number(),
  voClips: z.array(z.object({ src: z.string(), atF: z.number() })).default([]),
  bed: z.string().default(""),
  bedVolume: z.number().default(0.10),
  sfx: z.boolean().default(true),
  totalFrames: z.number(),
});

export type ChatReelProps = z.infer<typeof chatReelSchema>;
export type ChatTurn = z.infer<typeof chatTurnSchema>;
export const CHAT_FPS = 30;
export const computeChatDuration = (p: { totalFrames: number }) => Math.max(60, p.totalFrames);
