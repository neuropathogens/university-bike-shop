"""AP Japanese Language and Culture study series -> /study/ap/ap-japanese/tests/<slug>/ (engine: quizzes/ap_wl)."""
from pathlib import Path

from ap_wl.quizgen import build_all
from ap_japanese.lang import L
from ap_japanese.content import DOCS

QUIZZES = build_all(L, DOCS, Path(__file__).resolve().parent / "pages.json")
