"""Unit 6 Practice Set: Integration and Accumulation of Change (18 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, Table, fig

x, t, n, k = sp.symbols("x t n k", positive=True)

DOC = dict(
    unit=6, title="Integration and Accumulation of Change", topics="6.1–6.14",
    pdf="ap-calc-bc-06-integration-accumulation-practice.pdf", guide_pdf="ap-calc-bc-06-integration-accumulation-guide.pdf",
    sections={"1": "Accumulation and Riemann sums", "2": "Accumulation functions and the FTC",
              "3": "Antiderivatives and the FTC, part 2", "4": "Substitution and algebraic techniques",
              "5": "Integration by parts and partial fractions", "6": "Improper integrals and choosing a technique"},
    rules={"1": "R6.1–R6.3. Multiply each height by its own width. Increasing: left sum under, right sum over. Concave up: trapezoid over.",
           "2": "R6.4–R6.6. $\\frac{d}{dx}\\int_a^{u(x)}f(t)\\,dt=f(u(x))u'(x)$. For $g=\\int_a^xf$: $g'=f$, $g''=f'$, values are signed areas.",
           "3": "R6.7–R6.8. $\\int_a^bf=F(b)-F(a)$; amount at $b$ = amount at $a$ + $\\int_a^b$ rate.",
           "4": "R6.9–R6.10. Substitute $u$ and change the limits; divide improper fractions; complete the square for arctan.",
           "5": "R6.11–R6.12. $\\int u\\,dv=uv-\\int v\\,du$ (LIATE). Distinct linear factors: $\\frac{A}{x-a}+\\frac{B}{x-b}$.",
           "6": "R6.13–R6.14. Improper integrals are limits; $\\int_1^\\infty x^{-p}dx$ converges iff $p>1$, $\\int_0^1x^{-p}dx$ iff $p<1$."},
    abstract="Eighteen exam-style multiple-choice questions on Unit 6, grouped by the sections of the Unit 6 Study Guide, and one nine-point free-response question on an accumulation function defined by a graph. Items marked [calculator] allow a graphing calculator; the rest are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (36 min) and 15 minutes for the free response.",
    setup="Allow 36 minutes for the multiple choice and 15 for the free response. Item 10 needs a graphing calculator.",
)

F5 = fig("u6-q5", r"""\begin{tikzpicture}
\begin{axis}[width=8cm,height=4.4cm,axis lines=middle,xmin=-0.3,xmax=8.5,ymin=-2.6,ymax=3.4,xtick={1,...,8},ytick={-2,-1,1,2,3},xlabel={$t$},ylabel={$f(t)$},grid=major,grid style={gray!25},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[very thick] coordinates{(0,3) (3,0) (5,-2) (7,-2) (8,0)};
\end{axis}\end{tikzpicture}""", "Graph of f on 0 ≤ t ≤ 8 made of segments: from (0,3) down to (3,0), down to (5,−2), level to (7,−2), then up to (8,0).")

FFR = fig("u6-fr", r"""\begin{tikzpicture}
\begin{axis}[width=8.4cm,height=5cm,axis lines=middle,xmin=-2.4,xmax=6.5,ymin=-2.4,ymax=2.6,xtick={-2,-1,1,2,3,4,5,6},ytick={-2,-1,1,2},xlabel={$x$},ylabel={$f(x)$},grid=major,grid style={gray!25},axis equal image,
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[very thick] coordinates{(-2,2) (0,0)};
\addplot[very thick,domain=0:4,samples=120]{-sqrt(max(0,4-(x-2)^2))};
\addplot[very thick] coordinates{(4,0) (6,2)};
\end{axis}\end{tikzpicture}""", "Graph of f on −2 ≤ x ≤ 6: a segment from (−2,2) down to (0,0), a semicircle below the x-axis from (0,0) to (4,0) with center (2,0) and radius 2, and a segment from (4,0) up to (6,2).", width="0.55\\linewidth")

T1 = Table([["$t$ (min)", "0", "3", "5", "9"], ["$r(t)$ (gal/min)", "4", "7", "6", "10"]])

# checks
assert 7 * 3 + 6 * 2 + 10 * 4 == 73 and 3 * (7 + 6 + 10) == 69 and 4 * 3 + 7 * 2 + 6 * 4 == 50
assert sp.Rational(11, 2) * 3 + sp.Rational(13, 2) * 2 + 8 * 4 == sp.Rational(123, 2)
assert sp.limit(sp.summation((1 + 2 * k / n) ** 3 * 2 / n, (k, 1, n)), n, sp.oo) == sp.integrate(x**3, (x, 1, 3)) == 20
xx = sp.symbols("xx")
assert sp.simplify(sp.diff(sp.Integral(sp.sqrt(1 + t**2), (t, 0, xx**3)).doit(), xx) - 3 * xx**2 * sp.sqrt(1 + xx**6)) == 0
# areas under F5 graph
g = {3: sp.Rational(9, 2), 5: sp.Rational(9, 2) - 2, 7: sp.Rational(9, 2) - 2 - 4, 8: sp.Rational(9, 2) - 7}
assert g[5] == sp.Rational(5, 2) and g[7] == sp.Rational(-3, 2)
assert -(2 * 5 + 2) == -12  # int_3^1 (2f+1) with int_1^3 f = 8 - 3
assert 50 + sp.integrate(6 * t - t**2, (t, 0, 3)) == 68
assert sp.integrate(sp.sin(x) + 2 * x, (x, 0, sp.pi / 2)) == 1 + sp.pi**2 / 4
assert abs(1 + float(sp.Integral(sp.exp(-x**2), (x, 0, 2)).evalf()) - 1.882) < 5e-4
assert sp.integrate(x / (x**2 + 1), (x, 0, 1)) == sp.log(2) / 2
assert sp.integrate(sp.sin(x) ** 3 * sp.cos(x), (x, 0, sp.pi / 2)) == sp.Rational(1, 4)
assert sp.simplify(sp.diff(sp.atan(x + 3), x) - 1 / (x**2 + 6 * x + 10)) == 0
assert sp.simplify(sp.integrate(x * sp.exp(2 * x), x) - (x / 2 - sp.Rational(1, 4)) * sp.exp(2 * x)) == 0
assert sp.integrate(sp.log(x), (x, 1, sp.E)) == 1
assert sp.apart((x + 7) / ((x - 1) * (x + 3))) == 2 / (x - 1) - 1 / (x + 3)
assert sp.simplify(sp.integrate(1 / (x * sp.log(x) ** 2), (x, 2, sp.oo)) - 1 / sp.log(2)) == 0

QS = [
    Q(1, 1, "R6.2", "Water flows into a tank at rate $r(t)$ gallons per minute; selected values are in the table. Using a right Riemann sum with the three subintervals given by the table, the estimate of $\\int_0^9 r(t)\\,dt$ is",
      ["$50$", "$61.5$", "$69$", "$73$"], "D",
      "$7(3)+6(2)+10(4)=73$.",
      "A right sum multiplies each right-endpoint value by its own subinterval width (R6.2).",
      ["Widths: 3, 2, 4. Right endpoints: $r(3)=7$, $r(5)=6$, $r(9)=10$.", "$7\\cdot3+6\\cdot2+10\\cdot4=21+12+40=73$."],
      {"A": "is the left sum: $4(3)+7(2)+6(4)$.",
       "B": "is the trapezoidal sum.",
       "C": "uses width 3 for every subinterval; the widths are unequal."}, table=T1),
    Q(2, 1, "R6.2", "$f$ is increasing and concave down on $[0,4]$. Let $L$, $R$ and $T$ be the left, right and trapezoidal sums for $\\int_0^4 f(x)\\,dx$ with four equal subintervals, and $I$ the integral. Which ordering is correct?",
      ["$L<T<I<R$", "$L<I<T<R$", "$R<T<I<L$", "$T<L<I<R$"], "A",
      "Increasing: $L<I<R$. Concave down: $T<I$. And $T=\\frac{L+R}{2}>L$.",
      "Monotonicity decides left versus right; concavity decides the trapezoid (R6.2).",
      ["Increasing: left rectangles sit under the curve, right rectangles above: $L<I<R$.",
       "Concave down: chords lie under the curve, so $T<I$; $T$ is the average of $L$ and $R$, so $L<T$."],
      {"B": "puts the trapezoid above the integral, true for concave up, not concave down.",
       "C": "is the ordering for a decreasing function.",
       "D": "$T=\\frac{L+R}{2}$ is always between $L$ and $R$."}, layout="four"),
    Q(3, 1, "R6.3", "$\\displaystyle\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\left(1+\\frac{2k}{n}\\right)^3\\frac{2}{n}$ is equal to",
      ["$\\displaystyle\\int_0^2x^3\\,dx$", "$\\displaystyle\\int_1^3x^3\\,dx$", "$\\displaystyle\\int_1^2x^3\\,dx$", "$\\displaystyle2\\int_1^3x^3\\,dx$"], "B",
      "$\\Delta x=\\frac2n$, $x_k=1+\\frac{2k}{n}$ runs from 1 to 3.",
      "Read $\\Delta x$, then the starting point $a$, then $b=a+$ total width (R6.3).",
      ["$\\Delta x=\\frac2n$ and $x_k=1+k\\Delta x$, so $a=1$ and $b=1+2=3$.", "The sum is a right Riemann sum for $\\int_1^3x^3\\,dx$ (which equals 20)."],
      {"A": "drops the shift: with $a=0$ the function would be $(1+x)^3$, not $x^3$.",
       "C": "uses $b=2$; the width of the interval is 2, so $b=3$.",
       "D": "counts the factor 2 twice; it is already in $\\Delta x$."}, layout="four"),
    Q(4, 2, "R6.4", "$\\dfrac{d}{dx}\\displaystyle\\int_0^{x^3}\\sqrt{1+t^2}\\,dt=$",
      ["$\\sqrt{1+x^6}$", "$3x^2\\sqrt{1+x^2}$", "$\\sqrt{1+x^6}-1$", "$3x^2\\sqrt{1+x^6}$"], "D",
      "$f(u)u'=\\sqrt{1+x^6}\\cdot3x^2$.",
      "FTC part 1 with the chain rule (R6.4).",
      ["$f(t)=\\sqrt{1+t^2}$ evaluated at $u=x^3$: $\\sqrt{1+x^6}$.", "Times $u'=3x^2$."],
      {"A": "forgets the chain factor $3x^2$.",
       "B": "multiplies by $3x^2$ but evaluates $f$ at $x$ instead of $x^3$.",
       "C": "subtracts $f(0)$, as if evaluating an antiderivative; FTC part 1 has no such term."}, layout="four"),
    Q(5, 2, "R6.5", "The graph of $f$ is shown. If $g(x)=\\int_0^x f(t)\\,dt$, then $g(5)=$",
      ["$-1.5$", "$2.5$", "$4.5$", "$6.5$"], "B",
      "Area $4.5$ above, minus $2$ below on $[3,5]$.",
      "Accumulation values are signed areas (R6.5).",
      ["On $[0,3]$: triangle above, area $\\frac12(3)(3)=4.5$.", "On $[3,5]$: triangle below, area $\\frac12(2)(2)=2$. $g(5)=4.5-2=2.5$."],
      {"A": "is $g(7)$.",
       "C": "is $g(3)$.",
       "D": "adds the area below the axis instead of subtracting it."}, fig=F5),
    Q(6, 2, "R6.5", "For the same $g$, on which interval is $g$ both decreasing and concave down?",
      ["$(0,3)$", "$(5,7)$", "$(7,8)$", "$(3,5)$"], "D",
      "$g'=f<0$ on $(3,8)$; $g''=f'<0$ on $(0,5)$.",
      "$g$ decreases where $f<0$ and is concave down where $f$ decreases (R6.5).",
      ["$f<0$ on $(3,8)$: $g$ decreasing.", "$f$ decreasing on $(0,5)$: $g$ concave down. Both: $(3,5)$."],
      {"A": "$g$ is increasing there ($f>0$).",
       "B": "$f$ is constant there: $g''=0$, so $g$ is linear, not concave down.",
       "C": "$f$ is increasing there: $g$ is concave up."}),
    Q(7, 2, "R6.6", "If $\\int_1^5 f(x)\\,dx=8$ and $\\int_3^5 f(x)\\,dx=3$, then $\\int_3^1\\big(2f(x)+1\\big)\\,dx=$",
      ["$-12$", "$-11$", "$-10$", "$12$"], "A",
      "$\\int_1^3f=5$; reversed and doubled: $-10$; plus $\\int_3^1 1\\,dx=-2$.",
      "Additivity, reversing limits, and linearity (R6.6).",
      ["$\\int_1^3f=8-3=5$, so $\\int_3^1 2f=-10$.", "$\\int_3^1 1\\,dx=-(3-1)=-2$. Total $-12$."],
      {"B": "integrates the constant 1 as $-1$ instead of as the signed length $-2$.",
       "C": "drops the constant term $\\int_3^1 1\\,dx=-2$.",
       "D": "ignores the reversed limits."}),
    Q(8, 3, "R6.7", "A tank holds 50 liters at $t=0$. Water flows in at $r(t)=6t-t^2$ liters per hour for $0\\le t\\le3$. How many liters are in the tank at $t=3$?",
      ["$18$", "$59$", "$68$", "$86$"], "C",
      "$50+\\int_0^3(6t-t^2)\\,dt=50+18$.",
      "Amount at $b$ = amount at $a$ + $\\int_a^b$ rate (R6.7).",
      ["$\\int_0^3(6t-t^2)\\,dt=[3t^2-\\frac{t^3}{3}]_0^3=27-9=18$.", "$50+18=68$."],
      {"A": "forgets the initial 50 liters.",
       "B": "adds the rate $r(3)=9$ instead of the accumulated amount.",
       "D": "integrates $-t^2$ as $+\\frac{t^3}{3}$."}),
    Q(9, 3, "R6.8", "$\\displaystyle\\int_0^{\\pi/2}(\\sin x+2x)\\,dx=$",
      ["$-1+\\dfrac{\\pi^2}{4}$", "$\\dfrac{\\pi^2}{4}$", "$1+\\dfrac{\\pi^2}{2}$", "$1+\\dfrac{\\pi^2}{4}$"], "D",
      "$[-\\cos x+x^2]_0^{\\pi/2}=(0+\\frac{\\pi^2}{4})-(-1)$.",
      "Antiderivatives: $\\int\\sin x=-\\cos x$, $\\int2x=x^2$; then FTC part 2 (R6.7–R6.8).",
      ["$F(x)=-\\cos x+x^2$.", "$F(\\frac\\pi2)-F(0)=\\frac{\\pi^2}{4}-(-1)=1+\\frac{\\pi^2}{4}$."],
      {"A": "uses $\\int\\sin x\\,dx=\\cos x$.",
       "B": "drops the lower-limit value $-\\cos0=-1$.",
       "C": "integrates $2x$ as $2x^2$."}, layout="four"),
    Q(10, 3, "R6.7", "$F'(x)=e^{-x^2}$ and $F(0)=1$. What is $F(2)$?",
      ["$0.882$", "$1.018$", "$1.882$", "$3.000$"], "C",
      "$F(2)=1+\\int_0^2e^{-x^2}dx\\approx1+0.882$.",
      "Net change with a calculator: $F(2)=F(0)+\\int_0^2F'(x)\\,dx$ (R6.7).",
      ["$\\int_0^2e^{-x^2}dx\\approx0.882$ (calculator).", "$F(2)\\approx1.882$."],
      {"A": "forgets the initial value $F(0)=1$.",
       "B": "adds $F'(2)=e^{-4}\\approx0.018$ instead of the integral.",
       "D": "assumes the rate stays at $F'(0)=1$ for all 2 units: $1+1\\cdot2$; the rate decreases."}, calc=True),
    Q(11, 4, "R6.9", "$\\displaystyle\\int_0^1\\frac{x}{x^2+1}\\,dx=$",
      ["$\\dfrac{\\pi}{4}$", "$\\dfrac12\\ln2$", "$\\ln2$", "$2\\ln2$"], "B",
      "$u=x^2+1$: $\\frac12\\int_1^2\\frac{du}{u}=\\frac12\\ln2$.",
      "The derivative of the denominator is present (up to a constant): substitute (R6.9).",
      ["$u=x^2+1$, $du=2x\\,dx$, limits $1\\to2$.", "$\\frac12\\int_1^2\\frac{du}u=\\frac12\\ln2$."],
      {"A": "uses $\\arctan$; that needs $\\frac{1}{x^2+1}$ without the $x$.",
       "C": "forgets the factor $\\frac12$ from $du=2x\\,dx$.",
       "D": "multiplies by 2 instead of dividing."}),
    Q(12, 4, "R6.9", "$\\displaystyle\\int_0^{\\pi/2}\\sin^3x\\cos x\\,dx=$",
      ["$-\\dfrac14$", "$\\dfrac14$", "$\\dfrac13$", "$\\dfrac{\\pi^4}{64}$"], "B",
      "$u=\\sin x$: $\\int_0^1u^3\\,du=\\frac14$.",
      "Substitute and change the limits (R6.9).",
      ["$u=\\sin x$, $du=\\cos x\\,dx$; $x=0\\to u=0$, $x=\\frac\\pi2\\to u=1$.", "$\\int_0^1u^3\\,du=\\frac14$."],
      {"A": "takes $du=-\\cos x\\,dx$, the derivative of $\\cos$, not $\\sin$.",
       "C": "integrates $u^3$ as $\\frac{u^3}{3}$.",
       "D": "keeps the $x$-limits after substituting: $\\frac14(\\frac\\pi2)^4$."}),
    Q(13, 4, "R6.10", "$\\displaystyle\\int\\frac{dx}{x^2+6x+10}=$",
      ["$\\ln(x^2+6x+10)+C$", "$\\dfrac12\\arctan\\dfrac{x+3}{2}+C$", "$\\arctan(x+3)+C$", "$-\\dfrac{1}{x+3}+C$"], "C",
      "$x^2+6x+10=(x+3)^2+1$.",
      "Complete the square, then $\\int\\frac{du}{u^2+1}=\\arctan u$ (R6.10).",
      ["$x^2+6x+10=(x+3)^2+1$.", "With $u=x+3$: $\\int\\frac{du}{u^2+1}=\\arctan(x+3)+C$."],
      {"A": "would need the numerator $2x+6$.",
       "B": "completes the square as $(x+3)^2+4$; the constant is $10-9=1$.",
       "D": "drops the $+1$, integrating $\\frac{1}{(x+3)^2}$."}, layout="two"),
    Q(14, 5, "R6.11", "$\\displaystyle\\int xe^{2x}\\,dx=$",
      ["$\\dfrac{x}{2}e^{2x}-\\dfrac14e^{2x}+C$", "$xe^{2x}-e^{2x}+C$", "$\\dfrac{x}{2}e^{2x}+\\dfrac14e^{2x}+C$", "$\\dfrac{x^2}{4}e^{2x}+C$"], "A",
      "Parts: $u=x$, $dv=e^{2x}dx$, $v=\\frac12e^{2x}$.",
      "Integration by parts, $u$ = algebraic (LIATE) (R6.11).",
      ["$\\int xe^{2x}dx=\\frac x2e^{2x}-\\int\\frac12e^{2x}dx$.", "$=\\frac x2e^{2x}-\\frac14e^{2x}+C$."],
      {"B": "uses $v=e^{2x}$, forgetting the $\\frac12$.",
       "C": "sign error in $uv-\\int v\\,du$.",
       "D": "integrates each factor separately; the integral of a product is not the product of integrals."}, layout="two"),
    Q(15, 5, "R6.11", "$\\displaystyle\\int_1^e\\ln x\\,dx=$",
      ["$0$", "$1$", "$e-1$", "$e$"], "B",
      "$[x\\ln x-x]_1^e=(e-e)-(0-1)=1$.",
      "Parts with $u=\\ln x$, $dv=dx$ (R6.11).",
      ["$\\int\\ln x\\,dx=x\\ln x-\\int x\\cdot\\frac1x\\,dx=x\\ln x-x$.", "$(e\\cdot1-e)-(1\\cdot0-1)=0+1=1$."],
      {"A": "drops the lower-limit term $-(0-1)$.",
       "C": "integrates $\\ln x$ as if it were 1 on $[1,e]$.",
       "D": "forgets the $-x$ term: $[x\\ln x]_1^e=e$."}),
    Q(16, 5, "R6.12", "$\\displaystyle\\int\\frac{x+7}{(x-1)(x+3)}\\,dx=$",
      ["$2\\ln|x-1|-\\ln|x+3|+C$", "$2\\ln|x-1|+\\ln|x+3|+C$", "$-\\ln|x-1|+2\\ln|x+3|+C$", "$\\ln|x^2+2x-3|+C$"], "A",
      "$A=\\frac{8}{4}=2$, $B=\\frac{4}{-4}=-1$.",
      "Partial fractions by covering each factor (R6.12).",
      ["$\\frac{x+7}{(x-1)(x+3)}=\\frac{A}{x-1}+\\frac{B}{x+3}$.", "$A=\\frac{1+7}{1+3}=2$; $B=\\frac{-3+7}{-3-1}=-1$."],
      {"B": "sign error in $B$.",
       "C": "swaps the two coefficients.",
       "D": "would need the numerator to be the derivative $2x+2$."}, layout="two"),
    Q(17, 6, "R6.13", "$\\displaystyle\\int_2^\\infty\\frac{dx}{x(\\ln x)^2}$ is",
      ["$\\ln2$", "$\\dfrac{1}{2\\ln2}$", "$\\dfrac{1}{\\ln2}$", "divergent"], "C",
      "$u=\\ln x$: $\\int_{\\ln2}^\\infty u^{-2}du=\\frac{1}{\\ln2}$.",
      "Write the improper integral as a limit, substituting $u=\\ln x$ (R6.9, R6.13).",
      ["$\\lim_{b\\to\\infty}\\int_2^b\\frac{dx}{x\\ln^2x}=\\lim_{b\\to\\infty}\\left[-\\frac{1}{\\ln x}\\right]_2^b$.", "$=0+\\frac{1}{\\ln2}$."],
      {"A": "inverts the answer.",
       "B": "adds a spurious factor $\\frac12$, as if integrating $u^{-3}$.",
       "D": "compares with $\\frac1x$, but the extra $\\ln^2x$ makes the integral converge."}),
    Q(18, 6, "R6.13", "Which of the following improper integrals converge? $$\\text{I. }\\int_1^\\infty\\frac{dx}{\\sqrt x}\\qquad\\text{II. }\\int_0^1\\frac{dx}{\\sqrt x}\\qquad\\text{III. }\\int_0^\\infty e^{-x}\\,dx$$",
      ["I only", "II only", "II and III only", "I, II and III"], "C",
      "II is $p=\\frac12<1$ near 0 (value 2); III equals 1; I is $p=\\frac12\\le1$ at infinity.",
      "$p$-integrals: at infinity need $p>1$; near 0 need $p<1$ (R6.13).",
      ["I: $\\int_1^b x^{-1/2}dx=2\\sqrt b-2\\to\\infty$: diverges.", "II: $\\lim_{a\\to0^+}(2-2\\sqrt a)=2$. III: $\\lim_{b\\to\\infty}(1-e^{-b})=1$."],
      {"A": "I diverges ($p=\\frac12\\le1$ at infinity).",
       "B": "III also converges, to 1.",
       "D": "I diverges."}, layout="four"),
]


# FRQ: g(x) = 3 + int_0^x f
gv = {-2: 3 - 2, 0: 3, 4: 3 - 2 * sp.pi, 6: 3 - 2 * sp.pi + 2}
assert max(gv.values(), key=float) == 3 and float(gv[6]) < 0

FRS = [
    FRQ(1, [2], "An accumulation function from a graph",
        "The graph of a continuous function $f$ on $[-2,6]$ consists of two line segments and a semicircle, as shown. Let $g(x)=3+\\int_0^x f(t)\\,dt$.",
        [P("a", "Find $g(-2)$ and $g(4)$.",
           ["$g(-2)=1$", "$g(4)=3-2\\pi$"],
           ["$g(-2)=3+\\int_0^{-2}f=3-\\int_{-2}^0f=3-2=1$ (triangle of area 2).",
            "$g(4)=3+\\int_0^4f=3-2\\pi$ (semicircle of radius 2 below the axis, area $2\\pi$)."]),
         P("b", "Find the $x$-coordinate of each relative extremum of $g$ on $(-2,6)$ and classify it. Justify your answers.",
           ["relative maximum at $x=0$ because $g'=f$ changes from positive to negative", "relative minimum at $x=4$ because $g'=f$ changes from negative to positive"],
           ["$g'(x)=f(x)$. $f>0$ on $(-2,0)$ and $f<0$ on $(0,4)$: relative maximum at $x=0$.",
            "$f<0$ on $(0,4)$ and $f>0$ on $(4,6)$: relative minimum at $x=4$."]),
         P("c", "Find the absolute maximum value of $g$ on $[-2,6]$. Justify your answer.",
           ["considers the candidates $x=-2,0,4,6$", "$g(6)=5-2\\pi$ and the other values", "absolute maximum 3 at $x=0$, with the comparison"],
           ["Candidates: endpoints and critical points $x=0,4$.",
            "$g(-2)=1$, $g(0)=3$, $g(4)=3-2\\pi\\approx-3.28$, $g(6)=3-2\\pi+2=5-2\\pi\\approx-1.28$.",
            "The absolute maximum value is $g(0)=3$."]),
         P("d", "Find the $x$-coordinate of each point of inflection of the graph of $g$ on $(-2,6)$. Justify your answer.",
           ["$x=2$", "reason: $g''=f'$ changes sign ($f$ changes from decreasing to increasing) at $x=2$"],
           ["$g''=f'$. $f$ decreases on $(-2,2)$ and increases on $(2,6)$, so $g''$ changes sign only at $x=2$: the only inflection point."])],
        fig=FFR),
]
