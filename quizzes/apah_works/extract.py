"""Extract apah-250-every-work-explained.pdf into source/works.json: per-work entries, the 500 practice questions, and the key.

Needs pypdf (not used at build time). usage, from the repo root:
    PYTHONPATH=<dir with pypdf> python3 quizzes/apah_works/extract.py quizzes/apah_works/source/works.json
"""
import json
import re
import sys

import pypdf

r = pypdf.PdfReader("public/study/ap/ap-art-history/apah-250-every-work-explained.pdf")
P = [p.extract_text() for p in r.pages]


def clean(s):
    s = re.sub(r"(\w)-\n(\w)", r"\1\2", s)
    s = re.sub(r"\s*\n\s*", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ---- entries: pages 3..582; each starts at "<sec>.<k> No. <n> <title>"
body = "\n".join(re.sub(r"\n\d+\s*$", "", P[i].rstrip()) for i in range(2, 582))
heads = list(re.finditer(r"(?m)^(\d+)\.(\d+) No\. (\d+) (.+)$", body))
works = {}
for h, nxt in zip(heads, heads[1:] + [None]):
    n = int(h.group(3))
    text = body[h.end():nxt.start() if nxt else len(body)]
    title = h.group(4).strip()
    rest_lines = text.lstrip("\n").split("\n")
    while title.count("(") > title.count(")") and rest_lines:  # a long title wraps onto the next line
        nxt_line = rest_lines.pop(0).strip()
        title = title[:-1] + nxt_line if title.endswith("-") else title + " " + nxt_line
    e = dict(n=n, section=f"{h.group(1)}.{h.group(2)}", title=title)
    for field in ("Artist or culture", "Date", "Medium", "Content area"):
        m = re.search(r"(?m)^" + field + r" (.+)$", text)
        if m:
            e[field.split()[0].lower()] = m.group(1).strip()
    m = re.search(r"In plain English\.(.*?)(?=\nSpot it\.|\nRemember it\.|\nForm:)", text, re.S)
    e["plain"] = clean(m.group(1)) if m else ""
    for label, key in (("Spot it.", "spot"), ("Remember it.", "remember")):
        m = re.search(re.escape(label) + r"(.*?)(?=\n(?:Spot it\.|Remember it\.|Form:))", text, re.S)
        if m:
            e[key] = clean(m.group(1))
    bullets = {}
    for label, key in (("Form:", "form"), ("Function:", "function"), ("Content:", "content"), ("Context:", "context")):
        m = re.search(r"(?m)^" + label + r"[^\n]*\n(.*?)(?=^(?:Form:|Function:|Content:|Context:|Compare with\.|Vocabulary\.)|\Z)", text, re.S)
        if m:
            bullets[key] = [clean(b) for b in re.split(r"(?m)^• ", m.group(1)) if clean(b)]
    # the testable points list follows Context (it has no fixed heading), up to "Compare with."
    m = re.search(r"(?ms)^Compare with\.(.*?)(?=^Vocabulary\.|\Z)", text)
    e["compare"] = [clean(b) for b in re.split(r"(?m)^• ", m.group(1)) if clean(b)] if m else []
    m = re.search(r"(?ms)^Vocabulary\.(.*)", text)
    e["vocab"] = clean(m.group(1)) if m else ""
    e["bullets"] = bullets
    e["page"] = next(i + 1 for i in range(2, 582) if re.search(r"(?m)^\d+\.\d+ No\. %d " % n, P[i]))
    e["images"] = sorted(int(m) for m in re.findall(r"Figure %d(?:\.(\d+))?:" % n, text) if m) or [1]
    works[n] = e

# ---- questions: pages 583..645
qtext = "\n".join(P[i] for i in range(582, 645))
sections = re.findall(r"12\.(\d+) ([^\n]+)\nQuestions (\d+)–(\d+)", qtext)
qs = []
for m in re.finditer(r"(?ms)^(\d+)\. \[No\. (\d+)\] (.*?)\n\(A\) (.*?)\n\(B\) (.*?)\n\(C\) (.*?)\n\(D\) (.*?)(?=\n\d+\. \[No\.|\n12\.\d|\n\d+\s*$|\Z)", qtext):
    qs.append(dict(n=int(m.group(1)), work=int(m.group(2)), prompt=clean(m.group(3)),
                   choices=[clean(re.sub(r"\n\d+$", "", m.group(k))) for k in range(4, 8)]))

# ---- key: pages 646..
ktext = "\n".join(P[i] for i in range(645, len(P)))
strip = ktext[:ktext.index("# Ans.")]
letters = {int(a): b for a, b in re.findall(r"(\d+) ([ABCD])\b", strip)}
rows = {}
expl = ktext[ktext.index("# Ans."):]
for m in re.finditer(r"(?ms)^(\d+) ([ABCD]) (.*?)(?=^\d+ [ABCD] |\Z)", expl):
    txt = re.sub(r"(?m)^# Ans\. Why Rule \(work\)\s*$", "", m.group(3))
    txt = re.sub(r"\n\d+\s*$", "", txt.strip())
    why = clean(re.split(r"\sNo\. \d+,", " " + txt)[0])
    rows[int(m.group(1))] = why

json.dump(dict(works=works, sections=sections, questions=qs, letters=letters, rows=rows),
          open(sys.argv[1], "w"), ensure_ascii=False, separators=(",", ":"))
print("works", len(works), "questions", len(qs), "letters", len(letters), "rows", len(rows), "sections", len(sections))
