# JM_FastGet

[English](README_en.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja.md) | 简体中文

> 自动下载 JM 漫画并快速转换为 PDF 的一体化工具集。

---

## 简介

本工具集通过命令行工具 `jmv` / `jmcomic` 完成漫画的预览与下载，再调用 `webp2pdf.py` 将下载的 WebP 图片按序号合并为一个 PDF，并自动整理到指定目录。适合喜欢离线收藏漫画的用户。

## 功能特性

- **一键下载与转换** — 输入漫画编号，自动预览、确认、下载并转 PDF。
- **自动命名与归档** — 下载的文件夹按原始名称移动到 `D:\cartoon`，PDF 以文件夹名命名。
- **按序号排序合并** — 图片按文件名中的数字自然排序后合成为 PDF，页序正确。
- **双入口** — 可通过 `Load_cartoon.bat` 双击启动，也可直接运行 Python 脚本。

## 环境要求

| 依赖 | 用途 |
| --- | --- |
| Python 3.x | 运行脚本 |
| [img2pdf](https://pypi.org/project/img2pdf/) | WebP 图片合并为 PDF |
| `jmv` | JM 漫画预览 |
| `jmcomic` | JM 漫画下载 |

安装 Python 依赖：

```bash
pip install img2pdf
```

`jmv` 与 `jmcomic` 需要自行安装，并确保它们在系统 PATH 中（`auto_jm.py` 通过命令行调用）。

## 使用说明

### 方式一：双击批处理

直接双击 `Load_cartoon.bat`，它会自动运行 `auto_jm.py`。

### 方式二：命令行运行

```bash
python auto_jm.py
```

交互流程：

1. 输入漫画数字编号（输入 `q` 退出）。
2. 脚本运行 `jmv <编号>` 预览专辑。
3. 询问是否下载，输入 `是/不是`（或 `y/n`）。
4. 确认后运行 `jmcomic <编号>` 下载。
5. 下载完成后自动移动到 `D:\cartoon`。
6. 自动运行 `webp2pdf.py` 生成 PDF。

### 单独转换 PDF

如果你已有一个包含 WebP 图片的漫画文件夹，可以直接用 `webp2pdf.py`：

```bash
python webp2pdf.py <漫画文件夹路径>
```

输出：`D:\cartoon\<文件夹名>.pdf`

## 项目结构

```
JM_FastGet/
├── auto_jm.py          # 主脚本：预览、下载、移动、转 PDF 全流程
├── webp2pdf.py         # 将 WebP 图片按序号合并为 PDF
├── Load_cartoon.bat    # Windows 双击启动脚本
├── README.md           # 简体中文说明文档（默认）
├── README_en.md        # English documentation
├── README_zh-TW.md     # 繁體中文說明文件
└── README_ja.md        # 日本語のドキュメント
```

## 注意事项

- 脚本假设输出目录为 `D:\cartoon`，如需更改请修改两个 Python 文件中的 `ROOT` / `CARTON_DIR` 常量。
- 请遵守相关法律法规，仅下载你有权查看和收藏的内容，请勿用于商业用途。
- 本工具仅供个人学习与收藏使用，作者不对任何滥用行为负责。

## 作者

- GitHub: [yemlucre](https://github.com/yemlucre)

## License

本仓库仅供个人学习交流使用，未指定开源许可证。

---

[English Version](README_en.md) | [繁體中文版](README_zh-TW.md) | [日本語版](README_ja.md)
