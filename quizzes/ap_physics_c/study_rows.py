"""Write (or rewrite) the two Physics C sections of public/study/index.html from the built PDFs.

    python3 -I quizzes/ap_physics_c/study_rows.py     # then: python3 -I quizzes/link_study.py

Page counts and file sizes are read from the PDFs, so rerun this after texgen.py.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_physics_c.texgen import units, COURSE_DIR  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
INDEX = os.path.join(REPO, "public/study/index.html")
BLURB = {
    "mech": "Calculus-based mechanics, Units 1–7. Each unit has a study guide (notes, worked examples and section checks) and a question set (exam-style multiple choice and one full free-response question with a scoring guide). The four free-response types of the current exam each appear several times.",
    "em": "Calculus-based electricity and magnetism, Units 8–13, in the same format as Mechanics: a study guide and a question set for every unit, each question set ending with a full free-response question and an answer key.",
}
TITLE = {"mech": "Physics C: Mechanics", "em": "Physics C: Electricity and Magnetism"}
SID = {"mech": "ap-physics-c-mechanics", "em": "ap-physics-c-em"}


def info(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1)), size(path)


def size(path):
    b = os.path.getsize(path)
    return f"{b / 1048576:.1f} MB" if b >= 1048576 else f"{round(b / 1024)} KB"


def t(s):
    return s.replace("--", "–").replace("\\%", "%").replace("&", "&amp;")


def section(course):
    us = [u for u in units() if u.course == course]
    web = f"/study/ap/ap-physics-c/{COURSE_DIR[course]}/"
    disk = REPO + "/public" + web
    pack = f"ap-physc-{COURSE_DIR[course] if course == 'em' else 'mechanics'}-complete-pack.pdf"
    pn, ps = info(disk + pack)
    zs = size(REPO + "/public/study/ap/ap-physics-c/ap-physc-study-series.zip")
    rows = []
    for i, u in enumerate(us):
        gn, gs = info(disk + u.stem + "-guide.pdf")
        qn, qs = info(disk + u.stem + "-questions.pdf")
        sub = f"Topics {t(u.topics)}; {t(u.weight)}" + (" of the multiple-choice section" if i == 0 else "")
        rows.append(f'<tr><td class="num">{u.n}</td><td class="t"><a href="{web}{u.stem}-guide.pdf">Unit {u.n} Study Guide: {t(u.title)}</a><span class="sub">{sub}</span></td><td class="meta">{gn} pp</td><td class="meta">{gs}</td></tr>')
        rows.append(f'<tr><td class="num"></td><td class="t"><a href="{web}{u.stem}-questions.pdf">Unit {u.n} Question Set</a><span class="sub">Multiple choice plus {'an' if u.frq.kind[0] in 'AEIOUaeiou' else 'a'} {u.frq.kind.lower()} question on {u.frq_topic}; answer key with explanations</span></td><td class="meta">{qn} pp</td><td class="meta">{qs}</td></tr>')
    return (f'  <section class="subj" id="{SID[course]}">\n    <h3>{TITLE[course]}</h3>\n    <p class="blurb">{BLURB[course]}</p>\n'
            f'    <p class="all"><a class="btn" href="{web}{pack}">Complete pack, one PDF <span class="muted">· {pn} pp · {ps}</span></a>'
            f'<a class="btn" href="/study/ap/ap-physics-c/ap-physc-study-series.zip">All PDFs + LaTeX source, Mechanics + E&amp;M (.zip) <span class="muted">· {zs}</span></a></p>\n'
            '    <table class="docs"><tbody>\n' + "\n".join(rows) + "\n    </tbody></table>\n  </section>\n")


def main():
    h = open(INDEX, encoding="utf8").read()
    h = re.sub(r'  <section class="subj" id="ap-physics-c-[a-z]+">.*?</section>\n', "", h, flags=re.S)
    anchor = '  <section class="subj" id="ap-psychology">'
    h = h.replace(anchor, section("mech") + section("em") + anchor, 1)
    open(INDEX, "w", encoding="utf8").write(h)
    print("wrote the Physics C sections of /study")


if __name__ == "__main__":
    main()
