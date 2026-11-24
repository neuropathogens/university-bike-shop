"""AP Macroeconomics and AP Microeconomics unit practice sets -> /study/ap/ap-economics/tests/<course>-<unit>/.

Items come from the series' own question data (source/data/<course>-u<N>-practice.py, from ap-econ-source.zip),
and the answer letters are placed by the series' own balancer (source/gen.py, `assign`, seeded by the file name),
so choices and letters match the PDFs exactly; keys.json holds each PDF's printed answer strip and the build
asserts against it. `why` (the PDF key's reason) is the explanation's idea; ex_<course>_u<N>.py adds worked steps
and a note for every wrong choice. Topic links open the unit guide at the section's page (pages.json).
"""
import importlib
import importlib.util
import json
import re
from pathlib import Path

from lib.latex import to_html

HERE = Path(__file__).resolve().parent
LET = "ABCDE"
BASE = "/study/ap/ap-economics/"
KEYS = json.loads((HERE / "keys.json").read_text())
PAGES = json.loads((HERE / "pages.json").read_text())
MACROS = {"then": "&#8239;&rArr;&#8239;", "texteuro": "€", "small": "", "smallskip": "", "medskip": "", "noindent": "",
          "par": " "}
COURSE = {"macro": ("AP Macroeconomics", "ap-macroeconomics"), "micro": ("AP Microeconomics", "ap-microeconomics")}
GUIDES = {  # unit guide PDFs (already on /study)
    "macro": ["basic-economic-concepts", "economic-indicators-and-business-cycle", "national-income-and-price-determination",
              "financial-sector", "long-run-consequences-of-stabilization-policies", "open-economy"],
    "micro": ["basic-economic-concepts", "supply-and-demand", "production-cost-and-perfect-competition",
              "imperfect-competition", "factor-markets", "market-failure-and-role-of-government"],
}


def _load(path, name, extra=None):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    for k, v in (extra or {}).items():
        setattr(mod, k, v)
    spec.loader.exec_module(mod)
    return mod


GEN = _load(HERE / "source" / "gen.py", "ap_econ_gen")


def tx(s):
    return s.replace("\\'", "'")  # gen.py makes the same replacement in the .tex it writes


MATH = re.compile(r"(?<!\\)\$(.+?)(?<!\\)\$", re.S)


def h(s):
    # a literal \$ inside $..$ becomes \text{\textdollar} (same glyph in KaTeX), which lib/latex's checks expect
    s = MATH.sub(lambda m: "$" + m.group(1).replace("\\$", "\\text{\\textdollar}") + "$", tx(s))
    return to_html(s, MACROS)


def group(s, i):
    """(content, end) of the {...} group that starts at s[i] == '{'."""
    depth = 0
    for j in range(i, len(s)):
        depth += {"{": 1, "}": -1}.get(s[j], 0)
        if depth == 0:
            return s[i + 1:j], j + 1
    raise ValueError("unbalanced braces: " + s[i:i + 60])


def table_html(tab):
    """booktabs tabular -> HTML table. Rows above \\midrule are the header; \\multicolumn and \\multirow are kept."""
    body = tab[tab.index("\\begin{tabular}") + len("\\begin{tabular}"):tab.index("\\end{tabular}")]
    _, k = group(body, body.index("{"))
    body = body[k:]
    body = re.sub(r"\\cmidrule(\([a-z]+\))?\{[^}]*\}", "", body)
    head_src, rows_src = body.split("\\midrule", 1)
    head_src = head_src.replace("\\toprule", "")
    rows_src = rows_src.replace("\\bottomrule", "")
    spans = {}

    def cells(row, tag, first_th):
        out, col = [], 0
        parts = [c.strip() for c in re.split(r"(?<!\\)&", row)]
        for c in parts:
            if spans.get(col, 0) > 0 and c == "":  # the empty cell under a \multirow is covered by its rowspan
                spans[col] -= 1
                col += 1
                continue
            attrs, text = "", c
            m = re.match(r"\\multicolumn\{(\d+)\}\{[^}]*\}", c)
            if m:
                text, _ = group(c, m.end())
                attrs += f' colspan="{m.group(1)}"'
                n = int(m.group(1))
            else:
                n = 1
            m = re.match(r"\\multirow\{(\d+)\}\{\*\}", text)
            if m:
                text, _ = group(text, m.end())
                attrs += f' rowspan="{m.group(1)}"'
                spans[col] = int(m.group(1)) - 1
            t = tag if not (first_th and col == 0) else "th"
            scope = ' scope="col"' if tag == "th" else (' scope="row"' if t == "th" else "")
            out.append(f"<{t}{scope}{attrs}>{h(text)}</{t}>")
            col += n
        return "<tr>" + "".join(out) + "</tr>"

    rows = [r for r in re.split(r"\\\\", head_src) if r.strip()]
    head = "".join(cells(r, "th", False) for r in rows)
    rows = [r for r in re.split(r"\\\\", rows_src) if r.strip()]
    spans.clear()
    bodyh = "".join(cells(r, "td", True) for r in rows)
    return f'<div class="bt-wrap"><table class="bt"><thead>{head}</thead><tbody>{bodyh}</tbody></table></div>'


TAB = re.compile(r"\\par\\smallskip\{\\small(\\begin\{tabular\}.*?\\end\{tabular\})\}\\par\\smallskip", re.S)


def stem_html(stem):
    """Stem text with any embedded booktabs table; text after the table becomes its own paragraph."""
    stem = tx(stem)
    m = TAB.search(stem)
    if not m:
        return h(stem)
    before, after = stem[:m.start()], stem[m.end():]
    after = re.sub(r"^\\noindent\s*", "", after).replace("\\par\\smallskip", "").strip()
    return h(before) + table_html(m.group(1)) + (f'<p class="note">{h(after)}</p>' if after else "")


def set_quiz(course, unit):
    stem_name = f"{course}-u{unit}-practice"
    path = HERE / "source" / "data" / f"{stem_name}.py"
    data = _load(path, "ap_econ_" + stem_name.replace("-", "_"), dict(Sec=GEN.Sec, Q=GEN.Q, F=GEN.F))
    M, S = data.META, data.SECTIONS
    allq = [(s, q) for s in S for q in s.qs]
    placed = GEN.assign([q for _, q in allq], Path(path).stem)
    letters = "".join(L for _, L in placed)
    if letters != KEYS[f"{course}-u{unit}"]:
        raise SystemExit(f"{stem_name}: letters {letters} do not match the PDF key {KEYS[f'{course}-u{unit}']}")
    ex = importlib.import_module(f"ap_econ.ex_{course}_u{unit}").EX
    if len(ex) != len(allq):
        raise SystemExit(f"{stem_name}: {len(ex)} explanations for {len(allq)} questions")
    mc = []
    for n, ((sec, q), (choices, L), x) in enumerate(zip(allq, placed, ex), 1):
        ans = LET.index(L)
        if q["fixed"]:
            if set(x["o"]) != set(LET) - {L}:
                raise SystemExit(f"{stem_name} Q{n}: notes must cover exactly the wrong letters")
            others = {LET.index(k): h(v) for k, v in x["o"].items()}
        else:
            if len(x["o"]) != 4:
                raise SystemExit(f"{stem_name} Q{n}: need 4 wrong-choice notes")
            others = {(j if j < ans else j + 1): h(v) for j, v in enumerate(x["o"])}
            assert choices[ans] == q["correct"] and [c for i, c in enumerate(choices) if i != ans] == q["wrong"]
        mc.append(dict(n=n, sec=sec.topic, topic=sec.topic, tag=f"Rule {sec.topic}", prompt=stem_html(q["stem"]),
                       options=[h(c) for c in choices], answer=ans,
                       ex=dict(idea=h(q["why"]), steps=[h(s) for s in x.get("steps", [])], others=others)))
    cname, anchor = COURSE[course]
    uname = tx(M["unitname"])
    guide = f"{BASE}{course}/ap-{course}-unit-{unit}-{GUIDES[course][unit - 1]}.pdf"
    pdf = f"{BASE}{course}/ap-{course}-unit-{unit}-practice.pdf"
    pages = PAGES[f"{course}-u{unit}"]
    topics = {s.topic: (h(s.title), pages[s.topic]) for s in S}
    n = len(mc)
    url = f"{BASE}tests/{course}-{unit}/"
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-econ.{course}-{unit}.v1",
        title=f"{cname} Unit {unit} Practice Set", h1=f'Unit {unit} <span style="white-space:nowrap">Practice Set</span>',
        sub=h(uname), runhead=f"{cname} &middot; Unit {unit}: {h(uname)} &middot; Practice Set",
        desc=f"{cname} Unit {unit} ({uname}) practice set: {n} five-choice multiple-choice questions with worked "
             "explanations and a note on every wrong choice.",
        metaline=f"{n} multiple-choice questions, five choices each (about {round(n * 70 / 60)} min at exam pace)",
        setupNote="Allow about 70 seconds per question, the exam&rsquo;s pace. Each question names the topic rule it tests.",
        back=(f"/study/#{anchor}", "Study Library"), mc=mc, sections={s.topic: h(s.title) for s in S}, topics=topics,
        topicPrefix="", topicCol="Topic", guideCol="Guide section", byTopic="By topic",
        topicNote="Two or more misses on one topic: reread that section of the guide.",
        guide=guide, guideName=f"the <i>Unit {unit} guide</i>",
        foot=(f'From <a href="{pdf}"><i>{cname} Unit {unit} Practice Set</i></a> (PDF). Answers and reasons are the '
              "document&rsquo;s own key; the explanations add worked steps and say why each wrong choice is wrong. "
              f'Topic links open the matching section of <a href="{guide}">the Unit {unit} guide</a>. '
              "Your answers are saved only in this browser."),
    )


QUIZZES = [set_quiz(c, u) for c in ("macro", "micro") for u in range(1, 7)]
