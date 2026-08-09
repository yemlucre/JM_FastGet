# -*- coding: utf-8 -*-
# 版权声明: 本文件由 yemlucre 创作，创作日期 2026-08-09。保留所有权利。
r"""自动下载 JM 漫画并转 PDF。

流程:
1. 输入一串数字
2. 运行 jmv 数字 预览专辑
3. 询问是否下载(是 / 不是)
   - 不是 -> 重新输入数字
   - 是   -> 运行 jmcomic 数字 下载
4. 把下载的文件夹移动到 D:\cartoon
5. 运行 webp2pdf.py 生成 PDF
"""
import os
import shutil
import subprocess
import sys

CARTON_DIR = r"D:\cartoon"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def ask_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("是", "对", "y", "yes"):
            return True
        if ans in ("不是", "不对", "n", "no"):
            return False
        print("请回答 是 或 不是。")


def newest_subdir(base_dir):
    try:
        dirs = [
            os.path.join(base_dir, name)
            for name in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, name))
        ]
    except OSError:
        return None
    if not dirs:
        return None
    return max(dirs, key=os.path.getmtime)


def run_cmd(cmd):
    print(">>>", " ".join(cmd))
    try:
        return subprocess.run(cmd).returncode
    except FileNotFoundError:
        print(f"命令不存在: {cmd[0]}，请先安装。")
        return -1


def main():
    os.chdir(SCRIPT_DIR)

    while True:
        text = input("请输入漫画数字(输入 q 退出): ").strip()
        if text.lower() in ("q", "quit", "exit"):
            return
        number = "".join(ch for ch in text if ch.isdigit())
        if not number:
            print("没有识别到数字，请重新输入。")
            continue

        # 预览
        print(f"运行 jmv {number} 预览...")
        run_cmd(["jmv", "-y", number])

        # 是否下载
        if not ask_yes_no("是否下载这个漫画? (y/n): "):
            print("已取消，回到输入。")
            continue

        # 下载
        print(f"运行 jmcomic {number} 下载...")
        rc = run_cmd(["jmcomic", number])
        if rc != 0:
            print("下载失败，请检查网络或数字是否正确。")
            continue

        # 找到刚下载的文件夹，移动到 D:\cartoon
        folder = newest_subdir(SCRIPT_DIR)
        if folder is None:
            print("未找到下载的文件夹。")
            continue

        dst = os.path.join(CARTON_DIR, os.path.basename(folder))
        if os.path.normcase(os.path.dirname(os.path.abspath(folder))) == os.path.normcase(CARTON_DIR):
            print(f"文件夹已在目标目录: {dst}")
        elif os.path.exists(dst):
            print(f"目标已存在，跳过移动: {dst}")
        else:
            print(f"移动 {folder} -> {dst}")
            shutil.move(folder, dst)

        # 生成 PDF
        print("运行 webp2pdf.py 生成 PDF...")
        run_cmd([sys.executable, os.path.join(SCRIPT_DIR, "webp2pdf.py"), dst])

        print(f"完成! PDF 已生成: {os.path.join(CARTON_DIR, os.path.basename(dst) + '.pdf')}")
        return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已退出。")
