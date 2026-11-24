"""Content model for the AP world language study series (generalized from quizzes/ap_chinese/model.py).

One Python module per unit (<family>/content/pNN.py) builds two Doc objects, GUIDE and QSET. The same objects are
rendered to LaTeX (build_tex.py -> the PDFs) and to the interactive quizzes (quiz.py), so a question, its
answer, its key line and its explanation are written once.

Text is LaTeX-lite: the target language as plain Unicode, \\textbf, \\emph, ``quotes'', --, \\%, \\blank.
Blocks that appear only in the PDFs (vocabulary tables, notes) may use any LaTeX from ap-wl.sty.
"""
import random
import re

CJK = ("　", "〿"), ("㐀", "䶿"), ("一", "鿿"), ("＀", "￯")


def lite(s):
    """Escape a bare % or & in LaTeX-lite text."""
    if isinstance(s, (list, tuple)):
        return type(s)(lite(x) for x in s)
    return re.sub(r"(?<!\\)([%&])", r"\\\1", s) if isinstance(s, str) else s


def width(s):
    """Display width: a Chinese character counts double."""
    return sum(2 if any(a <= c <= b for a, b in CJK) else 1 for c in s)


class Doc:
    def __init__(self, stem, kind, title, docpart, abstract, scoring, short, sub=None):
        self.stem, self.kind = stem, kind          # stem like "01-families-communities"; kind "guide" | "questions"
        self.title, self.docpart, self.abstract, self.scoring = title, docpart, abstract, scoring
        self.short, self.sub = short, sub or title   # short: "Unit 1"; sub: quiz subtitle
        self.blocks = []
        self.topics = {}                            # key -> (name, guide stem, section number)
        self.tail = []                              # LaTeX after the answer key (scoring guides)
        self.fr = []
        self._sec = 0

    # ----- building -----
    def sec(self, title, quiz_title=None):
        self._sec += 1
        self.blocks.append(("sec", self._sec, title, quiz_title or title))
        return self._sec

    def tex(self, s):
        self.blocks.append(("tex", s))

    def src(self, title, paras, n, table=None, note=None):
        """A reading/listening source shared by the next n questions. paras: list of paragraphs (LaTeX-lite).
        table: (header cells, rows) shown after the paragraphs (the "chart")."""
        if table:
            table = (lite(table[0]), [lite(r) for r in table[1]])
        self.blocks.append(("src", dict(title=title, paras=lite(paras), n=n, table=table, note=lite(note))))

    def q(self, tag, stem, right, wrongs, why, idea, steps=()):
        """tag: '<topic key> <rule>'; wrongs: three (choice, why it is wrong) pairs."""
        assert len(wrongs) == 3, stem
        assert len({right, *[w for w, _ in wrongs]}) == 4, stem
        stem, right, wrongs = lite(stem), lite(right), [(lite(w), n) for w, n in wrongs]
        self.blocks.append(("q", dict(tag=tag, stem=stem, right=right, wrongs=list(wrongs), why=why, idea=idea,
                                      steps=list(steps))))

    def frq(self, **kw):
        """kind, head, mins, directions [paras], prompt [paras], panels [str] (story pictures, described),
        sources [dict(title, paras, table)], model [paras], rows [(name, pts, earns, misses)], tips [str], ask, lines."""
        for k in ("directions", "prompt", "panels", "model"):
            if k in kw:
                kw[k] = lite(kw[k])
        # sources: [dict(title, paras, table=(head, rows))] printed with the task (the Argumentative Essay's three sources)
        kw["sources"] = [dict(title=lite(s["title"]), paras=lite(s["paras"]),
                              table=(lite(s["table"][0]), [lite(r) for r in s["table"][1]]) if s.get("table") else None)
                         for s in kw.get("sources", [])]
        kw["rows"] = [(lite(a), p, lite(b), lite(c)) for a, p, b, c in kw["rows"]]
        self.fr.append(kw)
        self.blocks.append(("frq", kw))

    # ----- derived -----
    def items(self):
        return [b[1] for b in self.blocks if b[0] == "q"]

    def place(self):
        """Give every question a correct position 1-4: balanced counts, never three in a row, seeded by stem."""
        qs = self.items()
        rng = random.Random(self.stem + self.kind)
        for _ in range(5000):
            pool = [1, 2, 3, 4] * (len(qs) // 4 + 1)
            rng.shuffle(pool)
            pos = pool[:len(qs)]
            if any(pos[i] == pos[i + 1] == pos[i + 2] for i in range(len(pos) - 2)):
                continue
            counts = [pos.count(k) for k in (1, 2, 3, 4)]
            if max(counts) - min(counts) <= 1:
                break
        else:
            raise SystemExit(f"{self.stem}: could not place answers")
        for q, p in zip(qs, pos):
            wrong = [w for w, _ in q["wrongs"]]
            rng.shuffle(wrong)
            choices = wrong[:]
            choices.insert(p - 1, q["right"])
            q["pos"], q["choices"] = p, choices
        return self


def topic_key(tag):
    return tag.split()[0]
