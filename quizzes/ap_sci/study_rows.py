"""Write (or rewrite) one course's section of public/study/index.html from its built PDFs.

    python3 -I quizzes/<family>/study_rows.py       # needs pypdf; then: python3 -I quizzes/link_study.py
"""
import os
import re

from ap_sci.texgen import REPO

INDEX = os.path.join(REPO, "public/study/index.html")


def size(path):
    b = os.path.getsize(path)
    return f"{b / 1048576:.1f} MB" if b >= 1048576 else f"{round(b / 1024)} KB"


def info(path):
    from pypdf import PdfReader
    return len(PdfReader(path).pages), size(path)


def t(s):
    return s.replace("--", "–").replace("\\%", "%").replace("\\&", "&amp;").replace("``", "“").replace("''", "”")


def section(C):
    web = f"/study/ap/{C.slug}/"
    disk = REPO + "/public" + web
    pn, ps = info(disk + C.prefix + "complete-pack.pdf")
    zs = size(disk + C.prefix + "study-series.zip")
    rows = []
    for i, u in enumerate(C.units()):
        gn, gs = info(disk + u.stem + "-guide.pdf")
        qn, qs = info(disk + u.stem + "-questions.pdf")
        sub = f"Topics {t(u.topics)}; {t(u.weight)}" + (" of the multiple-choice section" if i == 0 else "")
        art = "an" if u.frq.kind[0] in "AEIOUaeiou" else "a"
        rows.append(f'<tr><td class="num">{u.n}</td><td class="t"><a href="{web}{u.stem}-guide.pdf">Unit {u.n} Study Guide: {t(u.title)}</a><span class="sub">{sub}</span></td><td class="meta">{gn} pp</td><td class="meta">{gs}</td></tr>')
        rows.append(f'<tr><td class="num"></td><td class="t"><a href="{web}{u.stem}-questions.pdf">Unit {u.n} Question Set</a><span class="sub">Multiple choice plus {art} {t(u.frq.kind[0].lower() + u.frq.kind[1:])} question on {t(u.frq_topic)}; answer key with explanations</span></td><td class="meta">{qn} pp</td><td class="meta">{qs}</td></tr>')
    return (f'  <section class="subj" id="{C.slug}">\n    <h3>{C.heading}</h3>\n    <p class="blurb">{C.blurb}</p>\n'
            f'    <p class="all"><a class="btn" href="{web}{C.prefix}complete-pack.pdf">Complete pack, one PDF <span class="muted">· {pn} pp · {ps}</span></a>'
            f'<a class="btn" href="{web}{C.prefix}study-series.zip">All PDFs + LaTeX source (.zip) <span class="muted">· {zs}</span></a></p>\n'
            '    <table class="docs"><tbody>\n' + "\n".join(rows) + "\n    </tbody></table>\n  </section>\n")


def write_section(C):
    h = open(INDEX, encoding="utf8").read()
    h = re.sub(rf'  <section class="subj" id="{C.slug}">.*?</section>\n', "", h, flags=re.S)
    anchor = f'  <section class="subj" id="{C.before_id}">'
    assert h.count(anchor) == 1, anchor
    h = h.replace(anchor, section(C) + anchor, 1)
    open(INDEX, "w", encoding="utf8").write(h)
    print(f"wrote the {C.heading} section of /study ({2 * len(C.nums)} rows)")
