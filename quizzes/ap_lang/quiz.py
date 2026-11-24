"""AP English Language study series -> /study/ap/ap-english-language/tests/<slug>/.

  method-checks     Part 0 guide's section checks
  part-N-checks     Part N guide's section checks (N = 1-4)
  part-N            Part N question set: three passages (two reading, one writing) + one essay

Items are parsed from the series' own LaTeX (source/, the same files as ap-lang-study-series.zip);
choices are in source order, so letters match the PDF keys. Passages become shared stimuli, with
paragraph and sentence markers highlighted for the questions that cite them. The essay is one draft
scored on the three AP rubric rows (thesis 1, evidence and commentary 4, sophistication 1), taken
from each set's scoring guide. Explanations: ex_<file>.py. source/pages.json gives each guide
section's page (from the .aux files) for the topic links.
"""
import importlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ROOT))
from lib.latex import to_html  # noqa: E402

BASE = "/study/ap/ap-english-language/"
BLANK = '<span class="blank" role="img" aria-label="blank"></span>'
PAGES = {k: {int(s): p for s, p in v.items()} for k, v in json.load(open(os.path.join(ROOT, "source", "pages.json"))).items()}

# stem -> (slug, part label, short name)
DOCS = {
    "00-exam-method": ("method", "Part 0", "The Exam and the Method"),
    "01-rhetorical-situation": ("part-1", "Part 1", "The Rhetorical Situation"),
    "02-claims-evidence": ("part-2", "Part 2", "Claims and Evidence"),
    "03-reasoning-organization": ("part-3", "Part 3", "Reasoning and Organization"),
    "04-style": ("part-4", "Part 4", "Style"),
}
STEM_OF = {s[:2]: s for s in DOCS}


def pdf_of(stem, kind):
    return BASE + f"ap-lang-{stem}-{kind}.pdf"


def marker(prefix):
    def f(p):
        n = to_html(p.group()).strip()
        return f'<span class="ln" data-m="{prefix}{n}">{"&para;" if prefix == "p" else ""}{n}</span> '
    return f


MACROS = {"textperiodcentered": "·", "blank": BLANK, "small": "", "footnotesize": "", "medskip": "", "smallskip": "",
          "pn": marker("p"), "sn": marker("s"), "enspace": " ", "quad": " "}


def h(s):
    return to_html(s, MACROS)


def group(s, i):
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


def tabular_html(tex):
    body = re.search(r"\\begin\{tabular\}\{[^}]*\}(.*?)\\end\{tabular\}", tex, re.S).group(1)
    body = re.sub(r"\\(toprule|bottomrule)", "", body)
    parts = re.split(r"\\midrule", body)

    def rows(chunk):
        return [r.strip() for r in re.split(r"\\\\", chunk) if r.strip()]
    head = rows(parts[0]) if len(parts) > 1 else []
    out = ['<div class="bt-wrap"><table class="bt">']
    if head:
        out.append("<thead>" + "".join("<tr>" + "".join(f'<th scope="col">{h(c.strip())}</th>' for c in re.split(r"(?<!\\)&", r)) + "</tr>" for r in head) + "</thead>")
    out.append("<tbody>")
    for r in rows(parts[-1]):
        cells = [c.strip() for c in re.split(r"(?<!\\)&", r)]
        out.append("<tr>" + f'<th scope="row">{h(cells[0])}</th>' + "".join(f"<td>{h(c)}</td>" for c in cells[1:]) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def body_html(tex):
    """Paragraphs (blank-line separated) and centered tables -> HTML."""
    out = []
    for piece in re.split(r"(\\begin\{center\}.*?\\end\{center\})", tex.strip(), flags=re.S):
        if piece.startswith("\\begin{center}"):
            out.append(tabular_html(piece))
        else:
            out += [f"<p>{h(p)}</p>" for p in re.split(r"\n\s*\n", piece) if p.strip()]
    return "".join(out)


def parse(path):
    """Ordered events and the tail after \\makekey."""
    t = open(path, encoding="utf8").read()
    body = t[t.index("\\begin{document}"):]
    key_at = body.find("\\makekey")
    main, tail = (body[:key_at], body[key_at:]) if key_at >= 0 else (body, "")
    ev = []
    pat = re.compile(r"\\section\{|\\begin\{passage\}|\\begin\{source\}|\\begin\{q\}|\\begin\{frq\}")
    i = 0
    while True:
        m = pat.search(main, i)
        if not m:
            break
        tok = m.group(0)
        if tok == "\\section{":
            title, i = group(main, m.end() - 1)
            ev.append(("section", title))
        elif tok in ("\\begin{passage}", "\\begin{source}"):
            env = tok[7:-1]
            (title, intro), j = args(main, m.end(), 2)
            end = main.index(f"\\end{{{env}}}", j)
            ev.append((env, title, intro, main[j:end]))
            i = end
        elif tok == "\\begin{q}":
            (pos, tag, why), j = args(main, m.end(), 3)
            end = main.index("\\end{q}", j)
            inner = main[j:end]
            cm = re.search(r"\\chh?(?=\{)", inner)
            choices, _ = args(inner, cm.end(), 4)
            ev.append(("q", dict(pos=int(pos), tag=tag, why=why, stem=inner[:cm.start()].strip(), choices=choices)))
            i = end
        else:
            (title,), j = args(main, m.end(), 1)
            end = main.index("\\end{frq}", j)
            ev.append(("frq", title, main[j:end]))
            i = end
    return ev, tail


def stem_html(tex):
    return "".join(f"<p>{h(p)}</p>" for p in re.split(r"\n\s*\n", tex.strip()) if p.strip())


def norm(s):
    return re.sub(r"^(?:``|\\\(|\s)+", "", s)


def has(opt, key):
    """An explanation key names a choice by its opening words, or by a distinctive phrase inside it."""
    return norm(opt).startswith(norm(key)) or key in opt


def match(key, opts):
    if key in opts:
        return key
    hits = [o for o in opts if norm(o).startswith(norm(key))] or [o for o in opts if key in o]
    if len(hits) != 1:
        raise SystemExit(f"explanation key {key!r} matches {len(hits)} of {opts}")
    return hits[0]


def load_ex(stem, kind):
    try:
        return importlib.import_module(f"ap_lang.ex_{stem.replace('-', '_')}_{kind}").EX
    except ModuleNotFoundError:
        return None


def refs(stem_tex):
    """Markers a question cites: 'paragraph 3', 'paragraphs 1 and 2', 'sentence 7', 'sentences 10 and 11'."""
    out = set()
    for kind, nums in re.findall(r"\b(paragraphs?|sentences?)\s+(\d+(?:\s*(?:,|and|--|-)\s*\d+)*)", stem_tex):
        ns = [int(x) for x in re.findall(r"\d+", nums)]
        if re.search(r"--|-", nums) and len(ns) == 2:
            ns = list(range(ns[0], ns[1] + 1))
        out |= {("p" if kind.startswith("p") else "s") + str(n) for n in ns}
    return out


def mark(html, cites):
    """Add data-qs (question numbers) to each cited marker."""
    by = {}
    for qn, ms in cites:
        for m in ms:
            by.setdefault(m, []).append(str(qn))
    return re.sub(r'data-m="([ps]\d+)"', lambda m: (f'data-qs="{" ".join(by[m.group(1)])}"' if m.group(1) in by else ""), html)


def guide_sections():
    out = {}
    for stem in DOCS:
        t = open(os.path.join(ROOT, "source", f"{stem}-guide.tex"), encoding="utf8").read()
        out[stem[:2]] = [re.sub(r"\s*\([^)]*\)\s*$", "", x) for x in re.findall(r"\\section\{([^}]*)\}", t)]
    return out


SECTIONS = guide_sections()


def essay(title, frq_body, tail, stim_id):
    """The set's essay: directions/prompt as the stem; the scoring guide's rows as three self-scored rows."""
    b = re.sub(r"^\s*\\small\s*", "", frq_body)
    b = re.sub(r"\\begin\{itemize\}\[[^\]]*\]", "<ul>", b).replace("\\end{itemize}", "</ul>")
    paras = []
    for p in re.split(r"\n\s*\n", b.strip()):
        if "<ul>" in p:
            head, lst = p.split("<ul>", 1)
            items = [x.strip() for x in lst.replace("</ul>", "").split("\\item") if x.strip()]
            paras.append((f"<p>{h(head)}</p>" if head.strip() else "") + "<ul>" + "".join(f"<li>{h(x)}</li>" for x in items) + "</ul>")
        elif p.strip():
            paras.append(f"<p>{h(p)}</p>")
    cm = re.search(r"\\begin\{compare\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{compare\}", tail, re.S)
    good, bad = h(cm.group(2)), h(cm.group(3))
    rows = [r.strip() for r in re.split(r"\\\\", cm.group(4)) if r.strip()]
    names = {"A": "Thesis", "B": "Evidence and commentary", "C": "Sophistication"}
    prompts = {"A": "Does the essay make a defensible thesis that responds to the prompt?",
               "B": "Does specific evidence support every claim, with commentary that consistently explains how?",
               "C": "Does the essay show sophistication of thought or a complex understanding of the rhetorical situation?"}
    parts = []
    for r in rows:
        cells = [c.strip() for c in re.split(r"(?<!\\)&", r)]
        m = re.match(r"([ABC])\.\s*(.*?)\s*\((\d)\)$", cells[0])
        lab, pts = m.group(1), int(m.group(3))
        parts.append(dict(label=lab, max=pts, prompt=f" <b>{names[lab]}</b> ({pts} point{'s' if pts > 1 else ''}). {prompts[lab]}",
                          solution=f"<p><b>{good}:</b> {h(cells[1])}</p>",
                          rubric=f"<p><b>{bad}:</b> {h(cells[2])}</p>"))
    assert [p["label"] for p in parts] == ["A", "B", "C"], parts
    qn, kind_fr, mins = re.match(r"Question (\d) \\textperiodcentered\\ ([A-Za-z ]+?) \\textperiodcentered.*?(\d+) minutes", title).groups()
    return dict(n=int(qn), mode="points", essay=True, kind=kind_fr, mins=int(mins), stim=stim_id,
                head=f"{kind_fr} &middot; 6 points &middot; {mins} minutes", guide=[], stem="".join(paras), parts=parts)


def build(stem, kind):
    slug, part, name = DOCS[stem]
    src = os.path.join(ROOT, "source", f"{stem}-{kind}.tex")
    ev, tail = parse(src)
    ex = load_ex(stem, kind)
    if ex is None:
        return None
    qs = [e[1] for e in ev if e[0] == "q"]
    assert len(ex) == len(qs), (stem, kind, len(ex), len(qs))
    sections, stims, mc, fr = {}, {}, [], []
    sec, n, cur, cites = 0, 0, None, {}
    frq_pending, sources = None, []
    for e in ev:
        if e[0] == "section":
            if e[1] == "Free response":
                cur = None
                continue
            sec += 1
            sections[sec] = h(re.sub(r"\s*\((reading|writing)\)\s*$", r" (\1)", e[1]))
            cur = None
        elif e[0] == "passage":
            sid = f"s{len(stims) + 1}"
            stims[sid] = dict(title=h(e[1]), html=f'<p class="stim-intro">{h(e[2])}</p>' + body_html(e[3]))
            cites[sid] = []
            if frq_pending:
                fr.append(essay(frq_pending[0], frq_pending[1], tail, sid))
                frq_pending = None
            else:
                cur = sid
        elif e[0] == "source":
            sources.append(e)
        elif e[0] == "q":
            q, x = e[1], ex[n]
            n += 1
            right = q["choices"][q["pos"] - 1]
            if not has(right, x["ans"]):
                raise SystemExit(f"{stem}-{kind} item {n}: explanation for {x['ans']!r}, answer is {right!r}")
            wrong = [c for c in q["choices"] if c != right]
            mapped = {match(k, wrong): v for k, v in x["others"].items()}
            if set(mapped) != set(wrong):
                raise SystemExit(f"{stem}-{kind} item {n}: notes missing for {set(wrong) - set(mapped)}")
            item = dict(n=n, sec=sec, topic=q["tag"].split()[0], tag=h(q["tag"]), prompt=stem_html(q["stem"]),
                        options=[h(c) for c in q["choices"]], answer=q["pos"] - 1,
                        ex=dict(idea=x["idea"], steps=x.get("steps", []),
                                others={q["choices"].index(w): v for w, v in mapped.items()}))
            if cur:
                item["stim"] = cur
                cites[cur].append((n, refs(q["stem"])))
            mc.append(item)
        elif e[0] == "frq":
            frq_pending = (e[1], e[2])
    if frq_pending:  # synthesis: the six sources become one stimulus
        sid = f"s{len(stims) + 1}"
        html = "".join(f'<p class="stim-sub"><b>{h(t)}</b> &nbsp;<i>{h(i)}</i></p>' + body_html(b) for _, t, i, b in sources)
        stims[sid] = dict(title="Sources", html=html)
        fr.append(essay(frq_pending[0], frq_pending[1], tail, sid))
    for sid, cs in cites.items():
        stims[sid]["html"] = mark(stims[sid]["html"], cs)
    for s in stims.values():
        s["html"] = s["html"].replace("<p></p>", "")
        s["html"] = re.sub(r' data-m="[ps]\d+"', "", s["html"])

    own_guide = pdf_of(stem, "guide")
    topics = {}
    for t in sorted({q["topic"] for q in mc}, key=lambda t: [int(x) for x in t.split(".")]):
        p, s = t.split(".")
        gstem = STEM_OF["0" + p]
        g = pdf_of(gstem, "guide")
        nm = SECTIONS["0" + p][int(s) - 1]
        label = h(nm) + ("" if g == own_guide else f" <span class=\"muted\">(Part {p})</span>")
        topics[t] = (label, PAGES["0" + p][int(s)]) + (() if g == own_guide else (f"{g}#page={PAGES['0' + p][int(s)]}",))

    pdf = pdf_of(stem, kind)
    if kind == "questions":
        url = BASE + f"tests/{slug}/"
        f0 = fr[0]
        z = dict(title=f"AP English Language {part} Question Set: {name}",
                 h1=f'{part} <span style="white-space:nowrap">Question Set</span>', sub=name,
                 metaline=f"{len(mc)} multiple-choice on 3 passages (about 35 min) &middot; 1 {f0['kind'].lower()} essay ({f0['mins']} min)",
                 setupNote="Allow about 35 minutes for the multiple choice, about 80 seconds per question. The passage stays above each question; the paragraph or sentence a question cites is highlighted.",
                 desc=f"AP English Language {part}, {name}: {len(mc)} exam-style multiple-choice questions on three passages with in-depth explanations, plus a full {f0['kind'].lower()} essay with a six-point scoring guide.",
                 fr=fr, frWord="Question",
                 frIntro=f"Allow {f0['mins']} minutes. Write the whole essay in the box, then open the scoring guide and score it row by row: thesis (0&ndash;1), evidence and commentary (0&ndash;4), sophistication (0&ndash;1).",
                 foot_doc=f"{part}: {name}: Question Set")
        target = re.search(r"Target: (\d+)\+ MCQ", open(src, encoding="utf8").read())
        if target:
            z["target"] = dict(label="Target", mc=int(target.group(1)))
    else:
        url = BASE + f"tests/{slug}-checks/"
        z = dict(title=f"AP English Language {part} Guide Checks: {name}",
                 h1=f'{part} <span style="white-space:nowrap">Guide Checks</span>', sub=name,
                 metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"AP English Language {part}, {name}: the study guide's {len(mc)} section check questions as a quiz, with in-depth explanations.",
                 foot_doc=f"{part}: {name}")
    foot_doc = z.pop("foot_doc")
    z.update(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-lang.{slug}{'' if kind == 'questions' else '-checks'}.v1",
        runhead=f"AP English Language &middot; {part}: {name}" + (" &middot; Question Set" if kind == "questions" else " &middot; Guide checks"),
        back=("/study/#ap-english-language", "Study Library"), mc=mc, stims=stims, sections=sections, topics=topics,
        topicPrefix="", topicCol="Topic", guideCol="Guide section", byTopic="By topic",
        topicNote="Two or more misses on one topic: reread that section of the guide.",
        guide=own_guide, guideName=f"the <i>{part} guide</i>",
        foot=(f'From <a href="{pdf}"><i>{foot_doc}</i></a> (PDF). Answers and rule tags are the document&rsquo;s own key; '
              "the explanations expand on it and say why each wrong choice is wrong. "
              f'Topic links open the matching section of the guide. All passages are fictional, written for practice. Your answers are saved only in this browser.'),
    )
    return z


def review(stem, kind):
    """Plain dump of items, for writing explanations."""
    ev, _ = parse(os.path.join(ROOT, "source", f"{stem}-{kind}.tex"))
    n = 0
    for e in ev:
        if e[0] == "q":
            n += 1
            q = e[1]
            print(f"{n}. [{q['tag']}] {q['stem']}")
            for k, c in enumerate(q["choices"], 1):
                print(f"   {'*' if k == q['pos'] else '-'} {c}")


QUIZZES = [z for s in DOCS for k in ("guide", "questions")
           if os.path.exists(os.path.join(ROOT, "source", f"{s}-{k}.tex")) for z in [build(s, k)] if z]

if __name__ == "__main__":
    review(sys.argv[1], sys.argv[2])
