from dataclasses import dataclass, field


@dataclass
class Q:
    rule: str          # guide section, e.g. "3.2"
    stem: str          # LaTeX; ___ marks the blank
    correct: str       # LaTeX
    wrong: list = field(default_factory=list)  # three LaTeX distractors
    why: str = ""      # LaTeX, no letter references

    def __post_init__(self):
        assert len(self.wrong) == 3, self.stem[:60]
        assert self.correct not in self.wrong, self.stem[:60]
        assert "___" in self.stem, self.stem[:60]
        assert self.rule in RULES, self.rule


RULES = {
    "3.2": "Joining clauses",
    "3.3": "Fragments",
    "3.4": "Semicolons",
    "3.5": "Colons",
    "3.6": "Dashes",
    "3.7": "Supplementary elements",
    "3.8": "Essential elements",
    "3.9": "Introductory elements",
    "3.10": "Conjunctive adverbs",
    "3.11": "Lists and series",
    "3.12": "Forbidden commas",
    "3.13": "Questions, quotations",
    "4.1": "Subject--verb agreement",
    "4.2": "Tense",
    "4.3": "Verb form",
    "4.4": "Possessives",
    "4.5": "Pronouns",
    "4.6": "Modifiers",
    "4.7": "Edge rules",
}

# position-based sections: (title, first item, last item, guide sections)
SECTIONS = [
    ("Sentence boundaries", 1, 5, r"\S3.2--3.6, 3.10"),
    ("Within-sentence punctuation", 6, 10, r"\S3.6--3.13"),
    ("Verbs", 11, 15, r"\S4.1--4.3, 4.7"),
    ("Nouns and pronouns", 16, 18, r"\S4.4--4.5"),
    ("Modifiers", 19, 20, r"\S4.6"),
]
