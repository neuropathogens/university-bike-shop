"""A course's quiz pages: /study/ap/<slug>/tests/unit-N/ (question set) and tests/unit-N-checks/ (guide checks).

Items come from the same unit modules that write the PDFs, so choices, letters and the key match. Run the
course's build_tex.py first: it records each guide section's page in pages.json (used by the topic links).
"""
import json
import os
import re

from lib.latex import to_html
from ap_sci import figs
from ap_sci.model import place


MAX_CHUNK = 28   # widest unbreakable run of inline math (in characters) that still fits a 320 px screen


def _chunk_width(m):
    """KaTeX breaks inline math only after top-level relations and binary operators; measure the widest run between them."""
    out, depth, cur, i = [], 0, "", 0
    while i < len(m):
        ch = m[i]
        depth += {"{": 1, "}": -1}.get(ch, 0)
        cur += ch
        if depth == 0:
            for op in ("=", "+", "-", "\\times", "\\approx", "<", ">", "\\cdot"):
                if m.startswith(op, i) and (op != "-" or cur.strip() != "-"):
                    cur += m[i + 1:i + len(op)]
                    i += len(op) - 1
                    out.append(cur)
                    cur = ""
                    break
        i += 1
    out.append(cur)

    def vis(s):
        s = re.sub(r"\\(times|cdot)", "x", s)
        s = re.sub(r"\\(sqrt|dfrac|tfrac|frac|mathrm|text|left|right|mathcal|vec|,|;|!)", "", s)
        s = re.sub(r"\\[A-Za-z]+", "x", s.replace("\\ ", " "))
        return len(re.sub(r"[{}^_\s]", "", s))
    return max(vis(c) for c in out)


def h(s):
    for m in re.finditer(r"(?<!\\)\$(.+?)(?<!\\)\$", s):
        if _chunk_width(m.group(1)) > MAX_CHUNK:
            raise SystemExit(f"inline math too wide for a phone screen; split it: ${m.group(1)}$")
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
    body = re.sub(r"\\(toprule|bottomrule|midrule)|\\cmidrule(\([^)]*\))?\{[^}]*\}", "", body)
    rows = [[h(c.strip()) for c in r.split("&")] for r in re.split(r"\\\\", body) if r.strip()]
    head = "".join(f'<th scope="col">{c}</th>' for c in rows[0])
    trs = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows[1:])
    return f'<div class="bt-wrap"><table class="bt"><thead><tr>{head}</tr></thead><tbody>{trs}</tbody></table></div>'


def blocks_html(tex, fig=None):
    """Paragraphs, booktabs tables and an optional graph (at [[fig]], else at the end)."""
    out = []
    tex = tex or ""
    if fig is not None and "[[fig]]" not in tex:
        tex = tex + "\n\n[[fig]]"
    for i, piece in enumerate(re.split(r"(\\begin\{tabular\}.*?\\end\{tabular\}|\[\[fig\]\])", tex, flags=re.S)):
        if piece == "[[fig]]":
            out.append(figs.svg(fig))
        elif i % 2:
            out.append(tabular_html(piece))
        else:
            for para in re.split(r"\n\s*\n|\\medskip|\\smallskip|\\bigskip", piece):
                if para.strip():
                    out.append("<p>" + h(para.strip()) + "</p>")
    return "".join(out)


def item(n, q, sec, topic_of, stim=None):
    d = dict(n=n, sec=sec, topic=topic_of[q.topic], tag=h(q.tag), prompt=h(q.stem), options=[h(c) for c in q.choices],
             answer=q.pos - 1, ex=dict(idea=h(q.why), steps=[h(s) for s in q.steps], others={k: h(v) for k, v in q.others.items()}))
    if q.fig:
        d["fig"] = figs.svg(q.fig)
    if stim:
        d["stim"] = stim
    return {k: v for k, v in d.items() if v is not None}


def build(C, u, kind, pages):
    base = f"/study/ap/{C.slug}/"
    guide = base + u.stem + "-guide.pdf"
    pdf = base + u.stem + f"-{kind}.pdf"
    pg = pages[str(u.n)]
    topic_of, topics = {}, {}
    for k, s in enumerate(u.sections, 1):
        m = re.match(r"(.*?)\s*\(([^)]*)\)$", s.title)
        key = h(m.group(2))
        topics[key] = (h(m.group(1)), pg[str(k)])
        for t in s.topics:
            topic_of[t] = key
    sections, mc, stims = {}, [], {}
    n = 0
    if kind == "questions":
        place(u.questions)
        for si, s in enumerate(u.qsections, 1):
            sections[si] = h(s.title)
            key = None
            if s.stim or s.fig:
                key = f"s{si}"
                stims[key] = dict(title=h(s.stim_title or s.title), html=blocks_html(s.stim, s.fig), cls="free")
            for q in s.qs:
                n += 1
                mc.append(item(n, q, si, topic_of, key))
    else:
        place(u.checks)
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
    plain = f"{C.short} Unit {u.n}"
    z = dict(back=(f"/study/#{C.slug}", "Study Library"), pdf=pdf, mc=mc, sections=sections, topics=topics, stims=stims,
             topicPrefix="", topicCol="Topic", guideCol="Guide section", byTopic="By topic",
             topicNote="Two or more misses on one topic: reread that section of the guide.",
             guide=guide, guideName=f"the <i>Unit {u.n} guide</i>")
    if kind == "questions":
        f = u.frq
        parts = [dict(label=p.label, max=p.pts, prompt=h(p.prompt), solution="<p>" + h(p.solution) + "</p>" + (figs.svg(p.fig) if p.fig else ""),
                      rubric=f"<p><b>Common miss:</b> {h(p.miss)}</p><p>Worth {p.pts} point{'s' if p.pts > 1 else ''}. "
                             "Give yourself the points only where your answer does what the model does.</p>") for p in f.parts]
        url = base + f"tests/unit-{u.n}/"
        mins = round(C.pace * len(mc))
        art = "an" if str(f.pts).startswith(("8", "11", "18")) else "a"
        z.update(title=f"{plain} Question Set", h1=f'Unit {u.n} <span style="white-space:nowrap">Question Set</span>', sub=h(u.title),
                 metaline=f"{len(mc)} multiple-choice (about {mins} min) &middot; 1 free response, {f.pts} points ({f.mins} min)",
                 setupNote=C.setup,
                 desc=f"{plain} ({u.title.replace('--', '–')}) question set: {len(mc)} exam-style multiple-choice questions with worked explanations, plus {art} {f.pts}-point {f.kind.lower()} free-response question with a scoring guide.",
                 fr=[dict(n=1, mode="points", kind=f.kind, mins=f.mins, head=f"{h(f.kind)} &middot; {f.pts} points &middot; about {f.mins} minutes",
                          guide=[], stem=blocks_html(f.stem, f.fig), parts=parts)],
                 frIntro=f"Allow about {f.mins} minutes. Work each part on paper, then open the model solution and give yourself the points your answer earns.",
                 target=dict(label="Target", mc=round(len(mc) * 0.7)),
                 key=f"study.{C.prefix}unit-{u.n}.v1", runhead=f"{C.short} &middot; {h(uname)} &middot; Question Set")
        doc = f"{uname}: Question Set"
    else:
        url = base + f"tests/unit-{u.n}-checks/"
        z.update(title=f"{plain} Guide Checks", h1=f'Unit {u.n} <span style="white-space:nowrap">Guide Checks</span>', sub=h(u.title),
                 metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"{plain} ({u.title.replace('--', '–')}): the study guide's {len(mc)} section check questions as a quiz, with worked explanations.",
                 key=f"study.{C.prefix}unit-{u.n}-checks.v1", runhead=f"{C.short} &middot; {h(uname)} &middot; Guide checks")
        doc = uname
    z.update(url=url, out="public" + url + "index.html",
             foot=(f'From <a href="{pdf}"><i>{h(doc)}</i></a> (PDF). Answers and topic tags are the document&rsquo;s own key; '
                   "the explanations work each problem and say why each wrong choice is wrong. "
                   f'Topic links open the matching section of <a href="{guide}">the guide</a>. Your answers are saved only in this browser.'))
    if not stims:
        z.pop("stims")
    return z


def build_all(C, here):
    pages = json.load(open(os.path.join(here, "pages.json")))
    return [build(C, u, k, pages) for u in C.units() for k in ("questions", "guide")]
