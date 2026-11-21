# Study quizzes

Interactive quiz pages for the documents on `/study`, written to `public/study/**/tests/<slug>/index.html`
and committed like any other static file. The Next.js build just copies them.

```
cd quizzes && npm ci              # once: KaTeX, used to pre-render math
python3 -I quizzes/build.py sat_conventions      # one family
python3 -I quizzes/build.py --all                # every family
```

`build.py` validates each quiz before writing it, pre-renders `$..$` / `$$..$$` with KaTeX, and updates
`manifest.json` (source PDF -> quiz URL), which drives the Quiz links on `/study`.

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
| `topics` | `{key: (name, guide_page)}`; `topicPrefix`, `topicCol`, `guideCol`, `byTopic`, `topicNote` label them |
| `guide`, `guideName` | PDF the topic links open at `#page=N` |
| `sections` | `{n: name}` shown in each question's eyebrow |
| `stims` | `{id: {title, html}}` shared passages/data, referenced by `q["stim"]` |
| `target` | optional `{label, mc}` score target shown on the results |
| `composite`, `frIntro`, `fr` | optional free response and composite score (see `lib/template.html`) |
| `mc` | list of `{n, prompt, options, answer (index), ex: {idea, steps, others: {index: note}}, sec?, topic?, stim?, fig?, table?, fixed?}` |

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
