"""Render one AP world language series (a family such as ap_spanish) to LaTeX and PDF.

Each family's build_tex.py calls main(L, DOCS, here). For every Doc it writes tex/out/<stem>-<kind>.tex, compiles
it with tectonic (or latexmk -xelatex when tectonic is missing), records the page of every guide section in
<family>/pages.json (used by the quizzes' topic links), and publishes to public/study/ap/<slug>/: one PDF per
document, the merged complete pack, and a .zip of all PDFs with the LaTeX source.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

from ap_wl.model import width

ENGINE = os.path.dirname(os.path.abspath(__file__))
STY = os.path.join(ENGINE, "tex", "ap-wl.sty")


def esc(s):
    """Plain text (the key's Why column) -> LaTeX."""
    for a, b in (("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("$", "\\$"), ("_", "\\_")):
        s = s.replace(a, b)
    return s


def choices_tex(cs):
    if max(width(c) for c in cs) <= 30:
        return "\\chh" + "".join("{" + c + "}" for c in cs)
    return "\\ch" + "".join("{" + c + "}" for c in cs)


def table_tex(table):
    head, rows = table
    cols = "@{}l" + "c" * (len(head) - 1) + "@{}"
    out = ["\\begin{center}\\small", f"\\begin{{tabular}}{{{cols}}}", "\\toprule",
           " & ".join(f"\\textbf{{{h}}}" for h in head) + " \\\\", "\\midrule"]
    out += [" & ".join(r) + " \\\\" for r in rows]
    out += ["\\bottomrule", "\\end{tabular}", "\\end{center}"]
    return "\n".join(out)


def frq_tex(f):
    o = [f"\\begin{{frq}}{{{f['head']}}}", "\\small"]
    o += [p + "\n" for p in f["directions"]]
    if f.get("panels"):
        o.append("\\textbf{The four pictures} (described in words for this practice set):")
        o.append("\\begin{enumerate}[label=\\arabic*.,leftmargin=2em,itemsep=2pt]")
        o += [f"\\item {p}" for p in f["panels"]]
        o.append("\\end{enumerate}")
    for s in f.get("sources", []):
        o.append(f"\\begin{{source}}{{{s['title']}}}")
        o.append("\n\n".join(s["paras"]))
        if s.get("table"):
            o.append(table_tex(s["table"]))
        o += ["\\end{source}", ""]
    o += [p + "\n" for p in f.get("prompt", [])]
    o.append(f"\\writelines{{{f.get('lines', 10)}}}")
    o.append("\\end{frq}")
    return "\n".join(o)


def guide_tex(f):
    total = sum(r[1] for r in f["rows"])
    o = [f"\\subsection*{{{esc(f['kind'])} scoring guide ({total} points)}}", "\\small",
         "\\begin{compare}{Row}{Full credit}{Common reasons for losing points}"]
    o += [f"{name} ({pts}) & {earns} & {miss} \\\\" for name, pts, earns, miss in f["rows"]]
    o.append("\\end{compare}")
    o.append("\\begin{keyidea}[Model response]")
    o += [p + "\\par" for p in f["model"]]
    o.append("\\end{keyidea}")
    if f.get("tips"):
        o.append("\\begin{trap}[Why it scores]")
        o.append(" ".join(f["tips"]))
        o.append("\\end{trap}")
    return "\n".join(o)


def doc_tex(L, d):
    pkg = "\\usepackage[japanese]{ap-wl}" if L.cjk else "\\usepackage{ap-wl}"
    o = ["\\documentclass[11pt]{article}", pkg, f"\\course{{{L.course}}}", f"\\vocabheads{L.vocabheads}",
         f"\\title{{{d.title}}}", "\\author{Paul Wang}", "\\date{November 2026}", f"\\docpart{{{d.docpart}}}", "",
         "\\begin{document}", "\\maketitle", "", "\\begin{abstract}", d.abstract, "\\end{abstract}", "",
         f"\\scoringline{{{d.scoring}}}", ""]
    for b in d.blocks:
        if b[0] == "sec":
            o += [f"\\section{{{b[2]}}}\\label{{sec:{b[1]}}}", ""]
        elif b[0] == "tex":
            o += [b[1].strip(), ""]
        elif b[0] == "src":
            s = b[1]
            o.append(f"\\begin{{source}}{{{s['title']}}}")
            o.append("\n\n".join(s["paras"]))
            if s.get("table"):
                o.append(table_tex(s["table"]))
            if s.get("note"):
                o.append(f"\n\\emph{{{s['note']}}}")
            o += ["\\end{source}", ""]
        elif b[0] == "q":
            q = b[1]
            o += [f"\\begin{{q}}{{{q['pos']}}}{{{esc(q['tag'])}}}{{{esc(q['why'])}}}", q["stem"], choices_tex(q["choices"]),
                  "\\end{q}", ""]
        elif b[0] == "frq":
            o += [frq_tex(b[1]), ""]
    o += ["\\makekey", ""]
    for f in d.fr:
        o += [guide_tex(f), ""]
    o += d.tail
    o.append("\\end{document}")
    out = "\n".join(o)
    if L.cjk:  # XeTeX treats CJK characters as letters: end a control word before them
        out = re.sub(r"(\\[A-Za-z]+)(?=[\u3000-\u9fff\uff00-\uffef])", r"\1{}", out)
    return out + "\n"


def name(d):
    return f"{d.stem}-{d.kind}"


def compile_one(out, n):
    if shutil.which("tectonic"):
        cmd = ["tectonic", "-X", "compile", "-Z", "deterministic-mode", "--keep-intermediates", "--keep-logs", n + ".tex"]
    else:
        cmd = ["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", n + ".tex"]
    r = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
    logf = os.path.join(out, n + ".log")
    log = open(logf, encoding="utf8", errors="replace").read() if os.path.exists(logf) else r.stdout + r.stderr
    if r.returncode:
        print(log[-3000:], r.stderr[-2000:])
        raise SystemExit(f"{n}: LaTeX failed")
    missing = sorted(set(re.findall(r"Missing character: There is no (\S+)", log)))
    if missing:
        raise SystemExit(f"{n}: missing glyphs {missing}")
    over = re.findall(r"Overfull \\hbox \((\d+\.\d+)pt", log)
    big = [float(x) for x in over if float(x) > 3]
    from pypdf import PdfReader
    npages = len(PdfReader(os.path.join(out, n + ".pdf")).pages)
    print(f"  {n:<44} {npages:>3} pp  {len(over)} overfull" + (f" (max {max(big):.0f}pt)" if big else ""))


def main(L, DOCS, here):
    out = os.path.join(here, "tex", "out")
    os.makedirs(out, exist_ok=True)
    shutil.copy(STY, out)
    for d in DOCS:
        d.place()
        with open(os.path.join(out, name(d) + ".tex"), "w", encoding="utf8") as fh:
            fh.write(doc_tex(L, d))
    only = sys.argv[1:]
    for d in DOCS:
        n = name(d)
        if not only or any(x in n for x in only):
            compile_one(out, n)
    pages = {}
    for d in DOCS:
        aux = os.path.join(out, name(d) + ".aux")
        if d.kind == "guide" and os.path.exists(aux):
            t = open(aux, encoding="utf8").read()
            pages[d.stem] = {k: int(p) for k, p in re.findall(r"\\newlabel\{sec:(\d+)\}\{\{[^}]*\}\{(\d+)\}", t)}
    pj = os.path.join(here, "pages.json")
    old = json.load(open(pj)) if os.path.exists(pj) else {}
    old.update(pages)
    json.dump(old, open(pj, "w"), indent=1, sort_keys=True)
    if not only:
        publish(L, DOCS, out)


def publish(L, DOCS, out):
    from pypdf import PdfWriter
    repo = os.path.dirname(os.path.dirname(ENGINE))
    pub = os.path.join(repo, "public", "study", "ap", L.slug)
    os.makedirs(pub, exist_ok=True)
    w = PdfWriter()
    top = f"{L.prefix}study-series"
    with zipfile.ZipFile(os.path.join(pub, L.prefix + "study-series.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        def add(src, arc):  # fixed timestamps, so an unchanged series zips to the same bytes
            z.writestr(zipfile.ZipInfo(arc, date_time=(2026, 11, 1, 0, 0, 0)), open(src, "rb").read(), zipfile.ZIP_DEFLATED)
        add(os.path.join(out, "ap-wl.sty"), f"{top}/latex/ap-wl.sty")
        z.writestr(zipfile.ZipInfo(f"{top}/latex/README.txt", date_time=(2026, 11, 1, 0, 0, 0)),
                   README.format(course=L.course, family=L.family), zipfile.ZIP_DEFLATED)
        for d in DOCS:
            n = name(d)
            pdf = os.path.join(out, n + ".pdf")
            shutil.copy(pdf, os.path.join(pub, L.prefix + n + ".pdf"))
            w.append(pdf, outline_item=f"{d.short} {'Study Guide' if d.kind == 'guide' else 'Question Set'}: {d.sub}")
            add(pdf, f"{top}/pdf/{n}.pdf")
            add(os.path.join(out, n + ".tex"), f"{top}/latex/{n}.tex")
    w.add_metadata({"/Title": f"{L.course}: Complete Study Pack", "/Author": "Paul Wang"})
    with open(os.path.join(pub, L.prefix + "complete-pack.pdf"), "wb") as fh:
        w.write(fh)


README = """{course} study series: LaTeX sources
Build: tectonic <file>.tex   or   latexmk -xelatex <file>.tex
Fonts are loaded by file name from the TeX tree (TeX Gyre Pagella, Inter, DejaVu Sans Mono; Harano Aji for Japanese),
so no system fonts are needed. All files share ap-wl.sty.

Question syntax:
  \\begin{{q}}{{<correct position 1-4>}}{{<rule tag>}}{{<why>}}
    Stem text.
    \\ch{{choice 1}}{{choice 2}}{{choice 3}}{{choice 4}}     % one per line
    \\chh{{...}}{{...}}{{...}}{{...}}                        % short choices, 2 columns
  \\end{{q}}
Letters, the answers-only strip, the #/Ans./Why/Rule table and \\qtotal are generated.
These .tex files are generated from the Python content model in the site repository
(quizzes/{family}/content/), which also drives the interactive quizzes.
"""
