#!/usr/bin/env python3
"""news-image-20261126 v4 entrypoint.

Copies the pre-rendered front page (entry.png, drawn in the build
session) to the grader's output directory. Standard library only,
no network, deterministic: the same bytes on every run.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The copy is byte-for-byte, so both grader runs write identical output.
    print("wrote", dst)


if __name__ == "__main__":
    main()
