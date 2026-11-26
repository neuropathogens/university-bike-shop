"""Quiz pages for one AP world language series (a family such as ap_spanish): /study/ap/<slug>/tests/<slug>/.

  playbook, unit-N          each Question Set (listening sets as transcripts, reading sets, one free-response task)
  playbook-checks, unit-N-checks   the check questions at the end of each section of the study guides

Items come from the family's Python content model (content/pNN.py, built on ap_wl.model), the same objects
ap_wl.texbuild renders to the PDFs, so choices, letters and the key match the PDFs exactly. Topic links open the
guide section's page (the family's pages.json, written by its build_tex.py). Generalized from quizzes/ap_chinese.
"""
import json

from lib.latex import to_html
from ap_wl.model import topic_key

BLANK = '<span class="blank" role="img" aria-label="blank"></span>'
MACROS = {"textperiodcentered": "·", "blank": BLANK, "small": "", "footnotesize": "", "medskip": "", "smallskip": ""}
SLUG = {"00": "playbook", **{f"0{i}": f"unit-{i}" for i in range(1, 10)}}
# Question-set skill tallies link to Part 0, section 3 (interpretive skills)
SKILLS = {"1.A": "1.A Recognize explicit meaning: details, data", "1.B": "1.B Interpret: main idea, purpose, tone, word meaning",
          "1.C": "1.C Synthesize and infer"}


EXAMNO = {"Project Presentation": 1, "Project Q&A": 2, "Argumentative Essay": 3, "Story Narration": 3, "Email Response": 4,
          # AP Spanish Literature and Culture
          "Text Explanation": 1, "Text and Art Comparison": 2, "Analysis of a Single Text": 3, "Text Comparison": 4,
          # AP Latin
          "Short Answer": 1, "Translation": 2, "Short Essay": 3, "Project Prose Passage Short Essay": 4,
          "Project Poetry Passage Short Essay": 5}


def h(s):
    return to_html(s, MACROS)


def sec_titles(d):
    return {b[1]: b[3] for b in d.blocks if b[0] == "sec"}


def pdf_url(L, d):
    return L.base + f"{L.prefix}{d.stem}-{d.kind}.pdf"


def table_html(table):
    head, rows = table
    out = ['<div class="bt-wrap"><table class="bt"><thead><tr>', "".join(f'<th scope="col">{h(c)}</th>' for c in head),
           "</tr></thead><tbody>"]
    for r in rows:
        out.append("<tr>" + f'<th scope="row">{h(r[0])}</th>' + "".join(f"<td>{h(c)}</td>" for c in r[1:]) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def stim_html(s):
    html = "".join(f"<p>{h(p)}</p>" for p in s["paras"])
    if s.get("table"):
        html += table_html(s["table"])
    if s.get("note"):
        html += f"<p><i>{h(s['note'])}</i></p>"
    return html


def fr_item(L, f, n):
    total = sum(r[1] for r in f["rows"])
    stem = "".join(f"<p>{h(p)}</p>" for p in f["directions"])
    if f.get("panels"):
        stem += "<p><b>The four pictures</b> (described in words for this practice set):</p><ol>" + \
                "".join(f"<li>{h(p)}</li>" for p in f["panels"]) + "</ol>"
    for s in f.get("sources", []):
        stem += f'<div class="stim"><p class="stim-h">{h(s["title"])}</p>' + "".join(f"<p>{h(p)}</p>" for p in s["paras"])
        if s.get("table"):
            stem += table_html(s["table"])
        stem += "</div>"
    stem += "".join(f"<p>{h(p)}</p>" for p in f.get("prompt", []))
    rubric = ('<div class="bt-wrap"><table class="bt"><thead><tr><th scope="col">Row</th><th scope="col">Full credit</th>'
              '<th scope="col">Common reasons for losing points</th></tr></thead><tbody>' +
              "".join(f'<tr><th scope="row">{h(name)} ({pts})</th><td>{h(e)}</td><td>{h(m)}</td></tr>' for name, pts, e, m in f["rows"]) +
              f"</tbody></table></div><p>Add the rows: out of {total}. Give yourself a row's top score only if your response does what the descriptor says.</p>")
    sol = "".join(f"<p>{h(p)}</p>" for p in f["model"])
    if f.get("tips"):
        sol += "<p><i>Why it scores:</i> " + h(" ".join(f["tips"])) + "</p>"
    label = {"Story Narration": "story", "Email Response": "email", "Project Presentation": "presentation",
             "Project Q&A": "Q1–Q4", "Argumentative Essay": "essay",
             "Text Explanation": "short answer", "Text and Art Comparison": "short answer",
             "Analysis of a Single Text": "essay", "Text Comparison": "essay",
             "Short Answer": "answers", "Translation": "translation", "Short Essay": "essay",
             "Project Prose Passage Short Essay": "essay", "Project Poetry Passage Short Essay": "essay"}.get(f["kind"], f.get("label", "response"))
    n = EXAMNO.get(f["kind"], n)  # show the task's question number on the exam
    return dict(n=n, mode="points", kind=f["kind"], mins=f["mins"],
                head=f"{f['kind'].replace('&', '&amp;')} &middot; {total} points &middot; about {f['mins']} minutes",
                guide=[], stem=stem,
                parts=[dict(label=label, max=total, prompt=h(f.get("ask", L.ask)), solution=sol, rubric=rubric)])


def build(L, DOCS, PAGES, d):
    G = {g.stem: g for g in DOCS if g.kind == "guide"}
    unit = d.stem[:2]
    slug = SLUG[unit] + ("-checks" if d.kind == "guide" else "")
    url = L.base + f"tests/{slug}/"
    guide = G[d.stem]
    sections, stims, mc, fr = {}, {}, [], []
    cur, left, sec, n = None, 0, 0, 0
    for b in d.blocks:
        if b[0] == "sec":
            sec = b[1]
            sections[sec] = h(b[3])
        elif b[0] == "src":
            sid = f"s{len(stims) + 1}"
            stims[sid] = dict(title=h(b[1]["title"]), html=stim_html(b[1]))
            cur, left = sid, b[1]["n"]
        elif b[0] == "q":
            q = b[1]
            n += 1
            ch = q["choices"]
            notes = dict(q["wrongs"])
            key = topic_key(q["tag"])
            if d.kind == "guide" and key != str(sec):
                raise SystemExit(f"{d.stem} guide item {n}: tag {q['tag']!r} is in section {sec}")
            if d.kind == "questions" and unit != "00":
                key = key[:3]
            item = dict(n=n, sec=sec, topic=key, tag=h(q["tag"]), prompt=h(q["stem"]), options=[h(c) for c in ch],
                        answer=q["pos"] - 1,
                        ex=dict(idea=h(q["idea"]), steps=[h(s) for s in q["steps"]],
                                others={i: h(notes[c]) for i, c in enumerate(ch) if c != q["right"]}))
            if left > 0:
                item["stim"] = cur
                left -= 1
            mc.append(item)
        elif b[0] == "frq":
            fr.append(fr_item(L, b[1], len(fr) + 1))
    assert left == 0, (d.stem, left)
    # topics
    topics = {}
    if d.kind == "questions" and unit != "00":
        p0 = G["00-exam-playbook"]
        for k in sorted({q["topic"] for q in mc}):
            topics[k] = ((L.skills or SKILLS)[k], PAGES[p0.stem]["3"], pdf_url(L, p0) + f"#page={PAGES[p0.stem]['3']}")
        guide_link, guide_name = pdf_url(L, p0), "<i>Part 0</i>, section 3"
    else:
        titles = sec_titles(guide)
        for k in sorted({q["topic"] for q in mc}, key=int):
            topics[k] = (h(titles[int(k)]), PAGES[guide.stem][k])
        guide_link, guide_name = pdf_url(L, guide), f"the <i>{guide.short} guide</i>"
    long_name = f"{d.short}: {d.sub}"
    if d.kind == "questions":
        nl = sum(1 for s in stims.values() if "Listening" in s["title"])
        nr = len(stims) - nl
        if stims:
            sets = f"({nl} listening as transcripts, {nr} reading) " if nl else ""
            meta = (f"{len(mc)} multiple-choice in {len(stims)} sets {sets}"
                    f"&middot; 1 {task_name(fr[0]['kind'])}")
            setup = L.setup or ("Listening sets are printed as transcripts: read each once at normal speed, then answer without rereading. "
                                "Allow about 1 minute per listening item and 80 seconds per reading item.")
        else:
            meta = f"{len(mc)} language-control items &middot; 1 {task_name(fr[0]['kind'])}"
            setup = "About 40 seconds per item. Every item drills a structure that the free-response language control row rewards."
        z = dict(title=f"{L.short} {d.short} Question Set", h1=f'{d.short} <span style="white-space:nowrap">Question Set</span>',
                 sub=h(d.sub), metaline=meta, setupNote=setup,
                 desc=f"{L.short} {long_name} question set: {len(mc)} multiple-choice questions with in-depth explanations, plus a {task_name(fr[0]['kind'])} task with a scoring guide and model response.",
                 fr=fr, frWord="Question",
                 frIntro=f"Allow about {fr[0]['mins']} minutes. Write (or, for speaking tasks, say aloud and jot keywords), then open the scoring guide and give yourself the points your response earns.")
        if unit != "00":
            z.update(topicCol="Skill", byTopic="By skill", topicNote="Two or more misses on one skill: reread section 3 of Part 0, then redo those items.")
        else:
            z.update(topicCol="Topic", byTopic="By topic", topicNote="Two or more misses on one topic: reread that section of the Part 0 guide.")
    else:
        z = dict(title=f"{L.short} {d.short} Guide Checks", h1=f'{d.short} <span style="white-space:nowrap">Guide Checks</span>',
                 sub=h(d.sub), metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"{L.short} {long_name}: the study guide's {len(mc)} section check questions as a quiz, with in-depth explanations.",
                 topicCol="Topic", byTopic="By topic", topicNote="Two or more misses on one topic: reread that section of the guide.")
    pdf = pdf_url(L, d)
    z.update(out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.{L.slug}.{slug}.v1",
             runhead=f"{L.short} &middot; {h(long_name)} &middot; " + ("Question Set" if d.kind == "questions" else "Guide checks"),
             back=(f"/study/#{L.slug}", "Study Library"), mc=mc, stims=stims, sections=sections, topics=topics,
             topicPrefix="", guideCol="Guide section", guide=guide_link, guideName=guide_name,
             foot=(f'From <a href="{pdf}"><i>{h(long_name)}{": Question Set" if d.kind == "questions" else ""}</i></a> (PDF). '
                   "Answers and rule tags are the document&rsquo;s own key; the explanations add the rule, how it applies, and why each wrong choice is wrong. "
                   "All passages, transcripts and prompts are original and written for practice. Your answers are saved only in this browser."))
    if L.cjk:  # kana and kanji fall through the Latin fonts to a Japanese font (not a Chinese fallback)
        z["head_extra"] = JA_FONTS
    return z


JA_FONTS = ('<style>html:root{--serif:"Latin Modern","Computer Modern Serif","CMU Serif",Georgia,"Hiragino Mincho ProN",'
            '"Yu Mincho","YuMincho","Noto Serif JP","Noto Serif CJK JP",serif}</style>')


def task_name(kind):
    """'Project Q&A' -> 'project Q&A' (keep the acronym), 'Argumentative Essay' -> 'argumentative essay'."""
    return kind.lower().replace("q&a", "Q&A")


def build_all(L, DOCS, pages_path):
    """The family's QUIZZES."""
    pages = json.load(open(pages_path))
    for d in DOCS:
        if not d.items() or "pos" not in d.items()[0]:
            d.place()
    return [build(L, DOCS, pages, d) for d in DOCS]
