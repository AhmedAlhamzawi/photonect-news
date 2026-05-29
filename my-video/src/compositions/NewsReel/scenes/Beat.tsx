import React from "react";
import { AbsoluteFill } from "remotion";
import type { BeatProps, VariantName } from "../schema";
import { BeatA } from "./BeatA";
import { BeatB } from "./BeatB";
import { BeatC } from "./BeatC";
import { SourceChip } from "../components/SourceChip";
import { MultiShotBackdrop } from "../components/MultiShotBackdrop";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";

type Props = BeatProps & {
  index: number;
  durationFrames: number;
  variant: VariantName;
};

// V10 (2026-05-29) dispatcher — wraps the variant-specific Beat scene.
//
// Two fixes this rev (Ahmed feedback):
//   1. GHOST OVERLAY removed. Previously the variant scene painted its OWN
//      VideoBackdrop (props.broll) at 0.92 opacity ON TOP of the cycling
//      MultiShotBackdrop — two superimposed images = "a low-opacity overlay
//      picture covering the main picture, looks like an editing mistake."
//      Now: when MultiShotBackdrop owns the imagery (brolls[] present), we tell
//      the variant to skip its VideoBackdrop via `hideBackdrop`, and the scene
//      wrapper renders at full opacity. ONE image layer, clean.
//   2. GiantStatStamp DELETED. The index===3 climax used to slam the stat at
//      fontSize 320 dead-center over everything in the last ~10s ("a big
//      centric number and a statement comes on top of everything... very bad").
//      Removed entirely — beat 3 now shows its stat inline like beats 1 & 2.
//
// Persistent overlay on all beats: SourceChip (lower-left attribution).

export const Beat: React.FC<Props> = (props) => {
  // MultiShotBackdrop cycles the beat through its brolls[] with per-shot Ken
  // Burns. It owns ALL backdrop duties (image + overlay + vignette) whenever
  // a valid brolls[] array is present.
  // V10.1 (2026-05-29) — Ahmed rejected the multi-shot cycle: "the pics are
  // thrown in so the text doesn't relate to the picture shown, the pictures are
  // shown more than once, and it flips between the whole pics every beat."
  // Fix: ONE still image per beat — the beat's own `broll`, content-matched to
  // its text — rendered by the variant's VideoBackdrop. No cycle, no repeats,
  // no ghost. Breaking shows hero; beat 1/2/3 each show a distinct broll.
  const useMultiShot = false;
  const sceneProps = { ...props, hideBackdrop: useMultiShot };

  let scene: React.ReactNode;
  switch (props.variant) {
    case "B":
      scene = <BeatB {...sceneProps} />;
      break;
    case "C":
      scene = <BeatC {...sceneProps} />;
      break;
    case "A":
    default:
      scene = <BeatA {...sceneProps} />;
      break;
  }

  return (
    <AbsoluteFill>
      {useMultiShot && (
        <MultiShotBackdrop
          shots={props.brolls!}
          durationFrames={props.durationFrames}
          accent={props.accent ?? PHOTONECT.signal}
          intensity="beat"
        />
      )}
      {/* Variant chrome — full opacity. When useMultiShot, the variant skips its
          own VideoBackdrop (hideBackdrop), so this is pure typography/cards/stats
          over the single MultiShotBackdrop image layer. */}
      <AbsoluteFill>{scene}</AbsoluteFill>
      <SourceChip
        source={props.brollSource}
        durationFrames={props.durationFrames}
      />
    </AbsoluteFill>
  );
};
