"""SAT Standard English Conventions, Practice Sets 1-10 -> /study/sat/conventions/tests/N/.

Items come from the series' own source (source/, copied from sat-conventions-latex-source.tar.gz).
arrange() reproduces the PDF's seeded order and letter positions exactly (checked against every PDF's
answer key when these quizzes were made). Explanations are in ex_setNN.py.
"""
import importlib
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "source"))
sys.path.insert(0, str(HERE.parent))
from model import RULES, SECTIONS  # noqa: E402
from sets_a import SET1, SET2, SET3, SET4, SET5  # noqa: E402
from sets_b import SET6, SET7, SET8, SET9, SET10  # noqa: E402
from lib.latex import to_html  # noqa: E402

SETS = [SET1, SET2, SET3, SET4, SET5, SET6, SET7, SET8, SET9, SET10]
GUIDE = "/study/sat/conventions/sat-conventions-00-guide.pdf"
# physical page of each rule's section in the guide PDF
GUIDE_PAGE = {"3.2": 5, "3.3": 6, "3.4": 6, "3.5": 7, "3.6": 7, "3.7": 8, "3.8": 8, "3.9": 9, "3.10": 9, "3.11": 10,
              "3.12": 10, "3.13": 11, "4.1": 12, "4.2": 13, "4.3": 13, "4.4": 14, "4.5": 15, "4.6": 16, "4.7": 16}
MACROS = {"IC": '<span class="sc">ic</span>', "DC": '<span class="sc">dc</span>'}
BLANK = '<span class="blank" role="img" aria-label="blank"></span>'
ASK = "Which choice completes the text so that it conforms to the conventions of Standard English?"


def arrange(n, items):
    """Copied from the series' build.py: seeded item order and answer positions."""
    rng = random.Random(1000 + n)
    order = list(range(20))
    if n >= 9:  # simulation sets: test order, no grouping
        rng.shuffle(order)
    positions = [0, 1, 2, 3] * 5
    while True:  # no letter more than twice in a row
        rng.shuffle(positions)
        if all(not (positions[i] == positions[i + 1] == positions[i + 2]) for i in range(18)):
            break
    out = []
    for k, idx in enumerate(order):
        q = items[idx]
        choices = list(q.wrong)
        choices.insert(positions[k], q.correct)
        out.append((idx, q, choices, positions[k]))
    return out


def h(s):
    return to_html(s, MACROS)


def match(key, wrong):
    """Exact wrong choice, else the unique one starting with key."""
    if key in wrong:
        return key
    hits = [w for w in wrong if w.startswith(key)]
    if len(hits) != 1:
        raise SystemExit(f"explanation key {key!r} matches {len(hits)} of {wrong}")
    return hits[0]


def quiz(n):
    items = SETS[n - 1]
    ex = importlib.import_module(f"sat_conventions.ex_set{n:02d}").EX
    assert len(ex) == len(items) == 20, n
    sim = n >= 9
    section_of = {}
    if not sim:
        for k, (_, a, b, _) in enumerate(SECTIONS, 1):
            for pos in range(a, b + 1):
                section_of[pos] = k
    mc = []
    for k, (idx, q, choices, ans) in enumerate(arrange(n, items), 1):
        e = ex[idx]
        if not q.correct.startswith(e["ans"]):
            raise SystemExit(f"Set {n} item {idx + 1}: explanation is for {e['ans']!r}, item answer is {q.correct!r}")
        mapped = {match(key, q.wrong): note for key, note in e["others"].items()}
        if set(mapped) != set(q.wrong):
            raise SystemExit(f"Set {n} item {idx + 1}: explanations missing for {set(q.wrong) - set(mapped)}")
        mc.append(dict(
            n=k, sec=section_of.get(k), topic=q.rule,
            prompt=h(q.stem.replace("___", "\x02")).replace("\x02", BLANK),
            options=[h(c) for c in choices], answer=ans,
            ex=dict(idea=e["idea"], steps=e["steps"],
                    others={choices.index(w): note for w, note in mapped.items()}),
        ))
    url = f"/study/sat/conventions/tests/{n}/"
    pdf = f"/study/sat/conventions/sat-conventions-{n:02d}-practice-set-{n}.pdf"
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.sat-conventions.{n}.v1",
        title=f"SAT Conventions Practice Set {n}",
        desc=f"Digital SAT Standard English Conventions, Practice Set {n}: 20 items with the rule behind each answer and why every wrong choice is wrong.",
        runhead=f"SAT Reading and Writing &middot; Standard English Conventions &middot; Practice Set {n}",
        back=("/study/#sat-conventions", "Study Library"),
        h1=f'Conventions Practice <span style="white-space:nowrap">Set {n}</span>',
        sub="Digital SAT &middot; Standard English Conventions",
        metaline="20 items (24 min)" + (" &middot; timed simulation in test order" if sim else " &middot; grouped by rule family"),
        setupNote=("Work it in one sitting, like the test: items are in test order with no headings. " if sim else "")
        + "Allow 24 minutes, about 72 seconds per item.",
        ask=ASK,
        sections={} if sim else {k: s[0] for k, s in enumerate(SECTIONS, 1)},
        topics={r: (h(RULES[r]), GUIDE_PAGE[r]) for r in sorted(RULES, key=lambda s: [int(x) for x in s.split(".")]) if r in GUIDE_PAGE},
        topicPrefix="§", topicCol="Rule", guideCol="Guide section", byTopic="By rule",
        topicNote="Two or more misses on one rule: reread that section of the guide, then redo those items.",
        guide=GUIDE, guideName="the <i>Conventions Guide</i>",
        foot=(f'From <a href="{pdf}"><i>Standard English Conventions on the Digital SAT: Practice Set {n}</i></a> (PDF). '
              "Answers and rule tags are the set&rsquo;s own key; the explanations expand on it with the rule, how it applies "
              "to the sentence, and why each wrong choice breaks a rule. Rule links open the matching section of "
              f'<a href="{GUIDE}"><i>the Conventions Guide</i></a>. Your answers are saved only in this browser.'),
        mc=mc,
    )


QUIZZES = [quiz(n) for n in range(1, 11)]
