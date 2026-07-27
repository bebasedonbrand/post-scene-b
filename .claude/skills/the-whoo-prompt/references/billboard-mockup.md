# 더 후 (THE WHOO) — Times Square billboard mockup

Playing a THE WHOO clip on a Times Square corner billboard. AI generates the
plate; the clip is corner-pinned onto it with `scripts/billboard_wrap.py`. No
generative video model can reproduce specific brand footage inside a screen —
compositing is the only way the real TVC ends up on the billboard.

Delivered: `whoo-timessquare/whoo-timessquare-composite.mp4`

---

## 1. The plate

Generated rather than licensed, so there are no third-party trademarks to clear
and the blank panel comes out clean. 16:9, `nano_banana_pro`, 2k:

```
Times Square, New York, at blue hour just after sunset. Street-level wide shot,
fixed camera, slight low angle. A colossal blank billboard wraps the corner of a
building on the right half of the frame, facing the camera nearly straight on.
Its surface is pure flat white — completely blank, evenly lit, no imagery, no
text, no logos, no patterns — edged by a thin dark frame. Below it, brightly lit
storefronts with colorful signage. In the foreground, a stream of yellow taxis
and cars rushes across the frame in heavy motion blur, headlights and tail lights
smearing into long streaks on wet asphalt. Pedestrians walk along the sidewalk at
the left. Surrounding buildings are covered in glowing advertising screens showing
only abstract color fields and blurred light, no readable text anywhere. Deep blue
twilight sky. Long exposure, cinematic, photorealistic, sharp architecture with
motion-blurred traffic, high detail.
```

Two lines carry most of the weight. `sharp architecture with motion-blurred
traffic` is what produces the long-exposure look — without it the whole frame
goes soft or the cars freeze. `no readable text anywhere` keeps the surrounding
screens from filling with mangled pseudo-lettering, the fastest tell that an
image is generated.

Ask for `unobstructed — no scaffolding, poles, wires, trees or people crossing in
front of its screen` if a plate keeps coming back with something across the panel;
anything crossing the screen has to be rotoscoped back over the composite later.

## 2. Solving the geometry

A corner billboard is **two planes**, and each needs its own homography. Placing
the quads by eye is what makes a composite read as a sticker — the eye catches a
plane that isn't a true rectangle projection immediately.

Solve them instead:

1. Threshold the plate for bright, low-saturation pixels; keep the largest blob.
2. Walk the mask column by column recording the topmost and bottommost lit pixel.
3. The fold sits where both profiles reach their extremum — the nearest edge is
   the highest point of the top rim and the lowest point of the bottom rim. On
   this plate that is x≈1860, not the x≈1677 an eyeballed contour suggested.
4. Fit lines to each rim segment either side of the fold, plus the two outer
   edges, with a couple of rounds of outlier rejection.
5. Intersect the lines for exact corners.

Solved for `plate-timessquare-blank.png` (2752×1536):

| corner | px |
| --- | --- |
| far top-left | 1057.8, 611.4 |
| fold top | 1827.5, 198.4 |
| fold bottom | 1872.1, 854.3 |
| far bottom-left | 984.4, 959.8 |
| far top-right | 2127.9, 317.1 |
| far bottom-right | 2190.4, 890.2 |

Main face = `[top-left, fold-top, fold-bottom, bottom-left]` — the large one
facing camera. Side face = `[fold-top, top-right, bottom-right, fold-bottom]`.

**Clip to the plate's own white area.** Fitted lines extrapolate through
occlusions; on this plate the panel's bottom-left corner is cut by the roofline
and storefront, so content pinned to the ideal rectangle floats off the building
there. Pin to the ideal quad, then mask by the detected white region
(`plate-panel-mask.png`) so the perspective stays exact but nothing spills.

## 3. Making it read as an LED wall

- **Pixel lattice in clip space, warped by the same homography.** Drawn in output
  coordinates it stays axis-aligned and instantly contradicts the perspective.
- **Lift and gain.** A photographed white panel is dimmer than a real LED wall;
  ~1.25× gain with a small black lift. Dark footage like this TVC intro needs it
  or the site reads as switched off.
- **Spill.** Blur the panel mask, subtract the panel, tint by the frame's mean
  color, add. The screen's light landing on the surrounding facade sells the
  composite more than anything applied to the screen itself.
- **Slow push-in.** ~3.5% over the shot. A frozen plate behind a moving screen
  looks wrong even when everything else is right.

## 4. Which face plays

`--side dark` runs the clip on the main face and idles the side face near-black,
matching how a corner site sells one face at a time. This is the delivered
version.

`--side play` runs the clip on both faces. A third option — splitting one frame
across the fold so the image wraps continuously — was tried and dropped: the fold
lands mid-logo and breaks the wordmark.

## 5. Running it

```
python3 .claude/skills/the-whoo-prompt/scripts/billboard_wrap.py \
  --bg whoo-timessquare/plate-timessquare-blank.png \
  --video whoo-timessquare/whoo-tvc-intro.mov \
  --clip-mask whoo-timessquare/plate-panel-mask.png \
  --out composite.mp4
```

Needs `opencv-python-headless`, `numpy`, `imageio-ffmpeg`. The corner constants
are module-level and specific to this plate — re-solve them for a new one.

Tuning: `--gain` `--lift` (screen brightness), `--side dark|play`,
`--grid-pitch` `--grid-strength` (lattice), `--zoom` (push-in), `--glow` (spill),
`--scale` (output width, default 1920).

## 6. Assets

| File | Notes |
| --- | --- |
| `whoo-timessquare/plate-timessquare-blank.png` | Generated plate, 2752×1536 |
| `whoo-timessquare/plate-panel-mask.png` | Detected white panel, used for clipping |
| `whoo-timessquare/whoo-tvc-intro.mov` | TVC intro, 1280×720, 24fps, 4.45s |
| `whoo-timessquare/whoo-timessquare-composite.mp4` | Delivered, 1920×1072, 24fps |
| `whoo-timessquare/billboard-mockup.mp4` | Separate mockup, transcoded from VP9 webm |
