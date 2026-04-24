import React from "react";
import type { BeatProps, VariantName } from "../schema";
import { BeatA } from "./BeatA";
import { BeatB } from "./BeatB";
import { BeatC } from "./BeatC";

type Props = BeatProps & {
  index: number;
  durationFrames: number;
  variant: VariantName;
};

// V6 dispatcher — restored full content density across all variants.
// Each variant renders the COMPLETE payload but with a distinct visual
// treatment, not different data slices:
//   A MONEY-SHOT  → BAR label + giant stat slam + heading + body + 3 pills (centered)
//   B KINETIC     → stat overlay on broll (top half) + STRIKE label + kinetic
//                   word-slam heading + body + 3 pills (bottom half)
//   C CINEMA      → bottom-anchored stack: hairline label → heading → body →
//                   3 pills → inline stat (progressive reveal)
// Safe-zone discipline via overflow:hidden + adaptive font sizing so every
// variant fits inside PLATFORM_SAFE regardless of content length.
export const Beat: React.FC<Props> = (props) => {
  switch (props.variant) {
    case "B": return <BeatB {...props} />;
    case "C": return <BeatC {...props} />;
    case "A":
    default:  return <BeatA {...props} />;
  }
};
