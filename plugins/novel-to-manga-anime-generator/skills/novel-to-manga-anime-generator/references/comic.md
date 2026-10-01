# Comic branch (steps ③ ④ ⑤ ⑦)

A comic's unit is the **panel**: one frozen moment. What you control is **pacing** (page breaks, panel size), **consistency** (REFs) and **reading flow**.

Language-dependent numbers (text per page, reading direction, balloon length) come from the table in SKILL.md.

## ③ Page breakdown

Split the source in story order. For each page write:

```
### Page 5 [Highlight page · 3 panels]
Source: from "…" to "…" (≈ N words/字)
[Location · time · light]
What happens: who does what, says what, how others react
[Beats on this page] 1. … 2. …
[Dialogue] Character: "…"
[Page-turn hook] …
```

**Page length** (see the language table for numbers):
- Narration / description-heavy text compresses → upper end of the range per page.
- Dense dialogue, detailed action, emotional scenes expand → lower end.
- Break where the state changes (an entrance, a key line, a reversal) — never in the middle of an action.

**Page types**

| Type | Panels | Used for |
|---|---|---|
| Regular page | 4–6 | dialogue, daily life, setup |
| Highlight page | 2–3 | key moves, reveals, emotional outbursts |
| Climax page | 1 full-page splash (spread if needed) | the strongest moment of the chapter |

- **Mix** for a 16–20 page chapter: 12–15 regular, 3–4 highlight, 0–1 climax (max 2 — more stops being special).
- **Page turns** (right-to-left manga): the last panel before a turn holds the question; highlight and climax pages go right after a page turn. For left-to-right comics, the same logic applies to the bottom-right panel of the right-hand page.
- **Redundancy**: if cutting something loses nothing for plot, character or emotion, merge or cut it. Don't pad.

**Converting prose to panels**

| Prose does | Comic does |
|---|---|
| Long inner monologue | expression close-up, small gesture (clenched fist, looking away), silent panel |
| Scenery description | one establishing wide panel, then background detail |
| Flashback / backstory | 1–3 flashback panels with faded edges, screentone or black borders |
| Abstract statements ("he was furious") | concrete images (veins, gritted teeth, a cup cracking) |
| Long dialogue | keep only the key lines; the rest via expressions |
| Multiple threads | one thread per page, separated by a scene-change panel |

Quiet emotional scenes often need *more* panels than fights: the tension lives in small reactions (eyes, hands, a turned back, an empty frame). A fight can be told in a few panels if only two moves matter.

## ④ Per-panel Context

For every panel:
- **[Panel]** page, number, size (large / medium / small / splash), aspect ratio
- **[Moment]** the frozen instant: who is where, facing which way, pose and expression, what they hold. Write visible things, not "the mood is tense".
- **[Shot & angle]**
- **[Text]** balloons (limits from the language table), caption boxes, sound effects
- **[REFs needed]** which REFs to upload (with outfit version)

**Continuity**: between adjacent panels, positions, outfits, props, injuries and time of day can't change by themselves; any change must happen inside some panel.

**Cause and direction**
- In a conversation, keep the two characters on fixed sides (180° rule).
- In fights, state who faces whom and the attack direction; someone knocked back needs an attacker.

**Page rhythm**
- Regular page: establish → advance → hook; alternate shot sizes between adjacent panels.
- Highlight page: wind-up (small) → peak (large) → reaction (small), or reaction (small) → reveal (large).
- Climax page: one image tells everything; low angle, broken panel borders, speed or focus lines; one line of dialogue at most.

**Reading flow**: characters' gaze and motion should lead the eye toward the next panel in reading order. For vertical webtoons, one panel per row; the white space between panels sets the pace; climaxes become extra-tall panels.

## ⑤ Seedream prompts (per panel)

Fixed structure (details and templates in `seedream.md`):
```
[style lock]. [shot], [angle]. [REF declaration: Use image 1 for …, image 2 for …]. [fixed appearance string] [the moment, full sentences]. Setting: [location]. [light & mood]. [comic elements]. Aspect ratio [ratio].
```
- REF upload order = image 1, image 2, … Attach only what appears in this panel (usually 1–4).
- Rewrite proper nouns as visible descriptions (models don't know the work's names).
- Balloons empty by default (`empty speech bubble`), letter them later; sound effects can be drawn, in double quotes.
- At most 1–2 main characters per panel; crowds of 3+ break most often.
- A whole page in one prompt (`A manga page with N panels…`) is for layout drafts only; final art is per panel.

## ⑦ Lettering, layout, QA

- Lay out panels, add balloons, text and sound effects in Canva (easy) or Clip Studio Paint (pro). Webtoons: a single tall vertical image.
- In API mode, `run_comic.py --preview` builds an HTML preview from the page layouts in the plan.
- QA: faces, hair, outfits, props match the REFs? Fingers and drawn text intact? Scene consistent with the previous panel? Then follow the error-routing order in SKILL.md.
