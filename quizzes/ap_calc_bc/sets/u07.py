"""Unit 7 Practice Set: Differential Equations (12 MC + 1 FRQ)."""
import math

import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, fig

x, t = sp.symbols("x t")
y = sp.Function("y")

DOC = dict(
    unit=7, title="Differential Equations", topics="7.1–7.9",
    pdf="ap-calc-bc-07-differential-equations-practice.pdf", guide_pdf="ap-calc-bc-07-differential-equations-guide.pdf",
    sections={"1": "Modeling and verifying solutions", "2": "Slope fields", "3": "Euler's method",
              "4": "Separation of variables", "5": "Exponential and logistic models"},
    rules={"1": "R7.1–R7.2. “Proportional to $X$” means $\\frac{dy}{dt}=kX$. Verify by substituting the function and its derivatives.",
           "2": "R7.3. Slopes constant along verticals: depends on $x$ only; along horizontals: $y$ only. Check signs and zero slopes.",
           "3": "R7.4. $y_{\\text{new}}=y+\\Delta x\\cdot\\frac{dy}{dx}$ at the current point; concave up solutions are underestimated.",
           "4": "R7.5–R7.6. Separate, integrate both sides, use the initial condition at once, then solve for $y$.",
           "5": "R7.7–R7.8. $y=y_0e^{kt}$. Logistic $\\frac{dP}{dt}=kP(1-\\frac PL)$: limit $L$, fastest growth at $\\frac L2$."},
    abstract="Twelve exam-style multiple-choice questions on Unit 7, grouped by the sections of the Unit 7 Study Guide, and one nine-point free-response question on a separable differential equation. Items marked [calculator] allow a graphing calculator; the rest are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (24 min) and 15 minutes for the free response.",
    setup="Allow 24 minutes for the multiple choice and 15 for the free response. Item 11 needs a graphing calculator.",
)

F3 = fig("u7-q3", r"""\begin{tikzpicture}
\begin{axis}[width=6cm,height=6cm,axis lines=middle,xmin=-2.6,xmax=2.6,ymin=-2.6,ymax=2.6,xtick={-2,-1,1,2},ytick={-2,-1,1,2},xlabel={$x$},ylabel={$y$},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\foreach \i in {-2,...,2}{\foreach \j in {-2,...,2}{
  \pgfmathsetmacro{\m}{\i-\j}
  \pgfmathsetmacro{\dx}{0.28/sqrt(1+\m*\m)}
  \edef\temp{\noexpand\addplot[thick,domain=\i-\dx:\i+\dx,samples=2]{\j+\m*(x-\i)};}\temp
}}
\end{axis}\end{tikzpicture}""", "Slope field on the grid −2 to 2: segments are horizontal along the line y = x, slopes are positive below that line and negative above it, and slopes along each diagonal parallel to y = x are equal.", width="0.36\\linewidth")

# checks
assert sp.simplify(sp.diff(sp.sin(2 * x), x, 2) + 4 * sp.sin(2 * x)) == 0
yy = 3.0
for xv in (1.0, 1.5):
    yy += 0.5 * (2 * xv - yy)
assert abs(yy - 2.75) < 1e-12
assert abs(2.5 + 0.5 * (2 * 2 - 2.5) - 3.25) < 1e-12
sol = sp.dsolve(sp.Eq(y(x).diff(x), 2 * x * y(x) ** 2), y(x), ics={y(0): 1})
assert sp.simplify(sol.rhs - 1 / (1 - x**2)) == 0
assert 200 * 2**3 == 1600
assert abs(20 + 70 * math.exp(-1) - 45.75) < 0.01 and abs(70 * math.exp(-1) - 25.75) < 0.01 and abs(90 * math.exp(-1) - 33.11) < 0.01
s7 = sp.dsolve(sp.Eq(y(x).diff(x), x * y(x)), y(x)).rhs
assert sp.simplify(s7.diff(x) - x * s7) == 0

QS = [
    Q(1, 1, "R7.1", "A rumor spreads through a school of 500 students. The rate at which the number $y$ who have heard it increases is proportional to the product of the number who have heard it and the number who have not. Which equation models this?",
      ["$\\dfrac{dy}{dt}=ky(500-y)$", "$\\dfrac{dy}{dt}=k(500-y)$", "$\\dfrac{dy}{dt}=ky$", "$\\dfrac{dy}{dt}=k\\dfrac{y}{500-y}$"], "A",
      "Proportional to the product: $k\\cdot y\\cdot(500-y)$.",
      "Translate “proportional to” as $k$ times the named quantity (R7.1).",
      ["Heard: $y$. Not heard: $500-y$.", "Rate proportional to their product: $\\frac{dy}{dt}=ky(500-y)$ (a logistic model)."],
      {"B": "uses only the number who have not heard.",
       "C": "uses only the number who have heard.",
       "D": "uses a quotient instead of a product."}, layout="two"),
    Q(2, 1, "R7.2", "Which function is a solution of $y''+4y=0$?",
      ["$e^{2x}$", "$x^2-2$", "$\\sin(2x)$", "$\\cos(4x)$"], "C",
      "$y''=-4\\sin2x$, so $y''+4y=0$.",
      "Substitute the function and its second derivative (R7.2).",
      ["$y=\\sin2x$: $y''=-4\\sin2x$.", "$y''+4y=-4\\sin2x+4\\sin2x=0$."],
      {"A": "$y''+4y=4e^{2x}+4e^{2x}\\neq0$.",
       "B": "$y''+4y=2+4x^2-8\\neq0$.",
       "D": "$y''=-16\\cos4x$, so $y''+4y=-12\\cos4x\\neq0$."}),
    Q(3, 2, "R7.3", "The slope field shown is for which differential equation?",
      ["$\\dfrac{dy}{dx}=x+y$", "$\\dfrac{dy}{dx}=x-y$", "$\\dfrac{dy}{dx}=y-x$", "$\\dfrac{dy}{dx}=xy$"], "B",
      "Zero slopes along $y=x$; at $(2,0)$ the slope is positive.",
      "Test where the slopes are zero and the sign at one convenient point (R7.3).",
      ["Horizontal segments lie along $y=x$, so $\\frac{dy}{dx}=0$ when $x=y$: $x-y$ or $y-x$.", "At $(2,0)$ the segment rises, so the slope is $+2$: $x-y$."],
      {"A": "would have zero slopes along $y=-x$.",
       "C": "has the right zero line but the opposite sign everywhere.",
       "D": "would have zero slopes along both axes."}, fig=F3, layout="four"),
    Q(4, 2, "R7.3", "Let $y=f(x)$ be the solution of $\\dfrac{dy}{dx}=(y-1)(y-4)$ with $f(0)=2$. As $x$ increases, $f(x)$",
      ["increases and approaches 4", "decreases without bound", "remains constant at 2", "decreases and approaches 1"], "D",
      "For $1<y<4$, $\\frac{dy}{dx}<0$; the solution falls toward the equilibrium $y=1$.",
      "Equilibria are where $\\frac{dy}{dx}=0$; solutions between them cannot cross them (R7.3).",
      ["Equilibria: $y=1$ and $y=4$.", "At $y=2$: $(1)(-2)<0$, so $f$ decreases, and it cannot cross $y=1$: it approaches 1."],
      {"A": "gets the sign of $\\frac{dy}{dx}$ wrong between the equilibria.",
       "B": "ignores the equilibrium $y=1$, which a solution cannot cross.",
       "C": "$y=2$ is not an equilibrium; the slope there is $-2$."}, layout="two"),
    Q(5, 3, "R7.4", "Let $y=f(x)$ solve $\\dfrac{dy}{dx}=2x-y$ with $f(1)=3$. Euler's method with two steps of size $0.5$ gives which approximation of $f(2)$?",
      ["$2$", "$2.5$", "$2.75$", "$3.25$"], "C",
      "$3+0.5(-1)=2.5$; then $2.5+0.5(3-2.5)=2.75$.",
      "Each step uses the slope at the current point (R7.4).",
      ["At $(1,3)$: slope $2-3=-1$; $f(1.5)\\approx3-0.5=2.5$.", "At $(1.5,2.5)$: slope $3-2.5=0.5$; $f(2)\\approx2.5+0.25=2.75$."],
      {"A": "takes one step of size 1: $3+(-1)(1)$.",
       "B": "stops after one step.",
       "D": "evaluates the second slope at $x=2$ instead of $x=1.5$."}),
    Q(6, 3, "R7.4", "Let $y=f(x)$ solve $\\dfrac{dy}{dx}=y^2$ with $f(0)=1$. Euler's method with one step of size $0.1$ approximates $f(0.1)$ as",
      ["$1.1$, an underestimate", "$1.1$, an overestimate", "$1.01$, an underestimate", "$1.2$, an overestimate"], "A",
      "$1+0.1(1)=1.1$; $y''=2yy'=2y^3>0$, so Euler underestimates.",
      "Euler follows tangent lines: concave-up solutions are underestimated (R7.4).",
      ["Slope at $(0,1)$: 1. Estimate: $1.1$.", "$\\frac{d^2y}{dx^2}=2y\\frac{dy}{dx}=2y^3>0$: concave up, so the estimate is too small (exact $\\frac{1}{0.9}\\approx1.111$)."],
      {"B": "reverses the concavity rule.",
       "C": "multiplies the slope by $\\Delta x^2=0.01$ instead of $\\Delta x$.",
       "D": "uses a step of 0.2, and calls it an overestimate."}, layout="two"),
    Q(7, 4, "R7.5", "The general solution of $\\dfrac{dy}{dx}=xy$ is",
      ["$y=e^{x^2/2}+C$", "$y=Ce^{x^2}$", "$y=\\dfrac{x^2}{2}+C$", "$y=Ce^{x^2/2}$"], "D",
      "$\\int\\frac{dy}y=\\int x\\,dx$: $\\ln|y|=\\frac{x^2}{2}+C$.",
      "Separate, integrate, and exponentiate; the constant becomes a factor (R7.5–R7.6).",
      ["$\\frac{dy}{y}=x\\,dx$, so $\\ln|y|=\\frac{x^2}{2}+C_1$.", "$y=\\pm e^{C_1}e^{x^2/2}=Ce^{x^2/2}$."],
      {"A": "adds the constant after exponentiating; it should multiply.",
       "B": "integrates $x$ as $x^2$.",
       "C": "integrates the right side only, treating $y$ as constant."}, layout="four"),
    Q(8, 4, "R7.6", "The solution of $\\dfrac{dy}{dx}=2xy^2$ with $y(0)=1$ is",
      ["$y=\\dfrac{1}{1+x^2}$", "$y=e^{x^2}$", "$y=\\dfrac{1}{1-x^2}$", "$y=1-x^2$"], "C",
      "$-\\frac1y=x^2+C$, $C=-1$, so $y=\\frac{1}{1-x^2}$.",
      "Separate, integrate, find $C$ from the initial condition, then solve for $y$ (R7.5–R7.6).",
      ["$\\int y^{-2}dy=\\int2x\\,dx$: $-\\frac1y=x^2+C$.", "At $(0,1)$: $C=-1$. So $\\frac1y=1-x^2$, $y=\\frac{1}{1-x^2}$."],
      {"A": "sign error in $\\int y^{-2}dy=-\\frac1y$.",
       "B": "solves $\\frac{dy}{dx}=2xy$ instead.",
       "D": "inverts only part of the expression."}, layout="four"),
    Q(9, 4, "R7.6", "The particular solution $y=\\dfrac{1}{1-x^2}$ through $(0,1)$ is defined on which interval?",
      ["all real numbers", "$-1<x<1$", "$x\\neq\\pm1$", "$x>1$"], "B",
      "The largest interval containing $x=0$ where $1-x^2\\neq0$.",
      "A particular solution lives on the largest open interval containing the initial point (R7.6).",
      ["$1-x^2=0$ at $x=\\pm1$.", "The interval containing 0 is $(-1,1)$."],
      {"A": "ignores the vertical asymptotes at $\\pm1$.",
       "C": "is the domain of the formula, but a solution must be on one interval through $x=0$.",
       "D": "does not contain the initial point $x=0$."}, layout="four"),
    Q(10, 5, "R7.7", "A population grows at a rate proportional to its size. It is 200 at $t=0$ and doubles every 5 years. What is it at $t=15$?",
      ["$800$", "$1200$", "$1600$", "$3200$"], "C",
      "Three doublings: $200\\cdot2^3$.",
      "$\\frac{dy}{dt}=ky$ gives exponential growth with a fixed doubling time (R7.7).",
      ["$y=200e^{kt}$ with $e^{5k}=2$.", "$y(15)=200(e^{5k})^3=200\\cdot8=1600$."],
      {"A": "counts two doublings.",
       "B": "assumes linear growth (adding the same amount each period); the model is exponential.",
       "D": "counts four doublings."}),
    Q(11, 5, "R7.7", "Coffee at 90°C cools in a 20°C room according to $\\dfrac{dT}{dt}=-0.1(T-20)$, $t$ in minutes. What is its temperature at $t=10$?",
      ["$20.00$", "$25.75$", "$33.11$", "$45.75$"], "D",
      "$T=20+70e^{-0.1t}$; $T(10)=20+70e^{-1}$.",
      "Newton's law of cooling: $T=A+(T_0-A)e^{kt}$ (R7.7).",
      ["$T-20=70e^{-0.1t}$.", "$T(10)=20+70e^{-1}\\approx45.75$."],
      {"A": "follows the initial rate $-7$ for 10 minutes; the rate slows as $T$ falls.",
       "B": "forgets to add the room temperature: $70e^{-1}$.",
       "C": "uses $T=90e^{-0.1t}$, ignoring the room temperature."}, calc=True),
    Q(12, 5, "R7.8", "A population satisfies $\\dfrac{dP}{dt}=0.3P-0.0006P^2$ with $P(0)=100$. Which statement is true?",
      ["$\\lim_{t\\to\\infty}P(t)=250$, and $P$ grows fastest when $P=500$",
       "$\\lim_{t\\to\\infty}P(t)=500$, and $P$ grows fastest when $P=250$",
       "$\\lim_{t\\to\\infty}P(t)=500$, and $P$ grows fastest when $P=500$",
       "$\\lim_{t\\to\\infty}P(t)=500$, and $P$ grows fastest at $t=0$"], "B",
      "$0.3P(1-\\frac{P}{500})$: $L=500$, fastest at $\\frac L2=250$.",
      "Factor into $kP(1-\\frac PL)$ to read the carrying capacity; growth is fastest at half of it (R7.8).",
      ["$0.3P-0.0006P^2=0.3P\\left(1-\\frac{P}{500}\\right)$: $L=500$.", "$\\frac{dP}{dt}$ is a downward parabola in $P$ with vertex at $P=250$."],
      {"A": "swaps the carrying capacity and the half-way point.",
       "C": "at $P=500$ the growth rate is 0, not largest.",
       "D": "$\\frac{dP}{dt}$ keeps increasing until $P$ reaches 250."}, layout="one"),
]

# FRQ: dy/dx = x(y - 1), f(2) = 3
yv = sp.symbols("Y")
d2 = sp.diff(x * (yv - 1), x) + sp.diff(x * (yv - 1), yv) * x * (yv - 1)
assert sp.expand(d2 - (yv - 1) * (1 + x**2)) == 0 and d2.subs({x: 2, yv: 3}) == 10
fs = sp.dsolve(sp.Eq(y(x).diff(x), x * (y(x) - 1)), y(x), ics={y(2): 3}).rhs
assert sp.simplify(fs - (1 + 2 * sp.exp(x**2 / 2 - 2))) == 0

FRS = [
    FRQ(1, [4], "A separable differential equation",
        "Consider the differential equation $\\dfrac{dy}{dx}=x(y-1)$. Let $y=f(x)$ be the particular solution with $f(2)=3$.",
        [P("a", "Write an equation for the line tangent to the graph of $f$ at $x=2$, and use it to approximate $f(2.1)$.",
           ["tangent line $y=3+4(x-2)$", "approximation $f(2.1)\\approx3.4$"],
           ["At $(2,3)$: $\\frac{dy}{dx}=2(3-1)=4$. Tangent: $y=3+4(x-2)$, so $f(2.1)\\approx3.4$."]),
         P("b", "Find $\\dfrac{d^2y}{dx^2}$ in terms of $x$ and $y$. Is the approximation in part (a) an overestimate or an underestimate? Justify your answer.",
           ["$\\frac{d^2y}{dx^2}=(y-1)+x\\frac{dy}{dx}$", "$=(y-1)(1+x^2)$, equal to 10 at $(2,3)$", "underestimate, because the graph is concave up near $x=2$"],
           ["$\\frac{d^2y}{dx^2}=(y-1)+x\\frac{dy}{dx}=(y-1)+x^2(y-1)=(y-1)(1+x^2)$.",
            "At $(2,3)$ this is $2\\cdot5=10>0$, and it stays positive near $x=2$ (where $y>1$), so the graph of $f$ is concave up there and lies above its tangent line: an underestimate."]),
         P("c", "Find $y=f(x)$, the particular solution with $f(2)=3$.",
           ["separates variables", "antiderivatives $\\ln|y-1|$ and $\\frac{x^2}{2}$", "uses the initial condition: $\\ln2=2+C$", "solves for $y$: $y=1+2e^{x^2/2-2}$"],
           ["$\\frac{dy}{y-1}=x\\,dx$, so $\\ln|y-1|=\\frac{x^2}{2}+C$.",
            "At $(2,3)$: $\\ln2=2+C$, so $C=\\ln2-2$.",
            "$y-1>0$ near the initial point, so $y-1=e^{x^2/2+\\ln2-2}=2e^{x^2/2-2}$ and $y=1+2e^{x^2/2-2}$."])]),
]
