"""Content model for the AP science study series (one source for the PDFs and the quiz pages).

Generalized from ap_physics_c/model.py. Each course family (ap_physics_1, ap_physics_2, ap_biology, ap_env_sci)
has one module per unit (uNN.py) defining UNIT = Unit(...). Text is LaTeX: $..$ math (KaTeX-safe, no custom
macros), \\textbf, \\emph, --, ``quotes''. The same strings go into the .tex files and, converted with
lib/latex.py, into the quiz pages, so the PDF and the quiz cannot drift apart.

    Q(tag, stem, right, [wrong1, wrong2, wrong3], why, steps, [note1, note2, note3], sort=False, fig=None)

`right` is written first; the generator places it (balancing A-D within each document) or, with sort=True,
orders numeric choices by value. `notes` explain each wrong choice, in the order the wrong choices are
written. `tag` starts with the CED topic number ("2.5 Newton's second law"). `fig` is a figs.Graph drawn
after the stem. A question set is a list of Set(title, qs, stim=None, fig=None, stim_title=None): `stim` is
shared stimulus text (paragraphs and at most one booktabs tabular) printed before the set's questions.
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
    fig: object = None
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
    kind: str        # the course's free-response type, e.g. "Mathematical Routines" or "Analyze Data"
    pts: int
    stem: str
    parts: list
    mins: int = 24
    fig: object = None   # figs.Graph; placed where the stem has [[fig]], else after the stem


@dataclass
class Sec:
    title: str       # "Newton's second law (2.5)"
    topics: list     # ["2.5"]
    body: str
    checks: list = field(default_factory=list)


@dataclass
class Set:
    title: str       # "Newton's laws (2.3--2.5)"
    qs: list
    stim: str = None
    fig: object = None
    stim_title: str = None


@dataclass
class Unit:
    n: int
    slug: str
    title: str
    weight: str      # "10--15\\%"
    topics: str      # "1.1--1.5"
    abstract: str
    sections: list
    qsections: list  # [Set(...)] or [(title, [Q...])]
    frq: FRQ
    frq_topic: str = ""   # one line for the /study row, e.g. "a block on an incline with drag"
    prefix: str = ""      # set by the course: "ap-phys1-"

    def __post_init__(self):
        self.qsections = [s if isinstance(s, Set) else Set(*s) for s in self.qsections]

    @property
    def stem(self):
        return f"{self.prefix}{self.n:02d}-{self.slug}"

    @property
    def questions(self):
        return [q for s in self.qsections for q in s.qs]

    @property
    def checks(self):
        return [q for s in self.sections for q in s.checks]


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
