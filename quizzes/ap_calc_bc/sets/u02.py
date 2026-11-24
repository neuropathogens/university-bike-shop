"""Unit 2 Practice Set: Differentiation: Definition and Fundamental Properties (12 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, Table, fig

x, h = sp.symbols("x h")

DOC = dict(
    unit=2, title="Differentiation: Definition and Fundamental Properties", topics="2.1–2.10",
    pdf="ap-calc-bc-02-differentiation-basics-practice.pdf", guide_pdf="ap-calc-bc-02-differentiation-basics-guide.pdf",
    sections={"1": "Rates of change and the definition of the derivative", "2": "Estimating derivatives and differentiability",
              "3": "Basic derivative rules", "4": "Product and quotient rules"},
    rules={"1": "R2.1–R2.3. Average rate $=\\frac{f(b)-f(a)}{b-a}$. $f'(a)=\\lim_{h\\to0}\\frac{f(a+h)-f(a)}{h}$: recognize the form, name $f$ and $a$.",
           "2": "R2.4–R2.6. Estimate with a difference quotient. Differentiable implies continuous; corners, cusps, vertical tangents and jumps are not differentiable.",
           "3": "R2.7–R2.9. $\\frac{d}{dx}x^n=nx^{n-1}$; $\\sin\\to\\cos$, $\\cos\\to-\\sin$, $e^x\\to e^x$, $\\ln x\\to\\frac1x$. Tangent: $y=f(a)+f'(a)(x-a)$.",
           "4": "R2.10–R2.12. $(uv)'=u'v+uv'$; $(u/v)'=\\frac{u'v-uv'}{v^2}$; $\\tan\\to\\sec^2$, $\\sec\\to\\sec\\tan$."},
    abstract="Twelve exam-style multiple-choice questions on Unit 2, grouped by the sections of the Unit 2 Study Guide, and one nine-point free-response question that estimates a derivative from a table and tests differentiability of a piecewise function. All items are no-calculator except those marked [calculator]. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (24 min) and 15 minutes for the free response.",
    setup="Allow 24 minutes for the multiple choice and 15 for the free response. Item 6 allows a graphing calculator.",
)

F5 = fig("u2-q5", r"""\begin{tikzpicture}
\begin{axis}[width=7cm,height=4.4cm,axis lines=middle,xmin=-0.5,xmax=6.5,ymin=-0.5,ymax=4.5,xtick={1,...,6},ytick={1,2,3,4},xlabel={$x$},ylabel={$y$},
 every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},every axis y label/.style={at={(ticklabel* cs:1)},anchor=south}]
\addplot[thick] coordinates{(0,1) (2,3) (4,3)};
\addplot[thick,domain=4:6,samples=40]{3+0.2*(x-4)^2};
\end{axis}\end{tikzpicture}""", "Graph of f on 0 ≤ x ≤ 6: a segment from (0,1) to (2,3), a horizontal segment from (2,3) to (4,3), then a curve rising smoothly from (4,3) with horizontal tangent at x = 4, ending near (6, 3.8).")

# checks
assert sp.diff(sp.sqrt(x), x).subs(x, 9) == sp.Rational(1, 6)
assert sp.limit((sp.sqrt(9 + h) - 3) / h, h, 0) == sp.Rational(1, 6)
assert sp.limit((sp.exp(2 * (1 + h)) - sp.exp(2)) / h, h, 0) == 2 * sp.exp(2)
f6 = x**3 - 2 * x
assert sp.Rational(f6.subs(x, 3) - f6.subs(x, 1), 2) == 11 and sp.diff(f6, x).subs(x, 2) == 10
a, b = sp.symbols("a b")
assert sp.solve([sp.Eq(a * 4 + b, 2**3 - 3), sp.Eq(2 * a * 2, 3 * 4)], [a, b]) == {a: 3, b: -7}
g10 = (3 * x - 1) / (x**2 + 1)
assert sp.diff(g10, x).subs(x, 1) == sp.Rational(1, 2)
f11 = x**2 * sp.sin(x)
assert sp.simplify(sp.diff(f11, x).subs(x, sp.pi / 2) - sp.pi) == 0
assert sp.simplify(sp.diff(sp.tan(x) * sp.sec(x), x).subs(x, sp.pi / 4) - 3 * sp.sqrt(2)) == 0
y12 = 4 / sp.sqrt(x) + x
assert sp.diff(y12, x).subs(x, 4) == sp.Rational(3, 4)

QS = [
    Q(1, 1, "R2.1", "For $f(x)=x^3-2x$, the average rate of change of $f$ on $[1,3]$ is",
      ["$10$", "$11$", "$22$", "$25$"], "B",
      "$\\frac{f(3)-f(1)}{3-1}=\\frac{21-(-1)}{2}=11$.",
      "Average rate of change is the secant slope $\\frac{f(b)-f(a)}{b-a}$; no derivative is needed (R2.1).",
      ["$f(3)=27-6=21$ and $f(1)=1-2=-1$.", "$\\frac{21-(-1)}{3-1}=\\frac{22}{2}=11$."],
      {"A": "is $f'(2)=3(4)-2$, the instantaneous rate at the midpoint, not the average rate.",
       "C": "forgets to divide by $b-a=2$.",
       "D": "is $f'(3)=27-2$, an instantaneous rate at one endpoint."}),
    Q(2, 1, "R2.3", "$\\displaystyle\\lim_{h\\to0}\\frac{\\sqrt{9+h}-3}{h}$ is",
      ["$0$", "$\\dfrac{1}{18}$", "$\\dfrac16$", "$\\dfrac13$"], "C",
      "It is $f'(9)$ for $f(x)=\\sqrt x$: $\\frac{1}{2\\sqrt9}=\\frac16$.",
      "A limit of the form $\\lim_{h\\to0}\\frac{f(a+h)-f(a)}{h}$ is $f'(a)$ (R2.3).",
      ["Here $f(x)=\\sqrt x$, $a=9$, $f(9)=3$.", "$f'(x)=\\frac{1}{2\\sqrt x}$, so $f'(9)=\\frac16$."],
      {"A": "stops at the numerator going to 0; the denominator also goes to 0.",
       "B": "uses $\\frac{1}{2\\cdot9}$, forgetting the square root in $\\frac{1}{2\\sqrt x}$.",
       "D": "forgets the factor $\\frac12$ from the power rule: $\\frac{1}{\\sqrt9}$."}),
    Q(3, 1, "R2.3", "$\\displaystyle\\lim_{x\\to1}\\frac{e^{2x}-e^2}{x-1}$ is",
      ["$e^2$", "$2e$", "$2e^2$", "nonexistent"], "C",
      "It is $f'(1)$ for $f(x)=e^{2x}$: $2e^{2}$.",
      "The form $\\lim_{x\\to a}\\frac{f(x)-f(a)}{x-a}$ is $f'(a)$ (R2.3). (Chain rule, Unit 3: $\\frac{d}{dx}e^{2x}=2e^{2x}$.)",
      ["$f(x)=e^{2x}$, $a=1$, $f(1)=e^2$.", "$f'(x)=2e^{2x}$, so $f'(1)=2e^2$."],
      {"A": "drops the factor 2 from the chain rule.",
       "B": "multiplies by 2 but evaluates $e^{x}$ instead of $e^{2x}$ at 1.",
       "D": "$\\tfrac00$ is indeterminate; the limit is a derivative and exists."}),
    Q(4, 2, "R2.4", "The table gives selected values of a differentiable function $W$. Using the data, the best estimate of $W'(6)$ is",
      ["$-2$", "$2$", "$3$", "$4$"], "D",
      "$\\frac{W(8)-W(4)}{8-4}=\\frac{29-13}{4}=4$.",
      "Estimate $W'(c)$ with the difference quotient over the smallest interval in the table that contains $c$ (R2.4).",
      ["The closest inputs around 6 are 4 and 8.", "$\\frac{29-13}{8-4}=\\frac{16}{4}=4$."],
      {"A": "uses the interval $[8,11]$, which does not contain 6.",
       "B": "uses the whole table, $\\frac{W(11)-W(0)}{11}=\\frac{22}{11}$; a wider interval is a worse estimate.",
       "C": "uses $[0,4]$: $\\frac{13-1}{4}=3$, which does not contain 6."},
      table=Table([["$t$", "0", "4", "8", "11"], ["$W(t)$", "1", "13", "29", "23"]])),
    Q(5, 2, "R2.5", "The graph of $f$ is shown. At which of the following values of $x$ is $f$ not differentiable?",
      ["$x=1$ only", "$x=4$ only", "$x=2$ and $x=4$", "$x=2$ only"], "D",
      "Corner at $x=2$ (slopes 1 and 0); at $x=4$ the slopes are 0 on both sides.",
      "A corner, where the left and right slopes differ, is not differentiable; a smooth join with matching slopes is (R2.5).",
      ["At $x=2$: left slope $\\frac{3-1}{2-0}=1$, right slope 0. A corner.",
       "At $x=4$: the flat segment has slope 0 and the curve $3+0.2(x-4)^2$ has slope $0.4(x-4)=0$ at 4. Smooth."],
      {"A": "the segment from (0,1) to (2,3) is a straight line; $f$ is differentiable at $x=1$.",
       "B": "at $x=4$ both one-sided slopes are 0, so the join is smooth.",
       "C": "only $x=2$ is a corner; $x=4$ is a smooth join."}, fig=F5),
    Q(6, 2, "R2.4", "A cup of coffee cools; its temperature $H(t)$, in degrees, is given in the table for $t$ in minutes. Which is the best estimate of $H'(5)$, and its units?",
      ["$-\\frac83$ degrees per minute", "$-2$ degrees per minute", "$-1$ degree per minute", "$168$ degrees"], "B",
      "$\\frac{H(7)-H(3)}{7-3}=\\frac{164-172}{4}=-2$ °/min.",
      "Symmetric difference quotient around $t=5$; units are output per input (R2.1, R2.4).",
      ["The closest inputs on either side of 5 are 3 and 7.", "$\\frac{164-172}{4}=-2$ degrees per minute."],
      {"A": "uses $[0,3]$: $\\frac{172-180}{3}=-\\frac83$; that interval does not contain 5.",
       "C": "uses $[3,7]$ but divides by 8 instead of 4.",
       "D": "is an estimate of $H(5)$, the temperature, not its rate of change."}, calc=True, layout="two",
      table=Table([["$t$ (min)", "0", "3", "7", "10"], ["$H(t)$ (°F)", "180", "172", "164", "160"]])),
    Q(7, 2, "R2.6", "Let $f(x)=\\begin{cases}ax^2+b,&x\\le2\\\\ x^3-3,&x>2\\end{cases}$. For which $a$ and $b$ is $f$ differentiable at $x=2$?",
      ["$a=3$, $b=-7$", "$a=3$, $b=17$", "$a=\\frac32$, $b=-1$", "$a=12$, $b=-43$"], "A",
      "Slopes: $4a=12$, so $a=3$; values: $4a+b=5$, so $b=-7$.",
      "Differentiable at a junction: the pieces agree in value (continuity) and in slope (R2.6).",
      ["Slopes at 2: $2a(2)=4a$ and $3(2)^2=12$, so $a=3$.", "Values at 2: $4a+b=8-3=5$, so $12+b=5$, $b=-7$."],
      {"B": "sign error solving $12+b=5$.",
       "C": "solves the slope equation as $2a=3$, forgetting to evaluate $2ax$ and $3x^2$ at $x=2$; then $4a+b=5$ gives $b=-1$.",
       "D": "sets $a$ equal to the right-hand slope 12, forgetting the factor $2x=4$ in $2ax$; then $48+b=5$."}),
    Q(8, 3, "R2.7", "If $y=\\dfrac{4}{\\sqrt{x}}+x$, then $\\dfrac{dy}{dx}$ at $x=4$ is",
      ["$-\\dfrac14$", "$0$", "$\\dfrac34$", "$\\dfrac54$"], "C",
      "$y'=-2x^{-3/2}+1=-\\frac14+1=\\frac34$.",
      "Rewrite the root as a power, then apply the power rule (R2.7).",
      ["$y=4x^{-1/2}+x$, so $y'=-2x^{-3/2}+1$.", "At $x=4$: $x^{-3/2}=\\frac18$, so $y'=-\\frac14+1=\\frac34$."],
      {"A": "drops the $+1$ from differentiating $x$.",
       "B": "keeps the exponent $-\\frac12$ after differentiating: $-2\\cdot4^{-1/2}+1=0$.",
       "D": "gets the sign of $-2x^{-3/2}$ wrong."}),
    Q(9, 3, "R2.9", "An equation of the line tangent to $y=3\\ln x+x^2$ at $x=1$ is",
      ["$y=5x-4$", "$y=5x-5$", "$y=2x-1$", "$y=5x-1$"], "A",
      "Point $(1,1)$, slope $\\frac31+2=5$: $y=1+5(x-1)$.",
      "Tangent line: $y=f(a)+f'(a)(x-a)$ (R2.8, R2.9).",
      ["$f(1)=3\\ln1+1=1$; $f'(x)=\\frac3x+2x$, so $f'(1)=5$.", "$y=1+5(x-1)=5x-4$."],
      {"B": "uses the point $(1,0)$, forgetting the $x^2$ term in $f(1)$.",
       "C": "uses slope 2, dropping the derivative of $3\\ln x$.",
       "D": "takes $\\ln1=1$, so it uses the wrong point $(1,4)$."}),
    Q(10, 4, "R2.11", "If $g(x)=\\dfrac{3x-1}{x^2+1}$, then $g'(1)=$",
      ["$-\\dfrac12$", "$\\dfrac12$", "$\\dfrac32$", "$\\dfrac52$"], "B",
      "$\\frac{3(2)-(2)(2)}{2^2}=\\frac{2}{4}=\\frac12$.",
      "Quotient rule: $\\frac{u'v-uv'}{v^2}$, numerator in that order (R2.11).",
      ["$u=3x-1$, $u'=3$, $v=x^2+1$, $v'=2x$. At $x=1$: $u=2$, $v=2$, $v'=2$.", "$g'(1)=\\frac{3\\cdot2-2\\cdot2}{2^2}=\\frac{2}{4}=\\frac12$."],
      {"A": "reverses the numerator: $uv'-u'v$.",
       "C": "is $u'/v=\\frac32$, dividing derivatives term by term.",
       "D": "adds the two numerator terms: $\\frac{6+4}{4}$."}),
    Q(11, 4, "R2.10", "If $f(x)=x^2\\sin x$, then $f'\\!\\left(\\frac{\\pi}{2}\\right)=$",
      ["$0$", "$\\dfrac{\\pi}{2}$", "$\\dfrac{\\pi^2}{4}$", "$\\pi$"], "D",
      "$f'=2x\\sin x+x^2\\cos x$; at $\\frac\\pi2$: $\\pi\\cdot1+0=\\pi$.",
      "Product rule $(uv)'=u'v+uv'$ (R2.10).",
      ["$f'(x)=2x\\sin x+x^2\\cos x$.", "At $\\frac\\pi2$: $\\sin=1$, $\\cos=0$, so $f'=2\\cdot\\frac\\pi2=\\pi$."],
      {"A": "uses $u'v'=2x\\cos x$, which is 0 at $\\frac\\pi2$.",
       "B": "forgets the factor 2 in $(x^2)'=2x$.",
       "C": "is $f(\\frac\\pi2)$, the value, not the derivative (and also what you get by swapping $\\sin$ and $\\cos$ in the product rule)."}),
    Q(12, 4, "R2.12", "If $y=\\tan x\\sec x$, then $\\dfrac{dy}{dx}$ at $x=\\frac{\\pi}{4}$ is",
      ["$\\sqrt2$", "$2\\sqrt2$", "$3\\sqrt2$", "$2\\sqrt2+2$"], "C",
      "$\\sec^3x+\\tan^2x\\sec x=2\\sqrt2+\\sqrt2=3\\sqrt2$.",
      "Product rule with $\\frac{d}{dx}\\tan x=\\sec^2x$ and $\\frac{d}{dx}\\sec x=\\sec x\\tan x$ (R2.10, R2.12).",
      ["$y'=\\sec^2x\\cdot\\sec x+\\tan x\\cdot\\sec x\\tan x=\\sec^3x+\\sec x\\tan^2x$.",
       "At $\\frac\\pi4$: $\\sec=\\sqrt2$, $\\tan=1$, so $y'=2\\sqrt2+\\sqrt2=3\\sqrt2$."],
      {"A": "is $y(\\frac\\pi4)=1\\cdot\\sqrt2$, the value.",
       "B": "keeps only the $\\sec^3x$ term.",
       "D": "uses $\\frac{d}{dx}\\sec x=\\sec^2 x$: $\\sec^3x+\\tan x\\sec^2x=2\\sqrt2+2$."}),
]

T_FR = Table([["$t$ (hours)", "0", "2", "5", "8", "10"], ["$R(t)$ (liters per hour)", "40", "52", "61", "55", "48"]])
FRS = [
    FRQ(1, [1, 2, 3], "Rates from a table; a piecewise model",
        "Water flows into a tank at a rate of $R(t)$ liters per hour, where $R$ is differentiable and $t$ is measured in hours. Selected values of $R$ are given in the table.",
        [P("a", "Find the average rate of change of $R$ over $0\\le t\\le10$. Indicate units.",
           ["$\\frac{R(10)-R(0)}{10-0}=0.8$", "units: liters per hour per hour"],
           ["$\\frac{48-40}{10}=0.8$ liters per hour per hour."]),
         P("b", "Use the data to estimate $R'(6.5)$. Show the computations that lead to your answer, and explain the meaning of your estimate in context.",
           ["difference quotient on $[5,8]$", "estimate $-2$", "interpretation: at $t=6.5$ the inflow rate is decreasing by about 2 liters per hour per hour"],
           ["$R'(6.5)\\approx\\frac{R(8)-R(5)}{8-5}=\\frac{55-61}{3}=-2$.",
            "At $t=6.5$ hours, the rate at which water flows in is decreasing at about 2 liters per hour per hour."]),
         P("c", "For $10\\le t\\le14$ the rate is modeled by $R(t)=\\begin{cases}48-a(t-10)^2,&10\\le t\\le12\\\\ bt+c,&12<t\\le14\\end{cases}$ where $R$ is differentiable at $t=12$ and $R(14)=24$. Find the values of $a$, $b$ and $c$.",
           ["continuity equation $48-4a=12b+c$", "slope equation $-4a=b$", "uses $R(14)=24$: $14b+c=24$", "solves: $a=2$, $b=-8$, $c=136$"],
           ["Continuity at 12: $48-4a=12b+c$. Matching slopes: $-2a(12-10)=-4a=b$.",
            "$R(14)=14b+c=24$. Subtract the continuity equation: $2b=24-(48-4a)=4a-24$. With $b=-4a$: $-8a=4a-24$, so $a=2$.",
            "Then $b=-8$ and $c=24-14b=136$. Check: $R(12)=48-8=40=12(-8)+136$."])]),
]
# FRQ (c): 48-4a = 12b + c, b = -4a, 14b + c = 24
A, B, C = sp.symbols("A B C")
sol = sp.solve([sp.Eq(48 - 4 * A, 12 * B + C), sp.Eq(B, -4 * A), sp.Eq(14 * B + C, 24)], [A, B, C])
assert sol == {A: 2, B: -8, C: 136}, sol
