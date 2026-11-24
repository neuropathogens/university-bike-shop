#!/usr/bin/env python3
"""Generate practice-set .tex files from question data.

Each data module in practice/data/ defines
    META     = dict(course=..., unit=..., unitname=..., title=..., keywords=..., abstract=...)
    SECTIONS = [Sec(topic, title, rule, [questions...]), ...]
Questions are built with
    Q(stem, correct, [w1, w2, w3, w4], why)          -> letters assigned by the balancer
    F(stem, [c1, c2, c3, c4, c5], 'B', why)          -> fixed order (e.g. numeric choices)
The balancer spreads correct answers evenly over A-E and avoids three in a row.
"""
import importlib.util, random, sys, pathlib, collections

LET = 'ABCDE'
HERE = pathlib.Path(__file__).resolve().parent


class Sec:
    def __init__(self, topic, title, rule, qs):
        self.topic, self.title, self.rule, self.qs = topic, title, rule, qs


def Q(stem, correct, wrong, why):
    assert len(wrong) == 4, stem[:60]
    return dict(stem=stem, correct=correct, wrong=wrong, why=why, fixed=None)


def F(stem, choices, letter, why):
    assert len(choices) == 5 and letter in LET, stem[:60]
    return dict(stem=stem, choices=choices, letter=letter, why=why, fixed=True)


def assign(questions, seed):
    rng = random.Random(seed)
    n = len(questions)
    fixed = collections.Counter(q['letter'] for q in questions if q['fixed'])
    target = {L: n // 5 + (1 if i < n % 5 else 0) for i, L in enumerate(rng.sample(LET, 5))}
    pool = []
    for L in LET:
        pool += [L] * max(0, target[L] - fixed[L])
    free = [i for i, q in enumerate(questions) if not q['fixed']]
    while len(pool) < len(free):
        pool.append(rng.choice(LET))
    for _ in range(2000):
        rng.shuffle(pool)
        letters = [None] * n
        for i, q in enumerate(questions):
            if q['fixed']:
                letters[i] = q['letter']
        for i, L in zip(free, pool):
            letters[i] = L
        if all(not (letters[i] == letters[i + 1] == letters[i + 2]) for i in range(n - 2)):
            break
    out = []
    for q, L in zip(questions, letters):
        if q['fixed']:
            out.append((q['choices'], L))
            continue
        k = LET.index(L)
        wrong = list(q['wrong'])
        ch = wrong[:k] + [q['correct']] + wrong[k:]
        out.append((ch, L))
    return out


def build(datafile):
    spec = importlib.util.spec_from_file_location('d', datafile)
    mod = importlib.util.module_from_spec(spec)
    mod.Sec, mod.Q, mod.F = Sec, Q, F
    spec.loader.exec_module(mod)
    M, S = mod.META, mod.SECTIONS
    allq = [q for s in S for q in s.qs]
    placed = assign(allq, datafile.stem)
    n = len(allq)
    pace = f"{n} questions $\\times$ 70\\,s $\\approx$ {round(n * 70 / 60)} min"
    L = []
    w = L.append
    w(r"\documentclass{appractice}")
    w(rf"\course{{{M['course']}}}\unit{{{M['unit']}}}\unitname{{{M['unitname']}}}")
    w(rf"\title{{{M['title']}}}")
    w(rf"\keywords{{{M['keywords']}}}")
    w(rf"\numq{{{n}}}\pace{{{pace}}}")
    w(r"\begin{document}")
    w(r"\maketitle")
    w(r"\begin{abstract}")
    w(M['abstract'] + f" The set has {n} original multiple-choice questions with five choices each, matching the exam's format. Questions are grouped by College Board topic, and each group opens with the rule it tests. Write your answer in the blank to the left of each question; the answer key on the last page gives every answer with the reasoning and the rule behind it.")
    w(r"\end{abstract}")
    w(r"\scoreline")
    k = 0
    keyrows = []
    for s in S:
        w(r"\needspace{11\baselineskip}")
        w(rf"\topic{{{s.topic}}}{{{s.title}}}")
        w(r"\begin{rulebox}\textbf{Rule " + s.topic + r".}\enskip " + s.rule + r"\end{rulebox}")
        for q in s.qs:
            ch, Lt = placed[k]
            k += 1
            w(rf"\qitem{{{k}}}{{{q['stem']}}}" + ''.join('{' + c + '}' for c in ch))
            keyrows.append((k, Lt, q['why'], s.topic))
    w(r"\keysection")
    # answers-only strip
    per = 15
    w(r"\noindent\textbf{Answers only.}\par\smallskip")
    for start in range(0, n, per):
        chunk = keyrows[start:start + per]
        w(r"\noindent{\small\begin{tabular}{@{}l" + 'c' * len(chunk) + r"@{}}\toprule")
        w(r"\# & " + ' & '.join(str(r[0]) for r in chunk) + r" \\")
        w(r"Ans. & " + ' & '.join(r'\textbf{' + r[1] + '}' for r in chunk) + r" \\\bottomrule")
        w(r"\end{tabular}}\par\smallskip")
    w(r"\medskip")
    w(r"{\small\setlength{\LTpre}{4pt}\renewcommand\arraystretch{1.2}")
    w(r"\begin{longtable}{@{}r c p{0.73\linewidth} c@{}}")
    w(r"\toprule \# & Ans. & Why & Rule \\ \midrule \endhead")
    w(r"\bottomrule \endlastfoot")
    for num, Lt, why, topic in keyrows:
        w(rf"{num} & \textbf{{{Lt}}} & {why} & {topic} \\")
    w(r"\end{longtable}}")
    w(r"\end{document}")
    out = HERE / (datafile.stem + '.tex')
    txt = '\n'.join(L) + '\n'
    txt = txt.replace("\\'", "'")
    out.write_text(txt)
    cnt = collections.Counter(p[1] for p in placed)
    print(f"{out.name}: {n} questions, letters {dict(sorted(cnt.items()))}")


if __name__ == '__main__':
    files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted((HERE / 'data').glob('*.py'))
    for f in files:
        build(f)
