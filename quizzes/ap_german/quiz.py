"""AP German Language and Culture study series -> /study/ap/ap-german/tests/<slug>/ (engine: quizzes/ap_wl)."""
from pathlib import Path

from ap_wl.quizgen import build_all
from ap_german.lang import L
from ap_german.content import DOCS

QUIZZES = build_all(L, DOCS, Path(__file__).resolve().parent / "pages.json")
