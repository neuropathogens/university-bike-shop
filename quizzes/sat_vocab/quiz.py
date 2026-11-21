"""SAT Vocabulary series -> /study/sat/vocabulary/tests/<slug>/.

  diagnostic   Part 0's eight-item diagnostic
  lexicon-1..3 the 20-item definition self-checks at the end of Parts 1-3
  1..10        Practice Sets 1-10

Items come from the series' own source (source/, copied from sat-vocab-source.zip). load_defs, load_sets,
assign_positions and defcheck are copied from its build.py, so item order, choice order and answer letters
match the PDFs exactly (checked against every PDF's key when these quizzes were made).
Practice-set and diagnostic explanations are hand-written in ex_setNN.py; the definition self-check
explanations are generated from the lexicon (each wrong choice is identified as another word's definition).
"""
import glob
import html
import importlib
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "source")
LETTERS = "ABCD"
TAGS = {
    "C": ("WIC-C", "Words in Context: completion"),
    "M": ("WIC-M", "Words in Context: meaning as used"),
    "T": ("WIC-T", "Words in Context: tone and connotation"),
    "X": ("TRN", "Transitions"),
}
DEFAULT_STEM = {
    "C": "Which choice completes the text with the most logical and precise word or phrase?",
    "T": "Which choice completes the text with the most logical and precise word or phrase?",
    "X": "Which choice completes the text with the most logical transition?",
}
BASE = "/study/sat/vocabulary/"
PART0 = BASE + "sat-vocab-00-overview-and-method.pdf"
# physical pages of Part 0's sections for each item type
TAG_PAGE = {"WIC-C": 2, "WIC-M": 3, "WIC-T": 3, "TRN": 6}
LEXICONS = {
    1: ("sat-vocab-01-lexicon-1-top-frequency.pdf", "Lexicon I: Top-Frequency Words", "top"),
    2: ("sat-vocab-02-lexicon-2-mid-frequency.pdf", "Lexicon II: Mid-Frequency Words", "mid"),
    3: ("sat-vocab-03-lexicon-3-low-frequency.pdf", "Lexicon III: Low-Frequency Words", "low"),
}
# physical page of each lesson (Parts 1-2) or letter (Part 3) in the lexicon PDFs
LEX_PAGE = {
    1: {"1.1": 1, "1.2": 2, "1.3": 3, "1.4": 4, "1.5": 4, "1.6": 5, "1.7": 6, "1.8": 7, "1.9": 7, "1.10": 8, "1.11": 9,
        "1.12": 10, "1.13": 10, "1.14": 11, "1.15": 12},
    2: {"2.1": 1, "2.2": 2, "2.3": 3, "2.4": 3, "2.5": 4, "2.6": 4, "2.7": 5, "2.8": 5, "2.9": 6, "2.10": 6, "2.11": 6,
        "2.12": 7, "2.13": 7, "2.14": 8, "2.15": 8, "2.16": 9, "2.17": 9, "2.18": 10, "2.19": 10, "2.20": 11, "2.21": 11,
        "2.22": 12, "2.23": 12, "2.24": 13, "2.25": 13, "2.26": 14, "2.27": 14, "2.28": 14, "2.29": 15, "2.30": 15,
        "2.31": 16, "2.32": 16, "2.33": 17, "2.34": 17, "2.35": 18, "2.36": 18, "2.37": 19, "2.38": 19, "2.39": 19,
        "2.40": 20, "2.41": 20, "2.42": 21, "2.43": 21, "2.44": 22, "2.45": 22},
    3: {"A": 2, "B": 4, "C": 5, "D": 7, "E": 9, "F": 10, "G": 11, "H": 12, "I": 13, "J": 15, "K": 15, "L": 15, "M": 16,
        "N": 17, "O": 18, "P": 18, "Q": 20, "R": 21, "S": 22, "T": 24, "U": 25, "V": 26, "W": 26, "Y": 27, "Z": 27},
}
SET_SOURCES = {1: "Lessons 1.1–1.5", 2: "Lessons 1.6–1.10", 3: "Lessons 1.11–1.15", 4: "Lessons 2.1–2.15",
               5: "Lessons 2.16–2.30", 6: "Lessons 2.31–2.45", 7: "Part 3, A–F", 8: "Part 3, G–P",
               9: "Part 3, Q–Z, plus phrases", 10: "all parts"}
BLANK = '<span class="blank" role="img" aria-label="blank"></span>'


# ------------------------------------------------------------------ copied from the series' build.py
def load_defs():
    lessons, allw = {}, {}
    for f in sorted(glob.glob(os.path.join(SRC, "defs_*.txt"))):
        key = os.path.basename(f)[5:-4]
        cur = None
        groups = []
        for line in open(f, encoding="utf8"):
            line = line.rstrip("\n")
            if not line:
                continue
            if line.startswith("## "):
                cur = (line[3:].strip(), [])
                groups.append(cur)
                continue
            p = line.split("|")
            e = dict(word=p[0], pos=p[1], d=p[2], syn=p[3] if len(p) > 3 else "")
            if cur is None:
                cur = ("", [])
                groups.append(cur)
            cur[1].append(e)
            allw[p[0].lower()] = e
        lessons[key] = groups
    return lessons, allw


def load_sets():
    sets = []
    for f in sorted(glob.glob(os.path.join(SRC, "sets_*.txt"))):
        cur = q = None
        for raw in open(f, encoding="utf8"):
            line = raw.rstrip("\n")
            if line.startswith("=== "):
                n, title, abstract = line[4:].split("|")
                cur = dict(n=int(n), title=title, abstract=abstract, items=[])
                sets.append(cur)
                continue
            if line.startswith("@ "):
                q = dict(tag=line[2:].strip(), text=[], stem=None, right=None, wrong=[], why="")
                cur["items"].append(q)
                continue
            if q is None:
                continue
            if line.startswith("? "):
                q["stem"] = line[2:]
            elif line.startswith("* "):
                q["right"] = line[2:]
            elif line.startswith("- "):
                q["wrong"].append(line[2:])
            elif line.startswith("> "):
                q["why"] = line[2:]
            elif line.strip():
                q["text"].append(line)
    return sorted(sets, key=lambda s: s["n"])


def assign_positions(items, seed):
    rng = random.Random(seed)
    n = len(items)
    for _ in range(10000):
        pos = [i % 4 for i in range(n)]
        rng.shuffle(pos)
        if all(not (pos[i] == pos[i - 1] == pos[i - 2]) for i in range(2, n)):
            break
    for q, p in zip(items, pos):
        opts = q["wrong"][:]
        rng.shuffle(opts)
        opts.insert(p, q["right"])
        q["opts"] = opts
        q["ans"] = LETTERS[p]


def defcheck(entries, n, seed):
    rng = random.Random(seed)
    pick = rng.sample(entries, n)
    items = []
    for e in pick:
        same = [x for x in entries if x is not e and x["pos"].split("/")[0] == e["pos"].split("/")[0] and x["d"] != e["d"]]
        if len(same) < 3:
            same = [x for x in entries if x is not e and x["d"] != e["d"]]
        wrong = [rng.sample(same, 3)]
        items.append(dict(tag="D", entry=e, wrong_entries=wrong[0], right=e["d"], wrong=[x["d"] for x in wrong[0]]))
    return items


# ------------------------------------------------------------------ text
def text_html(s):
    """Plain source text -> HTML with curly quotes and the blank."""
    s = html.escape(s, quote=False)
    s = re.sub(r'(^|[\s(\[—–/])"', "\\1“", s).replace('"', "”")
    s = re.sub(r"(\w)'", "\\1’", s).replace("'", "‘")
    s = re.sub(r"_{4,}", "\x02", s)
    return s.replace("\x02", BLANK)


def bold_target(text, stem):
    m = re.search(r"“([^”]+)”", stem)
    if not m:
        return text
    w = re.escape(m.group(1))
    return re.sub(r"(?<![\w-])(" + w + r")(?![\w-])", r"<b>\1</b>", text, count=1, flags=re.I)


def match(key, opts):
    if key in opts:
        return key
    hits = [o for o in opts if o.startswith(key)]
    if len(hits) != 1:
        raise SystemExit(f"explanation key {key!r} matches {len(hits)} of {opts}")
    return hits[0]


# ------------------------------------------------------------------ quizzes
def common(url, pdf, key, title, h1, sub, metaline, setup_note, foot_doc, foot_extra):
    return dict(
        out="public" + url + "index.html", url=url, pdf=pdf, key=key, title=title,
        runhead="SAT Reading and Writing &middot; Vocabulary &middot; " + title.replace("SAT Vocabulary ", ""),
        back=("/study/#sat-vocabulary", "Study Library"), h1=h1, sub=sub, metaline=metaline, setupNote=setup_note,
        foot=(f'From <a href="{pdf}"><i>{foot_doc}</i></a> (PDF). {foot_extra} Your answers are saved only in this browser.'),
    )


def wic_quiz(s, slug):
    n = s["n"]
    items = s["items"]
    if n == 0:
        assign_positions(items, 1000)
        ordered = items
    else:
        assign_positions(items, 500 + n)
        ordered = [q for t in "CMTX" for q in items if q["tag"] == t]
    ex = importlib.import_module(f"sat_vocab.ex_set{n:02d}").EX
    assert len(ex) == len(items), (n, len(ex), len(items))
    exmap = {id(q): e for q, e in zip(items, ex)}
    sec_of = {t: k for k, t in enumerate([t for t in "CMTX" if any(q["tag"] == t for q in items)], 1)}
    mc = []
    for k, q in enumerate(ordered, 1):
        e = exmap[id(q)]
        if q["right"] != e["ans"]:
            raise SystemExit(f"Set {n}: explanation for {e['ans']!r} is aligned with item whose answer is {q['right']!r}")
        wrong = [o for o in q["opts"] if o != q["right"]]
        mapped = {match(key, wrong): note for key, note in e["others"].items()}
        if set(mapped) != set(wrong):
            raise SystemExit(f"Set {n} item {q['right']!r}: missing notes for {set(wrong) - set(mapped)}")
        stem = q["stem"] or DEFAULT_STEM[q["tag"]]
        prompt = text_html(" ".join(q["text"]))
        if q["tag"] == "M":
            prompt = bold_target(prompt, text_html(stem))
        mc.append(dict(n=k, sec=None if n == 0 else sec_of[q["tag"]], topic=TAGS[q["tag"]][0], prompt=prompt,
                       ask=text_html(stem), options=[text_html(o) for o in q["opts"]], answer=LETTERS.index(q["ans"]),
                       ex=dict(idea=e["idea"], steps=e["steps"],
                               others={q["opts"].index(w): note for w, note in mapped.items()})))
    topics = {code: (name, TAG_PAGE[code]) for code, name in TAGS.values()}
    if n == 0:
        url, pdf = BASE + "tests/diagnostic/", PART0
        base = common(url, pdf, "study.sat-vocab.diagnostic.v1", "SAT Vocabulary Diagnostic", "Vocabulary Diagnostic",
                      "Digital SAT &middot; Vocabulary &middot; Part 0", "8 items (10 min) &middot; one per trap type",
                      "Allow 10 minutes. Each item is built on one of the eight trap types in Part 0, Section 5.",
                      "SAT Vocabulary, Part 0: How the Test Works, Method and Word Roots",
                      "Answers are the diagnostic&rsquo;s own key; the explanations expand on it with the clue, the meaning of each choice, and why the wrong ones fail.")
        base.update(desc="Digital SAT vocabulary diagnostic: eight Words in Context and transition items, one per trap type, with full explanations.")
    else:
        url, pdf = BASE + f"tests/{n}/", BASE + f"sat-vocab-{3 + n:02d}-practice-set-{n}.pdf"
        base = common(url, pdf, f"study.sat-vocab.{n}.v1", f"SAT Vocabulary Practice Set {n}",
                      f'Vocabulary Practice <span style="white-space:nowrap">Set {n}</span>',
                      text_html(s["title"]), f"20 items (24 min) &middot; words mainly from {SET_SOURCES[n]}",
                      "Allow 24 minutes, about 71 seconds per question. Use Part 0&rsquo;s six steps: cover the choices, find the clue, predict, fix the charge, eliminate by trap type, reread.",
                      f"SAT Vocabulary, Practice Set {n}: {text_html(s['title'])}",
                      "Answers are the set&rsquo;s own key; the explanations expand on it with the clue, the meaning of each choice, and why the wrong ones fail. Type links open the matching section of Part 0.")
        base.update(desc=f"Digital SAT vocabulary Practice Set {n} ({s['title']}): 20 Words in Context and transition items with the clue, each word's meaning, and why every wrong choice fails.",
                    bands=[[18, "18 or more: mastery."], [15, "15&ndash;17: review the words you missed."],
                           [0, f"14 or fewer: relearn {SET_SOURCES[n]} before retaking."]])
    base.update(mc=mc, topics=topics, sections={} if n == 0 else {k: TAGS[t][1] for t, k in sec_of.items()},
                topicPrefix="", topicCol="Type", guideCol="Part 0 section", byTopic="By item type",
                topicNote="Two or more misses of one type: reread that section of Part 0.",
                guide=PART0, guideName="<i>Part 0: How the Test Works</i>")
    return base


def lexicon_quiz(part, lex):
    pdf_name, title, kind = LEXICONS[part]
    if part == 1:
        groups = lex["top"]
        entries = [e for _, es in groups for e in es]
        seed = 11
    elif part == 2:
        groups = lex["mid1"] + lex["mid2"]
        entries = [e for _, es in groups for e in es]
        seed = 22
    else:
        entries = [e for g in ("low1", "low2", "low3", "low4") for _, es in lex[g] for e in es]
        entries.sort(key=lambda e: e["word"].lower())
        groups = None
        seed = 33
    lesson_of = ({e["word"]: l for l, es in groups for e in es} if groups else
                 {e["word"]: e["word"][0].upper() for e in entries})
    items = defcheck(entries, 20, seed)
    assign_positions(items, seed + 1)
    pdf = BASE + pdf_name
    mc = []
    for k, q in enumerate(items, 1):
        e = q["entry"]
        by_def = {x["d"]: x for x in q["wrong_entries"]}
        les = lesson_of[e["word"]]
        syn = f" Synonyms: {text_html(e['syn'])}." if e["syn"] else ""
        idea = f"<b>{text_html(e['word'])}</b> (<i>{text_html(e['pos'])}</i>): {text_html(e['d'])}.{syn}"
        where = f"Lesson {les}" if part < 3 else f"the {les} words"
        steps = [f"Each wrong choice is the real definition of another word in this part, so the only way to be sure is to know <i>{text_html(e['word'])}</i>. It is in {where}."]
        others = {}
        for i, o in enumerate(q["opts"]):
            if o == q["right"]:
                continue
            w = by_def[o]
            wsyn = f" (synonyms: {text_html(w['syn'])})" if w["syn"] else ""
            others[i] = f"is the definition of <i>{text_html(w['word'])}</i> ({text_html(w['pos'])}){wsyn}, not of <i>{text_html(e['word'])}</i>."
        mc.append(dict(n=k, topic=les, prompt=f"Which choice best defines “{text_html(e['word'])}” ({text_html(e['pos'])})?",
                       options=[text_html(o) for o in q["opts"]], answer=LETTERS.index(q["ans"]),
                       ex=dict(idea=idea, steps=steps, others=others)))
    url = BASE + f"tests/lexicon-{part}/"
    used = sorted({m["topic"] for m in mc}, key=lambda t: [int(x) for x in t.split(".")] if part < 3 else [ord(t)])
    base = common(url, pdf, f"study.sat-vocab.lexicon-{part}.v1", f"SAT Vocabulary {title} Self-Check",
                  f'{title.split(":")[0]} <span style="white-space:nowrap">Self-Check</span>', text_html(title.split(": ")[1]) + " &middot; Part " + str(part),
                  "20 definition items &middot; drawn at random from this part",
                  "Choose the definition of each word. The wrong choices are definitions of other words in the same part.",
                  f"SAT Vocabulary, Part {part}: {title}",
                  "Answers are the part&rsquo;s own key; each explanation gives the word&rsquo;s definition and names the words the other three choices define. "
                  + ("Lesson" if part < 3 else "Letter") + " links open that page of the lexicon.")
    base.update(desc=f"SAT vocabulary {title}: the part's 20-item definition self-check, with each word's definition and the words the wrong choices define.",
                mc=mc, topics={t: (f"page {LEX_PAGE[part][t]}", LEX_PAGE[part][t]) for t in used},
                topicPrefix="Lesson " if part < 3 else "Letter ", topicCol="Lesson" if part < 3 else "Letter", guideCol="Lexicon page",
                byTopic="By lesson" if part < 3 else "By letter", guide=pdf, guideName=f"<i>Part {part}</i>",
                topicNote="Reread the entries for the words you missed.")
    return base


def build():
    lex, _ = load_defs()
    sets = load_sets()
    quizzes = []
    for s in sets:
        try:
            importlib.import_module(f"sat_vocab.ex_set{s['n']:02d}")
        except ModuleNotFoundError:
            continue  # explanations not written yet
        quizzes.append(wic_quiz(s, s["n"]))
    quizzes += [lexicon_quiz(p, lex) for p in (1, 2, 3)]
    return quizzes


QUIZZES = build()
