"""Convert the LaTeX *text* used in the study sources to HTML.

Math ($...$, $$...$$, \\(...\\), \\[...\\]) is passed through unchanged as $...$ / $$...$$ so the
builder can pre-render it with KaTeX. Everything else is converted here. Unknown macros raise, so a
new source never renders a stray backslash.
"""
import html
import re

ACCENTS = {
    "'": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "y": "ý", "A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú", "c": "ć", "n": "ń", "s": "ś", "z": "ź"},
    "`": {"a": "à", "e": "è", "i": "ì", "o": "ò", "u": "ù", "A": "À", "E": "È"},
    '"': {"a": "ä", "e": "ë", "i": "ï", "o": "ö", "u": "ü", "A": "Ä", "O": "Ö", "U": "Ü"},
    "^": {"a": "â", "e": "ê", "i": "î", "o": "ô", "u": "û"},
    "~": {"a": "ã", "n": "ñ", "o": "õ", "N": "Ñ"},
    "c": {"c": "ç", "C": "Ç"},
    "v": {"c": "č", "s": "š", "z": "ž", "C": "Č", "S": "Š", "Z": "Ž", "r": "ř", "e": "ě"},
}

# no-argument macros -> HTML
SIMPLE = {
    "S": "§", "dots": "…", "ldots": "…", "textellipsis": "…", "%": "%", "&": "&amp;", "#": "#", "_": "_", "$": "&#36;",
    "{": "{", "}": "}", ",": "&thinsp;", " ": " ", "/": "", "-": "&shy;", "@": "", "quad": "&emsp;", "qquad": "&emsp;&emsp;",
    "textendash": "–", "textemdash": "—", "textbar": "|", "textdegree": "°", "copyright": "©", "pounds": "£",
    "checkmark": "✓", "times": "×", "newline": "<br>", "\\": "<br>", "par": "<br>", "noindent": "", "smallskip": "",
    "medskip": "", "bigskip": "", "hfill": " ", "centering": "", "ae": "æ", "oe": "œ", "o": "ø", "ss": "ß", "i": "ı",
    "LaTeX": "LaTeX", "TeX": "TeX", "item": "", "textquoteright": "’", "textquoteleft": "‘",
}
# one-argument macros -> (open, close); None = drop the argument entirely
WRAP = {
    "emph": ("<i>", "</i>"), "textit": ("<i>", "</i>"), "textbf": ("<b>", "</b>"), "textsc": ('<span class="sc">', "</span>"),
    "underline": ("<u>", "</u>"), "texttt": ("<code>", "</code>"), "textrm": ("", ""), "textnormal": ("", ""),
    "mbox": ("", ""), "hbox": ("", ""), "text": ("", ""), "textup": ("", ""), "textsf": ("", ""),
    "enquote": ("“", "”"), "mathrm": ("", ""), "textsuperscript": ("<sup>", "</sup>"), "textsubscript": ("<sub>", "</sub>"),
    "label": None, "index": None, "vspace": None, "hspace": None, "phantom": None,
}


class LatexError(ValueError):
    pass


def _split_math(s):
    """Yield (is_math, text) pieces; math keeps $..$ / $$..$$ delimiters."""
    pat = re.compile(r"\$\$(.+?)\$\$|\\\[(.+?)\\\]|(?<!\\)\$(.+?)(?<!\\)\$|\\\((.+?)\\\)", re.S)
    pos = 0
    for m in pat.finditer(s):
        if m.start() > pos:
            yield False, s[pos:m.start()]
        if m.group(1) is not None or m.group(2) is not None:
            yield True, "$$" + (m.group(1) if m.group(1) is not None else m.group(2)) + "$$"
        else:
            yield True, "$" + (m.group(3) if m.group(3) is not None else m.group(4)) + "$"
        pos = m.end()
    if pos < len(s):
        yield False, s[pos:]


def _accents(s):
    def rep(m):
        acc, ch = m.group(1), m.group(2) or m.group(3)
        try:
            return ACCENTS[acc][ch]
        except KeyError:
            raise LatexError(f"unknown accent \\{acc}{ch}")
    return re.sub(r"\\(['`\"^~]|c(?= |\{)|v(?= |\{))\s*(?:\{(\\?[A-Za-z])\}|([A-Za-z]))", rep, s)


def _typography(s):
    s = s.replace("---", "—").replace("--", "–")
    s = s.replace("``", "“").replace("''", "”").replace("`", "‘").replace("'", "’")
    return s


class _P:
    def __init__(self, s, macros):
        self.s, self.i, self.macros = s, 0, macros

    def group(self):
        """Read a {...} group at the current position (after optional spaces); return its raw text."""
        while self.i < len(self.s) and self.s[self.i] == " ":
            self.i += 1
        if self.i >= len(self.s) or self.s[self.i] != "{":
            raise LatexError(f"expected {{ at {self.s[self.i:self.i + 30]!r}")
        depth, start = 0, self.i
        while self.i < len(self.s):
            c = self.s[self.i]
            if c == "\\":
                self.i += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    self.i += 1
                    return self.s[start + 1:self.i - 1]
            self.i += 1
        raise LatexError("unbalanced braces")

    def run(self):
        out = []
        s = self.s
        while self.i < len(s):
            c = s[self.i]
            if c == "\\":
                m = re.match(r"\\([A-Za-z]+)", s[self.i:])
                if m:
                    name = m.group(1)
                    self.i += len(m.group(0))
                    if name in self.macros:
                        val = self.macros[name]
                        if callable(val):
                            out.append(val(self))
                        else:
                            out.append(val)
                            self._eat_space()
                    elif name in WRAP:
                        arg = self.group()
                        w = WRAP[name]
                        if w is not None:
                            out.append(w[0] + convert_text(arg, self.macros) + w[1])
                    elif name in SIMPLE:
                        out.append(SIMPLE[name])
                        self._eat_space()
                    else:
                        raise LatexError(f"unknown macro \\{name} near {s[max(0, self.i - 40):self.i + 20]!r}")
                else:
                    ch = s[self.i + 1:self.i + 2]
                    if ch in SIMPLE:
                        out.append(SIMPLE[ch])
                        self.i += 2
                    else:
                        raise LatexError(f"unknown control symbol \\{ch}")
            elif c == "{":
                out.append(convert_text(self.group(), self.macros))
            elif c == "}":
                raise LatexError("stray }")
            elif c == "~":
                out.append("&nbsp;")
                self.i += 1
            else:
                out.append(c)
                self.i += 1
        return "".join(out)

    def _eat_space(self):
        """After a control word, TeX swallows one space or an empty {} group."""
        if self.s.startswith("{}", self.i):
            self.i += 2
        elif self.s.startswith(" ", self.i):
            self.i += 1


def convert_text(s, macros=None):
    """Convert a LaTeX text fragment (no math) to HTML."""
    s = s.replace("&", "\x01AMP\x01").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("\\\x01AMP\x01", "&amp;").replace("\x01AMP\x01", "&amp;")
    s = _typography(_accents(s))
    return _P(s, macros or {}).run()


def to_html(s, macros=None):
    """Convert LaTeX source (text + math) to HTML with $..$ math left for KaTeX."""
    parts = []
    for is_math, piece in _split_math(s):
        parts.append(piece if is_math else convert_text(piece, macros))
    out = re.sub(r"\s*\n\s*", " ", "".join(parts)).strip()
    if "\\" in re.sub(r"\$\$.+?\$\$|\$.+?\$", "", out, flags=re.S):
        raise LatexError(f"backslash left in {out[:80]!r}")
    return out


def esc(s):
    return html.escape(s, quote=True)
