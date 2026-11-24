"""Unit 5 Practice Set: Analytical Applications of Differentiation (15 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, fig

x, t = sp.symbols("x t")

DOC = dict(
    unit=5, title="Analytical Applications of Differentiation", topics="5.1–5.12",
    pdf="ap-calc-bc-05-analytical-applications-practice.pdf", guide_pdf="ap-calc-bc-05-analytical-applications-guide.pdf",
    sections={"1": "Mean Value and Extreme Value Theorems", "2": "Increasing, decreasing, and extrema",
              "3": "Concavity and the second derivative test", "4": "Connecting $f$, $f'$ and $f''$", "5": "Optimization",
              "6": "Behaviors of implicit relations"},
    rules={"1": "R5.1–R5.2. MVT: continuous on $[a,b]$, differentiable on $(a,b)$ gives $f'(c)=\\frac{f(b)-f(a)}{b-a}$. EVT needs a closed interval.",
           "2": "R5.3–R5.6. Critical points: $f'=0$ or undefined. Extremum where $f'$ changes sign. Absolute extrema: critical points and endpoints.",
           "3": "R5.7–R5.8. Inflection where $f''$ changes sign. $f'(c)=0$, $f''(c)<0$: max; $f''(c)>0$: min.",
           "4": "R5.9. On a graph of $f'$: above the axis, $f$ increases; rising, $f$ is concave up; crossing from $+$ to $-$, $f$ has a maximum.",
           "5": "R5.10. One variable, critical points, then justify the absolute extremum.",
           "6": "R5.11. Signs of $\\frac{dy}{dx}$ and $\\frac{d^2y}{dx^2}$ at a point describe an implicit curve there."},
    abstract="Fifteen exam-style multiple-choice questions on Unit 5, grouped by the sections of the Unit 5 Study Guide, and one nine-point free-response question that analyzes a function from its derivative. Items marked [calculator] allow a graphing calculator; the rest are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (30 min) and 15 minutes for the free response.",
    setup="Allow 30 minutes for the multiple choice and 15 for the free response. Item 14 needs a graphing calculator.",
)

F11 = fig("u5-q11", r"""\begin{tikzpicture}
\begin{axis}[width=7.6cm,height=4.6cm,axis lines=middle,xmin=-0.3,xmax=7.5,ymin=-2.6,ymax=2.6,xtick={1,...,7},ytick={-2,-1,1,2},xlabel={$x$},ylabel={$f'(x)$},grid=major,grid style={gray!25},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[very thick] coordinates{(0,-2) (2,2) (4,2) (6,-2) (7,0)};
\end{axis}\end{tikzpicture}""", "Graph of f′ on 0 ≤ x ≤ 7, made of segments: from (0,−2) up to (2,2), level to (4,2), down to (6,−2), then up to (7,0). It crosses the x-axis at x = 1 and x = 5.")

# checks
assert sp.solve(sp.Eq(3 * x**2, 9), x) == [-sp.sqrt(3), sp.sqrt(3)]
f4 = x**sp.Rational(2, 3) * (x - 5)
assert sp.solve(sp.diff(f4, x), x) == [2]
f6 = x**3 - 12 * x
assert [f6.subs(x, k) for k in (-3, -2, 2, 5)] == [9, 16, -16, 65]
assert sp.solve(sp.diff(x * sp.exp(-x), x), x) == [1]
assert sp.solve(sp.diff(x**4 - 4 * x**3, x, 2), x) == [0, 2]
xs = [float(v) for v in (sp.asin(sp.log(sp.Rational(3, 2))), sp.pi - sp.asin(sp.log(sp.Rational(3, 2))))]
assert abs(xs[0] - 0.4171) < 1e-3 and abs(xs[1] - 2.7245) < 1e-3
S = x**2 + 128 / x
assert sp.solve(sp.diff(S, x), x)[0] == 4 and S.subs(x, 4) == 48
Y = 2 / sp.sqrt(x)  # x y^2 = 4, y > 0
assert sp.diff(Y, x).subs(x, 1) == -1 and sp.diff(Y, x, 2).subs(x, 1) == sp.Rational(3, 2)

QS = [
    Q(1, 1, "R5.1", "For $f(x)=x^3$ on $[0,3]$, the value of $c$ guaranteed by the Mean Value Theorem is",
      ["$0$", "$\\dfrac32$", "$\\sqrt3$", "$3$"], "C",
      "$3c^2=\\frac{27-0}{3}=9$, so $c=\\sqrt3$.",
      "MVT: $f'(c)$ equals the average rate of change on $[a,b]$ (R5.1).",
      ["Average rate: $\\frac{27-0}{3-0}=9$.", "$f'(c)=3c^2=9$, so $c=\\sqrt3$ (the root in $(0,3)$)."],
      {"A": "is where $f'=0$, Rolle's conclusion; that needs $f(0)=f(3)$, which is false here.",
       "B": "is the midpoint of the interval; the MVT point is generally not the midpoint.",
       "D": "is an endpoint; the MVT promises $c$ strictly inside $(0,3)$."}),
    Q(2, 1, "R5.1", "Which function satisfies the hypotheses of the Mean Value Theorem on $[-1,1]$?",
      ["$x^3-x$", "$|x|$", "$x^{2/3}$", "$\\dfrac1x$"], "A",
      "A polynomial is continuous and differentiable everywhere.",
      "MVT needs continuity on $[-1,1]$ and differentiability on $(-1,1)$ (R5.1).",
      ["$x^3-x$ is a polynomial: both hypotheses hold.", "The others fail at $x=0$."],
      {"B": "has a corner at 0: not differentiable there.",
       "C": "has a cusp at 0: not differentiable there.",
       "D": "is not even defined (or continuous) at 0."}),
    Q(3, 1, "R5.2", "Which function is guaranteed by the Extreme Value Theorem to have an absolute maximum on the given interval?",
      ["$\\dfrac1x$ on $(0,1]$", "$\\tan x$ on $\\left[0,\\frac\\pi2\\right)$", "$x^2$ on $(-1,2)$", "$\\cos x$ on $[0,5]$"], "D",
      "Continuous on a closed interval.",
      "The EVT needs a continuous function on a closed interval (R5.2).",
      ["$\\cos x$ is continuous and $[0,5]$ is closed, so both extrema are attained."],
      {"A": "is unbounded near 0, and the interval is not closed.",
       "B": "grows without bound as $x\\to\\frac\\pi2^-$; the interval is not closed.",
       "C": "approaches 4 as $x\\to2$ but never reaches it on the open interval."}, layout="two"),
    Q(4, 2, "R5.3", "The critical points of $f(x)=x^{2/3}(x-5)$ are",
      ["$x=2$ only", "$x=0$ and $x=2$", "$x=0$ and $x=5$", "$x=5$ only"], "B",
      "$f'=\\frac{5(x-2)}{3x^{1/3}}$: zero at 2, undefined at 0.",
      "Critical points are where $f'=0$ or $f'$ is undefined, inside the domain (R5.3).",
      ["$f(x)=x^{5/3}-5x^{2/3}$, so $f'(x)=\\frac53x^{2/3}-\\frac{10}{3}x^{-1/3}=\\frac{5(x-2)}{3x^{1/3}}$.",
       "$f'=0$ at $x=2$; $f'$ undefined at $x=0$, which is in the domain."],
      {"A": "misses $x=0$, where $f'$ does not exist.",
       "C": "uses the zeros of $f$, not of $f'$.",
       "D": "is a zero of $f$, not a critical point."}),
    Q(5, 2, "R5.5", "If $f'(x)=(x-2)^2(x+1)(x-4)$, at which values of $x$ does $f$ have a relative minimum?",
      ["$x=-1$ only", "$x=2$ and $x=4$", "$x=4$ only", "$x=-1$ and $x=4$"], "C",
      "$f'$ changes from $-$ to $+$ only at 4; no sign change at 2.",
      "First derivative test: a minimum where $f'$ changes from negative to positive (R5.5).",
      ["Sign of $f'$: $+$ for $x<-1$, $-$ on $(-1,2)$ and $(2,4)$, $+$ for $x>4$. The squared factor never changes sign.",
       "Only at $x=4$ does $f'$ go from $-$ to $+$."],
      {"A": "is a relative maximum ($f'$ changes $+$ to $-$).",
       "B": "includes 2, where $f'=0$ but does not change sign.",
       "D": "includes $-1$, the relative maximum."}),
    Q(6, 2, "R5.6", "What is the absolute maximum value of $f(x)=x^3-12x$ on $[-3,5]$?",
      ["$-16$", "$9$", "$16$", "$65$"], "D",
      "Candidates: $f(-3)=9$, $f(-2)=16$, $f(2)=-16$, $f(5)=65$.",
      "Candidates test: critical points and endpoints (R5.6).",
      ["$f'=3x^2-12=0$ at $x=\\pm2$.", "Values: $9,\\ 16,\\ -16,\\ 65$. The largest is $f(5)=65$."],
      {"A": "is the absolute minimum.",
       "B": "is $f(-3)$, the left endpoint.",
       "C": "is the relative maximum at $x=-2$; it forgets the right endpoint."}),
    Q(7, 2, "R5.4", "On which interval is $f(x)=xe^{-x}$ increasing?",
      ["$(-\\infty,1)$", "$(1,\\infty)$", "$(0,\\infty)$", "$(-\\infty,0)$"], "A",
      "$f'=e^{-x}(1-x)>0$ for $x<1$.",
      "Increasing where $f'>0$ (R5.4).",
      ["$f'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)$.", "$e^{-x}>0$, so the sign is that of $1-x$: positive for $x<1$."],
      {"B": "is where $f'<0$, the decreasing interval.",
       "C": "is where $f>0$; positivity of $f$ says nothing about increasing.",
       "D": "is where $f<0$."}),
    Q(8, 3, "R5.7", "At which values of $x$ does $f(x)=x^4-4x^3$ have a point of inflection?",
      ["$x=0$ only", "$x=2$ only", "$x=3$ only", "$x=0$ and $x=2$"], "D",
      "$f''=12x(x-2)$ changes sign at 0 and at 2.",
      "Inflection where $f''$ changes sign (R5.7).",
      ["$f'=4x^3-12x^2$, $f''=12x^2-24x=12x(x-2)$.", "$f''>0$ for $x<0$, $<0$ on $(0,2)$, $>0$ for $x>2$: both are inflection points."],
      {"A": "misses $x=2$.",
       "B": "misses $x=0$, perhaps because $f'(0)=0$ too; it is still an inflection point.",
       "C": "is the critical point where $f$ has its minimum."}),
    Q(9, 3, "R5.8", "$f$ is twice differentiable with $f'(2)=0$ and $f''(2)=-5$. At $x=2$, $f$ has",
      ["a relative minimum", "a relative maximum", "a point of inflection", "none of these; the test is inconclusive"], "B",
      "Second derivative test: $f'=0$ and $f''<0$ give a maximum.",
      "Second derivative test (R5.8).",
      ["$f'(2)=0$: critical point.", "$f''(2)<0$: concave down there, so a relative maximum."],
      {"A": "reverses the test: $f''>0$ gives a minimum.",
       "C": "needs $f''$ to change sign; $f''(2)\\neq0$.",
       "D": "the test is inconclusive only when $f''(2)=0$."}, layout="two"),
    Q(10, 3, "R5.7", "If $f'(x)=x^3-3x$, on which interval is the graph of $f$ concave down?",
      ["$(-\\sqrt3,\\sqrt3)$", "$(-1,1)$", "$(1,\\infty)$", "$(-\\infty,-1)$"], "B",
      "$f''=3x^2-3<0$ on $(-1,1)$.",
      "Concave down where $f''<0$, that is, where $f'$ decreases (R5.7).",
      ["$f''(x)=3x^2-3=3(x-1)(x+1)$.", "Negative on $(-1,1)$."],
      {"A": "uses the zeros of $f'$ instead of $f''$.",
       "C": "is part of where $f''>0$: concave up.",
       "D": "is also concave up ($f''>0$ there)."}),
    Q(11, 4, "R5.9", "The graph of $f'$, the derivative of $f$, is shown for $0\\le x\\le7$. At what value of $x$ does $f$ have a relative maximum?",
      ["$1$", "$2$", "$5$", "$7$"], "C",
      "$f'$ changes from positive to negative at $x=5$.",
      "On a graph of $f'$, a relative max of $f$ is where $f'$ crosses from above to below the axis (R5.9).",
      ["$f'>0$ on $(1,5)$ and $f'<0$ on $(5,7)$.", "So $f$ increases then decreases at 5: a relative maximum."],
      {"A": "$f'$ changes from negative to positive at 1: a relative minimum.",
       "B": "is where $f'$ stops increasing; that concerns concavity, not extrema.",
       "D": "$f'<0$ just before 7, so $f$ is decreasing into the endpoint: a minimum candidate, not a maximum."}, fig=F11),
    Q(12, 4, "R5.9", "For the same graph of $f'$, on which intervals is the graph of $f$ concave up?",
      ["$(0,2)$ and $(6,7)$", "$(1,5)$", "$(2,4)$", "$(0,1)$ and $(5,7)$"], "A",
      "$f'$ is increasing on $(0,2)$ and $(6,7)$.",
      "$f$ is concave up where $f'$ is increasing, that is where the $f'$ graph rises (R5.9).",
      ["Rising segments of the $f'$ graph: $(0,2)$ and $(6,7)$.", "On $(2,4)$ the graph is flat ($f''=0$) and on $(4,6)$ it falls."],
      {"B": "is where $f'>0$: $f$ is increasing, not necessarily concave up.",
       "C": "is where $f'$ is constant: $f''=0$, so $f$ is linear there.",
       "D": "is where $f'<0$: $f$ is decreasing."}, fig=F11),
    Q(13, 5, "R5.10", "An open-top box with a square base must hold 32 ft³. Which dimensions minimize the surface area (base side × base side × height)?",
      ["$2\\times2\\times8$", "$3\\times3\\times\\frac{32}{9}$", "$\\sqrt[3]{32}$ on every side", "$4\\times4\\times2$"], "D",
      "$S=x^2+\\frac{128}{x}$; $S'=0$ at $x=4$, so $h=2$.",
      "Optimization: write $S$ in one variable using the volume, then find and justify the minimum (R5.10).",
      ["$h=\\frac{32}{x^2}$, so $S=x^2+4xh=x^2+\\frac{128}{x}$.",
       "$S'=2x-\\frac{128}{x^2}=0$ gives $x^3=64$, $x=4$, $h=2$; $S'$ changes $-$ to $+$, so this is the minimum ($S=48$)."],
      {"A": "has surface area $4+64=68$.",
       "B": "has surface area $9+\\frac{128}{3}\\approx51.7$, more than 48.",
       "C": "a cube is optimal for a closed box, not an open one ($S\\approx50.4$)."}, layout="two"),
    Q(14, 5, "R5.5", "The derivative of $f$ is $f'(x)=e^{\\sin x}-1.5$ for $0\\le x\\le6$. At what value of $x$ does $f$ have a relative maximum?",
      ["$0.417$", "$1.571$", "$2.724$", "$3.142$"], "C",
      "$f'=0$ where $\\sin x=\\ln1.5$; $f'$ changes $+$ to $-$ at $x\\approx2.724$.",
      "Find the zeros of $f'$ with the calculator and check the sign change (R5.5).",
      ["$e^{\\sin x}=1.5$ at $x=\\arcsin(\\ln1.5)\\approx0.417$ and $\\pi-0.417\\approx2.724$.",
       "$f'<0$ on $(0,0.417)$, $>0$ on $(0.417,2.724)$, $<0$ on $(2.724,6)$: maximum at 2.724."],
      {"A": "is where $f'$ changes from $-$ to $+$: a relative minimum.",
       "B": "is $\\frac\\pi2$, where $f'$ itself is largest: an inflection point of $f$.",
       "D": "is $\\pi$, where $f'=1-1.5<0$; not a critical point."}, calc=True),
    Q(15, 6, "R5.11", "Consider the curve $xy^2=4$ with $y>0$. At the point $(1,2)$, the curve is",
      ["increasing and concave up", "decreasing and concave up", "increasing and concave down", "decreasing and concave down"], "B",
      "$\\frac{dy}{dx}=-\\frac{y}{2x}=-1<0$; $\\frac{d^2y}{dx^2}=\\frac32>0$.",
      "Use the signs of $\\frac{dy}{dx}$ and $\\frac{d^2y}{dx^2}$ at the point (R5.11).",
      ["$y^2+2xy\\frac{dy}{dx}=0$, so $\\frac{dy}{dx}=-\\frac{y}{2x}=-1$ at $(1,2)$.",
       "$\\frac{d^2y}{dx^2}=-\\frac{2xy'-2y}{4x^2}$; at $(1,2)$: $-\\frac{-2-4}{4}=\\frac32>0$. (Check: $y=2x^{-1/2}$.)"],
      {"A": "has the wrong sign of $\\frac{dy}{dx}$.",
       "C": "has both signs wrong.",
       "D": "has the wrong sign of $\\frac{d^2y}{dx^2}$."}, layout="two"),
]

fp = (x**2 - x - 2) / 2
F = 4 + sp.integrate(fp.subs(x, t), (t, 0, x))
assert F.subs(x, 3) == sp.Rational(13, 4) and F.subs(x, 4) == sp.Rational(20, 3)
assert (F.subs(x, 4) - 4) / 4 == sp.Rational(2, 3)
assert fp.subs(x, 3) == 2 and sp.Rational(13, 4) + 2 * sp.Rational(1, 5) == sp.Rational(73, 20)

FRS = [
    FRQ(1, [1, 2, 3], "Analyzing a function from its derivative",
        "A function $f$ is differentiable on $[-3,4]$ with $f'(x)=\\dfrac{x^2-x-2}{2}$. It is known that $f(0)=4$, $f(3)=\\frac{13}{4}$ and $f(4)=\\frac{20}{3}$.",
        [P("a", "Find the $x$-coordinates of all relative extrema of $f$ on $(-3,4)$ and classify each. Justify your answers.",
           ["relative maximum at $x=-1$ with justification ($f'$ changes from positive to negative)", "relative minimum at $x=2$ with justification ($f'$ changes from negative to positive)"],
           ["$f'(x)=\\frac{(x-2)(x+1)}{2}=0$ at $x=-1$ and $x=2$.",
            "$f'$ changes from positive to negative at $x=-1$: relative maximum. $f'$ changes from negative to positive at $x=2$: relative minimum."]),
         P("b", "On what open interval is the graph of $f$ concave up? Justify your answer.",
           ["$f''(x)=x-\\frac12$", "concave up on $(\\frac12,4)$ because $f''>0$ there"],
           ["$f''(x)=\\frac{2x-1}{2}=x-\\frac12$, positive for $x>\\frac12$. Concave up on $(\\frac12,4)$."]),
         P("c", "Must there be a value $c$, $0<c<4$, with $f'(c)=\\frac23$? Justify your answer.",
           ["average rate of change $\\frac{f(4)-f(0)}{4}=\\frac23$", "yes, by the MVT, citing that $f$ is differentiable (hence continuous)"],
           ["$\\frac{f(4)-f(0)}{4-0}=\\frac{20/3-4}{4}=\\frac23$.",
            "$f$ is differentiable on $[-3,4]$, so it is continuous on $[0,4]$ and differentiable on $(0,4)$. By the MVT there is a $c$ in $(0,4)$ with $f'(c)=\\frac23$."]),
         P("d", "Write an equation for the line tangent to the graph of $f$ at $x=3$, and use it to approximate $f(3.2)$. Is the approximation an overestimate or an underestimate? Give a reason.",
           ["tangent line $y=\\frac{13}{4}+2(x-3)$", "approximation $f(3.2)\\approx3.65$", "underestimate, because $f''>0$ (concave up) on $[3,3.2]$"],
           ["$f'(3)=\\frac{9-3-2}{2}=2$, so $y=\\frac{13}{4}+2(x-3)$.",
            "$f(3.2)\\approx\\frac{13}{4}+2(0.2)=3.65$.",
            "$f''(x)=x-\\frac12>0$ on $[3,3.2]$, so the graph is concave up and lies above its tangent line: an underestimate."])]),
]
