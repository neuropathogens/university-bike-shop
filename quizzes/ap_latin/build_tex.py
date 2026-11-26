"""Render the AP Latin series to LaTeX and PDF and publish it (engine: quizzes/ap_wl/texbuild.py).

    python3 -I quizzes/ap_latin/build_tex.py            # all documents, then publish
    python3 -I quizzes/ap_latin/build_tex.py 03-        # compile only matching documents (no publish)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.texbuild import main  # noqa: E402
from ap_latin.lang import L  # noqa: E402
from ap_latin.content import DOCS  # noqa: E402

if __name__ == "__main__":
    main(L, DOCS, HERE)
