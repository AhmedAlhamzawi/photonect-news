import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import {
  ChapterCycleProps,
  PhraseMarkerProps,
  HEKAYA_PALETTE,
} from "../schema";
import { ParallaxImage } from "../components/ParallaxImage";
import { Embers } from "../components/Embers";
import { PhraseReveal } from "../components/PhraseReveal";

interface Props {
  cycle: ChapterCycleProps;
  /** All phrase markers — this scene picks the ones inside its frame range. */
  phrases: PhraseMarkerProps[];
  /** Absolute frame offset from composition start (used to map phrases). */
  absoluteStart: number;
}

/**
 * The workhorse scene — cycles through 5-7 photos with ~2.5s cuts and layers
 * phrase reveals timed to the VO. Each photo gets its own KB direction so
 * cumulative motion is varied (not metronomic).
 */
export const Chapter: React.FC<Props> = ({ cycle, phrases, absoluteStart }) => {
  const frame = useCurrentFrame();

  // Compute which photo to show based on cycle progress
  const cuts = cycle.photos.length;
  const perPhotoFrames = Math.max(1, Math.floor(cycle.durationFrames / cuts));
  const currentPhotoIdx = Math.min(
    Math.floor(frame / perPhotoFrames),
    cuts - 1,
  );
  const photo = cycle.photos[currentPhotoIdx];

  // Direction rotates per photo so the cumulative effect is layered, not metronomic
  const directions: Array<"in" | "out" | "left" | "right"> = [
    "in",
    "out",
    "left",
    "right",
  ];
  const direction = directions[currentPhotoIdx % directions.length];

  // Filter phrases relevant to this scene's time window
  const sceneEnd = absoluteStart + cycle.durationFrames;
  const myPhrases = phrases.filter(
    (p) => p.startFrame >= absoluteStart && p.startFrame < sceneEnd,
  );

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      <ParallaxImage
        src={photo}
        durationFrames={perPhotoFrames}
        direction={direction}
        // Archival treatment on every third photo for cycle variety
        duotone={currentPhotoIdx % 3 === 2}
      />
      <Embers />

      {myPhrases.map((p, i) => {
        const localStart = p.startFrame - absoluteStart;
        const isFullBleed = p.layoutType === "full-bleed-quote";
        const isSingleWord = p.layoutType === "single-word";

        return (
          <div
            key={i}
            style={{
              position: "absolute",
              top: isFullBleed || isSingleWord ? "32%" : "auto",
              bottom: isFullBleed || isSingleWord ? "auto" : 320,
              left: 70,
              right: 70,
              textAlign: isFullBleed || isSingleWord ? "center" : "right",
              display: "flex",
              justifyContent: isFullBleed || isSingleWord ? "center" : "flex-end",
            }}
          >
            <PhraseReveal
              text={p.arabicText}
              startFrame={localStart}
              durationFrames={p.durationFrames}
              keyWord={p.keyWord}
              fontSize={isSingleWord ? 140 : isFullBleed ? 72 : 52}
              center={isFullBleed || isSingleWord}
            />
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
