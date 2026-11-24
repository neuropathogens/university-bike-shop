"""Shared data model for the AP Calculus BC practice sets and practice exam.

One source feeds both outputs: build_pdfs.py writes each set's LaTeX (practice-set format, key on the last
pages) and quiz.py turns the same items into the interactive quiz pages.

Text is plain Unicode with $..$ / $$..$$ for math. Outside math, to_tex() escapes % & #, and to_html()
escapes & < >; math is left alone for LaTeX and for the quiz builder's KaTeX pass.
"""
import re

LET = "ABCD"
BASE = "/study/ap/ap-calculus-bc/"
FIGS = {}  # name -> (tikz, alt, width)

_MATH = re.compile(r"(\$\$.+?\$\$|(?<!\\)\$.+?(?<!\\)\$)", re.S)


def _split(s):
    return _MATH.split(s)


def to_tex(s):
    out = []
    for i, part in enumerate(_split(s)):
        if i % 2:
            out.append(part)
        else:
            part = part.replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")
            part = part.replace("\n\n", "\\par ")
            out.append(part)
    return "".join(out)


def to_html(s):
    out = []
    for i, part in enumerate(_split(s)):
        if i % 2:
            out.append(part)
        else:
            part = part.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            part = part.replace("\n\n", "</p><p>")
            out.append(part)
    return "".join(out)


def fig(name, tikz, alt, width="0.45\\linewidth"):
    """Register a TikZ figure. build_pdfs.py compiles it to figs/<name>.pdf (PDF) and tests/fig/<name>.svg (web)."""
    FIGS[name] = (tikz, alt, width)
    return name


def fig_html(name):
    _, alt, _ = FIGS[name]
    return (f'<figure class="fig"><img src="{BASE}tests/fig/{name}.svg" alt="{to_html(alt)}" '
            f'loading="lazy" style="width:min(100%,480px);height:auto"></figure>')


def fig_tex(name):
    _, _, width = FIGS[name]
    return f"\\begin{{center}}\\includegraphics[width={width}]{{figs/{name}.pdf}}\\end{{center}}"


class Table:
    """A grid table given as rows of cells; the first cell of every row is a header."""

    def __init__(self, rows, caption=""):
        self.rows, self.caption = rows, caption

    def tex(self):
        n = len(self.rows[0])
        spec = "|c|" + "c|" * (n - 1)
        body = "\\hline\n" + "".join(" & ".join(to_tex(c) for c in r) + " \\\\ \\hline\n" for r in self.rows)
        cap = f"\\par{{\\small {to_tex(self.caption)}}}" if self.caption else ""
        return f"\\begin{{center}}\\small\\renewcommand{{\\arraystretch}}{{1.35}}\\begin{{tabular}}{{{spec}}}\n{body}\\end{{tabular}}{cap}\\end{{center}}"

    def html(self):
        trs = "".join("<tr>" + f'<th scope="row">{to_html(r[0])}</th>' + "".join(f"<td>{to_html(c)}</td>" for c in r[1:]) + "</tr>"
                      for r in self.rows)
        cap = f'<p class="figcap">{to_html(self.caption)}</p>' if self.caption else ""
        return f'{cap}<table class="bt"><tbody>{trs}</tbody></table>'


def Q(n, sec, rule, prompt, options, answer, why, idea, steps, others, calc=False, fig=None, table=None, layout=None):
    """A four-choice item. sec = guide section number (quiz topic), rule = rule tag (e.g. R6.4)."""
    assert len(options) == 4 and len(set(options)) == 4, (n, options)
    assert answer in LET and set(others) == set(LET) - {answer}, (n, answer, sorted(others))
    return dict(n=n, sec=str(sec), rule=rule, prompt=prompt, options=options, answer=answer, why=why, idea=idea,
                steps=steps, others=others, calc=calc, fig=fig, table=table, layout=layout)


def P(label, prompt, rubric, solution):
    """One part of a free-response question. rubric: list of point descriptions (one point each)."""
    return dict(label=label, prompt=prompt, rubric=rubric, solution=solution)


def FRQ(n, secs, title, stem, parts, calc=False, fig=None, table=None, space="1.6in"):
    return dict(n=n, secs=[str(s) for s in secs], title=title, stem=stem, parts=parts, calc=calc, fig=fig,
                table=table, space=space, pts=sum(len(p["rubric"]) for p in parts))


def check_letters(qs, name):
    """Answer letters: every letter used, none more than twice in a row, counts within 2 of each other... ish."""
    seq = "".join(q["answer"] for q in qs)
    counts = {c: seq.count(c) for c in LET}
    assert min(counts.values()) >= max(counts.values()) - 2 or len(seq) < 8, (name, counts)
    assert not re.search(r"(.)\1\1", seq), (name, seq)
    return counts
