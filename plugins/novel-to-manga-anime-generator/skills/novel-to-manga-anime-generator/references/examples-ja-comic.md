# 作例（漫画）：『竹取物語』冒頭（パブリックドメイン）

ユーザーが冒頭部分の現代語訳（約 2,000 字）を貼り付けます：竹取の翁が光る竹を見つける → 中に小さな女の子 → 翁と媼が育てる → 竹から黄金が出て家が栄える → 三か月で美しい娘に成長 → 「なよ竹のかぐや姫」と名付けられ、求婚者が集まる。

原文の書き出し（参考）：「今は昔、竹取の翁といふものありけり。野山にまじりて竹を取りつつ、よろづのことに使ひけり。」

形式：漫画、右→左。画風ロック：`traditional Japanese yamato-e scroll painting style, flat mineral pigments, gold leaf clouds, fine ink outlines`

---

## 第1回：① REF ＋ ② 構成案

### ① REF 一覧

| 種類 | 名前 | ファイル |
|---|---|---|
| 人物 | 竹取の翁 | char_okina.png |
| 人物 | 媼 | char_ouna.png |
| 人物 | かぐや姫（三寸の幼子） | char_kaguya_child.png |
| 人物 | かぐや姫（成長後・十二単） | char_kaguya_juni.png |
| 場所 | 竹林 | loc_bamboo_grove.png |
| 場所 | 翁の家（成長後に立派になった屋敷） | loc_okina_house.png |
| 小道具 | 光る竹 | prop_glowing_bamboo.png |

成長前と成長後のかぐや姫は**別の REF**（衣装も体格も変わるため）。

**翁：固定外見文字列**
```
OKINA: kind elderly bamboo cutter around 70, thin wiry build, sun-browned wrinkled face, white topknot and thin white beard, plain undyed hemp work robe tied with a rope belt, straw sandals, a bamboo-cutting hatchet at his waist
```

**翁：REF プロンプト**
```
Character reference sheet of OKINA: kind elderly bamboo cutter around 70, thin wiry build, sun-browned wrinkled face, white topknot and thin white beard, plain undyed hemp work robe tied with a rope belt, straw sandals, a bamboo-cutting hatchet at his waist. Traditional Japanese yamato-e scroll painting style, flat mineral pigments, fine ink outlines. Front view, three-quarter view, side view and back view standing in a row, full body, plus a row of expressions: neutral, surprised, joyful, tearful, worried. Plain white background, no text.
```

**かぐや姫（成長後）：固定外見文字列**
```
KAGUYA: graceful young noblewoman around 17, pale luminous skin, gentle almond eyes, floor-length straight black hair, layered Heian-era junihitoe robes in moon-white, lavender and pale gold, a folding fan in hand
```
［補］原文は「この子のかたちけうらなること世になく」程度で具体的な外見描写が少ないため、色や衣装は補足しています。

**光る竹：小道具 REF プロンプト**
```
Prop reference sheet of a single tall green bamboo stalk whose lower section glows from within with soft golden light, light leaking through the node seams, traditional Japanese yamato-e scroll painting style, flat mineral pigments, fine ink outlines. Shown full length, as a close-up of the glowing section, and next to a person for scale. Plain white background, no text.
```

（媼・幼いかぐや姫・竹林・屋敷も同じ形式で作成。）

### ② 構成案

- **範囲**：約 2,000 字 → 5 ページ
- **出来事**：翁の紹介（残す）→ 光る竹の発見（拡大）→ **竹の中の小さな姫**（クライマックス）→ 家で育てる・黄金の竹（残す、まとめる）→ 三か月で成長・命名（残す）→ 求婚者が集まる（次章への引き）
- **冒頭の引き**：1 ページ目の最後のコマ、竹林の奥で一本だけ光る竹（正体は見せない）
- **クライマックス**：光る筒の中に座る三寸ほどの姫 → 3 ページ目、1 コマ全面
- **ラストの引き**：屋敷の門前に集まる貴公子たちの影
- **心理描写の変換**：「あやしがりて」→ 翁が目をこすり、斧を持つ手が止まる

---

## 第2回：③ ページ割り

| ページ | 原文範囲 | 字数 | 種類 | ポイント | ページ末の引き |
|---|---|---|---|---|---|
| 1 | 「今は昔」〜竹を取って暮らす翁 | 約 450 | 通常・5 コマ | 翁の暮らし、竹林 | 奥で光る一本の竹 |
| 2 | 光る竹に近づく〜「筒の中光りたり」 | 約 300 | **見せ場・3 コマ** | 光の正体へ迫る | 斧を振り上げる翁 |
| 3 | 「三寸ばかりなる人、いとうつくしうてゐたり」 | 約 150 | **クライマックス・1 コマ** | 小さな姫の発見 | — |
| 4 | 家に連れ帰る〜黄金の入った竹〜家が豊かになる | 約 600 | 通常・6 コマ | 育てる日々 | 驚くほど早く大きくなる姫 |
| 5 | 三か月で成人〜命名の宴〜求婚者 | 約 500 | 通常・5 コマ | 美しく成長、名付け | 門前に集まる貴公子たち |

2 ページ目（左ページ）の最後で翁が光る竹に手をかけ、ページをめくると 3 ページ目の 1 コマ全面で姫が現れます。

**2 ページ目の詳細**
```
### 2 ページ目【見せ場・3 コマ】
原文：光る竹に気づいて近寄るところから「筒の中光りたり」まで（約 300 字）
【竹林・夕暮れ・木漏れ日が消え、竹の光だけが目立つ】
内容：翁が不思議に思って近づき、根元の筒が内側から光っているのを見つけ、そっと斧を当てる。
【見どころ】1. 薄暗い竹林で一本だけ光る竹  2. 光に照らされた翁の驚いた顔  3. 節の継ぎ目から漏れる金色の光
【台詞】翁：「……なんと、竹が光っておる」
【ページ末の引き】竹に斧を当てる翁の手（めくると中身が分かる）
```

---

## 第3回：④ コマ Context ＋ ⑤ プロンプト（2・3 ページ目）

### 2 ページ目（見せ場・3 コマ）

| コマ | 大きさ | 景別／アングル | 瞬間 | 文字 | REF |
|---|---|---|---|---|---|
| 1 | 小 | ロング・俯瞰 | 薄暗い竹林、奥で一本だけ光る竹へ翁が歩み寄る | — | 翁、竹林、光る竹 |
| 2 | 小 | アップ | 金色の光に照らされた翁の驚いた顔 | 翁：「……なんと、竹が光っておる」 | 翁 |
| 3 | **大（半ページ以上）** | クローズアップ | 節の継ぎ目から光が漏れる筒に、翁が斧をそっと当てる手元 | 描き文字「ぼう…」 | 翁、光る竹 |

**2 ページ目・3 コマ目：Context**
- 【コマ】p02_3、大、3:4
- 【瞬間】光る竹の根元の節。継ぎ目から金色の光が漏れ、翁のしわだらけの手が斧の刃を節の少し上にそっと当てている
- 【景別・アングル】クローズアップ、アイレベル
- 【文字】描き文字「ぼう…」を右上に
- 【REF】char_okina、prop_glowing_bamboo

**2 ページ目・3 コマ目：プロンプト**（アップロード：image 1 = char_okina、image 2 = prop_glowing_bamboo）
```
Traditional Japanese yamato-e scroll painting style, flat mineral pigments, gold leaf clouds, fine ink outlines. Close-up, eye level. Use image 1 for the old man's hands and sleeve, image 2 for the glowing bamboo. The base of a tall green bamboo stalk glows from within, golden light leaking through the seams of the node; an old man's wrinkled, sun-browned hand in an undyed hemp sleeve gently rests the blade of a small hatchet just above the node. Dim bamboo grove at dusk, the only light coming from the stalk. A soft sound effect "ぼう…" in thin brushed Japanese letters at the top right. Aspect ratio 3:4.
```

### 3 ページ目（クライマックス・1 コマ全面）

| コマ | 大きさ | 景別／アングル | 瞬間 | 文字 | REF |
|---|---|---|---|---|---|
| 1 | 全面 | フル・あおり気味 | 割れた竹の筒の中、金色の光に包まれて三寸ほどの美しい女の子が座っている。手前に腰を抜かした翁の後ろ姿 | 翁：「なんと……うつくしい」 | 翁、幼いかぐや姫、光る竹、竹林 |

**3 ページ目：プロンプト**（アップロード：image 1 = char_kaguya_child、image 2 = char_okina、image 3 = prop_glowing_bamboo、image 4 = loc_bamboo_grove）
```
Traditional Japanese yamato-e scroll painting style, flat mineral pigments, gold leaf clouds, fine ink outlines. Full-page splash, slightly low angle. Use image 1 for the tiny girl, image 2 for the old man, image 3 for the bamboo and image 4 for the location. Inside a freshly split section of a glowing bamboo stalk sits a tiny, exquisitely beautiful girl no taller than a hand's length, in miniature layered white robes, bathed in radiant golden light that spills out across the grove. In the foreground, seen from behind, the old bamboo cutter has fallen back onto the ground, his hatchet dropped beside him. Tall bamboo rising on both sides, gold-leaf clouds drifting at the top. One speech bubble near the old man containing the text "なんと……うつくしい" in vertical Japanese handwriting. Aspect ratio 2:3.
```

---

## ⑥ API モード：comic_plan.json（抜粋）

```json
{
  "lang": "ja",
  "style_anchor": "Traditional Japanese yamato-e scroll painting style, flat mineral pigments, gold leaf clouds, fine ink outlines.",
  "reading_direction": "rtl",
  "refs": [
    {"id": "char_okina", "prompt": "Character reference sheet of OKINA: ..."},
    {"id": "char_kaguya_child", "prompt": "Character reference sheet of a tiny girl ..."},
    {"id": "prop_glowing_bamboo", "prompt": "Prop reference sheet of a single tall green bamboo stalk ..."},
    {"id": "loc_bamboo_grove", "prompt": "Environment concept art of a dense bamboo grove at dusk ..."}
  ],
  "panels": [
    {"id": "p02_3", "refs": ["char_okina", "prop_glowing_bamboo"], "aspect": "3:4",
     "prompt": "Close-up, eye level. Use image 1 for the old man's hands and sleeve, image 2 for the glowing bamboo. ..."},
    {"id": "p03_1", "refs": ["char_kaguya_child", "char_okina", "prop_glowing_bamboo", "loc_bamboo_grove"], "aspect": "2:3",
     "prompt": "Full-page splash, slightly low angle. Use image 1 for the tiny girl, ..."}
  ],
  "pages": [
    {"id": "p03", "type": "クライマックス", "rows": [["p03_1"]]}
  ]
}
```
本番の plan にはすべてのコマを書きます。`pages` は `panels` にある id しか参照できません（存在しない id があると `--check` で止まります）。
```bash
python scripts/run_comic.py comic_plan.json --check          # チェックと枚数見積もり（無料）
python scripts/run_comic.py comic_plan.json --stage refs     # まず REF を生成して確認
python scripts/run_comic.py comic_plan.json --stage panels   # 全コマ生成＋ preview.html
```

## ⑦ 写植・チェック

- CLIP STUDIO PAINT か Canva で、2 ページ目は上段に小コマ 2 つ（右→左）、下段に大コマ 1 つを配置。台詞は縦書きの吹き出しで。
- チェック：翁の腰の斧が毎コマあるか、光る竹の光の色が 1〜3 ページで同じ金色か、幼い姫と成長後の姫の顔立ちがつながっているか。

## 生成枚数の見積もり

- REF：人物 4（成長前後のかぐや姫を含む）＋場所 2＋小道具 1 ＝ 7 枚（作り直し込みで約 10 枚）
- コマ：5 ページ 20 コマ × 1.5〜2 ≈ 30〜40 枚

> 👉 **おすすめ：BytePlus Lumina のサブスクリプション** — 月額固定、ブラウザでそのまま生成でき、普段使いならいちばんお得です → https://byteplus.pxf.io/vDqjnd
> 🤖 AI エージェントに全自動で大量生成させたい場合：**BytePlus ModelArk API**（従量課金）→ https://byteplus.pxf.io/c/7876220/3836120/48404
> （アフィリエイトリンク）
>
> ⚠️ 原作の権利を取得していない場合、商用利用はしないでください。
