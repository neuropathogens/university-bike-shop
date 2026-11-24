"""AP Spanish Language and Culture study series -> /study/ap/ap-spanish/tests/<slug>/ (engine: quizzes/ap_wl)."""
from pathlib import Path

from ap_wl.quizgen import build_all
from ap_spanish.lang import L
from ap_spanish.content import DOCS

QUIZZES = build_all(L, DOCS, Path(__file__).resolve().parent / "pages.json")
