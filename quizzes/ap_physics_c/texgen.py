"""Write and compile the AP Physics C PDFs from the unit modules.

    python3 -I quizzes/ap_physics_c/texgen.py            # all 13 units + packs + source zip
    python3 -I quizzes/ap_physics_c/texgen.py 3 4        # just these units (no packs)

Writes latex/<stem>-{guide,questions}.tex, compiles with XeLaTeX (latexmk) in build/, copies the PDFs to
public/study/ap/ap-physics-c/{mechanics,em}/ and records each guide section's page in pages.json (the quiz
topic links open the guide at that page).
"""
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_physics_c.model import place  # noqa: E402

LATEX = os.path.join(HERE, "latex")
BUILD = os.path.join(HERE, "build")
PUBLIC = os.path.join(os.path.dirname(os.path.dirname(HERE)), "public", "study", "ap", "ap-physics-c")
COURSE_DIR = {"mech": "mechanics", "em": "em"}
FRQ_SHORT = {"Mathematical Routines": "MR", "Translation Between Representations": "TBR",
             "Experimental Design and Analysis": "EDA", "Qualitative/Quantitative Translation": "QQT"}


def units(nums=None):
    out = []
    for n in nums or range(1, 14):
        out.append(importlib.import_module(f"ap_physics_c.u{n:02d}").UNIT)
    return out


def plain_len(s):
    t = re.sub(r"\\[A-Za-z]+", "", s)
    return len(re.sub(r"[{}$\\^_ ]", "", t))


def q_env(q):
    short = max(plain_len(c) for c in q.choices) <= 24 and not any("\\frac" in c or "\\dfrac" in c for c in q.choices)
    ch = "\\chh" if short else "\\ch"
    choices = "".join("{" + c + "}" for c in q.choices)
    return f"\\begin{{q}}{{{q.pos}}}{{{q.tag}}}{{{q.why}}}\n{q.stem}\n{ch}{choices}\n\\end{{q}}\n"


def head(u, title, docpart):
    short = "AP Physics C: Mechanics" if u.course == "mech" else "AP Physics C: E\\&M"
    hp = docpart.split(" \\textperiodcentered\\ ")[:2]
    return (f"\\documentclass[11pt]{{article}}\n\\usepackage{{ap-physc}}\n\\course{{{u.course_name}}}\n"
            f"\\headcourse{{{short}}}\n\\headpart{{{' \\textperiodcentered\\ '.join(hp)}}}\n"
            f"\\title{{{title}}}\n\\author{{Paul Wang}}\n\\date{{November 2026}}\n\\docpart{{{docpart}}}\n\n"
            "\\begin{document}\n\\maketitle\n\n")


def guide_tex(u):
    checks = [q for s in u.sections for q in s.checks]
    place(checks)
    n = len(checks)
    out = [head(u, f"Unit {u.n}: {u.title}", f"Unit {u.n} \\textperiodcentered\\ Study Guide \\textperiodcentered\\ {u.weight} of MCQ")]
    out.append(f"\\begin{{abstract}}\n{u.abstract.strip()}\n\\end{{abstract}}\n\n")
    out.append(f"\\scoringline{{Check questions: \\blank\\ / \\qtotal \\qquad Target: {round(n * 0.8)}+ \\qquad Weakest topic: \\blank[8em]}}\n\n")
    for k, s in enumerate(u.sections, 1):
        out.append(f"\\section{{{s.title}}}\\label{{sec:{k}}}\n\n{s.body.strip()}\n\n")
        if s.checks:
            out.append("\\subsubsection{Check}\\mbox{}\n\n" + "".join(q_env(q) for q in s.checks) + "\n")
    out.append("\\makekey\n\\end{document}\n")
    return "".join(out)


def questions_tex(u):
    qs = [q for _, sq in u.qsections for q in sq]
    place(qs)
    n, f = len(qs), u.frq
    out = [head(u, f"Unit {u.n}: {u.title}: Question Set", f"Unit {u.n} \\textperiodcentered\\ Question Set")]
    abstract = (f"Exam-style practice on Unit {u.n} (topics {u.topics}), which is {u.weight} of the multiple-choice section. "
                f"Section~1--{len(u.qsections)} hold {n} four-choice multiple-choice questions grouped by topic; most need a short "
                f"calculation or a line of reasoning, as on the exam. The last page before the key is a full {f.kind} "
                f"free-response question ({f.pts} points). All items are original and written for practice. Use the AP equation "
                f"sheet and a calculator. Allow about {2 * n} minutes for the multiple choice (the exam's pace is about 2 minutes "
                f"per question) and {f.mins} minutes for the free response. The answer key explains every item and names its topic; "
                f"a scoring guide for the free response follows it.")
    out.append(f"\\begin{{abstract}}\n{abstract}\n\\end{{abstract}}\n\n")
    out.append(f"\\scoringline{{MCQ: \\blank\\ / \\qtotal \\qquad FRQ: \\blank\\ / {f.pts} \\qquad Target: {round(n * 0.7)}+ MCQ "
               f"\\qquad Pace: 2 min per MCQ}}\n\n")
    for title, sq in u.qsections:
        out.append(f"\\section{{{title}}}\n\n" + "".join(q_env(q) for q in sq) + "\n")
    out.append(f"\\section{{Free response}}\n\n\\begin{{frq}}{{Question 1 \\textperiodcentered\\ {f.kind} \\textperiodcentered\\ "
               f"{f.pts} points \\textperiodcentered\\ {f.mins} minutes}}\n{f.stem.strip()}\n\n"
               "\\begin{enumerate}[label=(\\alph*),leftmargin=2em,itemsep=4pt]\n")
    for p in f.parts:
        out.append(f"\\item {p.prompt.strip()} \\pts{{{p.pts}}}\n")
    out.append("\\end{enumerate}\n\\end{frq}\n\n\\makekey\n\n")
    out.append(f"\\subsection*{{Free-response scoring guide ({f.pts} points)}}\n\\small\n"
               "Award each point only when the answer does what the model does. Points are independent unless a part says otherwise; "
               "a correct method with an answer carried forward from an earlier error earns the later points.\n"
               "\\begin{scoring}\n")
    for p in f.parts:
        out.append(f"({p.label}) ({p.pts}) & {p.solution.strip()} & {p.miss.strip()} \\\\\n")
    out.append("\\end{scoring}\n\n\\end{document}\n")
    return "".join(out), qs


def compile_tex(name):
    env = dict(os.environ, TEXINPUTS=LATEX + "//:")
    r = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", f"-outdir={BUILD}",
                        os.path.join(LATEX, name + ".tex")], env=env, capture_output=True, text=True)
    if r.returncode:
        log = open(os.path.join(BUILD, name + ".log"), encoding="utf8", errors="replace").read()
        i = log.find("\n!")
        raise SystemExit(f"{name}: LaTeX failed\n{log[i:i + 1500] if i >= 0 else r.stdout[-2000:]}")
    return os.path.join(BUILD, name + ".pdf")


def section_pages(name):
    aux = open(os.path.join(BUILD, name + ".aux"), encoding="utf8").read()
    return {int(k): int(p) for k, p in re.findall(r"\\newlabel\{sec:(\d+)\}\{\{[^}]*\}\{(\d+)\}", aux)}


def npages(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def main(args):
    os.makedirs(BUILD, exist_ok=True)
    nums = [int(a) for a in args] or None
    pj = os.path.join(HERE, "pages.json")
    pages = json.load(open(pj)) if os.path.exists(pj) else {}
    for u in units(nums):
        dest = os.path.join(PUBLIC, COURSE_DIR[u.course])
        os.makedirs(dest, exist_ok=True)
        g = u.stem + "-guide"
        open(os.path.join(LATEX, g + ".tex"), "w").write(guide_tex(u))
        qtex, _ = questions_tex(u)
        qn = u.stem + "-questions"
        open(os.path.join(LATEX, qn + ".tex"), "w").write(qtex)
        for name in (g, qn):
            pdf = compile_tex(name)
            shutil.copy(pdf, os.path.join(dest, name + ".pdf"))
            print(f"  {name}.pdf  {npages(pdf)} pp  {os.path.getsize(pdf) // 1024} KB")
        pages[str(u.n)] = section_pages(g)
    json.dump(pages, open(pj, "w"), indent=1)
    if nums is None:
        packs()


def packs():
    for course, label in (("mech", "mechanics"), ("em", "em")):
        us = [u for u in units() if u.course == course]
        files = [os.path.join(PUBLIC, COURSE_DIR[course], f"{u.stem}-{k}.pdf") for u in us for k in ("guide", "questions")]
        out = os.path.join(PUBLIC, COURSE_DIR[course], f"ap-physc-{label}-complete-pack.pdf")
        subprocess.run(["pdfunite", *files, out], check=True)
        print(f"  {os.path.basename(out)}  {npages(out)} pp  {os.path.getsize(out) // 1024} KB")
    z = os.path.join(PUBLIC, "ap-physc-study-series.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(os.listdir(LATEX)):
            if f.endswith((".tex", ".sty")):
                zf.write(os.path.join(LATEX, f), f"ap-physc-study-series/latex/{f}")
        for course in ("mech", "em"):
            d = os.path.join(PUBLIC, COURSE_DIR[course])
            for f in sorted(os.listdir(d)):
                if f.endswith(".pdf") and "complete-pack" not in f:
                    zf.write(os.path.join(d, f), f"ap-physc-study-series/pdf/{f}")
        zf.writestr("ap-physc-study-series/latex/README.txt", README)
    print(f"  {os.path.basename(z)}  {os.path.getsize(z) // 1024} KB")


README = """AP Physics C study series (Mechanics Units 1-7, E&M Units 8-13), Paul Wang, November 2026.

Each unit has a Study Guide (notes + section checks) and a Question Set (multiple choice + one free-response
question with a scoring guide). Compile any file with XeLaTeX:  latexmk -xelatex <file>.tex
(needs ap-physc.sty beside it, TeX Gyre Pagella and Inter fonts).

The .tex files are generated from a Python content model (one module per unit) that also builds the
interactive quizzes on universitybikeshop.com/study. A question is
  \\begin{q}{<correct position 1-4>}{<topic tag>}{<why>} stem \\ch{A}{B}{C}{D} \\end{q}
and the letters, answer key and question total are generated from it.
"""

if __name__ == "__main__":
    main(sys.argv[1:])
