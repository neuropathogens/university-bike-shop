"""AP Statistics Unit 6 Practice Sets B and C -> /study/ap/ap-statistics/tests/6b/, /6c/.

q_6b.py / q_6c.py hold the transcribed sets (TeX in $..$), ex_6b.py / ex_6c.py the in-depth MC explanations,
checks_6b.py / checks_6c.py assert every key answer and every distractor origin named in the explanations.
(Moved here from the original one-off builder; the localStorage keys are unchanged so saved progress survives.)
"""
import importlib

LET = "ABCD"
GUIDE = "/study/ap/ap-statistics/unit-6/ap-stats-unit-6-1-complete-guide.pdf"


def quiz(slug):
    Q = importlib.import_module(f"ap_stats.q_{slug}")
    EX = importlib.import_module(f"ap_stats.ex_{slug}").EX
    importlib.import_module(f"ap_stats.checks_{slug}")
    M = Q.META
    key = dict(__import__("re").findall(r"(\d+) ([A-D])", Q.ANSWERS_ONLY))
    mc = []
    for q in Q.MC:
        assert key[str(q["n"])] == q["answer"], q["n"]
        e = EX[q["n"]]
        mc.append(dict(n=q["n"], sec=q["sec"], topic=q["topic"], fixed=bool(q.get("fixed")), prompt=q["prompt"],
                       table=q.get("table", ""), options=list(q["options"]), answer=LET.index(q["answer"]),
                       ex=dict(idea=e["idea"], steps=list(e["steps"]), others={LET.index(k): v for k, v in e["others"].items()})))
    fr = []
    for f in Q.FR:
        multi = "&ndash;" in f["topics"]
        fr.append(dict(n=f["n"], mode="epi", head=f"Topic{'s' if multi else ''} {f['topics']} &middot; scored 0&ndash;4",
                       guide=list(f["guide"]), stem=f["stem"],
                       parts=[dict(label=p["label"], prompt=p["prompt"], solution=p["solution"], e=p["e"], p=p["p"]) for p in f["parts"]]))
    url = f"/study/ap/ap-statistics/tests/{slug}/"
    letter = M["set"]
    return dict(
        out="public" + url + "index.html", url=url, pdf=M["pdf"], key=M["key"], fkey=M["fkey"],
        title=f"Unit 6 Practice Set {letter}",
        desc="AP Statistics Unit 6 (sampling distributions, topics 6.1–6.7): 18 multiple-choice questions with explanations and two free-response questions with model solutions and scoring guidelines.",
        runhead=f"AP Statistics &middot; Unit 6 Practice Set {letter}", back=("/study/#ap-statistics", "Study Library"),
        h1=f'Unit 6 Practice <span style="white-space:nowrap">Set {letter}</span>', sub="Sampling distributions &middot; topics 6.1&ndash;6.7",
        metaline="18 multiple-choice questions (40 min) &middot; 2 free-response questions (25 min)",
        setupNote="Allow 40 minutes and keep a calculator handy.",
        mc=mc, fr=fr, sections=Q.SECTIONS, topics={t: (v[0], v[2]) for t, v in Q.TOPICS.items()},
        topicPrefix="Topic ", topicCol="Topic", guideCol="Guide section", byTopic="By topic", topicNote=M["topicNote"],
        guide=GUIDE, guideName="the <i>Unit 6 Complete Guide</i>",
        composite=dict(mcWeight=50, frWeight=50, bands=[[80, "Ready for the Chapter 6 test."], [60, M["bandMid"]], [0, M["bandLow"]]]),
        frIntro="Allow 25 minutes. Show all work. Name each distribution with its parameters, and write calculator inputs with labels. Then open the model solution and mark each part essentially correct (E), partially correct (P), or incorrect (I).",
        foot=(f'From <a href="{M["pdf"]}"><i>Unit 6 Practice Set {letter}</i></a> (PDF). Answers, free-response model solutions and scoring guidelines are the set&rsquo;s own key; '
              "the multiple-choice explanations expand on it with the full working and why each wrong choice is wrong. "
              f'Topic links open the matching section of <a href="{GUIDE}"><i>Unit 6 Complete Guide</i></a>. '
              'Use a calculator (<span style="white-space:nowrap">TI-84</span>). Your answers, drafts and scores are saved only in this browser.'),
    )


QUIZZES = [quiz("6b"), quiz("6c")]
