"""Compile the AP Biology PDFs (python3 -I quizzes/ap_biology/build_tex.py [unit numbers]); needs tectonic and pypdf."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_sci.texgen import main  # noqa: E402
from ap_biology.course import C  # noqa: E402

if __name__ == "__main__":
    main(C, HERE, sys.argv[1:])
