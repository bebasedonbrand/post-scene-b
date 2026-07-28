---
name: the-whoo-prompt
description: Generate AI image prompts (Nano Banana / Midjourney) for the 더 후 (THE WHOO) editorial campaign featuring MODEL K. Use whenever the user asks for a new 더 후 shot, wants to change the pose, setting, garment, or color of an existing 더 후 image, references MODEL K, or says things like "더 후 프롬프트 만들어줘", "이 배경으로 바꿔줘", "포즈만 바꿔줘", "새 컷 뽑아줘" in the context of this ivory-and-jade Korean editorial campaign.
---

# 더 후 (THE WHOO) — Prompt System

Image prompts for **더 후 / THE WHOO**, the Korean royal-court heritage beauty
brand. Two visual worlds:

- **World A — MODEL K. editorial.** An ivory-and-jade campaign built around a
  fixed model identity and a fixed color/grade system. Every shot is a variation
  of one campaign — the identity, the palette, and the film grade never change;
  only the garment, pose, and setting move. This is the default when the user
  asks for a new 더 후 컷.
- **World B — product & spa imagery.** The brand's own royal-court world: deep
  plum and gold 환유 (Hwanyu) packaging, warm lacquer-and-brocade hanok spa
  interiors. **Products are never altered** — always edit in place, never
  regenerate. See shot 09 in `references/shot-library.md`.
- **World C — placement mockups.** Brand footage playing on real-world screens
  (Times Square billboards and the like). Generate the plate, then composite the
  clip with `scripts/billboard_wrap.py` — a generative video model cannot put
  specific brand footage inside a screen. See `references/billboard-mockup.md`.

Generation tool: **Nano Banana** (image attachments + natural-language prompt,
no `--flags`). Midjourney conventions are kept in `references/brand-bible.md`
for when the user asks for them instead.

Beyond image work, `references/estimate.md` holds the PT 제작 견적 — current
figures, the unit-rate logic, and the conditions written into the document.
Read it before touching `whoo-pt-estimate/`.

## Workflow

1. **Read `references/brand-bible.md`** — the locked identity, garment, color and
   grade blocks. These are copy-paste constants; do not paraphrase them.
2. **Check `references/shot-library.md`** — every shot already produced, with its
   full prompt. If the user's request is a variation of an existing shot, start
   from that prompt and change only the block they asked about.
3. **Assemble the prompt** in this fixed block order:
   `IDENTITY → OUTFIT → POSE → SETTING → COMPOSITION → EDITORIAL GRADE`
4. **Tell the user which images to attach, in order.** Nano Banana refers to
   attachments by number ("image 1", "image 2"), so the order is part of the
   prompt. Default order: MODEL K. face reference first, mood/pose/setting
   references after.
5. **Close with 2–4 팁** — how to push the effect harder, what to do if the face
   drifts, and which single line to swap for the most likely follow-up request.

## Rules that hold across every shot

- **Identity is never re-described loosely.** Always the exact IDENTITY block.
  MODEL K.'s face drifting is the most common failure — see the face-fix recipe
  in `references/shot-library.md`.
- **Jade celadon `#CAE1D9` is the only color in the frame.** Everything else is
  warm neutral (ivory, oatmeal, greige, warm timber). If a reference image has
  another accent color, convert it to celadon rather than adding it.
- **Whites lean ivory, never pure white.**
- **One cohesive campaign, single film stock.** The EDITORIAL GRADE block is
  appended verbatim to every prompt, including edit-in-place prompts.
- **Korean, not pan-Asian.** Always spell out "Korean hanok / giwa tiled roof,
  minimal, modern, no dancheong; not Chinese, not Japanese" in any traditional
  setting — the models default to Chinese or Japanese architecture otherwise.
- **No fashion gestures.** Poses are still, grounded, self-possessed. Dignity
  over movement, even mid-stride.
- **Never touch a product render.** In any shot containing THE WHOO packaging,
  the jars, bottles, lids, tray and wordmark stay pixel-identical. Spell this out
  as an explicit constraint in the prompt — models silently redesign labels
  otherwise.

## Editing an existing image vs. generating a new one

- **Editing** (user says "여기서 ~만 바꿔줘"): attach the finished image as image 1,
  open with `Edit image 1.`, state explicitly what stays *pixel-identical*, then
  the single change. Always re-append the EDITORIAL GRADE block so the edit
  doesn't drift off the campaign stock.
- **Generating** (user gives a new mood reference): attach MODEL K. first, the
  mood reference second, and write `Recreate the exact setting, pose, and
  composition of image 2` — then override only the blocks that differ.

## Assets in this skill

| File | Use |
| --- | --- |
| `assets/model-k-character-sheet.png` | Full MODEL K. sheet — profile, full body, expressions, details. Best identity anchor for full-body shots. |
| `assets/model-k-face-closeup.png` | Tight face close-up. Best identity anchor for face-replacement edits and close-ups. |
| `assets/shot-hanok-courtyard.png` | Delivered shot — hanok courtyard, ivory suit, hands clasped. |
| `assets/shot-hanok-interior.png` | Delivered shot — modern hanok interior, hand in pocket. |
| `assets/ref-modern-hanok-interior.jpeg` | Mood ref — dark timber columns, glass wall onto giwa courtyard. |
| `assets/ref-hand-in-pocket-pose.jpeg` | Pose ref — confident stance, one hand in pocket. |
