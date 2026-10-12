#!/usr/bin/env python3
"""Create a clean case folder for a new project from the my-case template.

    python3 tools/new-case.py onboarding-redesign
    python3 tools/new-case.py onboarding-redesign --title "Onboarding redesign"

The new folder is a copy of my-case with the [EXAMPLE] items removed, the example
rows cleared from the hub pages, the case name filled in, and index.html rebuilt.
my-case itself is not changed, so it stays a clean template for the next project.
Standard library only.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "my-case")
IGNORE = shutil.ignore_patterns(".DS_Store", "__pycache__", "_export", "index.html")
ITEM_RE = re.compile(r"^[OHMDEF]\d+\.md$")
ITEM_LINK_RE = re.compile(r"\]\((?:\.\./)?(?:[a-z]+/)?[OHMDEF]\d+\.md\)")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def clean_hub_page(text, is_readme):
    out = []
    for line in text.split("\n"):
        if line.startswith("|"):
            first = line.split("|")[1].strip() if line.count("|") > 1 else ""
            if "[EXAMPLE]" in line or ITEM_LINK_RE.search(line):
                continue  # a row that describes an example item
            if re.match(r"^D\d+\b", first):
                continue  # example rows in the alignment audit and verdict tables
            if re.fullmatch(r"M\d+", first):
                line = line.replace("| %s |" % first, "| [metric] |", 1)
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\[O1\]\([^)]*O1\.md\)", "[opportunity ID]", text)
    if is_readme:
        empty = {
            "alignment": "_Chưa có decision nào. Bảng này được dựng khi bạn thêm item._",
            "warnings": "- Chưa có item nào, nên chưa có warning.",
        }

        def block(m):
            kind = m.group(1)
            if kind in empty:
                return "%s\n%s\n<!-- /generated -->" % (m.group(0).split("\n")[0], empty[kind])
            return m.group(0)

        text = re.sub(r"<!-- generated:(\w+)[^\n]*-->\n.*?<!-- /generated -->", block, text, flags=re.S)
        text = text.replace(" Dữ liệu `[EXAMPLE]` ở đây để bạn thấy hub chạy ra sao. Xoá và thay bằng dữ liệu của bạn.", "")
    return text


def main():
    ap = argparse.ArgumentParser(description="Create a clean case folder from the my-case template.")
    ap.add_argument("name", help="folder name: lowercase letters, digits and hyphens, e.g. onboarding-redesign")
    ap.add_argument("--title", help="project name shown in the hub (default: derived from the folder name)")
    ap.add_argument("--dest", default=ROOT, help="parent folder for the new case (default: the workspace root)")
    a = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.name):
        sys.exit("Tên folder chỉ gồm chữ thường, số và dấu gạch ngang, ví dụ: onboarding-redesign")
    if not os.path.isdir(TEMPLATE):
        sys.exit("Không tìm thấy folder template: %s" % TEMPLATE)
    dest = os.path.join(os.path.abspath(a.dest), a.name)
    if os.path.exists(dest):
        sys.exit("Folder đã tồn tại: %s\nChọn một tên khác, hoặc xoá folder đó nếu bạn muốn làm lại." % dest)
    title = a.title or a.name.replace("-", " ").capitalize()

    shutil.copytree(TEMPLATE, dest, ignore=IGNORE)
    insights = os.path.join(dest, "insights")

    removed = 0
    for dirpath, dirnames, filenames in os.walk(insights):
        dirnames[:] = [d for d in dirnames if not d.startswith("_")]
        for name in sorted(filenames):
            p = os.path.join(dirpath, name)
            if ITEM_RE.match(name) and "[EXAMPLE]" in read(p):
                os.remove(p)
                removed += 1
    # example rows in the stage pages and reference pages
    for folder in (os.path.join(dest, "stages"), os.path.join(dest, "standards")):
        for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
            p = os.path.join(folder, name)
            if os.path.isfile(p) and name.endswith(".md"):
                write(p, clean_hub_page(read(p), False))
    p = os.path.join(dest, "insights", "case-log.md")
    if os.path.isfile(p):
        write(p, clean_hub_page(read(p), False))

    for folder in ("opportunities", "hypotheses", "metrics", "decisions", "evidence", "findings"):
        d = os.path.join(insights, folder)
        os.makedirs(d, exist_ok=True)
        if not os.listdir(d):
            write(os.path.join(d, ".gitkeep"), "")  # keeps the empty folder in Git
    p = os.path.join(dest, "_skills", "how-the-hub-works.md")
    if os.path.isfile(p):
        write(p, re.sub(r"^- Các item `\[EXAMPLE\]`.*\n", "", read(p), flags=re.M))

    p = os.path.join(dest, "README.md")
    t = read(p).replace("# Project: [tên dự án]", "# Project: %s" % title)
    t = re.sub(r"^\| Tên dự án \| \|$", "| Tên dự án | %s |" % title, t, flags=re.M)
    t = re.sub(r"<!-- template-only -->.*?<!-- /template-only -->\n\n?", "", t, flags=re.S)  # note that only makes sense in my-case
    t = t.replace("# my-case", "# %s" % a.name).replace("my-case/\n", "%s/\n" % a.name)
    write(p, t)

    print("Đã tạo: %s" % dest)
    print("  - Đã xoá %d item [EXAMPLE] và dọn các dòng mẫu trong standards/" % removed)
    tool = os.path.join(dest, "_skills", "export-hub.py")
    if os.path.isfile(tool):
        r = subprocess.run([sys.executable, tool], cwd=dest, capture_output=True, text=True)
        print("  - index.html: %s" % ("đã tạo" if r.returncode == 0 else "lỗi, chạy lại: python3 _skills/export-hub.py"))
        if r.returncode != 0:
            print(r.stderr.strip()[-400:])
    print("\nViệc đầu tiên:")
    print("  1. Mở folder %s bằng công cụ bạn quen (AI coding tool, VS Code hoặc Obsidian)." % a.name)
    print("  2. Mở README.md trong folder, điền Project card, rồi điền context/product-and-users.md và context/data-rules.md.")
    print("  3. Khi có item đầu tiên, copy một file trong insights/_templates/ vào folder loại tương ứng, ví dụ insights/decisions/.")


if __name__ == "__main__":
    main()
