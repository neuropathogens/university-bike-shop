"""Unit 1 Practice Set: Limits and Continuity (12 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, Table, fig

x = sp.symbols("x")

DOC = dict(
    unit=1, title="Limits and Continuity", topics="1.1–1.16",
    pdf="ap-calc-bc-01-limits-continuity-practice.pdf", guide_pdf="ap-calc-bc-01-limits-continuity-guide.pdf",
    sections={"1": "What a limit is", "2": "Evaluating limits algebraically", "3": "The squeeze theorem",
              "4": "Continuity and discontinuities", "5": "Infinite limits and limits at infinity",
              "6": "The Intermediate Value Theorem"},
    rules={"1": "R1.1–R1.4. The limit ignores $f(a)$; the two-sided limit exists only when both one-sided limits agree. Substitute first when $f$ is continuous.",
           "2": "R1.5–R1.6. $\\tfrac00$ means simplify: factor, cancel, rationalize. $\\frac{\\sin u}{u}\\to1$ and $\\frac{1-\\cos u}{u}\\to0$ as $u\\to0$.",
           "3": "R1.7. If $g\\le f\\le h$ and $g,h\\to L$, then $f\\to L$.",
           "4": "R1.8–R1.10. Continuous at $a$: $f(a)$ defined, limit exists, and they are equal. Hole, jump, or infinite discontinuity.",
           "5": "R1.11–R1.13. $\\frac{c}{0}$ gives $\\pm\\infty$ (check signs). At $\\pm\\infty$ compare degrees; $\\sqrt{x^2}=|x|$.",
           "6": "R1.14–R1.16. Continuous on $[a,b]$ and $k$ between $f(a)$ and $f(b)$ implies $f(c)=k$ for some $c$."},
    abstract="Twelve exam-style multiple-choice questions on all sixteen Unit 1 topics, grouped by the sections of the Unit 1 Study Guide, and one nine-point free-response question on continuity, a removable discontinuity and the Intermediate Value Theorem. Items 1–10 are no-calculator; items marked [calculator] allow a graphing calculator. Write each answer in the blank beside the number. The key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (24 min) and 15 minutes for the free response.",
    setup="Allow 24 minutes for the multiple choice and 15 for the free response. Items 11–12 allow a graphing calculator.",
)

F1 = fig("u1-q1", r"""\begin{tikzpicture}
\begin{axis}[width=7cm,height=4.6cm,axis lines=middle,xmin=-0.5,xmax=6.5,ymin=-0.5,ymax=4.6,xtick={1,...,6},ytick={1,2,3,4},xlabel={$x$},ylabel={$y$},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[thick,domain=0:3]{0.5*x+1.5};
\addplot[thick,domain=3:6]{3-(x-3)*0.6};
\addplot[only marks,mark=*,mark size=1.8pt,mark options={fill=white}] coordinates{(3,3)};
\addplot[only marks,mark=*,mark size=1.8pt] coordinates{(3,1)};
\end{axis}\end{tikzpicture}""", "Graph of f on 0 ≤ x ≤ 6: a line rising from (0, 1.5) to an open circle at (3, 3), then a line falling from (3, 3) to (6, 1.2); a solid dot at (3, 1).")

# checks
assert sp.limit((x**2 - 4) / (x**2 + x - 6), x, 2) == sp.Rational(4, 5)
assert sp.limit((sp.sqrt(x + 4) - 2) / x, x, 0) == sp.Rational(1, 4)
assert sp.limit(sp.sin(3 * x) / sp.tan(2 * x), x, 0) == sp.Rational(3, 2)
assert sp.limit((1 - sp.cos(x)) / x**2, x, 0) == sp.Rational(1, 2)
assert sp.limit((5 * x**3 - x) / (2 - 4 * x**3), x, sp.oo) == sp.Rational(-5, 4)
assert sp.limit(sp.sqrt(9 * x**2 + x) / (2 * x - 1), x, -sp.oo) == sp.Rational(-3, 2)
assert sp.limit((x + 1) / (x - 2) ** 1, x, 2, "-") == -sp.oo
a = sp.symbols("a")
assert sp.solve(sp.Eq(a * 2 + 3, 2**2 - a), a) == [sp.Rational(1, 3)]

QS = [
    Q(1, 1, "R1.2", "The graph of $f$ is shown. Which statement is true?",
      ["$\\lim_{x\\to3}f(x)=1$", "$\\lim_{x\\to3}f(x)=3$", "$\\lim_{x\\to3}f(x)$ does not exist", "$f$ is continuous at $x=3$"], "B",
      "Both one-sided limits are 3; the dot at height 1 is $f(3)$, not the limit.",
      "A limit reads the height the curve approaches from each side; the isolated value $f(3)$ does not matter (R1.1–R1.3).",
      ["From the left, the line rises toward the open circle at height 3; from the right the line also starts at height 3.",
       "Both one-sided limits equal 3, so $\\lim_{x\\to3}f(x)=3$."],
      {"A": "1 is $f(3)$, the value at the point; a limit ignores it.",
       "C": "the one-sided limits are equal (both 3), so the limit exists.",
       "D": "$f(3)=1\\neq3=\\lim_{x\\to3}f(x)$, so the third continuity condition fails: a removable discontinuity."},
      fig=F1),
    Q(2, 1, "R1.3", "The table gives values of $g$ near $x=2$. Which is the best estimate of $\\lim_{x\\to2}g(x)$?",
      ["$0$", "$2$", "$4.9$", "$5$"], "D",
      "Values approach 5 from both sides.",
      "Read the trend from both sides of $x=2$; $g(2)$ itself is not in the table and does not matter (R1.3).",
      ["Left: 4.61, 4.96, 4.996. Right: 5.004, 5.04, 5.41.", "Both sides close in on 5."],
      {"A": "there is no 0 anywhere in the values; the limit is about outputs, not the input.",
       "B": "2 is the input $x$ approaches, not the output $g(x)$ approaches.",
       "C": "4.9 is one left-side value; closer values (4.996, 5.004) show the outputs heading to 5."},
      table=Table([["$x$", "1.9", "1.99", "1.999", "2.001", "2.01", "2.1"],
                   ["$g(x)$", "4.61", "4.96", "4.996", "5.004", "5.04", "5.41"]])),
    Q(3, 2, "R1.5", "$\\displaystyle\\lim_{x\\to2}\\frac{x^2-4}{x^2+x-6}$ is",
      ["$0$", "$\\dfrac{4}{5}$", "$1$", "nonexistent"], "B",
      "$\\frac{(x-2)(x+2)}{(x-2)(x+3)}=\\frac{x+2}{x+3}\\to\\frac45$.",
      "Substitution gives $\\tfrac00$, the signal to factor and cancel the common factor $(x-2)$ (R1.5).",
      ["$x^2-4=(x-2)(x+2)$ and $x^2+x-6=(x-2)(x+3)$.", "Cancel: $\\frac{x+2}{x+3}$; substitute $x=2$: $\\frac{4}{5}$."],
      {"A": "reads the 0 in the numerator as the answer; the denominator is also 0.",
       "C": "would follow from cancelling $x^2$ terms, which is not a legal cancellation.",
       "D": "$\\tfrac00$ is indeterminate, not proof that the limit fails; after cancelling it exists."}),
    Q(4, 2, "R1.5", "$\\displaystyle\\lim_{x\\to0}\\frac{\\sqrt{x+4}-2}{x}$ is",
      ["$-\\dfrac14$", "$0$", "$\\dfrac14$", "$\\dfrac12$"], "C",
      "Multiply by the conjugate: $\\frac{1}{\\sqrt{x+4}+2}\\to\\frac14$.",
      "A root minus a number over something going to 0: multiply by the conjugate (R1.5). (It is also $\\frac{d}{dx}\\sqrt{x}$ at $x=4$.)",
      ["$\\frac{(\\sqrt{x+4}-2)(\\sqrt{x+4}+2)}{x(\\sqrt{x+4}+2)}=\\frac{x}{x(\\sqrt{x+4}+2)}=\\frac{1}{\\sqrt{x+4}+2}$.", "At $x=0$: $\\frac{1}{2+2}=\\frac14$."],
      {"A": "a sign slip: $(\\sqrt{x+4}-2)(\\sqrt{x+4}+2)=x$, not $-x$.",
       "B": "stops at the numerator going to 0, ignoring the denominator.",
       "D": "forgets the $+2$ in the conjugate sum, using $\\frac{1}{\\sqrt{4}}$."}),
    Q(5, 2, "R1.6", "$\\displaystyle\\lim_{x\\to0}\\frac{\\sin 3x}{\\tan 2x}$ is",
      ["$0$", "$\\dfrac23$", "$1$", "$\\dfrac32$"], "D",
      "$\\frac{\\sin3x}{3x}\\cdot\\frac{2x}{\\sin2x}\\cdot\\cos2x\\cdot\\frac{3}{2}\\to\\frac32$.",
      "Match each sine with its own argument to use $\\frac{\\sin u}{u}\\to1$ (R1.6).",
      ["$\\frac{\\sin3x}{\\tan2x}=\\frac{\\sin3x}{\\sin2x}\\cos2x=\\frac{\\sin3x}{3x}\\cdot\\frac{2x}{\\sin2x}\\cdot\\frac{3x}{2x}\\cos2x$.",
       "The limits are $1\\cdot1\\cdot\\frac32\\cdot1=\\frac32$."],
      {"A": "treats $\\sin 0=0$ in the numerator as decisive; the denominator also goes to 0.",
       "B": "inverts the ratio of the arguments.",
       "C": "assumes the two special limits cancel completely and ignores the coefficients 3 and 2."}),
    Q(6, 3, "R1.7", "If $3-x^2\\le f(x)\\le 3+x^2$ for all $x$, then $\\displaystyle\\lim_{x\\to0}f(x)$ is",
      ["$0$", "$3$", "$6$", "impossible to determine"], "B",
      "Both bounds tend to 3, so the squeeze theorem gives 3.",
      "Squeeze theorem: bounds with a common limit force the middle function to that limit (R1.7).",
      ["$\\lim_{x\\to0}(3-x^2)=3$ and $\\lim_{x\\to0}(3+x^2)=3$.", "So $\\lim_{x\\to0}f(x)=3$."],
      {"A": "is the limit of $x^2$, not of the bounds.",
       "C": "adds the two bounds' limits.",
       "D": "the squeeze theorem determines the limit without knowing $f$ itself."}),
    Q(7, 4, "R1.10", "For what value of $a$ is $f(x)=\\begin{cases}ax+3,&x<2\\\\ x^2-a,&x\\ge2\\end{cases}$ continuous at $x=2$?",
      ["$-\\dfrac13$", "$0$", "$\\dfrac13$", "$1$"], "C",
      "$2a+3=4-a$ gives $a=\\frac13$.",
      "Continuity of a piecewise function: the left-hand limit must equal the right-hand limit and $f(2)$ (R1.8, R1.10).",
      ["Left: $\\lim_{x\\to2^-}(ax+3)=2a+3$. Right and $f(2)$: $4-a$.", "$2a+3=4-a\\Rightarrow3a=1\\Rightarrow a=\\frac13$."],
      {"A": "sign error when moving $a$ across the equation: check $2(-\\frac13)+3=\\frac73$ but $4+\\frac13=\\frac{13}{3}$.",
       "B": "with $a=0$ the left-hand limit is 3 and the right-hand limit is 4: a jump.",
       "D": "solves $2a+3=4+a$, dropping the minus sign on $a$."}),
    Q(8, 4, "R1.9", "$h(x)=\\dfrac{x^2-1}{x^2-3x+2}$ has",
      ["vertical asymptotes at $x=1$ and $x=2$",
       "a removable discontinuity at $x=2$ and a vertical asymptote at $x=1$",
       "removable discontinuities at $x=1$ and $x=2$",
       "a removable discontinuity at $x=1$ and a vertical asymptote at $x=2$"], "D",
      "$\\frac{(x-1)(x+1)}{(x-1)(x-2)}$: the canceled factor is a hole, the surviving one an asymptote.",
      "A zero of the denominator gives a hole if its factor cancels and a vertical asymptote if it survives (R1.9).",
      ["Factor: $\\frac{(x-1)(x+1)}{(x-1)(x-2)}=\\frac{x+1}{x-2}$ for $x\\neq1$.",
       "At $x=1$ the limit is $\\frac{2}{-1}=-2$: a hole. At $x=2$ the reduced form is $\\frac{3}{0}$: a vertical asymptote."],
      {"A": "treats every zero of the denominator as an asymptote; $x-1$ cancels.",
       "B": "swaps the two behaviors.",
       "C": "only $x-1$ cancels; near $x=2$ the function is unbounded."}, layout="one"),
    Q(9, 5, "R1.12", "$\\displaystyle\\lim_{x\\to\\infty}\\frac{5x^3-x}{2-4x^3}$ is",
      ["$-\\dfrac54$", "$0$", "$\\dfrac52$", "$\\infty$"], "A",
      "Equal degrees: ratio of leading coefficients $\\frac{5}{-4}$.",
      "For a rational function at infinity compare degrees; equal degrees give the ratio of leading coefficients (R1.12).",
      ["Both numerator and denominator have degree 3.", "Leading coefficients 5 and $-4$: the limit is $-\\frac54$."],
      {"B": "is the answer when the numerator has lower degree.",
       "C": "uses the constant term 2 instead of the leading coefficient $-4$.",
       "D": "is the answer only when the numerator has higher degree."}),
    Q(10, 5, "R1.13", "$\\displaystyle\\lim_{x\\to-\\infty}\\frac{\\sqrt{9x^2+x}}{2x-1}$ is",
      ["$-\\dfrac32$", "$0$", "$\\dfrac32$", "$\\dfrac92$"], "A",
      "For $x<0$, $\\sqrt{9x^2+x}=-x\\sqrt{9+1/x}$; the ratio tends to $\\frac{-3}{2}$.",
      "$\\sqrt{x^2}=|x|$, which is $-x$ when $x\\to-\\infty$ (R1.13).",
      ["$\\sqrt{9x^2+x}=|x|\\sqrt{9+\\tfrac1x}=-x\\sqrt{9+\\tfrac1x}$ for $x<0$.",
       "$\\frac{-x\\sqrt{9+1/x}}{x(2-1/x)}=\\frac{-\\sqrt{9+1/x}}{2-1/x}\\to-\\frac32$. (Check: the numerator is positive and the denominator negative.)"],
      {"C": "is the limit as $x\\to+\\infty$; it ignores $|x|=-x$ for negative $x$.",
       "D": "forgets to take the square root of 9.",
       "B": "treats the root as lower degree than the denominator; $\\sqrt{x^2}$ has degree 1."}),
    Q(11, 6, "R1.16", "$f$ is continuous on $[0,4]$ with values in the table. What is the least number of solutions $f(x)=1$ must have on $[0,4]$?",
      ["One", "Two", "Three", "Four"], "C",
      "Values cross 1 on $(0,1)$, $(1,2)$ and $(3,4)$: at least three.",
      "With a table for a continuous function, each sign change of $f(x)-k$ between consecutive inputs guarantees a solution there by the IVT (R1.16).",
      ["$f-1$ at $x=0,1,2,3,4$: $2,-1,3,4,-2$.", "Sign changes on $(0,1)$, $(1,2)$, $(3,4)$: at least three solutions."],
      {"A": "counts only the first crossing.",
       "B": "misses the crossing between $x=3$ ($f=5$) and $x=4$ ($f=-1$).",
       "D": "counts a crossing on $(2,3)$, where $f$ goes from 4 to 5 and never needs to reach 1."},
      calc=True, table=Table([["$x$", "0", "1", "2", "3", "4"], ["$f(x)$", "3", "0", "4", "5", "$-1$"]])),
    Q(12, 6, "R1.15", "Let $f(x)=x^3-4x+2$. The IVT applied on which interval guarantees a zero of $f$ in $(1,2)$, and which value of $f$ makes it work?",
      ["$[1,2]$, since $f(1)=1$ and $f(2)=2$", "$[0,1]$, since $f(0)=2$ and $f(1)=-1$",
       "No interval works, since $f$ is not monotonic", "$[1,2]$, since $f(1)=-1$ and $f(2)=2$"], "D",
      "$f$ is a polynomial (continuous) and changes sign on $[1,2]$: $-1<0<2$.",
      "IVT: continuous on $[a,b]$ and 0 between $f(a)$ and $f(b)$ (R1.15). Polynomials are continuous everywhere.",
      ["$f(1)=1-4+2=-1$ and $f(2)=8-8+2=2$.", "$f$ is continuous on $[1,2]$ and $-1<0<2$, so $f(c)=0$ for some $c$ in $(1,2)$. (A calculator gives $c\\approx1.675$.)"],
      {"A": "miscomputes $f(1)$; with $f(1)=1$ there would be no sign change.",
       "B": "is a true sign change, but it places a zero in $(0,1)$, not $(1,2)$.",
       "C": "the IVT needs only continuity, not monotonicity."}, calc=True, layout="one"),
]

FRS = [
    FRQ(1, [4, 6], "Continuity and the IVT",
        "Let $f$ be the function defined by $f(x)=\\dfrac{x^2-x-6}{x-3}$ for $x\\neq3$ and $f(3)=k$, where $k$ is a constant. Let $g(x)=x^3-2x-5$.",
        [P("a", "Find $\\lim_{x\\to3}f(x)$. Show the work that leads to your answer.",
           ["factors and cancels (or equivalent)", "limit equals 5"],
           ["$\\frac{x^2-x-6}{x-3}=\\frac{(x-3)(x+2)}{x-3}=x+2$ for $x\\neq3$, so $\\lim_{x\\to3}f(x)=3+2=5$."]),
         P("b", "For what value of $k$ is $f$ continuous at $x=3$? Justify your answer using the definition of continuity.",
           ["$k=5$", "justification names all three conditions: $f(3)$ defined, the limit exists, and they are equal"],
           ["$k=5$. Then $f(3)=5$ is defined, $\\lim_{x\\to3}f(x)=5$ exists by part (a), and $\\lim_{x\\to3}f(x)=f(3)$, so $f$ is continuous at 3."]),
         P("c", "With the value of $k$ from part (b), is there a value $c$ in $[0,4]$ with $f(c)=g(c)$? Justify your answer.",
           ["defines $h=f-g$ (or compares $f$ and $g$ at both endpoints)", "$h(0)=7$ and $h(4)=-45$ (or equivalent values)",
            "states that $h$ is continuous on $[0,4]$", "applies the IVT to conclude yes"],
           ["Let $h(x)=f(x)-g(x)=(x+2)-(x^3-2x-5)$, which equals $x+2-x^3+2x+5$ for every $x$ once $k=5$.",
            "$h$ is a polynomial, so it is continuous on $[0,4]$. $h(0)=2-(-5)=7>0$ and $h(4)=6-51=-45<0$.",
            "Since $h(4)<0<h(0)$, the IVT gives $c$ in $(0,4)$ with $h(c)=0$, that is $f(c)=g(c)$."]),
         P("d", "Find $\\displaystyle\\lim_{x\\to\\infty}\\frac{g(x)}{2x^3+f(x)}$.",
           ["answer $\\frac12$ with supporting work"],
           ["$\\frac{x^3-2x-5}{2x^3+x+2}$ has equal degrees, so the limit is $\\frac12$."])]),
]

# FRQ numbers
assert sp.limit((x**2 - x - 6) / (x - 3), x, 3) == 5
hh = (x + 2) - (x**3 - 2 * x - 5)
assert hh.subs(x, 0) == 7 and hh.subs(x, 4) == -45
assert sp.limit((x**3 - 2 * x - 5) / (2 * x**3 + x + 2), x, sp.oo) == sp.Rational(1, 2)
