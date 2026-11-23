"""Parse the ACT Science LaTeX sources (source/0N-*.tex) into passages and questions.

Walks the document body in order: \\section{Rule XX-N: title} (or any other section title) starts a new group and
ends the current passage; \\passage{title} ... \\passageend is a passage (text, \\figlabel + \\datatable tables,
figbox figures); \\begin{q}{pos}{rule}{why} ... \\end{q} is a question, attached to the passage it follows (if no
\\section came between). Every tikzpicture is numbered in document order so it can be matched to its image.
"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent / "source"
TOK = re.compile(r"\\section\*?\{|\\passage\{|\\passageend|\\begin\{q\}|\\makekey")


def group(s, i):
    """Read the {...} group at or after i (skipping whitespace); return (content, index after it)."""
    while s[i] in " \t\n":
        i += 1
    if s[i] != "{":
        raise ValueError(f"expected {{ at {s[i:i + 40]!r}")
    depth, start = 0, i
    while True:
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1:i], i + 1
        i += 1


def parse(name):
    t = (SRC / name).read_text()
    t = re.sub(r"(?<!\\)%.*", "", t)
    body = t[t.index("\\begin{document}"):]
    meta = {k: re.search(r"\\" + k + r"\{(.*)\}", t).group(1) for k in ("settitle", "setsubtitle", "settarget", "settime")}
    groups, passages, cur_sec, cur_pas, i, tikz = [], [], None, None, 0, 0
    questions = []
    while True:
        m = TOK.search(body, i)
        if not m:
            break
        tok = m.group(0)
        if tok == "\\makekey":
            break
        if tok.startswith("\\section"):
            title, i = group(body, m.end() - 1)
            cur_sec, cur_pas = title, None
            groups.append(title)
            continue
        if tok == "\\passage{":
            title, j = group(body, m.end() - 1)
            end = body.index("\\passageend", j)
            content = body[j:end]
            figs = []
            for _ in re.finditer(r"\\begin\{tikzpicture\}", content):
                tikz += 1
                figs.append(tikz)
            cur_pas = dict(n=len(passages) + 1, title=title, content=content, figs=figs, section=cur_sec)
            passages.append(cur_pas)
            i = end + len("\\passageend")
            continue
        if tok == "\\passageend":
            i = m.end()
            continue
        # \begin{q}{pos}{rule}{why} ... \end{q}
        pos, j = group(body, m.end())
        rule, j = group(body, j)
        why, j = group(body, j)
        end = body.index("\\end{q}", j)
        content = body[j:end]
        figs = []
        for _ in re.finditer(r"\\begin\{tikzpicture\}", content):
            tikz += 1
            figs.append(tikz)
        questions.append(dict(pos=int(pos), rule=rule, why=why, body=content, figs=figs,
                              passage=cur_pas["n"] if cur_pas else None, section=cur_sec))
        i = end + len("\\end{q}")
    # every tikzpicture must sit in a passage or a question, or the numbering would not match the images
    assert tikz == body[:body.index("\\makekey")].count("\\begin{tikzpicture}"), name
    return dict(meta=meta, sections=groups, passages=passages, questions=questions)
