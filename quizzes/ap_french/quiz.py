"""AP French Language and Culture study series -> /study/ap/ap-french/tests/<slug>/ (engine: quizzes/ap_wl)."""
from pathlib import Path

from ap_wl.quizgen import build_all
from ap_french.lang import L
from ap_french.content import DOCS

QUIZZES = build_all(L, DOCS, Path(__file__).resolve().parent / "pages.json")
