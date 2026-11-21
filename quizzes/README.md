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
