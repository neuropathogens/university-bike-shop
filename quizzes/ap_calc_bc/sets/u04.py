"""Unit 4 Practice Set: Contextual Applications of Differentiation (12 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, Table

t, x = sp.symbols("t x")

DOC = dict(
    unit=4, title="Contextual Applications of Differentiation", topics="4.1–4.7",
    pdf="ap-calc-bc-04-contextual-applications-practice.pdf", guide_pdf="ap-calc-bc-04-contextual-applications-guide.pdf",
    sections={"1": "Derivatives in context", "2": "Related rates", "3": "Local linearity and approximation", "4": "L'Hôpital's rule"},
    rules={"1": "R4.1–R4.3. Interpret with value, units and time. $v=x'$, $a=v'$; speed increases when $v$ and $a$ share a sign.",
           "2": "R4.4–R4.5. Relate the quantities, differentiate with respect to $t$, then substitute the instant's values.",
           "3": "R4.6–R4.7. $f(x)\\approx f(a)+f'(a)(x-a)$; concave up means underestimate, concave down means overestimate.",
           "4": "R4.8–R4.9. Confirm $\\frac00$ or $\\frac\\infty\\infty$, then $\\lim\\frac fg=\\lim\\frac{f'}{g'}$; rewrite $1^\\infty$ and $0\\cdot\\infty$ first."},
    abstract="Twelve exam-style multiple-choice questions on Unit 4, grouped by the sections of the Unit 4 Study Guide, and one nine-point free-response question on straight-line motion and L'Hôpital's rule. All items are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (24 min) and 15 minutes for the free response.",
    setup="Allow 24 minutes for the multiple choice and 15 for the free response. No calculator.",
)

# checks
X2 = t**3 - 9 * t**2 + 24 * t
assert sp.expand(sp.diff(X2, t) - 3 * (t - 2) * (t - 4)) == 0
X3 = 2 * t**3 - 15 * t**2 + 36 * t
assert sp.solve(sp.diff(X3, t), t) == [2, 3] and sp.diff(X3, t, 2).subs(t, 2) == -6 and X3.subs(t, 2) == 28
assert 4 * sp.pi * 16 * sp.Rational(1, 2) == 32 * sp.pi
assert sp.Rational(-5 * 2, 12) == sp.Rational(-5, 6)
h = sp.symbols("h")
dhdt = sp.solve(sp.Eq(3, sp.diff(sp.pi * h**3 / 12, h).subs(h, 6) * sp.Symbol("d")), sp.Symbol("d"))[0]
assert sp.simplify(dhdt - 1 / (3 * sp.pi)) == 0
assert sp.limit((1 - sp.cos(2 * x)) / x**2, x, 0) == 2
assert sp.limit((1 + 2 / x) ** (3 * x), x, sp.oo) == sp.exp(6)
XF = 2 * t**3 - 9 * t**2 + 12 * t
vF, aF = sp.diff(XF, t), sp.diff(XF, t, 2)
assert vF.subs(t, sp.Rational(5, 4)) == sp.Rational(-9, 8) and aF.subs(t, sp.Rational(5, 4)) == -3
assert [XF.subs(t, k) for k in range(4)] == [0, 5, 4, 9]
assert sp.limit((XF - 5) / (t - 1) ** 2, t, 1) == -3

QS = [
    Q(1, 1, "R4.1", "$W(t)$ is the number of gallons of water in a tank $t$ hours after noon. Which is the best interpretation of $W'(4)=-6$?",
      ["Four hours after noon the tank holds 6 fewer gallons than it did at noon.",
       "At 4 p.m. the amount of water in the tank is decreasing at 6 gallons per hour.",
       "During the first 4 hours, water leaves the tank at an average rate of 6 gallons per hour.",
       "At 4 p.m. the rate at which water leaves the tank is decreasing by 6 gallons per hour per hour."], "B",
      "A derivative is an instantaneous rate: value, units (gallons per hour), and the time.",
      "$W'(4)$ is the instantaneous rate of change of the amount at $t=4$, in gallons per hour (R4.1).",
      ["The sign is negative: the amount is decreasing.", "Units of $W'$: gallons per hour; the time is $t=4$, that is 4 p.m."],
      {"A": "describes the net change $W(4)-W(0)$, which needs an integral, not a derivative.",
       "C": "describes an average rate over $[0,4]$, not an instantaneous rate at $t=4$.",
       "D": "describes $W''(4)$, with units gallons per hour per hour."}, layout="one"),
    Q(2, 1, "R4.2", "A particle moves along the $x$-axis with position $x(t)=t^3-9t^2+24t$ for $t\\ge0$. For which values of $t$ is the speed of the particle increasing?",
      ["$2<t<4$ only", "$t>3$ only", "$0<t<2$ and $3<t<4$", "$2<t<3$ and $t>4$"], "D",
      "$v=3(t-2)(t-4)$, $a=6t-18$; same signs on $(2,3)$ (both negative) and $t>4$ (both positive).",
      "Speed increases when velocity and acceleration have the same sign (R4.2).",
      ["$v(t)=3t^2-18t+24=3(t-2)(t-4)$: positive on $(0,2)$, negative on $(2,4)$, positive for $t>4$.",
       "$a(t)=6t-18$: negative for $t<3$, positive for $t>3$. Same sign on $(2,3)$ and $(4,\\infty)$."],
      {"A": "is where the particle moves left ($v<0$), not where its speed increases.",
       "B": "is where $a>0$; acceleration alone does not decide speed.",
       "C": "are the intervals where $v$ and $a$ have opposite signs: the particle is slowing down."}, layout="two"),
    Q(3, 1, "R4.2", "A particle has position $x(t)=2t^3-15t^2+36t$. What is its acceleration the first time it is at rest?",
      ["$-6$", "$0$", "$6$", "$28$"], "A",
      "$v=6(t-2)(t-3)$; first rest at $t=2$; $a(2)=24-30=-6$.",
      "At rest means $v=0$; then evaluate $a=v'$ there (R4.2).",
      ["$v(t)=6t^2-30t+36=6(t-2)(t-3)$, so the particle is first at rest at $t=2$.", "$a(t)=12t-30$, $a(2)=-6$."],
      {"B": "is the velocity at that instant, not the acceleration.",
       "C": "is $a(3)$, at the second time the particle is at rest.",
       "D": "is the position $x(2)$."}),
    Q(4, 1, "R4.3", "$P(t)$ is the population of a town, $t$ years after 2020. Which is the best interpretation of $P''(5)=30$?",
      ["In 2025 the population increased by 30 people.",
       "In 2025 the population was 30.",
       "In 2025 the rate of population growth was increasing at 30 people per year per year.",
       "In 2025 the population was increasing at 30 people per year."], "C",
      "$P''$ is the rate of change of the growth rate: people per year per year.",
      "A second derivative says how the rate itself is changing; units are people per year squared (R4.1, R4.3).",
      ["$P'(t)$ is the growth rate, in people per year.", "$P''(5)=30$: at $t=5$ the growth rate is increasing at 30 people per year per year."],
      {"A": "describes a net change over a year, not a rate.",
       "B": "describes $P(5)$.",
       "D": "describes $P'(5)$, the first derivative."}, layout="one"),
    Q(5, 2, "R4.5", "The radius of a sphere increases at 0.5 cm per second. How fast is the volume increasing when the radius is 4 cm? ($V=\\frac43\\pi r^3$)",
      ["$8\\pi$ cm³/s", "$32\\pi$ cm³/s", "$64\\pi$ cm³/s", "$\\frac{256}{3}\\pi$ cm³/s"], "B",
      "$\\frac{dV}{dt}=4\\pi r^2\\frac{dr}{dt}=4\\pi(16)(0.5)$.",
      "Differentiate the relation with respect to $t$, then substitute (R4.4–R4.5).",
      ["$\\frac{dV}{dt}=4\\pi r^2\\frac{dr}{dt}$.", "$4\\pi(16)(0.5)=32\\pi$."],
      {"A": "uses $r$ instead of $r^2$.",
       "C": "forgets the factor $\\frac{dr}{dt}=0.5$.",
       "D": "is the volume at $r=4$, not its rate of change."}),
    Q(6, 2, "R4.4", "A 13-foot ladder leans against a wall. The bottom slides away from the wall at 2 ft/s. How fast is the top sliding down the wall when the bottom is 5 ft from the wall?",
      ["$\\frac{5}{12}$ ft/s", "$\\frac56$ ft/s", "$2$ ft/s", "$\\frac{24}{5}$ ft/s"], "B",
      "$xx'+yy'=0$ with $x=5$, $y=12$, $x'=2$: $y'=-\\frac{10}{12}$.",
      "Relate $x^2+y^2=169$, differentiate, then substitute the instant's values (R4.4).",
      ["When $x=5$, $y=\\sqrt{169-25}=12$.", "$2xx'+2yy'=0$: $5(2)+12y'=0$, $y'=-\\frac56$. The top slides down at $\\frac56$ ft/s."],
      {"A": "forgets the factor $\\frac{dx}{dt}=2$.",
       "C": "assumes the top moves as fast as the bottom; the rates differ unless $x=y$.",
       "D": "swaps $x$ and $y$: $\\frac{12\\cdot2}{5}$."}),
    Q(7, 2, "R4.5", "Water is poured at 3 m³/min into a conical tank, vertex down, 10 m tall with top radius 5 m. How fast is the water level rising when the water is 6 m deep?",
      ["$\\dfrac{1}{48\\pi}$ m/min", "$\\dfrac{1}{9\\pi}$ m/min", "$\\dfrac{1}{3\\pi}$ m/min", "$\\dfrac{1}{\\pi}$ m/min"], "C",
      "$r=\\frac h2$, $V=\\frac{\\pi h^3}{12}$, $3=\\frac{\\pi h^2}{4}h'=9\\pi h'$.",
      "Use similar triangles to remove $r$ before differentiating (R4.4–R4.5).",
      ["$\\frac rh=\\frac5{10}$, so $r=\\frac h2$ and $V=\\frac13\\pi\\frac{h^2}{4}h=\\frac{\\pi h^3}{12}$.",
       "$\\frac{dV}{dt}=\\frac{\\pi h^2}{4}\\frac{dh}{dt}$: $3=9\\pi\\frac{dh}{dt}$, so $\\frac{dh}{dt}=\\frac{1}{3\\pi}$."],
      {"A": "inverts the ratio: $r=2h$, so $V=\\frac43\\pi h^3$.",
       "B": "drops the $\\frac13$ in the cone formula.",
       "D": "substitutes $r=3$ before differentiating, treating the radius as constant: $V=3\\pi h$."}),
    Q(8, 3, "R4.6", "$f$ is differentiable with $f(2)=5$ and $f'(2)=-3$. The tangent-line approximation of $f(2.2)$ is",
      ["$4.4$", "$4.7$", "$5.0$", "$5.6$"], "A",
      "$5+(-3)(0.2)=4.4$.",
      "$f(x)\\approx f(a)+f'(a)(x-a)$ (R4.6).",
      ["$x-a=0.2$.", "$5-3(0.2)=4.4$."],
      {"B": "uses a step of 0.1 instead of 0.2.",
       "C": "is $f(2)$, with no correction.",
       "D": "adds the correction: sign error."}),
    Q(9, 3, "R4.7", "$f(1)=2$, $f'(1)=3$ and $f''(x)=-x^2-1$ for all $x$. Using the line tangent at $x=1$, the approximation of $f(1.2)$ is",
      ["$2.6$, an underestimate", "$2.3$, an overestimate", "$3.6$, an overestimate", "$2.6$, an overestimate"], "D",
      "$2+3(0.2)=2.6$; $f''<0$, so the tangent lies above the curve.",
      "Concave down between the points makes the tangent line an overestimate (R4.6–R4.7).",
      ["$L(1.2)=2+3(0.2)=2.6$.", "$f''(x)=-x^2-1<0$ on $[1,1.2]$: $f$ is concave down, so $L$ overestimates."],
      {"A": "reverses the concavity rule: concave down gives an overestimate.",
       "B": "uses a step of 0.1.",
       "C": "uses $f'(1)\\cdot1.2$ in place of $f'(1)(1.2-1)$."}, layout="two"),
    Q(10, 4, "R4.9", "$\\displaystyle\\lim_{x\\to0}\\frac{1-\\cos 2x}{x^2}$ is",
      ["$0$", "$1$", "$2$", "$4$"], "C",
      "L'Hôpital twice: $\\frac{2\\sin2x}{2x}\\to\\frac{4\\cos2x}{2}=2$.",
      "$\\frac00$: apply L'Hôpital's rule, as many times as the form stays indeterminate (R4.9).",
      ["$\\frac{2\\sin2x}{2x}$ is still $\\frac00$.", "Again: $\\frac{4\\cos2x}{2}\\to2$."],
      {"A": "applies the special limit $\\frac{1-\\cos u}{u}\\to0$, but the denominator here is $x^2$, not $x$.",
       "B": "ignores the 2 inside the cosine.",
       "D": "differentiates the numerator twice but the denominator only once."}),
    Q(11, 4, "R4.9", "Differentiable $f$ and $g$ satisfy $f(3)=g(3)=0$, $f'(3)=4$ and $g'(3)=-2$. What is $\\displaystyle\\lim_{x\\to3}\\frac{f(x)}{g(x)}$?",
      ["$-2$", "$-\\dfrac12$", "$0$", "nonexistent"], "A",
      "$\\frac00$, so the limit is $\\frac{f'(3)}{g'(3)}=-2$.",
      "With $\\frac00$ and continuous derivatives, $\\lim\\frac fg=\\frac{f'(3)}{g'(3)}$ (R4.9).",
      ["$f(3)=g(3)=0$: indeterminate.", "$\\frac{f'(3)}{g'(3)}=\\frac{4}{-2}=-2$."],
      {"B": "inverts the ratio.",
       "C": "reads $\\frac00$ as 0.",
       "D": "treats $\\frac00$ as proof that the limit fails to exist."}),
    Q(12, 4, "R4.8", "$\\displaystyle\\lim_{x\\to\\infty}\\left(1+\\frac2x\\right)^{3x}$ is",
      ["$1$", "$e^2$", "$e^5$", "$e^6$"], "D",
      "$\\ln y=3x\\ln(1+\\frac2x)\\to6$.",
      "$1^\\infty$ is indeterminate: take the log, find its limit with L'Hôpital, then exponentiate (R4.8).",
      ["$\\ln y=\\frac{3\\ln(1+2/x)}{1/x}$, a $\\frac00$ form.", "L'Hôpital: $\\frac{3\\cdot\\frac{-2/x^2}{1+2/x}}{-1/x^2}=\\frac{6}{1+2/x}\\to6$, so the limit is $e^6$."],
      {"A": "treats $1^\\infty$ as 1; it is indeterminate.",
       "B": "ignores the factor 3 in the exponent.",
       "C": "adds the 2 and the 3 instead of multiplying."}),
]

FRS = [
    FRQ(1, [1, 4], "Straight-line motion",
        "A particle moves along the $x$-axis so that its position at time $t\\ge0$ is $x(t)=2t^3-9t^2+12t$.",
        [P("a", "Find the velocity and the acceleration of the particle at $t=\\frac54$. Is the speed of the particle increasing or decreasing at $t=\\frac54$? Give a reason for your answer.",
           ["$v(\\frac54)=-\\frac98$", "$a(\\frac54)=-3$", "speed increasing, because $v$ and $a$ are both negative"],
           ["$v(t)=6t^2-18t+12=6(t-1)(t-2)$, so $v(\\frac54)=6(\\frac14)(-\\frac34)=-\\frac98$.",
            "$a(t)=12t-18$, so $a(\\frac54)=-3$.", "Both are negative, so the speed is increasing at $t=\\frac54$."]),
         P("b", "For $0<t<3$, at what times does the particle change direction? Justify your answer.",
           ["$t=1$ and $t=2$", "justification: $v$ changes sign at each"],
           ["$v=6(t-1)(t-2)$ changes from positive to negative at $t=1$ and from negative to positive at $t=2$, so the particle changes direction at $t=1$ and $t=2$."]),
         P("c", "Find the total distance the particle travels over $0\\le t\\le3$.",
           ["positions at $t=0,1,2,3$: $0,5,4,9$", "total distance 11"],
           ["$x(0)=0$, $x(1)=5$, $x(2)=4$, $x(3)=9$.", "Distance $=|5-0|+|4-5|+|9-4|=5+1+5=11$."]),
         P("d", "Find $\\displaystyle\\lim_{t\\to1}\\frac{x(t)-5}{(t-1)^2}$.",
           ["shows the form is $\\frac00$ and applies L'Hôpital's rule (or factors)", "limit $-3$"],
           ["$x(1)-5=0$ and $(1-1)^2=0$. L'Hôpital: $\\lim\\frac{v(t)}{2(t-1)}$, again $\\frac00$ since $v(1)=0$.",
            "Again: $\\lim\\frac{a(t)}{2}=\\frac{a(1)}{2}=\\frac{-6}{2}=-3$. (Or factor: $x(t)-5=(t-1)^2(2t-5)$.)"])]),
]
