"""AP Spanish Literature and Culture study series -> /study/ap/ap-spanish-literature/tests/<slug>/ (engine: quizzes/ap_wl)."""
from pathlib import Path

from ap_wl.quizgen import build_all
from ap_spanish_lit.lang import L
from ap_spanish_lit.content import DOCS

QUIZZES = build_all(L, DOCS, Path(__file__).resolve().parent / "pages.json")
