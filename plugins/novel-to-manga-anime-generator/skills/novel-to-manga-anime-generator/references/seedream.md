# Seedream prompts (REFs, comic panels, anime keyframes)

Based on public Seedream 5.0 material (2026). Default model: **5.0 Lite** — enough for most work. **5.0 Pro** is for images that need precise control of positions and elements. If Lumina's UI names things differently, follow the UI.

## Model facts

- Text-to-image, reference-guided editing and multi-reference fusion (Lite up to 14 references, Pro up to 10; the scripts cap at 10). Locks character identity across a series.
- Follows detailed, multi-step instructions, including text drawn in the image.
- Renders text natively in 10+ languages: put the exact words **in double quotes** and say where they go; write non-English text directly in that language (Chinese, Japanese…), don't ask for a translation.
- Output is clean enough to serve as a video first frame, so a still can seed a matching Seedance clip.

## Writing rules

1. Use **full natural-language sentences** (subject + action + environment), not keyword piles.
2. Order: **style → shot & angle → character (fixed appearance string) → action & expression → setting → light & mood → comic elements (comic only) → aspect ratio**.
3. With references, state each one's role: `Use image 1 for the character's face, hair and outfit. Use image 2 for the background location.`
4. 1–2 main characters per image; 3+ in one frame breaks most often.
5. For fixes, say "change only X, keep everything else", don't rewrite the whole prompt.

## Templates

### Character REF — comic (multi-view)
```
Character reference sheet of [fixed appearance string], [style lock]. Front view, three-quarter view, side view and back view standing in a row, full body, neutral pose, plus a row of 6 facial expressions: neutral, smile, angry, sad, surprised, determined. Plain white background, clean even lighting, no text.
```

### Character REF — anime (single front view)
```
[style anchor]. Full body character portrait of [fixed appearance string], standing upright facing the camera, both feet on the ground, whole body visible from head to shoes, [demeanor]. Plain clean white background, even lighting, no text, no watermark.
```
Video REFs use one front full-body image; multi-view sheets may make the video model duplicate the character. Outfit versions reuse the same appearance string and change only the clothes.

### Prop REF
```
Prop reference sheet of [prop description], [style lock]. Shown from front, side and top views on a plain white background, plus one view of it held in a hand for scale. No text.
```

### Location REF
```
Environment concept art of [location description], [style lock], wide establishing shot, no characters, [time & light], highly detailed background.
```

### Comic panel
```
[style lock]. [shot], [angle]. Use image 1 for the character's appearance. [fixed appearance string] [action and expression, full sentences]. Setting: [location]. [light & mood]. [comic elements: empty speech bubble at top right / speed lines / screentone]. Aspect ratio [ratio].
```

### Comic page draft (layout check only)
```
A manga page with [N] panels, read [right to left / left to right], clean gutters, [style lock].
Panel 1 (top, wide): …
Panel 2 (middle, close-up): …
Panel 3 (bottom, large): …
Keep [name] consistent with image 1 in every panel. Leave all speech bubbles empty.
```

### Text inside the image
```
… a speech bubble at the top left containing the text "[words in the user's language]" in a bold hand-lettered font …
… a large sound effect "[SFX]" in jagged white letters with a black outline across the panel …
```

### Anime keyframe (second 0, for Seedance image-to-video)
```
[style anchor]. [shot], [angle]. Use image 1 for [character A], image 2 for [character B], image 3 for the location. [second-0 positions, facing, pose, gaze, held items]. [time, light, weather]. No text, no speech bubbles. Aspect ratio [16:9 or 9:16].
```
- Freeze the character just **before** the action starts, not mid-action.
- Use the same style anchor as the Seedance prompts so the video keeps the look.
- To control the ending, also generate a last-second frame.

## Troubleshooting

| Problem | Fix |
|---|---|
| Character looks different each time | Always upload the REF; paste the appearance string verbatim; never change the style words |
| Faces of several characters blend | One REF per character, and say which image is who |
| Wrong or garbled drawn text | Shorter text in double quotes, or leave balloons empty and letter later |
| Broken hands or props | Change the angle so hands are out of frame, or inpaint just that area |
| Style drifts | Put the style lock first, and upload an approved image as a style reference |
