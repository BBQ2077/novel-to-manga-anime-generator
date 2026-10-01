# Seedance prompts (per-shot video)

Based on public Seedance 2.5 material (2026). Specs vary by plan and interface; follow what Lumina / ModelArk actually offers.

## Model facts

- 4–30 s per generation; multi-shot storytelling inside one generation.
- References: up to 30 images, 10 videos, 10 audio clips.
- Native dialogue, sound effects and music with lip sync, 10+ languages.
- Image-to-video with a first frame and an optional last frame. "First/last frame" mode and "multimodal reference" mode can't be mixed.

## Fixed per-shot structure

```
[style anchor]. [Time · location · weather / light source]
[REF declaration — r2v only]
[Second-0 picture: background, positions, facing, pose, held items]
The camera frames [subject] in a [shot size].
0–4 s: [subject + action/change + camera move]
4–8 s: …
8–12 s: …
[Sound: dialogue, effects, music]
```

### 1. Style anchor
One text for the whole film, unchanged, always first. Example:
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field.
```

### 2. REF declaration (r2v mode)
```
@Image1 defines Hamlet's face, hair and mourning outfit; do not use the image background. @Image2 defines the castle battlements location.
```
- One sentence per reference saying what it provides.
- Characters with a REF don't need their fixed look re-described, unless the shot changes it (new outfit, wounds).
- 4–5 references per shot at most; beyond that prioritize characters > key props > location.
- In **i2v mode** there is no REF declaration: the keyframe is the first frame; describe only what moves and changes, not what is already visible.

### 3. Second-0 picture
Only what is visible at the start. For continuous shots it must match the previous shot's last second — but never write "continuing from the previous shot"; describe the frame:
- ✗ `Continuing from the last shot, the bus is damaged.`
- ✓ `A bus with its side caved in stands in the middle of the road, black smoke pouring from the breach.`

### 4. Camera subject
Always `The camera frames <subject> in a <shot size>`. Never just "the camera moves".

### 5. Timeline
- 1–3 segments (4 for intense scenes), covering every second, no gaps or overlaps.
- Each segment: time + concrete subject + action or visible change.
- A segment's end state is the next segment's start.
- When framing changes, say how (push in, cut to…).
- Long takes (`0–12 s` as one segment): start state → continuous change → settled end, with 1–2 s of lead-in and lead-out; keep long takes under ~20% of all shots.
- Real cuts inside a clip: `Shot 1 [0–4 s]: … Shot 2 [4–9 s]: cut to …`

## Camera moves

- Preferred: static, push in, pull out, tracking, turning toward the subject, close-up on the subject.
- Occasionally: high angle, wide establishing, side tracking, bird's-eye.
- Avoid: 360° orbits, spinning, violent shaking — the most common causes of deformed characters.
- One main move per segment, max 3 per shot.

## Action, fights, physics

- Write the process: "raises the sword, then brings it down" beats "attacks".
- **Fights: restate facing in every segment** ("Hamlet faces Laertes on the left"), or characters drift to face away from the enemy.
- Hits, explosions, collisions: force + visible result.
  - ✗ `The blade hits him.`
  - ✓ `The rapier's tip grazes Laertes's arm; his sleeve tears and he staggers back two steps.`
- State counts explicitly ("one guard", "two ravens"); never let the model choose.

## Proper nouns

The model doesn't know the work's names; rewrite them as visible descriptions:

| Source | In the prompt |
|---|---|
| Elsinore | a grey stone Danish castle on a sea cliff |
| the Ghost of King Hamlet | a pale translucent king in full armor, glowing faintly |
| 金箍棒 | a long black iron staff banded with gold at both ends |
| かぐや姫 | a young noblewoman in layered Heian-era robes with very long black hair |

Names can stay in the outline and Context, not in generation prompts.

## Sound

### A. Native audio
| Brackets | Use | Example |
|---|---|---|
| `{ }` | dialogue | `{To be, or not to be.}` |
| `< >` | sound effect | `<waves crashing against the cliff>` |
| `( )` | music | `(a low cello drone builds slowly)` |
| `【 】` | on-screen subtitle | not recommended — add subtitles in post |

- Declare language and delivery **before** the line: `Dialogue language: English, Hamlet speaks quietly, bitter.` Only the words go inside `{ }`.
- Short lines (≈ 7 words or less) can be lip-synced; give the second they're spoken.
- Long lines, narration, off-screen voices: don't put the words or speaking verbs in the prompt; show the listener, a back view, hands or the setting, and add the voice in post.
- Commas make pauses, periods end lines; many clauses increase drift.

### B. Silent generation, voice in post
No `{ }` in the prompt, visuals only. Plan line timing from the outline and Context, then re-align to the **actual audio file length** after recording.

## Common mistakes

| Mistake | Fix |
|---|---|
| Style anchor differs between shots | One anchor for the whole film, verbatim |
| @Image numbering doesn't match upload order | Renumber by this shot's upload order |
| Proper nouns in the prompt | Rewrite as visible descriptions |
| Abstract emotion ("she is nervous") | Visible signs (fingers twisting her sleeve, eyes darting) |
| Action without result | Add force and visible outcome |
| Several events in one shot | Go back to the Context and re-split |
| Asking for readable text | Remove it; subtitles in post |
