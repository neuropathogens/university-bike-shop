"""AP Chinese study series -> /study/ap/ap-chinese/tests/<slug>/.

  <unit>          the unit's Question Set (listening sets as transcripts, reading sets, one free-response task)
  <unit>-checks   the check questions at the end of each section of the unit's study guide

Items come from the series' Python content model (content/), the same objects build_tex.py renders to the
PDFs, so choices, letters and the key match the PDFs exactly. Topic links open the guide section's page
(pages.json, written by build_tex.py from the LaTeX labels).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ROOT))
from lib.latex import to_html  # noqa: E402
from ap_chinese.content import DOCS  # noqa: E402
from ap_chinese.model import topic_key  # noqa: E402

BASE = "/study/ap/ap-chinese/"
BLANK = '<span class="blank" role="img" aria-label="blank"></span>'
MACROS = {"textperiodcentered": "·", "blank": BLANK, "small": "", "footnotesize": "", "medskip": "", "smallskip": ""}
PAGES = json.load(open(os.path.join(ROOT, "pages.json")))
SLUG = {"00": "playbook", **{f"0{i}": f"unit-{i}" for i in range(1, 7)}}
# Question-set skill tallies link to Part 0, section 3 (interpretive skills)
SKILLS = {"1.A": "1.A Recognize explicit meaning: details, data", "1.B": "1.B Interpret: main idea, purpose, tone, word meaning",
          "1.C": "1.C Synthesize and infer"}


def h(s):
    return to_html(s, MACROS)


def guides():
    return {d.stem: d for d in DOCS if d.kind == "guide"}


def sec_titles(d):
    return {b[1]: b[3] for b in d.blocks if b[0] == "sec"}


def pdf_url(d):
    return BASE + f"ap-chinese-{d.stem}-{d.kind}.pdf"


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


def fr_item(f, n):
    total = sum(r[1] for r in f["rows"])
    stem = "".join(f"<p>{h(p)}</p>" for p in f["directions"])
    if f.get("panels"):
        stem += "<p><b>The four pictures</b> (described in words for this practice set):</p><ol>" + \
                "".join(f"<li>{h(p)}</li>" for p in f["panels"]) + "</ol>"
    stem += "".join(f"<p>{h(p)}</p>" for p in f.get("prompt", []))
    rubric = ('<table class="bt"><thead><tr><th scope="col">Row</th><th scope="col">Full credit</th>'
              '<th scope="col">Common reasons for losing points</th></tr></thead><tbody>' +
              "".join(f'<tr><th scope="row">{h(name)} ({pts})</th><td>{h(e)}</td><td>{h(m)}</td></tr>' for name, pts, e, m in f["rows"]) +
              f"</tbody></table><p>Add the rows: out of {total}. Give yourself a row's top score only if your response does what the descriptor says.</p>")
    sol = "".join(f"<p>{h(p)}</p>" for p in f["model"])
    if f.get("tips"):
        sol += "<p><i>Why it scores:</i> " + h(" ".join(f["tips"])) + "</p>"
    label = {"Story Narration": "story", "Email Response": "email", "Project Presentation": "presentation",
             "Project Q&A": "Q1–Q4"}[f["kind"]]
    return dict(n=n, mode="points", kind=f["kind"], mins=f["mins"],
                head=f"{f['kind'].replace('&', '&amp;')} &middot; {total} points &middot; about {f['mins']} minutes",
                guide=[], stem=stem,
                parts=[dict(label=label, max=total, prompt=h(f.get("ask", "Write your response in Chinese.")), solution=sol, rubric=rubric)])


def build(d):
    G = guides()
    unit = d.stem[:2]
    slug = SLUG[unit] + ("-checks" if d.kind == "guide" else "")
    url = BASE + f"tests/{slug}/"
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
            fr.append(fr_item(b[1], len(fr) + 1))
    assert left == 0, (d.stem, left)
    # topics
    topics = {}
    if d.kind == "questions" and unit != "00":
        p0 = G["00-exam-playbook"]
        for k in sorted({q["topic"] for q in mc}):
            topics[k] = (SKILLS[k], PAGES[p0.stem]["3"], pdf_url(p0) + f"#page={PAGES[p0.stem]['3']}")
        guide_link, guide_name = pdf_url(p0), "<i>Part 0</i>, section 3"
    else:
        titles = sec_titles(guide)
        for k in sorted({q["topic"] for q in mc}, key=int):
            topics[k] = (titles[int(k)], PAGES[guide.stem][k])
        guide_link, guide_name = pdf_url(guide), f"the <i>{guide.short} guide</i>"
    long_name = f"{d.short}: {d.sub}"
    if d.kind == "questions":
        nl = sum(1 for s in stims.values() if "Listening" in s["title"])
        nr = len(stims) - nl
        if stims:
            meta = (f"{len(mc)} multiple-choice in {len(stims)} sets ({nl} listening as transcripts, {nr} reading) "
                    f"&middot; 1 {fr[0]['kind'].lower()}")
            setup = ("Listening sets are printed as transcripts: read each once at normal speed, then answer without rereading. "
                     "Allow about 1 minute per listening item and 80 seconds per reading item.")
        else:
            meta = f"{len(mc)} language-control items &middot; 1 {fr[0]['kind'].lower()}"
            setup = "About 40 seconds per item. Every item drills a structure that the free-response language control row rewards."
        z = dict(title=f"AP Chinese {d.short} Question Set", h1=f'{d.short} <span style="white-space:nowrap">Question Set</span>',
                 sub=h(d.sub), metaline=meta, setupNote=setup,
                 desc=f"AP Chinese {long_name} question set: {len(mc)} multiple-choice questions with in-depth explanations, plus a {fr[0]['kind'].lower()} task with a scoring guide and model response.",
                 fr=fr, frWord="Question",
                 frIntro=f"Allow about {fr[0]['mins']} minutes. Write (or, for speaking tasks, say aloud and jot keywords), then open the scoring guide and give yourself the points your response earns.")
        if unit != "00":
            z.update(topicCol="Skill", byTopic="By skill", topicNote="Two or more misses on one skill: reread section 3 of Part 0, then redo those items.")
        else:
            z.update(topicCol="Topic", byTopic="By topic", topicNote="Two or more misses on one topic: reread that section of the Part 0 guide.")
    else:
        z = dict(title=f"AP Chinese {d.short} Guide Checks", h1=f'{d.short} <span style="white-space:nowrap">Guide Checks</span>',
                 sub=h(d.sub), metaline=f"{len(mc)} check questions from the end of each section of the guide",
                 setupNote="These are the guide&rsquo;s own section checks. Read the section first, then use them to confirm you have it.",
                 desc=f"AP Chinese {long_name}: the study guide's {len(mc)} section check questions as a quiz, with in-depth explanations.",
                 topicCol="Topic", byTopic="By topic", topicNote="Two or more misses on one topic: reread that section of the guide.")
    pdf = pdf_url(d)
    z.update(out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-chinese.{slug}.v1",
             runhead=f"AP Chinese &middot; {h(long_name)} &middot; " + ("Question Set" if d.kind == "questions" else "Guide checks"),
             back=("/study/#ap-chinese", "Study Library"), mc=mc, stims=stims, sections=sections, topics=topics,
             topicPrefix="", guideCol="Guide section", guide=guide_link, guideName=guide_name,
             foot=(f'From <a href="{pdf}"><i>{h(long_name)}{": Question Set" if d.kind == "questions" else ""}</i></a> (PDF). '
                   "Answers and rule tags are the document&rsquo;s own key; the explanations add the rule, how it applies, and why each wrong choice is wrong. "
                   "All passages, transcripts and prompts are original and written for practice. Your answers are saved only in this browser."))
    return z


def _placed():
    for d in DOCS:
        if not d.items() or "pos" not in d.items()[0]:
            d.place()
    return DOCS


QUIZZES = [build(d) for d in _placed()]
