"""AP Calculus BC: unit practice sets 1-10 and the full practice exam -> /study/ap/ap-calculus-bc/tests/<slug>/.

The items live in sets/uNN.py and sets/exam.py (one source for the PDFs and the quizzes; see model.py and
build_pdfs.py). Each module asserts its computed answers with plain Python or SymPy. Topic links open the
section of the unit's study guide at the page recorded in pages.json (written by build_pdfs.py).
"""
import importlib
import json
from pathlib import Path

from ap_calc_bc.model import BASE, LET, Table, check_letters, fig_html, to_html

HERE = Path(__file__).resolve().parent
PAGES = json.loads((HERE / "pages.json").read_text()) if (HERE / "pages.json").exists() else {}
UNITS = [f"u{i:02d}" for i in range(1, 11)]


def _extras(q):
    out = ""
    if q.get("fig"):
        out += fig_html(q["fig"])
    return out


def _table(q):
    t = q.get("table")
    return t.html() if isinstance(t, Table) else ""


def mc_item(q, sec_key):
    prompt = to_html(q["prompt"])
    d = dict(n=q["n"], sec=sec_key, topic=q["topic"], tag=q["rule"], prompt=prompt,
             options=[to_html(o) for o in q["options"]], answer=LET.index(q["answer"]),
             ex=dict(idea=to_html(q["idea"]), steps=[to_html(s) for s in q["steps"]],
                     others={LET.index(k): to_html(v) for k, v in q["others"].items()}))
    if q.get("fig"):
        d["fig"] = _extras(q)
    if q.get("table"):
        d["table"] = _table(q)
    return d


def fr_item(f, guide_topics):
    parts = []
    for p in f["parts"]:
        sol = "".join(f"<p>{to_html(s)}</p>" for s in p["solution"])
        rub = "<p><b>Scoring.</b></p><ul>" + "".join(f"<li>1 point: {to_html(r)}</li>" for r in p["rubric"]) + "</ul>"
        parts.append(dict(label=p["label"], max=len(p["rubric"]), prompt=" " + to_html(p["prompt"]), solution=sol, rubric=rub))
    stem = to_html(f["stem"])
    if f.get("fig"):
        stem += fig_html(f["fig"])
    if f.get("table"):
        stem += f["table"].html()
    head = f"{to_html(f['title'])} &middot; {f['pts']} points &middot; {'calculator required' if f['calc'] else 'no calculator'}"
    return dict(n=f["n"], mode="points", head=head, stem=stem, parts=parts, guide=guide_topics)


def unit_quiz(mod):
    m = importlib.import_module(f"ap_calc_bc.sets.{mod}")
    D, qs, frs = m.DOC, m.QS, m.FRS
    check_letters(qs, mod)
    assert all(f["pts"] == 9 for f in frs), mod
    u = D["unit"]
    guide_pdf = BASE + D["guide_pdf"]
    pages = PAGES.get(D["guide_pdf"], {})
    topics = {s: (t, pages.get(s, 1)) for s, t in D["sections"].items()}
    for q in qs:
        q["topic"] = q["sec"]
    url = BASE + f"tests/unit-{u}/"
    pdf = BASE + D["pdf"]
    nmc, npts = len(qs), sum(f["pts"] for f in frs)
    mc = [mc_item(q, "2" if q["calc"] else "1") for q in qs]
    fr = [fr_item(f, f["secs"]) for f in frs]
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-calc-bc.unit-{u}.v1",
        title=f"AP Calculus BC Unit {u} Practice Set: {D['title']}",
        desc=f"AP Calculus BC Unit {u}, {D['title']}: {nmc} multiple-choice questions with worked solutions and a {npts}-point free-response question with a scoring guide.",
        runhead=f"AP Calculus BC &middot; Unit {u} Practice Set", back=("/study/#ap-calculus-bc", "Study Library"),
        h1=f'Unit {u} Practice <span style="white-space:nowrap">Set</span>', sub=f"{to_html(D['title'])} &middot; topics {D['topics']}",
        metaline=f"{nmc} multiple-choice questions &middot; 1 free-response question ({npts} points)",
        setupNote=D["setup"], mc=mc, fr=fr, sections={"1": "No calculator", "2": "Calculator active"},
        topics=topics, topicPrefix="&sect;", topicCol="Guide section", guideCol="In the guide", byTopic="By section",
        guide=guide_pdf, guideName=f"the <i>Unit {u} Study Guide</i>",
        topicNote="Two or more misses in one section: reread its rule boxes and worked example, then redo those items.",
        composite=dict(mcWeight=nmc, frWeight=npts, bands=[]),
        frIntro="Work the question on paper with full justification, as on the exam. Then open the model solution and give yourself each point the scoring guide awards.",
        foot=(f'From <a href="{pdf}"><i>Unit {u} Practice Set</i></a> (PDF). Answers, rule tags and the free-response scoring guide are the set&rsquo;s own key; '
              "the explanations add the worked solution and why each wrong choice fails. "
              f'Section links open the matching page of the <a href="{guide_pdf}"><i>Unit {u} Study Guide</i></a>. Your answers are saved only in this browser.'),
    )


def exam_quiz():
    m = importlib.import_module("ap_calc_bc.sets.exam")
    D, qs, frs = m.DOC, m.QS, m.FRS
    check_letters(qs, "exam")
    guides = {}
    for mod in UNITS:
        um = importlib.import_module(f"ap_calc_bc.sets.{mod}")
        guides[str(um.DOC["unit"])] = (um.DOC["title"], 1, BASE + um.DOC["guide_pdf"])
    for q in qs:
        q["topic"] = q["sec"]  # in the exam, sec is the unit number
    url = BASE + "tests/practice-exam/"
    pdf = BASE + D["pdf"]
    mc = [mc_item(q, "2" if q["calc"] else "1") for q in qs]
    fr = [fr_item(f, f["secs"]) for f in frs]
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key="study.ap-calc-bc.practice-exam.v1",
        title="AP Calculus BC Full Practice Exam",
        desc="A full-length AP Calculus BC practice exam in the May 2027 format: 42 multiple-choice questions (29 no calculator, 13 calculator) and 6 free-response questions, with worked solutions, scoring guides and an estimated AP score.",
        runhead="AP Calculus BC &middot; Full Practice Exam", back=("/study/#ap-calculus-bc", "Study Library"),
        h1='Full Practice <span style="white-space:nowrap">Exam</span>', sub="AP Calculus BC &middot; May 2027 format",
        metaline="42 multiple choice (Part A: 29, no calculator, 62 min; Part B: 13, calculator, 38 min) &middot; 6 free response (54 points, 90 min)",
        setupNote=D["setup"], mc=mc, fr=fr, sections={"1": "Part A &middot; no calculator", "2": "Part B &middot; calculator required"},
        topics=guides, topicPrefix="Unit ", topicCol="Unit", guideCol="Study guide", byTopic="By unit",
        guide=BASE + "ap-calc-bc-00-exam-guide.pdf", guideName="the unit study guides",
        flag=dict(below=0.6, text="review this unit&rsquo;s guide"),
        topicNote="Units under 60%: reread that unit&rsquo;s study guide, then redo its practice set.",
        composite=dict(mcWeight=54, frWeight=54, bands=[
            [68, "Estimated AP score: 5. (Cut scores change every year; treat this as a rough guide.)"],
            [52, "Estimated AP score: 4. (Cut scores change every year.)"],
            [40, "Estimated AP score: 3. (Cut scores change every year.)"],
            [29, "Estimated AP score: 2."], [0, "Estimated AP score: 1."]]),
        frIntro="Section II: Part A (questions 1&ndash;2, calculator required, 30 minutes) and Part B (questions 3&ndash;6, no calculator, 60 minutes). Write on paper with full justification, then open each model solution and award yourself the points the scoring guide allows.",
        foot=(f'From <a href="{pdf}"><i>AP Calculus BC Full Practice Exam</i></a> (PDF). Answers and scoring guides are the exam&rsquo;s own key; '
              "the explanations add the worked solution and why each wrong choice fails. The composite weights the two sections equally, as the real exam does; "
              "the score bands are estimates. Unit links open that unit&rsquo;s study guide. Your answers are saved only in this browser."),
    )


def _available(mod):
    return importlib.util.find_spec(f"ap_calc_bc.sets.{mod}") is not None


import importlib.util  # noqa: E402

QUIZZES = [unit_quiz(_m) for _m in UNITS if _available(_m)] + ([exam_quiz()] if _available("exam") else [])
