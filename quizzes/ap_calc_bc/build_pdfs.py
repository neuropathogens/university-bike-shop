"""Build the AP Calculus BC PDFs (study guides, practice sets, practice exam, complete pack, source zip).

    python3 -I quizzes/ap_calc_bc/build_pdfs.py            # everything
    python3 -I quizzes/ap_calc_bc/build_pdfs.py u06 g06    # just these (uNN = practice set, gNN = guide, exam)

Practice sets and the exam are generated from sets/*.py (the same data the quizzes use), so the PDF key and
the quiz can never disagree. Guides are hand-written LaTeX in source/guides/. Figures registered with
model.fig() are compiled once to source/figs/<name>.pdf (for LaTeX) and public/.../tests/fig/<name>.svg (web).
Writes pages.json (guide section -> page) for the quiz topic links. Needs pdflatex/latexmk, pdftocairo, pypdf.
"""
import hashlib
import importlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from ap_calc_bc.model import FIGS, LET, Table, fig_tex, to_tex  # noqa: E402

REPO = HERE.parent.parent
SRC = HERE / "source"
BUILD = SRC / "build"
FIGDIR = SRC / "figs"
PUB = REPO / "public/study/ap/ap-calculus-bc"
WEBFIG = PUB / "tests/fig"
UNITS = [f"u{i:02d}" for i in range(1, 11)]
GUIDES = sorted(p.stem for p in (SRC / "guides").glob("*.tex"))

FIG_DOC = r"""\documentclass[border=2pt]{standalone}
\usepackage[T1]{fontenc}\usepackage{lmodern}\usepackage{amsmath,amssymb}
\usepackage{tikz}\usepackage{pgfplots}\pgfplotsset{compat=1.18}\usepgfplotslibrary{fillbetween}
\usetikzlibrary{arrows.meta,calc,patterns,decorations.markings}
\begin{document}
%s
\end{document}
"""


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode:
        log = r.stdout[-4000:] + r.stderr[-2000:]
        raise SystemExit(f"FAILED: {' '.join(map(str, cmd))}\n{log}")
    return r


def build_figs():
    FIGDIR.mkdir(exist_ok=True)
    WEBFIG.mkdir(parents=True, exist_ok=True)
    tmp = BUILD / "figs"
    tmp.mkdir(parents=True, exist_ok=True)
    for name, (tikz, _, _) in FIGS.items():
        doc = FIG_DOC % tikz
        h = hashlib.sha1(doc.encode()).hexdigest()[:12]
        stamp = tmp / f"{name}.hash"
        pdf, svg = FIGDIR / f"{name}.pdf", WEBFIG / f"{name}.svg"
        if stamp.exists() and stamp.read_text() == h and pdf.exists() and svg.exists():
            continue
        (tmp / f"{name}.tex").write_text(doc)
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"], tmp)
        shutil.copy(tmp / f"{name}.pdf", pdf)
        run(["pdftocairo", "-svg", str(pdf), str(svg)], tmp)
        stamp.write_text(h)
        print("  fig", name)


def choices(q):
    o = [to_tex(x) for x in q["options"]]

    def vis(s):
        s = re.sub(r"\\[a-zA-Z]+", "", s)
        return len(re.sub(r"[${}^_\\ ]", "", s))
    lay = q.get("layout") or ("four" if max(map(vis, o)) <= 13 else "two" if max(map(vis, o)) <= 30 else "one")
    return {"four": r"\chfour", "two": r"\chtwo", "one": r"\chone"}[lay] + "".join("{" + x + "}" for x in o)


def q_tex(q):
    s = [f"\\begin{{q}}{{{q['n']}}}", to_tex(q["prompt"]) + (r"\calcmark" if q["calc"] else "")]
    if q.get("fig"):
        s.append(fig_tex(q["fig"]))
    if isinstance(q.get("table"), Table):
        s.append(q["table"].tex())
    s.append(choices(q))
    s.append(r"\end{q}")
    return "\n".join(s)


def frq_tex(f, label="Question"):
    calc = "calculator required" if f["calc"] else "no calculator"
    s = [f"\\begin{{frq}}{{{label} {f['n']} --- {to_tex(f['title'])} ({f['pts']} points, {calc})}}", to_tex(f["stem"])]
    if f.get("fig"):
        s.append(fig_tex(f["fig"]))
    if f.get("table"):
        s.append(f["table"].tex())
    for p in f["parts"]:
        s.append(f"\\partlabel{{{p['label']}}}{to_tex(p['prompt'])}\\workspace{{{f['space']}}}")
    s.append(r"\end{frq}")
    return "\n".join(s)


def frq_key(f, label="Question"):
    s = [f"\\subsection*{{{label} {f['n']}: {to_tex(f['title'])} ({f['pts']} points)}}"]
    for p in f["parts"]:
        sol = " ".join(to_tex(x) for x in p["solution"])
        pts = "".join(f"\\item 1 point: {to_tex(r)}\n" for r in p["rubric"])
        s.append(f"\\textbf{{({p['label']})}} {sol}\n\\begin{{itemize}}[leftmargin=1.6em,itemsep=0pt]\n{pts}\\end{{itemize}}")
    return "\n".join(s)


def key_tex(qs, groups):
    strip = "".join(f"\\keyitem{{{q['n']}}}{{{q['answer']}}}" for q in qs)
    rows = []
    for title, members in groups:
        rows.append(f"\\keysection{{{to_tex(title)}}}")
        for q in members:
            rule = q["rule"] + (r", \emph{calc}" if q["calc"] else "")
            rows.append(f"{q['n']} & {q['answer']} & {to_tex(q['why'])} & {rule}\\\\")
    return f"\\keystrip{{{strip}}}\n\\vspace{{4pt}}\n\\begin{{keytable}}\n" + "\n".join(rows) + "\n\\end{keytable}"


def head(title, volume, short, abstract, total, pace):
    return "\n".join([
        r"\documentclass{apcalc}", f"\\title{{{title}}}", r"\author{Paul Wang}", r"\date{November 2026}",
        f"\\volume{{{volume}}}", f"\\shorttitle{{{short}}}", r"\begin{document}", r"\maketitle",
        r"\begin{abstract}", to_tex(abstract), r"\end{abstract}", f"\\scoringline{{{total}}}{{{to_tex(pace)}}}"])


def set_tex(mod):
    m = importlib.import_module(f"ap_calc_bc.sets.{mod}")
    D, qs, frs = m.DOC, m.QS, m.FRS
    u = D["unit"]
    pts = sum(f["pts"] for f in frs)
    out = [head(f"Unit {u} Practice Set: {to_tex(D['title'])}", f"Practice Set {u} of 10 (topics {D['topics']})",
                f"Unit {u} --- Practice Set", D["abstract"], f"{len(qs)} MC \\quad\\blank\\ / {pts} FR",
                D["pace"])]
    groups = []
    for sec, title in D["sections"].items():
        members = [q for q in qs if q["sec"] == sec]
        if not members:
            continue
        groups.append((f"{sec}. {title}", members))
        out.append(f"\\section*{{{sec}\\quad {to_tex(title)}}}")
        if D["rules"].get(sec):
            out.append(f"\\begin{{setrule}}{to_tex(D['rules'][sec])}\\end{{setrule}}")
        out += [q_tex(q) for q in members]
    assert sum(len(g[1]) for g in groups) == len(qs), mod
    out.append(r"\clearpage\section*{Free response}")
    out.append(to_tex(D.get("frnote", "Show all work. Justify every conclusion with calculus, and give decimal answers correct to three places.")))
    out += [frq_tex(f) for f in frs]
    out.append(r"\clearpage\section*{Answer key}")
    out.append(key_tex(qs, groups))
    out.append(r"\section*{Free-response scoring guide}")
    out += [frq_key(f) for f in frs]
    out.append(r"\end{document}")
    return D["pdf"], "\n".join(out)


def exam_tex():
    m = importlib.import_module("ap_calc_bc.sets.exam")
    D, qs, frs = m.DOC, m.QS, m.FRS
    out = [head("AP Calculus BC: Full Practice Exam", "May 2027 format", "Full Practice Exam", D["abstract"],
                "42 MC \\quad\\blank\\ / 54 FR", D["pace"])]
    out.append(to_tex(D["front"]))
    A = [q for q in qs if not q["calc"]]
    B = [q for q in qs if q["calc"]]
    assert len(A) == 29 and len(B) == 13 and qs == A + B
    out.append(r"\clearpage\section*{Section I, Part A: 29 questions, 62 minutes. No calculator.}")
    out += [q_tex(q).replace(r"\calcmark", "") for q in A]
    out.append(r"\clearpage\section*{Section I, Part B: 13 questions, 38 minutes. Graphing calculator required.}")
    out += [q_tex(q).replace(r"\calcmark", "") for q in B]
    FA = [f for f in frs if f["calc"]]
    FB = [f for f in frs if not f["calc"]]
    out.append(r"\clearpage\section*{Section II, Part A: 2 questions, 30 minutes. Graphing calculator required.}")
    out.append(to_tex(D["frnote"]))
    out += [frq_tex(f) for f in FA]
    out.append(r"\clearpage\section*{Section II, Part B: 4 questions, 60 minutes. No calculator.}")
    out += [frq_tex(f) for f in FB]
    out.append(r"\clearpage\section*{Answer key}")
    groups = [("Part A (no calculator)", A), ("Part B (calculator)", B)]
    out.append(key_tex(qs, groups).replace(r", \emph{calc}", ""))
    out.append(to_tex(D["scoring"]))
    out.append(r"\section*{Free-response scoring guide}")
    out += [frq_key(f) for f in frs]
    out.append(r"\end{document}")
    return D["pdf"], "\n".join(out)


def compile_tex(name, tex_path):
    run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", f"-outdir={BUILD}", f"-jobname={name}", str(tex_path)], SRC)
    pdf = BUILD / f"{name}.pdf"
    shutil.copy(pdf, PUB / f"{name}.pdf")
    pages = int(re.search(r"Pages:\s+(\d+)", run(["pdfinfo", str(pdf)], SRC).stdout).group(1))
    print(f"  {name}.pdf  {pages} pp  {pdf.stat().st_size // 1024} KB")
    return BUILD / f"{name}.pages"


def main(args):
    for mod in UNITS + ["exam"]:
        if importlib.util.find_spec(f"ap_calc_bc.sets.{mod}"):
            importlib.import_module(f"ap_calc_bc.sets.{mod}")
    PUB.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    (SRC / "sets").mkdir(exist_ok=True)
    build_figs()
    pj = HERE / "pages.json"
    pages = json.loads(pj.read_text()) if pj.exists() else {}
    want = set(args) if args else None
    for g in GUIDES:
        if want and "g" + g[:2] not in want:
            continue
        name = f"ap-calc-bc-{g}"
        pf = compile_tex(name, SRC / "guides" / f"{g}.tex")
        if pf.exists():
            pages[f"{name}.pdf"] = {a: int(b) for a, b in (l.split() for l in pf.read_text().split("\n") if l.strip())}
    for mod in UNITS + ["exam"]:
        if (want and mod not in want) or not importlib.util.find_spec(f"ap_calc_bc.sets.{mod}"):
            continue
        pdf, tex = set_tex(mod) if mod != "exam" else exam_tex()
        name = pdf[:-4]
        path = SRC / "sets" / f"{name}.tex"
        path.write_text(tex)
        compile_tex(name, path)
    pj.write_text(json.dumps(pages, indent=1, sort_keys=True) + "\n")
    if not args or "pack" in want:
        pack()


def pack():
    from pypdf import PdfReader, PdfWriter
    order = sorted(p.name for p in PUB.glob("ap-calc-bc-[0-9]*.pdf"))
    w = PdfWriter()
    for name in order:
        r = PdfReader(PUB / name)
        start = len(w.pages)
        for pg in r.pages:
            w.add_page(pg)
        title = r.metadata.title if r.metadata and r.metadata.title else name
        w.add_outline_item(re.sub(r"^ap-calc-bc-\d+-|\.pdf$", "", name).replace("-", " ").title() if not title or title == name else title, start)
    w.add_metadata({"/Title": "AP Calculus BC: Complete Study Pack", "/Author": "Paul Wang"})
    w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    out = PUB / "ap-calc-bc-complete-pack.pdf"
    with open(out, "wb") as f:
        w.write(f)
    print(f"  complete pack: {len(w.pages)} pp, {out.stat().st_size // 1024} KB")
    z = PUB / "ap-calc-bc-latex-source.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(SRC.rglob("*")):
            if p.is_file() and "build" not in p.relative_to(SRC).parts:
                zf.write(p, "ap-calc-bc-source/" + str(p.relative_to(SRC)))
        for p in sorted([HERE / "model.py", HERE / "build_pdfs.py", HERE / "quiz.py"] + list((HERE / "sets").glob("*.py"))):
            zf.write(p, "ap-calc-bc-source/python/" + str(p.relative_to(HERE)))
    print(f"  source zip: {z.stat().st_size // 1024} KB")


if __name__ == "__main__":
    import importlib.util
    main(sys.argv[1:])
