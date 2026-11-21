"""ACT English series, Parts 1-4 -> /study/act/english/tests/<part>/.

Items come from the series' own source (source/, copied from act-english-source.zip): numbering, choices,
answers and rule tags match the PDFs (whose letters alternate A-D / F-J by item number; the quiz numbers
choices 1-4 and keeps them in source order, NO CHANGE first). A passage section becomes one shared passage;
each item shows it with its own boxed number and underline highlighted. Explanations are in ex_<part>.py.
"""
import importlib
import importlib.util
import re

from act_english.source import conventions, language, practice_test, production
from act_english.source.model import CATS
from lib.latex import convert_text, to_html

BASE = "/study/act/english/"
PARTS = [  # (module, ex module, slug, pdf, rule-link pages {section key: page})
    (conventions, "ex_conventions", "1", "act-english-1-conventions.pdf",
     {"boundaries": 2, "semicolons": 3, "commas1": 4, "commas2": 5, "apostrophes": 5, "sva": 6, "tense": 7, "pronouns": 8,
      "modifiers": 9, "parallel": 9, "idioms": 10}),
    (production, "ex_production", "2", "act-english-2-production-of-writing.pdf",
     {"transitions": 2, "relevance": 4, "purpose": 5, "organization": 7, "cohesion": 8}),
    (language, "ex_language", "3", "act-english-3-knowledge-of-language.pdf",
     {"concision": 2, "diction": 3, "tone": 4, "combining": 5}),
    (practice_test, "ex_practice", "practice-section", "act-english-4-practice-section.pdf", {}),
]
PART_OF = {"POW": "2", "KLA": "3", "CSE": "1"}
CAT_GUIDE = {"POW": "act-english-2-production-of-writing.pdf", "KLA": "act-english-3-knowledge-of-language.pdf",
             "CSE": "act-english-1-conventions.pdf"}
DEFAULT_ASK = "Which choice is best? (NO CHANGE keeps the underlined portion.)"


def _ul(p):
    return '<u class="ul">' + convert_text(p.group(), p.macros) + "</u>"


def _qn(p):
    k = p.group()
    return f'<span class="qn" data-q="{k}">{k}</span>'


def _ulq(p):
    k, body = p.group(), p.group()
    return f'<u class="ul" data-q="{k}">' + convert_text(body, p.macros) + f'</u><span class="qn" data-q="{k}">{k}</span>'


MACROS = {"ul": _ul, "qnum": _qn, "ulq": _ulq, "sn": lambda p: "<b>[" + p.group() + "]</b>", "rightarrow": "→"}


def h(s):
    return to_html(s, MACROS)


def _close(s, i):
    """Index just past the } matching the { at s[i]."""
    depth = 0
    while i < len(s):
        if s[i] == "\\":
            i += 2
            continue
        depth += {"{": 1, "}": -1}.get(s[i], 0)
        i += 1
        if depth == 0:
            return i
    raise ValueError("unbalanced")


def mark(passage, start):
    """Replace each @@ with a boxed item number; an underline ending at the marker becomes that item's underline."""
    out, k, i, under = [], start, 0, {}
    while True:
        j = passage.find("@@", i)
        if j < 0:
            out.append(passage[i:])
            break
        seg = passage[i:j]
        u = seg.rfind("\\ul{")
        if u >= 0 and _close(seg, u + 3) == len(seg):
            under[k] = seg[u + 4:-1]
            out.append(seg[:u] + f"\\ulq{{{k}}}{{{under[k]}}}")
        else:
            out.append(seg + f"\\qnum{{{k}}}")
        k += 1
        i = j + 2
    return "".join(out), under


def passage_html(src):
    return "".join("<p>" + h(par) + "</p>" for par in re.split(r"\n\s*\n", src.strip()))


def match(key, choices):
    """Index of the wrong choice an explanation key names: exact if it ends in a newline, else the unique prefix."""
    if key.endswith("\n"):
        hits = [i for i, c in enumerate(choices) if c == key[:-1]]
    else:
        hits = [i for i, c in enumerate(choices) if c.startswith(key)]
    if len(hits) != 1:
        raise SystemExit(f"explanation key {key!r} matches {len(hits)} of {choices}")
    return hits[0]


def quiz(mod, exmod, slug, pdf, pages):
    g = mod.GUIDE
    EX = importlib.import_module(f"act_english.{exmod}").EX
    practice = g.subscores
    mc, sections, stims, topics, n = [], {}, {}, {}, 1
    num = {s.tag: str(i) for i, s in enumerate(g.sections, 1) if s.tag and s.key in pages}
    for s in g.sections:
        if not s.questions:
            continue
        sec = len(sections) + 1
        title = re.sub(r"\s+", " ", s.title)
        sections[sec] = h(title + (f": {s.passage_title}" if practice else ""))
        under = {}
        if s.passage:
            src, under = mark(s.passage, n)
            sid = f"p{sec}"
            stims[sid] = {"title": h(s.passage_title), "html": passage_html(src)}
        if not practice and s.tag in num:
            topics[num[s.tag]] = (h(s.tag), pages[s.key])
        for q in s.questions:
            idea, steps, others = EX[n]
            rule = q.rule or s.tag
            cat = q.cat or s.cat
            ask = q.stem or s.stem
            if s.passage:
                prompt = (f'<span class="sc">Underlined</span> <u class="ul">{h(under[n])}</u>' if n in under
                          else f'<span class="sc">At box</span> <span class="qn">{n}</span> in the passage')
                ask = ask or DEFAULT_ASK
            elif q.context:
                prompt = h(q.context)
            else:
                prompt, ask = ask, ""
            ix = {match(k, q.choices): note for k, note in others.items()}
            if set(ix) != set(range(4)) - {q.ans}:
                raise SystemExit(f"Part {slug} item {n}: notes for {sorted(ix)}, answer {q.ans}")
            d = dict(n=n, sec=sec, topic=PART_OF[cat] if practice else num.get(rule, rule), prompt=prompt, options=[h(c) for c in q.choices],
                     answer=q.ans, fixed=True, ex=dict(idea=idea, steps=steps, others=ix))
            if ask:
                d["ask"] = h(ask)
            if practice:
                d["tag"] = f"{CATS[cat]} &middot; {h(rule)}"
            elif q.rule and q.rule != s.tag:
                d["tag"] = h(q.rule)
            if s.passage:
                d["stim"] = f"p{sec}"
            mc.append(d)
            n += 1
    for q in mc:  # an override like "Transitions (punctuation)" links to its base rule's section
        if not practice and q["topic"] not in topics:
            base = [num[t] for t in num if q["topic"].startswith(t + " ")]
            if len(base) != 1:
                raise SystemExit(f"Part {slug} item {q['n']}: no section for rule {q['topic']!r}")
            q["topic"] = base[0]
    if practice:
        topics = {PART_OF[c]: (CATS[c], 1, BASE + CAT_GUIDE[c]) for c in ("POW", "KLA", "CSE")}
    url = BASE + f"tests/{slug}/"
    total = n - 1
    title = f"ACT English Part {g.slug[0]}: {g.title}" if not practice else "ACT English Full-Length Practice Section"
    cfg = dict(
        out="public" + url + "index.html", url=url, pdf=BASE + pdf, key=f"study.act-english.{slug}.v1",
        title=title, runhead=f"ACT English &middot; {g.short}", back=("/study/#act-english", "Study Library"),
        sub=f"ACT English &middot; Part {g.slug[0]}", mc=mc, sections=sections, stims=stims, topics=topics,
        foot=(f'From <a href="{BASE + pdf}"><i>ACT English Part {g.slug[0]}: {g.title}</i></a> (PDF). Answers and rule tags are the '
              "part&rsquo;s own key; the explanations expand on it with the rule, how it applies to the sentence, and why each "
              "wrong choice is wrong. Choices stay in the test&rsquo;s order (NO CHANGE first). Your answers are saved only in this browser."),
    )
    if practice:
        cfg.update(
            h1='Full-Length <span style="white-space:nowrap">Practice Section</span>',
            desc="ACT English full-length practice section: five passages and 50 questions with a worked explanation for every answer and a score by reporting category.",
            metaline=f"{total} questions &middot; 35 minutes &middot; five passages",
            setupNote="Set a 35-minute timer and use Exam mode for a real simulation (about 42 seconds per question). Answer every question: there is no penalty for guessing.",
            topicPrefix="Part ", topicCol="Review", guideCol="Reporting category", byTopic="By reporting category",
            topicNote="Tally your misses by category, then reread that part of the series and redo the items you missed. "
                      "ACT converts raw scores to the 1&ndash;36 scale with a different table for each form, so treat the raw score as a diagnostic.",
            guide=BASE + "act-english-0-overview.pdf", guideName="its part of the series",
            flag={"below": 0.7, "text": "below 70%: review this part"},
        )
    else:
        cfg.update(
            h1=h(g.title), desc=f"ACT English Part {g.slug[0]} ({g.title}): {total} ACT-format items with the rule behind each answer and why every wrong choice is wrong.",
            metaline=f"{total} ACT-format items &middot; grouped by rule, then a mixed passage",
            setupNote="Read the whole sentence, not just the underlined part; then check what changes between the choices.",
            topicPrefix="&sect;", topicCol="Section", guideCol="Rule", byTopic="By rule",
            topicNote="Two or more misses on one rule: reread that section of the guide, then redo those items.",
            guide=BASE + pdf, guideName="the guide",
        )
    return cfg


QUIZZES = [quiz(*p) for p in PARTS if importlib.util.find_spec(f"act_english.{p[1]}") is not None]
