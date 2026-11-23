"""Data model for ACT English practice-set guides.

Every question stores its correct answer as an index (0-3). Letters are
assigned at build time from the question number, mirroring the real test:
odd-numbered items use A/B/C/D, even-numbered items use F/G/H/J.
"""
from __future__ import annotations

from dataclasses import dataclass, field

CATS = {
    "POW": "Production of Writing",
    "KLA": "Knowledge of Language",
    "CSE": "Conventions of Standard English",
}


@dataclass
class Q:
    choices: list[str]
    ans: int
    why: str
    stem: str = ""
    context: str = ""
    rule: str = ""      # overrides the section tag in the answer key
    cat: str = ""       # overrides the section category
    layout: str = "auto"  # auto | grid | list

    def __post_init__(self) -> None:
        if len(self.choices) != 4:
            raise ValueError(f"need 4 choices: {self.choices}")
        if not 0 <= self.ans <= 3:
            raise ValueError(f"bad answer index {self.ans}")


@dataclass
class Section:
    title: str
    key: str                      # label used for \ref and the key's Rule column
    tag: str = ""                 # short rule name for the answer key
    cat: str = ""                 # POW | KLA | CSE
    body: str = ""                # LaTeX inside the rule box
    intro: str = ""               # LaTeX before the rule box
    stem: str = ""                # default stem for questions in this section
    passage: str = ""             # LaTeX with @@ markers, one per question, in order
    passage_label: str = ""
    passage_title: str = ""
    questions: list[Q] = field(default_factory=list)
    newpage: bool = False


@dataclass
class Guide:
    slug: str
    kicker: str
    title: str
    subtitle: str
    short: str
    abstract: str
    sections: list[Section]
    date: str = "November 2026"
    subscores: bool = False
