"""Fail if a page is missing a title, has an image without alt text,
or links to a file that isn't in the site folder.

Usage: python3 scripts/check_site.py site
"""
import os
import re
import sys
from urllib.parse import urlparse

root = sys.argv[1] if len(sys.argv) > 1 else "site"
problems = []
pages = 0
for dirpath, _, files in os.walk(root):
    for name in files:
        if not name.endswith(".html"):
            continue
        pages += 1
        path = os.path.join(dirpath, name)
        html = open(path, encoding="utf-8").read()
        if "<title>" not in html:
            problems.append(f"{path}: no <title>")
        for img in re.findall(r"<img\b[^>]*>", html):
            if 'alt="' not in img:
                problems.append(f"{path}: image without alt text: {img[:80]}")
        for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
            if ref.startswith(("#", "mailto:", "tel:", "data:")) or urlparse(ref).scheme:
                continue
            target = ref.split("#")[0].split("?")[0]
            if not target:
                continue
            full = os.path.normpath(os.path.join(dirpath, target))
            if os.path.isdir(full):
                full = os.path.join(full, "index.html")
            if not os.path.exists(full):
                problems.append(f"{path}: broken link to {ref}")

print(f"Checked {pages} pages.")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("No problems found.")
