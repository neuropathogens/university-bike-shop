"""AP Physics 1 -> /study/ap/ap-physics-1/tests/unit-N/ and unit-N-checks/ (see ap_sci/quizgen.py)."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_sci.quizgen import build_all  # noqa: E402
from ap_physics_1.course import C  # noqa: E402

QUIZZES = build_all(C, HERE)
