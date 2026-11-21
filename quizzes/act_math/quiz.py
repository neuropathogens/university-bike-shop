"""ACT Math study guides and practice test -> /study/act/math/tests/<slug>/.

Transcribed from the PDFs (no source shipped). Each guide gNN.py defines DOC (metadata, rules with their
PDF page) and QS (questions, built with Q()). Answers and rule tags are the guide's own key; the in-depth
explanations are written here. Each module asserts its computed answers with plain Python.
Topic links open the rule's page in the same PDF (the guides state each rule before drilling it).
"""
import importlib

LET = "ABCD"
BASE = "/study/act/math/"
MODULES = ["g00", "g01", "g02", "g03", "g04", "g05", "g06", "g07", "g08"]


def Q(n, rule, prompt, options, answer, idea, steps, others, sec=None, fig=None, table=None):
    assert len(options) == 4 and answer in LET and set(others) == set(LET) - {answer}, n
    d = dict(n=n, topic=rule, prompt=prompt, options=options, answer=LET.index(answer),
             ex=dict(idea=idea, steps=steps, others={LET.index(k): v for k, v in others.items()}))
    if sec:
        d["sec"] = sec
    if fig:
        d["fig"] = fig
    if table:
        d["table"] = table
    return d


def quiz(mod):
    m = importlib.import_module(f"act_math.{mod}")
    D, qs = m.DOC, m.QS
    key = D["key"].split()
    assert len(key) == 2 * len(qs), (mod, len(key) // 2, len(qs))
    for q, (num, letter) in zip(qs, zip(key[::2], key[1::2])):
        assert int(num) == q["n"] and LET[q["answer"]] == letter, (mod, q["n"], letter)
    url = BASE + f"tests/{D['slug']}/"
    pdf = BASE + D["pdf"]
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.act-math.{D['slug']}.v1",
        title=f"ACT Math {D['title']}", desc=D["desc"],
        runhead=f"ACT Mathematics &middot; {D['title']}", back=("/study/#act-math", "Study Library"),
        h1=D["h1"], sub=D["sub"], metaline=D["metaline"], setupNote=D["setup"],
        mc=qs, sections=D.get("sections", {}), topics=D["rules"], topicPrefix="Rule ", topicCol="Rule",
        guideCol="Rule in the guide", byTopic="By rule", guide=D.get("guide", pdf),
        guideName=D.get("guideName", "the guide"),
        topicNote="For every miss, reread the rule named in the key, then redo the item.",
        foot=(f'From <a href="{pdf}"><i>ACT Math {D["title"]}</i></a> (PDF). Answers and rule tags are the guide&rsquo;s own key; '
              "the explanations expand on it with the rule, the worked solution, and why each wrong choice is wrong. "
              "Rule links open the page of the guide that states the rule. Your answers are saved only in this browser."),
        **({"target": D["target"]} if "target" in D else {}), **({"bands": D["bands"]} if "bands" in D else {}),
    )


import importlib.util  # noqa: E402

QUIZZES = [quiz(_m) for _m in MODULES if importlib.util.find_spec(f"act_math.{_m}") is not None]
