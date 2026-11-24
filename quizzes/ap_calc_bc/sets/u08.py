"""Unit 8 Practice Set: Applications of Integration (12 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q

x, t, yv = sp.symbols("x t y")

DOC = dict(
    unit=8, title="Applications of Integration", topics="8.1–8.13",
    pdf="ap-calc-bc-08-applications-of-integration-practice.pdf", guide_pdf="ap-calc-bc-08-applications-of-integration-guide.pdf",
    sections={"1": "Average value", "2": "Motion and accumulation in context", "3": "Area between curves", "4": "Volumes", "5": "Arc length"},
    rules={"1": "R8.1. $f_{\\text{avg}}=\\frac{1}{b-a}\\int_a^bf$; not the average rate of change.",
           "2": "R8.2–R8.3. Displacement $\\int v$; distance $\\int|v|$; amount $=A_0+\\int(\\text{in}-\\text{out})$.",
           "3": "R8.4–R8.6. $\\int(\\text{top}-\\text{bottom})\\,dx$ or $\\int(\\text{right}-\\text{left})\\,dy$; split where curves cross.",
           "4": "R8.7–R8.10. Cross sections $\\int A(x)\\,dx$; discs $\\pi\\int R^2$; washers $\\pi\\int(R^2-r^2)$; radii from the axis.",
           "5": "R8.11. $L=\\int_a^b\\sqrt{1+(f')^2}\\,dx$."},
    abstract="Twelve exam-style multiple-choice questions on Unit 8, grouped by the sections of the Unit 8 Study Guide, and one nine-point calculator-active free-response question on the area and volumes of a region between two curves. Items marked [calculator] allow a graphing calculator; the rest are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (24 min) and 15 minutes for the free response.",
    setup="Allow 24 minutes for the multiple choice and 15 for the free response. Items 4 and 12 and the free response need a graphing calculator.",
    frnote="Calculator required. Show the integral you evaluate, and give decimal answers correct to three places.",
)

# checks
assert sp.integrate(x**2, (x, 0, 6)) / 6 == 12
v2 = t**2 - 4 * t + 3
assert sp.integrate(sp.Abs(v2), (t, 0, 3)) == sp.Rational(8, 3) and sp.integrate(v2, (t, 0, 3)) == 0
assert 5 + sp.integrate(3 * t**2 - 2, (t, 0, 2)) == 9
r4 = sp.nsolve(8 + 4 * sp.sin(t) - 2 * t, t, 3.4)
assert abs(r4 - 3.430) < 5e-4
assert sp.integrate(3 * x - x**2, (x, 0, 3)) == sp.Rational(9, 2) and sp.integrate(2 * x - x**2, (x, 0, 2)) == sp.Rational(4, 3)
assert sp.integrate(yv + 2 - yv**2, (yv, -1, 2)) == sp.Rational(9, 2)
assert sp.integrate(x, (x, 0, 4)) == 8 and sp.integrate(sp.sqrt(x), (x, 0, 4)) == sp.Rational(16, 3)
assert sp.simplify(sp.pi * sp.integrate(sp.exp(2 * x), (x, 0, 1)) - sp.pi * (sp.E**2 - 1) / 2) == 0
assert sp.pi * sp.integrate(x**2 - x**4, (x, 0, 1)) == 2 * sp.pi / 15 and sp.pi * sp.integrate((x - x**2) ** 2, (x, 0, 1)) == sp.pi / 30
assert abs(sp.Integral(sp.sec(x), (x, 0, sp.pi / 4)).evalf() - sp.log(1 + sp.sqrt(2)).evalf()) < 1e-12
assert abs(sp.Integral(sp.sqrt(1 + 9 * x**4), (x, 0, 1)).evalf() - 1.548) < 5e-4

QS = [
    Q(1, 1, "R8.1", "What is the average value of $f(x)=x^2$ on $[0,6]$?",
      ["$6$", "$12$", "$18$", "$72$"], "B",
      "$\\frac16\\int_0^6x^2\\,dx=\\frac{72}{6}$.",
      "Average value $=\\frac{1}{b-a}\\int_a^bf$ (R8.1).",
      ["$\\int_0^6x^2\\,dx=72$.", "$\\frac{72}{6}=12$."],
      {"A": "is the average rate of change $\\frac{36-0}{6}$.",
       "C": "averages the endpoint values $\\frac{0+36}{2}$.",
       "D": "is the integral, not divided by the length 6."}),
    Q(2, 2, "R8.2", "A particle moves with velocity $v(t)=t^2-4t+3$. What is the total distance it travels for $0\\le t\\le3$?",
      ["$0$", "$\\dfrac43$", "$2$", "$\\dfrac83$"], "D",
      "$\\int_0^1v=\\frac43$ and $\\int_1^3|v|=\\frac43$.",
      "Distance is $\\int|v|$: split where $v$ changes sign (R8.2).",
      ["$v=(t-1)(t-3)$: positive on $(0,1)$, negative on $(1,3)$.", "$\\int_0^1v\\,dt=\\frac43$ and $\\int_1^3v\\,dt=-\\frac43$, so the distance is $\\frac83$."],
      {"A": "is the displacement $\\int_0^3v\\,dt$.",
       "B": "counts only one of the two pieces.",
       "C": "is the time spent moving left, not a distance."}),
    Q(3, 2, "R8.2", "A particle is at $x=5$ when $t=0$ and has velocity $v(t)=3t^2-2$. Where is it at $t=2$?",
      ["$4$", "$9$", "$10$", "$15$"], "B",
      "$5+\\int_0^2(3t^2-2)\\,dt=5+4$.",
      "Position $=$ initial position $+\\int v$ (R8.2).",
      ["$\\int_0^2(3t^2-2)\\,dt=[t^3-2t]_0^2=4$.", "$x(2)=5+4=9$."],
      {"A": "forgets the initial position: it is the displacement.",
       "C": "is $v(2)$, the velocity.",
       "D": "adds $v(2)=10$ to the initial position."}),
    Q(4, 2, "R8.3", "Water enters a tank at $E(t)=8+4\\sin t$ gallons per hour and leaves at $L(t)=2t$ gallons per hour, $0\\le t\\le6$. The tank holds 20 gallons at $t=0$. At what time is the amount of water in the tank greatest?",
      ["$1.571$", "$3.430$", "$4.000$", "$6.000$"], "B",
      "$E-L$ changes from $+$ to $-$ at $t\\approx3.430$; that amount beats both endpoints.",
      "The amount increases while in $>$ out; compare the sign change with the endpoints (R8.3).",
      ["$A'(t)=E(t)-L(t)=0$ at $t\\approx3.430$ (calculator), positive before and negative after.",
       "$A(3.430)=20+\\int_0^{3.430}(E-L)\\,dt\\approx43.510$, while $A(0)=20$ and $A(6)\\approx32.159$."],
      {"A": "is where the inflow $E$ is largest, not where the amount is largest.",
       "C": "solves $2t=8$, ignoring the $4\\sin t$ part of the inflow.",
       "D": "is the end of the interval; the amount is falling after $t\\approx3.43$."}, calc=True),
    Q(5, 3, "R8.4", "What is the area of the region between $y=x$ and $y=x^2-2x$?",
      ["$-\\dfrac92$", "$\\dfrac43$", "$\\dfrac92$", "$\\dfrac{27}{2}$"], "C",
      "They meet at $x=0,3$; $\\int_0^3(3x-x^2)\\,dx=\\frac92$.",
      "Area $=\\int(\\text{top}-\\text{bottom})$ between the intersections (R8.4).",
      ["$x^2-2x=x$ at $x=0$ and $x=3$; the line is on top.", "$\\int_0^3(x-(x^2-2x))\\,dx=\\left[\\frac32x^2-\\frac{x^3}{3}\\right]_0^3=\\frac{27}{2}-9=\\frac92$."],
      {"A": "subtracts top from bottom; an area is positive.",
       "B": "uses 0 and 2, the zeros of $x^2-2x$, as the limits.",
       "D": "drops the $-x^2$ term."}),
    Q(6, 3, "R8.5", "The region is bounded by $x=y^2$ and $x=y+2$. Which integral gives its area?",
      ["$\\displaystyle\\int_{-1}^{2}(y+2-y^2)\\,dy$", "$\\displaystyle\\int_{-1}^{2}(y^2-y-2)\\,dy$", "$\\displaystyle\\int_{1}^{4}\\left(\\sqrt x-(x-2)\\right)dx$", "$\\displaystyle\\int_{0}^{4}(y+2-y^2)\\,dy$"], "A",
      "In $y$: right $x=y+2$ minus left $x=y^2$, from $y=-1$ to $2$.",
      "When left and right boundaries are functions of $y$, integrate right minus left in $y$ (R8.5).",
      ["$y^2=y+2$ at $y=-1$ and $y=2$.", "For $-1<y<2$, the line $x=y+2$ is to the right of the parabola. Area $=\\frac92$."],
      {"B": "is left minus right: the negative of the area.",
       "C": "misses the part of the region below the $x$-axis, where the left boundary is $-\\sqrt x$.",
       "D": "uses $x$-values (0 to 4) as $y$-limits."}, layout="two"),
    Q(7, 4, "R8.7", "The base of a solid is the region under $y=\\sqrt x$ for $0\\le x\\le4$. Cross sections perpendicular to the $x$-axis are squares. What is the volume?",
      ["$\\pi$", "$\\dfrac{16}{3}$", "$8$", "$8\\pi$"], "C",
      "$\\int_0^4(\\sqrt x)^2\\,dx=8$.",
      "Cross-section volume: $\\int A(x)\\,dx$ with $A=s^2$ (R8.7).",
      ["Side $s=\\sqrt x$, so $A(x)=x$.", "$\\int_0^4x\\,dx=8$."],
      {"A": "uses semicircles: $\\frac\\pi8\\int_0^4x\\,dx$.",
       "B": "is the area of the base, $\\int_0^4\\sqrt x\\,dx$.",
       "D": "is the volume of revolution about the $x$-axis, $\\pi\\int_0^4x\\,dx$."}),
    Q(8, 4, "R8.8", "The region under $y=e^x$ for $0\\le x\\le1$ is revolved about the $x$-axis. The volume is",
      ["$\\dfrac{e^2-1}{2}$", "$\\pi(e-1)$", "$\\dfrac{\\pi(e^2-1)}{2}$", "$\\pi(e^2-1)$"], "C",
      "$\\pi\\int_0^1e^{2x}\\,dx=\\frac\\pi2(e^2-1)$.",
      "Disc method: $\\pi\\int R^2$ with $R=e^x$ (R8.8).",
      ["$R=e^x$, $R^2=e^{2x}$.", "$\\pi\\int_0^1e^{2x}dx=\\frac\\pi2(e^2-1)$."],
      {"A": "forgets the factor $\\pi$.",
       "B": "forgets to square the radius.",
       "D": "forgets the $\\frac12$ from $\\int e^{2x}dx=\\frac12e^{2x}$."}),
    Q(9, 4, "R8.9", "The region between $y=x$ and $y=x^2$ is revolved about the $x$-axis. The volume is",
      ["$-\\dfrac{2\\pi}{15}$", "$\\dfrac{\\pi}{30}$", "$\\dfrac{2}{15}$", "$\\dfrac{2\\pi}{15}$"], "D",
      "$\\pi\\int_0^1(x^2-x^4)\\,dx=\\frac{2\\pi}{15}$.",
      "Washers: outer $R=x$, inner $r=x^2$; square each separately (R8.9).",
      ["On $[0,1]$, $x\\ge x^2$: $R=x$, $r=x^2$.", "$\\pi\\int_0^1(x^2-x^4)\\,dx=\\pi\\left(\\frac13-\\frac15\\right)=\\frac{2\\pi}{15}$."],
      {"A": "swaps outer and inner radii.",
       "B": "uses $\\pi\\int(R-r)^2$ instead of $\\pi\\int(R^2-r^2)$.",
       "C": "forgets the factor $\\pi$."}),
    Q(10, 4, "R8.10", "The region bounded by $y=x^2$ and $y=4$ is revolved about the line $y=4$. Which integral gives the volume?",
      ["$\\displaystyle\\pi\\int_{-2}^{2}(4-x^2)^2\\,dx$", "$\\displaystyle\\pi\\int_{-2}^{2}(16-x^4)\\,dx$", "$\\displaystyle\\pi\\int_{-2}^{2}(4-x^2)\\,dx$", "$\\displaystyle\\pi\\int_{-2}^{2}x^4\\,dx$"], "A",
      "The region touches the axis $y=4$; disc radius $4-x^2$.",
      "Radius is the distance from the axis $y=4$ to the curve (R8.8, R8.10).",
      ["The region lies between $y=x^2$ and the axis $y=4$, for $-2\\le x\\le2$.", "Discs of radius $4-x^2$: $\\pi\\int_{-2}^2(4-x^2)^2dx=\\frac{512\\pi}{15}$."],
      {"B": "is the washer about the $x$-axis.",
       "C": "forgets to square the radius.",
       "D": "measures the radius from the $x$-axis instead of from $y=4$."}, layout="two"),
    Q(11, 5, "R8.11", "The length of the curve $y=\\ln(\\cos x)$ from $x=0$ to $x=\\frac\\pi4$ is",
      ["$\\ln\\sqrt2$", "$\\sqrt2-1$", "$\\dfrac{\\pi}{4}$", "$\\ln(1+\\sqrt2)$"], "D",
      "$\\sqrt{1+\\tan^2x}=\\sec x$; $\\int_0^{\\pi/4}\\sec x\\,dx=\\ln(\\sqrt2+1)$.",
      "Arc length $\\int\\sqrt{1+(y')^2}$, here simplified by $1+\\tan^2=\\sec^2$ (R8.11).",
      ["$y'=-\\tan x$, so $\\sqrt{1+y'^2}=\\sec x$ on $[0,\\frac\\pi4]$.", "$[\\ln|\\sec x+\\tan x|]_0^{\\pi/4}=\\ln(\\sqrt2+1)$."],
      {"A": "integrates $|y'|=\\tan x$, forgetting the 1 under the root.",
       "B": "evaluates $\\sec x$ itself at the limits instead of its antiderivative.",
       "C": "is the length of the interval, ignoring the slope."}),
    Q(12, 5, "R8.11", "What is the length of the curve $y=x^3$ from $x=0$ to $x=1$?",
      ["$1.380$", "$1.414$", "$1.548$", "$2.800$"], "C",
      "$\\int_0^1\\sqrt{1+9x^4}\\,dx\\approx1.548$.",
      "Arc length with the calculator (R8.11).",
      ["$y'=3x^2$, so $(y')^2=9x^4$.", "$\\int_0^1\\sqrt{1+9x^4}\\,dx\\approx1.548$."],
      {"A": "uses $3x^2$ without squaring: $\\int_0^1\\sqrt{1+3x^2}\\,dx$.",
       "B": "is the straight-line distance $\\sqrt2$ from $(0,0)$ to $(1,1)$, a lower bound.",
       "D": "forgets the square root: $\\int_0^1(1+9x^4)\\,dx$."}, calc=True),
]

# FRQ numbers
f, g = 3 - x**2, sp.exp(x) - 1
a = sp.nsolve(f - g, x, -1.9)
b = sp.nsolve(f - g, x, 1.0)
area = sp.Integral(f - g, (x, a, b)).evalf()
vol = (sp.pi * sp.Integral((f + 2) ** 2 - (g + 2) ** 2, (x, a, b))).evalf()
sq = sp.Integral((f - g) ** 2, (x, a, b)).evalf()
assert abs(a + 1.965) < 1e-3 and abs(b - 1.058) < 1e-3
assert abs(area - 6.428) < 1e-3 and abs(vol - 125.091) < 1e-3 and abs(sq - 16.353) < 1e-3

FRS = [
    FRQ(1, [3, 4], "Area and volume",
        "Let $R$ be the region enclosed by the graphs of $f(x)=3-x^2$ and $g(x)=e^x-1$. The graphs intersect at $x=a$ and $x=b$, where $a<0<b$.",
        [P("a", "Find the area of $R$.",
           ["integrand $f(x)-g(x)$ with limits $a\\approx-1.965$ and $b\\approx1.058$", "area $\\approx6.428$"],
           ["The intersections (calculator): $a\\approx-1.96464$, $b\\approx1.05801$.", "$\\int_a^b\\big(3-x^2-e^x+1\\big)\\,dx\\approx6.428$."]),
         P("b", "Find the volume of the solid generated when $R$ is revolved about the horizontal line $y=-2$.",
           ["constant $\\pi$ and limits $a$, $b$", "integrand $(f(x)+2)^2-(g(x)+2)^2$", "volume $\\approx125.091$"],
           ["Outer radius $f(x)+2$, inner radius $g(x)+2$ (both curves are above $y=-2$ on $[a,b]$).",
            "$V=\\pi\\int_a^b\\left[(5-x^2)^2-(e^x+1)^2\\right]dx\\approx125.091$."]),
         P("c", "$R$ is the base of a solid whose cross sections perpendicular to the $x$-axis are squares. Find the volume of the solid.",
           ["integrand $(f(x)-g(x))^2$ with limits", "volume $\\approx16.353$"],
           ["$V=\\int_a^b\\big(f(x)-g(x)\\big)^2dx\\approx16.353$."]),
         P("d", "The vertical line $x=k$ divides $R$ into two regions of equal area. Write, but do not solve, an equation involving one or more integrals whose solution gives $k$.",
           ["one integral with limits $a$ and $k$ (or $k$ and $b$) and integrand $f-g$", "set equal to half the area (or to the other piece)"],
           ["$\\int_a^k\\big(f(x)-g(x)\\big)\\,dx=\\frac12\\int_a^b\\big(f(x)-g(x)\\big)\\,dx$, or equivalently $\\int_a^k(f-g)\\,dx=\\int_k^b(f-g)\\,dx$."])],
        calc=True),
]
