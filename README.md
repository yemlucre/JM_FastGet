# JM_FastGet

> 自动下载 JM 漫画并快速转换为 PDF 的一体化工具集。
> An all-in-one toolkit that automatically downloads JM comics and converts them into PDFs quickly.

---

## 简介 / Introduction

本工具集通过命令行工具 `jmv` / `jmcomic` 完成漫画的预览与下载，再调用 `webp2pdf.py` 将下载的 WebP 图片按序号合并为一个 PDF，并自动整理到指定目录。适合喜欢离线收藏漫画的用户。

This toolkit uses the CLI tools `jmv` / `jmcomic` to preview and download comics, then calls `webp2pdf.py` to merge the downloaded WebP images into a single PDF by page order, and automatically organizes everything into a target folder. It is suitable for users who like to keep offline collections.

---

## 功能特性 / Features

- **一键下载与转换** — 输入漫画编号，自动预览、确认、下载并转 PDF。
  **One-click download & convert** — Enter a comic ID, preview, confirm, download, and convert to PDF automatically.
- **自动命名与归档** — 下载的文件夹按原始名称移动到 `D:\cartoon`，PDF 以文件夹名命名。
  **Auto naming & archiving** — Downloaded folders are moved to `D:\cartoon` under their original names, and the PDF is named after the folder.
- **按序号排序合并** — 图片按文件名中的数字自然排序后合成为 PDF，页序正确。
  **Numeric ordering** — Images are naturally sorted by the digits in their filenames before merging, keeping correct page order.
- **双入口** — 可通过 `Load_cartoon.bat` 双击启动，也可直接运行 Python 脚本。
  **Two entry points** — Launch via double-clicking `Load_cartoon.bat`, or run the Python script directly.

---

## 环境要求 / Requirements

| 依赖 / Dependency | 用途 / Purpose |
| --- | --- |
| Python 3.x | 运行脚本 / Run the scripts |
| [img2pdf](https://pypi.org/project/img2pdf/) | WebP 图片合并为 PDF / Merge WebP images into PDF |
| `jmv` | JM 漫画预览 / Preview JM comics |
| `jmcomic` | JM 漫画下载 / Download JM comics |

安装 Python 依赖：

```bash
pip install img2pdf
```

`jmv` 与 `jmcomic` 需要自行安装，并确保它们在系统 PATH 中（`auto_jm.py` 通过命令行调用）。

`jmv` and `jmcomic` need to be installed separately and available on your system PATH (`auto_jm.py` invokes them via the command line).

---

## 使用说明 / Usage

### 方式一：双击批处理 / Way 1: Double-click the batch file

直接双击 `Load_cartoon.bat`，它会自动运行 `auto_jm.py`。

Simply double-click `Load_cartoon.bat` — it will run `auto_jm.py` for you.

### 方式二：命令行运行 / Way 2: Run from the command line

```bash
python auto_jm.py
```

交互流程 / Interactive flow:

1. 输入漫画数字编号（输入 `q` 退出）。
   Enter the comic's numeric ID (type `q` to quit).
2. 脚本运行 `jmv <编号>` 预览专辑。
   The script runs `jmv <ID>` to preview the album.
3. 询问是否下载，输入 `是/不是`（或 `y/n`）。
   Asked whether to download; answer `是/不是` (or `y/n`).
4. 确认后运行 `jmcomic <编号>` 下载。
   After confirmation, `jmcomic <ID>` downloads the comic.
5. 下载完成后自动移动到 `D:\cartoon`。
   The downloaded folder is moved to `D:\cartoon`.
6. 自动运行 `webp2pdf.py` 生成 PDF。
   `webp2pdf.py` runs automatically to generate the PDF.

### 单独转换 PDF / Convert PDF alone

如果你已有一个包含 WebP 图片的漫画文件夹，可以直接用 `webp2pdf.py`：

If you already have a comic folder of WebP images, use `webp2pdf.py` directly:

```bash
python webp2pdf.py <漫画文件夹路径>
python webp2pdf.py <path/to/comic-folder>
```

输出：`D:\cartoon\<文件夹名>.pdf`

Output: `D:\cartoon\<folder-name>.pdf`

---

## 项目结构 / Project Structure

```
JM_FastGet/
├── auto_jm.py          # 主脚本：预览、下载、移动、转 PDF 全流程
│                       # Main script: preview, download, move & convert
├── webp2pdf.py         # 将 WebP 图片按序号合并为 PDF
│                       # Merge WebP images into PDF by numeric order
├── Load_cartoon.bat    # Windows 双击启动脚本
│                       # Windows double-click launcher
└── README.md           # 本文档 / This document
```

---

## 注意事项 / Notes

- 脚本假设输出目录为 `D:\cartoon`，如需更改请修改两个 Python 文件中的 `ROOT` / `CARTON_DIR` 常量。
  The scripts assume an output directory of `D:\cartoon`; change the `ROOT` / `CARTON_DIR` constants in the Python files if needed.
- 请遵守相关法律法规，仅下载你有权查看和收藏的内容，请勿用于商业用途。
  Please comply with applicable laws and regulations. Only download content you are entitled to access and collect; do not use it commercially.
- 本工具仅供个人学习与收藏使用，作者不对任何滥用行为负责。
  This tool is for personal study and collection only. The author is not responsible for any misuse.

---

## 作者 / Author

- GitHub: [yemlucre](https://github.com/yemlucre)

---

## License

本仓库仅供个人学习交流使用，未指定开源许可证。

This repository is for personal study and communication only, and is not distributed under any open-source license.
