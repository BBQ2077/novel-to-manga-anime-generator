# Full example (comic): *Hamlet*, Act 1 Scenes 4–5 (public domain)

The user pastes Act 1 Scenes 4–5 (≈ 2,300 words): Hamlet, Horatio and Marcellus keep watch on the battlements; the Ghost appears and beckons; Hamlet breaks free of his friends and follows; the Ghost reveals he was murdered by Claudius and demands revenge; "Remember me."

Format: comic, left-to-right. Style lock: `European graphic novel style, ligne claire line work, muted watercolor palette, detailed backgrounds, moody night lighting`

---

## Round 1: ① REFs + ② adaptation outline

### ① REF list

| Type | Name | File |
|---|---|---|
| Character | Hamlet (mourning clothes) | char_hamlet_mourning.png |
| Character | Horatio | char_horatio.png |
| Character | Marcellus | char_marcellus.png |
| Character | The Ghost (King Hamlet) | char_ghost.png |
| Location | Castle battlements at night | loc_battlements.png |
| Prop | Hamlet's rapier | prop_rapier.png |

**Hamlet — fixed appearance string**
```
HAMLET: slender young Danish prince around 20, pale sharp-featured face, dark tired eyes with shadows beneath, untidy shoulder-length black hair, black mourning doublet with a high collar, black cloak, black hose and boots, no jewelry except a thin silver ring
```

**Hamlet — REF prompt**
```
Character reference sheet of HAMLET: slender young Danish prince around 20, pale sharp-featured face, dark tired eyes with shadows beneath, untidy shoulder-length black hair, black mourning doublet with a high collar, black cloak, black hose and boots, no jewelry except a thin silver ring. European graphic novel style, ligne claire line work, muted watercolor palette. Front view, three-quarter view, side view and back view standing in a row, full body, plus a row of expressions: neutral, grief, suspicion, terror, fury. Plain white background, no text.
```

**The Ghost — fixed appearance string**
```
THE GHOST: tall broad-shouldered king in his fifties, grey beard, stern hollow eyes, full steel plate armor with a raised visor, a dark royal cloak, the whole figure pale and faintly translucent with a cold blue glow
```
[added] The play gives armor, beard ("a sable silvered") and a pale face; the blue glow is added for readability.

**Battlements — location REF prompt**
```
Environment concept art of a stone castle battlement platform on a sea cliff at night, crenellated walls, a single brazier, a narrow stair down into a tower, the black sea far below, European graphic novel style, ligne claire line work, muted watercolor palette, cold moonlight and drifting mist. Wide establishing shot, no characters.
```

(Horatio, Marcellus and the rapier follow the same pattern.)

### ② Adaptation outline

- **Scope**: ≈ 2,300 words → 9 pages
- **Events**: the cold watch (keep) → Hamlet on Claudius's revels (cut to 1 panel) → the Ghost appears (keep) → it beckons, friends hold him back (keep) → Hamlet breaks free and follows (expand) → the revelation of the murder (expand) → **"Remember me"** (climax) → Hamlet swears his friends to secrecy (keep)
- **Opening hook**: page 1 ends with a pale shape on the far wall that only the reader sees
- **Climax**: the Ghost towering in the moonlight saying "Remember me" → page 8, splash
- **Ending hook**: "The time is out of joint" — Hamlet alone, deciding to feign madness
- **Inner monologue**: Hamlet's spoken reflections are cut to their core lines; his doubt is shown by his hand hovering over the rapier hilt

---

## Round 2: ③ Page breakdown

| Page | Source | Words | Type | Focus | Page-turn hook |
|---|---|---|---|---|---|
| 1 | "The air bites shrewdly" → the cannon of Claudius's revels | ~300 | Regular, 5 | Cold, tense watch | A pale shape on the far wall |
| 2 | "Look, my lord, it comes!" → "Angels and ministers of grace defend us!" | ~200 | Regular, 4 | The Ghost appears | The Ghost beckons |
| 3 | Friends warn him not to follow | ~300 | Regular, 6 | Fear vs. resolve | Hamlet's hand on his rapier |
| 4 | "Unhand me, gentlemen" → he follows | ~150 | **Highlight, 3** | Breaking free | Hamlet disappears into the dark |
| 5 | "Whither wilt thou lead me?" → "I am thy father's spirit" | ~300 | Regular, 5 | Identity revealed | "Revenge his foul and most unnatural murder" |
| 6 | "Murder most foul" → the poison in the ear | ~350 | Regular, 5 | The murder in flashback | "Now wears his crown" |
| 7 | The Ghost's charge about the Queen → dawn approaches | ~250 | **Highlight, 3** | Hamlet's fury | The Ghost starts to fade |
| 8 | "Adieu, adieu, adieu. Remember me." | ~100 | **Climax, splash** | The farewell | — |
| 9 | Friends arrive; the oath; "The time is out of joint" | ~350 | Regular, 6 | Secrecy and resolve | Hamlet alone at dawn |

Pages 7 and 8 are a pair: page 7 ends on the fading Ghost; the page turn reveals the splash.

**Page 4 breakdown**
```
### Page 4 [Highlight page · 3 panels]
Source: from "Hold off your hands" to "Go on; I'll follow thee" (≈ 150 words)
[Battlements · midnight · moonlight through mist]
What happens: Horatio and Marcellus grab Hamlet's arms; he tears free, draws his rapier on them, and turns to follow the Ghost.
[Beats] 1. Two hands gripping his cloak  2. The blade flashing toward his friends  3. Hamlet's back as he walks into the dark
[Dialogue] Hamlet: "Unhand me, gentlemen." / "I'll make a ghost of him that lets me!"
[Page-turn hook] Only mist where Hamlet stood
```

---

## Round 3: ④ Per-panel Context + ⑤ Prompts (pages 4 and 8)

### Page 4 (highlight, 3 panels)

| Panel | Size | Shot / angle | Moment | Text | REFs |
|---|---|---|---|---|---|
| 1 | small | close-up | Horatio's and Marcellus's hands clamp onto Hamlet's cloak | Hamlet: "Unhand me, gentlemen." | Hamlet, Horatio, Marcellus |
| 2 | **large (over half the page)** | medium, low angle | Hamlet wrenches free and swings his drawn rapier toward his friends, who stumble back | Hamlet: "I'll make a ghost of him that lets me!" | Hamlet, Horatio, Marcellus, rapier, battlements |
| 3 | small | wide, high angle | Hamlet's back walking into the mist toward the faint glow | — | Hamlet, battlements |

**Page 4, panel 2 — Context**
- [Panel] p04_2, large, 4:3
- [Moment] Hamlet, centre, facing left toward his friends, has just torn free; rapier drawn in his right hand, point toward Horatio; cloak swirling. Horatio (left) and Marcellus (far left) stumble back with raised hands.
- [Shot & angle] medium, low angle
- [Text] one balloon, top right
- [REFs] char_hamlet_mourning, char_horatio, char_marcellus, prop_rapier, loc_battlements

**Page 4, panel 2 — Prompt** (upload: image 1 = char_hamlet_mourning, image 2 = char_horatio, image 3 = char_marcellus, image 4 = prop_rapier, image 5 = loc_battlements)
```
European graphic novel style, ligne claire line work, muted watercolor palette, detailed backgrounds, moody night lighting. Medium shot, low angle. Use image 1 for Hamlet, image 2 for Horatio, image 3 for Marcellus, image 4 for the rapier and image 5 for the location. HAMLET: slender young Danish prince around 20, pale sharp-featured face, dark tired eyes, untidy shoulder-length black hair, black mourning doublet with a high collar, black cloak. In the centre he has just wrenched himself free and faces left, his drawn rapier in his right hand pointing at Horatio, his cloak swirling behind him, his face fierce and wild. On the left, Horatio and Marcellus stumble backwards with their hands raised. Stone battlements at night, mist, cold moonlight from behind Hamlet. One empty speech bubble at top right. Aspect ratio 4:3.
```

### Page 8 (climax, single splash)

| Panel | Size | Shot / angle | Moment | Text | REFs |
|---|---|---|---|---|---|
| 1 | splash | full body, extreme low angle | The Ghost towers on the parapet against the moon, one gauntleted hand pointing down at Hamlet, his form dissolving into mist at the edges; Hamlet kneels below, looking up | Ghost: "Remember me." | Ghost, Hamlet, battlements |

**Page 8 — Prompt** (upload: image 1 = char_ghost, image 2 = char_hamlet_mourning, image 3 = loc_battlements)
```
European graphic novel style, ligne claire line work, muted watercolor palette, detailed backgrounds, moody night lighting. Full-page splash, full body, extreme low angle. Use image 1 for the ghost king, image 2 for Hamlet and image 3 for the location. THE GHOST: tall broad-shouldered king in his fifties, grey beard, stern hollow eyes, full steel plate armor with a raised visor, a dark royal cloak, pale and faintly translucent with a cold blue glow. He towers on the parapet in front of a huge full moon, one gauntleted hand pointing down, the edges of his body dissolving into drifting mist. Below, Hamlet kneels on the stones looking up, his face torn between grief and terror. Cold blue moonlight, deep shadows. One speech bubble near the ghost containing the text "Remember me." in thin pale hand-lettered capitals. Aspect ratio 2:3.
```

---

## ⑥ API mode: comic_plan.json (excerpt)

```json
{
  "lang": "en",
  "style_anchor": "European graphic novel style, ligne claire line work, muted watercolor palette, detailed backgrounds, moody night lighting.",
  "reading_direction": "ltr",
  "refs": [
    {"id": "char_hamlet_mourning", "prompt": "Character reference sheet of HAMLET: ..."},
    {"id": "char_ghost", "prompt": "Character reference sheet of THE GHOST: ..."},
    {"id": "loc_battlements", "prompt": "Environment concept art of a stone castle battlement platform ..."}
  ],
  "panels": [
    {"id": "p08_1", "refs": ["char_ghost", "char_hamlet_mourning", "loc_battlements"], "aspect": "2:3",
     "prompt": "Full-page splash, full body, extreme low angle. Use image 1 for the ghost king, image 2 for Hamlet and image 3 for the location. ..."}
  ],
  "pages": [
    {"id": "p08", "type": "climax", "rows": [["p08_1"]]}
  ]
}
```
The full plan lists every panel; `pages` may only reference panel ids that exist in `panels`, or `--check` stops.
```bash
python scripts/run_comic.py comic_plan.json --check          # check and count, free
python scripts/run_comic.py comic_plan.json --stage refs     # REFs first, for approval
python scripts/run_comic.py comic_plan.json --stage panels   # all panels + preview.html
```

## ⑦ Lettering and checks

- Lay out page 4 in Canva or Clip Studio Paint: one small panel on top, the large panel across the middle, one small panel at the bottom.
- Check: Hamlet is in black mourning clothes in every panel; the rapier only appears after he draws it; the Ghost's glow is the same blue on pages 2, 5 and 8.

## Generation count

- REFs: 4 characters + 1 location + 1 prop = 6 (≈ 9 with retries)
- Panels: 9 pages ≈ 38 panels × 1.5–2 ≈ 57–76 images

> 👉 **Recommended: subscribe to BytePlus Lumina** — fixed monthly fee, generate right in the browser, best value for normal use → https://byteplus.pxf.io/vDqjnd
> 🤖 Want an AI agent to generate everything automatically in bulk? Activate the **BytePlus ModelArk API** (pay per use) → https://byteplus.pxf.io/c/7876220/3836120/48404
> (affiliate links)
>
> ⚠️ If you don't hold the rights to the original work, do not use the result commercially.
