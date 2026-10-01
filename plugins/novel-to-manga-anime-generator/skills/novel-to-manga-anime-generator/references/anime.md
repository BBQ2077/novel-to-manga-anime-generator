# Anime branch (steps ③ ④ ⑤ ⑦)

A comic is "one panel, one image"; anime is "one shot, a span of time". Video adds three things to manage: **time, continuity and sound** — which is why this branch has two extra layers (per-minute outline and per-shot Context).

Language-dependent defaults (dialogue language, script length per minute) come from the table in SKILL.md.

## Reference numbers

- A Japanese TV anime episode (~22 min) has about 300 cuts; a typical cut is 2–5 s, long ones 8–15 s.
- AI generation produces one clip at a time (Seedance 2.5: 4–30 s), so a clip can contain 2–4 cuts via `Shot 1 / Shot 2`. Keep the overall rhythm close to real anime; don't let a whole clip be one static shot.
- Script volume: a 3-minute short needs roughly a 300–400-word script. Novel text usually has to be compressed several times over to become a script.

## ③ Per-minute outline

For each minute:

```
### 0:00–1:00
[Time/light · location · weather]
What happens: who does what, says what, how others react, what the viewer sees
[Beats this minute] 1. … 2. … 3. …
[Dialogue / narration this minute]
- Character (on screen): "…" — purpose: advance the plot
- Narrator (off screen): "…" — purpose: establish time
```

- 3–4 beats per minute; climax sections 8–10. Roughly one beat every 10–20 s. A beat can be plot, action, expression, interaction, information, a joke, spectacle, lighting or plain visual beauty.
- Only refine the outline: no new major events, characters or twists.
- Time, outfits, injuries and held items must carry over from minute to minute.
- Redundancy test: if walking, staring, repeating the same expression or information could be cut with no loss, merge or cut it.
- Test: **reading only the outline, can you picture what happens, what is seen and what is heard this minute?**

## ④ Per-shot Context

Split the outline into generatable shots. **Use one fixed length for every shot** (10–15 s recommended, e.g. 12 s everywhere; Seedance 2.5 allows 4–30 s). If an event doesn't fit, re-split here — never leave it for the prompt to solve.

Each shot:
- **[Link]** continuous or transition (for transitions: how much time passed, new location)
- **[Second 0]** time, light, location, positions, facing, pose, gaze, held items, any change left by the previous shot
- **[Main event]** one main event per shot: who does what to whom, how, and the result
- **[Last second]** the end state, so the next shot can pick up directly
- **[REFs needed]** which REFs (with outfit version)

**Continuity**: shot N's last second = shot N+1's second 0. Position, outfit, props, injuries, time of day and damage can't change between shots.

**Cause and direction**: for fights, standoffs and chases, state who faces whom, the movement direction and the attack direction. A body thrown back needs an attacker; a door that opens needs someone to open it.

**Dialogue**
- Short lines (≈ 7 words / 7 字 / 7 文字 or less) can be lip-synced on screen.
- Long lines, narration and off-screen voices: **audio-visual separation** — show the listener's reaction, a back view, hands or the environment; add the voice in post.
- Max 2–3 lines per shot, ~0.25 s gap between lines. Lines don't replace visuals ("I'm scared" isn't a visible fear).

**Shot variety**: occasionally use high angle, wide establishing, side tracking or bird's-eye; close-ups for faces, eyes, hands and key props. Don't repeat the same framing shot after shot. Every shot must answer: what does the viewer look at, and what is lost if it's cut?

## ⑤ Keyframes and Seedance prompts

**Keyframes (Seedream)**: for each shot, generate **the second-0 frame** with the REFs (optionally the last second too) and use it for image-to-video. This is the most stable way to keep characters consistent.

**Continuous shots** (same scene, no transition): skip the keyframe and let Seedance return the previous shot's **last frame** as this shot's first frame — positions, outfits and light carry over naturally (API mode: `first_frame_from`). Transitions and new locations get a fresh Seedream keyframe.

**Seedance prompt structure** (details in `seedance.md`):
1. **Style anchor** — one text for the whole film, never changed
2. **[Time · location · weather or light source]**
3. **REF declaration** (r2v mode only; in i2v mode the keyframe is the first frame and the prompt only describes motion): `@Image1` is who, `@Image2` is where. Max 4–5 per shot.
4. **Second-0 picture**: background, positions, facing
5. **Camera subject and framing**: "The camera frames … in a medium shot"
6. **Timeline**: 1–3 segments (4 for intense scenes), covering every second with no gaps or overlaps

Rules:
- Proper nouns → visible descriptions.
- Hits, explosions, collisions: describe the force and the visible result.
- In fight shots, restate facing in **every** segment, or characters drift to face away from the enemy.
- One main camera move per segment, max 3 per shot; avoid 360° orbits and violent shaking.
- Never ask for readable text in video (it garbles); subtitles go in post.
- No meta-instructions like "continue from the previous shot" — describe what the frame looks like now.

## ⑦ Sound, editing, QA

**Sound** — pick one for the whole film:
- A. Seedance native audio: `{dialogue}`, `<sound effect>`, `(music)` — good for short lines.
- B. Silent video, voice added afterwards (TTS or human) — most control, better for dialogue-heavy films. Re-align timing to the actual audio file length.

**Editing**: join clips, add music, subtitles and color in CapCut or DaVinci Resolve. Always time things against the actual generated clip lengths. In API mode, `run_anime.py --concat` joins clips with ffmpeg.

**QA** (generated clips): characters, outfits, locations, creatures, weapons match the REFs? Time of day, light, positions, facing, gaze and attack direction as written? Extra or missing limbs, anime turning photoreal, duplicated or vanished characters? Then follow the error-routing order in SKILL.md.
