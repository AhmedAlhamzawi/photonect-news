import React from "react";
import { AbsoluteFill, Series, interpolate, useCurrentFrame, Easing } from "remotion";
import { AINewsDailyProps } from "./schema";
import { PHOTONECT } from "../PhotonectBrandReel/brand";
import { GrainOverlay, Vignette } from "../PhotonectBrandReel/GrainOverlay";
import { SceneTitle } from "./scenes/SceneTitle";
import { SceneBigNumber } from "./scenes/SceneBigNumber";
import { SceneRace } from "./scenes/SceneRace";
import { SceneCompute } from "./scenes/SceneCompute";
import { SceneReveal } from "./scenes/SceneReveal";
import { SceneAlliance } from "./scenes/SceneAlliance";
import { SceneOutro } from "./scenes/SceneOutro";
import { DotGrid, ScanBeam, BottomTicker, TopStrip } from "./MotionLayers";

// 30fps, 58s total = 1740 frames
// Title 150 | 5 stories × 300 = 1500 | Outro 90 = 1740
export const TITLE_FRAMES = 150;
export const STORY_FRAMES = 300;
export const OUTRO_FRAMES = 90;

export const computeAINewsDailyDurationInFrames = (storyCount: number) =>
  TITLE_FRAMES + storyCount * STORY_FRAMES + OUTRO_FRAMES;

const BackgroundGradient: React.FC = () => {
  const frame = useCurrentFrame();
  const cx = interpolate(frame, [0, 1740], [30, 70], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  const cy = interpolate(frame, [0, 1740], [40, 60], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at ${cx}% ${cy}%, ${PHOTONECT.signal}1E 0%, ${PHOTONECT.ink} 60%)`,
      }}
    />
  );
};

export const AINewsDaily: React.FC<AINewsDailyProps> = ({
  dateLabel,
  arabicDateLabel,
  stories,
  tickerHeadlines,
  arabicTickerHeadlines,
  handle,
}) => {
  const totalStories = stories.length;

  return (
    <AbsoluteFill style={{ background: PHOTONECT.ink }}>
      {/* Persistent background layers — always moving */}
      <BackgroundGradient />
      <DotGrid />
      <ScanBeam />

      {/* Scenes */}
      <Series>
        <Series.Sequence durationInFrames={TITLE_FRAMES} premountFor={30}>
          <SceneTitle />
        </Series.Sequence>

        {stories.map((story, i) => {
          const idx = i + 1;
          return (
            <Series.Sequence key={i} durationInFrames={STORY_FRAMES} premountFor={30}>
              {story.variant === "bigNumber" ? (
                <SceneBigNumber
                  kicker={story.kicker}
                  arabicKicker={story.arabicKicker}
                  prefix={story.prefix}
                  value={story.value}
                  suffix={story.suffix}
                  decimals={story.decimals}
                  label={story.label}
                  context={story.context}
                  arabicContext={story.arabicContext}
                  supportingStats={story.supportingStats}
                  arabic={story.arabic}
                  images={story.images}
                  storyIndex={idx}
                  total={totalStories}
                />
              ) : story.variant === "race" ? (
                <SceneRace
                  kicker={story.kicker}
                  arabicKicker={story.arabicKicker}
                  context={story.context}
                  arabicContext={story.arabicContext}
                  arabic={story.arabic}
                  unit={story.unit}
                  items={story.items}
                  images={story.images}
                  storyIndex={idx}
                  total={totalStories}
                />
              ) : story.variant === "compute" ? (
                <SceneCompute
                  kicker={story.kicker}
                  arabicKicker={story.arabicKicker}
                  value={story.value}
                  unit={story.unit}
                  label={story.label}
                  partners={story.partners}
                  context={story.context}
                  arabicContext={story.arabicContext}
                  supportingStats={story.supportingStats}
                  arabic={story.arabic}
                  images={story.images}
                  storyIndex={idx}
                  total={totalStories}
                />
              ) : story.variant === "reveal" ? (
                <SceneReveal
                  kicker={story.kicker}
                  arabicKicker={story.arabicKicker}
                  title={story.title}
                  quote={story.quote}
                  context={story.context}
                  arabicContext={story.arabicContext}
                  supportingStats={story.supportingStats}
                  arabic={story.arabic}
                  images={story.images}
                  storyIndex={idx}
                  total={totalStories}
                />
              ) : (
                <SceneAlliance
                  kicker={story.kicker}
                  arabicKicker={story.arabicKicker}
                  nodes={story.nodes}
                  verdict={story.verdict}
                  context={story.context}
                  arabicContext={story.arabicContext}
                  arabic={story.arabic}
                  images={story.images}
                  storyIndex={idx}
                  total={totalStories}
                />
              )}
            </Series.Sequence>
          );
        })}

        <Series.Sequence durationInFrames={OUTRO_FRAMES} premountFor={30}>
          <SceneOutro handle={handle} />
        </Series.Sequence>
      </Series>

      {/* Persistent UI chrome — top strip and bottom scrolling ticker */}
      <TopStrip dateLabel={dateLabel} arabicDateLabel={arabicDateLabel} />
      <BottomTicker headlines={tickerHeadlines} arabicHeadlines={arabicTickerHeadlines} />

      {/* Texture */}
      <Vignette strength={0.5} />
      <GrainOverlay opacity={0.07} seed={7} />
    </AbsoluteFill>
  );
};
