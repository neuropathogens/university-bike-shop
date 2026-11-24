"""Shared source format for the AP Chemistry unit practice sets (every unit except Unit 5).

One unit module (u1.py, u2.py, ...) holds each set's questions once. From that one source this module writes
  * the practice-set LaTeX (tex/build/ap-chem-unit-N-{2,3}-practice-set-{a,b}.tex), in the Unit 5 layout, and
  * the quiz dicts for quizzes/build.py (tests/Na/, tests/Nb/).

Text is a small HTML subset (<i>, <b>, <br>, <sup>, <sub>) with Unicode punctuation; $..$ / $$..$$ is TeX with
mhchem (\\ce{}) and must work in both pdfLaTeX and KaTeX. Blocks (prompts, stems, stimuli) are lists of
  str  -> a paragraph,   L([...]) -> centred lines (cells split on "|"),   T(head, rows) -> a booktabs table.

  M(topic, prompt, correct, [(wrong, note)] * 3, why, idea, steps)   correct choice placed by the letter balancer
  F(topic, prompt, [4 choices], "C", {letter: note}, why, idea, steps)  fixed order (e.g. numbers ascending)
  S(title)   starts a numbered section;   Stim(blocks)   shared lead-in for the questions that pass it as stim=
  FR(points, topics, stem_blocks, [P(label, prompt, points, solution, lead=None)])
`why` is the one-line reason printed in the PDF key; `idea` + `steps` + the wrong-choice notes are the quiz
explanation.
"""
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEX = HERE / "tex"
BUILD = TEX / "build"
BASE = "/study/ap/ap-chemistry/"
LET = "ABCD"


# ======================================================================== source objects
class T:
    def __init__(self, head, rows, align=None):
        self.head, self.rows, self.align = head, rows, align


class L:
    def __init__(self, lines):
        self.lines = lines


class Stim:
    def __init__(self, blocks):
        self.blocks = blocks if isinstance(blocks, list) else [blocks]
        self.id = None


class S:
    def __init__(self, title):
        self.title = title


class MC:
    def __init__(self, topic, prompt, options, ans, notes, why, idea, steps, stim=None, tbl=None):
        self.topic, self.prompt, self.options, self.ans, self.notes = topic, prompt, options, ans, notes
        self.why, self.idea, self.steps, self.stim, self.tbl = why, idea, list(steps), stim, tbl
        self.n = None
        self.sec = None


def M(topic, prompt, correct, wrongs, why, idea, steps=(), stim=None, tbl=None):
    assert len(wrongs) == 3, prompt
    return MC(topic, prompt, [correct] + [w[0] for w in wrongs], None, [None] + [w[1] for w in wrongs],
              why, idea, steps, stim, tbl)


def F(topic, prompt, options, ans, notes, why, idea, steps=(), stim=None, tbl=None):
    i = LET.index(ans)
    assert len(options) == 4 and set(notes) == set(LET) - {ans}, prompt
    return MC(topic, prompt, list(options), i, [notes.get(c) for c in LET], why, idea, steps, stim, tbl)


class P:
    def __init__(self, label, prompt, pts, sol, lead=None):
        self.label, self.prompt, self.pts, self.sol, self.lead = label, prompt, pts, sol, lead


class FR:
    def __init__(self, pts, topics, stem, parts):
        self.pts, self.topics, self.stem, self.parts = pts, topics, stem if isinstance(stem, list) else [stem], parts
        assert sum(p.pts for p in parts) == pts, (pts, [p.label for p in parts])


# ======================================================================== text conversion
DISPLAY_MIN = 24
_CE = re.compile(r"(?<!\$)\$\\ce\{((?:[^{}]|\{[^{}]*\})*)\}\$(?!\$)([.,;:?](?=\s|$))?")


def displayify(s):
    """A long inline reaction becomes display math, so it never overflows a line or a phone."""
    def rep(m):
        b, punct = m.group(1), m.group(2) or ""
        if ("->" in b or "<=>" in b) and len(b) >= DISPLAY_MIN:
            return "$$\\ce{" + b + "}" + (r"\text{" + punct + "}" if punct else "") + "$$"
        return m.group(0)
    return _CE.sub(rep, s)


_SEG = re.compile(r"(\$\$.+?\$\$|\$.+?\$)", re.S)
UNI = {"–": "--", "—": "---", "’": "'", "‘": "`", "“": "``", "”": "''", "−": "\\textminus{}", "°": "\\textdegree{}",
       "×": "$\\times$", "→": "$\\rightarrow$", "⇒": "$\\Rightarrow$", "≥": "$\\geq$", "≤": "$\\leq$", "≈": "$\\approx$",
       "Δ": "$\\Delta$", "·": "$\\cdot$", "μ": "$\\mu$", "\u00a0": "~", "\u2009": "\\,", "λ": "$\\lambda$",
       "ν": "$\\nu$", "…": "\\ldots{}", "é": "\\'e", "â": "\\^a", "Å": "\\AA{}", "±": "$\\pm$", "≠": "$\\neq$",
       "½": "$\\tfrac12$", "ü": '\\"u', "ö": '\\"o', "→": "$\\rightarrow$", "↔": "$\\leftrightarrow$", "σ": "$\\sigma$",
       "π": "$\\pi$", "∝": "$\\propto$", "ℓ": "$\\ell$", "≫": "$\\gg$", "≪": "$\\ll$", "Ω": "$\\Omega$", "θ": "$\\theta$", "≡": "$\\equiv$", "ø": "{\\o}", "÷": "$\\div$", "≥": "$\\geq$", "⟶": "$\\longrightarrow$", "✓": "$\\checkmark$", "→": "$\\rightarrow$", "Ø": "{\\O}", "⁻": "\\textsuperscript{\\textminus}", "⁺": "\\textsuperscript{+}", "²": "\\textsuperscript{2}", "³": "\\textsuperscript{3}"}
UNI.update({'δ': '$\\delta$', 'α': '$\\alpha$', 'β': '$\\beta$', 'γ': '$\\gamma$', 'ε': '$\\varepsilon$', '∞': '$\\infty$', '⇌': '$\\rightleftharpoons$', '↑': '$\\uparrow$', '↓': '$\\downarrow$', '√': '$\\surd$', '°': '\\textdegree{}', '′': "$'$", 'ΔG': '$\\Delta G$', '∘': '$^\\circ$', 'ō': '\\=o', 'Θ': '$\\Theta$', 'κ': '$\\kappa$', 'χ': '$\\chi$', 'ρ': '$\\rho$', 'τ': '$\\tau$', '⋅': '$\\cdot$', '−': '\\textminus{}'})
TAGS = {"<i>": "\\emph{", "</i>": "}", "<b>": "\\textbf{", "</b>": "}", "<br>": "\\newline{}",
        "<sup>": "\\textsuperscript{", "</sup>": "}", "<sub>": "\\textsubscript{", "</sub>": "}"}


def tex(s, disp=False):
    if disp:
        s = displayify(s)
    out = []
    for seg in _SEG.split(s):
        if not seg:
            continue
        if seg.startswith("$$"):
            out.append("\\[" + seg[2:-2] + "\\]")
        elif seg.startswith("$"):
            out.append(seg)
        else:
            for k, v in TAGS.items():
                seg = seg.replace(k, "\x01" + v + "\x02")
            parts = re.split(r"\x01(.*?)\x02", seg)
            res = []
            for j, p in enumerate(parts):
                if j % 2:
                    res.append(p)
                    continue
                p = p.replace("\\", "\\textbackslash{}").replace("&", "\\&").replace("%", "\\%").replace("#", "\\#")
                p = p.replace("_", "\\_").replace("<", "$<$").replace(">", "$>$")
                q = []
                for ch in p:
                    if ord(ch) < 128:
                        q.append(ch)
                    elif ch in UNI:
                        q.append(UNI[ch])
                    else:
                        raise SystemExit(f"no TeX for {ch!r} in {s[:80]!r}")
                res.append("".join(q))
            out.append("".join(res))
    return "".join(out)


_CE_ANY = re.compile(r"(?<!\$)\$\\ce\{((?:[^{}]|\{[^{}]*\})*)\}\$(?!\$)")


def breakable(s):
    """Split a long inline reaction into pieces at its + and arrow signs, so it can wrap on a phone."""
    def rep(m):
        b = m.group(1)
        if len(b) >= 22 and "||" in b and " " not in b:  # cell notation: let it wrap at the salt bridge
            left, right = b.split("||", 1)
            return "$\\ce{" + left + "}$ $\\ce{||}$ $\\ce{" + right + "}$"
        if len(b) < 22 or not re.search(r" (->|<=>|\+) ", b):
            return m.group(0)
        parts = re.split(r" (->|<=>|\+) ", b)
        out = []
        for k, part in enumerate(parts):
            out.append("$\\ce{" + part + "}$" if k % 2 == 0 else "$\\ce{" + part + "}$")
        return " ".join(out)
    return _CE_ANY.sub(rep, s)


def html(s, disp=False):
    if disp:
        s = displayify(s)
    s = breakable(s)
    out = []
    for seg in _SEG.split(s):
        if seg.startswith("$"):
            out.append(seg)
        else:
            out.append(re.sub(r"&(?![a-z]+;|#\d+;)", "&amp;", seg))
    return "".join(out)


# ---- blocks
def _cells(line):
    return line.split("|")


def table_html(t):
    h = "".join(f'<th scope="col">{html(c)}</th>' for c in t.head)
    b = "".join("<tr>" + f'<th scope="row">{html(r[0])}</th>' + "".join(f"<td>{html(c)}</td>" for c in r[1:]) + "</tr>"
                for r in t.rows)
    return f'<div class="bt-wrap"><table class="bt"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def table_tex(t):
    al = t.align or ("l" + "c" * (len(t.head) - 1))
    rows = [" & ".join(tex(c) for c in t.head) + " \\\\ \\midrule"]
    rows += [" & ".join(tex(c) for c in r) + " \\\\" for r in t.rows]
    return "\\ctab{\\begin{tabular}{" + al + "}\\toprule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}}"


def lines_tex(l):
    ncol = max(len(_cells(x)) for x in l.lines)
    body = " \\\\\n".join(" & ".join(tex(c) for c in _cells(x)) for x in l.lines)
    return "\\ctab{\\begin{tabular}{@{}" + "l" * ncol + "@{}}\n" + body + "\n\\end{tabular}}"


def lines_html(l):
    return "<br>".join("&ensp;".join(html(c) for c in _cells(x)) for x in l.lines)


def blocks(b):
    return b if isinstance(b, list) else [b]


def blocks_tex(b):
    out = []
    for x in blocks(b):
        if isinstance(x, str):
            out.append(tex(x, disp=True))
        elif isinstance(x, T):
            out.append(table_tex(x))
        elif isinstance(x, L):
            out.append(lines_tex(x))
        else:
            raise TypeError(x)
    return "\n\n".join(out)


def inline_html(b):
    """Blocks inside one <p> (a prompt): paragraphs and lines joined with <br>; no tables."""
    out = []
    for x in blocks(b):
        if isinstance(x, str):
            out.append(html(x, disp=True))
        elif isinstance(x, L):
            out.append(lines_html(x))
        else:
            raise TypeError(f"table inside an inline prompt: {x}")
    return "<br>".join(out)


def block_html(b):
    out = []
    for x in blocks(b):
        if isinstance(x, str):
            out.append(f"<p>{html(x, disp=True)}</p>")
        elif isinstance(x, L):
            out.append(f"<p>{lines_html(x)}</p>")
        elif isinstance(x, T):
            out.append(table_html(x))
    return "".join(out)


def plain_len(s):
    s = re.sub(r"\\ce\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\(mathrm|text|unit)\{([^}]*)\}", r"\2", s)
    s = re.sub(r"\\[a-zA-Z]+|[{}$^_\\]", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    return len(s)


# ======================================================================== set assembly
def assemble(items, seed):
    """Number the questions, attach sections and stimuli, and place the correct choices (A-D balanced)."""
    secs, mcs, cur = {}, [], 0
    for it in items:
        if isinstance(it, S):
            cur += 1
            secs[cur] = it.title
        else:
            it.sec = cur
            mcs.append(it)
    for i, q in enumerate(mcs, 1):
        q.n = i
    n = len(mcs)
    quota = {c: n // 4 + (1 if k < n % 4 else 0) for k, c in enumerate("BDAC")}
    fixed = [q for q in mcs if q.ans is not None]
    # Fixed-order items (numbers ascending) may be listed in reverse when one letter would be over-used.
    for q in fixed:
        quota[LET[q.ans]] -= 1
    for q in fixed:
        here, mirror = LET[q.ans], LET[3 - q.ans]
        if quota[here] < 0 and quota[mirror] > 0:
            quota[here] += 1
            quota[mirror] -= 1
            q.options, q.notes, q.ans = q.options[::-1], q.notes[::-1], 3 - q.ans
    assert all(v >= 0 for v in quota.values()), quota
    rng = random.Random(seed)
    letters = []
    for q in mcs:
        if q.ans is None:
            ok = [c for c in LET if quota[c] > 0 and not (len(letters) >= 2 and letters[-1] == letters[-2] == c)]
            ok = ok or [c for c in LET if quota[c] > 0]
            w = [quota[c] for c in ok]
            c = rng.choices(ok, weights=w)[0]
            quota[c] -= 1
            pos = LET.index(c)
            opts, notes = q.options[1:], q.notes[1:]
            q.options = opts[:pos] + [q.options[0]] + opts[pos:]
            q.notes = notes[:pos] + [None] + notes[pos:]
            q.ans = pos
        letters.append(LET[q.ans])
    _break_runs(mcs, {id(q) for q in fixed})
    stims, k = {}, 0
    for q in mcs:
        if q.stim is not None and q.stim.id is not None and q.stim.id not in stims:
            raise SystemExit(f"Q{q.n}: a Stim object is shared between sets; give each set its own")
        if q.stim is not None and q.stim.id is None:
            k += 1
            q.stim.id = f"s{k}"
            stims[q.stim.id] = q.stim
    for s in stims.values():
        ns = [q.n for q in mcs if q.stim is s]
        assert ns == list(range(ns[0], ns[-1] + 1)), ns
        s.range = (ns[0], ns[-1])
    return secs, mcs, stims


def _move(q, pos):
    c, nt = q.options.pop(q.ans), q.notes.pop(q.ans)
    q.options.insert(pos, c)
    q.notes.insert(pos, nt)
    q.ans = pos


def _runs_ok(lets, idxs):
    for i in idxs:
        for a in range(max(0, i - 2), min(len(lets) - 2, i + 1)):
            if lets[a] == lets[a + 1] == lets[a + 2]:
                return False
    return True


def _break_runs(mcs, fixed_ids):
    """Remove runs of three equal answer letters without changing the letter counts: re-place a free item, or
    reverse a fixed-order item, and give the letter it gives up to a free item elsewhere."""
    for _ in range(200):
        lets = [LET[q.ans] for q in mcs]
        bad = next((i for i in range(2, len(lets)) if lets[i] == lets[i - 1] == lets[i - 2]), None)
        if bad is None:
            return
        done = False
        for i in (bad, bad - 1, bad - 2):
            q, cur = mcs[i], lets[bad]
            targets = [LET[3 - q.ans]] if id(q) in fixed_ids else [c for c in LET if c != cur]
            for new in targets:
                for j, r in enumerate(mcs):
                    if j == i or id(r) in fixed_ids or lets[j] != new:
                        continue
                    trial = lets[:]
                    trial[i], trial[j] = new, cur
                    if not _runs_ok(trial, [i, j]):
                        continue
                    if id(q) in fixed_ids:
                        q.options, q.notes, q.ans = q.options[::-1], q.notes[::-1], 3 - q.ans
                    else:
                        _move(q, LET.index(new))
                    _move(r, LET.index(cur))
                    done = True
                    break
                if done:
                    break
            if done:
                break
        if not done:
            return


def stim_title(s):
    a, b = s.range
    return f"Question {a}" if a == b else (f"Questions {a} and {b}" if b == a + 1 else f"Questions {a}–{b}")


# ======================================================================== LaTeX
def mc_tex(q, first_of_stim):
    out = []
    if first_of_stim:
        s = q.stim
        out.append(f"\\stimintro{{{tex(stim_title(s))}.}}" + blocks_tex(s.blocks))
    body = blocks_tex(q.prompt)
    if q.tbl:
        body += "\n" + table_tex(q.tbl)
    opts = [tex(o) for o in q.options]
    short = max(plain_len(o) for o in q.options) <= 30
    ch = "\\chtwo" if short else "\\chone"
    out.append(f"\\begin{{qbox}}{{{q.n}}}{body}\n{ch}" + "".join("{" + o + "}" for o in opts) + "\n\\end{qbox}")
    return "\n".join(out)


def part_label_tex(lbl):
    m = re.fullmatch(r"([a-z])(?:\((\w+)\))?", lbl)
    return m.group(1), m.group(2)


def fr_tex(f, n):
    out = [f"\\begin{{frbox}}{{{n}}}\\textbf{{({f.pts} points)}}\\par\n" + blocks_tex(f.stem)]
    out.append("\\begin{enumerate}[label={},leftmargin=2.4em,labelwidth=2em,labelsep=0.4em,align=right,itemsep=4pt]")
    open_sub = False
    for p in f.parts:
        let, sub = part_label_tex(p.label)
        pt = f"{p.pts} point" + ("s" if p.pts > 1 else "")
        if sub is None:
            if open_sub:
                out.append("\\end{enumerate}")
                open_sub = False
            out.append(f"\\item[({let})] " + blocks_tex(p.prompt) + f"\\pts{{{pt}}}")
        else:
            if not open_sub:
                out.append(f"\\item[({let})] " + (blocks_tex(p.lead) if p.lead else "") +
                           "\n\\begin{enumerate}[label={},leftmargin=2.6em,labelwidth=2.2em,labelsep=0.4em,align=right,itemsep=3pt]")
                open_sub = True
            out.append(f"\\item[({sub})] " + blocks_tex(p.prompt) + f"\\pts{{{pt}}}")
    if open_sub:
        out.append("\\end{enumerate}")
    out.append("\\end{enumerate}\n\\end{frbox}")
    return "\n".join(out)


def set_tex(U, letter, mcs, secs, frs):
    N, other = U["n"], "B" if letter == "A" else "A"
    first, last = min(U["topics"]), max(U["topics"], key=lambda t: int(t.split(".")[1]))
    rng = f"{first}–{last}"
    nsec = len(secs)
    lines = [r"\documentclass[11pt]{article}", r"\usepackage{apchem}",
             f"\\doctitle{{Unit {N} Practice Set {letter}:}}",
             f"\\docsubtitle{{30 Multiple-Choice and 2 Free-Response Questions on {tex(U['short'])}, Grouped by Topic}}",
             r"\docstatus{Practice draft}", r"\begin{document}", r"\titleblock", r"\begin{abstract}",
             tex(f"This set covers all of Unit {N}, {U['title']} (Topics {rng}), in 30 multiple-choice and 2 "
                 f"free-response questions, one long (10 points) and one short (4 points). Every item is new; none repeat "
                 f"<i>Unit {N} Practice Set {other}</i> or the worked examples in the <i>Unit {N} Content Guide</i>. "
                 f"The multiple-choice questions are grouped into {['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven'][nsec]} "
                 "sections by topic, so a cluster of misses points to one section of the guide instead of to the whole unit. "
                 "Allow 45 minutes for the multiple choice and 30 minutes for the free response; a calculator, the periodic "
                 "table and the equations sheet are allowed, as on the AP exam. Write each multiple-choice answer on the blank "
                 "to the left of its number, write the free responses on separate paper, finish the whole set, and only then "
                 "turn to the key."),
             r"\end{abstract}",
             r"\leadline{Scoring}{" + tex(
                 "multiple choice out of 30, free response out of 14. 27–30 and 12–14: ready for the exam. 21–26 or 8–11: "
                 "reread the guide section behind each miss and redo its worked examples" +
                 (", then take Set B. " if letter == "A" else ". ") +
                 f"Under 21 or under 8: work through the whole <i>Unit {N} Content Guide</i> again" +
                 (" before taking Set B." if letter == "A" else ", then redo the questions you missed on both sets.")) + "}"]
    seen = set()
    cur = None
    for q in mcs:
        if q.sec != cur:
            cur = q.sec
            ts = sorted({x.topic for x in mcs if x.sec == cur}, key=lambda t: int(t.split(".")[1]))
            tl = f"Topic {ts[0]}" if len(ts) == 1 else (f"Topics {ts[0]}–{ts[-1]}" if _consecutive(ts) else "Topics " + ", ".join(ts))
            lines.append(f"\\section{{{tex(secs[cur])} ({tex(tl)})}}")
        first_stim = q.stim is not None and q.stim.id not in seen
        if q.stim is not None:
            seen.add(q.stim.id)
        lines.append(mc_tex(q, first_stim))
    lines.append(f"\\clearpage\\section{{Free response (Topics {tex(rng)})}}")
    lines.append("Answer on separate paper. Show the setup of every calculation with units, and justify every claim with "
                 "data or with the model it relies on.")
    for i, f in enumerate(frs):
        if i:
            lines.append("\\clearpage")
        lines.append(fr_tex(f, 31 + i))
    # ---- key
    lines.append("\\clearpage\\section*{Answer key}")
    lines.append(tex(f"Count your multiple-choice score out of 30 and your free-response score out of 14. Check each miss "
                     f"against its topic in the <i>Unit {N} Content Guide</i>, where Section <i>n</i> covers Topic {N}.<i>n</i> "
                     f"and Section {len(U['topics']) + 1} covers lab skills and free-response technique. If you get two or more misses on one topic, "
                     "reread that section and redo its worked examples."))
    lines.append("\\par\\textbf{Answers only:}\\par\\nopagebreak\\begin{tabular}{@{}" + "l" * 10 + "@{}}")
    rows = []
    for r in range(0, 30, 10):
        rows.append(" & ".join(f"{q.n}\\,{LET[q.ans]}\\hspace{{1.2em}}" for q in mcs[r:r + 10]))
    lines.append(" \\\\\n".join(rows) + "\n\\end{tabular}\n")
    lines.append("\\begin{longtable}{@{}r@{\\hspace{1.2em}}c@{\\hspace{1.2em}}p{0.70\\linewidth}l@{}}\\toprule\n"
                 "\\# & Ans. & Why & Topic \\\\ \\midrule\\endhead")
    for q in mcs:
        lines.append(f"{q.n} & {LET[q.ans]} & {tex(q.why)} & {q.topic} \\\\")
    lines.append("\\bottomrule\\end{longtable}")
    lines.append("\\clearpage\\textbf{Free-response scoring guide.}\\par")
    for i, f in enumerate(frs):
        lines.append(f"\\par\\needspace{{6\\baselineskip}}\\textbf{{Question {31 + i}}} ({f.pts} points)\\par\\nopagebreak")
        lines.append("\\begin{longtable}{@{}l@{\\hspace{1.2em}}c@{\\hspace{1.2em}}p{0.76\\linewidth}@{}}\\toprule\n"
                     "Part & Pts & What earns the point \\\\ \\midrule\\endhead")
        for p in f.parts:
            let, sub = part_label_tex(p.label)
            lab = f"({let})" + (f"({sub})" if sub else "")
            lines.append(f"{lab} & {p.pts} & {tex(p.sol)} \\\\[2pt]")
        lines.append("\\bottomrule\\end{longtable}")
    lines.append(r"\end{document}")
    return "\n".join(lines) + "\n"


def _consecutive(ts):
    nums = [int(t.split(".")[1]) for t in ts]
    return nums == list(range(nums[0], nums[-1] + 1))


# ======================================================================== quiz dicts
def _pts_part(label, prompt, pts, solution):
    return dict(label=label, max=pts, prompt=prompt, solution=f"<p>{solution}</p>",
                rubric=f"<p>Worth {pts} point{'s' if pts > 1 else ''}.</p>")


def quiz_dict(U, letter, mcs, secs, stims, frs, pages):
    N = U["n"]
    lo = letter.lower()
    url = BASE + f"tests/{N}{lo}/"
    pdf = BASE + f"unit-{N}/ap-chem-unit-{N}-{2 if letter == 'A' else 3}-practice-set-{lo}.pdf"
    guide = BASE + f"unit-{N}/ap-chem-unit-{N}-1-content-guide.pdf"
    first, last = min(U["topics"]), max(U["topics"], key=lambda t: int(t.split(".")[1]))
    topics = {t: (name, pages[t]) for t, name in sorted(U["topics"].items(), key=lambda kv: int(kv[0].split(".")[1]))}
    mc = []
    for q in mcs:
        d = dict(n=q.n, sec=q.sec, topic=q.topic, prompt=inline_html(q.prompt), options=[html(o) for o in q.options],
                 answer=q.ans, ex=dict(idea=html(q.idea), steps=[html(s) for s in q.steps],
                                       others={i: html(v) for i, v in enumerate(q.notes) if i != q.ans}))
        if q.stim is not None:
            d["stim"] = q.stim.id
        if q.tbl is not None:
            d["table"] = table_html(q.tbl).replace('<div class="bt-wrap">', "", 1)[:-6]
        mc.append(d)
    st = {s.id: dict(title=stim_title(s).replace("–", "&ndash;"), html=block_html(s.blocks)) for s in stims.values()}
    fr = []
    for i, f in enumerate(frs):
        parts, seen_lead = [], set()
        for p in f.parts:
            pr = inline_html(p.prompt)
            let = p.label[0]
            if p.lead and let not in seen_lead:
                pr = inline_html(p.lead) + "<br>" + pr
                seen_lead.add(let)
            parts.append(_pts_part(p.label, pr, p.pts, html(p.sol)))
        tl = ", ".join(f.topics)
        fr.append(dict(n=31 + i, mode="points", head=f"{f.pts} points &middot; topic{'s' if len(f.topics) > 1 else ''} {tl}",
                       guide=[t for t in f.topics if t in topics], stem=block_html(f.stem), parts=parts))
    other_note = ", then take Set B" if letter == "A" else ""
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=f"study.ap-chem.{N}{lo}.v1",
        title=f"AP Chemistry Unit {N} Practice Set {letter}",
        desc=f"AP Chemistry Unit {N} ({U['title']}) Practice Set {letter}: 30 multiple-choice questions with worked "
             "explanations and two free-response questions with scoring guides.",
        runhead=f"AP Chemistry &middot; Unit {N} {html(U['short'])} &middot; Practice Set {letter}",
        back=("/study/#ap-chemistry", "Study Library"),
        h1=f'Unit {N} Practice <span style="white-space:nowrap">Set {letter}</span>',
        sub=f"{html(U['title'])} &middot; topics {first}&ndash;{last}",
        metaline="30 multiple-choice (45 min) &middot; 2 free-response, 10 + 4 points (30 min)",
        setupNote="Allow 45 minutes and keep a calculator handy, as on the AP exam.",
        mc=mc, stims=st, fr=fr, sections=secs, topics=topics, topicPrefix="Topic ", topicCol="Topic",
        guideCol="Content Guide section", byTopic="By topic", guide=guide, guideName=f"the <i>Unit {N} Content Guide</i>",
        topicNote="Two or more misses on one topic: reread that section of the Content Guide and redo its worked examples.",
        bands=[[27, "27&ndash;30: ready for the exam (with 12&ndash;14 on the free response)."],
               [21, "21&ndash;26: reread the guide section behind each miss and redo its worked examples" + other_note + "."],
               [0, f"Under 21: work through the whole <i>Unit {N} Content Guide</i> again" +
                (" before taking Set B." if letter == "A" else ", then redo the questions you missed on both sets.")]],
        frIntro="Allow 30 minutes. Show the setup of every calculation with units, and justify every claim with data or with "
                "the model it relies on. Then open the scoring guide and give yourself the points you earned.",
        foot=(f'From <a href="{pdf}"><i>Unit {N} Practice Set {letter}</i></a> (PDF). Answers, free-response points and '
              "scoring guides are the set&rsquo;s own key; the multiple-choice explanations expand on it with the full working "
              "and why each wrong choice is wrong. "
              f'Topic links open the matching section of <a href="{guide}"><i>the Unit {N} Content Guide</i></a>. '
              "Your answers are saved only in this browser."),
    )


# ======================================================================== per unit
def load_unit(mod):
    U = mod.UNIT
    out = {}
    for letter, seed in (("A", 11 * U["n"] + 1), ("B", 11 * U["n"] + 2)):
        items, frs = getattr(mod, f"SET_{letter}"), getattr(mod, f"FR_{letter}")
        secs, mcs, stims = assemble(items, seed)
        assert len(mcs) == 30, (U["n"], letter, len(mcs))
        assert len(frs) == 2 and frs[0].pts == 10 and frs[1].pts == 4
        for q in mcs:
            assert q.topic in U["topics"], (q.n, q.topic)
            assert all(q.notes[i] for i in range(4) if i != q.ans), (U["n"], letter, q.n)
            assert len(set(q.options)) == 4, (U["n"], letter, q.n, q.options)
        out[letter] = (secs, mcs, stims, frs)
    return U, out


def pages_from_aux(aux):
    pages = {}
    for m in re.finditer(r"\\newlabel\{t:([\w.]+)\}\{\{[^{}]*\}\{(\d+)\}", Path(aux).read_text()):
        pages[m.group(1)] = int(m.group(2))
    return pages


def guide_pages():
    p = HERE / "guide_pages.json"
    return json.loads(p.read_text()) if p.exists() else {}
