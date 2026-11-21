"""APAH 250 every-work practice (500 items) -> /study/ap/ap-art-history/tests/works-<k>/, one quiz per content area.

Source: source/works.json, extracted from apah-250-every-work-explained.pdf by extract.py (entries, questions, key).
Each explanation is the key's reason, the work's identification, the most relevant facts from the work's own entry
in the guide, and a note on every wrong choice (notes_<k>.py, written for this site). After answering, the work's
official photograph (the APAH page's cb/ images) is shown.
"""
import html
import importlib
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "source" / "works.json").read_text())
W = {int(k): v for k, v in D["works"].items()}
BASE = "/study/ap/ap-art-history/"
PDF = BASE + "apah-250-every-work-explained.pdf"
LET = "ABCD"
STOP = set("""a an the of in on at to for from by with and or but as is are was were be been it its this that these those which who
whom what when where why how not no only than then so such into onto over under about after before during while their there they
he she his her them we our you your i one two three four five many much more most other some any all each both
would could should may might can did does do has have had made make used use like also very""".split())


def esc(s):
    return html.escape(s, quote=False)


def words(s):
    return {w for w in re.findall(r"[a-z][a-z’'-]+", s.lower()) if w not in STOP and len(w) > 2}


def facts(e, q, ans, why):
    """The entry bullets that share the most content words with the question, its answer, and the key's reason."""
    target = words(q["prompt"] + " " + ans + " " + why)
    cands = [b for k in ("form", "function", "content", "context") for b in e["bullets"].get(k, [])]
    cands += [e[k] for k in ("plain", "spot", "remember") if e.get(k)]
    scored = sorted(((len(words(b) & target), -len(b), b) for b in cands), reverse=True)
    out = [b for s, _, b in scored if s >= 2 and b.rstrip(".") not in why][:2]
    return out


def ident(e):
    bits = [e.get("artist"), e.get("date"), e.get("medium")]
    return f"No. {e['n']}, <i>{esc(e['title'])}</i>: " + "; ".join(esc(b) for b in bits if b) + "."


def figure(e):
    return (f'<figure class="fig fig-after"><img class="photo" src="{BASE}cb/{e["n"]}-1.jpg" alt="{esc(e["title"])}, official photograph" '
            f'loading="lazy"><figcaption>No. {e["n"]}, {esc(e["title"])}</figcaption></figure>')


def quiz(k, area, lo, hi):
    notes = importlib.import_module(f"apah_works.notes_{k}").NOTES
    mc = []
    for q in D["questions"]:
        if not lo <= q["n"] <= hi:
            continue
        e = W[q["work"]]
        ans = LET.index(D["letters"][str(q["n"])])
        why = D["rows"][str(q["n"])]
        wrong = [i for i in range(4) if i != ans]
        note = notes[q["n"]]
        if len(note) != 3 or not all(note):
            raise SystemExit(f"Works area {k} item {q['n']}: need 3 notes")
        steps = [ident(e)] + ["From the guide: " + esc(f) for f in facts(e, q, q["choices"][ans], why)]
        mc.append(dict(n=q["n"], topic=str(e["n"]), tag=f"No. {e['n']}, {esc(e['title'])}", prompt=esc(q["prompt"]),
                       options=[esc(c) for c in q["choices"]], answer=ans, after=figure(e),
                       ex=dict(idea=esc(why), steps=steps, others={i: esc(t) for i, t in zip(wrong, note)})))
    works = sorted({q["work"] for q in D["questions"] if lo <= q["n"] <= hi})
    url = BASE + f"tests/works-{k}/"
    nav = " &middot; ".join((f"<b>{j}</b>" if j == k else f'<a href="{BASE}tests/works-{j}/">{j}</a>') for j, *_ in AREAS)
    cfg = dict(
        out="public" + url + "index.html", url=url, pdf=PDF, key=f"study.apah-works.{k}.v1",
        title=f"APAH 250 Practice {k}: {html.unescape(area)}", runhead="AP Art History &middot; The 250 required works &middot; Practice",
        back=("/study/#ap-art-history", "Study Library"), h1=esc(area), sub=f"APAH 250 &middot; Content area {k} of 10",
        metaline=f"{len(mc)} questions (Nos. {lo}&ndash;{hi}) &middot; two per work &middot; works {works[0]}&ndash;{works[-1]}",
        desc=f"AP Art History practice on the required works, {html.unescape(area)}: {len(mc)} questions, two per work, each explained with the guide's facts and why every wrong choice is wrong.",
        setupNote=f"Content areas: {nav}. Each answer shows the work&rsquo;s official photograph.",
        mc=mc, topics={str(n): (esc(W[n]["title"]), W[n]["page"]) for n in works}, topicPrefix="No. ", topicCol="Work",
        guideCol="Entry in the guide", byTopic="By work", topicNote="Two misses on one work: reread its entry in the guide.",
        guide=PDF, guideName="the guide",
        foot=(f'From <a href="{PDF}"><i>APAH 250: Every Required Work, Explained</i></a> (PDF), Section 12. Answers and reasons are the '
              "guide&rsquo;s own key; the explanations add the work&rsquo;s identification, the relevant facts from its entry, and why each "
              "wrong choice is wrong. Photographs as on this site&rsquo;s APAH page. Your answers are saved only in this browser."),
    )
    if k != 1:
        cfg["manifest"] = False
    return cfg


AREAS = [(int(k), name, int(lo), int(hi)) for k, name, lo, hi in D["sections"]]
QUIZZES = [quiz(*a) for a in AREAS if importlib.util.find_spec(f"apah_works.notes_{a[0]}") is not None]
