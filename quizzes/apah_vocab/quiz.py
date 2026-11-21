"""APAH Vocabulary, Section 10 practice (754 items) -> /study/ap/ap-art-history/tests/vocab-<k>/, one quiz per category.

Source: source/vocab.json, extracted from apah-vocabulary.pdf by extract.py (glossary entries, questions, key).
Explanations are built from the glossary itself: the answer's full entry (definition, "Think of it as", "Seen in",
"See also") and each wrong choice's own definition. Prompts in the PDF hide the answer by writing "this" in its
place, which also broke words that contain the term ("thiss", "Stonethis"); those are repaired here as "these"
or a blank, never by restoring the hidden term.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "source" / "vocab.json").read_text())
BASE = "/study/ap/ap-art-history/"
PDF = BASE + "apah-vocabulary.pdf"
GLOSS_PAGE = {1: 3, 2: 13, 3: 24, 4: 38, 5: 59, 6: 71, 7: 91, 8: 102}  # glossary section for practice section k
LET = "ABCD"


def norm(s):
    return re.sub(r"\s+", " ", s.lower().replace("’", "'")).strip()


ENTRY = {norm(e["term"]): e for e in D["entries"].values()}


def esc(s):
    return html.escape(s, quote=False)


def fix_prompt(s):
    s = s.replace("shothis", "showing")
    s = re.sub(r"\b([Tt])his(?:s|es)\b", lambda m: "These" if m.group(1) == "T" else "these", s)
    s = re.sub(r"(?<=\w)this|this(?=\w)", "___", s)  # the hidden term inside a longer word
    s = re.sub(r"(^|[.?!] )(these|this)\b", lambda m: m.group(1) + m.group(2).capitalize(), s)
    return s


def first_sentences(s, limit=220):
    if len(s) <= limit:
        return s
    cut = s[:limit]
    i = max(cut.rfind(". "), cut.rfind("; "))
    return (cut[:i + 1] if i > 60 else cut.rsplit(" ", 1)[0] + "…").strip()


def explain(ans, wrong):
    e = ENTRY[norm(ans)]
    pron = f" ({esc(e['pron'])})" if e.get("pron") else ""
    idea = f"<b>{esc(e['term'])}</b>{pron}: {esc(e['def'])}"
    steps = []
    if e.get("think"):
        steps.append(esc(e["think"]) if e["think"].startswith("Think") else "Think of it as: " + esc(e["think"]))
    if e.get("seen"):
        steps.append("Seen in: " + esc(e["seen"].rstrip(".")) + ".")
    if e.get("see"):
        steps.append("Related terms: " + esc(e["see"].rstrip(".")) + ".")
    if not steps:
        steps.append("Match the key words of the definition to the term; the other choices come from the same category.")
    others = {}
    for i, w in wrong.items():
        we = ENTRY[norm(w)]
        others[i] = "means something else: " + esc(first_sentences(we["def"]))
    return dict(idea=idea, steps=steps, others=others)


def quiz(k, title, lo, hi):
    mc = []
    for q in D["questions"]:
        if not lo <= q["n"] <= hi:
            continue
        ans = LET.index(D["letters"][str(q["n"])])
        assert norm(D["rows"][str(q["n"])]).startswith(norm(q["choices"][ans]) + ":"), q["n"]
        wrong = {i: c for i, c in enumerate(q["choices"]) if i != ans}
        mc.append(dict(n=q["n"], topic=str(k), prompt=esc(fix_prompt(q["prompt"])), options=[esc(c) for c in q["choices"]],
                       answer=ans, ex=explain(q["choices"][ans], wrong)))
    url = BASE + f"tests/vocab-{k}/"
    nav = " &middot; ".join(
        (f"<b>{j}</b>" if j == k else f'<a href="{BASE}tests/vocab-{j}/">{j}</a>') for j, *_ in SECTIONS)
    cfg = dict(
        out="public" + url + "index.html", url=url, pdf=PDF, key=f"study.apah-vocab.{k}.v1",
        title=f"APAH Vocabulary {k}: {html.unescape(title)}", runhead="AP Art History &middot; Vocabulary &middot; Name the term",
        back=("/study/#ap-art-history", "Study Library"), h1=esc(title), sub=f"AP Art History Vocabulary &middot; Section {k} of 8",
        metaline=f"{len(mc)} questions (Nos. {lo}&ndash;{hi}) &middot; name the term from its definition",
        desc=f"AP Art History vocabulary practice, {html.unescape(title)}: {len(mc)} name-the-term questions, each explained with the glossary entry and what the wrong choices mean.",
        setupNote=f"Sections: {nav}. The wrong choices come from the same category, so they look plausible: match the definition’s key words.",
        ask="Which term does this define?",
        mc=mc, topics={str(k): (esc(title), GLOSS_PAGE[k])}, topicPrefix="Section ", topicCol="Section", guideCol="In the glossary",
        byTopic="Score", topicNote="Reread the glossary section for every term you missed, then retry the missed questions.",
        guide=PDF, guideName="the glossary",
        foot=(f'From <a href="{PDF}"><i>APAH Vocabulary: Every Term, Explained</i></a> (PDF), Section 10. Answers are the PDF&rsquo;s key; '
              "each explanation is the term&rsquo;s own glossary entry, plus what each wrong choice means. Your answers are saved only in this browser."),
    )
    if k != 1:
        cfg["manifest"] = False  # the /study row links Section 1, which links the rest
    return cfg


SECTIONS = [(int(k), name, int(lo), int(hi)) for k, name, lo, hi in D["sections"]]
QUIZZES = [quiz(k, name, lo, hi) for k, name, lo, hi in SECTIONS]
