import { interpolate, useCurrentFrame, useVideoConfig, Easing } from "remotion";

// Shared normalized progress: 0 → 1 → 0 across a scene.
// Derive all animated properties from this.
export const useSceneProgress = (
  enterSeconds: number = 0.6,
  exitSeconds: number = 0.4,
) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const enter = interpolate(frame, [0, enterSeconds * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const exit = interpolate(
    frame,
    [durationInFrames - exitSeconds * fps, durationInFrames],
    [0, 1],
    {
      easing: Easing.bezier(0.7, 0, 0.84, 0),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  return { progress: enter - exit, enter, exit, frame, fps, durationInFrames };
};
