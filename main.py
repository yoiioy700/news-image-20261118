"""Ship the broadsheet: place the finished front page where the grader looks.

The page itself is drawn by render_news_image_v6.py and stored in this
repository as frontpage.png. This entrypoint does one small job and does it
out loud: it carries that page into the output folder under the name the
competition asks for, then proves the copy is a whole PNG before it exits.
"""

import hashlib
import os
import sys
from pathlib import Path

PNG_MAGIC = bytes((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))
PAGE_NAME = "frontpage.png"
OUTPUT_NAME = "entry.png"


def page_file():
    here = Path(__file__).resolve().parent
    return here / PAGE_NAME


def output_folder():
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(chosen)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def check_png(data):
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        raise SystemExit("frontpage.png is not a PNG: bad signature")
    if b"IEND" not in data[-16:]:
        raise SystemExit("frontpage.png looks cut off: no IEND trailer")
    if len(data) < 29 or data[12:16] != b"IHDR":
        raise SystemExit("frontpage.png has no IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    return width, height


def main():
    page = page_file()
    if not page.is_file():
        raise SystemExit(f"missing page next to this script: {page}")
    data = page.read_bytes()
    width, height = check_png(data)
    target = output_folder() / OUTPUT_NAME
    target.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
        raise SystemExit(f"copy failed: {target} does not match {page}")
    print(f"wrote {target} ({width}x{height}, {len(data)} bytes, sha256 {digest[:12]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
