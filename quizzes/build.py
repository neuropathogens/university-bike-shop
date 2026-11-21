"""Build the interactive quiz pages under public/study.

    cd quizzes && npm ci            # once: KaTeX for math pre-rendering
    python3 -I quizzes/build.py sat_conventions [more families...]
    python3 -I quizzes/build.py --all

Each family is a package quizzes/<family>/ whose quiz.py defines QUIZZES, a list of quiz dicts (schema in
README.md). Text is HTML; $..$ / $$..$$ is TeX, pre-rendered here with KaTeX. Every quiz is validated
before anything is written. quizzes/manifest.json maps each source PDF to its quiz URL (used to add the
Quiz links on /study).
"""
import html
import importlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
LIB = HERE / "lib"
sys.path.insert(0, str(HERE))

REQUIRED = ("out", "url", "key", "title", "desc", "runhead", "h1", "sub", "metaline", "back", "foot", "setupNote", "mc")


def fail(quiz, msg):
    raise SystemExit(f"[{quiz.get('url', '?')}] {msg}")


def validate(z):
    for k in REQUIRED:
        if k not in z:
            fail(z, f"missing {k}")
    if not z["url"].startswith("/study/") or not z["url"].endswith("/"):
        fail(z, "url must be /study/.../")
    if z["out"] != "public" + z["url"] + "index.html":
        fail(z, "out must match url")
    topics, sections = z.get("topics", {}), z.get("sections", {})
    seen = set()
    for q in z["mc"]:
        n = q["n"]
        if n in seen:
            fail(z, f"duplicate question {n}")
        seen.add(n)
        opts = q["options"]
        if not 2 <= len(opts) <= 6 or len(set(opts)) != len(opts):
            fail(z, f"Q{n}: options must be 2-6 and distinct: {opts}")
        if not (isinstance(q["answer"], int) and 0 <= q["answer"] < len(opts)):
            fail(z, f"Q{n}: bad answer index")
        ex = q.get("ex")
        if not ex or not ex.get("idea"):
            fail(z, f"Q{n}: missing explanation")
        others = ex["others"]
        if set(others) != set(range(len(opts))) - {q["answer"]}:
            fail(z, f"Q{n}: explanation must cover exactly the wrong choices, got {sorted(others)}")
        if any(not str(v).strip() for v in others.values()):
            fail(z, f"Q{n}: empty wrong-choice note")
        if q.get("topic") and q["topic"] not in topics:
            fail(z, f"Q{n}: unknown topic {q['topic']}")
        if q.get("sec") and q["sec"] not in sections:
            fail(z, f"Q{n}: unknown section {q['sec']}")
        if q.get("stim") and q["stim"] not in z.get("stims", {}):
            fail(z, f"Q{n}: unknown stimulus {q['stim']}")
    for f in z.get("fr", []):
        if f.get("mode", "epi") not in ("epi", "points"):
            fail(z, f"FR {f['n']}: bad mode")
        for p in f["parts"]:
            if f.get("mode") == "points" and not (isinstance(p.get("max"), int) and p["max"] >= 1):
                fail(z, f"FR {f['n']}{p['label']}: points part needs max")


class Tex:
    """Collect $..$ / $$..$$ for one batched KaTeX call."""

    def __init__(self):
        self.items = []

    def rich(self, s):
        if not isinstance(s, str):
            return s

        def sub(m, display):
            self.items.append([m.group(1).strip(), display])
            return f"\x00{len(self.items) - 1}\x00"
        s = re.sub(r"\$\$(.+?)\$\$", lambda m: sub(m, True), s, flags=re.S)
        s = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", lambda m: sub(m, False), s)
        if "$" in s.replace("\\$", ""):
            raise SystemExit(f"unbalanced $ in {s[:100]!r}")
        return s.replace("\\$", "$")

    def render(self):
        if not self.items:
            return []
        r = subprocess.run(["node", str(LIB / "render_tex.cjs")], input=json.dumps(self.items), capture_output=True,
                           text=True, cwd=str(HERE))
        if r.returncode:
            raise SystemExit("KaTeX failed:\n" + r.stderr[-2000:])
        return json.loads(r.stdout)


def walk(o, fn):
    if isinstance(o, str):
        return fn(o)
    if isinstance(o, list):
        return [walk(x, fn) for x in o]
    if isinstance(o, tuple):
        return tuple(walk(x, fn) for x in o)
    if isinstance(o, dict):
        return {k: walk(v, fn) for k, v in o.items()}
    return o


def page_data(z):
    meta_keys = ("key", "ask", "setupNote", "topicPrefix", "topicCol", "guideCol", "byTopic", "topicNote", "guide",
                 "guideName", "target", "composite", "frIntro")
    data = {
        "meta": {k: z[k] for k in meta_keys if k in z},
        "topics": {t: {"name": v[0], "page": v[1]} for t, v in z.get("topics", {}).items()},
        "sections": {str(k): v for k, v in z.get("sections", {}).items()},
        "stims": z.get("stims", {}),
        "mc": [],
        "fr": z.get("fr", []),
    }
    for q in z["mc"]:
        d = {k: q[k] for k in ("n", "prompt", "options", "answer") }
        for k in ("sec", "topic", "fixed", "table", "fig", "ask", "stim"):
            if q.get(k):
                d[k] = str(q[k]) if k == "sec" else q[k]
        d["ex"] = {"idea": q["ex"]["idea"], "steps": list(q["ex"].get("steps", [])),
                   "others": {str(i): v for i, v in q["ex"]["others"].items()}}
        data["mc"].append(d)
    return data


def build_quiz(z, tpl):
    validate(z)
    tex = Tex()
    data = walk(page_data(z), tex.rich)
    head = {k: tex.rich(z[k]) for k in ("h1", "sub", "metaline", "foot")}
    math = tex.render()

    def fill(s):
        return re.sub(r"\x00(\d+)\x00", lambda m: math[int(m.group(1))], s)
    data = walk(data, fill)
    head = {k: fill(v) for k, v in head.items()}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    has_fr = bool(z.get("fr"))
    tabs = ('  <div class="tabs" role="tablist">\n'
            '    <button type="button" class="tab" role="tab" id="tab-mc" aria-controls="mc" aria-selected="true">Multiple choice</button>\n'
            '    <button type="button" class="tab" role="tab" id="tab-fr" aria-controls="fr" aria-selected="false">Free response</button>\n'
            '  </div>\n') if has_fr else ""
    pdf = z.get("pdf")
    rep = {
        "{{TITLE}}": html.escape(z["title"]), "{{DESC}}": html.escape(z["desc"], quote=True),
        "{{KATEX_CSS}}": '<link rel="stylesheet" href="/study/katex/katex.min.css">' if math else "",
        "{{RUNHEAD}}": z["runhead"], "{{BACK_HREF}}": z["back"][0], "{{BACK_LABEL}}": z["back"][1],
        "{{PDF_LINK}}": f'<a href="{pdf}">PDF version</a>' if pdf else "",
        "{{H1}}": head["h1"], "{{SUB}}": head["sub"], "{{METALINE}}": head["metaline"], "{{FOOT}}": head["foot"],
        "{{TABS}}": tabs, "{{MC_ROLE}}": ' role="tabpanel" aria-labelledby="tab-mc"' if has_fr else "",
    }
    page = tpl
    for k, v in rep.items():
        page = page.replace(k, v)
    page = page.replace("{{DATA}}", blob)
    if "{{" in page.replace(blob, ""):
        fail(z, "unfilled placeholder")
    out = REPO / z["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return out, len(page), len(math)


def main(args):
    families = sorted(p.name for p in HERE.iterdir() if (p / "quiz.py").exists()) if args == ["--all"] else args
    if not families:
        raise SystemExit(__doc__)
    tpl = (LIB / "template.html").read_text()
    mpath = HERE / "manifest.json"
    manifest = json.loads(mpath.read_text()) if mpath.exists() else {}
    for fam in families:
        mod = importlib.import_module(f"{fam}.quiz")
        urls = set()
        for z in mod.QUIZZES:
            if z["url"] in urls:
                fail(z, "duplicate url")
            urls.add(z["url"])
            out, size, nmath = build_quiz(z, tpl)
            print(f"  {z['url']:<52} {len(z['mc']):>3} MC {len(z.get('fr', [])):>2} FR {size / 1024:>5.0f} KB {nmath:>4} math")
            if z.get("pdf"):
                manifest[z["pdf"]] = z["url"]
        print(f"{fam}: {len(mod.QUIZZES)} quizzes")
    mpath.write_text(json.dumps(dict(sorted(manifest.items())), indent=1) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
