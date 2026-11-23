"""Extract the APAH vocabulary PDF into source/vocab.json: glossary entries, the 754 questions, and the key.

Needs pypdf (not used at build time). usage, from the repo root:
    PYTHONPATH=<dir with pypdf> python3 quizzes/apah_vocab/extract.py quizzes/apah_vocab/source/vocab.json
(then re-save compactly). Term names are found by their bold font; adjacent bold runs are merged (the okina is a separate run).
"""
import json
import re
import sys

import pypdf  # noqa: E402

r = pypdf.PdfReader("public/study/ap/ap-art-history/apah-vocabulary.pdf")
PAGES = r.pages


def styled(i):
    """Page text with \x01 before bold runs and \x02 after them, \x03 around italic runs."""
    out = []

    def v(text, cm, tm, font, size):
        name = (font or {}).get("/BaseFont", "") if font else ""
        if not text:
            return
        if "Bold" in name and abs(size - 10) < 0.2:
            out.append("\x01" + text + "\x02")
        elif "Italic" in name:
            out.append("\x03" + text + "\x04")
        else:
            out.append(text)
    PAGES[i].extract_text(visitor_text=v)
    return "".join(out).replace("\x02\x01", "")


def clean(s):
    s = re.sub(r"[\x03\x04]", "", s)
    s = re.sub(r"(\w)-\n(\w)", r"\1\2", s)  # hyphenation at line ends
    s = re.sub(r"\s*\n\s*", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---- glossary: pages 3..111 (0-based 2..110), sections 2-9
gloss_text = ""
sec_of_page = {}
for i in range(2, 111):
    t = styled(i)
    t = re.sub(r"\n\d+\s*$", "", t.rstrip())  # page number
    gloss_text += "\n" + t
# section headings like "2 Looking and describing" are bold but larger; they were not marked (size check)
entries = {}
order = []
for chunk in gloss_text.split("\x01")[1:]:
    term, _, rest = chunk.partition("\x02")
    term = clean(term)
    if not term:
        continue
    rest = rest.strip()
    pron = ""
    m = re.match(r"\s*\x03\s*\(([^)]*)\)\s*\x04", rest)
    if m:
        pron = m.group(1)
        rest = rest[m.end():]
    body = clean(rest)
    # strip trailing section headings that leak in (e.g. "3 Painting, drawing and printmaking")
    parts = {}
    m2 = re.split(r"\s*(Think of it as:|Seen in:|See also:)\s*", body)
    parts["def"] = m2[0].strip()
    for k in range(1, len(m2) - 1, 2):
        parts[{"Think of it as:": "think", "Seen in:": "seen", "See also:": "see"}[m2[k]]] = m2[k + 1].strip()
    key = term
    if key in entries:
        key = term + " #2"
    entries[key] = dict(term=term, pron=pron, **parts)
    order.append(key)

# ---- questions: pages 112..226
qtext = "\n".join(PAGES[i].extract_text() for i in range(111, 226))
sections = re.findall(r"10\.(\d+) ([^\n]+)\nQuestions (\d+)–(\d+)", qtext)
qs = []
for m in re.finditer(r"(?m)^(\d+)\. Which term means: (.*?)\n\(A\) (.*?)\n\(B\) (.*?)\n\(C\) (.*?)\n\(D\) (.*?)$", qtext, re.S):
    n = int(m.group(1))
    qs.append(dict(n=n, prompt=clean(m.group(2)), choices=[clean(m.group(k)) for k in range(3, 7)]))

# ---- key: pages 227..274
ktext = "\n".join(PAGES[i].extract_text() for i in range(226, 274))
strip = ktext[:ktext.index("# Ans.")]
letters = {int(a): b for a, b in re.findall(r"(\d+) ([ABCD])\b", strip)}
expl = ktext[ktext.index("# Ans."):]
rows = {}
for m in re.finditer(r"(?m)^(\d+) ([ABCD]) (.*?)(?=^\d+ [ABCD] |\Z)", expl, re.S):
    rows[int(m.group(1))] = clean(m.group(3))

json.dump(dict(entries=entries, order=order, sections=sections, questions=qs, letters=letters, rows=rows),
          open(sys.argv[1], "w"), ensure_ascii=False, indent=0)
print("entries", len(entries), "questions", len(qs), "letters", len(letters), "rows", len(rows), "sections", sections)
