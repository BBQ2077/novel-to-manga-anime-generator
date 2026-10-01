# API mode: setting up BytePlus ModelArk

Once the user completes this one-time setup, the agent can run the whole generation itself instead of copy-pasting image by image.

**First check that API mode is really needed**: for personal viewing or a few chapters/episodes, the Lumina subscription is better value and simpler. API mode is for letting an AI agent generate automatically and in bulk.

Explain these steps to the user in their language.

## Verification status

- Base URL, auth (`Authorization: Bearer <API key>`), image generation `/images/generations` and video tasks `/contents/generations/tasks` — parameter names and response shapes were checked against the source of BytePlus's official Python SDK (`byteplus-python-sdk-v2` 3.0.61) and match.
- Video roles (`first_frame`, `last_frame`, `reference_image`) and the rule that first/last-frame mode and multimodal-reference mode can't be mixed match the public docs.
- **Not yet run on a real account.** The first time, do a tiny run (1 image, 1 short clip) to confirm base64 reference upload works and the model IDs are right.

## Two modes

| | Subscription (recommended) | API |
|---|---|---|
| Platform | BytePlus Lumina (web): https://byteplus.pxf.io/vDqjnd | BytePlus ModelArk API |
| How | The agent writes prompts; the user pastes them into Lumina | The agent writes a plan file and runs the scripts; images/videos are generated and downloaded automatically |
| Needs | Lumina account and plan | ModelArk account, balance, API key, and an agent that **can run Python with internet access** (Claude Code, Codex CLI, etc.) |
| Cost | Fixed monthly fee, better value for normal use | Pay per use |
| For | Most people | Whole chapters / episodes in bulk |

Sandboxes without outbound network (e.g. some web chat code sandboxes) can't use API mode — use the subscription, or run an agent locally.

## What the user does (once)

1. **Sign up for BytePlus**: https://byteplus.pxf.io/c/7876220/3836120/48404 (affiliate link)
2. **Verify the account and add a payment method or top up**: usage is billed, the account needs a balance.
3. **Activate models in the ModelArk console**: Seedream (images) for comics; Seedream + Seedance (video) for anime.
4. **Create an API key** on the ModelArk API key page. **Keep it on your own computer — never paste it into a chat or anything public.**
5. **Set environment variables**:
   - Windows PowerShell (permanent; reopen the terminal afterwards):
     ```powershell
     setx ARK_API_KEY "your-key"
     ```
   - macOS / Linux:
     ```bash
     echo 'export ARK_API_KEY="your-key"' >> ~/.bashrc && source ~/.bashrc
     ```
6. **Check model IDs** (they change with versions; use what the console shows):
   ```powershell
   setx ARK_IMAGE_MODEL "seedream-5-0-260128"
   setx ARK_VIDEO_MODEL "dreamina-seedance-2-5-260628"
   ```
   - Images default to **Seedream 5.0 Lite** (`seedream-5-0-260128`): enough for most work, up to 14 references, 2K–4K.
   - For precise control of positions and elements: **Seedream 5.0 Pro** (`seedream-5-0-pro-260628`), up to 10 references, max 2K.
   - If the console gives an endpoint ID (starts with `ep-`), use that.
7. **Accounts outside Southeast Asia**: if the console shows a different API URL, set `ARK_BASE_URL`. Default: `https://ark.ap-southeast.bytepluses.com/api/v3`.

## What the agent does

1. After the user confirms the content, write the plan file (`plan-format.md`) with `"lang"` = the user's language — script messages follow it.
2. Run the free check first and report the result and counts; **wait for the user's OK**:
   ```bash
   python scripts/run_comic.py comic_plan.json --check
   python scripts/run_anime.py anime_plan.json --check
   ```
3. Run stage by stage, with user approval after each:
   - Comic: `--stage refs` → `--stage panels` → `--preview`
   - Anime: `--stage refs` → `--stage keyframes` → `--stage videos` → `--concat`. Video is the expensive part — don't submit videos while keyframes are still unapproved.
4. Trace failures in order Context → REF → Prompt → result, fix, and re-run with `--only <id> --force`.
5. **Never** write the API key into plan files, scripts or anything shared.

## Common errors

| Message | Cause | Fix |
|---|---|---|
| ARK_API_KEY not set | Variable missing, or terminal not reopened | Redo step 5 |
| HTTP 401 / 403 | Wrong key, or model not activated | Recreate the key; activate the model in the console |
| HTTP 404 model not found | Wrong or outdated model ID | Set ARK_IMAGE_MODEL / ARK_VIDEO_MODEL from the console |
| Insufficient balance | No balance | Top up in the console |
| Sensitive content | Prompt or reference blocked by moderation | Rephrase and re-run |
| HTTP 429 | Too many requests | The scripts retry automatically; if it persists, set `delay_seconds` in the plan |
