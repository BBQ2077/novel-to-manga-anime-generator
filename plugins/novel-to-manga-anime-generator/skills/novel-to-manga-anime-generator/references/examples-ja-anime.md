# 作例（アニメ）：『竹取物語』月への帰還 → 3 分アニメ（パブリックドメイン）

ユーザーが終盤「月の使者が迎えに来る」場面の現代語訳を貼り付け、3 分・16:9・日本語台詞のアニメにしたいと依頼します。

あらすじ：八月十五夜、帝は二千人の兵を翁の家に送って姫を守らせる。真夜中、満月の十倍もの光とともに天人が雲に乗って降りてくると、兵たちは戦う気力を失う。姫は帝に手紙と不死の薬を残し、天の羽衣を着せられると地上の思いを忘れて月へ昇っていく。

**画風アンカー**（全編固定）
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field.
```

---

## 第1回：① REF ＋ ② 構成案

### REF 一覧

| 種類 | ファイル | 備考 |
|---|---|---|
| 人物 | char_kaguya_juni.png | 正面全身 1 枚・白背景（十二単） |
| 人物 | char_kaguya_hagoromo.png | 天の羽衣を着た後の姿（衣装違い＝別 REF、顔・髪は同じ） |
| 人物 | char_okina_formal.png | 屋敷の主になった翁の正装 |
| 人物 | char_tennin.png | 天人の長（月の使者） |
| 人物 | char_soldier.png | 帝の兵（量産用の 1 体） |
| 場所 | loc_okina_mansion_night.png | 屋敷の庭と屋根、夜 |
| 小道具 | prop_hagoromo.png | 天の羽衣（人物 REF に描き込まない） |

**char_kaguya_juni**
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting. Full body character portrait of KAGUYA: graceful young noblewoman around 17, pale luminous skin, gentle almond eyes, floor-length straight black hair, layered Heian-era junihitoe robes in moon-white, lavender and pale gold. Standing upright facing the camera, whole body visible from head to the hem of the robes, calm and sorrowful expression. Plain clean white background, even lighting, no text, no watermark.
```

### 構成案（3 分）

| 時間 | 内容 |
|---|---|
| 0:00–0:30 | **冒頭の引き**：満月の下、屋根の上にずらりと並ぶ弓を構えた兵たち。誰もが空を見上げて息を殺している。 |
| 0:30–1:10 | 屋敷の奥、姫が翁と媼に別れを告げる。翁は泣きながら姫を抱きしめる。 |
| 1:10–2:20 | **クライマックス**（70 秒、全体の約 4 割）：真夜中、空が昼のように白く輝き、雲に乗った天人たちが降りてくる。兵の手から力が抜け、弓が落ちる。閉ざした戸がひとりでに開く。 |
| 2:20–2:45 | 姫が帝への手紙と不死の薬を託す。天人が羽衣を着せかけると、姫の目から涙が消える。 |
| 2:45–3:00 | 姫が雲に乗って月へ昇っていく。地上で見上げる翁の後ろ姿。 |

**音声方針**：ナレーションなし、日本語台詞。話者は姫・翁・天人の長。姫の長い別れの言葉は声と画を分離して処理します（翁の泣き顔に声を重ねる）。

---

## 第2回：③ 分ごとの細綱（抜粋 1:10–2:20）

```
### 1:10–2:20
【真夜中（子の刻）・翁の屋敷の庭と屋根・無風、満月】
内容：空が満月の十倍の明るさで白く輝き、庭の砂利の一粒一粒まで照らし出される。
雲に乗った天人たちが、地面から五尺ほどの高さまでゆっくり降りてくる。
屋根の兵たちは弓を引こうとするが、腕に力が入らず、手から弓が滑り落ちる。
固く閉ざした塗籠の戸と格子が、誰も触れていないのにひとりでに開いていく。
天人の長が雲の上から翁に呼びかける。
【見どころ】
1. 夜が昼に変わる瞬間の白い光（全体の色が一変する）
2. 雲に乗って降りてくる天人たちの群れ（大場面）
3. 兵の手から滑り落ちる弓のアップ
4. ひとりでに開く戸
5. 天人の長の静かな威圧感
【台詞／音声】
- 天人の長（画面内・短句）：「迎えに参った」——目的：圧倒的な存在感
- 翁（画面内・短句）：「渡さぬ！」——目的：抵抗
- 天人の長（画面外・長句）：「汝、幼き人。いささかなる功徳を翁つくりけるによりて……」——目的：経緯の説明（声と画を分離）
```

---

## 第3回：④ Context ＋ ⑤ キーフレーム ＋ Seedance プロンプト（連続する 12 秒×2 カット）

### カット 09

**【つなぎ】** 連続
**【0 秒目】** 真夜中。屋敷の瓦屋根の上に兵が 5 人、画面左を向いて並び、弓を構えて夜空を見上げている。空は暗く、満月だけが明るい。
**【主な出来事】** 空が急速に白く輝き始め、雲に乗った天人たちが画面右上からゆっくり降りてくる。兵たちは目を細め、腕が震える。
**【最後の 1 秒】** 空は昼のように白く、天人の雲が屋根の高さまで降りている。兵たちは同じ位置で、弓を構えたまま震えている。
**【REF】** char_soldier、char_tennin、loc_okina_mansion_night

**⑤ キーフレーム（0 秒目）**
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting. Wide shot, low angle. Use image 1 for the soldiers' armor and look, image 2 for the location. On the tiled roof of a Heian-era mansion, exactly five soldiers in Heian armor stand in a row facing left, bows drawn, looking up at the night sky. A bright full moon in a dark sky, faint clouds. No text. Aspect ratio 16:9.
```

**⑥ Seedance プロンプト**（i2v：キーフレームを先頭フレームとしてアップロード。動きだけを書く）
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field. [Midnight · tiled roof of a Heian-era mansion · windless, full moon]
The camera frames the five soldiers on the roof in a wide shot from a low angle.
0–4 s: The night sky begins to glow white from the upper right, the light spreading fast until every roof tile is sharply lit; the five soldiers, still facing left, squint and raise their arms against the glare.
4–9 s: The camera slowly tilts up; a mass of luminous white clouds carrying robed celestial figures descends gently from the upper right toward the roof.
9–12 s: The camera returns to the soldiers in a medium shot; still in the same row facing left, their drawn bows tremble violently in their hands. Exactly five soldiers throughout.
<a deep resonant hum rising> <bowstrings creaking> (a high choir enters softly)
```

### カット 10（連結：先頭フレーム = カット 09 の最終フレーム）

**【つなぎ】** 連続
**【0 秒目】** = カット 09 の最後の 1 秒
**【主な出来事】** 兵たちの腕から力が抜け、弓が次々と手から滑り落ちて瓦の上を転がる。雲の上の天人の長が静かに口を開く。
**【最後の 1 秒】** 兵たちは膝をつき、弓は屋根の上に散らばっている。雲は屋根の高さに留まっている。
**【REF】** なし（先頭フレームがすべてを引き継ぐ）

**⑥ Seedance プロンプト**（i2v、`first_frame_from: s09`）
```
Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field. [Midnight turned bright as day · tiled roof of a Heian-era mansion · windless]
The camera frames the soldiers in a medium shot.
0–5 s: The soldiers, facing left, go limp one after another; their bows slip from their fingers and clatter down the roof tiles.
5–8 s: The camera holds on a close-up of an empty, trembling hand.
8–12 s: The camera pulls out to a wide shot; the five soldiers have sunk to their knees, bows scattered on the tiles, while the glowing cloud hovers level with the roof. The celestial leader on the cloud speaks at second 10–11.
Dialogue language: Japanese, calm, distant and commanding. {迎えに参った}
<bows clattering on tiles> (the choir swells)
```

---

## ⑦ API モード：anime_plan.json（抜粋）

```json
{
  "lang": "ja",
  "style_anchor": "Japanese anime film style, theatrical-quality animation, clean fine line art, cel shading, layered lighting, natural hair and cloth motion, cinematic color grading, shallow depth of field.",
  "duration": 12, "ratio": "16:9", "generate_audio": true,
  "refs": [
    {"id": "char_soldier", "prompt": "Full body character portrait of a Heian-era soldier ..."},
    {"id": "char_tennin", "prompt": "Full body character portrait of a celestial envoy ..."},
    {"id": "loc_okina_mansion_night", "prompt": "Environment concept art of a Heian-era mansion at night ..."}
  ],
  "shots": [
    {"id": "s09", "mode": "i2v",
     "keyframe_refs": ["char_soldier", "loc_okina_mansion_night"],
     "keyframe_prompt": "Wide shot, low angle. Use image 1 for the soldiers' armor and look, image 2 for the location. ...",
     "video_prompt": "[Midnight · tiled roof of a Heian-era mansion · windless, full moon]\nThe camera frames the five soldiers on the roof in a wide shot from a low angle.\n0–4 s: ..."},
    {"id": "s10", "mode": "i2v", "first_frame_from": "s09",
     "video_prompt": "[Midnight turned bright as day · tiled roof · windless]\nThe camera frames the soldiers in a medium shot.\n0–5 s: ..."}
  ]
}
```
```bash
python scripts/run_anime.py anime_plan.json --check              # チェックと見積もり（無料）
python scripts/run_anime.py anime_plan.json --stage refs         # REF を生成して確認
python scripts/run_anime.py anime_plan.json --stage keyframes    # キーフレームを生成して確認
python scripts/run_anime.py anime_plan.json --stage videos       # 動画を送信・ダウンロード
python scripts/run_anime.py anime_plan.json --concat             # final.mp4 に結合
```

## 生成前チェック（カット 09〜10）

- [x] カット 09 のキーフレームは REF 2 枚（アップロード順どおり）、カット 10 は連結なので REF なし
- [x] カット 09 の最後の 1 秒 = カット 10 の 0 秒目（兵の位置・向き・光）
- [x] すべての区間で兵の向き（画面左）を明記
- [x] 兵の人数を「5 人」と明記し、モデルに任せていない
- [x] 固有名詞を言い換え済み（天人 → robed celestial figures、羽衣は未登場）
- [x] 動画内に読める文字を要求していない
- [x] 天人の長の長い口上は次のカットで声と画を分離（翁の顔のアップに声を重ねる）

## 生成量の見積もり（3 分 = 15 カット × 12 秒）

- REF：人物 5（羽衣後の姫を含む）＋場所 1＋小道具 1 ＝ 7 枚（作り直し込みで約 10 枚）
- キーフレーム：約 10 枚（5 カットは連結）× 1.5 ≈ 15 枚
- 動画：180 秒 × 1.5〜2 ≈ 270〜360 秒

> 👉 **おすすめ：BytePlus Lumina のサブスクリプション** — 月額固定、ブラウザでそのまま生成でき、普段使いならいちばんお得です → https://byteplus.pxf.io/vDqjnd
> 🤖 AI エージェントに全自動で大量生成させたい場合：**BytePlus ModelArk API**（従量課金）→ https://byteplus.pxf.io/c/7876220/3836120/48404
> （アフィリエイトリンク）
>
> ⚠️ 原作の権利を取得していない場合、商用利用はしないでください。
