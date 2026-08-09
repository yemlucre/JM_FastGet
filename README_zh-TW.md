# JM_FastGet

[English](README_en.md) | **[简体中文](README.md)** | [日本語](README_ja.md) | 繁體中文

> 自動下載 JM 漫畫並快速轉換為 PDF 的一體化工具集。

---

## 簡介

本工具集透過命令列工具 `jmv` / `jmcomic` 完成漫畫的預覽與下載，再呼叫 `webp2pdf.py` 將下載的 WebP 圖片依序號合併為一個 PDF，並自動整理到指定目錄。適合喜歡離線收藏漫畫的使用者。

## 功能特色

- **一鍵下載與轉換** — 輸入漫畫編號，自動預覽、確認、下載並轉成 PDF。
- **自動命名與歸檔** — 下載的資料夾依原始名稱移動到 `D:\cartoon`，PDF 以資料夾名命名。
- **依序號排序合併** — 圖片依檔案名稱中的數字自然排序後合成為 PDF，頁序正確。
- **雙入口** — 可透過 `Load_cartoon.bat` 雙擊啟動，也可直接執行 Python 腳本。

## 環境需求

| 依賴 | 用途 |
| --- | --- |
| Python 3.x | 執行腳本 |
| [img2pdf](https://pypi.org/project/img2pdf/) | WebP 圖片合併為 PDF |
| `jmv` | JM 漫畫預覽 |
| `jmcomic` | JM 漫畫下載 |

安裝 Python 依賴：

```bash
pip install img2pdf
```

`jmv` 與 `jmcomic` 需要自行安裝，並確保它們在系統 PATH 中（`auto_jm.py` 透過命令列呼叫）。

## 使用說明

### 方式一：雙擊批次檔

直接雙擊 `Load_cartoon.bat`，它會自動執行 `auto_jm.py`。

### 方式二：命令列執行

```bash
python auto_jm.py
```

互動流程：

1. 輸入漫畫數字編號（輸入 `q` 退出）。
2. 腳本執行 `jmv <編號>` 預覽專輯。
3. 詢問是否下載，輸入 `是/不是`（或 `y/n`）。
4. 確認後執行 `jmcomic <編號>` 下載。
5. 下載完成後自動移動到 `D:\cartoon`。
6. 自動執行 `webp2pdf.py` 產生 PDF。

### 單獨轉換 PDF

如果你已有一個包含 WebP 圖片的漫畫資料夾，可以直接用 `webp2pdf.py`：

```bash
python webp2pdf.py <漫畫資料夾路徑>
```

輸出：`D:\cartoon\<資料夾名>.pdf`

## 專案結構

```
JM_FastGet/
├── auto_jm.py          # 主腳本：預覽、下載、移動、轉 PDF 全流程
├── webp2pdf.py         # 將 WebP 圖片依序號合併為 PDF
├── Load_cartoon.bat    # Windows 雙擊啟動腳本
├── README.md           # 简体中文说明文档（默认）
├── README_en.md        # English documentation
├── README_zh-TW.md     # 繁體中文說明文件
└── README_ja.md        # 日本語のドキュメント
```

## 注意事項

- 腳本假設輸出目錄為 `D:\cartoon`，如需更改請修改兩個 Python 檔案中的 `ROOT` / `CARTON_DIR` 常數。
- 請遵守相關法律法規，僅下載你有權查看和收藏的內容，請勿用於商業用途。
- 本工具僅供個人學習與收藏使用，作者不對任何濫用行為負責。

## 作者

- GitHub: [yemlucre](https://github.com/yemlucre)

## License

本倉庫僅供個人學習交流使用，未指定開源授權條款。

---

[English Version](README_en.md) | [简体中文版](README.md) | [日本語版](README_ja.md)
