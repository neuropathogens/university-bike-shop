"""Data graphs for the AP science series, drawn twice from one description: pgfplots for the PDFs and inline SVG
for the quiz pages (SVG strokes and text use currentColor, so the graph follows the page's light or dark theme).

    Graph(xlabel, ylabel, x=(min, max, step), y=(min, max, step), series=[Series(name, pts)], kind="line")

kind: "line" (points joined), "scatter" (points only, optional best-fit line via Series(fit=(m, b))),
"bar" (grouped bars; Graph.cats names the groups and each Series.pts is a list of heights).
Points may carry error bars: (x, y, err). Labels are LaTeX ($..$ math, \\Delta, ^2, _x, \\mu, \\circ).
"""
import html
import re
from dataclasses import dataclass, field

COLORS_TEX = ["navy", "cobalt", "orange!85!black", "green!45!black"]
COLORS_SVG = ["currentColor", "#3b6cf6", "#e0661b", "#2f9e44"]
MARKS_TEX = ["*", "square*", "triangle*", "diamond*"]
DASH_TEX = ["solid", "dashed", "dotted", "dashdotted"]
DASH_SVG = ["", "6 4", "2 3", "7 3 2 3"]


@dataclass
class Series:
    name: str
    pts: list
    line: bool = None        # default: kind == "line"
    fit: tuple = None        # (slope, intercept): draw this straight line across the plot (scatter)
    smooth: bool = False
    marks: bool = True       # False for drawn graphs (a v-t graph), True for data


@dataclass
class Graph:
    xlabel: str
    ylabel: str
    x: tuple
    y: tuple
    series: list
    kind: str = "line"
    cats: list = None
    caption: str = ""
    legend: bool = None      # default: more than one series
    width: float = 3.6       # inches in the PDF
    height: float = 2.35
    xticks: list = None      # explicit tick values (else from step)
    yticks: list = None
    curves: list = field(default_factory=list)   # [(name, f, style)] smooth functions drawn as lines
    legend_pos: str = "ne"   # "ne" or "nw"
    notes: list = field(default_factory=list)   # [(x, y, text, where)] point labels; where: above/below/left/right/...

    def __post_init__(self):
        if self.legend is None:
            self.legend = len(self.series) + len(self.curves) > 1


def decimals(step):
    """Decimal places that show every tick of this step exactly (0.05 -> 2, 0.5 -> 1, 2 -> 0)."""
    for d in range(6):
        if abs(round(step * 10 ** d) - step * 10 ** d) < 1e-9:
            return d
    return 6


def num(v, d=None):
    s = f"{v:.{d}f}" if d is not None else f"{v:.6g}"
    if s in ("-0", "-0.0", "-0.00"):
        s = s[1:]
    return s.replace("-", "−") if s.startswith("-") else s


def ticks(lo, hi, step, explicit=None):
    if explicit is not None:
        return list(explicit)
    out, k = [], 0
    while lo + k * step <= hi + 1e-9:
        out.append(round(lo + k * step, 10))
        k += 1
    return out


# ------------------------------------------------------------------ pgfplots
def tex(g):
    x0, x1, _ = g.x
    y0, y1, _ = g.y
    xt, yt = ticks(*g.x, g.xticks), ticks(*g.y, g.yticks)
    opts = [f"width={g.width}in", f"height={g.height}in", "axis lines=left", "grid=major", "grid style={rulegray,line width=0.3pt}",
            f"ymin={y0}", f"ymax={y1}", f"ytick={{{','.join(f'{v:g}' for v in yt)}}}" if yt else "ytick=\\empty",
            "tick label style={font=\\sffamily\\scriptsize}", "label style={font=\\sffamily\\footnotesize}",
            "scaled ticks=false",
            f"yticklabel style={{/pgf/number format/fixed,/pgf/number format/fixed zerofill,/pgf/number format/1000 sep={{}},/pgf/number format/precision={decimals(g.y[2])}}}",
            f"xticklabel style={{/pgf/number format/fixed,/pgf/number format/fixed zerofill,/pgf/number format/1000 sep={{}},/pgf/number format/precision={decimals(g.x[2])}}}",
            f"xlabel={{{g.xlabel}}}", f"ylabel={{{g.ylabel}}}", "every axis plot/.append style={line width=0.8pt}",
            "legend style={font=\\sffamily\\scriptsize,draw=rulegray,fill=white,fill opacity=0.9,text opacity=1}",
            "legend cell align=left", "legend pos=north west" if g.legend_pos == "nw" else "legend pos=north east"]
    if g.kind == "bar":
        n = len(g.cats)
        opts += ["ybar", f"bar width={min(14, 90 / (n * len(g.series))):.1f}pt", f"xmin=-0.6", f"xmax={n - 0.4}",
                 f"xtick={{{','.join(str(i) for i in range(n))}}}", f"xticklabels={{{','.join('{' + c.replace(' / ', '\\\\') + '}' for c in g.cats)}}}",
                 "x tick label style={font=\\sffamily\\scriptsize,align=center}", "major x tick style={draw=none}", "xmajorgrids=false",
                 "enlarge x limits=false"]
    else:
        opts += [f"xmin={x0}", f"xmax={x1}", f"xtick={{{','.join(f'{v:g}' for v in xt)}}}" if xt else "xtick=\\empty"]
    out = ["\\begin{tikzpicture}\\begin{axis}[" + ",\n  ".join(opts) + "]"]
    if y0 < 0 < y1 and g.kind != "bar":
        out.append(f"\\draw[black!75,line width=0.6pt] (axis cs:{x0},0) -- (axis cs:{x1},0);")
    for i, s in enumerate(g.series):
        c = COLORS_TEX[i % 4]
        if g.kind == "bar":
            err = any(len(p) == 2 for p in s.pts if isinstance(p, tuple))
            pts = " ".join(f"({k},{p[0]}) +- (0,{p[1]})" if isinstance(p, tuple) else f"({k},{p})" for k, p in enumerate(s.pts))
            eb = ",error bars/.cd,y dir=both,y explicit,error bar style={black,line width=0.6pt}" if err else ""
            fill = ["navy!80", "cobalt!55", "orange!60", "green!45!black!60"][i % 4]
            out.append(f"\\addplot[draw=navy,fill={fill}{eb}] coordinates {{{pts}}};")
        else:
            line = s.line if s.line is not None else g.kind == "line"
            err = any(len(p) == 3 for p in s.pts)
            pts = " ".join(f"({p[0]},{p[1]}) +- (0,{p[2]})" if len(p) == 3 else f"({p[0]},{p[1]})" for p in s.pts)
            st = [c, f"mark={MARKS_TEX[i % 4]}" if s.marks else "no marks", "mark size=1.7pt", DASH_TEX[i % 4] if line else "only marks",
                  "mark options={solid}"] + (["smooth"] if s.smooth else []) + (["line width=1.1pt"] if not s.marks else [])
            if err:
                st += ["error bars/.cd", "y dir=both", "y explicit", f"error bar style={{{c},line width=0.6pt}}"]
            out.append(f"\\addplot[{','.join(st)}] coordinates {{{pts}}};")
        if g.legend:
            out.append(f"\\addlegendentry{{{s.name}}}")
        if s.fit:
            m, b = s.fit
            out.append(f"\\addplot[{c},domain={x0}:{x1},samples=2,thin] {{{m}*x+{b}}};")
            if g.legend:
                out.append("\\addlegendentry{best fit}")
    for j, (name, f, k) in enumerate(g.curves):
        xs = [x0 + (x1 - x0) * t / 80 for t in range(81)]
        pts = " ".join(f"({x:.5g},{f(x):.5g})" for x in xs if y0 - 1e9 < f(x) < 1e9)
        out.append(f"\\addplot[{COLORS_TEX[k % 4]},{DASH_TEX[k % 4]},smooth,restrict y to domain={y0}:{y1}] coordinates {{{pts}}};")
        if g.legend:
            out.append(f"\\addlegendentry{{{name}}}")
    for x, y, text, where in g.notes:
        out.append(f"\\node[{where},font=\\sffamily\\footnotesize\\bfseries,inner sep=2pt] at (axis cs:{x},{y}) {{{text}}};")
    out.append("\\end{axis}\\end{tikzpicture}")
    body = "\n".join(out)
    cap = f"\\figcap{{{g.caption}}}" if g.caption else ""
    return f"\\figbox{{{body}}}{cap}\n"


# ------------------------------------------------------------------ SVG
SUP = str.maketrans("0123456789-+", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
GREEK = {"Delta": "Δ", "mu": "μ", "theta": "θ", "lambda": "λ", "rho": "ρ", "omega": "ω", "alpha": "α", "tau": "τ",
         "pi": "π", "circ": "°", "Omega": "Ω", "times": "×", "cdot": "·", "phi": "φ", "Phi": "Φ", "epsilon": "ε",
         "varepsilon": "ε", "sigma": "σ", "beta": "β", "gamma": "γ", "eta": "η", "%": "%", "textdegree": "°",
         "pm": "±", "bar": "", "approx": "≈", "ge": "≥", "le": "≤"}


def plain(s):
    """LaTeX label -> plain Unicode for SVG text."""
    t = s.replace("\\,", "\u2009").replace("\\ ", " ").replace("~", "\u00a0").replace("--", "–")
    prev = None
    while prev != t:  # innermost groups first, so nested braces resolve
        prev = t
        t = re.sub(r"\^\{([^{}]*)\}", lambda m: m.group(1).translate(SUP), t)
        t = re.sub(r"_\{([^{}]*)\}", lambda m: m.group(1).translate(SUB) if m.group(1).isdigit() else "\x01" + m.group(1) + "\x02", t)
        t = re.sub(r"\\(?:mathrm|text|textrm|mathit|emph|textit|mathbf|textbf)\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\([A-Za-z]+|%)", lambda m: GREEK.get(m.group(1), m.group(1)), t)
    t = re.sub(r"\^(\S)", lambda m: m.group(1).translate(SUP), t)
    t = re.sub(r"_(\d)", lambda m: m.group(1).translate(SUB), t)
    t = re.sub(r"_([A-Za-z])", "\x01\\1\x02", t)
    t = t.replace("$", "").replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", t).strip()


def label(s):
    """LaTeX label -> escaped SVG text, letter subscripts as <tspan>s."""
    t = html.escape(plain(s))
    return t.replace("\x01", '<tspan baseline-shift="sub" font-size="78%">').replace("\x02", "</tspan>")


def alt(s):
    return plain(s).replace("\x01", "").replace("\x02", "")


def marker(i, x, y, color):
    if i % 4 == 0:
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="{color}"/>'
    if i % 4 == 1:
        return f'<rect x="{x - 3.4:.1f}" y="{y - 3.4:.1f}" width="6.8" height="6.8" fill="{color}"/>'
    if i % 4 == 2:
        return f'<path d="M{x:.1f} {y - 4.4:.1f}L{x + 4.2:.1f} {y + 3:.1f}L{x - 4.2:.1f} {y + 3:.1f}Z" fill="{color}"/>'
    return f'<path d="M{x:.1f} {y - 4.6:.1f}L{x + 4:.1f} {y:.1f}L{x:.1f} {y + 4.6:.1f}L{x - 4:.1f} {y:.1f}Z" fill="{color}"/>'


def svg(g):
    W, H = 480, round(480 * g.height / g.width)
    L, R, T, B = 62, 16, 14, 48 if g.kind != "bar" else 56
    x0, x1, _ = g.x
    y0, y1, _ = g.y
    if g.kind == "bar":
        n = len(g.cats)
        x0, x1 = -0.6, n - 0.4
    X = lambda v: L + (v - x0) / (x1 - x0) * (W - L - R)
    Y = lambda v: H - B - (v - y0) / (y1 - y0) * (H - T - B)
    o = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{html.escape(alt(g.caption) or "Graph of " + alt(g.ylabel) + " versus " + alt(g.xlabel))}" '
         f'style="max-width:100%;height:auto;font:13px system-ui,-apple-system,sans-serif" fill="currentColor">']
    o.append('<g stroke="currentColor" stroke-opacity=".16" stroke-width="1">')
    for v in ticks(*g.y, g.yticks):
        o.append(f'<line x1="{L}" x2="{W - R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
    if g.kind != "bar":
        for v in ticks(*g.x, g.xticks):
            o.append(f'<line y1="{T}" y2="{H - B}" x1="{X(v):.1f}" x2="{X(v):.1f}"/>')
    o.append("</g>")
    o.append(f'<path d="M{L} {T}V{H - B}H{W - R}" fill="none" stroke="currentColor" stroke-width="1.3"/>')
    if y0 < 0 < y1 and g.kind != "bar":
        o.append(f'<line x1="{L}" x2="{W - R}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" stroke="currentColor" stroke-width="1.1"/>')
    for v in ticks(*g.y, g.yticks):
        o.append(f'<text x="{L - 6}" y="{Y(v) + 4.5:.1f}" text-anchor="end">{num(v, decimals(g.y[2]))}</text>')
    if g.kind == "bar":
        for k, c in enumerate(g.cats):
            lines = alt(c).split(" / ") if " / " in c else [alt(c)]
            for j, ln in enumerate(lines):
                o.append(f'<text x="{X(k):.1f}" y="{H - B + 17 + 14 * j}" text-anchor="middle">{html.escape(ln)}</text>')
    else:
        for v in ticks(*g.x, g.xticks):
            o.append(f'<text x="{X(v):.1f}" y="{H - B + 17}" text-anchor="middle">{num(v, decimals(g.x[2]))}</text>')
    o.append(f'<text x="{(L + W - R) / 2:.1f}" y="{H - 8}" text-anchor="middle" font-weight="600">{label(g.xlabel)}</text>')
    o.append(f'<text transform="translate(15 {(T + H - B) / 2:.1f}) rotate(-90)" text-anchor="middle" font-weight="600">{label(g.ylabel)}</text>')
    legend = []
    ns = len(g.series)
    for i, s in enumerate(g.series):
        c = COLORS_SVG[i % 4]
        if g.kind == "bar":
            bw = min(26, (W - L - R) / len(g.cats) * 0.7 / ns)
            for k, p in enumerate(s.pts):
                h_, e = (p if isinstance(p, tuple) else (p, None))
                cx = X(k) + (i - (ns - 1) / 2) * bw
                op = ["0.78", "0.55", "0.6", "0.6"][i % 4]
                o.append(f'<rect x="{cx - bw / 2 + 1:.1f}" y="{Y(h_):.1f}" width="{bw - 2:.1f}" height="{Y(y0) - Y(h_):.1f}" fill="{c}" fill-opacity="{op}" stroke="{c}"/>')
                if e:
                    o.append(f'<path d="M{cx:.1f} {Y(h_ - e):.1f}V{Y(h_ + e):.1f}M{cx - 4:.1f} {Y(h_ - e):.1f}h8M{cx - 4:.1f} {Y(h_ + e):.1f}h8" stroke="currentColor" stroke-width="1.2"/>')
            legend.append((s.name, f'<rect x="-6" y="-6" width="12" height="12" fill="{c}" fill-opacity="{["0.78", "0.55", "0.6", "0.6"][i % 4]}" stroke="{c}"/>'))
            continue
        line = s.line if s.line is not None else g.kind == "line"
        if line:
            d = "M" + "L".join(f"{X(p[0]):.1f} {Y(p[1]):.1f}" for p in s.pts)
            dash = f' stroke-dasharray="{DASH_SVG[i % 4]}"' if DASH_SVG[i % 4] else ""
            o.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2"{dash}/>')
        for p in s.pts:
            if len(p) == 3:
                o.append(f'<path d="M{X(p[0]):.1f} {Y(p[1] - p[2]):.1f}V{Y(p[1] + p[2]):.1f}M{X(p[0]) - 4:.1f} {Y(p[1] - p[2]):.1f}h8M{X(p[0]) - 4:.1f} {Y(p[1] + p[2]):.1f}h8" stroke="{c}" stroke-width="1.2"/>')
            if s.marks:
                o.append(marker(i, X(p[0]), Y(p[1]), c))
        legend.append((s.name, (f'<line x1="-10" x2="10" y1="0" y2="0" stroke="{c}" stroke-width="2"' + (f' stroke-dasharray="{DASH_SVG[i % 4]}"' if DASH_SVG[i % 4] else "") + "/>" if line else "") + (marker(i, 0, 0, c) if s.marks else "")))
        if s.fit:
            m, b = s.fit
            xa, xb = x0, x1
            ya, yb = m * xa + b, m * xb + b
            # clip to the y range
            if ya < y0: xa, ya = (y0 - b) / m, y0
            if ya > y1: xa, ya = (y1 - b) / m, y1
            if yb > y1: xb, yb = (y1 - b) / m, y1
            if yb < y0: xb, yb = (y0 - b) / m, y0
            o.append(f'<line x1="{X(xa):.1f}" y1="{Y(ya):.1f}" x2="{X(xb):.1f}" y2="{Y(yb):.1f}" stroke="{c}" stroke-width="1.3"/>')
            legend.append(("best fit", f'<line x1="-10" x2="10" y1="0" y2="0" stroke="{c}" stroke-width="1.3"/>'))
    for name, f, k in g.curves:
        c = COLORS_SVG[k % 4]
        xs = [x0 + (x1 - x0) * t / 120 for t in range(121)]
        pts = [(x, f(x)) for x in xs]
        pts = [(x, y) for x, y in pts if y0 - (y1 - y0) * 0.02 <= y <= y1 + (y1 - y0) * 0.02]
        d = "M" + "L".join(f"{X(x):.1f} {Y(y):.1f}" for x, y in pts)
        dash = f' stroke-dasharray="{DASH_SVG[k % 4]}"' if DASH_SVG[k % 4] else ""
        o.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2"{dash}/>')
        legend.append((name, f'<line x1="-10" x2="10" y1="0" y2="0" stroke="{c}" stroke-width="2"{dash}/>'))
    OFF = {"above": (0, -9, "middle"), "below": (0, 18, "middle"), "left": (-8, 5, "end"), "right": (8, 5, "start"),
           "above left": (-6, -7, "end"), "above right": (6, -7, "start"), "below left": (-6, 16, "end"), "below right": (6, 16, "start")}
    for x, y, text, where in g.notes:
        dx, dy, anc = OFF[where]
        o.append(f'<text x="{X(x) + dx:.1f}" y="{Y(y) + dy:.1f}" text-anchor="{anc}" font-weight="700">{label(text)}</text>')
    if g.legend and legend:
        wmax = max(len(alt(n)) for n, _ in legend) * 7.2 + 34
        lx = L + 10 if g.legend_pos == "nw" else W - R - wmax - 6
        o.append(f'<rect x="{lx:.1f}" y="{T + 4}" width="{wmax:.1f}" height="{len(legend) * 19 + 8}" fill="var(--bg,#fff)" fill-opacity=".92" stroke="currentColor" stroke-opacity=".3"/>')
        for j, (name, sym) in enumerate(legend):
            yy = T + 4 + 14 + j * 19
            o.append(f'<g transform="translate({lx + 16:.1f} {yy - 4})">{sym}</g><text x="{lx + 32:.1f}" y="{yy + 1}">{label(name)}</text>')
    o.append("</svg>")
    cap = f'<figcaption>{label(g.caption)}</figcaption>' if g.caption else ""
    return f'<figure class="fig sci-fig">{"".join(o)}{cap}</figure>'
