"""AP Physics C (Mechanics Units 1-7, E&M Units 8-13) -> /study/ap/ap-physics-c/tests/<slug>/.

  unit-N          the unit's Question Set: multiple choice + one free-response question scored in points
  unit-N-checks   the check questions at the end of each section of the unit's Study Guide

Items come from the same content model that writes the PDFs (uNN.py, see model.py), so choices, letters and
the key match the PDFs. Run texgen.py first: it records each guide section's page in pages.json.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ROOT))
from lib.latex import to_html  # noqa: E402
from ap_physics_c.model import place  # noqa: E402
from ap_physics_c.texgen import units, COURSE_DIR  # noqa: E402

BASE = "/study/ap/ap-physics-c/"
PAGES = json.load(open(os.path.join(ROOT, "pages.json")))


def h(s):
    return to_html(s)


def tabular_html(tex):
    """booktabs \\begin{tabular} -> booktabs-style HTML table (first row is the header)."""
    i = tex.index("\\begin{tabular}") + len("\\begin{tabular}")
    depth = 0
    for j in range(i, len(tex)):  # skip the brace-balanced column spec
        depth += {"{": 1, "}": -1}.get(tex[j], 0)
        if depth == 0:
            break
    body = tex[j + 1:tex.index("\\end{tabular}")]
    body = re.sub(r"\\(toprule|bottomrule|midrule)", "", body)
    rows = [[h(c.strip()) for c in r.split("&")] for r in re.split(r"\\\\", body) if r.strip()]
    head = "".join(f'<th scope="col">{c}</th>' for c in rows[0])
    trs = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows[1:])
    return f'<div class="bt-wrap"><table class="bt"><thead><tr>{head}</tr></thead><tbody>{trs}</tbody></table></div>'


def stem_html(tex):
    """FRQ stem: paragraphs plus an optional data table."""
    out = []
    for i, piece in enumerate(re.split(r"(\\begin\{tabular\}.*?\\end\{tabular\})", tex, flags=re.S)):
        if i % 2:
            out.append(tabular_html(piece))
            continue
        for para in re.split(r"\n\s*\n|\\medskip", piece):
            if para.strip():
                out.append("<p>" + h(para.strip()) + "</p>")
    return "".join(out)


def item(n, q, sec, topic_of):
    return dict(n=n, sec=sec, topic=topic_of[q.topic], tag=h(q.tag), prompt=h(q.stem), options=[h(c) for c in q.choices],
                answer=q.pos - 1, ex=dict(idea=h(q.why), steps=[h(s) for s in q.steps], others={k: h(v) for k, v in q.others.items()}))


def build(u, kind):
    course = "Mechanics" if u.course == "mech" else "E&amp;M"
    folder = BASE + COURSE_DIR[u.course] + "/"
    guide = folder + u.stem + "-guide.pdf"
    pdf = folder + u.stem + f"-{kind}.pdf"
    pages = PAGES[str(u.n)]
    topic_of = {}
    topics = {}
    for k, s in enumerate(u.sections, 1):
        m = re.match(r"(.*?)\s*\(([^)]*)\)$", s.title)
        key = h(m.group(2))
        topics[key] = (h(m.group(1)), pages[str(k)])
        for t in s.topics:
            topic_of[t] = key
    sections, mc = {}, []
    if kind == "questions":
        qs = [q for _, sq in u.qsections for q in sq]
        place(qs)
        n = 0
        for si, (title, sq) in enumerate(u.qsections, 1):
            sections[si] = h(title)
            for q in sq:
                n += 1
                mc.append(item(n, q, si, topic_of))
    else:
        qs = [q for s in u.sections for q in s.checks]
        place(qs)
        n = 0
        for si, s in enumerate(u.sections, 1):
            if not s.checks:
                continue
            sections[si] = h(s.title)
            for q in s.checks:
                n += 1
                mc.append(item(n, q, si, topic_of))
    used = {q["topic"] for q in mc}
    topics = {k: v for k, v in topics.items() if k in used}
    uname = f"Unit {u.n}: {u.title}"
    plain = f"AP Physics C: {'Mechanics' if u.course == 'mech' else 'E&M'} Unit {u.n}"
    z = dict(back=("/study/#ap-physics-c-" + ("mechanics" if u.course == "mech" else "em"), "Study Library"), pdf=pdf, mc=mc, sections=sections, topics=topics,
             topicPrefix="", topicCol="Topic", guideCol="Guide section", byTopic="By topic",
             topicNote="Two or more misses on one topic: reread that section of the guide.",
             guide=guide, guideName=f"the <i>Unit {u.n} guide</i>")
    if kind == "questions":
        f = u.frq
        parts = [dict(label=p.label, max=p.pts, prompt=h(p.prompt), solution="<p>" + h(p.solution) + "</p>",
                      rubric=f"<p><b>Common miss:</b> {h(p.miss)}</p><p>Worth {p.pts} point{'s' if p.pts > 1 else ''}. "
                             "Give yourself the points only where your answer does what the model does.</p>") for p in u.frq.parts]
        url = BASE + f"tests/unit-{u.n}/"
        z.update(title=f"{plain} Question Set", h1=f'Unit {u.n} <span style="white-space:nowrap">Question Set</span>', sub=h(u.title),
                 metaline=f"{len(mc)} multiple-choice (about {2 * len(mc)} min) &middot; 1 free response, {f.pts} points ({f.mins} min)",
                 setupNote="Allow about 2 minutes per question, the exam&rsquo;s pace. Keep the AP equation sheet and a calculator at hand.",
                 desc=f"{plain} ({u.title}) question set: {len(mc)} exam-style multiple-choice questions with worked explanations, plus {'an' if str(f.pts).startswith(('8', '11', '18')) else 'a'} {f.pts}-point {f.kind.lower()} free-response question with a scoring guide.",
                 fr=[dict(n=1, mode="points", kind=f.kind, mins=f.mins, head=f"{f.kind} &middot; {f.pts} points &middot; {f.mins} minutes",
                          guide=[], stem=stem_html(f.stem), parts=parts)],
                 frIntro=f"Allow {f.mins} minutes. Work each part on paper, then open the model solution and give yourself the points your answer earns.",
                 target=dict(label="Target", mc=round(len(mc) * 0.7)),
                 key=f"study.ap-physc.unit-{u.n}.v1", runhead=f"AP Physics C: {course} &middot; {h(uname)} &middot; Question Set")
        doc = f"{uname}: Question Set"
    else:
        url = BASE + f"tests/unit-{u.n}-checks/"
        z.update(title=f"{plain} Guide Checks", h1=f'Unit {u.n} <span style="white-space:nowrap">Guide Checks</span>', sub=h(u.title),
                 metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"{plain} ({u.title}): the study guide's {len(mc)} section check questions as a quiz, with worked explanations.",
                 key=f"study.ap-physc.unit-{u.n}-checks.v1", runhead=f"AP Physics C: {course} &middot; {h(uname)} &middot; Guide checks")
        doc = f"{uname}"
    z.update(url=url, out="public" + url + "index.html",
             foot=(f'From <a href="{pdf}"><i>{h(doc)}</i></a> (PDF). Answers and topic tags are the document&rsquo;s own key; '
                   "the explanations work each problem and say why each wrong choice is wrong. "
                   f'Topic links open the matching section of <a href="{guide}">the guide</a>. Your answers are saved only in this browser.'))
    return z


QUIZZES = [build(u, k) for u in units() for k in ("questions", "guide")]
