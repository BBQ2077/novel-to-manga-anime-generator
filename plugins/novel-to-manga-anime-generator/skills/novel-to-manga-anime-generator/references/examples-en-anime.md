# Full example (anime): *Hamlet*, Act 1 Scenes 4–5 → 3-minute anime (public domain)

The user pastes Act 1 Scenes 4–5 and asks for a 3-minute, 16:9 anime with English dialogue.

**Style anchor** (fixed for the whole film)
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field.
```

---

## Round 1: ① REFs + ② outline

### REF list

| Type | File | Note |
|---|---|---|
| Character | char_hamlet_mourning.png | single front full-body, white background |
| Character | char_horatio.png | |
| Character | char_ghost.png | armored king, translucent |
| Character | char_claudius.png | for the orchard flashback |
| Character | char_king_robe.png | the living king in the flashback: same face as the Ghost, solid, in a sleeping robe (outfit change → its own REF) |
| Location | loc_battlements.png | stone platform on a sea cliff, brazier, tower stair |
| Prop | prop_rapier.png | not drawn into Hamlet's character REF |

**char_hamlet_mourning**
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting. Full body character portrait of HAMLET: slender young Danish prince around 20, pale sharp-featured face, dark tired eyes with shadows beneath, untidy shoulder-length black hair, black mourning doublet with a high collar, black cloak, black hose and boots, a thin silver ring. Standing upright facing the camera, both feet on the ground, whole body visible from head to boots, brooding expression. Plain clean white background, even lighting, no text, no watermark.
```

### Adaptation outline (3 minutes)

| Time | Content |
|---|---|
| 0:00–0:30 | **Hook**: mist rolls over a moonlit castle; a pale armored figure glides along the far wall — then is gone. Cannons boom from the feast below. |
| 0:30–1:00 | Hamlet and Horatio on the watch; the Ghost appears and beckons; Horatio holds him back; Hamlet breaks free |
| 1:00–1:40 | Hamlet follows the Ghost to the edge of the cliff; "I am thy father's spirit" |
| 1:40–2:40 | **Climax** (60 s, a third of the runtime): the murder revealed — flashback of Claudius pouring poison into the sleeping king's ear; "Remember me" as the Ghost dissolves at dawn |
| 2:40–3:00 | Hamlet alone, sword raised like a cross: "The time is out of joint." |

**Voice plan**: no narrator; English dialogue; speakers Hamlet, Horatio, the Ghost. The Ghost's long speech is audio-visually separated (voice over the flashback).

---

## Round 2: ③ Per-minute outline (excerpt 1:40–2:40)

```
### 1:40–2:40
[Night turning to grey dawn · cliff-edge corner of the battlements · wind, mist thinning]
What happens: The Ghost tells how he was murdered while sleeping in his orchard.
Flashback: a sunlit orchard, the old king asleep on a bench; Claudius creeps up and pours
a dark vial into his ear; the king's skin blisters and he convulses. Back on the cliff,
Hamlet's knuckles whiten on his rapier hilt. A rooster crows far away; the Ghost begins
to fade from the feet up, raises a hand toward Hamlet and dissolves into the dawn mist.
Hamlet reaches out and grasps empty air.
[Beats]
1. Orchard flashback in warm, saturated color (contrast with the cold present)
2. The vial tipping — extreme close-up
3. Hamlet's white knuckles on the hilt
4. The Ghost fading from the feet up as first light hits
5. Hamlet's hand closing on empty mist
[Dialogue]
- Ghost (voice-over, long): "Sleeping within my orchard, my custom always of the afternoon…" — purpose: the reveal
- Ghost (on screen, short): "Remember me." — purpose: climax line
- Hamlet (on screen, short): "Remember thee!" — purpose: his vow
```

---

## Round 3: ④ Context + ⑤ keyframe + Seedance prompt (two consecutive 12 s shots)

### Shot 11

**[Link]** continuous
**[Second 0]** Grey pre-dawn light. The Ghost stands on the left on the stone parapet, facing right toward Hamlet; Hamlet stands on the right, facing left, his right hand on the hilt of his sheathed rapier. Mist at knee height.
**[Main event]** A rooster crows; the Ghost's feet begin to dissolve into mist; he raises one gauntleted hand toward Hamlet and says "Remember me."
**[Last second]** Only the Ghost's raised hand and face remain, almost transparent; Hamlet has stepped one pace forward, still facing left.
**[REFs]** char_ghost, char_hamlet_mourning, loc_battlements

**⑤ Keyframe (second 0)**
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting. Medium wide shot, eye level. Use image 1 for the ghost king, image 2 for Hamlet and image 3 for the location. On the left, the translucent armored ghost king stands on the stone parapet facing right; on the right, Hamlet in black mourning clothes faces him, his right hand resting on the hilt of a sheathed rapier. Grey pre-dawn light from the right, knee-high mist over the stones, the sea far below. No text. Aspect ratio 16:9.
```

**⑥ Seedance prompt** (i2v: upload the keyframe as the first frame; describe only motion)
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field. [Pre-dawn · cliff-edge battlements · wind, mist thinning, grey light from the right]
The camera frames the ghost king and Hamlet in a medium wide shot.
0–4 s: A gust of wind sweeps the mist; the ghost king, facing right toward Hamlet, begins to dissolve from the feet up into pale vapor.
4–8 s: The camera slowly pushes in on the ghost king; still facing Hamlet, he raises one gauntleted hand toward him and speaks at second 5–7.
8–12 s: The camera cuts to a medium shot of Hamlet facing left; he steps one pace forward, eyes wide, as the light on his face turns warmer. The ghost's appearance stays consistent with the first frame until it fades.
Dialogue language: English, the ghost speaks low and echoing. {Remember me.}
<distant rooster crow> <wind over stone> (a single sustained cello note)
```

### Shot 12 (chained: first frame = last frame of shot 11)

**[Link]** continuous
**[Second 0]** = last second of shot 11
**[Main event]** The last of the Ghost vanishes; Hamlet lunges and closes his hand on empty mist, then sinks to one knee.
**[Last second]** Hamlet kneeling, facing left toward the empty parapet, first sunlight on his face.
**[REFs]** none needed — the first frame carries everything

**⑥ Seedance prompt** (i2v, `first_frame_from: s11`)
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field. [Dawn · cliff-edge battlements · wind dropping, first sunlight from the right]
The camera frames Hamlet in a medium shot.
0–5 s: The last pale wisps of the ghost blow away over the parapet; Hamlet, facing left, lunges and closes his right hand on empty mist.
5–9 s: The camera holds on Hamlet's empty fist in a close-up, trembling.
9–12 s: The camera pulls out to a medium wide shot; Hamlet sinks to one knee, still facing the empty parapet on the left, sunlight spreading across the stones. He speaks at second 10–11.
Dialogue language: English, Hamlet whispers, shaken. {Remember thee!}
<wind fading> (the cello resolves into a quiet chord)
```

---

## ⑦ API mode: anime_plan.json (excerpt)

```json
{
  "lang": "en",
  "style_anchor": "Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field.",
  "duration": 12, "ratio": "16:9", "generate_audio": true,
  "refs": [
    {"id": "char_hamlet_mourning", "prompt": "Full body character portrait of HAMLET: ..."},
    {"id": "char_ghost", "prompt": "Full body character portrait of THE GHOST: ..."},
    {"id": "loc_battlements", "prompt": "Environment concept art of a stone castle battlement platform ..."}
  ],
  "shots": [
    {"id": "s11", "mode": "i2v",
     "keyframe_refs": ["char_ghost", "char_hamlet_mourning", "loc_battlements"],
     "keyframe_prompt": "Medium wide shot, eye level. Use image 1 for the ghost king, image 2 for Hamlet and image 3 for the location. ...",
     "video_prompt": "[Pre-dawn · cliff-edge battlements · wind, mist thinning]\nThe camera frames the ghost king and Hamlet in a medium wide shot.\n0–4 s: ..."},
    {"id": "s12", "mode": "i2v", "first_frame_from": "s11",
     "video_prompt": "[Dawn · cliff-edge battlements · first sunlight]\nThe camera frames Hamlet in a medium shot.\n0–5 s: ..."}
  ]
}
```
```bash
python scripts/run_anime.py anime_plan.json --check              # check and count, free
python scripts/run_anime.py anime_plan.json --stage refs         # REFs, for approval
python scripts/run_anime.py anime_plan.json --stage keyframes    # keyframes, for approval
python scripts/run_anime.py anime_plan.json --stage videos       # submit and download videos
python scripts/run_anime.py anime_plan.json --concat             # join into final.mp4
```

## Hard gate (shots 11–12)

- [x] Shot 11 keyframe has 3 REFs in upload order; shot 12 is chained, no REFs
- [x] Shot 11 last second = shot 12 second 0 (positions, facing, light)
- [x] Facing restated in every segment (Ghost faces right, Hamlet faces left)
- [x] Proper nouns rewritten (King Hamlet → the ghost king; Elsinore → battlements on a sea cliff)
- [x] No readable text requested in the video
- [x] The Ghost's long orchard speech is voice-over on the flashback shots, not lip-synced

## Generation count (3 minutes = 15 shots × 12 s)

- REFs: 5 characters + 1 location + 1 prop = 7 (≈ 10 with retries)
- Keyframes: ~10 (5 shots are chained) × 1.5 ≈ 15
- Video: 180 s × 1.5–2 ≈ 270–360 s

> 👉 **Recommended: subscribe to BytePlus Lumina** — fixed monthly fee, generate right in the browser, best value for normal use → https://byteplus.pxf.io/vDqjnd
> 🤖 Want an AI agent to generate everything automatically in bulk? Activate the **BytePlus ModelArk API** (pay per use) → https://byteplus.pxf.io/c/7876220/3836120/48404
> (affiliate links)
>
> ⚠️ If you don't hold the rights to the original work, do not use the result commercially.
