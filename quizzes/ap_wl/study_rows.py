"""Write (or rewrite) one world-language section of public/study/index.html from the published PDFs.

    write_section(L, DOCS, heading, blurb, subs, before_id)

subs maps "<stem>-<kind>" to the row's one-line description. The section goes in front of the section whose id is
before_id (AP subjects are alphabetical) or replaces an existing section with the same id. Run link_study.py
afterwards to add the Quiz links.
"""
import os
import re

from pypdf import PdfReader

ENGINE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(ENGINE))
INDEX = os.path.join(REPO, "public", "study", "index.html")


def size(path):
    b = os.path.getsize(path)
    return f"{b / 1048576:.1f} MB" if b >= 1048576 else f"{round(b / 1024)} KB"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def row(L, d, sub):
    path = os.path.join(REPO, "public", "study", "ap", L.slug, f"{L.prefix}{d.stem}-{d.kind}.pdf")
    href = f"{L.base}{L.prefix}{d.stem}-{d.kind}.pdf"
    unit = d.stem[:2]
    num = str(int(unit)) if d.kind == "guide" else ""
    if d.kind == "guide":
        title = f"{d.short} Study Guide: {d.sub}"
    else:
        title = f"{d.short} Question Set" + (f": {d.sub}" if unit == "00" else "")
    pages = len(PdfReader(path).pages)
    return (f'<tr><td class="num">{num}</td><td class="t"><a href="{href}">{esc(title)}</a><span class="sub">{esc(sub)}</span></td>'
            f'<td class="meta">{pages} pp</td><td class="meta">{size(path)}</td></tr>')


def write_section(L, DOCS, heading, blurb, subs, before_id):
    pub = os.path.join(REPO, "public", "study", "ap", L.slug)
    pack = os.path.join(pub, f"{L.prefix}complete-pack.pdf")
    zpath = os.path.join(pub, f"{L.prefix}study-series.zip")
    rows = "\n".join(row(L, d, subs[f"{d.stem}-{d.kind}"]) for d in DOCS)
    sec = (f'  <section class="subj" id="{L.slug}">\n    <h3>{esc(heading)}</h3>\n    <p class="blurb">{blurb}</p>\n'
           f'    <p class="all"><a class="btn" href="{L.base}{L.prefix}complete-pack.pdf">Complete pack, one PDF <span class="muted">'
           f'· {len(PdfReader(pack).pages)} pp · {size(pack)}</span></a><a class="btn" href="{L.base}{L.prefix}study-series.zip">'
           f'All PDFs + LaTeX source (.zip) <span class="muted">· {size(zpath)}</span></a></p>\n'
           f'    <table class="docs"><tbody>\n{rows}\n    </tbody></table>\n  </section>\n')
    html = open(INDEX, encoding="utf8").read()
    pat = re.compile(rf'  <section class="subj" id="{re.escape(L.slug)}">.*?</section>\n', re.S)
    if pat.search(html):
        html = pat.sub(lambda m: sec, html, count=1)
    else:
        anchor = f'  <section class="subj" id="{before_id}">'
        if anchor not in html:
            raise SystemExit(f"no section {before_id!r} in /study")
        html = html.replace(anchor, sec + anchor, 1)
    open(INDEX, "w", encoding="utf8").write(html)
    print(f"wrote the {heading} section of /study ({len(DOCS)} rows)")
