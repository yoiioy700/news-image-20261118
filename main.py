#!/usr/bin/env python3
"""news-image-20261118 entry: sum up 18 November 2026's world news in one image.

The front page is drawn at build time and shipped in this repository as
frontpage.png (see README.md for how it was made). This program is
standard-library only -- the make.fun sandbox installs nothing and has no
network -- so it simply copies that image to /output/entry.png. The copy is
byte-identical on every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(_HERE, "frontpage.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
