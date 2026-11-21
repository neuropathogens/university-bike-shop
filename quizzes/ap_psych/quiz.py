"""AP Psychology study series -> /study/ap/ap-psychology/tests/<slug>/.

  <unit>          the unit's Question Set (MC + shared data displays + the 7-point EBQ)
  <unit>-checks   the check questions at the end of each section of the unit's guide

Items are parsed from the series' own LaTeX (source/, copied from ap-psych-study-series.zip). Choices are
in source order (the PDFs do not shuffle), so letters match the PDF keys. Explanations: ex_<file>.py.
"""
import importlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ROOT))
from lib.latex import to_html  # noqa: E402

BASE = "/study/ap/ap-psychology/"
BLANK = '<span class="blank" role="img" aria-label="blank"></span>'
MACROS = {"textperiodcentered": "·", "blank": BLANK, "small": "", "footnotesize": "", "medskip": "", "smallskip": ""}

# file stem -> (slug, short name, guide section pages {section number: physical page})
UNITS = {
    "00-research-methods": ("research-methods", "Research Methods &amp; Data", {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}),
    "01-biological-bases": ("unit-1", "Unit 1: Biological Bases of Behavior", {1: 1, 2: 2, 3: 2, 4: 4, 5: 6, 6: 7}),
    "02-cognition": ("unit-2", "Unit 2: Cognition", {1: 1, 2: 2, 3: 4, 4: 4, 5: 5, 6: 6, 7: 6, 8: 7}),
    "03-development-learning": ("unit-3", "Unit 3: Development and Learning", {1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 4, 7: 6, 8: 7, 9: 8}),
    "04-social-personality": ("unit-4", "Unit 4: Social Psychology and Personality", {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}),
    "05-mental-physical-health": ("unit-5", "Unit 5: Mental and Physical Health", {1: 1, 2: 2, 3: 2, 4: 3, 5: 6}),
}
# number of items after each data display that refer to it, per question set
STIM_COUNTS = {"00-research-methods": [3, 4], "01-biological-bases": [2], "02-cognition": [3],
               "03-development-learning": [3], "04-social-personality": [2], "05-mental-physical-health": [3]}
TARGET = {"00-research-methods": None}


def h(s):
    return to_html(s, MACROS)


def group(s, i):
    """Return (content, end) of the {...} group starting at s[i] == '{'."""
    assert s[i] == "{", s[i:i + 30]
    depth = 0
    j = i
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
    """\\begin{tabular}{..} rows \\end{tabular} (booktabs) -> booktabs-style HTML table."""
    body = re.search(r"\\begin\{tabular\}\{[^}]*\}(.*?)\\end\{tabular\}", tex, re.S).group(1)
    body = re.sub(r"\\(toprule|bottomrule)", "", body)
    parts = re.split(r"\\midrule", body)
    def rows(chunk):
        return [r.strip() for r in re.split(r"\\\\", chunk) if r.strip()]
    head = rows(parts[0]) if len(parts) > 1 else []
    data = rows(parts[-1])
    out = ['<table class="bt">']
    if head:
        out.append("<thead>" + "".join("<tr>" + "".join(f'<th scope="col">{h(c.strip())}</th>' for c in re.split(r"(?<!\\)&", r)) + "</tr>" for r in head) + "</thead>")
    out.append("<tbody>")
    for r in data:
        cells = [c.strip() for c in re.split(r"(?<!\\)&", r)]
        out.append("<tr>" + f'<th scope="row">{h(cells[0])}</th>' + "".join(f"<td>{h(c)}</td>" for c in cells[1:]) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def stim_html(tex):
    tex = tex.strip()
    out = []
    for piece in re.split(r"(\\begin\{center\}.*?\\end\{center\})", tex, flags=re.S):
        if piece.startswith("\\begin{center}"):
            out.append('<div class="bt-wrap">' + tabular_html(piece) + "</div>")
        elif piece.strip():
            out.append("<p>" + h(piece) + "</p>")
    return "".join(out)


def parse(path):
    """Ordered events: ('section', title) / ('stim', tex) / ('q', dict) / ('frq', title, body); plus tail after \\makekey."""
    t = open(path, encoding="utf8").read()
    body = t[t.index("\\begin{document}"):]
    key_at = body.find("\\makekey")
    main, tail = (body[:key_at], body[key_at:]) if key_at >= 0 else (body, "")
    ev = []
    pat = re.compile(r"\\section\{|\\begin\{stimulus\}|\\begin\{q\}|\\begin\{frq\}")
    i = 0
    while True:
        m = pat.search(main, i)
        if not m:
            break
        tok = m.group(0)
        if tok == "\\section{":
            title, i = group(main, m.end() - 1)
            ev.append(("section", title))
        elif tok == "\\begin{stimulus}":
            end = main.index("\\end{stimulus}", m.end())
            ev.append(("stim", main[m.end():end]))
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


def topic_of(tag):
    code = tag.split()[0].split("/")[0]
    return code


def load_ex(stem, kind):
    mod = f"ap_psych.ex_{stem.replace('-', '_')}_{kind}"
    try:
        return importlib.import_module(mod).EX
    except ModuleNotFoundError:
        return None


def norm(s):
    """Ignore a leading LaTeX quote or math opener when matching explanation keys."""
    return re.sub(r"^(?:``|\\\(|\s)+", "", s)


def match(key, opts):
    if key in opts:
        return key
    hits = [o for o in opts if norm(o).startswith(norm(key))]
    if len(hits) != 1:
        raise SystemExit(f"explanation key {key!r} matches {len(hits)} of {opts}")
    return hits[0]


def ebq(frq_body, tail):
    """The Question Set's free response (EBQ or AAQ): stem (directions/sources) + parts scored in points."""
    b = re.sub(r"^\s*\\small\s*", "", frq_body)
    lst = re.search(r"\\begin\{enumerate\}\[[^\]]*\](.*?)\\end\{enumerate\}", b, re.S)
    stem_tex = b[:lst.start()]
    paras = [x.strip() for x in re.split(r"\n\s*\n|\\medskip", stem_tex) if x.strip()]
    stem = "".join(f"<p>{h(x)}</p>" for x in paras)
    items = [x.strip() for x in re.split(r"\\item\s", lst.group(1)) if x.strip()]
    letters = "ABCDEF"
    prompts = []
    for k, x in enumerate(items):
        m = re.match(r"\(i\)\s*(.*?)\s*\(ii\)\s*(.*)", x, re.S)
        if m:
            prompts += [(f"{letters[k]}(i)", h(m.group(1))), (f"{letters[k]}(ii)", h(m.group(2)))]
        else:
            prompts.append((letters[k], h(x)))
    cm = re.search(r"\\begin\{compare\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{compare\}", tail, re.S)
    good, bad = h(cm.group(2)), h(cm.group(3))
    rows = [r.strip() for r in re.split(r"\\\\", cm.group(4)) if r.strip()]
    parsed = []
    for r in rows:
        cells = [c.strip() for c in re.split(r"(?<!\\)&", r)]
        m = re.match(r"([A-F](?:\((?:i|ii)\))?)\.?\s*(.*?)\s*\((\d)\)$", cells[0])
        parsed.append((m.group(1), int(m.group(3)), h(cells[1]), h(cells[2])))
    assert [x[0] for x in parsed] == [x[0] for x in prompts], ([x[0] for x in parsed], [x[0] for x in prompts])
    parts = []
    for (lab, pts, earns, miss), (_, pr) in zip(parsed, prompts):
        parts.append(dict(label=lab, max=pts, prompt=pr,
                          solution=f"<p><b>{good}:</b> {earns}</p>",
                          rubric=f"<p><b>{bad}:</b> {miss}</p><p>Worth {pts} point{'s' if pts > 1 else ''}. Give yourself full credit only if your answer does what the model does.</p>"))
    return stem, parts


def build_quiz(stem_name, kind):
    slug, uname, pages = UNITS[stem_name]
    src = os.path.join(ROOT, "source", f"{stem_name}-{kind}.tex")
    ev, tail = parse(src)
    ex = load_ex(stem_name, kind)
    if ex is None:
        return None
    qs = [e[1] for e in ev if e[0] == "q"]
    assert len(ex) == len(qs), (stem_name, kind, len(ex), len(qs))
    sections, stims, mc = {}, {}, []
    sec = 0
    stim_counts = list(STIM_COUNTS.get(stem_name, [])) if kind == "questions" else []
    cur_stim, left = None, 0
    n = 0
    fr = []
    for e in ev:
        if e[0] == "section":
            if e[1].strip() == "Evidence-Based Question":
                continue
            sec += 1
            sections[sec] = h(re.sub(r"\s*\([^)]*\)\s*$", "", e[1]))
        elif e[0] == "stim":
            sid = f"s{len(stims) + 1}"
            stims[sid] = dict(title="Data display" if "tabular" in e[1] else "Study", html=stim_html(e[1]))
            cur_stim, left = sid, stim_counts.pop(0)
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
            item = dict(n=n, sec=sec, topic=topic_of(q["tag"]), tag=h(q["tag"]), prompt=h(q["stem"]),
                        options=[h(c) for c in q["choices"]], answer=q["pos"] - 1,
                        ex=dict(idea=x["idea"], steps=x["steps"], others={q["choices"].index(w): v for w, v in mapped.items()}))
            if left > 0:
                item["stim"] = cur_stim
                left -= 1
            mc.append(item)
        elif e[0] == "frq":
            st, parts = ebq(e[2], tail)
            qn = int(re.search(r"Question (\d+)", e[1]).group(1))
            kind_fr, pts_fr, mins_fr = re.search(r"(EBQ|AAQ)\D*(\d+) points\D*(\d+) minutes", e[1]).groups()
            fr_name = {"EBQ": "Evidence-Based Question", "AAQ": "Article Analysis Question"}[kind_fr]
            fr.append(dict(n=qn, mode="points", kind=fr_name, mins=int(mins_fr), head=f"{fr_name} &middot; {pts_fr} points &middot; {mins_fr} minutes",
                           guide=[], stem=st, parts=parts))
    assert not stim_counts, stim_counts
    unit_no = stem_name[:2]
    guide = BASE + f"ap-psych-{stem_name}-guide.pdf"
    pdf = BASE + f"ap-psych-{stem_name}-{kind}.pdf"
    topics = {}
    for q in mc:
        t = q["topic"]
        if t in topics:
            continue
        k = int(t.split("-")[1]) if t.startswith("RM-") else int(t.split(".")[1])
        name = re.sub(r"\s*\([^)]*\)\s*$", "", GUIDE_SECTIONS[stem_name][k - 1])
        topics[t] = (h(name), pages[k])
    order = sorted(topics, key=lambda t: [int(x) for x in re.findall(r"\d+", t)])
    topics = {t: topics[t] for t in order}
    if kind == "questions":
        url = BASE + f"tests/{slug}/"
        title = f"AP Psychology {uname.split(':')[0]} Question Set" if slug != "research-methods" else "AP Psychology Research Methods Question Set"
        h1 = (uname.split(":")[0] if slug != "research-methods" else "Research Methods") + ' <span style="white-space:nowrap">Question Set</span>'
        target = re.search(r"Target: (\d+)\+ MCQ", open(src, encoding="utf8").read())
        z = dict(title=title.replace("&amp;", "&"), h1=h1,
                 sub=uname.split(": ")[-1] if slug != "research-methods" else "Research Methods &amp; Data",
                 metaline=f"{len(mc)} multiple-choice (about 30 min) &middot; 1 {fr[0]['kind'].lower()} ({fr[0]['mins']} min)",
                 setupNote="Allow about 30 minutes for the multiple choice, about 72 seconds per question. Data-display items show the study above the question.",
                 desc=f"AP Psychology {uname.replace('&amp;', '&')} question set: {len(mc)} exam-style multiple-choice questions with in-depth explanations, plus a 7-point {fr[0]['kind'].lower()} with a scoring guide.",
                 fr=fr, frIntro=f"Allow {fr[0]['mins']} minutes. Write each part, then open the scoring guide and give yourself the points your answer earns. Cite sources by author and year.",
                 foot_doc=f"{uname}: Question Set")
        if target:
            z["target"] = dict(label="Target", mc=int(target.group(1)))
    else:
        url = BASE + f"tests/{slug}-checks/"
        z = dict(title=f"AP Psychology {uname.split(':')[0] if slug != 'research-methods' else 'Research Methods'} Guide Checks".replace("&amp;", "&"),
                 h1=(uname.split(":")[0] if slug != "research-methods" else "Research Methods") + ' <span style="white-space:nowrap">Guide Checks</span>',
                 sub=uname.split(": ")[-1] if slug != "research-methods" else "Research Methods, Statistics &amp; the FRQs",
                 metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"AP Psychology {uname.replace('&amp;', '&')}: the study guide's {len(mc)} section check questions as a quiz, with in-depth explanations.",
                 foot_doc=f"{uname}" + ("" if slug == "research-methods" else ""))
    foot_doc = z.pop("foot_doc")
    z.update(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-psych.{slug}{'' if kind == 'questions' else '-checks'}.v1",
        runhead=f"AP Psychology &middot; {uname}" + (" &middot; Question Set" if kind == "questions" else " &middot; Guide checks"),
        back=("/study/#ap-psychology", "Study Library"), mc=mc, stims=stims, sections=sections, topics=topics,
        topicPrefix="", topicCol="Topic", guideCol="Guide section", byTopic="By topic",
        topicNote="Two or more misses on one topic: reread that section of the guide.",
        guide=guide, guideName="the <i>" + ("Research Methods guide" if slug == "research-methods" else uname.split(":")[0] + " guide") + "</i>",
        foot=(f'From <a href="{pdf}"><i>{foot_doc}</i></a> (PDF). Answers and rule tags are the document&rsquo;s own key; '
              "the explanations expand on it with the concept, how it applies to the scenario, and why each wrong choice is wrong. "
              f'Topic links open the matching section of <a href="{guide}">the guide</a>. Your answers are saved only in this browser.'),
    )
    return z


def guide_sections():
    out = {}
    for stem_name in UNITS:
        t = open(os.path.join(ROOT, "source", f"{stem_name}-guide.tex"), encoding="utf8").read()
        out[stem_name] = re.findall(r"\\section\{([^}]*)\}", t)
    return out


GUIDE_SECTIONS = guide_sections()


def review(stem_name, kind):
    """Plain dump of items, for writing explanations."""
    ev, _ = parse(os.path.join(ROOT, "source", f"{stem_name}-{kind}.tex"))
    n = 0
    for e in ev:
        if e[0] == "q":
            n += 1
            q = e[1]
            print(f"{n}. [{q['tag']}] {q['stem']}")
            for k, c in enumerate(q["choices"], 1):
                print(f"   {'*' if k == q['pos'] else '-'} {c}")
            print(f"   > {q['why']}")
        elif e[0] == "stim":
            print("STIM:", e[1].strip()[:400])


QUIZZES = [z for s in UNITS for k in ("questions", "guide") for z in [build_quiz(s, k)] if z]

if __name__ == "__main__":
    review(sys.argv[1], sys.argv[2])
