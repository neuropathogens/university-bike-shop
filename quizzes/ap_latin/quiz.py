"""AP Latin study series -> /study/ap/ap-latin/tests/<slug>/ (engine: quizzes/ap_wl)."""
from pathlib import Path

from ap_wl.quizgen import build_all
from ap_latin.lang import L
from ap_latin.content import DOCS

QUIZZES = build_all(L, DOCS, Path(__file__).resolve().parent / "pages.json")
