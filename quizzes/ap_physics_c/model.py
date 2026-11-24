"""Content model for the AP Physics C study series (one source for the PDFs and the quiz pages).

Each unit module (u01.py ... u13.py) defines UNIT = Unit(...). Text is LaTeX: $..$ math (KaTeX-safe, no
custom macros), \\textbf, \\emph, --, ``quotes''. The same strings go into the .tex files and, converted with
lib/latex.py, into the quiz pages, so the PDF and the quiz cannot drift apart.

    Q(tag, stem, right, [wrong1, wrong2, wrong3], why, steps, [note1, note2, note3], sort=False)

`right` is written first; the generator places it (balancing A-D within each document) or, with sort=True,
orders numeric choices by value. `notes` explain each wrong choice, in the order the wrong choices are
written. `tag` starts with the CED topic number ("2.5 Newton's second law").
"""
import re
from dataclasses import dataclass, field


@dataclass
class Q:
    tag: str
    stem: str
    right: str
    wrong: list
    why: str
    steps: list
    notes: list
    sort: bool = False
    # filled in by place()
    choices: list = None
    pos: int = None          # 1-4
    others: dict = None      # choice index -> note

    def __post_init__(self):
        assert len(self.wrong) == 3 and len(self.notes) == 3, self.stem[:60]
        assert len({self.right, *self.wrong}) == 4, ("duplicate choices", self.stem[:60])

    @property
    def topic(self):
        return re.match(r"(\d+\.\d+)", self.tag).group(1)


@dataclass
class Part:
    label: str
    pts: int
    prompt: str
    solution: str
    miss: str


@dataclass
class FRQ:
    kind: str        # Mathematical Routines | Translation Between Representations | Experimental Design and Analysis | Qualitative/Quantitative Translation
    pts: int
    stem: str
    parts: list
    mins: int = 24


@dataclass
class Sec:
    title: str       # "Newton's second law (2.5)"
    topics: list     # ["2.5"]
    body: str
    checks: list = field(default_factory=list)


@dataclass
class Unit:
    n: int
    slug: str
    title: str
    weight: str      # "20--25\\%"
    topics: str      # "2.1--2.10"
    abstract: str
    sections: list
    qsections: list  # [(title, [Q...])]
    frq: FRQ
    frq_topic: str = ""   # one line for the /study row, e.g. "a block on an incline with drag"

    @property
    def course(self):
        return "mech" if self.n <= 7 else "em"

    @property
    def course_name(self):
        return "AP Physics C: Mechanics" if self.n <= 7 else "AP Physics C: Electricity and Magnetism"

    @property
    def stem(self):
        return f"ap-physc-{self.n:02d}-{self.slug}"


def _num(s):
    """Numeric value of a choice like '$3.0\\times10^{-2}\\,\\mathrm{J}$' (for sort=True)."""
    t = s.replace("{", "").replace("}", "").replace("$", "").replace("\\,", " ").replace("−", "-")
    m = re.search(r"(-?\d+(?:\.\d+)?)(?:\s*\\times\s*10\^(-?\d+))?", t)
    assert m, s
    v = float(m.group(1))
    if m.group(2):
        v *= 10 ** int(m.group(2))
    if re.search(r"\\frac", s) or "/" in t.split(" ")[0]:
        raise AssertionError(f"sort=True needs plain numbers: {s}")
    return v


PATTERN = [2, 4, 1, 3, 3, 1, 4, 2, 1, 2, 4, 3, 2, 3, 1, 4]


def place(qs):
    """Assign choice order to a document's questions: balance positions, no letter three times running."""
    counts = {1: 0, 2: 0, 3: 0, 4: 0}
    last = []
    for i, q in enumerate(qs):
        items = [(q.right, None)] + [(w, n) for w, n in zip(q.wrong, q.notes)]
        if q.sort:
            items.sort(key=lambda x: _num(x[0]))
            up = items.index(next(x for x in items if x[1] is None)) + 1
            down = 5 - up
            ok = lambda p: not (len(last) >= 2 and last[-1] == last[-2] == p)
            if (counts[down], not ok(down)) < (counts[up], not ok(up)):
                items.reverse()
        else:
            pref = PATTERN[i % len(PATTERN)]
            options = sorted(counts, key=lambda p: (counts[p], (p - pref) % 4))
            pos = next(p for p in options if not (len(last) >= 2 and last[-1] == last[-2] == p))
            wrongs = items[1:]
            items = wrongs[:pos - 1] + [items[0]] + wrongs[pos - 1:]
        q.choices = [c for c, _ in items]
        q.pos = q.choices.index(q.right) + 1
        q.others = {k: n for k, (c, n) in enumerate(items) if n is not None}
        counts[q.pos] += 1
        last.append(q.pos)
    return counts
