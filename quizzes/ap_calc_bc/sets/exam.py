"""AP Calculus BC Full Practice Exam (May 2027 format): 42 MC (29 no calculator + 13 calculator) and 6 FRQ.

In the exam, an item's `sec` is its unit number (the quiz tallies by unit and links to that unit's guide).
"""
import math

import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, Table, fig

x, t, th = sp.symbols("x t theta")

DOC = dict(
    pdf="ap-calc-bc-11-practice-exam.pdf",
    abstract="A full-length practice exam in the May 2027 format: Section I has 42 multiple-choice questions (Part A, 29 questions in 62 minutes without a calculator; Part B, 13 questions in 38 minutes with a graphing calculator), and Section II has six nine-point free-response questions (Part A, 2 questions in 30 minutes with a calculator; Part B, 4 questions in 60 minutes without). The multiple-choice questions follow the unit weighting in the course description, and every item is tagged with its unit and the rule from the unit guides that it tests. All questions are original. The key at the end gives an answers-only strip, a reason and rule for every multiple-choice item, a scoring worksheet, and the free-response scoring guides.",
    pace="Section I: 100 minutes. Section II: 90 minutes. Take the sections in order, timed, with a 10-minute break between them.",
    front="\\section*{Directions}\nSection I: choose the best of the four answers and write its letter in the blank beside the question. There is no penalty for wrong answers. In Part B, if the exact value is not one of the choices, select the choice that best approximates it. Section II: show all work. Justify every conclusion with calculus, write the integral or expression you evaluate on the calculator, and give decimal answers correct to three places. Unless otherwise specified, the domain of a function is the set of real numbers for which it is defined, and angles are in radians.",
    frnote="Show all work. Justify your answers, and give decimal answers correct to three places.",
    scoring="\\section*{Scoring worksheet}\nMultiple choice: number correct $\\times\\,1.2857=$ \\blank\\ (out of 54). Free response: total points \\blank\\ (out of 54). Composite: the sum, out of 108. As a rough guide from past exams (cut scores change every year): 68+ is about a 5, 52+ a 4, 40+ a 3, 29+ a 2.",
    setup="Take Part A (29 questions) in 62 minutes without a calculator, then Part B (13 questions) in 38 minutes with one. The free response is on the second tab.",
)

F12 = fig("ex-q12", r"""\begin{tikzpicture}
\begin{axis}[width=7.2cm,height=4.6cm,axis lines=middle,xmin=-0.3,xmax=5.4,ymin=-1.6,ymax=2.4,xtick={1,...,5},ytick={-1,1,2},xlabel={$x$},ylabel={$f'(x)$},grid=major,grid style={gray!25},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[very thick,domain=0:5,samples=80]{(x-1)*(x-4)/2};
\end{axis}\end{tikzpicture}""", "Graph of f′ on 0 ≤ x ≤ 5: an upward-opening parabola crossing the x-axis at x = 1 and x = 4, with its lowest point at (2.5, −1.125); f′(0) = 2 and f′(5) = 2.")

FF4 = fig("ex-fr4", r"""\begin{tikzpicture}
\begin{axis}[width=8.4cm,height=4.8cm,axis lines=middle,xmin=-3.4,xmax=4.5,ymin=-2.6,ymax=2.6,xtick={-3,-2,-1,1,2,3,4},ytick={-2,-1,1,2},xlabel={$x$},ylabel={$f(x)$},grid=major,grid style={gray!25},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[very thick] coordinates{(-3,0) (-2,-2) (0,2) (2,2) (4,-2)};
\end{axis}\end{tikzpicture}""", "Graph of f on −3 ≤ x ≤ 4 made of line segments through (−3,0), (−2,−2), (0,2), (2,2) and (4,−2). It crosses the x-axis at x = −1 and x = 3.", width="0.55\\linewidth")

T_FR3 = Table([["$t$ (seconds)", "0", "2", "5", "8", "12"], ["$v(t)$ (meters per second)", "10", "16", "22", "18", "6"]])

# ---------------- checks (Part A) ----------------
assert sp.limit((x**2 - 9) / (x**2 - 2 * x - 3), x, 3) == sp.Rational(3, 2)
assert sp.limit((3 * x**2 - 5) / (7 + x - 6 * x**2), x, sp.oo) == sp.Rational(-1, 2)
assert sp.diff(x**4, x).subs(x, 2) == 32
assert sp.diff(x * sp.sec(x), x).subs(x, 0) == 1
assert sp.diff(sp.atan(sp.sqrt(x)), x).subs(x, 1) == sp.Rational(1, 4)
assert sp.limit((sp.exp(3 * x) - 1) / sp.sin(x), x, 0) == 3
assert 0 + 1 + 4 == 5 and sp.integrate(x**2, (x, 0, 3)) == 9
assert sp.integrate(sp.tan(x) * sp.sec(x) ** 2, (x, 0, sp.pi / 4)) == sp.Rational(1, 2)
assert sp.simplify(sp.diff(x**2 * sp.log(x) / 2 - x**2 / 4, x) - x * sp.log(x)) == 0
assert sp.simplify(sp.integrate(1 / (x**2 - 1), (x, 2, 3)) - sp.log(sp.Rational(3, 2)) / 2) == 0
assert sp.integrate(x * sp.exp(-x**2), (x, 1, sp.oo)) == 1 / (2 * sp.E)
assert sp.integrate(2 - x - x**2, (x, -2, 1)) == sp.Rational(9, 2) and sp.integrate(2 - x - x**2, (x, -1, 2)) == sp.Rational(3, 2)
assert sp.integrate(3 * t * sp.sqrt(4 + t**2), (t, 0, 1)) == 5 * sp.sqrt(5) - 8
assert sp.integrate((3 + 2 * sp.cos(th)) ** 2 / 2, (th, 0, 2 * sp.pi)) == 11 * sp.pi
nn = sp.symbols("n", integer=True, positive=True)
assert sp.summation(4**nn / 5 ** (nn + 1), (nn, 1, sp.oo)) == sp.Rational(4, 5)
assert sp.series(sp.cos(2 * x), x, 0, 6).removeO().coeff(x, 4) == sp.Rational(2, 3)
yy = 2.0
for xv in (0.0, 0.5):
    yy += 0.5 * xv * yy
assert abs(yy - 2.5) < 1e-12

QS = [
    # ---------------- Part A: no calculator ----------------
    Q(1, 1, "R1.5", "$\\displaystyle\\lim_{x\\to3}\\frac{x^2-9}{x^2-2x-3}$ is",
      ["$0$", "$1$", "$\\dfrac32$", "nonexistent"], "C",
      "$\\frac{(x-3)(x+3)}{(x-3)(x+1)}=\\frac{x+3}{x+1}\\to\\frac64$.",
      "$\\frac00$: factor and cancel (R1.5).",
      ["Cancel $x-3$: $\\frac{x+3}{x+1}$.", "At $x=3$: $\\frac{6}{4}=\\frac32$."],
      {"A": "reads the numerator's 0 as the answer.", "B": "cancels the $x^2$ terms, which is not a legal step.",
       "D": "$\\frac00$ is indeterminate; after cancelling the limit exists."}),
    Q(2, 1, "R1.12", "$\\displaystyle\\lim_{x\\to\\infty}\\frac{3x^2-5}{7+x-6x^2}$ is",
      ["$-\\dfrac12$", "$0$", "$\\dfrac12$", "$\\dfrac37$"], "A",
      "Equal degrees: $\\frac{3}{-6}$.",
      "Rational function at infinity: compare degrees (R1.12).",
      ["Both have degree 2.", "Leading coefficients 3 and $-6$: $-\\frac12$."],
      {"B": "is the answer when the numerator has lower degree.", "C": "drops the sign of $-6x^2$.",
       "D": "uses the constant term 7 instead of the leading coefficient."}),
    Q(3, 2, "R2.3", "$\\displaystyle\\lim_{h\\to0}\\frac{(2+h)^4-16}{h}$ is",
      ["$16$", "$24$", "$32$", "$64$"], "C",
      "It is $f'(2)$ for $f(x)=x^4$: $4\\cdot2^3$.",
      "Recognize the limit as a derivative (R2.3).",
      ["$f(x)=x^4$, $a=2$, $f(2)=16$.", "$f'(2)=4(2)^3=32$."],
      {"A": "is $f(2)$.", "B": "uses $3\\cdot2^3$: the power rule's coefficient is the old exponent, 4.",
       "D": "uses $4\\cdot2^4$: the exponent must drop by one."}),
    Q(4, 2, "R2.6", "Let $f(x)=\\begin{cases}x^2+a,&x\\le1\\\\ bx,&x>1\\end{cases}$. For which $a$ and $b$ is $f$ differentiable at $x=1$?",
      ["$a=0$, $b=2$", "$a=1$, $b=2$", "$a=2$, $b=3$", "$a=1$, $b=1$"], "B",
      "Slopes: $b=2$; values: $1+a=b$.",
      "Differentiable at a junction: match values and slopes (R2.6).",
      ["Slopes at 1: $2x=2$ and $b$, so $b=2$.", "Values at 1: $1+a=b=2$, so $a=1$."],
      {"A": "matches slopes only; with $a=0$ the pieces do not meet ($1\\neq2$).",
       "C": "matches values but not slopes ($2\\neq3$).", "D": "matches values but not slopes ($2\\neq1$)."}, layout="two"),
    Q(5, 2, "R2.10", "If $f(x)=x\\sec x$, then $f'(0)=$",
      ["$0$", "$1$", "$2$", "undefined"], "B",
      "$\\sec x+x\\sec x\\tan x$ at 0 is $1+0$.",
      "Product rule with $(\\sec x)'=\\sec x\\tan x$ (R2.10, R2.12).",
      ["$f'(x)=\\sec x+x\\sec x\\tan x$.", "$f'(0)=1+0=1$."],
      {"A": "multiplies the derivatives: $1\\cdot\\sec0\\tan0=0$.", "C": "adds $\\sec0$ twice.",
       "D": "$\\sec x$ is defined and differentiable at 0."}),
    Q(6, 3, "R3.2", "Let $h(x)=g(x^2)$, where $g$ is differentiable and $g'(4)=-3$. What is $h'(2)$?",
      ["$-12$", "$-6$", "$-3$", "$12$"], "A",
      "$h'(x)=g'(x^2)\\cdot2x$; $h'(2)=g'(4)\\cdot4$.",
      "Chain rule (R3.1–R3.2).",
      ["$h'(2)=g'(2^2)\\cdot2(2)$.", "$=(-3)(4)=-12$."],
      {"B": "multiplies by 2 instead of $2x=4$.", "C": "forgets the inside derivative.", "D": "drops the sign of $g'(4)$."}),
    Q(7, 3, "R3.6", "If $y=\\arctan(\\sqrt x)$, then $\\dfrac{dy}{dx}$ at $x=1$ is",
      ["$\\dfrac14$", "$\\dfrac12$", "$1$", "$\\dfrac\\pi4$"], "A",
      "$\\frac{1}{1+x}\\cdot\\frac{1}{2\\sqrt x}=\\frac12\\cdot\\frac12$.",
      "$\\frac{d}{dx}\\arctan u=\\frac{u'}{1+u^2}$ (R3.6).",
      ["$u=\\sqrt x$, $u^2=x$, $u'=\\frac{1}{2\\sqrt x}$.", "At 1: $\\frac{1}{2}\\cdot\\frac12=\\frac14$."],
      {"B": "forgets the chain factor $u'$.", "C": "drops the $u^2$ in the denominator.", "D": "is $y(1)=\\arctan1$, the value."}),
    Q(8, 4, "R4.4", "The area of a circle increases at $6\\pi$ cm² per second. How fast is the radius increasing when the radius is 3 cm?",
      ["$\\dfrac13$ cm/s", "$1$ cm/s", "$3$ cm/s", "$6\\pi$ cm/s"], "B",
      "$\\frac{dA}{dt}=2\\pi r\\frac{dr}{dt}$: $6\\pi=6\\pi\\frac{dr}{dt}$.",
      "Differentiate $A=\\pi r^2$ with respect to $t$, then substitute (R4.4).",
      ["$\\frac{dA}{dt}=2\\pi r\\frac{dr}{dt}$.", "$6\\pi=2\\pi(3)\\frac{dr}{dt}$, so $\\frac{dr}{dt}=1$."],
      {"A": "uses $2\\pi r^2=18\\pi$ in place of $2\\pi r=6\\pi$.",
       "C": "solves $6\\pi=2\\pi\\frac{dr}{dt}$, dropping the factor $r=3$.",
       "D": "reports the rate of change of the area as the rate for the radius."}),
    Q(9, 4, "R4.9", "$\\displaystyle\\lim_{x\\to0}\\frac{e^{3x}-1}{\\sin x}$ is",
      ["$0$", "$1$", "$3$", "nonexistent"], "C",
      "L'Hôpital: $\\frac{3e^{3x}}{\\cos x}\\to3$.",
      "$\\frac00$, so differentiate top and bottom (R4.9).",
      ["Both tend to 0.", "$\\lim\\frac{3e^{3x}}{\\cos x}=\\frac{3}{1}=3$."],
      {"A": "reads $\\frac00$ as 0.", "B": "forgets the chain factor 3.", "D": "the indeterminate form resolves to 3."}),
    Q(10, 5, "R5.5", "If $f'(x)=x(x-2)^2(x+3)$, then $f$ has a relative maximum at",
      ["$x=-3$", "$x=0$", "$x=2$", "$x=-3$ and $x=2$"], "A",
      "$f'$ changes $+\\to-$ only at $-3$.",
      "First derivative test (R5.5).",
      ["Signs of $f'$: $+$ for $x<-3$, $-$ on $(-3,0)$, $+$ on $(0,2)$ and $(2,\\infty)$.", "Maximum at $-3$; minimum at 0; no extremum at 2."],
      {"B": "is a relative minimum ($-\\to+$).", "C": "$f'$ does not change sign at 2 (squared factor).",
       "D": "includes 2, where there is no sign change."}),
    Q(11, 5, "R5.7", "If $f''(x)=(x-1)(x-4)^2$, the graph of $f$ has points of inflection at",
      ["$x=4$ only", "$x=1$ and $x=4$", "no values of $x$", "$x=1$ only"], "D",
      "$f''$ changes sign at 1 only; the squared factor does not change sign.",
      "Inflection requires a sign change of $f''$ (R5.7).",
      ["$f''<0$ for $x<1$, $>0$ on $(1,4)$ and for $x>4$.", "Only $x=1$."],
      {"A": "$f''(4)=0$ but $f''$ does not change sign there.", "B": "includes 4, where $f''$ keeps its sign.",
       "C": "$f''$ does change sign at 1."}, layout="two"),
    Q(12, 5, "R5.9", "The graph of $f'$ is shown for $0\\le x\\le5$. On which interval is $f$ both decreasing and concave up?",
      ["$(1,2.5)$", "$(1,4)$", "$(4,5)$", "$(2.5,4)$"], "D",
      "$f'<0$ on $(1,4)$; $f'$ increasing on $(2.5,5)$.",
      "Decreasing where $f'<0$; concave up where $f'$ increases (R5.9).",
      ["$f'<0$ between its zeros 1 and 4.", "$f'$ rises after its minimum at 2.5. Both: $(2.5,4)$."],
      {"A": "$f'$ is falling there: concave down.", "B": "includes $(1,2.5)$, where $f$ is concave down.",
       "C": "$f'>0$ there: $f$ is increasing."}, fig=F12, layout="four"),
    Q(13, 6, "R6.2", "The left Riemann sum for $\\int_0^3x^2\\,dx$ with three equal subintervals is",
      ["$5$", "$9$", "$9.5$", "$14$"], "A",
      "$1\\cdot(0+1+4)=5$.",
      "Left endpoints times the width (R6.2).",
      ["Width 1; left endpoints 0, 1, 2.", "$0^2+1^2+2^2=5$."],
      {"B": "is the exact integral.", "C": "is the trapezoidal sum.", "D": "is the right sum $1+4+9$."}),
    Q(14, 6, "R6.4", "If $F(x)=\\displaystyle\\int_0^{2x}\\sin(t^2)\\,dt$, then $F'(x)=$",
      ["$\\sin(4x^2)$", "$2\\sin(2x^2)$", "$4x\\cos(4x^2)$", "$2\\sin(4x^2)$"], "D",
      "$\\sin((2x)^2)\\cdot2$.",
      "FTC with a variable upper limit: $f(u)u'$ (R6.4).",
      ["$u=2x$, $u'=2$.", "$F'(x)=\\sin(4x^2)\\cdot2$."],
      {"A": "forgets the chain factor 2.", "B": "squares only $x$, not $2x$.", "C": "differentiates the integrand instead of evaluating it."}, layout="four"),
    Q(15, 6, "R6.9", "$\\displaystyle\\int_0^{\\pi/4}\\tan x\\sec^2x\\,dx=$",
      ["$\\dfrac14$", "$\\dfrac12$", "$1$", "$\\dfrac{\\sqrt2}{2}$"], "B",
      "$u=\\tan x$: $\\int_0^1u\\,du=\\frac12$.",
      "Substitute and change the limits (R6.9).",
      ["$u=\\tan x$, $du=\\sec^2x\\,dx$, limits $0\\to1$.", "$\\int_0^1u\\,du=\\frac12$."],
      {"A": "integrates $u$ as $\\frac{u^2}{4}$.", "C": "integrates $u$ as $u$.", "D": "uses $\\sin\\frac\\pi4$ from a mistaken antiderivative."}),
    Q(16, 6, "R6.11", "$\\displaystyle\\int x\\ln x\\,dx=$",
      ["$x\\ln x-x+C$", "$\\dfrac{x^2}{2}\\ln x+\\dfrac{x^2}{4}+C$", "$\\ln x+1+C$", "$\\dfrac{x^2}{2}\\ln x-\\dfrac{x^2}{4}+C$"], "D",
      "Parts: $u=\\ln x$, $dv=x\\,dx$.",
      "Integration by parts with $u=\\ln x$ (LIATE) (R6.11).",
      ["$v=\\frac{x^2}{2}$, $du=\\frac{dx}{x}$.", "$\\frac{x^2}{2}\\ln x-\\int\\frac{x}{2}\\,dx=\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}+C$."],
      {"A": "is $\\int\\ln x\\,dx$.", "B": "sign error in $uv-\\int v\\,du$.", "C": "is the derivative of $x\\ln x$, not an antiderivative."}, layout="two"),
    Q(17, 6, "R6.12", "$\\displaystyle\\int_2^3\\frac{dx}{x^2-1}=$",
      ["$\\dfrac12\\ln\\dfrac32$", "$\\ln\\dfrac32$", "$\\dfrac12\\ln2$", "$\\ln\\dfrac43$"], "A",
      "$\\frac{1}{x^2-1}=\\frac12\\left(\\frac{1}{x-1}-\\frac{1}{x+1}\\right)$.",
      "Partial fractions (R6.12).",
      ["Antiderivative: $\\frac12\\ln\\left|\\frac{x-1}{x+1}\\right|$.", "$\\frac12\\left(\\ln\\frac12-\\ln\\frac13\\right)=\\frac12\\ln\\frac32$."],
      {"B": "forgets the coefficient $\\frac12$.", "C": "keeps only $\\frac12\\ln|x-1|$.", "D": "keeps only $\\ln|x+1|$ terms."}),
    Q(18, 6, "R6.13", "$\\displaystyle\\int_1^\\infty xe^{-x^2}\\,dx$ is",
      ["$\\dfrac{1}{2e}$", "$\\dfrac1e$", "$\\dfrac12$", "divergent"], "A",
      "$\\lim_{b\\to\\infty}\\left[-\\frac12e^{-x^2}\\right]_1^b=\\frac{1}{2e}$.",
      "Improper integral as a limit, with $u=x^2$ (R6.13).",
      ["Antiderivative $-\\frac12e^{-x^2}$.", "$0-\\left(-\\frac12e^{-1}\\right)=\\frac{1}{2e}$."],
      {"B": "drops the $\\frac12$ from the substitution.", "C": "evaluates at the lower limit 0 instead of 1.", "D": "the integrand decays fast; the limit is finite."}),
    Q(19, 7, "R7.4", "Let $y=f(x)$ solve $\\dfrac{dy}{dx}=xy$ with $f(0)=2$. Euler's method with two steps of size $0.5$ gives which approximation of $f(1)$?",
      ["$2$", "$2.25$", "$2.5$", "$3$"], "C",
      "Slope 0 at $(0,2)$; slope $1$ at $(0.5,2)$: $2+0.5$.",
      "Euler: slope at the current point times the step (R7.4).",
      ["At $(0,2)$: slope 0, so $f(0.5)\\approx2$.", "At $(0.5,2)$: slope $1$, so $f(1)\\approx2+0.5(1)=2.5$."],
      {"A": "stops after the first step.", "B": "uses the slope $0.5$ in the second step (forgets $y=2$).", "D": "uses one step of size 1 with the slope at $x=1$."}),
    Q(20, 7, "R7.6", "The solution of $\\dfrac{dy}{dx}=y\\cos x$ with $y(0)=3$ is",
      ["$y=e^{\\sin x}+2$", "$y=3e^{\\cos x}$", "$y=3+\\sin x$", "$y=3e^{\\sin x}$"], "D",
      "$\\ln|y|=\\sin x+C$; $y(0)=3$ gives $y=3e^{\\sin x}$.",
      "Separate, integrate, use the initial condition (R7.5–R7.6).",
      ["$\\frac{dy}{y}=\\cos x\\,dx$, so $\\ln|y|=\\sin x+C$.", "$y=Ae^{\\sin x}$ and $A=3$."],
      {"A": "adds the constant after exponentiating.", "B": "integrates $\\cos x$ as $\\cos x$.", "C": "integrates only the right side."}, layout="four"),
    Q(21, 8, "R8.4", "The area of the region enclosed by $y=4-x^2$ and $y=x+2$ is",
      ["$\\dfrac76$", "$\\dfrac32$", "$\\dfrac{10}{3}$", "$\\dfrac92$"], "D",
      "Intersections $x=-2,1$; $\\int_{-2}^1(2-x-x^2)\\,dx$.",
      "Top minus bottom between the intersections (R8.4).",
      ["$4-x^2=x+2$ gives $x^2+x-2=0$, $x=-2$ or $1$.", "$\\int_{-2}^1(2-x-x^2)\\,dx=\\frac76+\\frac{10}{3}=\\frac92$."],
      {"A": "uses only $[0,1]$.", "B": "uses the wrong roots $-1$ and $2$.", "C": "uses only $[-2,0]$."}),
    Q(22, 9, "R9.1", "For $x=e^t$, $y=t^2+1$, the value of $\\dfrac{dy}{dx}$ at $t=1$ is",
      ["$\\dfrac2e$", "$\\dfrac e2$", "$2$", "$2e$"], "A",
      "$\\frac{2t}{e^t}$ at 1.",
      "$\\frac{dy}{dx}=\\frac{y'(t)}{x'(t)}$ (R9.1).",
      ["$y'=2t=2$, $x'=e^t=e$.", "$\\frac{2}{e}$."],
      {"B": "inverts the quotient.", "C": "forgets to divide by $x'(t)$.", "D": "multiplies instead of dividing."}),
    Q(23, 9, "R9.5", "A particle has velocity $\\langle6t,\\,3t^2\\rangle$. How far does it travel for $0\\le t\\le1$?",
      ["$\\sqrt{10}$", "$5\\sqrt5-8$", "$4$", "$5\\sqrt5$"], "B",
      "Speed $3t\\sqrt{4+t^2}$; $\\int_0^1=[(4+t^2)^{3/2}]_0^1$.",
      "Distance is the integral of speed (R9.5).",
      ["Speed $=\\sqrt{36t^2+9t^4}=3t\\sqrt{4+t^2}$.", "$\\int_0^13t\\sqrt{4+t^2}\\,dt=(4+t^2)^{3/2}\\Big|_0^1=5\\sqrt5-8\\approx3.18$."],
      {"A": "is the length of the displacement $\\langle3,1\\rangle$.", "C": "adds the displacement components $3+1$.",
       "D": "drops the lower-limit value 8."}),
    Q(24, 9, "R9.9", "The area of the region enclosed by the polar curve $r=3+2\\cos\\theta$ is",
      ["$\\dfrac{11\\pi}{2}$", "$11\\pi$", "$13\\pi$", "$22\\pi$"], "B",
      "$\\frac12\\int_0^{2\\pi}(9+12\\cos\\theta+4\\cos^2\\theta)\\,d\\theta=\\frac12(18\\pi+4\\pi)$.",
      "$A=\\frac12\\int r^2\\,d\\theta$ over one full trace (R9.9).",
      ["$\\int_0^{2\\pi}\\cos\\theta\\,d\\theta=0$ and $\\int_0^{2\\pi}\\cos^2\\theta\\,d\\theta=\\pi$.", "$\\frac12(18\\pi+4\\pi)=11\\pi$."],
      {"A": "uses $0\\le\\theta\\le\\pi$, half the curve.", "C": "integrates $\\cos^2\\theta$ as $2\\pi$ over a period.", "D": "forgets the $\\frac12$."}),
    Q(25, 10, "R10.2", "$\\displaystyle\\sum_{n=1}^{\\infty}\\frac{4^n}{5^{n+1}}=$",
      ["$\\dfrac{4}{45}$", "$\\dfrac{4}{25}$", "$\\dfrac45$", "$4$"], "C",
      "First term $\\frac{4}{25}$, ratio $\\frac45$: $\\frac{4/25}{1/5}$.",
      "Geometric sum: first term over $1-r$ (R10.2).",
      ["First term ($n=1$): $\\frac{4}{25}$; $r=\\frac45$.", "$\\frac{4/25}{1-4/5}=\\frac45$."],
      {"A": "divides by $1+r$.", "B": "is the first term only.", "D": "uses $\\frac45$ as the first term."}),
    Q(26, 10, "R10.8", "Which series converges?",
      ["$\\displaystyle\\sum\\frac{n!}{5^n}$", "$\\displaystyle\\sum\\frac{n+1}{n}$", "$\\displaystyle\\sum\\frac{1}{n^{1/3}}$", "$\\displaystyle\\sum\\frac{5^n}{n!}$"], "D",
      "Ratio $\\frac{5}{n+1}\\to0<1$.",
      "Ratio test for factorials and powers (R10.8).",
      ["$\\frac{a_{n+1}}{a_n}=\\frac{5}{n+1}\\to0$.", "Converges (to $e^5-1$ from $n=1$)."],
      {"A": "ratio $\\frac{n+1}{5}\\to\\infty$: diverges.", "B": "terms tend to 1: diverges.", "C": "$p=\\frac13\\le1$: diverges."}, layout="four"),
    Q(27, 10, "R10.13", "The interval of convergence of $\\displaystyle\\sum_{n=1}^\\infty\\frac{(x-3)^n}{n\\,5^n}$ is",
      ["$(-2,8)$", "$(-2,8]$", "$[-2,8)$", "$[-2,8]$"], "C",
      "Radius 5 about 3; $x=-2$: AST converges; $x=8$: harmonic diverges.",
      "Ratio test, then both endpoints (R10.13).",
      ["$\\frac{|x-3|}{5}<1$: $-2<x<8$.", "$x=8$: $\\sum\\frac1n$ diverges. $x=-2$: $\\sum\\frac{(-1)^n}{n}$ converges."],
      {"A": "omits $x=-2$.", "B": "reverses the endpoint results.", "D": "includes $x=8$."}, layout="four"),
    Q(28, 10, "R10.12", "$f(0)=1$, $f'(0)=2$, $f''(0)=-6$, $f'''(0)=12$. The third-degree Taylor polynomial for $f$ about $x=0$ is",
      ["$1+2x-6x^2+12x^3$", "$1+2x-3x^2+4x^3$", "$1+2x-6x^2+2x^3$", "$1+2x-3x^2+2x^3$"], "D",
      "Coefficients $\\frac{f^{(k)}(0)}{k!}$: $-\\frac62$, $\\frac{12}{6}$.",
      "Divide each derivative by $k!$ (R10.12).",
      ["$\\frac{-6}{2!}=-3$.", "$\\frac{12}{3!}=2$."],
      {"A": "forgets the factorials.", "B": "divides $f'''$ by 3 instead of $3!$.", "C": "forgets $2!$ in the $x^2$ term."}, layout="two"),
    Q(29, 10, "R10.14", "In the Maclaurin series for $\\cos(2x)$, the coefficient of $x^4$ is",
      ["$-\\dfrac23$", "$\\dfrac{1}{24}$", "$\\dfrac23$", "$\\dfrac43$"], "C",
      "$\\frac{(2x)^4}{4!}=\\frac{16x^4}{24}$.",
      "Substitute $2x$ into the cosine series (R10.14–R10.15).",
      ["$\\cos u=1-\\frac{u^2}{2}+\\frac{u^4}{24}-\\cdots$.", "$\\frac{16}{24}=\\frac23$."],
      {"A": "wrong sign: the $u^4$ term is positive.", "B": "forgets to raise 2 to the fourth power.", "D": "uses $2^4/12$, a wrong factorial."}),
    # ---------------- Part B: calculator ----------------
    Q(30, 1, "R1.16", "How many solutions does $x^5-3x+1=0$ have on $[-2,2]$?",
      ["One", "Two", "Three", "Five"], "C",
      "Graph: zeros near $-1.389$, $0.335$, $1.215$.",
      "Use the calculator's graph and zero finder; continuity guarantees each crossing (R1.15).",
      ["$x^5-3x+1$ changes sign three times on $[-2,2]$.", "Zeros at about $-1.389$, $0.335$, $1.215$."],
      {"A": "finds only one zero; zoom in near $x=0$ to $x=1.3$.", "B": "misses the negative zero.",
       "D": "counts the degree; two of the five roots are not real."}, calc=True),
    Q(31, 3, "R3.5", "Let $f(x)=x^5+x+1$ and $g=f^{-1}$. What is $g'(5)$?",
      ["$0.0003$", "$0.081$", "$1.226$", "$12.309$"], "B",
      "$f(a)=5$ at $a\\approx1.2263$; $g'(5)=\\frac{1}{5a^4+1}$.",
      "Solve $f(a)=b$ with the calculator, then take $\\frac{1}{f'(a)}$ (R3.5).",
      ["Solve $x^5+x+1=5$: $a\\approx1.22634$.", "$f'(a)=5a^4+1\\approx12.309$, so $g'(5)\\approx0.081$."],
      {"A": "uses $\\frac{1}{f'(5)}$.", "C": "is $g(5)=a$.", "D": "forgets the reciprocal."}, calc=True),
    Q(32, 4, "R4.2", "A particle moves on the $x$-axis with velocity $v(t)=t\\sin(t^2)$. Which is true at $t=2$?",
      ["$a(2)\\approx-5.986$, and the speed is increasing", "$a(2)\\approx-5.986$, and the speed is decreasing",
       "$a(2)\\approx-1.514$, and the speed is increasing", "$a(2)\\approx5.986$, and the speed is decreasing"], "A",
      "$v(2)\\approx-1.514<0$ and $a(2)\\approx-5.986<0$: same sign.",
      "Speed increases when $v$ and $a$ share a sign (R4.2).",
      ["$a(t)=\\sin(t^2)+2t^2\\cos(t^2)$; $a(2)\\approx-5.986$.", "$v(2)=2\\sin4\\approx-1.514$: both negative, so the speed increases."],
      {"B": "checks only the sign of $a$.", "C": "reports $v(2)$ as the acceleration.", "D": "sign error in $a(2)$."}, calc=True, layout="one"),
    Q(33, 5, "R5.6", "What is the absolute maximum value of $f(x)=\\sin x+0.3x^2-x$ on $[1,4]$?",
      ["$0.043$", "$0.142$", "$0.174$", "$1.426$"], "C",
      "Critical point $x\\approx1.426$ with $f\\approx0.174$; endpoints give $0.142$ and $0.043$.",
      "Candidates test with the calculator (R5.6).",
      ["$f'(x)=\\cos x+0.6x-1=0$ at $x\\approx1.426$ in $[1,4]$.", "$f(1)\\approx0.142$, $f(1.426)\\approx0.174$, $f(4)\\approx0.043$."],
      {"A": "is $f(4)$, the absolute minimum.", "B": "is $f(1)$, an endpoint value.", "D": "is the $x$-coordinate, not the value."}, calc=True),
    Q(34, 5, "R5.5", "The derivative of $f$ is $f'(x)=e^{\\cos x}-\\frac x2$ for $0<x<6$. At what value of $x$ does $f$ have a relative maximum?",
      ["$1.721$", "$3.142$", "$4.155$", "$5.000$"], "A",
      "$f'$ changes from positive to negative at $x\\approx1.721$ (its only zero in $(0,6)$).",
      "Find the zeros of $f'$ and check the sign change (R5.5).",
      ["Graph $f'$: one zero, at $x\\approx1.721$.", "$f'>0$ before and $<0$ after: relative maximum."],
      {"B": "is where $e^{\\cos x}$ is smallest; $f'(\\pi)<0$ is not zero.", "C": "is where $f''=0$: an inflection point of $f$.",
       "D": "$f'(5)<0$; it is not a critical point."}, calc=True),
    Q(35, 6, "R6.7", "$F(0)=10$ and $F'(t)=\\ln(1+t^2)$. What is $F(3)$?",
      ["$3.406$", "$12.303$", "$13.406$", "$16.908$"], "C",
      "$10+\\int_0^3\\ln(1+t^2)\\,dt\\approx10+3.406$.",
      "Net change: $F(3)=F(0)+\\int_0^3F'$ (R6.7).",
      ["$\\int_0^3\\ln(1+t^2)\\,dt\\approx3.406$.", "$F(3)\\approx13.406$."],
      {"A": "forgets $F(0)$.", "B": "adds the rate $F'(3)=\\ln10$.", "D": "treats the rate as constant at $\\ln10$ for 3 units."}, calc=True),
    Q(36, 6, "R6.4", "For what value of $k$ is $\\displaystyle\\int_0^ke^{-x^2}\\,dx=0.8$?",
      ["$0.472$", "$0.800$", "$1.172$", "$1.609$"], "C",
      "Solve $\\int_0^ke^{-x^2}dx=0.8$ numerically.",
      "Store the integral as a function of its upper limit and solve (R6.4).",
      ["Define $G(k)=\\int_0^ke^{-x^2}dx$.", "$G(k)=0.8$ at $k\\approx1.172$."],
      {"A": "solves $e^{-k^2}=0.8$.", "B": "assumes the integrand is 1.", "D": "solves $\\int_0^ke^{-x}dx=0.8$, giving $\\ln5$."}, calc=True),
    Q(37, 7, "R7.8", "A population satisfies $\\dfrac{dP}{dt}=0.02P\\left(1-\\dfrac{P}{800}\\right)$ with $P(0)=100$, so $P(t)=\\dfrac{800}{1+7e^{-0.02t}}$. What is $P(50)$?",
      ["$223.766$", "$271.828$", "$400.000$", "$800.000$"], "A",
      "$\\frac{800}{1+7e^{-1}}\\approx223.766$.",
      "Evaluate the logistic solution (R7.8).",
      ["$e^{-0.02\\cdot50}=e^{-1}$.", "$\\frac{800}{1+7e^{-1}}\\approx223.766$."],
      {"B": "uses unlimited exponential growth $100e^{1}$.", "C": "is $\\frac L2$, where growth is fastest.", "D": "is the carrying capacity, reached only as $t\\to\\infty$."}, calc=True),
    Q(38, 8, "R8.1", "What is the average value of $f(x)=\\sqrt{1+x^3}$ on $[0,2]$?",
      ["$1.000$", "$1.621$", "$2.000$", "$3.241$"], "B",
      "$\\frac12\\int_0^2\\sqrt{1+x^3}\\,dx\\approx1.621$.",
      "Average value $\\frac{1}{b-a}\\int_a^bf$ (R8.1).",
      ["$\\int_0^2\\sqrt{1+x^3}\\,dx\\approx3.241$.", "Divide by 2: $1.621$."],
      {"A": "is the average rate of change $\\frac{3-1}{2}$.", "C": "averages the endpoint values $\\frac{1+3}{2}$.", "D": "forgets to divide by 2."}, calc=True),
    Q(39, 8, "R8.9", "The region between $y=2\\sin x$ and $y=x$ in the first quadrant is revolved about the $x$-axis. What is the volume?",
      ["$0.842$", "$1.433$", "$2.126$", "$6.678$"], "D",
      "$\\pi\\int_0^{b}(4\\sin^2x-x^2)\\,dx$, $b\\approx1.895$.",
      "Washers: $R=2\\sin x$, $r=x$, square each (R8.9).",
      ["$2\\sin x=x$ at $x=0$ and $b\\approx1.8955$.", "$\\pi\\int_0^b(4\\sin^2x-x^2)\\,dx\\approx6.678$."],
      {"A": "is the area of the region.", "B": "uses $\\pi\\int(R-r)^2$.", "C": "forgets the factor $\\pi$."}, calc=True),
    Q(40, 9, "R9.5", "A particle has $x'(t)=e^{-t}+\\sin(t^2)$ and $x(0)=2$. What is $x(2)$?",
      ["$1.379$", "$1.669$", "$2.865$", "$3.669$"], "D",
      "$2+\\int_0^2(e^{-t}+\\sin t^2)\\,dt\\approx2+1.669$.",
      "Position = initial position + integral of velocity (R9.5).",
      ["$\\int_0^2(e^{-t}+\\sin(t^2))\\,dt\\approx1.669$.", "$x(2)\\approx3.669$."],
      {"A": "adds $x'(2)$ to $x(0)$.", "B": "forgets $x(0)$.", "C": "drops the $\\sin(t^2)$ term."}, calc=True),
    Q(41, 9, "R9.9", "What is the area of the region bounded by $r=2+\\sin(2\\theta)$ for $0\\le\\theta\\le\\frac\\pi2$ and the coordinate axes?",
      ["$2.071$", "$5.534$", "$7.069$", "$11.069$"], "B",
      "$\\frac12\\int_0^{\\pi/2}(2+\\sin2\\theta)^2\\,d\\theta\\approx5.534$.",
      "Polar area $\\frac12\\int r^2$ (R9.9).",
      ["$A=\\frac12\\int_0^{\\pi/2}r^2\\,d\\theta$.", "$\\approx5.534$."],
      {"A": "forgets to square $r$.", "C": "uses $0\\le\\theta\\le\\pi$.", "D": "forgets the $\\frac12$."}, calc=True),
    Q(42, 10, "R10.11", "The second-degree Taylor polynomial for $f$ about $x=1$ is $3-2(x-1)+5(x-1)^2$, and $|f'''(x)|\\le12$ for $1\\le x\\le1.3$. The Lagrange error bound for $|f(1.3)-P_2(1.3)|$ is",
      ["$0.027$", "$0.054$", "$0.162$", "$0.324$"], "B",
      "$\\frac{12}{3!}(0.3)^3=2(0.027)$.",
      "Lagrange: $\\frac{M}{(n+1)!}|x-a|^{n+1}$ (R10.11).",
      ["$M=12$, $n=2$, $|x-a|=0.3$.", "$\\frac{12}{6}(0.027)=0.054$."],
      {"A": "omits $\\frac{M}{3!}$, using $(0.3)^3$ alone.", "C": "uses $2!$ instead of $3!$.", "D": "omits the factorial."}, calc=True),
]
# ---------------- checks (Part B) ----------------
assert len([r for r in sp.Poly(x**5 - 3 * x + 1).nroots() if r.is_real]) == 3
a31 = sp.nsolve(x**5 + x - 4, x, 1.2)
assert abs(1 / (5 * a31**4 + 1) - 0.0812) < 1e-3
assert abs((sp.sin(t**2) + 2 * t**2 * sp.cos(t**2)).subs(t, 2).evalf() + 5.986) < 1e-3
c33 = sp.nsolve(sp.cos(x) + 0.6 * x - 1, x, 1.4)
assert abs((sp.sin(x) + 0.3 * x**2 - x).subs(x, c33) - 0.1736) < 1e-3
assert abs(sp.nsolve(sp.exp(sp.cos(x)) - x / 2, x, 1.7) - 1.721) < 1e-3
assert abs(sp.nsolve(-sp.sin(x) * sp.exp(sp.cos(x)) - sp.Rational(1, 2), x, 4.2) - 4.155) < 1e-3
assert abs((10 + sp.Integral(sp.log(1 + t**2), (t, 0, 3))).evalf() - 13.406) < 1e-3
assert abs(sp.nsolve(sp.Integral(sp.exp(-t**2), (t, 0, x)) - 0.8, x, 1.2) - 1.172) < 1e-3
assert abs(800 / (1 + 7 * math.exp(-1)) - 223.766) < 1e-3
assert abs((sp.Integral(sp.sqrt(1 + x**3), (x, 0, 2)) / 2).evalf() - 1.621) < 1e-3
b39 = sp.nsolve(2 * sp.sin(x) - x, x, 1.9)
assert abs((sp.pi * sp.Integral(4 * sp.sin(x) ** 2 - x**2, (x, 0, b39))).evalf() - 6.678) < 1e-3
assert abs((2 + sp.Integral(sp.exp(-t) + sp.sin(t**2), (t, 0, 2))).evalf() - 3.669) < 1e-3
assert abs((sp.Integral((2 + sp.sin(2 * th)) ** 2, (th, 0, sp.pi / 2)) / 2).evalf() - 5.534) < 1e-3
assert abs(12 / 6 * 0.3**3 - 0.054) < 1e-9

# ---------------- free response ----------------
W, D = 25 * sp.exp(-0.05 * t), 20 + 10 * sp.sin(t / 2)
r1, r2, r3 = (sp.nsolve(W - D, t, g) for g in (0.8, 6.7, 11.3))
Amt = lambda T: (150 + sp.Integral(W - D, (t, 0, T))).evalf()  # noqa: E731
assert abs(sp.Integral(W, (t, 0, 12)).evalf() - 225.594) < 1e-3 and (W - D).subs(t, 6).evalf() < 0
assert abs(r2 - 6.712) < 1e-3 and abs(Amt(r2) - 118.763) < 1e-3 and abs(Amt(12) - 134.798) < 1e-3 and Amt(r1) > 150
assert abs(sp.diff(D, t).subs(t, 4).evalf() + 2.081) < 1e-3
rp = th + sp.sin(2 * th)
assert abs((sp.Integral(rp**2, (th, 0, sp.pi)) / 2).evalf() - 4.382) < 1e-3
assert sp.diff(rp, th).subs(th, sp.pi / 2) == -1
Xp, Yp = rp * sp.cos(th), rp * sp.sin(th)
assert abs((sp.diff(Yp, th) / sp.diff(Xp, th)).subs(th, sp.pi / 2).evalf() - 0.637) < 1e-3
assert [round(float(rp.subs(th, v)), 3) for v in (0, sp.pi / 3, 2 * sp.pi / 3, sp.pi)] == [0.0, 1.913, 1.228, 3.142]
assert (10 + 16) / 2 * 2 + (16 + 22) / 2 * 3 + (22 + 18) / 2 * 3 + (18 + 6) / 2 * 4 == 191
assert (6 - 18) / 4 == -3 and sp.integrate(6 - 2 * (t - 12), (t, 12, 15)) == 9
# FR4 areas: f through (-3,0) (-2,-2) (0,2) (2,2) (4,-2)
gvals = {-3: 6, -1: 4, 3: 10, 4: 9}
assert min(gvals.values()) == 4
ys = sp.Function("y")
s5 = sp.dsolve(sp.Eq(ys(x).diff(x), ys(x) ** 2 * (2 * x + 1)), ys(x), ics={ys(0): -1}).rhs
assert sp.simplify(s5 + 1 / (x**2 + x + 1)) == 0
e = -1.0
for xv in (0.0, 0.1):
    e += 0.1 * e**2 * (2 * xv + 1)
assert abs(e - (-0.8028)) < 1e-9
assert abs(60 * 0.5**4 / 24 - 0.15625) < 1e-12

FRS = [
    FRQ(1, [8, 6, 5], "Water in a tank",
        "A tank holds 150 gallons of water at time $t=0$. For $0\\le t\\le12$ hours, water is pumped into the tank at the rate $W(t)=25e^{-0.05t}$ gallons per hour and drains out at the rate $D(t)=20+10\\sin\\left(\\frac t2\\right)$ gallons per hour.",
        [P("a", "How many gallons of water are pumped into the tank during $0\\le t\\le12$?",
           ["integral $\\int_0^{12}W(t)\\,dt$", "answer $225.594$ gallons"],
           ["$\\int_0^{12}W(t)\\,dt\\approx225.594$ gallons."]),
         P("b", "Is the amount of water in the tank increasing or decreasing at $t=6$? Give a reason for your answer.",
           ["considers $W(6)-D(6)$", "decreasing, because $W(6)-D(6)\\approx-2.891<0$"],
           ["$W(6)-D(6)\\approx-2.891<0$, so the amount of water is decreasing at $t=6$."]),
         P("c", "At what time $t$, $0\\le t\\le12$, is the amount of water in the tank least? Justify your answer.",
           ["sets $W(t)-D(t)=0$ and identifies the candidates (endpoints and $t\\approx6.712$)", "amounts at the candidates: $150$, $\\approx118.763$, $\\approx134.798$", "answer $t\\approx6.712$, with the comparison as justification"],
           ["$A'(t)=W(t)-D(t)=0$ at $t\\approx0.822$, $6.712$, $11.327$. A minimum can occur only at $t=0$, $6.712$ (where $A'$ changes from negative to positive) or $t=12$.",
            "$A(t)=150+\\int_0^t(W-D)\\,dx$: $A(0)=150$, $A(6.712)\\approx118.763$, $A(12)\\approx134.798$.",
            "The least amount is at $t\\approx6.712$ hours."]),
         P("d", "Find $D'(4)$. Using correct units, explain the meaning of this value in context.",
           ["$D'(4)\\approx-2.081$", "interpretation: at $t=4$ the drain rate is decreasing at 2.081 gallons per hour per hour"],
           ["$D'(4)=5\\cos2\\approx-2.081$. At $t=4$ hours, the rate at which water drains is decreasing at 2.081 gallons per hour per hour."])],
        calc=True),
    FRQ(2, [9], "A polar curve",
        "The curve $r=\\theta+\\sin(2\\theta)$ for $0\\le\\theta\\le\\pi$ is drawn in the $xy$-plane.",
        [P("a", "Find the area of the region bounded by the curve and the $x$-axis.",
           ["integral $\\frac12\\int_0^{\\pi}r^2\\,d\\theta$", "answer $4.382$"],
           ["$\\frac12\\int_0^\\pi(\\theta+\\sin2\\theta)^2\\,d\\theta\\approx4.382$."]),
         P("b", "Find $\\frac{dr}{d\\theta}$ at $\\theta=\\frac\\pi2$. Is the point on the curve moving toward or away from the origin as $\\theta$ increases through $\\frac\\pi2$? Explain.",
           ["$\\frac{dr}{d\\theta}=-1$ at $\\frac\\pi2$", "toward the origin, because $r>0$ and $\\frac{dr}{d\\theta}<0$"],
           ["$\\frac{dr}{d\\theta}=1+2\\cos2\\theta=1+2\\cos\\pi=-1$.", "$r(\\frac\\pi2)=\\frac\\pi2>0$ and $r$ is decreasing, so the point is moving toward the origin."]),
         P("c", "Find the slope of the curve at $\\theta=\\frac\\pi2$.",
           ["$\\frac{dy}{d\\theta}$ and $\\frac{dx}{d\\theta}$ (or the polar slope formula)", "slope $\\approx0.637$"],
           ["$\\frac{dy}{d\\theta}=r'\\sin\\theta+r\\cos\\theta=-1$ and $\\frac{dx}{d\\theta}=r'\\cos\\theta-r\\sin\\theta=-\\frac\\pi2$ at $\\frac\\pi2$.",
            "$\\frac{dy}{dx}=\\frac{-1}{-\\pi/2}=\\frac2\\pi\\approx0.637$."]),
         P("d", "Find the greatest distance from the origin to a point on the curve. Justify your answer.",
           ["critical points from $\\frac{dr}{d\\theta}=0$: $\\theta=\\frac\\pi3$ and $\\frac{2\\pi}3$", "values of $r$ at the critical points and endpoints", "answer $\\pi$ (at $\\theta=\\pi$)"],
           ["$\\frac{dr}{d\\theta}=1+2\\cos2\\theta=0$ at $\\theta=\\frac\\pi3,\\frac{2\\pi}{3}$.",
            "$r(0)=0$, $r(\\frac\\pi3)\\approx1.913$, $r(\\frac{2\\pi}3)\\approx1.228$, $r(\\pi)=\\pi$; all are nonnegative, so distance $=r$.",
            "The greatest distance is $\\pi\\approx3.142$."])],
        calc=True),
    FRQ(3, [6, 5, 4], "A car's velocity",
        "A car moves along a straight road. Its velocity $v(t)$, in meters per second, is differentiable; selected values are given in the table.",
        [P("a", "Use a trapezoidal sum with the four subintervals in the table to approximate $\\int_0^{12}v(t)\\,dt$. Explain the meaning of this integral in context.",
           ["trapezoidal sum $191$", "meaning: the distance in meters the car travels from $t=0$ to $t=12$ (velocity is positive)"],
           ["$\\frac{10+16}{2}(2)+\\frac{16+22}{2}(3)+\\frac{22+18}{2}(3)+\\frac{18+6}{2}(4)=26+57+60+48=191$.",
            "It approximates the distance in meters the car travels during $0\\le t\\le12$ seconds (the car moves forward, so displacement is distance)."]),
         P("b", "Must there be a time $t$, $2<t<5$, at which $v(t)=20$? Justify your answer.",
           ["$v$ is continuous because it is differentiable", "$v(2)=16<20<22=v(5)$, so yes by the IVT"],
           ["$v$ is differentiable, hence continuous on $[2,5]$, and $16<20<22$, so by the IVT there is a $t$ in $(2,5)$ with $v(t)=20$."]),
         P("c", "Must there be a time $t$, $8<t<12$, at which the acceleration of the car is $-3$ meters per second per second? Justify your answer.",
           ["$\\frac{v(12)-v(8)}{12-8}=-3$", "yes by the MVT, citing differentiability"],
           ["$\\frac{6-18}{4}=-3$. $v$ is differentiable (so continuous), so by the MVT there is a $t$ in $(8,12)$ with $v'(t)=a(t)=-3$."]),
         P("d", "For $12\\le t\\le15$ the car slows with constant acceleration $-2$ meters per second per second. Find $v(15)$ and the distance the car travels from $t=12$ to $t=15$.",
           ["$v(t)=6-2(t-12)$, so $v(15)=0$", "distance $\\int_{12}^{15}v(t)\\,dt=9$ meters"],
           ["$v(t)=v(12)+\\int_{12}^t(-2)\\,ds=6-2(t-12)$, so $v(15)=0$.", "$v\\ge0$ on $[12,15]$, so the distance is $\\int_{12}^{15}(6-2(t-12))\\,dt=18-9=9$ meters."]),
         P("e", "Using your answer from part (a), estimate the average velocity of the car over $0\\le t\\le12$.",
           ["average velocity $\\approx\\frac{191}{12}\\approx15.917$ m/s"],
           ["$\\frac{1}{12}\\int_0^{12}v(t)\\,dt\\approx\\frac{191}{12}\\approx15.917$ meters per second."])],
        table=T_FR3),
    FRQ(4, [6, 5, 4], "An accumulation function",
        "The continuous function $f$ is defined on $[-3,4]$; its graph consists of four line segments, as shown. Let $g(x)=5+\\int_0^xf(t)\\,dt$.",
        [P("a", "Find $g(-3)$ and $g(4)$.",
           ["$g(-3)=6$", "$g(4)=9$"],
           ["$g(-3)=5-\\int_{-3}^0f=5-(-1+0)=6$ (triangle of area 1 below the axis on $[-3,-2]$; on $[-2,0]$ the areas $-1$ and $+1$ cancel).",
            "$g(4)=5+\\int_0^4f=5+4+0=9$ (rectangle of area 4; on $[2,4]$ the areas $+1$ and $-1$ cancel)."]),
         P("b", "Find the $x$-coordinate of each relative extremum of $g$ on $(-3,4)$ and classify it. Justify your answers.",
           ["relative minimum at $x=-1$: $g'=f$ changes from negative to positive", "relative maximum at $x=3$: $g'=f$ changes from positive to negative"],
           ["$g'=f$. $f$ changes from negative to positive at $x=-1$: relative minimum. $f$ changes from positive to negative at $x=3$: relative maximum."]),
         P("c", "Find the absolute minimum value of $g$ on $[-3,4]$. Justify your answer.",
           ["candidates: $x=-3,-1,3,4$", "values $6$, $4$, $10$, $9$", "absolute minimum $4$ at $x=-1$"],
           ["Candidates: endpoints and critical points $x=-1,3$.", "$g(-3)=6$, $g(-1)=5-\\int_{-1}^0f=5-1=4$, $g(3)=5+4+1=10$, $g(4)=9$.", "The absolute minimum value is $4$."]),
         P("d", "Find $\\displaystyle\\lim_{x\\to3}\\frac{g(x)-10}{(x-3)^2}$.",
           ["shows $\\frac00$ ($g(3)=10$) and applies L'Hôpital's rule", "limit $-1$"],
           ["$g(3)=10$, so the form is $\\frac00$. L'Hôpital: $\\lim\\frac{f(x)}{2(x-3)}$, again $\\frac00$ since $f(3)=0$.",
            "Again: $\\lim\\frac{f'(x)}{2}=\\frac{-2}{2}=-1$ ($f$ has slope $-2$ on $(2,4)$)."])],
        fig=FF4),
    FRQ(5, [7], "A differential equation",
        "Let $y=f(x)$ be the particular solution to $\\dfrac{dy}{dx}=y^2(2x+1)$ with $f(0)=-1$.",
        [P("a", "Write an equation for the line tangent to the graph of $f$ at $x=0$, and use it to approximate $f(0.2)$.",
           ["tangent line $y=-1+x$", "approximation $f(0.2)\\approx-0.8$"],
           ["At $(0,-1)$: $\\frac{dy}{dx}=(1)(1)=1$, so $y=-1+x$ and $f(0.2)\\approx-0.8$."]),
         P("b", "Use Euler's method, starting at $x=0$ with two steps of equal size, to approximate $f(0.2)$.",
           ["first step: $f(0.1)\\approx-0.9$", "second step: $f(0.2)\\approx-0.8028$"],
           ["Step 1: slope $(-1)^2(1)=1$, so $f(0.1)\\approx-1+0.1(1)=-0.9$.",
            "Step 2: slope $(-0.9)^2(1.2)=0.972$, so $f(0.2)\\approx-0.9+0.1(0.972)=-0.8028$."]),
         P("c", "Find $y=f(x)$, the particular solution with $f(0)=-1$.",
           ["separates variables", "antiderivative $-\\frac1y$", "antiderivative $x^2+x$", "uses the initial condition: $C=1$", "solves: $y=-\\frac{1}{x^2+x+1}$"],
           ["$\\frac{dy}{y^2}=(2x+1)\\,dx$, so $-\\frac1y=x^2+x+C$.", "At $(0,-1)$: $1=C$.", "$-\\frac1y=x^2+x+1$, so $y=-\\frac{1}{x^2+x+1}$."])]),
    FRQ(6, [10], "A Taylor polynomial",
        "A function $f$ has derivatives of all orders, with $f(0)=1$, $f'(0)=-2$, $f''(0)=6$, $f'''(0)=-24$, and $|f^{(4)}(x)|\\le60$ for $0\\le x\\le0.5$.",
        [P("a", "Write the third-degree Taylor polynomial $P_3(x)$ for $f$ about $x=0$.",
           ["first two terms $1-2x$", "terms $3x^2-4x^3$"],
           ["$P_3(x)=1-2x+\\frac{6}{2!}x^2-\\frac{24}{3!}x^3=1-2x+3x^2-4x^3$."]),
         P("b", "Use $P_3$ to approximate $f(0.5)$, and use the Lagrange error bound to show that $|f(0.5)-P_3(0.5)|<0.16$.",
           ["$P_3(0.5)=0.25$", "Lagrange form $\\frac{M}{4!}(0.5)^4$ with $M=60$", "bound $0.15625<0.16$"],
           ["$P_3(0.5)=1-1+0.75-0.5=0.25$.", "$|f(0.5)-P_3(0.5)|\\le\\frac{60}{4!}(0.5)^4=\\frac{60}{24}\\cdot\\frac{1}{16}=0.15625<0.16$."]),
         P("c", "Let $g(x)=\\int_0^xf(t)\\,dt$. Write the fourth-degree Taylor polynomial for $g$ about $x=0$.",
           ["integrates term by term", "$x-x^2+x^3-x^4$"],
           ["$\\int_0^x(1-2t+3t^2-4t^3)\\,dt=x-x^2+x^3-x^4$."]),
         P("d", "Let $h(x)=f(x^2)$. Write the first three nonzero terms of the Taylor series for $h$ about $x=0$.",
           ["substitutes $x^2$ for $x$ in the series for $f$", "$1-2x^2+3x^4$"],
           ["Substitute $x^2$ into $1-2x+3x^2-\\cdots$: $1-2x^2+3x^4-\\cdots$."])]),
]
for f in FRS:
    f["pts"] = sum(len(p["rubric"]) for p in f["parts"])
assert [f["pts"] for f in FRS] == [9, 9, 9, 9, 9, 9], [f["pts"] for f in FRS]
