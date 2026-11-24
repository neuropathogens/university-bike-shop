"""AP English Literature study series -> /study/ap/ap-english-literature/tests/<slug>/.

  exam-checks     Part 0 guide (exam format, rubric, essays): the section checks
  unit-N-checks   Unit N study guide: the section checks
  unit-N          Unit N Question Set: multiple choice on the passages, plus the full essay (Q1/Q2/Q3)

Items are parsed from the series' own LaTeX (source/, copied from ap-lit-study-series.zip; source/pages.json
gives each guide section's PDF page). Choices are in source order, so letters match the PDF keys.
Passages (\\pp paragraphs) and poems/scenes (\\pl lines) become shared stims: every paragraph and verse line is
numbered (the PDFs number verse every five lines), and the paragraph or line a question cites ("paragraph 3", "lines 5 and 9") is
marked and highlighted while that question is shown. Explanations: ex_<file>.py.
"""
import importlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ROOT))
from lib.latex import to_html  # noqa: E402

BASE = "/study/ap/ap-english-literature/"
BLANK = '<span class="blank" role="img" aria-label="blank"></span>'
MACROS = {"textperiodcentered": "·", "blank": BLANK, "small": "", "footnotesize": "", "medskip": "", "smallskip": "",
          "raggedright": ""}
PAGES = json.load(open(os.path.join(ROOT, "source", "pages.json")))

# file stem -> slug, short name, long name
DOCS = {
    "00-exam-and-essays": ("exam", "Part 0", "The Exam, the Rubric, and the Three Essays"),
    "01-prose-fiction": ("unit-1", "Unit 1", "Prose Fiction"),
    "02-poetry": ("unit-2", "Unit 2", "Poetry"),
    "03-longer-fiction-drama": ("unit-3", "Unit 3", "Longer Fiction and Drama"),
}
# the last guide section is the essay; on a question set its items are claim/evidence questions
LAN_NAME = "Literary argument: claims and evidence"


def h(s):
    s = re.sub(r"\\hspace\*?\{[^}]*\}", "", s)
    s = re.sub(r"\\begin\{itemize\}(\[[^\]]*\])?", "", s).replace("\\end{itemize}", "")
    return to_html(s, MACROS)


def group(s, i):
    """Return (content, end) of the {...} group starting at s[i] == '{'."""
    assert s[i] == "{", s[i:i + 30]
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced")


def args(s, i, n):
    out = []
    for _ in range(n):
        while s[i].isspace():
            i += 1
        a, i = group(s, i)
        out.append(a)
    return out, i


def text_items(body):
    """Split a passage/poem body into ('pp', text) / ('pl', text, indent) / ('stanza',) / ('spk', name) / ('sd', text) / ('src', text)."""
    out = []
    pat = re.compile(r"\\(pp|pli|pl|stanza|spk|sd|src)\b")
    ms = list(pat.finditer(body))
    for k, m in enumerate(ms):
        cmd = m.group(1)
        if cmd == "pp":
            end = ms[k + 1].start() if k + 1 < len(ms) else len(body)
            out.append(("pp", body[m.end():end].strip()))
        elif cmd == "stanza":
            out.append(("stanza",))
        else:
            (a,), _ = args(body, m.end(), 1)
            if cmd in ("pl", "pli"):
                lead = re.match(r"\s*\\hspace\*\{([\d.]+)em\}", a)
                indent = (1.5 if cmd == "pli" else 0) + (float(lead.group(1)) if lead else 0)
                out.append(("pl", a, indent))
            else:
                out.append((cmd, a))
    return out


def parse(path):
    """Ordered events: section / text / q / frq; plus the tail after \\makekey."""
    t = open(path, encoding="utf8").read()
    body = t[t.index("\\begin{document}"):]
    key_at = body.find("\\makekey")
    main, tail = (body[:key_at], body[key_at:]) if key_at >= 0 else (body, "")
    ev = []
    pat = re.compile(r"\\section\{|\\begin\{(passage|poem)\}|\\begin\{q\}|\\begin\{frq\}")
    i = 0
    while True:
        m = pat.search(main, i)
        if not m:
            break
        tok = m.group(0)
        if tok == "\\section{":
            title, i = group(main, m.end() - 1)
            ev.append(("section", title))
        elif m.group(1):
            kind = m.group(1)
            (head, intro), j = args(main, m.end(), 2)
            end = main.index("\\end{%s}" % kind, j)
            ev.append(("text", kind, head, intro, text_items(main[j:end])))
            i = end
        elif tok == "\\begin{q}":
            (pos, tag, why), j = args(main, m.end(), 3)
            end = main.index("\\end{q}", j)
            inner = main[j:end]
            cm = re.search(r"\\chh?(?=\{)", inner)
            stem = inner[:cm.start()].strip()
            choices, _ = args(inner, cm.end(), 4)
            ev.append(("q", dict(pos=int(pos), tag=tag, why=why, stem=stem, choices=choices)))
            i = end
        else:
            (title,), j = args(main, m.end(), 1)
            end = main.index("\\end{frq}", j)
            ev.append(("frq", title, main[j:end]))
            i = end
    return ev, tail


NUMS = r"\d+(?:--\d+)?(?:(?:,\s*|,?\s+and\s+)\d+(?:--\d+)?)*"


def cited(stem):
    """{'paragraph'|'line': set of numbers} cited in a question stem."""
    out = {"paragraph": set(), "line": set()}
    for kind, spec in re.findall(r"\b(paragraph|line)s?\s+(" + NUMS + ")", stem):
        for a, b in re.findall(r"(\d+)(?:--(\d+))?", spec):
            out[kind].update(range(int(a), int(b or a) + 1))
    return out


def text_html(kind, intro, items, cites):
    """cites: {number: [question numbers]} for paragraphs (passage) or lines (poem)."""
    out = [f'<p class="stim-intro">{h(intro)}</p>'] if intro.strip() else []
    n = 0
    lines = []
    for it in items:
        if it[0] == "pp":
            n += 1
            qs = cites.get(n)
            attr = f' data-qs="{" ".join(map(str, qs))}"' if qs else ""
            out.append(f'<p><span class="ln"{attr}>{n}</span> {h(it[1])}</p>')
        elif it[0] == "pl":
            n += 1
            qs = cites.get(n)
            attr = f' data-qs="{" ".join(map(str, qs))}"' if qs else ""
            # hanging indent without positioning, so the template can scroll the stim to a cited marker
            mark = f'<span class="ln"{attr} style="width:24px;box-sizing:border-box;margin-right:8px;text-indent:0">{n}</span>'
            ind = it[2]
            spacer = f'<span style="display:inline-block;width:{ind:g}em"></span>' if ind else ""
            lines.append(f'<span style="display:block;padding-left:calc(32px + {ind + 1:g}em);text-indent:calc(-32px - {ind + 1:g}em)">{mark}{spacer}{h(it[1])}</span>')
        elif it[0] == "stanza":
            lines.append('<span style="display:block;height:.75em"></span>')
        elif it[0] == "spk":
            lines.append(f'<span style="display:block;margin-top:.55em;padding-left:1.6em;font:600 12.5px/1.5 system-ui,-apple-system,sans-serif;letter-spacing:.05em">{h(it[1])}</span>')
        elif it[0] == "sd":
            lines.append(f'<span style="display:block;padding-left:3.6em;font-style:italic">[{h(it[1])}]</span>')
        elif it[0] == "src":
            lines.append(f'<span style="display:block;text-align:right;font-style:italic;margin-top:.4em">{h(it[1])}</span>')
    if lines:
        out.append('<p style="margin:0">' + "".join(lines) + "</p>")
    return "".join(out)


def load_ex(stem):
    try:
        return importlib.import_module(f"ap_lit.ex_{stem.replace('-', '_')}").EX
    except ModuleNotFoundError:
        return None


def norm(s):
    s = s.replace("\u2019", "'").replace("\u201c", "``").replace("\u201d", "''")
    return re.sub(r"^(?:``|`|\\\(|\\emph\{|\s)+", "", s)


def match(key, opts):
    if key in opts:
        return key
    hits = [o for o in opts if norm(o).startswith(norm(key))]
    if len(hits) != 1:
        raise SystemExit(f"explanation key {key!r} matches {len(hits)} of {opts}")
    return hits[0]


def essay(title, body, tail):
    """The question set's essay: prompt (stem), one 6-point part with the model response and the scoring guide."""
    b = body
    works = re.search(r"\\begin\{multicols\}\{\d\}(.*?)\\end\{multicols\}", b, re.S)
    if works:
        b = b[:works.start()] + b[works.end():]
    lst = re.search(r"\\begin\{itemize\}(\[[^\]]*\])?(.*?)\\end\{itemize\}", b, re.S)
    before, bullets = b[:lst.start()], lst.group(2)
    paras = [x.strip() for x in re.split(r"\n\s*\n|\\medskip", before) if x.strip()]
    stem = "".join(f"<p>{h(x)}</p>" for x in paras)
    stem += "<ul>" + "".join(f"<li>{h(x.strip())}</li>" for x in re.split(r"\\item\s", bullets) if x.strip()) + "</ul>"
    if works:
        names = [h(x.strip()) for x in re.split(r"\\\\", works.group(1)) if x.strip()]
        stem += '<p class="stim-note">Suggested works: ' + "; ".join(names) + ".</p>"
    cm = re.search(r"\\begin\{compare\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{compare\}", tail, re.S)
    good, bad = h(cm.group(2)), h(cm.group(3))
    rows = [r.strip() for r in re.split(r"\\\\", cm.group(4)) if r.strip()]
    rub = []
    for r in rows:
        cells = [c.strip() for c in re.split(r"(?<!\\)&", r)]
        rub.append(f"<p><b>{h(cells[0])}.</b> <i>{good}:</i> {h(cells[1])}<br><i>{bad}:</i> {h(cells[2])}</p>")
    me = re.search(r"\\begin\{modelessay\}\[(.*?)\]\s*(.*?)\\end\{modelessay\}", tail, re.S)
    model = "".join(f"<p>{h(x.strip())}</p>" for x in re.split(r"\n\s*\n", me.group(2)) if x.strip())
    kind = re.search(r"Question \d+ \\textperiodcentered\\ ([^\\]+?) \\textperiodcentered", title).group(1)
    n = int(re.search(r"Question (\d+)", title).group(1))
    mins = int(re.search(r"(\d+) minutes", title).group(1))
    part = dict(label="Essay", max=6, prompt="Write the full essay: thesis, body paragraphs, and a brief conclusion.",
                solution=f"<p><b>{h(me.group(1))}.</b></p>" + model,
                rubric="<p><b>Scoring guide.</b> Score each row separately and add them: Row A 0&ndash;1, Row B 0&ndash;4, Row C 0&ndash;1.</p>" + "".join(rub))
    return dict(n=n, mode="points", kind=kind, mins=mins, head=f"{kind} &middot; 6 points &middot; {mins} minutes",
                guide=[], stem=stem, parts=[part])


def guide_sections(stem_name):
    t = open(os.path.join(ROOT, "source", f"{stem_name}-guide.tex"), encoding="utf8").read()
    return re.findall(r"\\section\{([^}]*)\}", t)


def build_quiz(stem_name, kind):
    slug, short, long = DOCS[stem_name]
    src = os.path.join(ROOT, "source", f"{stem_name}-{kind}.tex")
    if not os.path.exists(src):
        return None
    ev, tail = parse(src)
    ex = load_ex(f"{stem_name}-{kind}")
    if ex is None:
        return None
    qs = [e[1] for e in ev if e[0] == "q"]
    assert len(ex) == len(qs), (stem_name, kind, len(ex), len(qs))
    # cited paragraphs/lines per text block: questions belong to the text that precedes them
    blocks, cur, qn = [], None, 0
    for e in ev:
        if e[0] == "text":
            cur = {"ev": e, "qs": []}
            blocks.append(cur)
        elif e[0] == "section":
            cur = None if kind == "guide" else cur
        elif e[0] == "q":
            qn += 1
            if cur is not None:
                cur["qs"].append((qn, e[1]["stem"]))
        elif e[0] == "frq":
            cur = None
    stims, stim_of = {}, {}
    sec_titles = [e[1] for e in ev if e[0] == "section"]
    for k, b in enumerate(blocks):
        _, tkind, head, intro, items = b["ev"]
        unit = "paragraph" if tkind == "passage" else "line"
        cites = {}
        for n, stem in b["qs"]:
            for x in sorted(cited(stem)[unit]):
                cites.setdefault(x, []).append(n)
            stim_of[n] = f"t{k + 1}"
        if b["qs"]:
            m = re.match(r"(Passage|Poem) (\d+): (.*)", sec_titles[min(k, len(sec_titles) - 1)])
            title = f"{m.group(1)} {m.group(2)} &middot; {h(m.group(3))}" if m else h(head)
        else:
            title = h(head)
        stims[f"t{k + 1}"] = dict(title=title, html=text_html(tkind, intro, items, cites))
    gsec = guide_sections(stem_name)
    pages = PAGES[f"{stem_name}-guide"]
    sections, mc, fr = {}, [], []
    sec = n = 0
    for e in ev:
        if e[0] == "section":
            if e[1].startswith("Free Response"):
                continue
            sec += 1
            sections[sec] = h(e[1])
        elif e[0] == "q":
            q = e[1]
            x = ex[n]
            n += 1
            right = q["choices"][q["pos"] - 1]
            if not norm(right).startswith(norm(x["ans"])):
                raise SystemExit(f"{stem_name}-{kind} item {n}: explanation for {x['ans']!r}, answer is {right!r}")
            wrong = [c for c in q["choices"] if c != right]
            mapped = {match(k, wrong): v for k, v in x["others"].items()}
            if set(mapped) != set(wrong):
                raise SystemExit(f"{stem_name}-{kind} item {n}: notes missing for {set(wrong) - set(mapped)}")
            item = dict(n=n, sec=sec, topic=q["tag"].split()[0], tag=h(q["tag"]), prompt=h(q["stem"]),
                        options=[h(c) for c in q["choices"]], answer=q["pos"] - 1,
                        ex=dict(idea=x["idea"], steps=x.get("steps", []),
                                others={q["choices"].index(w): v for w, v in mapped.items()}))
            if n in stim_of:
                item["stim"] = stim_of[n]
            mc.append(item)
        elif e[0] == "frq":
            f = essay(e[1], e[2], tail)
            nxt = ev[ev.index(e) + 1] if ev.index(e) + 1 < len(ev) else None
            if nxt and nxt[0] == "text":
                k = blocks.index(next(b for b in blocks if b["ev"] is nxt))
                f["stim"] = f"t{k + 1}"
                stims[f"t{k + 1}"]["cls"] = "free"
            fr.append(f)
    guide = BASE + f"ap-lit-{stem_name}-guide.pdf"
    pdf = BASE + f"ap-lit-{stem_name}-{kind}.pdf"
    topics = {}
    for q in mc:
        t = q["topic"]
        if t in topics:
            continue
        k = int(t.split(".")[1])
        name = gsec[k - 1]
        if kind == "questions" and k == len(gsec):
            name = LAN_NAME
        topics[t] = (h(name), pages[str(k)])
    topics = {t: topics[t] for t in sorted(topics, key=lambda t: int(t.split(".")[1]))}
    srctext = open(src, encoding="utf8").read()
    target = re.search(r"Target: (\d+)\+", srctext)
    nice = long if stem_name != "00-exam-and-essays" else "Exam, Rubric &amp; Essays"
    if kind == "questions":
        url = BASE + f"tests/{slug}/"
        mins = round(len(mc) * 65 / 60)
        z = dict(title=f"AP Literature {short} Question Set: {long}",
                 h1=f'{short} <span style="white-space:nowrap">Question Set</span>', sub=nice,
                 metaline=f"{len(mc)} multiple-choice (about {mins} min) &middot; 1 essay, {fr[0]['kind']} ({fr[0]['mins']} min)",
                 setupNote="Allow about 65 seconds per question, including reading. The passage stays above each question, and the paragraph or line the question cites is highlighted.",
                 desc=f"AP English Literature {short} question set ({long.lower()}): {len(mc)} exam-style multiple-choice questions on public-domain passages with in-depth explanations, plus a full {fr[0]['kind']} essay with a 6-point scoring guide and model response.",
                 fr=fr, frWord="Question",
                 frIntro=f"Allow {fr[0]['mins']} minutes. Write the essay, then open the model response and scoring guide and give yourself 0&ndash;6: Row A thesis (0&ndash;1), Row B evidence and commentary (0&ndash;4), Row C sophistication (0&ndash;1).",
                 foot_doc=f"{short}: {long}: Question Set")
    else:
        url = BASE + f"tests/{slug}-checks/"
        z = dict(title=f"AP Literature {short} Guide Checks: {long}",
                 h1=f'{short} <span style="white-space:nowrap">Guide Checks</span>', sub=nice,
                 metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"AP English Literature {short} study guide ({long.lower()}): the guide's {len(mc)} section check questions as a quiz, with in-depth explanations.",
                 foot_doc=f"{short}: {long}")
    if target:
        z["target"] = dict(label="Target", mc=int(target.group(1)))
    foot_doc = z.pop("foot_doc")
    z.update(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-lit.{slug}{'' if kind == 'questions' else '-checks'}.v1",
        runhead=f"AP English Literature &middot; {short}: {nice}" + (" &middot; Question Set" if kind == "questions" else " &middot; Guide checks"),
        back=("/study/#ap-english-literature", "Study Library"), mc=mc, stims=stims, sections=sections, topics=topics,
        topicPrefix="", topicCol="Topic", guideCol="Guide section", byTopic="By topic",
        topicNote="Two or more misses on one topic: reread that section of the guide.",
        guide=guide, guideName=f"the <i>{short} guide</i>",
        foot=(f'From <a href="{pdf}"><i>{foot_doc}</i></a> (PDF). Answers and rule tags are the document&rsquo;s own key; '
              "the explanations expand on it with the reasoning from the text and why each wrong choice is wrong. "
              + ("All passages are in the public domain. " if kind == "questions" else "")
              + f'Topic links open the matching section of <a href="{guide}">the guide</a>. Your answers are saved only in this browser.'),
    )
    return z


def review(stem_name):
    """Plain dump of items, for writing explanations."""
    ev, _ = parse(os.path.join(ROOT, "source", f"{stem_name}.tex"))
    n = 0
    for e in ev:
        if e[0] == "q":
            n += 1
            q = e[1]
            print(f"{n}. [{q['tag']}] {q['stem']}")
            for k, c in enumerate(q["choices"], 1):
                print(f"   {'*' if k == q['pos'] else '-'} {c}")
            print(f"   > {q['why']}")


QUIZZES = [z for s in DOCS for k in ("questions", "guide") for z in [build_quiz(s, k)] if z]

if __name__ == "__main__":
    review(sys.argv[1])
