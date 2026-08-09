# JM_FastGet

> An all-in-one toolkit that automatically downloads JM comics and converts them into PDFs.

[简体中文](README.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | English

---

## Introduction

This toolkit uses the CLI tools `jmv` / `jmcomic` to preview and download comics, then calls `webp2pdf.py` to merge the downloaded WebP images into a single PDF by page order, and automatically organizes everything into a target folder. It is suitable for users who like to keep offline collections.

## Features

- **One-click download & convert** — Enter a comic ID, preview, confirm, download, and convert to PDF automatically.
- **Auto naming & archiving** — Downloaded folders are moved to `D:\cartoon` under their original names, and the PDF is named after the folder.
- **Numeric ordering** — Images are naturally sorted by the digits in their filenames before merging, keeping correct page order.
- **Two entry points** — Launch via double-clicking `Load_cartoon.bat`, or run the Python script directly.

## Requirements

| Dependency | Purpose |
| --- | --- |
| Python 3.x | Run the scripts |
| [img2pdf](https://pypi.org/project/img2pdf/) | Merge WebP images into PDF |
| `jmv` | Preview JM comics |
| `jmcomic` | Download JM comics |

Install the Python dependency:

```bash
pip install img2pdf
```

`jmv` and `jmcomic` need to be installed separately and available on your system PATH (`auto_jm.py` invokes them via the command line).

## Usage

### Way 1: Double-click the batch file

Simply double-click `Load_cartoon.bat` — it will run `auto_jm.py` for you.

### Way 2: Run from the command line

```bash
python auto_jm.py
```

Interactive flow:

1. Enter the comic's numeric ID (type `q` to quit).
2. The script runs `jmv <ID>` to preview the album.
3. Asked whether to download; answer `是/不是` (or `y/n`).
4. After confirmation, `jmcomic <ID>` downloads the comic.
5. The downloaded folder is moved to `D:\cartoon`.
6. `webp2pdf.py` runs automatically to generate the PDF.

### Convert PDF alone

If you already have a comic folder of WebP images, use `webp2pdf.py` directly:

```bash
python webp2pdf.py <path/to/comic-folder>
```

Output: `D:\cartoon\<folder-name>.pdf`

## Project Structure

```
JM_FastGet/
├── auto_jm.py          # Main script: preview, download, move & convert
├── webp2pdf.py         # Merge WebP images into PDF by numeric order
├── Load_cartoon.bat    # Windows double-click launcher
├── README.md           # 简体中文说明文档（默认）/ Simplified Chinese documentation (default)
├── README_en.md        # English documentation
├── README_zh-TW.md     # 繁體中文說明文件 / Traditional Chinese documentation
└── README_ja.md        # 日本語のドキュメント / Japanese documentation
```

## Notes

- The scripts assume an output directory of `D:\cartoon`; change the `ROOT` / `CARTON_DIR` constants in the Python files if needed.
- Please comply with applicable laws and regulations. Only download content you are entitled to access and collect; do not use it commercially.
- This tool is for personal study and collection only. The author is not responsible for any misuse.

## Author

- GitHub: [yemlucre](https://github.com/yemlucre)

## License

This repository is for personal study and communication only, and is not distributed under any open-source license.
