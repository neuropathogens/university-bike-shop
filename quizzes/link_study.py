"""Add a "Quiz" link next to every document on /study that has a quiz (from manifest.json).

    python3 -I quizzes/link_study.py

Idempotent: existing quiz links are replaced, so it can be rerun after every family is built.
EXTRA covers quizzes that are not tied to one PDF row.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX = HERE.parent / "public/study/index.html"
# row link -> [(quiz url, label)] for quizzes not keyed by a PDF in manifest.json
EXTRA = {"/study/ap/ap-art-history/": [("/study/ap/ap-art-history/tests/5/", "Unit 5 test")]}
CSS = ".docs .t a.qz{display:inline-block;margin-left:8px;padding:0 6px;border:1px solid currentColor;font-family:var(--mono);font-size:12.5px;font-weight:400;line-height:1.55;text-decoration:none;vertical-align:1px;white-space:nowrap}\n.docs .t a.qz:hover{background:var(--fg);color:var(--bg)}\n"
MARK = "/* quiz links */\n"


def main():
    html = INDEX.read_text()
    manifest = json.loads((HERE / "manifest.json").read_text())
    links = {pdf: [(url, "Quiz")] for pdf, url in manifest.items()}
    links.update(EXTRA)
    if MARK in html:  # replace our CSS block (it runs from MARK to </style>)
        i = html.index(MARK)
        html = html[:i] + html[html.index("</style>", i):]
    html = html.replace("</style>", MARK + CSS + "</style>", 1)
    html = re.sub(r' <a class="qz" href="[^"]*">[^<]*</a>', "", html)  # drop old quiz links
    found = set()

    def row(m):
        href, rest = m.group(1), m.group(0)
        if href not in links:
            return rest
        found.add(href)
        add = "".join(f' <a class="qz" href="{u}">{lab}</a>' for u, lab in links[href])
        return rest + add
    html = re.sub(r'<td class="t"><a href="([^"]+)">[^<]*</a>', row, html)
    missing = set(links) - found
    if missing:
        raise SystemExit(f"no /study row for: {sorted(missing)}")
    INDEX.write_text(html)
    print(f"linked {len(found)} rows, {sum(len(v) for v in links.values())} quizzes")


if __name__ == "__main__":
    main()
