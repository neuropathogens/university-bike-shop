"""ACT Reading Volumes 1-2 -> /study/act/reading/tests/<slug>/.

Items, passages, answers and rule tags come from the series' LaTeX source (source/*.tex, copied from
act_reading_latex_source.zip; parsed by parse.py). The PDF numbers passage lines; on the web the text reflows, so
each \\linelabel the questions cite becomes a small boxed marker carrying its printed line number (source/lines.json,
read from the PDF). The markers a question cites are highlighted when that question is shown.
Explanations are in ex_vol1.py and ex_vol2.py.
"""
import importlib
import importlib.util
import json
import re

from act_reading.parse import SRC, group, parse
from lib.latex import to_html

BASE = "/study/act/reading/"
GUIDE = BASE + "act-reading-1-study-guide.pdf"
LINES = json.loads((SRC / "lines.json").read_text())
RULE_PAGE = {str(r): r + 6 for r in range(1, 12)}  # Rule N starts on page N + 6 of the guide (see its contents)
# Figure 1 of Passage IV, redrawn as SVG from the source's pgfplots data (bar values are printed on the bars)
FIG_DATA = [("Quiet", "(below 45 dB)", 2.9, 2.8), ("Moderate", "(45&ndash;55 dB)", 3.2, 3.0), ("Loud", "(above 55 dB)", 3.6, 3.1)]
FIG_CAPTION = ("<b>Figure 1.</b> Average minimum song frequency of one songbird species at sites grouped by typical traffic noise in 2019, "
               "recorded in spring 2019 and spring 2020. Data are illustrative.")


def figure_iv():
    x0, x1, y0, top, ymax = 78, 628, 300, 70, 4.2
    y = lambda v: y0 - (y0 - top) * v / ymax
    fg, light = "fill:var(--fg)", "fill:var(--line);stroke:var(--fg);stroke-width:1"
    s = ['<svg viewBox="0 0 660 380" width="660" height="380" role="img" style="max-width:100%;height:auto;font-family:var(--serif);font-size:14px" '
         'aria-label="Bar chart. Minimum song frequency in kilohertz, spring 2019 versus spring 2020: quiet sites 2.9 and 2.8; moderate sites 3.2 and 3.0; loud sites 3.6 and 3.1.">']
    for v in range(5):  # grid and y ticks
        s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(v):.1f}" y2="{y(v):.1f}" style="stroke:var(--line);stroke-width:{1 if v else 1.2}"/>'
                 f'<text x="{x0 - 10}" y="{y(v) + 5:.1f}" text-anchor="end" style="{fg}">{v}</text>')
    s.append(f'<text transform="translate(26 {(y0 + top) / 2:.0f}) rotate(-90)" text-anchor="middle" style="{fg}">Minimum song frequency (kHz)</text>')
    for k, (name, sub, a, b) in enumerate(FIG_DATA):
        cx = x0 + (x1 - x0) * (2 * k + 1) / 6
        for dx, v, st in ((-34, a, fg), (2, b, light)):
            s.append(f'<rect x="{cx + dx:.1f}" y="{y(v):.1f}" width="32" height="{y0 - y(v):.1f}" style="{st}"/>'
                     f'<text x="{cx + dx + 16:.1f}" y="{y(v) - 6:.1f}" text-anchor="middle" style="{fg};font-size:12.5px">{v}</text>')
        s.append(f'<text x="{cx:.1f}" y="{y0 + 22}" text-anchor="middle" style="{fg}">{name}</text>'
                 f'<text x="{cx:.1f}" y="{y0 + 40}" text-anchor="middle" style="{fg}">{sub}</text>')
    s.append(f'<text x="{(x0 + x1) / 2:.0f}" y="{y0 + 70}" text-anchor="middle" style="{fg}">Site&rsquo;s typical traffic noise in 2019</text>')
    s.append(f'<rect x="150" y="18" width="14" height="14" style="{fg}"/><text x="170" y="30" style="{fg}">Spring 2019 (normal traffic)</text>'
             f'<rect x="372" y="18" width="14" height="14" style="{light}"/><text x="392" y="30" style="{fg}">Spring 2020 (reduced traffic)</text>')
    s.append("</svg>")
    return f'<figure class="fig">{"".join(s)}<figcaption>{FIG_CAPTION}</figcaption></figure>'



def macros(cites):
    def marker(p):
        lab = p.group()
        if lab not in LINES:
            return ""
        qs = " ".join(str(n) for n in cites.get(lab, []))
        return f'<span class="ln" data-qs="{qs}" aria-label="line {LINES[lab]}">{LINES[lab]}</span>'

    def line(p):
        return f'<span style="white-space:nowrap">line {LINES[p.group()]}</span>'

    def lines(p):
        a, b = p.group(), p.group()
        return f'<span style="white-space:nowrap">lines {LINES[a]}&ndash;{LINES[b]}</span>'

    return {"linelabel": marker, "Line": line, "lines": lines, "P": "¶", "rightarrow": "→"}


def h(s, m):
    return to_html(s, m)


def table_html(src, m):
    cap, body = src.split("\\begin{tabular}", 1)
    cap = re.sub(r"\\small|\\\\\[[^\]]*\]", "", cap).strip()
    body = body[group(body, 0)[1]:].split("\\end{tabular}")[0]
    body = re.sub(r"\\(toprule|midrule|bottomrule)", "", body)
    rows = [r.strip() for r in body.split("\\\\") if r.strip()]
    cells = [[h(c.strip(), m) for c in re.split(r"(?<!\\)&", r)] for r in rows]
    head = "".join(f'<th scope="col">{c}</th>' for c in cells[0])
    trs = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in cells[1:])
    return (f'<div class="fig"><p class="figcap">{h(cap, m)}</p><div class="bt-wrap"><table class="bt"><thead><tr>{head}</tr></thead>'
            f"<tbody>{trs}</tbody></table></div></div>")


def unit_html(u, m):
    out = [f'<p class="stim-intro">{h(u["intro"], m)}</p>']
    fig = ""
    for kind, src in u["parts"]:
        if kind == "sub":
            out.append(f'<p class="stim-sub"><b>{h(src, m)}</b></p>')
        elif kind == "passage":
            out += [f"<p>{h(par, m)}</p>" for par in re.split(r"\n\s*\n", src.strip())]
        elif kind == "note":
            out.append(f'<p class="stim-note"><i>{h(src, m)}</i></p>')
        elif kind == "center":
            fig = figure_iv() if "tikzpicture" in src else table_html(src, m)
    return "".join(out), fig


def quiz(vol):
    tex = ["act_reading_vol1_master_guide.tex", "act_reading_vol2_practice_section.tex"][vol - 1]
    EX = importlib.import_module(f"act_reading.ex_vol{vol}").EX
    units = parse(tex)
    rules = {u["rule"][0]: u["rule"][1] for u in parse("act_reading_vol1_master_guide.tex")}
    # which questions cite each line label (in the stem or choices), so their markers light up
    cites, n = {}, 1
    for u in units:
        for q in u["questions"]:
            for s in [q["stem"], *q["choices"]]:
                for lab in re.findall(r"\\(?:Line|lines)\{([^}]*)\}(?:\{([^}]*)\})?", s):
                    for x in lab:
                        if x:
                            cites.setdefault(x, []).append(n)
            n += 1
    m = macros(cites)
    mc, sections, stims, n = [], {}, {}, 1
    for k, u in enumerate(units, 1):
        word, num = u["label"].split()
        label = f"{word.capitalize()} {num}"
        kind = u["kind"].lower().replace("vqi", "VQI")
        kind = kind[0].upper() + kind[1:]
        sections[k] = f"{label}: {kind}"
        html, fig = unit_html(u, m)
        stims[f"u{k}"] = {"title": f"{label} &middot; {kind}", "html": html}
        for q in u["questions"]:
            idea, steps, others = EX[n]
            rule = u["rule"][0] if vol == 1 else re.search(r"\(R(\d+)\)", q["skill"]).group(1)
            ans = "ABCD".index(q["ans"])
            if set(others) != set("ABCD") - {q["ans"]}:
                raise SystemExit(f"Vol {vol} item {n}: notes for {sorted(others)}, answer {q['ans']}")
            d = dict(n=n, sec=k, topic=rule, stim=f"u{k}", prompt=h(q["stem"], m), options=[h(c, m) for c in q["choices"]],
                     answer=ans, ex=dict(idea=idea, steps=steps, others={"ABCD".index(L): v for L, v in others.items()}))
            if fig:
                d["fig"] = fig
            mc.append(d)
            n += 1
    used = sorted({q["topic"] for q in mc}, key=int)
    topics = {r: (h(rules[r], m), RULE_PAGE[r]) + ((GUIDE + f"#page={RULE_PAGE[r]}",) if vol == 2 else ()) for r in used}
    slug = ["drills", "practice-section"][vol - 1]
    url = BASE + f"tests/{slug}/"
    pdf = BASE + ["act-reading-1-study-guide.pdf", "act-reading-2-practice-section.pdf"][vol - 1]
    total = n - 1
    cfg = dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.act-reading.{slug}.v1",
        runhead="ACT Reading &middot; " + ["The Eleven Rules: Drills", "Full-Length Practice Section"][vol - 1],
        back=("/study/#act-reading", "Study Library"), sub=f"ACT Reading &middot; Volume {vol}",
        mc=mc, sections=sections, stims=stims, topics=topics, topicPrefix="Rule ", topicCol="Rule", guideCol="In the study guide",
        byTopic="By rule", guide=GUIDE, guideName="the study guide",
        foot=(f'From <a href="{pdf}"><i>ACT Reading, Volume {vol}</i></a> (PDF). Answers and rule tags are the volume&rsquo;s own key; '
              "the explanations expand on it with the method, the evidence in the passage, and why each wrong choice is wrong. "
              "Boxed numbers in a passage are the printed line numbers the questions cite. Your answers are saved only in this browser."),
    )
    if vol == 1:
        cfg.update(
            title="ACT Reading Drills: The Eleven Rules", h1='The Eleven Rules: <span style="white-space:nowrap">Drills</span>',
            desc=f"ACT Reading Volume 1 drills: {total} questions on eleven short passages, one drill per rule, each with a worked explanation of the evidence and the traps.",
            metaline=f"{total} questions &middot; eleven drills, one per rule",
            setupNote="Read each passage once, actively, before its questions. Boxed numbers in the passage are the line numbers the questions cite.",
            topicNote="Two or more misses on one rule: reread that rule in the study guide, then redo its drill.",
        )
    else:
        cfg.update(
            title="ACT Reading Full-Length Practice Section", h1='Full-Length <span style="white-space:nowrap">Practice Section</span>',
            desc=f"ACT Reading full-length practice section: four passages and {total} questions, with a worked explanation for every answer and a tally by rule.",
            metaline=f"{total} questions &middot; 40 minutes &middot; four passage units",
            setupNote="Set a 40-minute timer and use Exam mode for a real simulation: about 10 minutes per passage unit. "
                      "Boxed numbers in a passage are the line numbers the questions cite.",
            topicNote="Log every miss by rule; two or more on one rule means rereading that rule in the study guide.",
        )
    return cfg


QUIZZES = [quiz(v) for v in (1, 2) if importlib.util.find_spec(f"act_reading.ex_vol{v}") is not None]
