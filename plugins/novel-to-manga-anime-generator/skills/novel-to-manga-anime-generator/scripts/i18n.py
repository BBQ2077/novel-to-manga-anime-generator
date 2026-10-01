"""User-facing messages in zh / en / ja.

The language comes from the plan's "lang" field ("zh", "en" or "ja"),
or the SKILL_LANG environment variable, defaulting to English.
"""

import os

LANG = os.environ.get("SKILL_LANG", "en")


def set_lang(lang):
    global LANG
    if lang:
        lang = lang.lower()
        LANG = "zh" if lang.startswith("zh") else "ja" if lang.startswith("ja") else "en"

MESSAGES = {
    # ---- ark.py ----
    "no_key": {
        "zh": "沒有設定 ARK_API_KEY。請到 ModelArk 控制台建立 API Key，並設成環境變數。",
        "en": "ARK_API_KEY is not set. Create an API key in the ModelArk console and set it as an environment variable.",
        "ja": "ARK_API_KEY が設定されていません。ModelArk コンソールで API キーを作成し、環境変数に設定してください。",
    },
    "http_error": {"zh": "HTTP {code} {path}：{detail}", "en": "HTTP {code} {path}: {detail}", "ja": "HTTP {code} {path}：{detail}"},
    "conn_error": {"zh": "連線失敗 {url}：{reason}", "en": "Connection failed {url}: {reason}", "ja": "接続に失敗しました {url}：{reason}"},
    "no_image": {"zh": "沒有回傳圖片：{resp}", "en": "No image returned: {resp}", "ja": "画像が返されませんでした：{resp}"},
    "bad_format": {"zh": "回傳格式無法辨識：{resp}", "en": "Unrecognized response format: {resp}", "ja": "レスポンス形式を認識できません：{resp}"},
    "mixed_modes": {
        "zh": "首尾幀模式和參考圖模式不要混用，請擇一。",
        "en": "First/last-frame mode and reference-image mode cannot be mixed. Pick one.",
        "ja": "先頭・末尾フレームモードと参照画像モードは併用できません。どちらかを選んでください。",
    },
    "no_task_id": {"zh": "沒有回傳 task id：{resp}", "en": "No task id returned: {resp}", "ja": "task id が返されませんでした：{resp}"},
    "no_video_url": {"zh": "任務成功但沒有 video_url：{resp}", "en": "Task succeeded but has no video_url: {resp}", "ja": "タスクは成功しましたが video_url がありません：{resp}"},
    "task_failed": {"zh": "任務 {tid} {status}：{error}", "en": "Task {tid} {status}: {error}", "ja": "タスク {tid} {status}：{error}"},
    "task_timeout": {"zh": "任務 {tid} 等待逾時（最後狀態：{status}）", "en": "Task {tid} timed out (last status: {status})", "ja": "タスク {tid} がタイムアウトしました（最終ステータス：{status}）"},

    # ---- shared runner ----
    "check_failed": {"zh": "❌ 生成前檢查沒有通過：", "en": "❌ Pre-generation check failed:", "ja": "❌ 生成前チェックに失敗しました："},
    "key_missing_run": {
        "zh": "❌ 沒有設定 ARK_API_KEY。請依 references/api-setup.md 開通 ModelArk 並設定 API Key。",
        "en": "❌ ARK_API_KEY is not set. Follow references/api-setup.md to activate ModelArk and set your API key.",
        "ja": "❌ ARK_API_KEY が設定されていません。references/api-setup.md に従って ModelArk を有効化し、API キーを設定してください。",
    },
    "err_style": {"zh": "缺少 style_anchor（畫風錨點）", "en": "Missing style_anchor", "ja": "style_anchor（画風アンカー）がありません"},
    "err_ref_src": {"zh": "REF {id}：需要 prompt 或 file 其中之一", "en": "REF {id}: needs either prompt or file", "ja": "REF {id}：prompt か file のどちらかが必要です"},
    "err_ref_file": {"zh": "REF {id}：找不到檔案 {file}", "en": "REF {id}: file not found {file}", "ja": "REF {id}：ファイルが見つかりません {file}"},
    "running_ref": {"zh": "→ REF {id}", "en": "→ REF {id}", "ja": "→ REF {id}"},
    "item_failed": {"zh": "  ✗ {err}", "en": "  ✗ {err}", "ja": "  ✗ {err}"},
    "preview": {"zh": "預覽：{path}", "en": "Preview: {path}", "ja": "プレビュー：{path}"},
    "n_failed": {"zh": "\n有 {n} 項失敗：{ids}", "en": "\n{n} item(s) failed: {ids}", "ja": "\n{n} 件が失敗しました：{ids}"},

    # ---- run_comic.py ----
    "err_panel_dup": {"zh": "格 {id}：id 重複", "en": "Panel {id}: duplicate id", "ja": "コマ {id}：id が重複しています"},
    "err_panel_prompt": {"zh": "格 {id}：缺少 prompt", "en": "Panel {id}: missing prompt", "ja": "コマ {id}：prompt がありません"},
    "err_panel_ref_missing": {"zh": "格 {id}：REF 不存在 {refs}", "en": "Panel {id}: unknown REF {refs}", "ja": "コマ {id}：存在しない REF {refs}"},
    "err_panel_ref_count": {"zh": "格 {id}：REF {n} 張，超過上限 {max}", "en": "Panel {id}: {n} REFs exceeds the limit of {max}", "ja": "コマ {id}：REF {n} 枚は上限 {max} 枚を超えています"},
    "err_panel_image_idx": {
        "zh": "格 {id}：prompt 引用 image {idx}，但只放了 {n} 張 REF",
        "en": "Panel {id}: prompt references image {idx} but only {n} REF(s) are attached",
        "ja": "コマ {id}：prompt が image {idx} を参照していますが、REF は {n} 枚しかありません",
    },
    "err_page_panel": {"zh": "頁 {id}：版型引用不存在的格 {panel}", "en": "Page {id}: layout references unknown panel {panel}", "ja": "ページ {id}：レイアウトが存在しないコマ {panel} を参照しています"},
    "comic_ok": {
        "zh": "✅ 檢查通過。這次要生成：REF {refs} 張、格子 {panels} 張，共 {total} 次 Seedream 呼叫（模型：{model}）",
        "en": "✅ Check passed. To generate: {refs} REF(s), {panels} panel(s) — {total} Seedream call(s) (model: {model})",
        "ja": "✅ チェック通過。今回の生成：REF {refs} 枚、コマ {panels} 枚、Seedream 呼び出し計 {total} 回（モデル：{model}）",
    },
    "running_panel": {"zh": "→ 格 {id}（REF {n} 張）", "en": "→ Panel {id} ({n} REF(s))", "ja": "→ コマ {id}（REF {n} 枚）"},
    "panel_ref_absent": {"zh": "✗ 格 {id}：REF 還沒生成 {paths}，跳過", "en": "✗ Panel {id}: REF not generated yet {paths}, skipped", "ja": "✗ コマ {id}：REF が未生成です {paths}、スキップします"},
    "comic_retry": {"zh": "修正後用 --only <id> 重跑。", "en": "Fix the issue and re-run with --only <id>.", "ja": "修正後、--only <id> で再実行してください。"},
    "comic_done": {"zh": "\n全部完成。", "en": "\nAll done.", "ja": "\nすべて完了しました。"},
    "preview_title": {"zh": "漫畫預覽", "en": "Comic preview", "ja": "漫画プレビュー"},

    # ---- run_anime.py ----
    "err_shot_dup": {"zh": "鏡 {id}：id 重複", "en": "Shot {id}: duplicate id", "ja": "カット {id}：id が重複しています"},
    "err_shot_mode": {"zh": "鏡 {id}：mode 只能是 i2v 或 r2v", "en": "Shot {id}: mode must be i2v or r2v", "ja": "カット {id}：mode は i2v か r2v のみです"},
    "err_shot_vprompt": {"zh": "鏡 {id}：缺少 video_prompt", "en": "Shot {id}: missing video_prompt", "ja": "カット {id}：video_prompt がありません"},
    "err_shot_duration": {"zh": "鏡 {id}：duration {d} 超出 4–30 秒", "en": "Shot {id}: duration {d} is outside 4–30 s", "ja": "カット {id}：duration {d} は 4〜30 秒の範囲外です"},
    "err_chain_mode": {"zh": "鏡 {id}：first_frame_from 只能用在 i2v 模式", "en": "Shot {id}: first_frame_from only works in i2v mode", "ja": "カット {id}：first_frame_from は i2v モードでのみ使えます"},
    "err_chain_order": {
        "zh": "鏡 {id}：first_frame_from 必須指向排在前面的鏡頭（{src}）",
        "en": "Shot {id}: first_frame_from must point to an earlier shot ({src})",
        "ja": "カット {id}：first_frame_from は前のカットを指定してください（{src}）",
    },
    "err_i2v_atimage": {
        "zh": "鏡 {id}：i2v 模式的 video_prompt 不應使用 @Image（只有首幀）",
        "en": "Shot {id}: i2v video_prompt must not use @Image (only the first frame is sent)",
        "ja": "カット {id}：i2v モードの video_prompt では @Image を使わないでください（先頭フレームのみ送信）",
    },
    "err_i2v_keyframe": {
        "zh": "鏡 {id}：i2v 模式需要 keyframe_prompt 或 keyframe_file",
        "en": "Shot {id}: i2v mode needs keyframe_prompt or keyframe_file",
        "ja": "カット {id}：i2v モードには keyframe_prompt か keyframe_file が必要です",
    },
    "err_kf_ref_count": {"zh": "鏡 {id}：關鍵畫面 REF 超過 {max} 張", "en": "Shot {id}: keyframe REFs exceed {max}", "ja": "カット {id}：キーフレーム REF が {max} 枚を超えています"},
    "err_kf_ref_missing": {"zh": "鏡 {id}：關鍵畫面 REF 不存在 {refs}", "en": "Shot {id}: unknown keyframe REF {refs}", "ja": "カット {id}：存在しないキーフレーム REF {refs}"},
    "err_kf_image_idx": {
        "zh": "鏡 {id}：關鍵畫面 prompt 引用第 {idx} 張圖，但只放了 {n} 張",
        "en": "Shot {id}: keyframe prompt references image {idx} but only {n} are attached",
        "ja": "カット {id}：キーフレーム prompt が {idx} 枚目の画像を参照していますが、{n} 枚しかありません",
    },
    "err_vref_count": {"zh": "鏡 {id}：影片 REF {n} 張，超過建議上限 {max}", "en": "Shot {id}: {n} video REFs exceeds the recommended {max}", "ja": "カット {id}：動画 REF {n} 枚は推奨上限 {max} 枚を超えています"},
    "err_vref_missing": {"zh": "鏡 {id}：影片 REF 不存在 {refs}", "en": "Shot {id}: unknown video REF {refs}", "ja": "カット {id}：存在しない動画 REF {refs}"},
    "err_vref_idx": {
        "zh": "鏡 {id}：video_prompt 引用 @Image{idx}，但只放了 {n} 張",
        "en": "Shot {id}: video_prompt references @Image{idx} but only {n} are attached",
        "ja": "カット {id}：video_prompt が @Image{idx} を参照していますが、{n} 枚しかありません",
    },
    "err_mixed_duration": {
        "zh": "每鏡秒數不一致 {ds}；如果是刻意的，在 plan 加上 allow_mixed_duration: true",
        "en": "Shot durations differ {ds}; if intentional, add allow_mixed_duration: true to the plan",
        "ja": "カットの秒数が不揃いです {ds}。意図的なら plan に allow_mixed_duration: true を追加してください",
    },
    "anime_ok": {
        "zh": "✅ 檢查通過。這次要生成：REF {refs} 張、關鍵畫面 {kf} 張（Seedream：{imodel}）、影片 {vids} 段共 {secs} 秒（Seedance：{vmodel}）",
        "en": "✅ Check passed. To generate: {refs} REF(s), {kf} keyframe(s) (Seedream: {imodel}), {vids} video(s), {secs} s total (Seedance: {vmodel})",
        "ja": "✅ チェック通過。今回の生成：REF {refs} 枚、キーフレーム {kf} 枚（Seedream：{imodel}）、動画 {vids} 本・計 {secs} 秒（Seedance：{vmodel}）",
    },
    "shot_ref_absent": {"zh": "✗ 鏡 {id}：REF 還沒生成 {paths}，跳過", "en": "✗ Shot {id}: REF not generated yet {paths}, skipped", "ja": "✗ カット {id}：REF が未生成です {paths}、スキップします"},
    "running_kf": {"zh": "→ 關鍵畫面 {id}", "en": "→ Keyframe {id}", "ja": "→ キーフレーム {id}"},
    "waiting": {"zh": "… 等待 {id}（{tid}）", "en": "… Waiting for {id} ({tid})", "ja": "… 待機中 {id}（{tid}）"},
    "no_lastframe": {
        "zh": "  ⚠ {id} 沒有回傳最後一格，接在它後面的鏡頭無法串接",
        "en": "  ⚠ {id} returned no last frame; the shot chained after it cannot start",
        "ja": "  ⚠ {id} の最終フレームが返されなかったため、後続のカットをつなげられません",
    },
    "no_first_frame": {
        "zh": "✗ 鏡 {id}：首幀還沒有（關鍵畫面未生成，或前一鏡沒有回傳最後一格），跳過",
        "en": "✗ Shot {id}: no first frame yet (keyframe not generated, or the previous shot returned no last frame), skipped",
        "ja": "✗ カット {id}：先頭フレームがありません（キーフレーム未生成、または前カットの最終フレームなし）、スキップします",
    },
    "submitted": {"zh": "→ 已送出 {id}：{tid}", "en": "→ Submitted {id}: {tid}", "ja": "→ 送信しました {id}：{tid}"},
    "anime_retry": {
        "zh": "依「Context → REF → Prompt → 生成結果」的順序找原因，修正後用 --only <id> 重跑。",
        "en": "Trace the cause in order Context → REF → Prompt → generated result, then re-run with --only <id>.",
        "ja": "「Context → REF → Prompt → 生成結果」の順に原因を調べ、修正後 --only <id> で再実行してください。",
    },
    "anime_done": {
        "zh": "\n全部完成。下一步：檢查每段影片，然後用 --concat 串接或匯入剪輯軟體。",
        "en": "\nAll done. Next: review each clip, then join them with --concat or import them into your editor.",
        "ja": "\nすべて完了しました。次は各動画を確認し、--concat で結合するか編集ソフトに読み込んでください。",
    },
    "no_ffmpeg": {
        "zh": "找不到 ffmpeg，請改用剪映／CapCut 手動串接 videos/ 裡的檔案。",
        "en": "ffmpeg not found. Join the files in videos/ manually with CapCut or another editor.",
        "ja": "ffmpeg が見つかりません。videos/ 内のファイルを CapCut などの編集ソフトで手動結合してください。",
    },
    "videos_missing": {"zh": "還有影片沒生成：{files}", "en": "Some videos are not generated yet: {files}", "ja": "未生成の動画があります：{files}"},
    "concat_done": {"zh": "完成：{path}", "en": "Done: {path}", "ja": "完了：{path}"},
}


def t(key, **kw):
    msg = MESSAGES[key]
    text = msg.get(LANG) or msg["en"]
    return text.format(**kw) if kw else text
