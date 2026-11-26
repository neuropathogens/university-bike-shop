"""Write the AP Physics 2 section of /study (python3 -I quizzes/ap_physics_2/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_sci.study_rows import write_section  # noqa: E402
from ap_physics_2.course import C  # noqa: E402

if __name__ == "__main__":
    write_section(C)
