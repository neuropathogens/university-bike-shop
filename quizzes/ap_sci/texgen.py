"""Write and compile a course's PDFs from its unit modules (tectonic, deterministic), then publish them.

    python3 -I quizzes/<family>/build_tex.py          # all units, then the complete pack and the LaTeX zip
    python3 -I quizzes/<family>/build_tex.py 3 4      # just these units (no publish)

.tex files and build products go to quizzes/<family>/tex/out/ (not committed). Each guide section's page is
recorded in quizzes/<family>/pages.json (the quiz topic links open the guide at that page). Publishing copies the
PDFs to public/study/ap/<slug>/ and rebuilds <prefix>complete-pack.pdf and <prefix>study-series.zip.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

from ap_sci import figs
from ap_sci.model import place

ENGINE = os.path.dirname(os.path.abspath(__file__))
STY = os.path.join(ENGINE, "tex", "ap-sci.sty")
REPO = os.path.dirname(os.path.dirname(ENGINE))


def plain_len(s):
    t = re.sub(r"\\[A-Za-z]+", "", s)
    return len(re.sub(r"[{}$\\^_ ]", "", t))


def q_env(q):
    short = max(plain_len(c) for c in q.choices) <= 24 and not any("\\frac" in c or "\\dfrac" in c for c in q.choices)
    ch = "\\chh" if short else "\\ch"
    choices = "".join("{" + c + "}" for c in q.choices)
    fig = figs.tex(q.fig) if q.fig else ""
    return f"\\begin{{q}}{{{q.pos}}}{{{q.tag}}}{{{q.why}}}\n{q.stem}\n{fig}{ch}{choices}\n\\end{{q}}\n"


def head(C, u, title, docpart):
    hp = docpart.split(" \\textperiodcentered\\ ")[:2]
    return (f"\\documentclass[11pt]{{article}}\n\\usepackage{{ap-sci}}\n\\course{{{C.name}}}\n"
            f"\\headcourse{{{C.tex_short}}}\n\\headpart{{{' \\textperiodcentered\\ '.join(hp)}}}\n"
            f"\\title{{{title}}}\n\\author{{Paul Wang}}\n\\date{{November 2026}}\n\\docpart{{{docpart}}}\n\n"
            "\\begin{document}\n\\maketitle\n\n")


def guide_tex(C, u):
    checks = u.checks
    place(checks)
    n = len(checks)
    out = [head(C, u, f"Unit {u.n}: {u.title}", f"Unit {u.n} \\textperiodcentered\\ Study Guide \\textperiodcentered\\ {u.weight} of MCQ")]
    out.append(f"\\begin{{abstract}}\n{u.abstract.strip()}\n\\end{{abstract}}\n\n")
    out.append(f"\\scoringline{{Check questions: \\blank\\ / \\qtotal \\qquad Target: {round(n * 0.8)}+ \\qquad Weakest topic: \\blank[8em]}}\n\n")
    for k, s in enumerate(u.sections, 1):
        out.append(f"\\section{{{s.title}}}\\label{{sec:{k}}}\n\n{s.body.strip()}\n\n")
        if s.checks:
            out.append("\\needspace{14\\baselineskip}\\subsubsection{Check}\\mbox{}\n\n" + "".join(q_env(q) for q in s.checks) + "\n")
    out.append("\\makekey\n\\end{document}\n")
    return "".join(out)


def stim_tex(s):
    title = f"{{\\sffamily\\bfseries\\color{{navy}}{s.stim_title}}}\\par\\smallskip\n" if s.stim_title else ""
    fig = figs.tex(s.fig) if s.fig else ""
    body = (s.stim or "").strip()
    if "[[fig]]" in body:
        body, fig = body.replace("[[fig]]", fig), ""
    return f"\\begin{{stimulus}}\n{title}{body}\n{fig}\\end{{stimulus}}\n"


def frq_stem_tex(f):
    fig = figs.tex(f.fig) if f.fig else ""
    stem = f.stem.strip()
    return stem.replace("[[fig]]", fig) if "[[fig]]" in stem else stem + ("\n\n" + fig if fig else "")


def label(p):
    return p.label if p.label.startswith("(") else f"({p.label})"


def questions_tex(C, u):
    qs = u.questions
    place(qs)
    n, f = len(qs), u.frq
    sets = sum(1 for s in u.qsections if s.stim or s.fig)
    out = [head(C, u, f"Unit {u.n}: {u.title}: Question Set", f"Unit {u.n} \\textperiodcentered\\ Question Set")]
    setnote = (f" {'One section is a set' if sets == 1 else f'{sets} sections are sets'} built on a shared stimulus (data, a graph or a "
               f"described experiment), as on the exam." if sets else "")
    abstract = (f"Exam-style practice on Unit {u.n} (topics {u.topics}), which is {u.weight} of the multiple-choice section. "
                f"Sections~1--{len(u.qsections)} hold {n} four-choice multiple-choice questions grouped by topic.{setnote} "
                f"The last page before the key is a full {f.kind} free-response question ({f.pts} points). All items are original "
                f"and written for practice. {C.tools} Allow about {round(C.pace * n)} minutes for the multiple choice (the exam gives "
                f"{C.exam_mc}) and {f.mins} minutes for the free response. The answer key explains every item and names its topic; "
                f"a scoring guide for the free response follows it.")
    out.append(f"\\begin{{abstract}}\n{abstract}\n\\end{{abstract}}\n\n")
    out.append(f"\\scoringline{{MCQ: \\blank\\ / \\qtotal \\qquad FRQ: \\blank\\ / {f.pts} \\qquad Target: {round(n * 0.7)}+ MCQ "
               f"\\qquad Pace: {C.pace:g} min per MCQ}}\n\n")
    for s in u.qsections:
        out.append(f"\\section{{{s.title}}}\n\n" + (stim_tex(s) if (s.stim or s.fig) else "") + "".join(q_env(q) for q in s.qs) + "\n")
    out.append(f"\\section{{Free response}}\n\n\\begin{{frq}}{{{f.kind} \\textperiodcentered\\ "
               f"{f.pts} points \\textperiodcentered\\ about {f.mins} minutes}}\n{frq_stem_tex(f)}\n\n"
               "\\begin{itemize}[leftmargin=2.6em,itemsep=4pt]\n")
    for p in f.parts:
        out.append(f"\\item[{label(p)}] {p.prompt.strip()} \\pts{{{p.pts}}}\n")
    out.append("\\end{itemize}\n\\end{frq}\n\n\\makekey\n\n")
    out.append(f"\\subsection*{{Free-response scoring guide ({f.pts} points)}}\n\\small\n"
               "Award each point only when the answer does what the model does. Points are independent unless a part says otherwise; "
               "a correct method with an answer carried forward from an earlier error earns the later points.\n"
               "\\begin{scoring}\n")
    for p in f.parts:
        out.append(f"{label(p)} ({p.pts}) & {p.solution.strip()} & {p.miss.strip()} \\\\\n")
    out.append("\\end{scoring}\n\n")
    for p in f.parts:
        if p.fig:
            out.append(f"\\needspace{{14\\baselineskip}}\\subsection*{{Model graph for part {label(p)}}}\n{figs.tex(p.fig)}\n")
    out.append("\\end{document}\n")
    assert sum(p.pts for p in f.parts) == f.pts, (u.n, "FRQ part points do not add up")
    return "".join(out)


def compile_one(out, n):
    cmd = ["tectonic", "-X", "compile", "-Z", "deterministic-mode", "--keep-intermediates", "--keep-logs", n + ".tex"]
    r = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
    logf = os.path.join(out, n + ".log")
    log = open(logf, encoding="utf8", errors="replace").read() if os.path.exists(logf) else r.stdout + r.stderr
    if r.returncode:
        i = log.find("\n!")
        print(log[i:i + 2500] if i >= 0 else log[-3000:], r.stderr[-1500:])
        raise SystemExit(f"{n}: LaTeX failed")
    missing = sorted(set(re.findall(r"Missing character: There is no (\S+)", log)))
    if missing:
        raise SystemExit(f"{n}: missing glyphs {missing}")
    over = re.findall(r"Overfull \\hbox \((\d+\.\d+)pt", log)
    big = [float(x) for x in over if float(x) > 3]
    from pypdf import PdfReader
    npages = len(PdfReader(os.path.join(out, n + ".pdf")).pages)
    print(f"  {n:<52} {npages:>3} pp  {len(over)} overfull" + (f" (max {max(big):.0f}pt)" if big else ""))
    return len(big)


def main(C, here, args):
    out = os.path.join(here, "tex", "out")
    os.makedirs(out, exist_ok=True)
    shutil.copy(STY, out)
    nums = [int(a) for a in args if a.isdigit()]
    us = C.units(nums or None)
    bad = 0
    pj = os.path.join(here, "pages.json")
    pages = json.load(open(pj)) if os.path.exists(pj) else {}
    for u in us:
        for kind, tex in (("guide", guide_tex(C, u)), ("questions", questions_tex(C, u))):
            n = f"{u.stem}-{kind}"
            with open(os.path.join(out, n + ".tex"), "w", encoding="utf8") as fh:
                fh.write(tex)
            bad += compile_one(out, n)
        aux = open(os.path.join(out, f"{u.stem}-guide.aux"), encoding="utf8").read()
        pages[str(u.n)] = {k: int(p) for k, p in re.findall(r"\\newlabel\{sec:(\d+)\}\{\{[^}]*\}\{(\d+)\}", aux)}
    json.dump(pages, open(pj, "w"), indent=1, sort_keys=True)
    if bad:
        raise SystemExit(f"{bad} overfull boxes over 3pt")
    if not nums:
        publish(C, out)


def publish(C, out):
    from pypdf import PdfWriter
    pub = os.path.join(REPO, "public", "study", "ap", C.slug)
    os.makedirs(pub, exist_ok=True)
    w = PdfWriter()
    top = f"{C.prefix}study-series"
    stamp = (2026, 11, 1, 0, 0, 0)
    with zipfile.ZipFile(os.path.join(pub, C.prefix + "study-series.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        def add(src, arc):  # fixed timestamps, so an unchanged series zips to the same bytes
            z.writestr(zipfile.ZipInfo(arc, date_time=stamp), open(src, "rb").read(), zipfile.ZIP_DEFLATED)
        add(STY, f"{top}/latex/ap-sci.sty")
        z.writestr(zipfile.ZipInfo(f"{top}/latex/README.txt", date_time=stamp), README.format(course=C.name, family=C.family), zipfile.ZIP_DEFLATED)
        for u in C.units():
            for kind in ("guide", "questions"):
                n = f"{u.stem}-{kind}"
                pdf = os.path.join(out, n + ".pdf")
                shutil.copy(pdf, os.path.join(pub, n + ".pdf"))
                w.append(pdf, outline_item=f"Unit {u.n} {'Study Guide' if kind == 'guide' else 'Question Set'}: {u.title.replace('--', '–')}")
                add(pdf, f"{top}/pdf/{n}.pdf")
                add(os.path.join(out, n + ".tex"), f"{top}/latex/{n}.tex")
    w.add_metadata({"/Title": f"{C.name}: Complete Study Pack", "/Author": "Paul Wang"})
    with open(os.path.join(pub, C.prefix + "complete-pack.pdf"), "wb") as fh:
        w.write(fh)
    print(f"  published {len(os.listdir(pub))} files to public/study/ap/{C.slug}/")


README = """{course} study series: LaTeX sources
Build: tectonic <file>.tex   or   latexmk -xelatex <file>.tex
Fonts are loaded by file name from the TeX tree (TeX Gyre Pagella, Inter, DejaVu Sans Mono), so no system fonts
are needed. All files share ap-sci.sty; graphs are pgfplots.

Each unit has a Study Guide (notes, worked examples and section checks) and a Question Set (multiple choice and one
free-response question with a scoring guide). Question syntax:
  \\begin{{q}}{{<correct position 1-4>}}{{<topic tag>}}{{<why>}}
    Stem text.
    \\ch{{choice 1}}{{choice 2}}{{choice 3}}{{choice 4}}     % one per line
    \\chh{{...}}{{...}}{{...}}{{...}}                        % short choices, 2 columns
  \\end{{q}}
Letters, the answers-only strip, the #/Ans./Why/Rule table and \\qtotal are generated.
These .tex files are generated from the Python content model in the site repository (quizzes/{family}/),
which also drives the interactive quizzes on universitybikeshop.com/study.
"""
