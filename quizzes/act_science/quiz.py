"""ACT Science Parts 1-6 -> /study/act/science/tests/<slug>/.

Passages, questions, answers and rule tags come from the series' LaTeX source (source/*.tex, copied from
act-science-latex-sources.zip; parsed by parse.py). siunitx units are written out as text, tables become HTML
tables, and each pgfplots figure is a crop of the published PDF (public/study/act/science/tests/fig/, rendered at
3x with PDFKit). Rule links open the page of the part that states the rule (source/pages.json, read from the PDFs).
Explanations are in ex_part1.py ... ex_part6.py.
"""
import html as _html
import importlib
import importlib.util
import json
import re
import struct
from pathlib import Path

from act_science.parse import SRC, group, parse
from lib.latex import _split_math, to_html

BASE = "/study/act/science/"
ROOT = Path(__file__).resolve().parents[2]
FIGURL = BASE + "tests/fig/"
PAGES = json.loads((SRC / "pages.json").read_text())
PARTS = [  # (source, slug, pdf)
    ("01-format-and-strategy", "1", "act-science-01-format-and-strategy.pdf"),
    ("02-interpretation-of-data", "2", "act-science-02-interpretation-of-data.pdf"),
    ("03-scientific-investigation", "3", "act-science-03-scientific-investigation.pdf"),
    ("04-evaluation-of-models", "4", "act-science-04-evaluation-of-models.pdf"),
    ("05-science-knowledge-primer", "5", "act-science-05-science-knowledge-primer.pdf"),
    ("06-full-practice-test", "practice-test", "act-science-06-full-practice-test.pdf"),
]
CATS = {"ID": ("2", "Interpretation of Data"), "SI": ("3", "Scientific Investigation"),
        "EM": ("4", "Evaluation of Models, Inferences &amp; Experimental Results")}
# tikzpicture number (document order) -> (image, alt text)
FIGS = {
    "02": {
        1: ("p2-solubility.png", "Line graph of solubility in grams per 100 grams of water against temperature from 0 to 80 °C. "
            "Compound X rises steeply from 14 to 168; Compound Y stays near 36 to 38; Compound Z falls from 60 to 16."),
        2: ("p2-boiling.png", "Line graph of boiling point against air pressure: 81 °C at 50 kPa, 86 at 60, 90 at 70, 94 at 80, 97 at 90, 100 at 100 kPa."),
        3: ("p2-bacteria.png", "Graph with a logarithmic vertical axis of cells per mL against time from 0 to 8 hours. Strain A rises from "
            "2 × 10³ to about 5 × 10⁵; Strain B rises in a straight line from 10² to 10⁶."),
        4: ("p2-graph-rising.png", "Pressure rises in a straight line as volume increases."),
        5: ("p2-graph-inverse.png", "Pressure drops steeply at first, then levels off as volume increases."),
        6: ("p2-graph-falling.png", "Pressure falls in a straight line as volume increases."),
        7: ("p2-graph-curving-up.png", "Pressure rises along an upward-curving line as volume increases."),
        8: ("p2-ocean.png", "Graph with two vertical axes against depth from 0 to 1000 m. Temperature (solid, left axis) falls from 24 °C to 4 °C. "
            "Dissolved oxygen (dashed, right axis, mg/L) falls from 7.0 to a low of 2.0 at 600 m, then rises to 3.5 at 1000 m."),
    },
    "06": {
        1: ("p6-soil-temperature.png", "Line graph of soil temperature against time of day, 0 to 24 h, at three depths. Surface: 12 °C at 0 h, 9 at 4 h, "
            "30 at 12 h, 27 at 16 h, back to 12 at 24 h. 10 cm: about 14 to 16 early, peaking at 24 near 16 h. 50 cm: flat at about 17."),
        2: ("p6-daily-range.png", "Line graph of daily temperature range against depth: 21 °C at 0 cm, 15 at 5, 10 at 10, 5 at 20, 2 at 30, 0.5 at 50 cm."),
        3: ("p6-rebound.png", "Line graph of rebound height against drop height, 25 to 100 cm, for three balls. Ball A: 20, 40, 60, 80. "
            "Ball B: about 14, 28, 41, 55. Ball C: about 8, 15, 23, 30."),
        4: ("p6-co2-ph.png", "Graph from 1990 to 2020 with two vertical axes. Atmospheric CO₂ (solid, left axis) rises from about 354 to 413 ppm; "
            "seawater pH (dashed, right axis) falls from about 8.11 to 8.05."),
    },
}
PREFIX = {"milli": "m", "centi": "c", "micro": "µ", "kilo": "k", "nano": "n", "mega": "M"}
UNIT = {"celsius": "°C", "metre": "m", "second": "s", "litre": "L", "gram": "g", "hour": "h", "pascal": "Pa", "volt": "V",
        "mole": "mol", "minute": "min", "joule": "J", "ampere": "A", "ohm": "Ω", "newton": "N", "hertz": "Hz", "kelvin": "K",
        "watt": "W", "percent": "%", "degree": "°"}
RULE_PART = {"OV": 1, "ID": 2, "SI": 3, "EM": 4, "PK": 5}
NB = "&#8239;"  # narrow no-break space, as siunitx sets between number and unit


def si_units(s):
    num, den, per, pre, last = [], [], False, "", None
    for mac, word in re.findall(r"\\([a-zA-Z]+)|([^\\\s]+)", s):
        if word or mac in UNIT:
            last = den if per else num
            last.append(word or pre + UNIT[mac])
            pre, per = "", False
        elif mac in PREFIX:
            pre = PREFIX[mac]
        elif mac == "per":
            per = True
        elif mac in ("squared", "cubed"):
            last[-1] += "²" if mac == "squared" else "³"
        else:
            raise ValueError(f"unknown unit \\{mac} in {s!r}")
    out = "&#8239;".join(num)
    if den:
        out += "/" + (den[0] if len(den) == 1 else "(" + "&#8239;".join(den) + ")")
    return out


def si_num(x):
    x = x.strip().replace("\\pm", "±")
    m = re.fullmatch(r"([-+]?[\d.]+)\s*[eE]\s*([-+]?\d+)", x)
    if m:
        mant, exp = m.groups()
        return mant.replace("-", "−") + "&#8239;×&#8239;10<sup>" + exp.replace("-", "−") + "</sup>"
    return x.replace("-", "−")


def _SI(p):
    n, u = p.group(), p.group()
    unit = si_units(u)
    return si_num(n) + ("" if unit in ("°", "%") else NB) + unit


MACROS = {"SI": _SI, "si": lambda p: si_units(p.group()), "ang": lambda p: si_num(p.group()) + "°",
          "ce": lambda p: "$\\ce{" + p.group() + "}$", "to": "→", "div": "÷", "approx": "≈", "geq": "≥", "leq": "≤", "le": "≤",
          "Delta": "Δ", "propto": "∝", "leftrightarrow": "↔", "lambda": "λ", "rho": "ρ", "cdot": "·", "circ": "°", "Omega": "Ω",
          "textperiodcentered": "·", "small": "", "normalsize": "", "centering": "", "raggedright": "", "footnotesize": ""}


def _math_units(piece):
    """\\SI / \\si inside $...$: KaTeX has no siunitx, so write the unit as \\text."""
    unit = lambda u: si_units(u).replace("&#8239;", " ")
    piece = re.sub(r"\\SI\{([^}]*)\}\{([^}]*)\}", lambda m: m.group(1) + r"\,\text{" + unit(m.group(2)) + "}", piece)
    return re.sub(r"\\si\{([^}]*)\}", lambda m: r"\text{" + unit(m.group(1)) + "}", piece)


def h(s):
    s = "".join(_math_units(x) if is_math else x for is_math, x in _split_math(s))
    s = re.sub(r"\\=\{\\i\}", "ī", s)
    s = re.sub(r"\\[hv]space\*?\{[^}]*\}", " ", s)
    return to_html(s, MACROS)


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def img(part, k, cls="fig-img", scale=1.6):
    name, alt = FIGS[part][k]
    w, hh = png_size(ROOT / "public" / FIGURL.lstrip("/") / name)
    w, hh = round(w / 3 * scale), round(hh / 3 * scale)
    return f'<img class="{cls}" src="{FIGURL}{name}" alt="{alt}" width="{w}" height="{hh}" loading="lazy">'


def table_html(rows_src):
    head_src, _, body_src = rows_src.partition("\\midrule")
    if not body_src:
        head_src, body_src = "", head_src

    def rows(src):
        src = re.sub(r"\\cmidrule(\([^)]*\))?\{[^}]*\}", "", src)
        return [r for r in (x.strip() for x in src.split("\\\\")) if r]

    def cells(r, tag):
        out = []
        for c in re.split(r"(?<!\\)&", r):
            c = c.strip()
            m = re.match(r"\\multicolumn\{(\d+)\}\{[^}]*\}", c)
            if m:
                inner, _ = group(c, m.end())
                out.append(f'<{tag} colspan="{m.group(1)}"' + (' scope="colgroup"' if tag == "th" else "") + f">{h(inner)}</{tag}>")
            else:
                out.append(f"<{tag}" + (' scope="col"' if tag == "th" else "") + f">{h(c)}</{tag}>")
        return "".join(out)

    thead = "".join(f"<tr>{cells(r, 'th')}</tr>" for r in rows(head_src))
    tbody = "".join(f"<tr>{cells(r, 'td')}</tr>" for r in rows(body_src))
    return f'<div class="bt-wrap"><table class="bt">' + (f"<thead>{thead}</thead>" if thead else "") + f"<tbody>{tbody}</tbody></table></div>"


def block_html(src, part, figs):
    """Passage LaTeX -> HTML: paragraphs, \\figlabel captions, \\datatable tables, display math, lists, figures."""
    src = re.sub(r"\\begin\{minipage\}(\[[^\]]*\])?\{[^}]*\}|\\end\{minipage\}|\\hfill|\\begin\{figbox\}|\\end\{figbox\}|"
                 r"\\begin\{center\}|\\end\{center\}|\\par\b|\\smallskip|\\medskip|\\noindent", "\n\n", src)
    figs = list(figs)
    src = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", lambda m: f"\n\n@@FIG{figs.pop(0)}@@\n\n", src, flags=re.S)
    out = []
    i = 0
    for m in re.finditer(r"\\datatable\{", src):
        out.append(("text", src[i:m.start()]))
        _, j = group(src, m.end() - 1)
        rows, j = group(src, j)
        out.append(("table", rows))
        i = j
    out.append(("text", src[i:]))
    html = []
    for kind, s in out:
        if kind == "table":
            html.append(table_html(s))
            continue
        for par in re.split(r"\n\s*\n", s):
            par = par.strip()
            if not par:
                continue
            fm = re.fullmatch(r"@@FIG(\d+)@@", par)
            if fm:
                html.append(f'<div class="fig">{img(part, int(fm.group(1)))}</div>')
                continue
            lm = re.fullmatch(r"\\figlabel\{(.*)\}", par, re.S)
            if lm:
                html.append(f'<p class="figcap"><b>{h(lm.group(1))}</b></p>')
                continue
            lst = re.fullmatch(r"\\begin\{(itemize|enumerate)\}(.*)\\end\{\1\}", par, re.S)
            if lst:
                tag = "ul" if lst.group(1) == "itemize" else "ol"
                items = [x.strip() for x in lst.group(2).split("\\item") if x.strip()]
                html.append(f"<{tag}>" + "".join(f"<li>{h(x)}</li>" for x in items) + f"</{tag}>")
                continue
            html.append(f"<p>{h(par)}</p>")
    # a caption directly before its table or figure reads as that element's title
    return "".join(html)


def split_choices(q, part):
    body = q["body"]
    m = re.search(r"\\choices(row|grid)?\{", body)
    if m:
        args, j = [], m.end() - 1
        for _ in range(4):
            a, j = group(body, j)
            args.append(a)
        return body[:m.start()], [h(a) for a in args], None
    # graph choices: \ch{k} & tikzpicture pairs in a tabular
    order = [int(k) for k in re.findall(r"\\ch\{(\d)\}", body)]
    assert sorted(order) == [1, 2, 3, 4] and len(q["figs"]) == 4, q["body"][:80]
    opts, labels = [""] * 4, [""] * 4
    for k, f in zip(order, q["figs"]):
        opts[k - 1] = img(part, f, cls="opt-img", scale=1.4)
        alt = FIGS[part][f][1].rstrip(".")
        labels[k - 1] = "the graph in which " + alt[0].lower() + alt[1:]
    return body[:body.index("\\begin{tabular}")], opts, labels


def roman(n):
    return ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"][n]


def quiz(src, slug, pdf):
    part = src[:2]
    EX = importlib.import_module(f"act_science.ex_part{int(part)}").EX
    d = parse(src + ".tex")
    practice = slug == "practice-test"
    rule_names = {}
    for other, _, _ in PARTS[:5]:
        for s in parse(other + ".tex")["sections"]:
            r = re.match(r"Rule ([A-Z]{2}-\d+): (.+)", s)
            if r:
                rule_names[r.group(1)] = r.group(2)
    mc, sections, stims, secidx = [], {}, {}, {}
    for n, q in enumerate(d["questions"], 1):
        key = ("p", q["passage"]) if q["passage"] else ("s", q["section"])
        if key not in secidx:
            secidx[key] = len(secidx) + 1
            if q["passage"]:
                p = d["passages"][q["passage"] - 1]
                sections[secidx[key]] = f"Passage {roman(p['n'])}: {h(p['title'])}"
                stims[f"p{p['n']}"] = {"title": f"Passage {roman(p['n'])} &middot; {h(p['title'])}",
                                       "html": block_html(p["content"], part, p["figs"]), "cls": "free"}
            else:
                sections[secidx[key]] = h(q["section"])
        stem, opts, labels = split_choices(q, part)
        idea, steps, others = EX[n]
        ans = q["pos"] - 1
        L = "ABCD" if n % 2 else "FGHJ"
        if set(others) != set(L) - {L[ans]}:
            raise SystemExit(f"Part {part} item {n}: notes for {sorted(others)}, answer {L[ans]}")
        rq = dict(n=n, sec=secidx[key], topic=CATS[q["rule"][:2]][0] if practice else q["rule"], prompt=block_html(stem, part, []).removeprefix("<p>").removesuffix("</p>"),
                  options=opts, answer=ans, ex=dict(idea=idea, steps=steps, others={L.index(k): v for k, v in others.items()}))
        if q["passage"]:
            rq["stim"] = f"p{q['passage']}"
        if labels:
            rq["labels"] = labels
        if practice:
            rq["tag"] = q["rule"]
        mc.append(rq)
    total = len(mc)
    meta = d["meta"]
    target = int(re.search(r"(\d+)", meta["settarget"]).group(1))
    minutes = int(re.search(r"(\d+)", meta["settime"]).group(1))
    if practice:
        topics = {CATS[c][0]: (CATS[c][1], 1, BASE + PARTS[int(CATS[c][0]) - 1][2]) for c in ("ID", "SI", "EM")}
    else:
        used = []
        for q in mc:
            if q["topic"] not in used:
                used.append(q["topic"])
        used.sort(key=lambda t: int(t.split("-")[1]))
        topics = {}
        for t in used:
            home = RULE_PART[t[:2]]
            topics[t] = (h(rule_names[t]), PAGES[t]) + ((BASE + PARTS[home - 1][2] + f"#page={PAGES[t]}",) if home != int(part) else ())
    url = BASE + f"tests/{slug}/"
    title = h(meta["settitle"])
    cfg = dict(
        out="public" + url + "index.html", url=url, pdf=BASE + pdf, key=f"study.act-science.{slug}.v1",
        title=_html.unescape(f"ACT Science {'Part ' + slug + ': ' if not practice else ''}{title}"), runhead=f"ACT Science &middot; {title}",
        back=("/study/#act-science", "Study Library"), sub=f"ACT Science &middot; Part {int(part)} of 6",
        h1=title if not practice else 'Full-Length <span style="white-space:nowrap">Practice Test</span>',
        metaline=f"{total} questions &middot; target {target} correct &middot; {minutes} min",
        target={"label": "Target", "mc": target},
        mc=mc, sections=sections, stims=stims, topics=topics,
        foot=(f'From <a href="{BASE + pdf}"><i>ACT Science Part {int(part)}: {title}</i></a> (PDF). Answers and rule tags are the '
              "part&rsquo;s own key; the explanations expand on it with the rule, the reading of the data, and why each wrong choice "
              "is wrong. Figures are taken from the PDF. Your answers are saved only in this browser."),
    )
    if practice:
        cfg.update(
            desc=f"ACT Science full-length practice test: seven passages and {total} questions, with a worked explanation for every answer and a score by reporting category.",
            setupNote="Set a 40-minute timer and use Exam mode for a real simulation. No calculator. Answer every question: there is no penalty for guessing.",
            topicPrefix="Part ", topicCol="Review", guideCol="Reporting category", byTopic="By reporting category",
            topicNote="A category below 70% correct is the next part to reread; then redo the items you missed.",
            guide=BASE + PARTS[0][2], guideName="its part of the series",
            flag={"below": 0.7, "text": "below 70%: review this part"},
        )
    else:
        cfg.update(
            desc=f"ACT Science Part {int(part)} ({h(meta['settitle'])}): {total} questions with the rule behind each answer and why every wrong choice is wrong.",
            setupNote=f"Work untimed the first time, then redo the drills against the clock (target time {minutes} minutes).",
            topicPrefix="", topicCol="Rule", guideCol="In the guide", byTopic="By rule",
            topicNote="Two or more misses on one rule: reread that rule in the guide, then redo its questions.",
            guide=BASE + pdf, guideName="the guide",
        )
    return cfg


QUIZZES = [quiz(*p) for p in PARTS if importlib.util.find_spec(f"act_science.ex_part{int(p[0][:2])}") is not None]
