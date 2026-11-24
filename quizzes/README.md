# Study quizzes

Interactive quiz pages for the documents on `/study`, written to `public/study/**/tests/<slug>/index.html`
and committed like any other static file. The Next.js build just copies them.

```
cd quizzes && npm ci              # once: KaTeX, used to pre-render math
python3 -I quizzes/build.py sat_conventions      # one family
python3 -I quizzes/build.py --all                # every family
```

`build.py` validates each quiz before writing it, pre-renders `$..$` / `$$..$$` with KaTeX, and updates
`manifest.json` (source PDF -> quiz URL), which drives the Quiz links on `/study`. After building, run
`python3 -I quizzes/link_study.py` (adds the Quiz links to `public/study/index.html`; idempotent) and
`python3 -I scripts/build_directory.py` (the site directory page).

## Layout

- `lib/template.html` — the quiz app (practice/exam modes, shuffling, per-topic tally linked to the guide PDF,
  review with explanations, optional free response with E/P/I or points scoring and a composite score).
- `lib/latex.py` — converts the LaTeX text in the study sources to HTML (unknown macros raise).
- `<family>/quiz.py` — defines `QUIZZES`, a list of quiz dicts. Explanations live next to it.

## Quiz dict

| key | |
|---|---|
| `url`, `out` | `/study/.../tests/<slug>/` and `public` + url + `index.html` |
| `pdf` | source PDF (linked in the header; manifest key) |
| `key` | localStorage key (unique per quiz) |
| `title`, `desc`, `runhead`, `h1`, `sub`, `metaline`, `foot`, `setupNote` | page text (HTML) |
| `back` | `(href, label)` for the header link back to `/study` |
| `ask` | optional question shown under every prompt (e.g. the SAT Conventions stem) |
| `topics` | `{key: (name, guide_page[, url])}` (a url overrides `guide#page=N`); `topicPrefix`, `topicCol`, `guideCol`, `byTopic`, `topicNote` label them |
| `guide`, `guideName` | PDF the topic links open at `#page=N` |
| `sections` | `{n: name}` shown in each question's eyebrow |
| `stims` | `{id: {title, html}}` shared passages/data, referenced by `q["stim"]` |
| `target` | optional `{label, mc}` score target shown on the results |
| `flag` | optional `{below, text}`: topics scored under `below` percent get `text` in the tally |
| `composite`, `frIntro`, `fr`, `frWord` | optional free response and composite score (see `lib/template.html`); `frWord` replaces "Question" in FR headings. With `mc` empty the page shows only the free response, with a running points total |
| `manifest` | `False` keeps the quiz out of `manifest.json` (when several quizzes share one PDF) |
| `mc` | list of `{n, prompt, options, answer (index), ex: {idea, steps, others: {index: note}}, sec?, topic?, tag?, stim?, fig?, table?, fixed?, labels?, after?}` |

Item extras: `tag` is the key's rule name shown with the explanation; `labels` gives display names for image
choices (they are not quoted); `after` is HTML (a figure or photo) revealed with the explanation. A stim's
`cls: "free"` lets a long passage run at full height; markers with `data-q`/`data-qs` in a passage are
highlighted while the questions they belong to are shown.

Every wrong choice must have a note in `ex.others`; the builder refuses a quiz otherwise.

## Families

- `sat_conventions` — SAT Standard English Conventions Practice Sets 1–10. Items come from the series' own
  source (`source/`, from `sat-conventions-latex-source.tar.gz`); `arrange()` reproduces each PDF's item
  order and answer letters exactly. Explanations: `ex_setNN.py`.
- `sat_vocab` — SAT Vocabulary: Part 0 diagnostic, Practice Sets 1–10, and the definition self-checks of
  Parts 1–3. Items come from the series' own source (`source/`, from `sat-vocab-source.zip`); the copied
  `assign_positions`/`defcheck` reproduce each PDF's choices and letters exactly. Practice-set explanations:
  `ex_setNN.py`; self-check explanations are generated from the lexicon (each wrong choice is named as
  another word's definition).
- `ap_psych` — AP Psychology: each unit's Question Set (MC, shared data displays, and the 7-point EBQ, or the
  AAQ for Research Methods, self-scored in points) and each guide's section checks. Parsed from the
  series' LaTeX (`source/`, from `ap-psych-study-series.zip`); choices are in source order, as in the PDFs.
  Explanations: `ex_<file>.py`. `STIM_COUNTS` says how many items follow each data display.
- `ap_chem` — AP Chemistry Unit 5 Practice Sets A and B (`tests/5a`, `tests/5b`): transcribed from the PDFs
  into TeX with mhchem (`\ce{}`); `checks.py` asserts every computed answer and every computed distractor.
  Long reaction equations are shown as display math so they never overflow a phone. The two energy-profile
  figures are crops of the PDF pages (`public/study/ap/ap-chemistry/tests/fig/`), rendered with
  `sips --resampleWidth 1800` from single pages split out with pypdf.
- `ap_stats` — AP Statistics Unit 6 Practice Sets B and C (`tests/6b`, `tests/6c`), moved here from their
  original one-off builder: `q_6x.py` (transcribed set), `ex_6x.py` (explanations), `checks_6x.py` (numeric
  asserts). E/P/I free response and the 50/50 composite score with each set's bands. `fkey` keeps the
  original localStorage keys.
- `act_math` — ACT Math Guides 0–7 and the practice test, transcribed from the PDFs (`gNN.py`: DOC + QS with
  in-depth explanations; computed answers asserted). Topics are the guides' rules, linked to their pages; the
  practice test tallies by guide and flags guides under 70%.
- `act_english` — ACT English Parts 1–4 from the series' source (`source/`). Each passage is one shared stim;
  the item's boxed number and underline are highlighted. Choices are numbered 1–4 in source order (NO CHANGE
  first); the PDFs' alternating A–D/F–J letters are checked against the key.
  Explanations: `ex_<part>.py`.
- `act_reading` — ACT Reading Volumes 1–2 (drills, practice section) from the LaTeX source; cited line numbers
  become boxed markers (`source/lines.json`), highlighted with their question. Figure 1 is an SVG chart.
- `act_science` — ACT Science Parts 1–6 from the LaTeX source; siunitx written out, tables as HTML, pgfplots
  figures as 3x PDFKit crops (`tests/fig/`), graph choices as labelled images. Explanations: `ex_partN.py`.
- `apah_vocab` — APAH Vocabulary, 754 items in 8 category quizzes (`vocab-1`..`8`), extracted from the PDF
  (`extract.py` -> `source/vocab.json`); explanations come from the glossary entries. Masking typos in the PDF's
  prompts are repaired without revealing the answer.
- `apah_works` — APAH 250 every-work practice, 500 items in 10 content-area quizzes (`works-1`..`10`), extracted
  from the PDF; the work's photo is shown after answering. Wrong-choice notes: `notes_<k>.py`.
- `college_math` — Differential Equations I–III, Linear Algebra, Multivariable Calculus and Real Analysis I–III
  (`/study/math/<subject>/tests/<slug>/`), transcribed from the PDFs: one module per volume (`de1.py` … `ra3.py`)
  with `Q()` items and `FRQ()` free-response items. Real Analysis II and III are proof problem sets (free
  response only, scored 5/10/15 with a proof rubric; III shows each section's "Tool -> use" box).
- `ap_physics_c` — AP Physics C: Mechanics (Units 1–7) and E&M (Units 8–13). Unlike the other families, the content
  lives here and the PDFs are generated from it: one module per unit (`u01.py` … `u13.py`, schema in `model.py`)
  holds the guide's sections and checks, the question set and its free-response question. `texgen.py` writes
  `latex/*.tex` (style `latex/ap-physc.sty`), compiles them with XeLaTeX, copies the PDFs, packs and source zip
  to `public/study/ap/ap-physics-c/`, and records guide section pages in `pages.json`; `quiz.py` builds
  `tests/unit-N/` and `tests/unit-N-checks/` from the same objects, so letters and keys always match the PDFs.
  `study_rows.py` rewrites the two Physics C sections of `/study`; `checks.py` recomputes every numeric answer.
  Edit a unit, then: `texgen.py` → `checks.py` → `study_rows.py` → `build.py ap_physics_c` → `link_study.py`.
