#!/usr/bin/env python3
"""
Build script — assembles HTML pages from src/ templates + _partials/.

Usage:
    python3 build.py

Replaces <!--include:nav--> and <!--include:footer--> markers with the
contents of _partials/nav.html and _partials/footer.html respectively,
then writes the result to the root directory.
"""

import os

PAGES = [
    "index.html",
    "scientific-projects.html",
    "policy-and-progress.html",
]

PARTIALS_DIR = "_partials"
SRC_DIR = "src"
OUT_DIR = "."


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def build():
    partials = {
        "nav": read(os.path.join(PARTIALS_DIR, "nav.html")),
        "footer": read(os.path.join(PARTIALS_DIR, "footer.html")),
    }

    for page in PAGES:
        src_path = os.path.join(SRC_DIR, page)
        out_path = os.path.join(OUT_DIR, page)

        content = read(src_path)
        for name, html in partials.items():
            content = content.replace(f"<!--include:{name}-->", html)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  built: {page}")


if __name__ == "__main__":
    build()
