# Novel to Manga & Anime Generator

**English** | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

An AI agent plugin that turns novel text into a **manga / comic / webtoon** or an **anime-style video**. Paste a chapter, choose comic or video, and the agent walks you through a full production pipeline and writes ready-to-use prompts for **Seedream** (images) and **Seedance** (video).

Works with **ChatGPT**, **Codex** and **Claude Code**. Replies in your language: English, 中文, 日本語.

## What it does

1. **REF sheets** — characters, locations and props, so every panel and shot stays consistent
2. **Adaptation outline** — what to keep, merge or cut; opening hook, climax, ending hook
3. **Comic**: page breakdown (regular / highlight / climax pages) → per-panel context → Seedream prompts → lettering
   **Anime**: per-minute outline → per-shot context (start state, event, end state) → keyframes → Seedance prompts → sound & editing
4. **QA** — a pre-generation checklist and a fix-in-order rule (Context → REF → Prompt → result)
5. **Optional automation** — Python scripts let an agent generate every image and video through the BytePlus ModelArk API

Full worked examples use public-domain classics: *Hamlet* (English), 西遊記 (Chinese), 竹取物語 (Japanese).

## Install

### ChatGPT
**Option A — add this repo as a marketplace**
1. ChatGPT → **Plugins** → **Add** → **Add marketplace**
2. Paste `https://github.com/BBQ2077/novel-to-manga-anime-generator`
3. Install **Novel to Manga & Anime Generator**

**Option B — upload the archive**
1. Download [`dist/novel-to-manga-anime-generator-plugin.zip`](dist/novel-to-manga-anime-generator-plugin.zip)
2. ChatGPT → **Plugins** → **Add** → **Upload plugin archive**

### Codex
Add this repository as a plugin marketplace, then install `novel-to-manga-anime-generator`.

### Claude Code
```
/plugin marketplace add BBQ2077/novel-to-manga-anime-generator
/plugin install novel-to-manga-anime-generator@manga-anime-tools
```

## Try it

- `Turn this chapter into a manga: [paste text]`
- `Make a 3-minute anime from this scene: [paste text]`

## Generating the images and videos

| | Subscription — **BytePlus Lumina** (recommended) | API — **BytePlus ModelArk** |
|---|---|---|
| Best for | Most people: a few chapters or episodes, tweaking as you go | Letting an agent generate everything automatically in bulk |
| Cost | Fixed monthly fee | Pay per use |
| How | Paste the prompts into the web app | Set an API key; the plugin's scripts do the rest |
| Link | https://byteplus.pxf.io/vDqjnd | https://byteplus.pxf.io/c/7876220/3836120/48404 |

API setup: [`references/api-setup.md`](plugins/novel-to-manga-anime-generator/skills/novel-to-manga-anime-generator/references/api-setup.md)

> The links above are affiliate links. Using them supports this project at no extra cost to you.

## Copyright

⚠️ If you don't hold the rights to the original work, do not use the result commercially.

## License

[MIT](LICENSE)
