import React from "react";
import { AbsoluteFill, Audio, interpolate, useCurrentFrame, Easing, staticFile } from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import {
  NewsReelProps,
  BREAKING_FRAMES,
  BEAT_FRAMES,
  BEAT3_FRAMES,
  SOURCES_FRAMES,
  computeNewsReelDurationInFrames,
  resolveVariant,
} from "./schema";
import { PHOTONECT } from "../PhotonectBrandReel/brand";
import { GrainOverlay, Vignette } from "../PhotonectBrandReel/GrainOverlay";
import { DotGrid, ScanBeam, TopStrip } from "../AINewsDaily/MotionLayers";
import { Breaking } from "./scenes/Breaking";
import { Beat } from "./scenes/Beat";
import { Sources } from "./scenes/Sources";

const BackgroundPulse: React.FC = () => {
  const frame = useCurrentFrame();
  const cx = interpolate(frame, [0, 900], [40, 60], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  const cy = interpolate(frame, [0, 900], [35, 65], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at ${cx}% ${cy}%, ${PHOTONECT.signal}14 0%, ${PHOTONECT.ink} 65%)`,
      }}
    />
  );
};

// V6 rev2 (2026-04-22 23:48) — rebuilt all 12 beds as lavfi-synthesized
// compositions with distinct musical character after Ahmed's 22 Apr rejection:
// "the music you did not change it, it is the same" / "one has a new music
// and it's bullshit". The previous V6 beds had size collisions, low loudness
// (bed_ambient_syn at −33.7 dB mean), and perceptually-identical drones.
// Rebuilt via automation/scripts/make-v6-beds.py:
//   - distinct key per bed (D-/G/Am/Em/C/Fm/Bm/Gm/Dm/Am-slow/Fm/Em)
//   - BPM range 50–130, distinct rhythmic feel per bed
//   - layered: sub-bass + triad + rhythmic pulse + melodic stinger + noise pad
//   - loudness-normalized to −16 LUFS / −1 dBFS peak (broadcast-ready)
//
// Bucket → default music bed. V6 uses 7 distinct defaults so adjacent buckets
// in the rotation never collide even before per-slug audioBed overrides.
const BUCKET_BED: Record<string, string> = {
  mena_geopolitics: "audio/bed_pressure.mp3",     // tense, urgent
  iraq_domestic:    "audio/bed_anchor.mp3",       // default news feel
  gulf_regional:    "audio/bed_echo.mp3",         // spacious, regional
  europe:           "audio/bed_ambient_syn.mp3",  // cinematic pad
  global_economy:   "audio/bed_voltage.mp3",      // electric, markets
  tech_ai:          "audio/bed_cycle.mp3",        // patrol sweep, AI
  wildcard:         "audio/bed_tide.mp3",         // backwards, atmospheric
};

// V7 (2026-04-25) — Four rotation moods, real broadcast-grade tracks.
// Each daily post gets one of the four moods; rotation is applied at the
// slate-assignment layer (props.json → audioBed) so adjacent posts never
// play the same track and the full stack of 12-13 keeps the viewer fresh.
// Legacy V6 lavfi beds retained for back-compat on older post folders.
const AVAILABLE_BEDS = new Set<string>([
  // V7 rotation moods
  "audio/mood_cinematic.mp3",              // slow piano + sub-bass + sparse strings
  "audio/mood_newsroom.mp3",               // rhythmic synth arps + light percussion
  "audio/mood_orchestral.mp3",             // low strings + soft brass + distant piano
  "audio/mood_mideast.mp3",                // oud + qanun + deep drum + cinematic pad
  // Legacy V6 rev2 beds (kept so old post folders keep rendering)
  "audio/news_bed.mp3",
  "audio/bed_anchor.mp3",
  "audio/bed_pressure.mp3",
  "audio/bed_weight.mp3",
  "audio/bed_velocity.mp3",
  "audio/bed_echo.mp3",
  "audio/bed_tide.mp3",
  "audio/bed_voltage.mp3",
  "audio/bed_fog.mp3",
  "audio/bed_steel.mp3",
  "audio/bed_pulse_syn.mp3",
  "audio/bed_cycle.mp3",
  "audio/bed_ambient_syn.mp3",
]);

// Bucket → default accent color. Gives each topic bucket a distinct visual
// signature without requiring props.json to specify an accent per beat.
// Resolution order per beat: explicit beat.accent → bucket default → PHOTONECT.signal
// This is additive: every existing props.json keeps rendering identically
// unless it opts in by setting `topicBucket`.
const BUCKET_ACCENTS: Record<string, string> = {
  mena_geopolitics: PHOTONECT.signal,  // brand red — hot conflict coverage
  iraq_domestic:    "#FFC217",         // brand yellow — domestic politics
  gulf_regional:    "#00E5A0",         // emerald — markets/gulf
  europe:           "#5B8FF9",         // cool blue — european files
  global_economy:   "#FFB020",         // amber — macro/oil/rates
  tech_ai:          "#C084FC",         // violet — tech / AI
  wildcard:         PHOTONECT.signal,  // fall through to brand
};

const pickAccent = (
  explicit: string | undefined,
  bucket: string | undefined,
): string | undefined => {
  if (explicit) return explicit;
  if (bucket && BUCKET_ACCENTS[bucket]) return BUCKET_ACCENTS[bucket];
  return undefined;  // let Beat fall back to PHOTONECT.signal
};

const pickAudioBed = (
  explicit: string | undefined,
  bucket: string | undefined,
): string => {
  // 1. Explicit prop wins (lets a slug override bucket default)
  if (explicit) {
    if (explicit.startsWith("http")) return explicit;
    if (AVAILABLE_BEDS.has(explicit)) return explicit;
  }
  // 2. Bucket default, if the file actually exists on disk
  if (bucket && BUCKET_BED[bucket] && AVAILABLE_BEDS.has(BUCKET_BED[bucket])) {
    return BUCKET_BED[bucket];
  }
  // 3. Safe fallback — anchor bed is loudnorm'd to -16 LUFS and always in AVAILABLE_BEDS
  return "audio/bed_anchor.mp3";
};

export const NewsReel: React.FC<NewsReelProps> = ({
  dateLabel,
  arabicDateLabel,
  handle,
  audioBed,
  variant,
  topicBucket,
  breaking,
  beats,
  sources,
  arabicTicker,
  voicePath,
  voiceDurationSeconds,
}) => {
  const BEAT_DURATIONS = [BEAT_FRAMES, BEAT_FRAMES, BEAT3_FRAMES];
  const frame = useCurrentFrame();
  const totalFrames = computeNewsReelDurationInFrames();
  const activeVariant = resolveVariant(variant, topicBucket);

  // V8 leap audio architecture (2026-05-10) — voice-over is now the spine.
  // Layers:
  //   - VO at full volume 1.0 (the dominant speech track, ar-IQ-BasselNeural)
  //   - Music BED ducked to 0.18 while VO speaks, swelling to 0.55 between
  //     VO start and end OR after VO ends
  //   - Silence drop at climax preserved (V7 pattern), runs INSIDE the VO
  //     duration so VO + silence at the same moment doubles the impact
  //   - Loop-hook cold-cut at end preserved
  //
  // Frame math: BREAKING(150) + BEAT(270) + BEAT(270) + BEAT3(240) + SOURCES(90) = 1020 frames.
  // ASSUMPTION: VO starts ~frame 24 (just after the cold-open hero settles)
  // and ends roughly when the VO mp3 ends. We compute VO_END from the
  // voiceDurationSeconds prop the generator wrote back; if missing, default
  // to total - 90 (so VO ends 3s before the reel ends).
  const VO_START = 24;
  const VO_END = voiceDurationSeconds
    ? Math.min(VO_START + Math.round(voiceDurationSeconds * 30), totalFrames - 30)
    : totalFrames - 90;

  // Strategic SILENCE drop near the climax — V7 pattern preserved.
  const SILENCE_START = BREAKING_FRAMES + BEAT_FRAMES * 2 + 60;          // ~26s
  const SILENCE_END   = SILENCE_START + 30;                              // 1.0s mute
  const REENTRY_END   = SILENCE_END + 20;                                // 0.67s reentry

  // Music volume curve — ducked under VO, swells when VO is silent (between
  // sections / after VO ends), full silence drop at climax.
  const audioVolume = interpolate(
    frame,
    [
      0,                            // music starts immediately
      18,                           // ramps to 0.45 by frame 18
      VO_START - 4,                 // start ducking just before VO enters
      VO_START + 4,                 // ducked under VO at 0.18
      SILENCE_START - 8,            // start ducking deeper toward silence
      SILENCE_START,                // full mute
      SILENCE_END,                  // hold mute
      REENTRY_END,                  // climb back to 0.18 (still ducked, VO still going)
      VO_END - 4,                   // begin swell as VO ends
      VO_END + 12,                  // music takes the floor at 0.55
      totalFrames - 45,             // hold through resolution
      totalFrames - 5,              // cold-cut for loop-hook
      totalFrames,
    ],
    [0, 0.45, 0.45, 0.18, 0.18, 0.02, 0.02, 0.18, 0.18, 0.55, 0.55, 0.55, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  // VO volume — comes in fast, holds at 1.0 (full output), exits cleanly with
  // the VO mp3's natural tail (edge-tts mp3s end with ~150ms of silence).
  const voiceVolume = voicePath
    ? interpolate(
        frame,
        [VO_START - 6, VO_START, VO_END, VO_END + 12],
        [0, 1, 1, 0],
        { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
      )
    : 0;

  const bedPath = pickAudioBed(audioBed, topicBucket);
  const audioSrc = bedPath.startsWith("http") ? bedPath : staticFile(bedPath);
  const voiceSrc = voicePath
    ? voicePath.startsWith("http") ? voicePath : staticFile(voicePath)
    : null;

  return (
    <AbsoluteFill style={{ background: PHOTONECT.ink }}>
      <Audio src={audioSrc} volume={audioVolume} />
      {voiceSrc && (
        <Audio
          src={voiceSrc}
          volume={voiceVolume}
          startFrom={0}
          // Music bed plays from frame 0; VO starts at VO_START. We use Sequence
          // semantics via the audio's natural offset by trimming with startFrom=0
          // and relying on volume=0 for the leading frames. Cleaner than wrapping
          // the Audio in a delayed Sequence because the Sequence would also
          // affect the surrounding TransitionSeries timeline.
        />
      )}

      <BackgroundPulse />
      <DotGrid />
      <ScanBeam />

      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={BREAKING_FRAMES}>
          <Breaking
            arabicKicker={breaking.arabicKicker}
            arabicHeadline={breaking.arabicHeadline}
            englishSubhead={breaking.englishSubhead}
            heroMedia={breaking.heroMedia}
            heroMediaType={breaking.heroMediaType}
          />
        </TransitionSeries.Sequence>

        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: 12 })}
        />

        {beats.map((beat, i) => (
          <React.Fragment key={i}>
            <TransitionSeries.Sequence durationInFrames={BEAT_DURATIONS[i]}>
              <Beat
                {...beat}
                accent={pickAccent(beat.accent, topicBucket)}
                index={i + 1}
                durationFrames={BEAT_DURATIONS[i]}
                variant={activeVariant}
              />
            </TransitionSeries.Sequence>
            <TransitionSeries.Transition
              presentation={fade()}
              timing={linearTiming({ durationInFrames: 12 })}
            />
          </React.Fragment>
        ))}

        <TransitionSeries.Sequence durationInFrames={SOURCES_FRAMES}>
          <Sources sources={sources} handle={handle} />
        </TransitionSeries.Sequence>
      </TransitionSeries>

      {/* Persistent UI chrome — sits inside platform-safe zone.
          BottomTicker removed: IG/TikTok occlude the bottom ~400px with
          caption/music chrome, so any ticker there is 100% invisible. */}
      <TopStrip dateLabel={dateLabel} arabicDateLabel={arabicDateLabel} showName="WORLD NEWS" />

      {/* Texture */}
      <Vignette strength={0.55} />
      <GrainOverlay opacity={0.08} seed={17} />
    </AbsoluteFill>
  );
};
