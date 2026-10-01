# Plan file formats (API mode)

After the user confirms the content, the agent writes one of these files and runs the matching script. `lang` (`"zh"`, `"en"`, `"ja"`) sets the language of the script's messages. `style_anchor` is prepended to every prompt automatically — **don't repeat it inside prompts**.

## comic_plan.json → `scripts/run_comic.py`

```json
{
  "lang": "en",
  "style_anchor": "European graphic novel style, ligne claire line work, muted watercolor palette, detailed backgrounds.",
  "reading_direction": "ltr",
  "delay_seconds": 0,
  "refs": [
    {"id": "char_hamlet", "prompt": "Character reference sheet of HAMLET: ... Plain white background, no text."},
    {"id": "loc_battlements", "prompt": "Environment concept art of ..."},
    {"id": "prop_skull", "file": "my_refs/skull.png"}
  ],
  "panels": [
    {"id": "p03_2", "refs": ["char_hamlet", "loc_battlements"], "aspect": "4:3",
     "prompt": "Medium shot, low angle. Use image 1 for the character's appearance and image 2 for the location. ..."}
  ],
  "pages": [
    {"id": "p03", "type": "highlight", "rows": [["p03_1", "p03_2"], ["p03_3"]]}
  ]
}
```

| Field | Meaning |
|---|---|
| `reading_direction` | `rtl` (manga, default) or `ltr` (Western comics, webtoon); affects the preview only |
| `delay_seconds` | pause between panels; raise it on HTTP 429 |
| `refs[].prompt` / `refs[].file` | generate the REF, or use an existing image (path relative to the plan) |
| `panels[].refs` | REFs to upload; **order = image 1, image 2 … in the prompt** (max 10) |
| `panels[].aspect` | `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, `2:3`, `21:9`, or pixels like `2048x1536` |
| `panels[].seed` | optional, for reproducibility |
| `pages[].rows` | layout: each array is one row of panel ids in reading order |

Output: `output/refs/`, `output/panels/`, `output/preview.html`, `output/manifest.json`.

## anime_plan.json → `scripts/run_anime.py`

```json
{
  "lang": "ja",
  "style_anchor": "Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field.",
  "duration": 12,
  "ratio": "16:9",
  "resolution": "720p",
  "generate_audio": true,
  "refs": [
    {"id": "char_kaguya_juni", "prompt": "Full body character portrait of KAGUYA: ..."},
    {"id": "loc_bamboo_grove", "file": "my_refs/bamboo.png"}
  ],
  "shots": [
    {"id": "s01", "mode": "i2v",
     "keyframe_refs": ["char_okina", "loc_bamboo_grove"],
     "keyframe_prompt": "Wide shot, eye level. Use image 1 for the old man and image 2 for the location. ...",
     "video_prompt": "[Dusk · bamboo grove · calm, warm side light]\nThe camera frames ... in a wide shot.\n0–4 s: ..."},
    {"id": "s02", "mode": "i2v", "first_frame_from": "s01",
     "video_prompt": "The camera slowly pushes in on ...\n0–6 s: ..."},
    {"id": "s03", "mode": "r2v",
     "video_refs": ["char_okina", "char_kaguya_child", "loc_bamboo_grove"],
     "video_prompt": "@Image1 defines the old man's appearance only. @Image2 ... \n0–4 s: ..."}
  ]
}
```

### Modes

| mode | Flow | When |
|---|---|---|
| `i2v` (default, most stable) | Seedream makes the second-0 keyframe from REFs; Seedance animates it | most shots |
| `i2v` + `first_frame_from` | the previous shot's last frame becomes this shot's first frame | continuous shots (same scene, no transition) |
| `r2v` | REFs go straight to Seedance via `@Image1…` | multi-character interaction, hard-to-control keyframes |

i2v `video_prompt` must not use `@Image`; describe only motion and change.

| Field | Meaning |
|---|---|
| `duration` | seconds per shot (4–30), same for every shot; per-shot overrides need `allow_mixed_duration: true` |
| `ratio` | `16:9`, `9:16`…; also sets keyframe size |
| `resolution` | optional, e.g. `720p`, `1080p`, depending on model and plan |
| `generate_audio` | `true`: native dialogue/SFX/music; `false`: silent, voice added in post |
| `shots[].keyframe_refs` | i2v: order = image 1, image 2 … in the keyframe prompt (max 10) |
| `shots[].keyframe_file` | optional existing second-0 image |
| `shots[].last_frame_file` | optional last-second image (first/last-frame control) |
| `shots[].first_frame_from` | optional (i2v): id of an earlier shot whose last frame becomes this shot's first frame; no keyframe prompt needed |
| `shots[].video_refs` | r2v: order = `@Image1`, `@Image2` … (recommended max 5) |
| `shots[].seed` | optional |

Output: `output/refs/`, `output/keyframes/`, `output/videos/`, `output/lastframes/`, `output/final.mp4` (`--concat`, needs ffmpeg), `output/manifest.json`.

Video task ids are saved in the manifest as soon as they're submitted; after a disconnect, re-running resumes waiting on the same tasks instead of submitting (and paying) again.

## What the scripts check automatically

- Missing style anchor; REFs without prompt/file or missing files; unknown REF ids; duplicate ids
- Comic: `image 3` in a prompt with only 2 REFs attached; more than 10 REFs; layouts pointing to unknown panels
- Anime: duration outside 4–30 s or uneven durations; i2v without a keyframe or with `@Image`; `@Image3` with only 2 REFs; more than 5 video REFs; `first_frame_from` pointing to a later shot or used in r2v

The scripts only catch format errors. Continuity, direction and cause-and-effect must still be checked by the agent against the hard gate in SKILL.md before writing the plan.
