# 더 후 (THE WHOO) — Shot Library

Every prompt produced so far, in order. To make a variation, copy the closest
shot and change only the block the user asked about. Block order is always
`IDENTITY → OUTFIT → POSE → SETTING → COMPOSITION → EDITORIAL GRADE`.

Two visual worlds live in this campaign:

- **World A — MODEL K. editorial** (shots 01–08): ivory suiting, jade celadon
  accent, Korean architecture, medium-format film grade. All prompts below.
- **World B — THE WHOO product & spa** (shot 09): the brand's own royal-court
  world — deep plum and gold 환유 packaging, warm lacquer-and-brocade hanok spa
  interiors. Product renders must never be altered; see shot 09.

---

## Face drift — the standard fix

MODEL K.'s face is the most common failure, especially at full-body distance.
Do **not** re-roll the whole image. Second-pass replace instead:

**Attach:** 1) the generated image, 2) `assets/model-k-face-closeup.png`

```
Edit image 1. Replace ONLY the woman's face with the exact face of the woman in
image 2 — her precise facial features: the almond eyes, straight brows, defined
cheekbones, nose shape, lip shape, and natural skin texture with subtle
freckles. Keep her identity 100% faithful to image 2.

Do not change anything else in image 1: keep the exact same pose, body
proportions, hand in pocket, outfit, jade ring, hair in the sleek low bun, jade
earring, lighting, shadows, background, and composition — pixel-identical except
the face. Match the face naturally to the existing head angle, scale, and the
warm directional lighting of the scene. Seamless, photorealistic blend.
```

If it still drifts, swap the reference to the full character sheet
(`assets/model-k-character-sheet.png`) — the multiple angles sometimes match
better than a single close-up. Add
`render the face sharp and clearly resolved despite the distance` for distant
framings.

---

## Shot 01 — Hanok courtyard, regal stillness

The origin shot. Ivory suit, hands clasped, palace courtyard, symmetrical.
Delivered: `assets/shot-hanok-courtyard.png`

```
Using MODEL K. from the reference — keep her EXACT same face, identity, sleek low bun, and jade cabochon stud earring flush against the earlobe.
Outfit: she wears the ivory shawl-collar longline suit — a soft shawl lapel with a low hidden closure, the blazer falling past the hips over matching ivory wide-leg trousers, the waistline never visible, one continuous ivory column, beige minimal heels. Tucked inside the collar, a silk-chiffon shawl in pale celadon green (#CAE1D9) shows as a subtle sliver along the inner neckline — a quiet band of jade color framing the neck, barely-there, never billowing. On one finger, a smooth dome-shaped jade ring in deep rich green nephrite. No other jewelry.
Pose: standing at the exact center of the frame, spine tall, shoulders level, chin level, one hand resting calmly over the other in front of her — the jade ring visible — a direct, level, self-possessed gaze into the camera. Regal stillness, no fashion gestures.
Setting: a modern Korean palace courtyard — wide pale stone paving, clean white plaster walls banded with dark timber, a floating curved giwa tiled roofline behind her with elegant eaves, one slender tree casting soft shadow. Late-afternoon sunlight raking across the stone, her long shadow trailing. Korean palace architecture — minimal, modern, no dancheong; not Chinese, not Japanese.
Composition: full-body vertical 3:4 (or 16:9 horizontal), frontal, symmetrical, monumental — one-point perspective toward the roofline, she anchors the vanishing point. Face clearly resolved, sharp facial features.
— EDITORIAL GRADE: one cohesive campaign, single film stock. Warm ivory–oatmeal–greige palette, deep warm wood shadows, skin warm and golden, jade celadon (#CAE1D9) the only accent color — echoed in the shawl sliver, the earring, the ring. Soft warm directional daylight (~4300K), no flash, no HDR. Medium-format film sensibility — soft contrast, lifted shadows, rolled-off highlights, fine grain, muted creamy color. Whites lean ivory, never pure white. Quiet, still, luminous, dignified.
```

---

## Shot 02 — Modern hanok interior, hand in pocket

Shot 01 with the pose upgraded to the campaign default and the setting moved
indoors. Retail fixtures explicitly removed — the first pass rendered the left
wall as a boutique display. Delivered: `assets/shot-hanok-interior.png`

Changed blocks only:

```
Pose: standing tall at the center of the frame, spine long, shoulders open and level — one hand tucked casually into her trouser pocket, the elbow softly bent; the other arm relaxed at her side, the jade ring visible on that hand. Weight settled evenly, chin level, a direct, level, self-possessed gaze into the camera. Effortless authority — relaxed but commanding, no fashion gestures.
Setting: inside a modern residential hanok — massive dark aged timber columns and an exposed beam ceiling in deep brown wood, plain warm plaster walls in soft ivory, a pale seamless stone floor, and a floor-to-ceiling glass wall behind her opening onto a quiet courtyard with a curved giwa tiled roofline and soft greenery beyond. The space is calm and empty — no shelves, no displays, no retail fixtures, no furniture clutter — just wood, plaster, stone, glass and light. Korean hanok architecture — minimal, modern, no dancheong; not Chinese, not Japanese.
Composition: full-body vertical 3:4 (or 16:9 horizontal), frontal, symmetrical, monumental — one-point perspective down the row of timber columns, she anchors the vanishing point, the bright courtyard framing her silhouette. Face clearly resolved, sharp facial features.
```

Spot-fix for a retail-looking wall in an already-generated image:

```
Keep everything else exactly the same. Only change the left wall: remove the backlit display niches and shelving — replace them with a plain warm ivory plaster wall with dark timber framing, matching the modern hanok architecture. No retail fixtures anywhere.
```

---

## Shot 03 — Terrace over hills, shawl in the wind

The one shot where the celadon shawl is the hero instead of a sliver.

```
Create a full-body editorial fashion photograph. Use the woman from image 1 — keep her EXACT same face, identity, sleek black low bun, and jade cabochon stud earring. Her face is visible in a clean elegant profile as she walks.

Outfit: the ivory shawl-collar longline suit — soft shawl lapel, the blazer falling past the hips over matching ivory wide-leg trousers, one continuous ivory column, beige minimal flats. In this shot, her pale celadon green (#CAE1D9) silk-chiffon shawl is unwrapped and alive: draped over her shoulders and caught by the wind, streaming and billowing behind her in one long translucent wave of jade color — the fabric luminous, weightless, backlit. On one finger, the smooth dome-shaped jade ring in deep green nephrite. No other jewelry.

Pose: captured mid-stride, walking with quiet purpose across the frame in profile — spine tall, chin level, shoulders open, one leg extended in a natural step, arms relaxed, the wide trousers swaying with the motion. Unhurried, self-possessed, dignified — no fashion gestures.

Setting: match the mood and setting of image 2 — an open modern terrace with warm timber columns and pale stone floor, looking out over a vast soft-focus landscape of rolling green-golden hills fading into atmospheric haze. Warm late-afternoon sunlight rakes across the scene, backlighting the flying shawl and casting her long shadow on the stone.

Composition: full-body vertical 3:4, she is placed off-center walking into open space, the billowing shawl filling the frame behind her, the hazy hills as a soft painterly backdrop. Her face clearly resolved and sharp in profile.

[EDITORIAL GRADE]
```

Dials: three-quarter back angle → `walking away from the camera at a
three-quarter back angle, her face turned just enough to show a clean profile`.
More drama → `the shawl billowing dramatically, twice her body width, frozen
mid-motion`.

---

## Shot 04 — Close-up profile, face buried in the shawl

Adapted from a chunky-knit reference. Silk chiffon can't hold that volume, so it
is described as many layers instead.

```
Create a close-up editorial beauty portrait. Use the woman from image 1 — keep her EXACT same face, identity, and sleek black low bun with soft loose strands. She wears her jade cabochon stud earring flush against the earlobe.

Recreate the exact composition, pose and mood of image 2: an intimate side profile, head turned away so we see the elegant line of her brow, eye, and the curve of her ear — the lower half of her face gently buried in fabric wrapped high around her neck, up to just below her eyes.

Replace the green knit from image 2 with her pale celadon green (#CAE1D9) silk-chiffon shawl — wrapped generously in soft layered folds around her neck and chin, the translucent chiffon gaining volume through its many airy layers, catching the light with a delicate luminous sheen. The jade celadon fabric is the only accent color.

Lighting and grade: soft diffused window light, warm ivory background falling out of focus. [EDITORIAL GRADE] Quiet, intimate, luminous, dignified.
```

Dials: cosier texture → `a plush celadon green mohair-knit scarf (#CAE1D9 tone)`.
Less coverage → `around her chin and mouth` instead of `up to just below her eyes`.

---

## Shot 05 — Seated in a dark corridor, ivory suit-dress

```
Create a full-body editorial fashion photograph. Use the woman from image 1 — keep her EXACT same face, identity, sleek black low bun, and jade cabochon stud earring flush against the earlobe.

Recreate the exact setting, pose, and composition of image 2: she sits in profile on a low mid-century wooden bench with an ivory linen cushion, placed in a dim corridor of warm dark timber panels and aged brick-toned tile walls, a shadowed doorway behind her, warm terracotta tile floor below. She leans forward gracefully, one forearm resting across her knee, her hand relaxed and draping — the jade ring visible — her body in profile while her face turns toward the camera with a direct, calm, self-possessed gaze. The long skirt of her dress pools softly toward the floor.

Outfit: replace the reference's dress with an ivory tailored suit-dress — a sleeveless column dress with a clean structured bodice cut like a tailored waistcoat, sharp minimal neckline, the fabric a refined suiting crepe that falls from the hip into a long fluid floor-length skirt. One continuous ivory column, the waistline never emphasized. Beige minimal heels barely visible. On one finger, the smooth dome-shaped jade ring in deep green nephrite. No other jewelry.

Lighting: match image 2 — soft ambient daylight falling from the left, her figure luminous against the deep brown shadows of the corridor, gentle falloff, quiet chiaroscuro.

Composition: full-body vertical 3:4, she sits just right of center, the dark doorway framing her silhouette, negative space above. Her face clearly resolved, sharp facial features.

[EDITORIAL GRADE]
```

Dials: hair down → `her black hair worn down, straight and loose past her
shoulders`. Dark-scene face rescue → `render her face bright and clearly lit
against the dark corridor`.

---

## Shot 06 — Monumental limestone, ivory dress-coat

```
Create a full-body editorial fashion photograph. Use the woman from image 1 — keep her EXACT same face, identity, sleek black low bun, and jade cabochon stud earring flush against the earlobe.

Recreate the exact setting, pose, and composition of image 2: she stands in pure side profile between monumental raw limestone boulders — massive pale sculptural rocks with rough weathered texture filling the left and right of the frame, a smooth pale stone floor, a muted grey-green wall softly falling into shadow behind. A single beam of warm directional light rakes across the scene, catching the rock texture and illuminating her figure against the shadowed background.

Her pose exactly as in image 2: standing tall in profile facing left, spine long, chin level, gaze calm and level toward the distance, arms hanging relaxed at her sides, mid-step stillness — sculptural, monumental, serene.

Outfit: keep the exact garment from image 2 — the full-coverage floor-length dress-coat with its high neckline, long sleeves, softly structured shoulders, and grand A-line skirt flaring to the floor, a fine ribbed turtleneck rising at the neck beneath it — but render it entirely in warm ivory white: the dress-coat in ivory felted wool with soft matte texture, the turtleneck in matching ivory. Everything she wears is one continuous ivory column. On one finger, the smooth dome-shaped jade ring in deep green nephrite. No other jewelry.

Composition: full-body vertical 3:4, she stands small at center between the huge boulders, monumental negative space, one-point stillness. Her face clearly resolved and sharp in profile.

[EDITORIAL GRADE] Quiet, still, luminous, dignified, sculptural.
```

Dials: to keep her tonally fused with the stone →
`pale oatmeal-ivory, harmonizing with the limestone`.

---

## Shot 07 — Top-down, celadon organza gown, celadon vessels

The strongest shot in the series. Organza texture + Korean celadon props.

```
Create an editorial fashion photograph shot directly from above — a top-down bird's-eye view. Use the woman from image 1 — keep her EXACT same face, identity, sleek black low bun, and jade cabochon stud earring. Seen from above, her face turned upward toward the camera, serene and self-possessed, framed by the fabric around her.

Recreate the composition and mood of image 2: she reclines on a long curved sofa, and her voluminous dress spreads around her in a dramatic sculptural fan — deep radiating folds pooling across the sofa and spilling over its edge, her body almost enveloped, only her face, one shoulder and one hand emerging from the drapery. The jade nephrite dome ring visible on her finger.

Fabric: the dress is made of the material in image 3 — crisp silk organza, semi-translucent with a luminous pearlescent sheen, holding sculptural airy volume, its layers overlapping so the folds glow where light passes through, edges finished with a fine narrow trim. Render this organza texture faithfully, but in pale celadon jade green (#CAE1D9).

Props: standing on the pale stone floor around the sofa, two or three celadon ceramic vessels like those in image 4 — soft rounded Korean celadon vases with a matte powdery jade-green glaze, varying heights, placed sparsely with generous space between them, casting long soft shadows.

Color: jade celadon (#CAE1D9) is the ONLY color in the frame — the organza dress, the celadon vessels, the earring, the ring. Everything else stays warm neutral: the curved sofa in ivory bouclé, the floor warm greige limestone, soft ivory plaster wall.

Lighting: warm directional late-afternoon light raking across the scene from one side, long soft shadows, the translucent organza glowing where the light grazes it.

Composition: perfectly top-down, slightly off-center — the curved line of the sofa sweeping through the frame, the fanned organza dress as the focal bloom, the celadon vessels punctuating the negative space of pale floor. Her face clearly resolved and sharp.

[EDITORIAL GRADE] Quiet, still, luminous, dignified, sculptural.
```

Dials: props read poorly from directly overhead → `shot from a high angle,
tilted slightly off vertical`. More volume →
`the organza layers billowing upward in frozen volume, air trapped between the
sheer layers`.

---

## Shot 08 — Shot 07 relocated into a grand dark hanok

An edit-in-place on the shot 07 result. The campaign's one dark cut.

```
Edit image 1. Keep the woman EXACTLY as she is — same face, identity, sleek low bun, pose reclining on the curved sofa, the celadon jade silk organza dress with all its sculptural fanning folds, the jade ring, the two celadon vessels. Keep the top-down bird's-eye camera angle and the warm raking light. Do not change her, her dress, or the sofa.

Change ONLY the surrounding architecture: place the scene inside a grand modern Korean interior in the mood of image 2 — a vast, austere, monumental room with wide polished microcement floors in deep warm grey, walls of dark charcoal plaster with a soft gradient of light washing down them, and tall dark timber panelling with a deep matte sheen. A traditional Korean hanji-paper lattice door with a fine black grid sits in the far wall. A single low black soban table rests on the floor at a distance. On one side, a wide floor-to-ceiling glass opening lets warm daylight flood in across the floor, throwing long luminous rectangles of light and deep soft shadows over the vast empty space.

The room is monumental and almost empty — enormous negative space, quiet and reverent, the ivory sofa and the woman forming a single glowing island of warm light at the center of the dark expanse.

Keep the celadon jade (#CAE1D9) as the only color: the organza dress and the celadon vessels glowing against the dark stone and charcoal walls.

[EDITORIAL GRADE] Quiet, still, luminous, dignified, monumental.
```

Dials: softer → charcoal walls become `warm greige plaster with a deep smoky
gradient`, floor becomes `warm sand-grey microcement`. Fully dark → sofa becomes
`deep charcoal bouclé` so the gown is the only light source. Grander →
`the ceiling soaring high above, the camera looking down from a great height`.

---

## Shot 09 — THE WHOO spa treatment scene (World B)

Different world from shots 01–08: the brand's own royal-court spa imagery, not
the MODEL K. editorial. Warm lacquer wood, brocade cushions, a therapist
applying cream to a reclining client, and the 환유 (Hwanyu) product line staged
on a gold tray.

**Hard constraint: the products may never be altered.** The plum-and-gold
Hwanyu jars and bottles, their gold crown-shaped lids, the gold tray, and the
THE WHOO wordmark on the tray must stay pixel-identical to the source. Treat
every prompt here as an edit-in-place, never a regeneration.

Target delivery size: **780 × 540 px (13:9, ≈1.444:1)**, high quality.

Upscale / cleanup prompt — attach the source image as image 1:

```
Edit image 1. Increase the resolution and clarity of this photograph — render it
sharp, clean and high-definition, with crisp detail in the fabric textures, the
brocade cushions, the wood grain, and the skin.

CRITICAL: the cosmetic products must remain completely unchanged. The deep plum
and gold jars and bottles on the gold tray, their gold crown-shaped lids, the
gold tray itself, and the "THE WHOO" wordmark on it must stay pixel-identical in
shape, proportion, color, label text and placement. Do not redesign, restyle,
relabel, add, remove, or rearrange any product. Do not alter the gold cream jar
held in the therapist's hand.

Keep everything else identical too: both women's faces and poses, the therapist's
plum linen uniform, the towels, the cushions, the lattice screen, the candle
holders, the orchid, the framing and the warm lighting. This is a resolution and
sharpness pass only — no creative changes.

Warm golden lighting, rich lacquer-brown and plum palette, gold accents, calm
luxurious spa atmosphere, photorealistic, high detail.
```

Composition note for the 780 × 540 crop: the source is wider than 13:9, so trim
from the left edge (the dark louvre panel) rather than the right — the product
tray sits right of center and must not be cropped or crowded.
