"""Parse the ACT Reading LaTeX sources (source/*.tex) into passage units and questions.

A unit starts at \\passagehead{label}{type}{intro} and collects its passage environments, \\subpassage headings,
an optional table or figure (a center block before the first question), notes such as
{\\small\\itshape Questions 10--12 ...}, and its \\Q{cat}{answer}{skill}{why}{stem}{A}{B}{C}{D} items.
A \\section or \\subsection ends the current unit; in Volume 1, "Rule N --- title" subsections set the rule.
"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent / "source"
TOK = re.compile(r"\\section\*?\{|\\subsection\*?\{|\\passagehead\{|\\subpassage\{|\\begin\{passage\}(\[cont\])?|"
                 r"\\begin\{center\}|\{\\small\\itshape|\\Q\{|\\answerkey\{")


def group(s, i):
    """Read the {...} group starting at or after i (skipping whitespace); return (content, index after it)."""
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
    units, unit, rule, i = [], None, None, 0
    while True:
        m = TOK.search(body, i)
        if not m:
            break
        tok = m.group(0)
        if tok.startswith("\\answerkey"):
            break
        if tok.startswith(("\\section", "\\subsection")):
            title, i = group(body, m.end() - 1)
            unit = None
            r = re.match(r"Rule (\d+) --- (.+)", title)
            if r:
                rule = (r.group(1), r.group(2))
            continue
        if tok.startswith("\\passagehead"):
            label, j = group(body, m.end() - 1)
            kind, j = group(body, j)
            intro, i = group(body, j)
            unit = dict(label=label, kind=kind, intro=intro, parts=[], questions=[], rule=rule)
            units.append(unit)
            continue
        if unit is None:
            i = m.end()
            continue
        if tok.startswith("\\subpassage"):
            head, i = group(body, m.end() - 1)
            unit["parts"].append(("sub", head))
        elif tok.startswith("\\begin{passage}"):
            j = body.index("\\end{passage}", m.end())
            unit["parts"].append(("passage", body[m.end():j]))
            i = j + len("\\end{passage}")
        elif tok.startswith("\\begin{center}"):
            j = body.index("\\end{center}", m.end())
            if not unit["questions"]:
                unit["parts"].append(("center", body[m.end():j]))
            i = j + len("\\end{center}")
        elif tok.startswith("{\\small\\itshape"):
            note, i = group(body, m.start())
            unit["parts"].append(("note", note.replace("\\small\\itshape", "").strip()))
        else:  # \Q
            args, j = [], m.end() - 1
            for _ in range(9):
                a, j = group(body, j)
                args.append(a)
            i = j
            cat, ans, skill, why, stem, *choices = args
            unit["questions"].append(dict(cat=cat, ans=ans, skill=skill, why=why, stem=stem, choices=choices))
    return units
