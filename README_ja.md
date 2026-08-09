# JM_FastGet

[English](README_en.md) | [简体中文](README.md) | [繁體中文](README_zh-TW.md) | 日本語

> JM 漫画を自動ダウンロードして PDF に素早く変換するオールインワンツールキット。

---

## 概要

このツールキットは、コマンドラインツール `jmv` / `jmcomic` で漫画のプレビューとダウンロードを行い、`webp2pdf.py` でダウンロードした WebP 画像をページ順に 1 つの PDF に結合し、指定のディレクトリに自動整理します。オフラインで漫画を保存しておきたい方に向いています。

## 機能

- **ワンクリックでダウンロード＆変換** — 漫画の ID を入力するだけで、プレビュー・確認・ダウンロード・PDF 変換を自動実行。
- **自動命名＆アーカイブ** — ダウンロードしたフォルダを元の名前のまま `D:\cartoon` に移動し、PDF はフォルダ名で命名。
- **ページ順に自動ソート** — ファイル名の数字で自然順に並べてから結合するため、ページ順が正しくなります。
- **2 つの起動方法** — `Load_cartoon.bat` をダブルクリックするか、Python スクリプトを直接実行できます。

## 必要環境

| 依存 | 用途 |
| --- | --- |
| Python 3.x | スクリプトの実行 |
| [img2pdf](https://pypi.org/project/img2pdf/) | WebP 画像を PDF に結合 |
| `jmv` | JM 漫画のプレビュー |
| `jmcomic` | JM 漫画のダウンロード |

Python の依存をインストール:

```bash
pip install img2pdf
```

`jmv` と `jmcomic` は別途インストールし、システムの PATH に含めてください（`auto_jm.py` はコマンドラインから呼び出します）。

## 使い方

### 方法 1: バッチファイルをダブルクリック

`Load_cartoon.bat` をダブルクリックすると、`auto_jm.py` が自動的に実行されます。

### 方法 2: コマンドラインで実行

```bash
python auto_jm.py
```

操作の流れ:

1. 漫画の数字 ID を入力します（`q` で終了）。
2. `jmv <ID>` でアルバムをプレビューします。
3. ダウンロードするか確認され、`是/不是`（または `y/n`）で答えます。
4. 確認後、`jmcomic <ID>` でダウンロードします。
5. ダウンロード完了後、`D:\cartoon` に自動的に移動します。
6. `webp2pdf.py` が自動実行され、PDF が生成されます。

### PDF 変換のみ行う場合

WebP 画像が入った漫画フォルダをすでに持っている場合は、`webp2pdf.py` を直接使えます:

```bash
python webp2pdf.py <漫画フォルダのパス>
```

出力: `D:\cartoon\<フォルダ名>.pdf`

## プロジェクト構成

```
JM_FastGet/
├── auto_jm.py          # メインスクリプト：プレビュー・ダウンロード・移動・変換
├── webp2pdf.py         # WebP 画像をページ順に PDF へ結合
├── Load_cartoon.bat    # Windows ダブルクリック起動スクリプト
├── README.md           # 简体中文说明文档（默认）
├── README_en.md        # English documentation
├── README_zh-TW.md     # 繁體中文說明文件
└── README_ja.md        # 日本語のドキュメント
```

## 注意事項

- 出力ディレクトリは `D:\cartoon` を想定しています。変更する場合は、Python ファイル内の `ROOT` / `CARTON_DIR` 定数を修正してください。
- 関連法令を遵守し、閲覧・保存する権利があるコンテンツのみをダウンロードしてください。商業用途は禁止です。
- 本ツールは個人の学習・収集用途のみを対象としており、作者は不正利用について責任を負いません。

## 作者

- GitHub: [yemlucre](https://github.com/yemlucre)

## License

本リポジトリは個人の学習・交流用であり、オープンソースライセンスは適用されていません。

---

[English Version](README_en.md) | [简体中文版](README.md) | [繁體中文版](README_zh-TW.md)
