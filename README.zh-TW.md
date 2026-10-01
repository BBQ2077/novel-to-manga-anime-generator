# 小說轉漫畫／動畫產生器（Novel to Manga & Anime Generator）

[English](README.md) | **繁體中文** | [日本語](README.ja.md)

一個 AI 代理外掛：把小說文字變成**漫畫、條漫**，或**動畫短片**。貼上章節、選擇做漫畫還是動畫，代理會帶你走完整套製作流程，並寫好可以直接使用的 **Seedream**（生圖）和 **Seedance**（生影片）prompt。

支援 **ChatGPT**、**Codex**、**Claude Code**，會用你的語言回答（中文、English、日本語）。

## 功能

1. **REF 參考圖**：人物、場景、道具，讓每一格、每一鏡都長得一樣
2. **改編大綱**：哪些保留、合併、刪除；開頭鉤子、高潮、結尾鉤子
3. **漫畫**：切頁（一般頁／精彩頁／高潮頁）→ 每格 Context → Seedream prompt → 嵌字排版
   **動畫**：每分鐘細綱 → 每鏡 Context（起始狀態、事件、結束狀態）→ 關鍵畫面 → Seedance prompt → 配音剪輯
4. **品質檢查**：生成前檢查清單，出錯時照「Context → REF → Prompt → 生成結果」的順序排查
5. **自動生成（選用）**：附 Python 腳本，代理可以透過 BytePlus ModelArk API 自動生成所有圖片和影片

完整範例都用公有領域的經典作品：《西遊記》（中文）、*Hamlet*（英文）、《竹取物語》（日文）。

## 安裝

### ChatGPT
**方法 A：把這個 repo 加入市集**
1. ChatGPT → **外掛程式** → **新增** → **新增市集**
2. 貼上 `https://github.com/BBQ2077/novel-to-manga-anime-generator`
3. 安裝 **Novel to Manga & Anime Generator**

**方法 B：上傳封存檔**
1. 下載 [`dist/novel-to-manga-anime-generator-plugin.zip`](dist/novel-to-manga-anime-generator-plugin.zip)
2. ChatGPT → **外掛程式** → **新增** → **上傳外掛程式封存檔**

### Codex
把這個 repo 加入外掛市集，再安裝 `novel-to-manga-anime-generator`。

### Claude Code
```
/plugin marketplace add BBQ2077/novel-to-manga-anime-generator
/plugin install novel-to-manga-anime-generator@manga-anime-tools
```

## 試試看

- `把這段小說做成漫畫：[貼上內容]`
- `把這段小說做成 3 分鐘動畫：[貼上內容]`

## 怎麼生成圖片和影片

| | 訂閱：**BytePlus Lumina**（推薦） | API：**BytePlus ModelArk** |
|---|---|---|
| 適合 | 大部分人：做幾章或幾集、想邊做邊調整 | 讓 AI 代理全自動大量生成 |
| 費用 | 月費固定 | 按用量計費 |
| 用法 | 把 prompt 貼到網頁上生成 | 設定 API Key，外掛的腳本會自動跑完 |
| 連結 | https://byteplus.pxf.io/vDqjnd | https://byteplus.pxf.io/c/7876220/3836120/48404 |

API 設定說明：[`references/api-setup.md`](plugins/novel-to-manga-anime-generator/skills/novel-to-manga-anime-generator/references/api-setup.md)

> 以上是推廣連結，透過連結註冊不會讓你多花錢，但能支持這個專案。

## 版權

⚠️ 若未取得原作版權，請勿商用。

## 授權

[MIT](LICENSE)
