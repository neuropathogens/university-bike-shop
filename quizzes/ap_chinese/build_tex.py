"""Render the AP Chinese series to LaTeX and PDF.

    python3 -I quizzes/ap_chinese/build_tex.py            # write tex/out/*.tex, compile, publish

Writes tex/out/<stem>-<kind>.tex, compiles each with latexmk -xelatex (needs ap-chinese.sty, Noto CJK and
TeX Gyre Pagella), records the physical page of every guide section in pages.json (used by quiz.py for
the topic links), and publishes to public/study/ap/ap-chinese/: one PDF per document, the merged
complete pack, and a .zip of all PDFs with the LaTeX source.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from content import DOCS  # noqa: E402
from model import width  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "tex", "out")
PUB = os.path.join(REPO, "public", "study", "ap", "ap-chinese")
PREFIX = "ap-chinese-"


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


def doc_tex(d):
    o = ["\\documentclass[11pt]{article}", "\\usepackage{ap-chinese}", f"\\title{{{d.title}}}",
         "\\author{Paul Wang}", "\\date{November 2026}", f"\\docpart{{{d.docpart}}}", "", "\\begin{document}",
         "\\maketitle", "", "\\begin{abstract}", d.abstract, "\\end{abstract}", "", f"\\scoringline{{{d.scoring}}}", ""]
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
    # XeTeX treats Chinese characters as letters: end a control word before them (\\blank一件 -> \\blank{}一件).
    return re.sub(r"(\\[A-Za-z]+)(?=[\u3000-\u9fff\uff00-\uffef])", r"\1{}", "\n".join(o)) + "\n"


def name(d):
    return f"{d.stem}-{d.kind}"


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copy(os.path.join(HERE, "tex", "ap-chinese.sty"), OUT)
    pages = {}
    for d in DOCS:
        d.place()
        with open(os.path.join(OUT, name(d) + ".tex"), "w", encoding="utf8") as fh:
            fh.write(doc_tex(d))
    only = sys.argv[1:]
    for d in DOCS:
        n = name(d)
        if only and not any(x in n for x in only):
            continue
        r = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", n + ".tex"],
                           cwd=OUT, capture_output=True, text=True)
        log = open(os.path.join(OUT, n + ".log"), encoding="utf8", errors="replace").read()
        if r.returncode:
            print(log[-3000:])
            raise SystemExit(f"{n}: LaTeX failed")
        missing = sorted(set(re.findall(r"Missing character: There is no (\S+)", log)))
        if missing:
            raise SystemExit(f"{n}: missing glyphs {missing}")
        over = len(re.findall(r"Overfull \\hbox \((\d+\.\d+)pt", log))
        npages = int(re.search(r"Output written on .*?\((\d+) page", log).group(1))
        print(f"  {n:<44} {npages:>3} pp  {over} overfull")
    for d in DOCS:
        n = name(d)
        aux = os.path.join(OUT, n + ".aux")
        if d.kind == "guide" and os.path.exists(aux):
            t = open(aux, encoding="utf8").read()
            pages[d.stem] = {k: int(p) for k, p in re.findall(r"\\newlabel\{sec:(\d+)\}\{\{[^}]*\}\{(\d+)\}", t)}
    pj = os.path.join(HERE, "pages.json")
    old = json.load(open(pj)) if os.path.exists(pj) else {}
    old.update(pages)
    json.dump(old, open(pj, "w"), indent=1, sort_keys=True)
    publish()


def publish():
    from pypdf import PdfWriter
    os.makedirs(PUB, exist_ok=True)
    w = PdfWriter()
    zpath = os.path.join(PUB, PREFIX + "study-series.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(OUT, "ap-chinese.sty"), "ap-chinese-study-series/latex/ap-chinese.sty")
        z.writestr("ap-chinese-study-series/latex/README.txt", README)
        for d in DOCS:
            n = name(d)
            pdf = os.path.join(OUT, n + ".pdf")
            dst = os.path.join(PUB, PREFIX + n + ".pdf")
            shutil.copy(pdf, dst)
            w.append(pdf, outline_item=f"{d.short} {'Study Guide' if d.kind == 'guide' else 'Question Set'}: {d.sub}")
            z.write(pdf, f"ap-chinese-study-series/pdf/{n}.pdf")
            z.write(os.path.join(OUT, n + ".tex"), f"ap-chinese-study-series/latex/{n}.tex")
    w.add_metadata({"/Title": "AP Chinese Language and Culture: Complete Study Pack", "/Author": "Paul Wang"})
    with open(os.path.join(PUB, PREFIX + "complete-pack.pdf"), "wb") as fh:
        w.write(fh)


README = """AP Chinese Language and Culture study series: LaTeX sources
Build: latexmk -xelatex <file>.tex   (XeLaTeX; fonts: TeX Gyre Pagella, Inter, Noto Serif/Sans CJK SC)
All files share ap-chinese.sty, the AP Psychology series style plus automatic switching to Noto CJK
for Chinese text (one XeTeX inter-character class; xeCJK is not needed).

Question syntax (same as the AP Psychology series):
  \\begin{q}{<correct position 1-4>}{<rule tag>}{<why>}
    Stem text.
    \\ch{choice 1}{choice 2}{choice 3}{choice 4}     % one per line
    \\chh{...}{...}{...}{...}                        % short choices, 2 columns
  \\end{q}
Letters, the answers-only strip, the #/Ans./Why/Rule table and \\qtotal are generated.
These .tex files are generated from the Python content model in the site repository
(quizzes/ap_chinese/content/), which also drives the interactive quizzes.
"""

if __name__ == "__main__":
    main()
