"""Build the AP Chemistry unit PDFs (every unit except Unit 5, which has no source here).

    python3 -I quizzes/ap_chem/build_pdfs.py            # all units
    python3 -I quizzes/ap_chem/build_pdfs.py 1 3        # some units

For each unit N: writes tex/build/ap-chem-unit-N-{2,3}-practice-set-{a,b}.tex from uN.py, compiles them and
tex/ap-chem-unit-N-1-content-guide.tex with latexmk (pdfLaTeX), copies the PDFs to
public/study/ap/ap-chemistry/unit-N/, and records each guide section's page in guide_pages.json (used by the
quizzes' topic links). Then build the quizzes:  python3 -I quizzes/build.py ap_chem
"""
import importlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import chemgen  # noqa: E402

REPO = HERE.parent.parent
PUB = REPO / "public/study/ap/ap-chemistry"
UNITS = [1, 2, 3, 4, 6, 7, 8, 9]


def latexmk(tex):
    r = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
                        f"-output-directory={chemgen.BUILD}", str(tex)],
                       cwd=str(chemgen.TEX), capture_output=True, text=True, errors="replace", env={**__import__("os").environ,
                                                                                 "TEXINPUTS": f"{chemgen.TEX}:"})
    if r.returncode:
        log = (chemgen.BUILD / (tex.stem + ".log"))
        tail = log.read_text(errors="replace")[-3000:] if log.exists() else r.stdout[-3000:]
        raise SystemExit(f"LaTeX failed on {tex.name}:\n{tail}")
    return chemgen.BUILD / (tex.stem + ".pdf")


def build_unit(n):
    mod = importlib.import_module(f"u{n}")
    U, sets = chemgen.load_unit(mod)
    chemgen.BUILD.mkdir(parents=True, exist_ok=True)
    out = PUB / f"unit-{n}"
    out.mkdir(parents=True, exist_ok=True)
    pdfs = []
    guide = chemgen.TEX / f"ap-chem-unit-{n}-1-content-guide.tex"
    pdfs.append(latexmk(guide))
    pages = chemgen.pages_from_aux(chemgen.BUILD / (guide.stem + ".aux"))
    missing = set(U["topics"]) - set(pages)
    if missing:
        raise SystemExit(f"unit {n}: guide has no \\label{{t:...}} for {sorted(missing)}")
    for letter, k in (("A", 2), ("B", 3)):
        secs, mcs, stims, frs = sets[letter]
        tex = chemgen.BUILD / f"ap-chem-unit-{n}-{k}-practice-set-{letter.lower()}.tex"
        tex.write_text(chemgen.set_tex(U, letter, mcs, secs, frs))
        pdfs.append(latexmk(tex))
    for p in pdfs:
        shutil.copy2(p, out / p.name)
        npages = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout
        npages = [ln.split()[-1] for ln in npages.splitlines() if ln.startswith("Pages:")][0]
        print(f"  {p.name:<48} {npages:>3} pp {p.stat().st_size / 1024:>5.0f} KB")
    return {t: pages[t] for t in U["topics"]}


def package():
    """All nine content guides in one bookmarked PDF, and a zip of the LaTeX and Python source."""
    import zipfile
    from pypdf import PdfReader, PdfWriter
    w = PdfWriter()
    for n in range(1, 10):
        f = PUB / f"unit-{n}" / f"ap-chem-unit-{n}-1-content-guide.pdf"
        start = len(w.pages)
        for page in PdfReader(f).pages:
            w.add_page(page)
        w.add_outline_item(f"Unit {n} Content Guide", start)
    w.add_metadata({"/Title": "AP Chemistry Content Guides, Units 1-9", "/Author": "Paul Wang"})
    out = PUB / "ap-chem-all-content-guides.pdf"
    with open(out, "wb") as fh:
        w.write(fh)
    z = PUB / "ap-chem-latex-source.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(chemgen.TEX.glob("*.tex")) + [chemgen.TEX / "apchem.sty"]:
            zf.write(f, f"ap-chem-source/tex/{f.name}")
        for f in sorted(chemgen.BUILD.glob("ap-chem-unit-*-practice-set-*.tex")):
            zf.write(f, f"ap-chem-source/tex/{f.name}")
        for f in [HERE / "chemgen.py", HERE / "build_pdfs.py"] + sorted(HERE.glob("u[0-9].py")):
            zf.write(f, f"ap-chem-source/python/{f.name}")
    for f in (out, z):
        print(f"  {f.name:<48} {f.stat().st_size / 1024:>5.0f} KB")


def main(args):
    units = [int(a) for a in args] or UNITS
    path = HERE / "guide_pages.json"
    allp = json.loads(path.read_text()) if path.exists() else {}
    for n in units:
        print(f"unit {n}")
        allp[str(n)] = build_unit(n)
    path.write_text(json.dumps(allp, indent=1, sort_keys=True) + "\n")
    if not args:
        package()


if __name__ == "__main__":
    main(sys.argv[1:])
