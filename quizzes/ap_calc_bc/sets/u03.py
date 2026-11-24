"""Unit 3 Practice Set: Composite, Implicit, and Inverse Functions (12 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q, Table

x, y = sp.symbols("x y")

DOC = dict(
    unit=3, title="Differentiation: Composite, Implicit, and Inverse Functions", topics="3.1–3.6",
    pdf="ap-calc-bc-03-composite-implicit-inverse-practice.pdf", guide_pdf="ap-calc-bc-03-composite-implicit-inverse-guide.pdf",
    sections={"1": "The chain rule", "2": "Implicit differentiation", "3": "Derivatives of inverse functions",
              "4": "Selecting procedures and higher-order derivatives"},
    rules={"1": "R3.1–R3.2. $\\frac{d}{dx}f(g(x))=f'(g(x))\\,g'(x)$. With a table, find $g(a)$ first, then $f'$ at that output.",
           "2": "R3.3–R3.4. Every $y$-term gets a factor $\\frac{dy}{dx}$. Horizontal tangent: numerator 0; vertical: denominator 0; the point must be on the curve.",
           "3": "R3.5–R3.6. $(f^{-1})'(b)=\\frac{1}{f'(a)}$ where $f(a)=b$. $\\arcsin'=\\frac{1}{\\sqrt{1-x^2}}$, $\\arctan'=\\frac{1}{1+x^2}$.",
           "4": "R3.7–R3.8. Identify the last operation. For an implicit $\\frac{d^2y}{dx^2}$, differentiate $\\frac{dy}{dx}$ and substitute it back."},
    abstract="Twelve exam-style multiple-choice questions on Unit 3, grouped by the sections of the Unit 3 Study Guide, and one nine-point free-response question on an implicitly defined curve. All items are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (24 min) and 15 minutes for the free response.",
    setup="Allow 24 minutes for the multiple choice and 15 for the free response. No calculator.",
)

T34 = Table([["$x$", "$f(x)$", "$f'(x)$", "$g(x)$", "$g'(x)$"], ["1", "4", "$-1$", "3", "2"], ["3", "2", "6", "1", "$-2$"]])

# checks
assert sp.diff((x**2 + 1) ** 5, x).subs(x, 1) == 160
assert sp.simplify(sp.diff(sp.log(sp.cos(x)), x) + sp.tan(x)) == 0
yx = sp.Function("Y")(x)
d5 = sp.solve(sp.diff(x**2 * yx + yx**3 - 10, x), sp.diff(yx, x))[0].subs(yx, 2).subs(x, 1)
assert d5 == sp.Rational(-4, 13)
assert sp.diff(sp.atan(3 * x), x).subs(x, sp.Rational(1, 3)) == sp.Rational(3, 2)
assert sp.diff(x**sp.Rational(3, 2), x, 2).subs(x, 1) == sp.Rational(3, 4)
assert sp.simplify(sp.diff(sp.sin(2 * x), x, 4) - 16 * sp.sin(2 * x)) == 0
fi = x**3 + 2 * x - 1
assert fi.subs(x, 1) == 2 and sp.diff(fi, x).subs(x, 1) == 5 and sp.diff(fi, x).subs(x, 2) == 14
# Q6: x^2 - xy + y^2 = 3; horizontal tangents where y = 2x
assert sp.solve([x**2 - x * y + y**2 - 3, y - 2 * x], [x, y]) == [(-1, -2), (1, 2)]

QS = [
    Q(1, 1, "R3.1", "If $f(x)=(x^2+1)^5$, then $f'(1)=$",
      ["$10$", "$32$", "$80$", "$160$"], "D",
      "$5(x^2+1)^4\\cdot2x=5\\cdot16\\cdot2=160$.",
      "Chain rule: derivative of the outer power at the inside, times the inside's derivative (R3.1).",
      ["$f'(x)=5(x^2+1)^4\\cdot2x$.", "At $x=1$: $5\\cdot2^4\\cdot2=160$."],
      {"A": "differentiates only the inside and multiplies by 5: $5\\cdot2x$.",
       "B": "is $f(1)=2^5$, the value.",
       "C": "forgets the inside derivative $2x$."}),
    Q(2, 1, "R3.1", "$\\dfrac{d}{dx}\\ln(\\cos x)=$",
      ["$-\\tan x$", "$\\dfrac{1}{\\cos x}$", "$-\\dfrac{1}{\\sin x}$", "$\\tan x$"], "A",
      "$\\frac{-\\sin x}{\\cos x}=-\\tan x$.",
      "$\\frac{d}{dx}\\ln u=\\frac{u'}{u}$ (R3.1).",
      ["$u=\\cos x$, $u'=-\\sin x$.", "$\\frac{u'}{u}=\\frac{-\\sin x}{\\cos x}=-\\tan x$."],
      {"B": "forgets the inside derivative $u'=-\\sin x$.",
       "C": "divides 1 by the derivative of $\\cos x$ instead of dividing $u'$ by $u$: $\\frac{1}{u'}$.",
       "D": "drops the minus sign in $\\frac{d}{dx}\\cos x=-\\sin x$."}),
    Q(3, 1, "R3.2", "The table gives values of $f$, $g$ and their derivatives. If $h(x)=f(g(x))$, then $h'(1)=$",
      ["$-2$", "$6$", "$12$", "$18$"], "C",
      "$f'(g(1))g'(1)=f'(3)\\cdot2=12$.",
      "Table composite: evaluate $g(1)$ first, then $f'$ at that output (R3.2).",
      ["$g(1)=3$, so $h'(1)=f'(3)\\cdot g'(1)$.", "$f'(3)=6$, $g'(1)=2$: $h'(1)=12$."],
      {"A": "uses $f'(1)g'(1)=(-1)(2)$, evaluating $f'$ at the input instead of at $g(1)$.",
       "B": "forgets the factor $g'(1)$.",
       "D": "multiplies by $g(1)=3$ instead of $g'(1)=2$."}, table=T34),
    Q(4, 1, "R3.2", "With the same table, if $k(x)=[g(x)]^3$, then $k'(3)=$",
      ["$-6$", "$-2$", "$3$", "$6$"], "A",
      "$3g(3)^2g'(3)=3\\cdot1\\cdot(-2)=-6$.",
      "Power of a function: $\\frac{d}{dx}g^3=3g^2g'$ (R3.1–R3.2).",
      ["$k'(x)=3[g(x)]^2g'(x)$.", "At 3: $g(3)=1$, $g'(3)=-2$, so $k'(3)=3(1)(-2)=-6$."],
      {"B": "reports $g'(3)$ alone.",
       "C": "is $3[g(3)]^2$, missing the factor $g'(3)$.",
       "D": "drops the sign of $g'(3)=-2$."}, table=T34),
    Q(5, 2, "R3.3", "For the curve $x^2y+y^3=10$, the value of $\\dfrac{dy}{dx}$ at the point $(1,2)$ is",
      ["$-16$", "$-\\dfrac13$", "$-\\dfrac{4}{13}$", "$\\dfrac{4}{13}$"], "C",
      "$2xy+x^2y'+3y^2y'=0\\Rightarrow y'=\\frac{-2xy}{x^2+3y^2}=-\\frac{4}{13}$.",
      "Implicit differentiation: product rule on $x^2y$, and $\\frac{dy}{dx}$ on every $y$-term (R3.3).",
      ["$\\frac{d}{dx}(x^2y)=2xy+x^2y'$ and $\\frac{d}{dx}y^3=3y^2y'$.", "$y'(x^2+3y^2)=-2xy$; at $(1,2)$: $y'=\\frac{-4}{1+12}=-\\frac{4}{13}$."],
      {"A": "forgets $\\frac{dy}{dx}$ on $y^3$: $4+y'+12=0$.",
       "B": "skips the product rule on $x^2y$, losing the term $x^2y'$: $\\frac{-4}{12}$.",
       "D": "sign error when moving $2xy$ across."}),
    Q(6, 2, "R3.4", "At which points does the curve $x^2-xy+y^2=3$ have a horizontal tangent line?",
      ["$(2,1)$ and $(-2,-1)$", "$(1,2)$ and $(-1,-2)$", "$(\\sqrt3,0)$ and $(-\\sqrt3,0)$", "$(0,\\sqrt3)$ and $(0,-\\sqrt3)$"], "B",
      "$y'=\\frac{y-2x}{2y-x}$; $y=2x$ on the curve gives $3x^2=3$.",
      "Horizontal tangent: numerator of $\\frac{dy}{dx}$ is 0 (denominator not 0), solved together with the curve (R3.4).",
      ["$2x-y-xy'+2yy'=0$, so $\\frac{dy}{dx}=\\frac{y-2x}{2y-x}$.",
       "Numerator 0: $y=2x$. Substitute: $x^2-2x^2+4x^2=3x^2=3$, so $x=\\pm1$: $(1,2)$ and $(-1,-2)$. Denominators: $2(2)-1=3\\neq0$."],
      {"A": "are where the denominator is 0: the vertical tangents.",
       "C": "are the $x$-intercepts; there $y'=\\frac{-2x}{-x}=2$.",
       "D": "are the $y$-intercepts; there $y'=\\frac{y}{2y}=\\frac12$."}, layout="two"),
    Q(7, 3, "R3.5", "Let $f(x)=x^3+2x-1$ and let $g$ be the inverse of $f$. What is $g'(2)$?",
      ["$\\dfrac{1}{14}$", "$\\dfrac15$", "$5$", "$14$"], "B",
      "$f(1)=2$, so $g'(2)=\\frac{1}{f'(1)}=\\frac15$.",
      "$(f^{-1})'(b)=\\frac{1}{f'(a)}$ where $f(a)=b$ (R3.5).",
      ["Solve $f(a)=2$: $a=1$ ($1+2-1$).", "$f'(x)=3x^2+2$, $f'(1)=5$, so $g'(2)=\\frac15$."],
      {"A": "uses $\\frac{1}{f'(2)}$: evaluates $f'$ at $b$ instead of at $a=g(b)$.",
       "C": "forgets the reciprocal.",
       "D": "is $f'(2)$: both mistakes at once."}),
    Q(8, 3, "R3.5", "A differentiable, invertible $f$ has $f(3)=7$, $f'(3)=4$, $f(7)=10$ and $f'(7)=-\\frac12$. If $g=f^{-1}$, then $g'(7)=$",
      ["$-2$", "$\\dfrac{1}{10}$", "$\\dfrac14$", "$4$"], "C",
      "$g(7)=3$, so $g'(7)=\\frac{1}{f'(3)}=\\frac14$.",
      "$g'(b)=\\frac{1}{f'(g(b))}$: first find which input of $f$ gives 7 (R3.5).",
      ["$f(3)=7$, so $g(7)=3$.", "$g'(7)=\\frac{1}{f'(3)}=\\frac14$."],
      {"A": "uses $\\frac{1}{f'(7)}$, evaluating $f'$ at 7 instead of at $g(7)=3$.",
       "B": "uses $\\frac{1}{f(7)}$, a value instead of a derivative.",
       "D": "forgets the reciprocal: $f'(3)$."}),
    Q(9, 3, "R3.6", "If $y=\\arctan(3x)$, then $\\dfrac{dy}{dx}$ at $x=\\frac13$ is",
      ["$\\dfrac12$", "$\\dfrac32$", "$\\dfrac94$", "$3$"], "B",
      "$\\frac{3}{1+(3x)^2}=\\frac{3}{2}$.",
      "$\\frac{d}{dx}\\arctan u=\\frac{u'}{1+u^2}$ (R3.6).",
      ["$u=3x$, $u'=3$: $y'=\\frac{3}{1+9x^2}$.", "At $x=\\frac13$: $\\frac{3}{1+1}=\\frac32$."],
      {"A": "forgets the chain factor $u'=3$.",
       "C": "squares only $x$, not $3x$: $\\frac{3}{1+3x^2}=\\frac{3}{4/3}$.",
       "D": "drops the $u^2$ term in the denominator."}),
    Q(10, 3, "R3.6", "$\\dfrac{d}{dx}\\arcsin(x^2)=$",
      ["$\\dfrac{1}{\\sqrt{1-x^4}}$", "$\\dfrac{2x}{\\sqrt{1-x^2}}$", "$-\\dfrac{2x}{\\sqrt{1-x^4}}$", "$\\dfrac{2x}{\\sqrt{1-x^4}}$"], "D",
      "$\\frac{u'}{\\sqrt{1-u^2}}$ with $u=x^2$.",
      "$\\frac{d}{dx}\\arcsin u=\\frac{u'}{\\sqrt{1-u^2}}$ (R3.6).",
      ["$u=x^2$, $u'=2x$, $u^2=x^4$.", "$\\frac{2x}{\\sqrt{1-x^4}}$."],
      {"A": "forgets the chain factor $u'=2x$.",
       "B": "uses $x^2$ instead of $u^2=x^4$ under the root.",
       "C": "has the sign of $\\arccos$'s derivative."}),
    Q(11, 4, "R3.8", "For the curve $y^2=x^3$ with $y>0$, $\\dfrac{d^2y}{dx^2}$ at the point $(1,1)$ is",
      ["$\\dfrac34$", "$\\dfrac32$", "$3$", "$\\dfrac{21}{4}$"], "A",
      "$y'=\\frac{3x^2}{2y}=\\frac32$; $y''=\\frac{6x(2y)-3x^2(2y')}{4y^2}=\\frac{12-9}{4}$.",
      "Implicit second derivative: differentiate $\\frac{dy}{dx}$ with the quotient rule, keeping $y'$, then substitute (R3.8).",
      ["$2yy'=3x^2$, so $y'=\\frac{3x^2}{2y}$; at $(1,1)$, $y'=\\frac32$.",
       "$y''=\\frac{6x\\cdot2y-3x^2\\cdot2y'}{(2y)^2}=\\frac{12-9}{4}=\\frac34$. (Check: $y=x^{3/2}$ gives $y''=\\frac34x^{-1/2}$.)"],
      {"B": "is $\\frac{dy}{dx}$, the first derivative.",
       "C": "treats $y$ as a constant when differentiating $\\frac{3x^2}{2y}$, losing the $-3x^2\\cdot2y'$ term.",
       "D": "adds the two terms of the quotient-rule numerator instead of subtracting."}),
    Q(12, 4, "R3.7", "If $f(x)=\\sin(2x)$, then $f^{(4)}(x)$, the fourth derivative, is",
      ["$-16\\sin(2x)$", "$8\\cos(2x)$", "$16\\cos(2x)$", "$16\\sin(2x)$"], "D",
      "Each derivative multiplies by 2 and cycles $\\sin\\to\\cos\\to-\\sin\\to-\\cos\\to\\sin$.",
      "Repeated chain rule: each differentiation contributes a factor 2, and four steps return to $\\sin$ (R3.1, R3.8).",
      ["$f'=2\\cos2x$, $f''=-4\\sin2x$, $f'''=-8\\cos2x$.", "$f^{(4)}=16\\sin2x$."],
      {"A": "keeps the minus sign from $f''$; two sign changes cancel by the fourth derivative.",
       "B": "is $-f'''$: three differentiations, not four, with a sign slip.",
       "C": "lands on cosine; four steps return to sine."}, layout="two"),
]

# FRQ: y^2 + xy - x^2 = 5
G = y**2 + x * y - x**2 - 5
dydx = -sp.diff(G, x) / sp.diff(G, y)
assert sp.simplify(dydx - (2 * x - y) / (2 * y + x)) == 0
assert G.subs({x: 1, y: -3}) == 0 and dydx.subs({x: 1, y: -3}) == -1
assert sp.solve(G.subs(x, -2 * y), y) == [-sp.I, sp.I]  # no real vertical tangents
yp = sp.symbols("yp")
d2 = ((2 - yp) * (2 * y + x) - (2 * x - y) * (2 * yp + 1)) / (2 * y + x) ** 2
assert d2.subs({x: 1, y: -3, yp: -1}) == sp.Rational(-2, 5)

FRS = [
    FRQ(1, [2, 4], "An implicitly defined curve",
        "Consider the curve given by $y^2+xy-x^2=5$.",
        [P("a", "Show that $\\dfrac{dy}{dx}=\\dfrac{2x-y}{2y+x}$.",
           ["implicit differentiation of all three terms (with the product rule on $xy$)", "algebra leading to the given expression"],
           ["$2y\\frac{dy}{dx}+y+x\\frac{dy}{dx}-2x=0$, so $\\frac{dy}{dx}(2y+x)=2x-y$ and $\\frac{dy}{dx}=\\frac{2x-y}{2y+x}$."]),
         P("b", "The point $(1,-3)$ is on the curve. Write an equation for the line tangent to the curve at this point.",
           ["slope $-1$", "tangent line $y=-3-(x-1)$"],
           ["At $(1,-3)$: $\\frac{dy}{dx}=\\frac{2+3}{-6+1}=-1$. Tangent: $y=-3-(x-1)$."]),
         P("c", "Show that the curve has no vertical tangent lines.",
           ["sets $2y+x=0$", "substitutes $x=-2y$ into the curve: $-5y^2=5$", "concludes: no real solution, so no vertical tangent"],
           ["A vertical tangent needs $2y+x=0$, so $x=-2y$.",
            "Then $y^2-2y^2-4y^2=-5y^2=5$, so $y^2=-1$, which has no real solution.",
            "No point of the curve has $2y+x=0$, so there is no vertical tangent."]),
         P("d", "Find the value of $\\dfrac{d^2y}{dx^2}$ at the point $(1,-3)$.",
           ["quotient rule applied to $\\frac{dy}{dx}$ with $\\frac{dy}{dx}$ retained", "value $-\\frac25$"],
           ["$\\frac{d^2y}{dx^2}=\\frac{(2-y')(2y+x)-(2x-y)(2y'+1)}{(2y+x)^2}$.",
            "At $(1,-3)$ with $y'=-1$: $\\frac{(3)(-5)-(5)(-1)}{25}=\\frac{-10}{25}=-\\frac25$."])]),
]
