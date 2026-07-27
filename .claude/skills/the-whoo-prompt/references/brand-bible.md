# 더 후 (THE WHOO) — Brand Bible

Locked constants. Copy these blocks verbatim into prompts; do not paraphrase.

---

## 1. IDENTITY — MODEL K.

Spec sheet (`assets/model-k-character-sheet.png`):

| | |
| --- | --- |
| HEIGHT | 176cm |
| BUST / WAIST / HIPS | 78 / 60 / 88 cm |
| SHOES | 250mm |
| HAIR | Black |
| EYES | Dark Brown |

Available expressions on the sheet: **NEUTRAL / SOFT / SERENE**.

Standard block:

```
Using MODEL K. from the reference — keep her EXACT same face, identity, sleek
low bun, and jade cabochon stud earring flush against the earlobe.
```

Nano Banana variant (attachment-based):

```
Use the woman from image 1 — keep her EXACT same face, identity, sleek black low
bun, and jade cabochon stud earring flush against the earlobe.
```

Descriptive expansion, when the model needs more to hold on to:

> elegant Korean woman in her early 30s, 176cm, slender elegant proportions,
> black hair in a sleek low bun with center part, dark brown eyes, natural
> glowing skin with subtle freckles, jade oval stud earrings, calm dignified
> expression

**Never** let the identity drift into a generic Asian model. If the face comes
back wrong, do a second-pass face replacement rather than re-rolling the whole
image — recipe in `shot-library.md`.

---

## 2. OUTFIT — the ivory suit (campaign hero look)

```
Outfit: she wears the ivory shawl-collar longline suit — a soft shawl lapel with
a low hidden closure, the blazer falling past the hips over matching ivory
wide-leg trousers, the waistline never visible, one continuous ivory column,
beige minimal heels. Tucked inside the collar, a silk-chiffon shawl in pale
celadon green (#CAE1D9) shows as a subtle sliver along the inner neckline — a
quiet band of jade color framing the neck, barely-there, never billowing. On one
finger, a smooth dome-shaped jade ring in deep rich green nephrite. No other
jewelry.
```

Rules inside this block:
- **One continuous ivory column** — the waistline is never emphasized or visible.
- The celadon shawl is **barely-there** in suit shots. It only becomes the hero
  in the wind/shawl shot, where it is explicitly unwrapped and billowing.
- **No other jewelry** beyond the jade earring and the jade nephrite dome ring.

### Garment variations already approved

| Variation | Description |
| --- | --- |
| Ivory suit-dress | Sleeveless column dress, structured bodice cut like a tailored waistcoat, sharp minimal neckline, suiting crepe falling from the hip into a long fluid floor-length skirt. |
| Ivory dress-coat | Full-coverage floor-length coat, high neckline, long sleeves, softly structured shoulders, grand A-line skirt, fine ribbed turtleneck beneath — ivory felted wool, soft matte texture. |
| Celadon organza gown | Crisp silk organza, semi-translucent, luminous pearlescent sheen, sculptural airy volume, overlapping layers glowing where light passes through, fine narrow trim at the edges — in `#CAE1D9`. The one garment that carries the accent color. |

---

## 3. COLOR

**Jade celadon `#CAE1D9` is the only color in the frame.** It appears as the
shawl sliver, the earring, the nephrite ring, celadon ceramic props, or (in the
gown shots) the dress itself.

Everything else stays warm neutral:

- ivory / oatmeal / greige
- warm timber, deep brown wood shadows
- pale limestone, warm microcement
- skin warm and golden

Approved prop: **Korean celadon vessels** — soft rounded vases, matte powdery
jade-green glaze, varying heights, placed sparsely with generous space, casting
long soft shadows.

---

## 4. EDITORIAL GRADE — appended verbatim to every prompt

```
— EDITORIAL GRADE: one cohesive campaign, single film stock. Warm
ivory–oatmeal–greige palette, deep warm wood shadows, skin warm and golden, jade
celadon (#CAE1D9) the only accent color — echoed in the shawl sliver, the
earring, the ring. Soft warm directional daylight (~4300K), no flash, no HDR.
Medium-format film sensibility — soft contrast, lifted shadows, rolled-off
highlights, fine grain, muted creamy color. Whites lean ivory, never pure white.
Quiet, still, luminous, dignified.
```

Optional tail words by shot type: `sculptural` (stone/monumental shots),
`monumental` (grand interiors), `intimate` (close-ups).

---

## 5. SETTING vocabulary

Korean spaces, always disambiguated:

> Korean hanok architecture — minimal, modern, no dancheong; not Chinese, not
> Japanese.

| Setting | Key phrases |
| --- | --- |
| Hanok courtyard | wide pale stone paving, white plaster walls banded with dark timber, curved giwa tiled roofline, one slender tree, late-afternoon light raking across stone |
| Modern residential hanok interior | massive dark aged timber columns, exposed beam ceiling, plain warm ivory plaster walls, pale seamless stone floor, floor-to-ceiling glass onto a giwa courtyard |
| Grand dark hanok interior | vast polished microcement floor in deep warm grey, dark charcoal plaster walls with a light gradient, dark timber panelling, hanji-paper lattice door with fine black grid, low black soban table, wide glass opening throwing luminous rectangles of light |
| Monumental stone | massive raw limestone boulders, rough weathered texture, pale stone floor, muted grey-green wall, single raking light beam |
| Terrace over hills | open terrace, warm timber columns, pale stone floor, vast soft-focus rolling green-golden hills in atmospheric haze |

**Never** include retail fixtures — no shelves, display niches, counters, or
backlit product cases. Add the negative phrase when a mood reference contains
them:

> The space is calm and empty — no shelves, no displays, no retail fixtures, no
> furniture clutter — just wood, plaster, stone, glass and light.

---

## 6. POSE vocabulary

Approved, in ascending order of assertiveness:

1. **Regal stillness** — `one hand resting calmly over the other in front of her
   — the jade ring visible — a direct, level, self-possessed gaze into the
   camera. Regal stillness, no fashion gestures.`
2. **Effortless authority** (the campaign default) — `one hand tucked casually
   into her trouser pocket, the elbow softly bent; the other arm relaxed at her
   side, the jade ring visible on that hand. Weight settled evenly, chin level,
   a direct, level, self-possessed gaze into the camera. Effortless authority —
   relaxed but commanding, no fashion gestures.`
3. **Relaxed power stance** — `both hands in pockets, relaxed power stance.`

Other approved poses: mid-stride walking in profile; seated leaning forward with
one forearm across the knee; reclining seen from directly above; pure side
profile standing.

Always close the pose block with `no fashion gestures`.

---

## 7. COMPOSITION defaults

- Vertical **3:4**, full body, frontal and symmetrical unless the shot says
  otherwise.
- `Her face clearly resolved, sharp facial features.` — always include; the face
  degrades at full-body distance.
- One-point perspective where the architecture allows it, with MODEL K.
  anchoring the vanishing point.

---

## 8. Midjourney form (when explicitly requested)

Same blocks, plus flags:

```
--ar 3:4 --style raw --cref [character sheet URL] --cw 100 --sref [mood URL] --v 6.1
```

- `--cw 100` locks face **and** wardrobe to the sheet; `--cw 0` locks the face only.
- Lower `--sw` (default 100) if the style reference overwhelms the composition.
- Midjourney needs hosted image **URLs**; Nano Banana takes **attachments**. The
  user works in Nano Banana by default.
