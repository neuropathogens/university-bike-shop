"""College math study guides (differential equations, linear algebra, multivariable calculus, real analysis)
-> /study/math/<subject>/tests/<slug>/.

Transcribed from the PDFs (no source exists). Each module defines DOC (metadata; `rules` maps a section number to
(title, page) in the PDF) and QS (questions built with Q()). Answers and rule tags are the document's own key, which
quiz() checks against DOC["key"]; the in-depth explanations are written here. Modules assert computed answers in
plain Python where a computation decides the item.
"""
import importlib
import importlib.util

LET = "ABCD"
MODULES = ["de1", "de2", "de3", "la", "mvc", "ra1", "ra2", "ra3"]
SUBJECT = {"de": ("differential-equations", "Differential Equations"), "la": ("linear-algebra", "Linear Algebra"),
           "mvc": ("multivariable-calculus", "Multivariable Calculus"), "ra": ("real-analysis", "Real Analysis")}


def Q(n, sec, rule, prompt, options, answer, idea, steps, others, fig=None, table=None):
    letters = LET[:len(options)]
    assert answer in letters and set(others) == set(letters) - {answer}, n
    d = dict(n=n, topic=str(sec), tag=rule, prompt=prompt, options=options, answer=letters.index(answer),
             ex=dict(idea=idea, steps=steps, others={letters.index(k): v for k, v in others.items()}))
    if fig:
        d["fig"] = fig
    if table:
        d["table"] = table
    return d


def FRQ(n, sec, rule, prompt, answer, steps, pts=1, lead="Answer", rubric=None, ask="Your solution and final answer."):
    """A free-response item (marked "fr" in the PDF): problem, model answer from the key, and the worked steps."""
    sol = f"<p><b>{lead}.</b> {answer}</p><ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>"
    rubric = rubric or (f"<p>{pts} point{'s' if pts > 1 else ''} if your final answer matches and your work shows the decisive steps above; "
                        "0 if the method or the answer is wrong.</p>")
    return dict(n=n, mode="points", head=f"{rule} &middot; {pts} point{'s' if pts > 1 else ''}", stem=prompt,
                parts=[dict(label="a", max=pts, prompt=ask, solution=sol, rubric=rubric)],
                guide=[str(sec)])


def quiz(mod):
    m = importlib.import_module(f"college_math.{mod}")
    D, qs, frs = m.DOC, m.QS, getattr(m, "FRS", [])
    key = D["key"].split()
    assert len(key) == 2 * len(qs), (mod, len(key) // 2, len(qs))
    for q, (num, letter) in zip(qs, zip(key[::2], key[1::2])):
        assert int(num) == q["n"] and LET[q["answer"]] == letter, (mod, q["n"], letter)
    folder, subject = SUBJECT[mod.rstrip("0123456789")]
    base = f"/study/math/{folder}/"
    rules = D["rules"]
    if D.get("rules_pdf"):  # topics link to the study-guide volume that states the rules
        rules = {k: (v[0], v[1], base + D["rules_pdf"] + f"#page={v[1]}") for k, v in rules.items()}
    url = base + f"tests/{D['slug']}/"
    pdf = base + D["pdf"]
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.{folder}.{D['slug']}.v1",
        title=f"{subject}: {D['title']}", desc=D["desc"], runhead=f"{subject} &middot; {D['title']}",
        back=(f"/study/#{folder}", "Study Library"), h1=D["h1"], sub=D["sub"], metaline=D["metaline"], setupNote=D["setup"],
        mc=qs, topics=rules, topicPrefix="&sect;", topicCol="Section", guideCol="In the guide", byTopic="By section",
        guide=D.get("guide", pdf), guideName=D.get("guideName", "the guide"),
        topicNote="Two or more misses in one section: reread its rule boxes, then redo those items.",
        foot=(f'From <a href="{pdf}"><i>{subject}: {D["title"]}</i></a> (PDF). Answers and rule tags are the document&rsquo;s own key; '
              "the explanations expand on it with the rule, a worked solution, and why each wrong choice fails. "
              "Section links open the page of the guide that states the rules. Your answers are saved only in this browser."),
        **({"frWord": D["frWord"]} if D.get("frWord") else {}),
        **({"fr": frs, "frIntro": D.get("frIntro", "Free-response items: work each one on paper, then open the model solution and mark yourself."),
            **({"composite": {"mcWeight": len(qs), "frWeight": sum(p["max"] for f in frs for p in f["parts"]), "bands": []}} if qs else {})}
           if frs else {}),
    )


QUIZZES = [quiz(_m) for _m in MODULES if importlib.util.find_spec(f"college_math.{_m}") is not None]
