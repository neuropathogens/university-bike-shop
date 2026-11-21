#!/usr/bin/env python3
"""Build public/directory/index.html: a tree of every page and file on the site.

Run from the repo root after adding, moving or removing a page or download:

    python3 scripts/build_directory.py

The page list (titles, descriptions, visibility) is written out by hand in
TREE below. File lists (PDFs, STLs, zips) are read from public/ so they stay
complete on their own. The script fails if public/ holds an HTML page that
TREE does not mention, so new pages cannot go missing silently.
"""

from __future__ import annotations

import datetime as dt
import html
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
OUT = PUBLIC / "directory" / "index.html"

# Pages that exist but are deliberately left off the directory (direct link only).
HIDDEN = set()

DOWNLOAD_EXT = (".pdf", ".zip", ".tar.gz", ".stl", ".stl.gz", ".step", ".3mf")


def page(path, title, desc, vis, children=(), files=None, note=None):
    return {"kind": "page", "path": path, "title": title, "desc": desc, "vis": vis,
            "children": list(children), "files": files, "note": note}


def folder(path, children=(), files=None, desc=None, anchor=None):
    return {"kind": "folder", "path": path, "children": list(children), "files": files,
            "desc": desc, "anchor": anchor}


def files(directory, label, anchor=None, recursive=False):
    """A collapsible list of the downloads in public/<directory>."""
    return {"dir": directory, "label": label, "anchor": anchor, "recursive": recursive}


def stl_part(slug, name):
    return folder(f"/secret/climbing/holds/stl/{slug}/",
                  files=files(f"secret/climbing/holds/stl/{slug}", "files"),
                  desc=name, anchor=f"/secret/climbing/holds/stl/#{slug}")


def quiz_folder(prefix, anchor):
    """The interactive quizzes under public<prefix>tests/ (built by quizzes/build.py), as one folder."""
    import re as _re
    base = PUBLIC / prefix.strip("/") / "tests"
    if not base.is_dir():
        return []
    def natural(s):
        return [int(x) if x.isdigit() else x for x in _re.split(r"(\d+)", s)]
    pages = []
    for d in sorted((d for d in base.iterdir() if (d / "index.html").exists()), key=lambda d: natural(d.name)):
        m = _re.search(r"<title>([^<]*)</title>", (d / "index.html").read_text(errors="ignore"))
        pages.append(page(f"{prefix}tests/{d.name}/", m.group(1) if m else d.name, "Interactive quiz with explanations.", "unlisted"))
    return [folder(f"{prefix}tests/", pages, desc="Quizzes", anchor=anchor)]


TREE = page("/", "Home", "The shop, what it sells, and how to book an appointment.", "nav", [
    page("/inventory", "Inventory", "Used road, gravel, triathlon and mountain bikes for sale.", "nav"),
    page("/sell-your-bike", "Sell Your Bike", "Consignment for a 10% commission.", "nav"),
    page("/service", "Service", "Tune-up and repair prices.", "nav"),
    page("/bike-fits", "Bike Fits", "Camera-based bike fitting for $99.", "nav"),
    page("/summer-camp", "Summer Camp", "The free five-day summer bike camp: photos and write-up.", "nav"),
    page("/events", "Events", "Past camps, community repair days and partnerships, with Instagram embeds.", "nav"),
    page("/projects", "Projects", "Bike-fit software, the open-source bikeparts library and the 3D-printable MTB launch.", "nav"),
    page("/reviews", "Reviews", "Facebook Marketplace seller ratings and reviews, plus Instagram Rider Spotlights.", "nav"),
    page("/sponsorships", "Sponsorships", "Paly Cycling Club, Stanford Cycling and school repair events.", "nav"),
    page("/about-us", "About Us", "The student team behind the shop.", "nav"),
    page("/location-hours", "Location & Hours", "Appointment-only workshop in Crescent Park, Palo Alto.", "nav"),

    page("/shooter/", "UBS Shooter", "Browser FPS game: multiplayer, ranked, Quick Play, zombies.", "unlisted"),

    page("/study/", "Study Library", "Index of every study PDF, with page counts and sizes.", "unlisted", [
        folder("/study/act/", [
            folder("/study/act/english/", quiz_folder("/study/act/english/", "/study/#act-english"), files=files("study/act/english", "PDFs"), anchor="/study/#act-english"),
            folder("/study/act/math/", quiz_folder("/study/act/math/", "/study/#act-math"), files=files("study/act/math", "PDFs"), anchor="/study/#act-math"),
            folder("/study/act/reading/", quiz_folder("/study/act/reading/", "/study/#act-reading"), files=files("study/act/reading", "PDFs"), anchor="/study/#act-reading"),
            folder("/study/act/science/", quiz_folder("/study/act/science/", "/study/#act-science"), files=files("study/act/science", "PDFs"), anchor="/study/#act-science"),
        ], desc="ACT", anchor="/study/#act"),
        folder("/study/sat/", [
            folder("/study/sat/conventions/", quiz_folder("/study/sat/conventions/", "/study/#sat-conventions"), files=files("study/sat/conventions", "PDFs"),
                   desc="Standard English Conventions", anchor="/study/#sat-conventions"),
            folder("/study/sat/vocabulary/", quiz_folder("/study/sat/vocabulary/", "/study/#sat-vocabulary"), files=files("study/sat/vocabulary", "PDFs"),
                   desc="Vocabulary", anchor="/study/#sat-vocabulary"),
        ], desc="SAT", anchor="/study/#sat"),
        folder("/study/math/", [
            folder("/study/math/linear-algebra/", quiz_folder("/study/math/linear-algebra/", "/study/#linear-algebra"), files=files("study/math/linear-algebra", "PDFs"), anchor="/study/#linear-algebra"),
            folder("/study/math/multivariable-calculus/", quiz_folder("/study/math/multivariable-calculus/", "/study/#multivariable-calculus"), files=files("study/math/multivariable-calculus", "PDFs"), anchor="/study/#multivariable-calculus"),
            folder("/study/math/real-analysis/", quiz_folder("/study/math/real-analysis/", "/study/#real-analysis"), files=files("study/math/real-analysis", "PDFs"), anchor="/study/#real-analysis"),
            folder("/study/math/differential-equations/", quiz_folder("/study/math/differential-equations/", "/study/#differential-equations"), files=files("study/math/differential-equations", "PDFs"), anchor="/study/#differential-equations"),
        ], desc="College math", anchor="/study/#math"),
        folder("/study/ap/", [
            page("/study/ap/ap-art-history/", "APAH 250",
                 "All 250 AP Art History works: browse, flashcards and quizzes.", "unlisted",
                 quiz_folder("/study/ap/ap-art-history/", "/study/#ap-art-history"),
                 files=files("study/ap/ap-art-history", "PDFs", anchor="/study/#ap-art-history"),
                 note="Each work has a deep link, #w1 to #w250 (e.g. #w12)."),
            folder("/study/ap/ap-chemistry/", [
                folder("/study/ap/ap-chemistry/unit-5/", files=files("study/ap/ap-chemistry/unit-5", "PDFs"),
                       desc="Unit 5, Kinetics", anchor="/study/#ap-chemistry"),
                *quiz_folder("/study/ap/ap-chemistry/", "/study/#ap-chemistry"),
            ], desc="AP Chemistry", anchor="/study/#ap-chemistry"),
            folder("/study/ap/ap-economics/", [
                folder("/study/ap/ap-economics/macro/", files=files("study/ap/ap-economics/macro", "PDFs"),
                       desc="AP Macroeconomics, Units 1–6", anchor="/study/#ap-macroeconomics"),
                folder("/study/ap/ap-economics/micro/", files=files("study/ap/ap-economics/micro", "PDFs"),
                       desc="AP Microeconomics, Units 1–6", anchor="/study/#ap-microeconomics"),
            ], files=files("study/ap/ap-economics", "LaTeX source"), desc="AP Economics", anchor="/study/#ap-macroeconomics"),
            folder("/study/ap/ap-english-literature/", [
                page("/study/ap/ap-english-literature/xyz-essay/", "The XYZ Essay",
                     "AP English Literature essay guide: thesis, quote units, scoring guide, Gatsby planning kit.", "unlisted"),
            ], desc="AP English Literature", anchor="/study/#ap-english-literature"),
            folder("/study/ap/ap-psychology/", quiz_folder("/study/ap/ap-psychology/", "/study/#ap-psychology"), files=files("study/ap/ap-psychology", "PDFs"),
                   desc="AP Psychology, Part 0 and Units 1–5", anchor="/study/#ap-psychology"),
            folder("/study/ap/ap-statistics/", [
                folder("/study/ap/ap-statistics/unit-6/", files=files("study/ap/ap-statistics/unit-6", "PDFs"),
                       desc="Unit 6, Sampling Distributions", anchor="/study/#ap-statistics"),
                *quiz_folder("/study/ap/ap-statistics/", "/study/#ap-statistics"),
            ], desc="AP Statistics", anchor="/study/#ap-statistics"),
        ], desc="AP", anchor="/study/#ap"),
    ]),

    page("/poker/", "Live Hold’em Tables", "Two papers for beginners at live no-limit hold’em: decision tables and mental-game tables.", "unlisted",
         files=files("poker", "PDFs")),

    folder("/secret/", [
        page("/secret/changelog/", "Site Changelog", "Everything that has changed on the site since June 2026, newest first.", "noindex"),
        page("/secret/claude-audit/", "Sixty-One Nights", "One story per week from fifteen weeks of a nightly activity log.", "noindex"),
        folder("/secret/climbing/", [
            page("/secret/climbing/holds/", "grip-lab: 3D-Printed Grip Trainers", "Working paper on ten printed bouldering grip and finger trainers, with build guide.", "noindex", [
                page("/secret/climbing/holds/stl/", "grip-lab: Print Files", "STL viewer and downloads for every printed piece, with quantities and materials.", "noindex", [
                    stl_part("edge_block", "Modular edge block"),
                    stl_part("load_cell_gauge", "Load-cell gauge housing"),
                    stl_part("pinch_block", "Adjustable pinch block"),
                    stl_part("sloper_dial", "Sloper dial"),
                    stl_part("warmup_puck", "Warm-up edge puck"),
                    stl_part("extensor_trainer", "Extensor trainer"),
                    stl_part("pocket_block", "Pocket block"),
                    stl_part("finger_isolation", "Finger isolation trainer"),
                    stl_part("dumbbell_clamp", "Hex dumbbell pinch clamp"),
                    stl_part("wrist_roller", "Thick-grip wrist roller"),
                    stl_part("coupons", "Tolerance coupons"),
                ], files=files("secret/climbing/holds/stl", "bundle zips")),
            ]),
            page("/secret/climbing/gauge/", "grip-lab gauge", "Web Bluetooth app for the load-cell gauge: live force, peak, RFD, repeaters.", "noindex",
                 note="Add ?demo to try it without the hardware."),
        ]),
        folder("/secret/cycling/", [
            page("/secret/cycling/3d-parts/", "Bikeparts: Printable Bicycle Accessories", "Open-source 3D-printable bike parts, with downloads for every size.", "noindex", [
                folder("/secret/cycling/3d-parts/files/", files=files("secret/cycling/3d-parts/files", "zips"),
                       anchor="/secret/cycling/3d-parts/#files"),
            ]),
        ]),
        folder("/secret/projects/", [
            page("/secret/projects/wbi/", "WBI Projects", "Twelve Wang Brothers Investments real-estate tools, moved here from their Netlify sites.", "noindex", [
                page("/secret/projects/wbi/wbi1/", "Research Drive Deal Analyzer", "3043–3075 Research Drive, Richmond, CA: deal analyzer.", "noindex"),
                page("/secret/projects/wbi/wbi2/", "Parkway Business Center Operations", "Operations dashboard for Parkway Business Center.", "noindex"),
                page("/secret/projects/wbi/wbi3/", "Evans Manor Strategy", "Evans Manor investment strategy and outlook.", "noindex"),
                page("/secret/projects/wbi/wbi4/", "Evans Manor Calculator", "Investment calculator for Evans Manor, 2316 Haste Street, Berkeley.", "noindex"),
                page("/secret/projects/wbi/wbi5/", "Evans Manor Monte Carlo", "Monte Carlo simulation for Evans Manor.", "noindex"),
                page("/secret/projects/wbi/wbi6/", "WBI6 Investment Simulator", "Deterministic model and Monte Carlo risk engine.", "noindex"),
                page("/secret/projects/wbi/wbi7/", "WBI7 In-House ARGUS", "Lease-level institutional DCF, with pitch, roadmap, sample deck, docs and tests.", "noindex"),
                page("/secret/projects/wbi/wbi8/", "Reno-to-Return Bridge", "Value-add underwriting.", "noindex"),
                page("/secret/projects/wbi/wbi10/", "Sub Bid Leveler", "Subcontractor bid leveling.", "noindex"),
                page("/secret/projects/wbi/dorminvestmentcalculator/", "Dorm Investment Calculator", "Multi-unit residential underwriting.", "noindex"),
                page("/secret/projects/wbi/montecarloinvestment/", "Dorm Investment Monte Carlo", "Multi-unit residential risk simulation.", "noindex"),
                page("/secret/projects/wbi/calwbi/", "calwbi", "Forwards to a Google Form.", "redirect"),
            ]),
        ]),
        page("/secret/directory/", "Old site directory", "Redirects here.", "redirect"),
    ]),

    page("/directory/", "Site Directory", "This page.", "noindex"),
])

SYSTEM_FILES = [
    ("/sitemap.xml", "Sitemap for search engines. Lists the {n} navigation pages only."),
    ("/robots.txt", "Crawler rules. Allows everything and points to the sitemap."),
    ("/llms.txt", "Plain-text summary of the shop for AI assistants."),
    ("/manifest.webmanifest", "Web-app manifest (name, colours, icons)."),
    ("/favicon.ico", "Browser-tab icon. Also /icon.svg, /apple-icon.png, /icon-192.png, /icon-512.png and /icon-maskable-512.png."),
]

VIS = {
    "nav": ("public", "In the navigation bar and the sitemap."),
    "unlisted": ("unlisted", "Not linked from the public site, but search engines may index it."),
    "noindex": ("noindex", "Not linked from the public site, and kept out of search engines."),
    "redirect": ("redirect", "Old address that forwards somewhere else."),
}


# ---------------------------------------------------------------- helpers

def tracked_public_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "public"], cwd=ROOT, check=True,
                         capture_output=True, text=True).stdout.split()
    return [p[len("public/"):] for p in out]


TRACKED = tracked_public_files()


def human(n: int) -> str:
    if n < 1000:
        return f"{n} B"
    for unit in ("KB", "MB", "GB"):
        n /= 1000
        if n < 1000 or unit == "GB":
            return f"{n:.1f}&nbsp;{unit}" if n < 10 else f"{n:.0f}&nbsp;{unit}"
    return ""


def list_downloads(spec) -> list[tuple[str, int]]:
    prefix = spec["dir"].strip("/") + "/"
    found = []
    for rel in TRACKED:
        if not rel.startswith(prefix) or not rel.endswith(DOWNLOAD_EXT):
            continue
        if not spec["recursive"] and "/" in rel[len(prefix):]:
            continue
        found.append((rel, (PUBLIC / rel).stat().st_size))
    return sorted(found)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def segment(path: str) -> str:
    if path == "/":
        return "universitybikeshop.com/"
    trail = "/" if path.endswith("/") else ""
    return path.rstrip("/").rsplit("/", 1)[-1] + trail


def all_pages(node, acc):
    if node["kind"] == "page":
        acc.append(node)
    for c in node["children"]:
        all_pages(c, acc)
    return acc


def render_files(spec) -> str:
    items = list_downloads(spec)
    if not items:
        return ""
    total = sum(s for _, s in items)
    kinds = sorted({re.sub(r"^[^.]*", "", Path(r).name).lstrip(".").upper() for r, _ in items})
    rows = []
    for rel, size in items:
        name = Path(rel).name
        note = ' <span class="m">viewer copy</span>' if name.endswith(".stl.gz") else ""
        rows.append(f'<li data-k="{esc("/" + rel.lower())}"><a class="tt" href="/{esc(rel)}" download>{esc(name)}</a>'
                    f'<span class="sz">{human(size)}</span>{note}</li>')
    count = len(items)
    label = f'{count} {"file" if count == 1 else "files"} &middot; {"/".join(kinds)} &middot; {human(total)}'
    return (f'<details class="files"><summary>{label}</summary><ul>{"".join(rows)}</ul></details>')


def render(node) -> str:
    path = node["path"]
    key = (path + " " + (node.get("title") or "") + " " + (node.get("desc") or "")).lower()
    parts = [f'<li data-k="{esc(key)}">', '<div class="node">']
    if node["kind"] == "page":
        tag, tip = VIS[node["vis"]]
        parts.append(f'<a class="tt seg" href="{esc(path)}" title="{esc(path)}">{esc(segment(path))}</a>')
        parts.append(f'<span class="tag {tag}" title="{esc(tip)}">{tag}</span>')
        parts.append(f'<span class="ttl">{esc(node["title"])}</span>')
        body = f'<div class="desc">{esc(node["desc"])}'
        if node["note"]:
            body += f' <span class="m">{esc(node["note"])}</span>'
        body += "</div>"
    else:
        label = esc(segment(path))
        if node.get("anchor"):
            parts.append(f'<a class="tt seg dir" href="{esc(node["anchor"])}" title="{esc(path)}">{label}</a>')
        else:
            parts.append(f'<span class="tt seg dir" title="{esc(path)}">{label}</span>')
        if node.get("desc"):
            parts.append(f'<span class="ttl m">{esc(node["desc"])}</span>')
        body = ""
    parts.append("</div>")
    parts.append(body)
    if node["files"]:
        parts.append(render_files(node["files"]))
    if node["children"]:
        parts.append('<ul>' + "".join(render(c) for c in node["children"]) + "</ul>")
    parts.append("</li>")
    return "".join(parts)


def check_coverage(pages) -> None:
    listed = {p["path"].rstrip("/") or "/" for p in pages} | {h.rstrip("/") for h in HIDDEN}
    missing = []
    for rel in TRACKED:
        if rel.endswith("index.html"):
            url = "/" + rel[: -len("index.html")]
            if url.rstrip("/") not in listed:
                missing.append(url)
    app_routes = [p.parent.name for p in (ROOT / "app").glob("*/page.tsx")]
    for r in app_routes:
        if f"/{r}" not in listed:
            missing.append(f"/{r}")
    if missing:
        sys.exit("Pages missing from TREE in scripts/build_directory.py: " + ", ".join(sorted(missing)))


def main() -> None:
    pages = all_pages(TREE, [])
    check_coverage(pages)
    counts = {v: sum(1 for p in pages if p["vis"] == v) for v in VIS}
    downloads = [r for r in TRACKED if r.endswith(DOWNLOAD_EXT)]
    dl_size = sum((PUBLIC / r).stat().st_size for r in downloads)
    today = dt.date.today()
    date = f"{today:%B} {today.day}, {today.year}"

    legend = "".join(f'<li><span class="tag {t}">{t}</span> {esc(tip)}</li>' for t, tip in VIS.values())
    system = "".join(
        f'<tr><td><a class="tt" href="{p}">{p}</a></td><td>{esc(d.format(n=counts["nav"]))}</td></tr>'
        for p, d in SYSTEM_FILES)

    template = (ROOT / "scripts" / "directory_template.html").read_text()
    out = (template
           .replace("{{DATE}}", date)
           .replace("{{N_PAGES}}", str(sum(counts[v] for v in ("nav", "unlisted", "noindex"))))
           .replace("{{N_NAV}}", str(counts["nav"]))
           .replace("{{N_UNLISTED}}", str(counts["unlisted"]))
           .replace("{{N_NOINDEX}}", str(counts["noindex"]))
           .replace("{{N_FILES}}", str(len(downloads)))
           .replace("{{FILES_SIZE}}", human(dl_size))
           .replace("{{LEGEND}}", legend)
           .replace("{{TREE}}", '<ul class="tree" id="tree">' + render(TREE) + "</ul>")
           .replace("{{SYSTEM}}", system))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(out)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(pages)} pages, {len(downloads)} downloads")


if __name__ == "__main__":
    os.chdir(ROOT)
    main()
