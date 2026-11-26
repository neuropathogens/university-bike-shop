"""Write the AP Biology section of /study (python3 -I quizzes/ap_biology/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_sci.study_rows import write_section  # noqa: E402
from ap_biology.course import C  # noqa: E402

if __name__ == "__main__":
    write_section(C)
