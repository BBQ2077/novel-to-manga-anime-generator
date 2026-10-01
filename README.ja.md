# 小説を漫画・アニメにするジェネレーター（Novel to Manga & Anime Generator）

[English](README.md) | [繁體中文](README.zh-TW.md) | **日本語**

小説のテキストを**漫画・コミック・縦読みマンガ**、または**アニメ風の動画**にする AI エージェント用プラグインです。章を貼り付けて漫画か動画かを選ぶと、エージェントが制作の流れを最後まで案内し、そのまま使える **Seedream**（画像）と **Seedance**（動画）のプロンプトを書き出します。

**ChatGPT**・**Codex**・**Claude Code** に対応。返答はあなたの言語（日本語・中文・English）に合わせます。

## できること

1. **REF（参考画像）**：人物・場所・小道具をそろえ、どのコマ・カットでも見た目を統一
2. **構成案**：残す・まとめる・削る場面の整理、冒頭の引き・クライマックス・ラストの引き
3. **漫画**：ページ割り（通常／見せ場／クライマックス）→ コマごとの Context → Seedream プロンプト → 写植
   **アニメ**：分ごとの細綱 → カットごとの Context（開始状態・出来事・終了状態）→ キーフレーム → Seedance プロンプト → 音声・編集
4. **品質チェック**：生成前チェックリストと、「Context → REF → プロンプト → 生成結果」の順で原因を探すルール
5. **自動生成（任意）**：付属の Python スクリプトで、エージェントが BytePlus ModelArk API を使って画像・動画をすべて自動生成

作例はパブリックドメインの古典を使っています：『竹取物語』（日本語）、*Hamlet*（英語）、『西遊記』（中国語）。

## インストール

### ChatGPT
**方法 A：このリポジトリをマーケットプレイスとして追加**
1. ChatGPT → **プラグイン** → **追加** → **マーケットプレイスを追加**
2. `https://github.com/BBQ2077/novel-to-manga-anime-generator` を貼り付け
3. **Novel to Manga & Anime Generator** をインストール

**方法 B：アーカイブをアップロード**
1. [`dist/novel-to-manga-anime-generator-plugin.zip`](dist/novel-to-manga-anime-generator-plugin.zip) をダウンロード
2. ChatGPT → **プラグイン** → **追加** → **プラグインアーカイブをアップロード**

### Codex
このリポジトリをプラグインのマーケットプレイスとして追加し、`novel-to-manga-anime-generator` をインストールしてください。

### Claude Code
```
/plugin marketplace add BBQ2077/novel-to-manga-anime-generator
/plugin install novel-to-manga-anime-generator@manga-anime-tools
```

## 使ってみる

- `この小説を漫画にしてください：[本文を貼り付け]`
- `この場面を 3 分のアニメにしてください：[本文を貼り付け]`

## 画像・動画の生成方法

| | サブスクリプション：**BytePlus Lumina**（おすすめ） | API：**BytePlus ModelArk** |
|---|---|---|
| 向いている人 | ほとんどの人：数章・数話を、調整しながら作りたい | AI エージェントに全自動で大量生成させたい |
| 料金 | 月額固定 | 従量課金 |
| 使い方 | プロンプトをウェブ画面に貼り付けて生成 | API キーを設定すれば、スクリプトが自動で生成 |
| リンク | https://byteplus.pxf.io/vDqjnd | https://byteplus.pxf.io/c/7876220/3836120/48404 |

API の設定方法：[`references/api-setup.md`](plugins/novel-to-manga-anime-generator/skills/novel-to-manga-anime-generator/references/api-setup.md)

> 上記はアフィリエイトリンクです。リンク経由で登録しても追加料金はかからず、このプロジェクトの支援になります。

## 著作権

⚠️ 原作の権利を取得していない場合、商用利用はしないでください。

## ライセンス

[MIT](LICENSE)
