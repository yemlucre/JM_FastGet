# -*- coding: utf-8 -*-
# 版权声明: 本文件由 yemlucre 创作，创作日期 2026-08-09。保留所有权利。
"""把漫画文件夹里的 webp 图片按序号合并为一个 PDF。

用法:
    python webp2pdf.py <漫画文件夹路径>

输出: D:\\cartoon\\<文件夹名>.pdf
"""
import os
import re
import sys

import img2pdf

ROOT = r"D:\cartoon"


def numeric_sort_key(name):
    match = re.search(r"(\d+)", name)
    return int(match.group(1)) if match else 0


def main():
    if len(sys.argv) < 2:
        print("用法: python webp2pdf.py <漫画文件夹路径>")
        sys.exit(1)

    src_dir = sys.argv[1]
    if not os.path.isdir(src_dir):
        print(f"文件夹不存在: {src_dir}")
        sys.exit(1)

    files = [
        os.path.join(src_dir, name)
        for name in os.listdir(src_dir)
        if name.lower().endswith(".webp")
    ]
    if not files:
        print(f"该文件夹下没有 webp 文件: {src_dir}")
        sys.exit(1)

    files.sort(key=lambda p: numeric_sort_key(os.path.basename(p)))

    out_name = os.path.basename(src_dir) + ".pdf"
    out_path = os.path.join(ROOT, out_name)

    print(f"共 {len(files)} 张图片")
    print(f"输出: {out_path}")

    with open(out_path, "wb") as f:
        f.write(img2pdf.convert(files))

    print("完成!")


if __name__ == "__main__":
    main()
