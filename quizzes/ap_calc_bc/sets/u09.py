"""Unit 9 Practice Set: Parametric Equations, Polar Coordinates, and Vector-Valued Functions (15 MC + 1 FRQ)."""
import sympy as sp

from ap_calc_bc.model import FRQ, P, Q

t, th = sp.symbols("t theta")

DOC = dict(
    unit=9, title="Parametric Equations, Polar Coordinates, and Vector-Valued Functions", topics="9.1–9.9",
    pdf="ap-calc-bc-09-parametric-polar-vector-practice.pdf", guide_pdf="ap-calc-bc-09-parametric-polar-vector-guide.pdf",
    sections={"1": "Parametric curves and their derivatives", "2": "Parametric arc length",
              "3": "Vector-valued functions and planar motion", "4": "Polar curves and their derivatives", "5": "Area in polar coordinates"},
    rules={"1": "R9.1–R9.2. $\\frac{dy}{dx}=\\frac{y'(t)}{x'(t)}$; $\\frac{d^2y}{dx^2}=\\frac{d}{dt}\\!\\left(\\frac{dy}{dx}\\right)\\big/x'(t)$.",
           "2": "R9.3. $L=\\int\\sqrt{x'(t)^2+y'(t)^2}\\,dt$.",
           "3": "R9.4–R9.5. Speed $\\sqrt{x'^2+y'^2}$; position = initial position + $\\int$ velocity, componentwise.",
           "4": "R9.6–R9.8. $x=r\\cos\\theta$, $y=r\\sin\\theta$; distance from the origin grows when $r$ and $\\frac{dr}{d\\theta}$ share a sign.",
           "5": "R9.9–R9.10. $A=\\frac12\\int r^2\\,d\\theta$; between curves $\\frac12\\int(r_{\\text{out}}^2-r_{\\text{in}}^2)\\,d\\theta$."},
    abstract="Fifteen exam-style multiple-choice questions on Unit 9, grouped by the sections of the Unit 9 Study Guide, and one nine-point calculator-active free-response question on a particle moving in the plane. Items marked [calculator] allow a graphing calculator; the rest are no-calculator. Write each answer in the blank beside the number; the key on the last pages gives an answers-only strip, a reason and rule for every item, and the free-response scoring guide.",
    pace="Exam pace: about 2 minutes per multiple-choice item (30 min) and 15 minutes for the free response.",
    setup="Allow 30 minutes for the multiple choice and 15 for the free response. Items 8 and 15 and the free response need a graphing calculator.",
    frnote="Calculator required. Show the integral or expression you evaluate, and give decimal answers correct to three places.",
)

# checks
x1, y1 = t**2 + 1, t**3 - t
assert (sp.diff(y1, t) / sp.diff(x1, t)).subs(t, 2) == sp.Rational(11, 4)
x2, y2 = t**3 - 3 * t, t**2 - 4 * t
assert sp.solve(sp.diff(y2, t), t) == [2] and (x2.subs(t, 2), y2.subs(t, 2)) == (2, -4)
x3, y3 = t**2 + t, t**3
d1 = sp.diff(y3, t) / sp.diff(x3, t)
assert sp.simplify(sp.diff(d1, t) / sp.diff(x3, t)).subs(t, 1) == sp.Rational(4, 9)
assert sp.integrate(2 * t * sp.sqrt(1 + t**2), (t, 0, 1)) == sp.Rational(2, 3) * (2 * sp.sqrt(2) - 1)
assert sp.sqrt(9 + 16) == 5
assert abs(sp.Integral(sp.sqrt(sp.cos(t**2) ** 2 + sp.sin(t) ** 2), (t, 0, 2)).evalf() - 2.207) < 5e-4
r = 1 + sp.cos(th)
dy, dx = sp.diff(r * sp.sin(th), th), sp.diff(r * sp.cos(th), th)
assert sp.simplify(dy / dx).subs(th, sp.pi / 2) == 1
r12 = 2 * sp.cos(2 * th)
assert r12.subs(th, sp.pi / 3) == -1 and sp.diff(r12, th).subs(th, sp.pi / 3) == -2 * sp.sqrt(3)
assert sp.integrate(sp.sin(3 * th) ** 2 / 2, (th, 0, sp.pi / 3)) == sp.pi / 12
assert sp.integrate((9 * sp.cos(th) ** 2 - (1 + sp.cos(th)) ** 2) / 2, (th, -sp.pi / 3, sp.pi / 3)) == sp.pi
assert abs(sp.Integral((th + sp.sin(th)) ** 2 / 2, (th, 0, sp.pi)).evalf() - 9.095) < 5e-4

QS = [
    Q(1, 1, "R9.1", "For the curve $x=t^2+1$, $y=t^3-t$, the value of $\\dfrac{dy}{dx}$ at $t=2$ is",
      ["$\\dfrac{4}{11}$", "$\\dfrac{11}{4}$", "$6$", "$11$"], "B",
      "$\\frac{3t^2-1}{2t}=\\frac{11}{4}$.",
      "$\\frac{dy}{dx}=\\frac{dy/dt}{dx/dt}$ (R9.1).",
      ["$\\frac{dy}{dt}=3t^2-1=11$ and $\\frac{dx}{dt}=2t=4$ at $t=2$.", "$\\frac{dy}{dx}=\\frac{11}{4}$."],
      {"A": "inverts the quotient.",
       "C": "divides second derivatives: $\\frac{6t}{2}$.",
       "D": "forgets to divide by $\\frac{dx}{dt}$."}),
    Q(2, 1, "R9.1", "At what point does the curve $x=t^3-3t$, $y=t^2-4t$ have a horizontal tangent line?",
      ["$(2,-4)$", "$(-2,-3)$", "$(2,5)$", "$(0,0)$"], "A",
      "$\\frac{dy}{dt}=2t-4=0$ at $t=2$, where $\\frac{dx}{dt}=9\\neq0$.",
      "Horizontal tangent: $\\frac{dy}{dt}=0$ with $\\frac{dx}{dt}\\neq0$ (R9.1).",
      ["$\\frac{dy}{dt}=0$ at $t=2$; $\\frac{dx}{dt}=3(4)-3=9$.", "Point: $x=8-6=2$, $y=4-8=-4$."],
      {"B": "is at $t=1$, where $\\frac{dx}{dt}=0$: a vertical tangent.",
       "C": "is at $t=-1$, also a vertical tangent.",
       "D": "is at $t=0$, where the slope is $\\frac{-4}{-3}\\neq0$."}),
    Q(3, 1, "R9.2", "For $x=t^2+t$, $y=t^3$, the value of $\\dfrac{d^2y}{dx^2}$ at $t=1$ is",
      ["$\\dfrac49$", "$1$", "$\\dfrac43$", "$3$"], "A",
      "$\\frac{d}{dt}\\frac{3t^2}{2t+1}=\\frac{6t^2+6t}{(2t+1)^2}=\\frac{12}{9}$; divide by $x'(1)=3$.",
      "$\\frac{d^2y}{dx^2}=\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)\\Big/\\frac{dx}{dt}$ (R9.2).",
      ["$\\frac{dy}{dx}=\\frac{3t^2}{2t+1}$; its $t$-derivative is $\\frac{6t(2t+1)-6t^2}{(2t+1)^2}=\\frac{6t^2+6t}{(2t+1)^2}$, which is $\\frac43$ at $t=1$.",
       "Divide by $\\frac{dx}{dt}=2t+1=3$: $\\frac{4}{9}$."],
      {"B": "is $\\frac{dy}{dx}$ at $t=1$.",
       "C": "forgets the final division by $\\frac{dx}{dt}$.",
       "D": "divides second derivatives: $\\frac{y''(1)}{x''(1)}=\\frac62$."}),
    Q(4, 2, "R9.3", "What is the length of the path $x=t^2$, $y=\\frac23t^3$ for $0\\le t\\le1$?",
      ["$\\dfrac{\\sqrt{13}}{3}$", "$\\dfrac23\\left(2\\sqrt2-1\\right)$", "$\\dfrac53$", "$\\dfrac{4\\sqrt2}{3}$"], "B",
      "Speed $=\\sqrt{4t^2+4t^4}=2t\\sqrt{1+t^2}$; integrate.",
      "Parametric arc length is the integral of speed (R9.3).",
      ["$x'=2t$, $y'=2t^2$: speed $2t\\sqrt{1+t^2}$.", "$\\int_0^12t\\sqrt{1+t^2}\\,dt=\\frac23\\left[(1+t^2)^{3/2}\\right]_0^1=\\frac23(2\\sqrt2-1)\\approx1.219$."],
      {"A": "is the straight-line distance from $(0,0)$ to $(1,\\frac23)$, a lower bound.",
       "C": "adds the components instead of using the Pythagorean speed.",
       "D": "drops the lower-limit term $-\\frac23$."}, layout="four"),
    Q(5, 3, "R9.4", "A particle has velocity $\\langle3t^2,\\,4t\\rangle$. What is its speed at $t=1$?",
      ["$\\sqrt7$", "$5$", "$7$", "$25$"], "B",
      "$\\sqrt{3^2+4^2}=5$.",
      "Speed is the magnitude of the velocity vector (R9.4).",
      ["At $t=1$: $\\langle3,4\\rangle$.", "$\\sqrt{9+16}=5$."],
      {"A": "takes the square root of the sum of the components.",
       "C": "adds the components.",
       "D": "forgets the square root."}),
    Q(6, 3, "R9.4", "A particle's position is $\\langle\\sin2t,\\,t^3\\rangle$. Its acceleration vector at $t=\\frac\\pi4$ is",
      ["$\\left\\langle0,\\,\\frac{3\\pi^2}{16}\\right\\rangle$", "$\\left\\langle4,\\,\\frac{3\\pi}{2}\\right\\rangle$", "$\\left\\langle-4,\\,\\frac{3\\pi^2}{16}\\right\\rangle$", "$\\left\\langle-4,\\,\\frac{3\\pi}{2}\\right\\rangle$"], "D",
      "$\\langle-4\\sin2t,\\,6t\\rangle$ at $\\frac\\pi4$.",
      "Differentiate each component twice (R9.4).",
      ["$v=\\langle2\\cos2t,3t^2\\rangle$, $a=\\langle-4\\sin2t,6t\\rangle$.", "At $\\frac\\pi4$: $\\langle-4,\\frac{6\\pi}{4}\\rangle=\\langle-4,\\frac{3\\pi}{2}\\rangle$."],
      {"A": "is the velocity vector.",
       "B": "loses the sign from $\\frac{d}{dt}\\cos2t=-2\\sin2t$.",
       "C": "mixes the acceleration's first component with the velocity's second."}, layout="two"),
    Q(7, 3, "R9.5", "A particle has velocity $\\langle2t,\\,e^t\\rangle$ and is at $(1,3)$ when $t=0$. Where is it at $t=1$?",
      ["$(1,e)$", "$(3,e+2)$", "$(2,e+2)$", "$(2,e+3)$"], "C",
      "$x=1+\\int_0^12t\\,dt=2$; $y=3+\\int_0^1e^t\\,dt=3+e-1$.",
      "Position = initial position + integral of velocity, componentwise (R9.5).",
      ["$x(1)=1+1=2$.", "$y(1)=3+(e-1)=e+2$."],
      {"A": "evaluates the antiderivatives $t^2$ and $e^t$ at $t=1$, with no initial position and no lower-limit values.",
       "B": "adds the velocity at $t=1$ to $x(0)$: $1+2$.",
       "D": "uses $\\int_0^1e^t\\,dt=e$, forgetting $e^0=1$ at the lower limit."}, layout="four"),
    Q(8, 3, "R9.5", "A particle moves with velocity $\\langle\\cos(t^2),\\,\\sin t\\rangle$. What is the total distance it travels for $0\\le t\\le2$?",
      ["$1.416$", "$1.489$", "$2.207$", "$2.472$"], "C",
      "$\\int_0^2\\sqrt{\\cos^2(t^2)+\\sin^2t}\\,dt\\approx2.207$.",
      "Distance traveled is the integral of speed (R9.5).",
      ["Speed $=\\sqrt{\\cos^2(t^2)+\\sin^2t}$.", "$\\int_0^2(\\text{speed})\\,dt\\approx2.207$ (calculator)."],
      {"A": "integrates only the $y$-component, $\\int_0^2\\sin t\\,dt$.",
       "B": "is the length of the displacement vector, not the distance along the path.",
       "D": "forgets the square root in the speed."}, calc=True),
    Q(9, 3, "R9.4", "A particle has velocity $\\langle t^2-4,\\,3-t\\rangle$ for $0<t<5$. For which $t$ is it moving left and up?",
      ["$0<t<2$", "$2<t<3$", "$3<t<5$", "$0<t<3$"], "A",
      "Left: $x'<0$ for $t<2$; up: $y'>0$ for $t<3$.",
      "Signs of the velocity components give the direction (R9.4).",
      ["$x'=t^2-4<0$ on $(0,2)$.", "$y'=3-t>0$ on $(0,3)$. Both: $(0,2)$."],
      {"B": "is moving right and up.",
       "C": "is moving right and down.",
       "D": "includes $(2,3)$, where the particle moves right."}),
    Q(10, 4, "R9.6", "Which rectangular equation is equivalent to $r=6\\sin\\theta$?",
      ["$x^2+y^2=6x$", "$y=6$", "$x^2+y^2=36$", "$x^2+y^2=6y$"], "D",
      "Multiply by $r$: $r^2=6r\\sin\\theta$.",
      "Use $r^2=x^2+y^2$ and $y=r\\sin\\theta$ (R9.6).",
      ["$r^2=6r\\sin\\theta$.", "$x^2+y^2=6y$: a circle of radius 3 centered at $(0,3)$."],
      {"A": "converts $r=6\\cos\\theta$.",
       "B": "converts $r\\sin\\theta=6$.",
       "C": "converts $r=6$."}, layout="four"),
    Q(11, 4, "R9.7", "For the polar curve $r=1+\\cos\\theta$, the slope $\\dfrac{dy}{dx}$ at $\\theta=\\frac\\pi2$ is",
      ["$-1$", "$0$", "$1$", "undefined"], "C",
      "$\\frac{dy}{d\\theta}=-1$ and $\\frac{dx}{d\\theta}=-1$ at $\\frac\\pi2$.",
      "$\\frac{dy}{dx}=\\frac{dy/d\\theta}{dx/d\\theta}$ with $y=r\\sin\\theta$, $x=r\\cos\\theta$ (R9.7).",
      ["At $\\frac\\pi2$: $r=1$, $r'=-\\sin\\theta=-1$.", "$\\frac{dy}{d\\theta}=r'\\sin\\theta+r\\cos\\theta=-1$; $\\frac{dx}{d\\theta}=r'\\cos\\theta-r\\sin\\theta=-1$. Slope 1."],
      {"A": "is $\\frac{dr}{d\\theta}$, not $\\frac{dy}{dx}$.",
       "B": "takes $\\frac{dy}{d\\theta}=r\\cos\\theta=0$, dropping the $r'\\sin\\theta$ term.",
       "D": "takes $\\frac{dx}{d\\theta}=r'\\cos\\theta=0$, dropping the $-r\\sin\\theta$ term."}),
    Q(12, 4, "R9.8", "For $r=2\\cos(2\\theta)$ at $\\theta=\\frac\\pi3$, which statement is true?",
      ["The point moves toward the origin, because $\\frac{dr}{d\\theta}<0$.",
       "The point moves away from the origin, because $r$ and $\\frac{dr}{d\\theta}$ are both negative.",
       "The point moves toward the origin, because $r<0$.",
       "The point moves away from the origin, because $\\frac{dr}{d\\theta}>0$."], "B",
      "$r=-1$, $r'=-2\\sqrt3$: same sign, so $|r|$ increases.",
      "Distance from the origin is $|r|$; it grows when $r$ and $\\frac{dr}{d\\theta}$ have the same sign (R9.8).",
      ["$r(\\frac\\pi3)=2\\cos\\frac{2\\pi}3=-1$.", "$\\frac{dr}{d\\theta}=-4\\sin2\\theta=-2\\sqrt3<0$. Both negative: $|r|$ increases, so the point moves away."],
      {"A": "uses the sign of $\\frac{dr}{d\\theta}$ alone; that rule holds only when $r>0$.",
       "C": "the sign of $r$ alone says where the point is plotted, not how its distance changes.",
       "D": "$\\frac{dr}{d\\theta}=-2\\sqrt3$ is negative."}, layout="one"),
    Q(13, 5, "R9.9", "The area of one petal of the rose $r=\\sin3\\theta$ is",
      ["$\\dfrac{\\pi}{12}$", "$\\dfrac{\\pi}{6}$", "$\\dfrac{\\pi}{4}$", "$\\dfrac{\\pi}{3}$"], "A",
      "$\\frac12\\int_0^{\\pi/3}\\sin^23\\theta\\,d\\theta=\\frac{\\pi}{12}$.",
      "One petal is traced from $\\theta=0$ to $\\frac\\pi3$; area $\\frac12\\int r^2$ (R9.9).",
      ["$r=0$ at $\\theta=0$ and $\\frac\\pi3$.", "$\\frac12\\int_0^{\\pi/3}\\frac{1-\\cos6\\theta}{2}\\,d\\theta=\\frac12\\cdot\\frac{\\pi}{6}=\\frac{\\pi}{12}$."],
      {"B": "forgets the $\\frac12$ in the area formula.",
       "C": "is the area of all three petals.",
       "D": "is the length of the $\\theta$-interval."}),
    Q(14, 5, "R9.10", "Which expression gives the area inside $r=3\\cos\\theta$ and outside $r=1+\\cos\\theta$?",
      ["$\\displaystyle\\frac12\\int_{-\\pi/3}^{\\pi/3}(2\\cos\\theta-1)^2\\,d\\theta$",
       "$\\displaystyle\\frac12\\int_{0}^{\\pi/3}\\left(9\\cos^2\\theta-(1+\\cos\\theta)^2\\right)d\\theta$",
       "$\\displaystyle\\frac12\\int_{-\\pi/3}^{\\pi/3}\\left(9\\cos^2\\theta-(1+\\cos\\theta)^2\\right)d\\theta$",
       "$\\displaystyle\\int_{-\\pi/3}^{\\pi/3}\\left(9\\cos^2\\theta-(1+\\cos\\theta)^2\\right)d\\theta$"], "C",
      "Intersections at $\\cos\\theta=\\frac12$; outer minus inner, each squared; the area is $\\pi$.",
      "Area between polar curves: $\\frac12\\int(r_{\\text{out}}^2-r_{\\text{in}}^2)$ between intersections (R9.10).",
      ["$3\\cos\\theta=1+\\cos\\theta$ at $\\theta=\\pm\\frac\\pi3$.", "On $(-\\frac\\pi3,\\frac\\pi3)$, $3\\cos\\theta$ is outside. The integral equals $\\pi$."],
      {"A": "squares the difference of the radii instead of subtracting the squares.",
       "B": "covers only the upper half of the region.",
       "D": "forgets the $\\frac12$."}, layout="one"),
    Q(15, 5, "R9.9", "What is the area of the region bounded by the polar curve $r=\\theta+\\sin\\theta$ for $0\\le\\theta\\le\\pi$ (and the $x$-axis)?",
      ["$3.467$", "$5.168$", "$5.953$", "$9.095$"], "D",
      "$\\frac12\\int_0^\\pi(\\theta+\\sin\\theta)^2\\,d\\theta\\approx9.095$.",
      "Polar area with the calculator (R9.9).",
      ["$A=\\frac12\\int_0^\\pi r^2\\,d\\theta$.", "$\\frac12\\int_0^\\pi(\\theta+\\sin\\theta)^2\\,d\\theta\\approx9.095$."],
      {"A": "forgets to square $r$: $\\frac12\\int_0^\\pi r\\,d\\theta$.",
       "B": "drops the $\\sin\\theta$ term entirely: $\\frac12\\int_0^\\pi\\theta^2\\,d\\theta=\\frac{\\pi^3}{6}$.",
       "C": "squares term by term, losing the cross term $2\\theta\\sin\\theta$."}, calc=True),
]

# FRQ: particle in the plane
xp, yp = sp.log(t**2 + 1) - 1, 2 * sp.sin(t)
assert abs(sp.sqrt(xp**2 + yp**2).subs(t, 2).evalf() - 1.918) < 5e-4
assert sp.diff(xp, t).subs(t, 2) == sp.Rational(4, 5) and abs(sp.diff(yp, t).subs(t, 2).evalf() + 0.832) < 5e-4
assert abs((4 + sp.integrate(yp, (t, 0, 3))).evalf() - 7.980) < 5e-4
assert abs(sp.Integral(sp.sqrt(xp**2 + yp**2), (t, 0, 3)).evalf() - 4.786) < 5e-4
assert abs((1 + sp.Integral(xp, (t, 0, 1))).evalf() - 0.264) < 5e-4 and abs((4 + sp.integrate(yp, (t, 0, 1))).evalf() - 4.919) < 5e-4
assert abs((yp / xp).subs(t, 1).evalf() + 5.485) < 5e-4

FRS = [
    FRQ(1, [3, 1], "A particle moving in the plane",
        "A particle moves in the $xy$-plane so that $\\dfrac{dx}{dt}=\\ln(t^2+1)-1$ and $\\dfrac{dy}{dt}=2\\sin t$ for $t\\ge0$. At $t=0$ the particle is at $(1,4)$.",
        [P("a", "Find the speed of the particle at $t=2$, and find its acceleration vector at $t=2$.",
           ["speed $\\approx1.918$", "acceleration $\\langle0.8,\\,-0.832\\rangle$"],
           ["Speed $=\\sqrt{x'(2)^2+y'(2)^2}=\\sqrt{(\\ln5-1)^2+(2\\sin2)^2}\\approx1.918$.",
            "$a(2)=\\left\\langle\\frac{2t}{t^2+1},\\,2\\cos t\\right\\rangle_{t=2}=\\langle0.8,\\,-0.832\\rangle$."]),
         P("b", "Find the $y$-coordinate of the particle's position at $t=3$.",
           ["$4+\\int_0^3 2\\sin t\\,dt$", "$y(3)\\approx7.980$"],
           ["$y(3)=4+\\int_0^32\\sin t\\,dt=4+2(1-\\cos3)\\approx7.980$."]),
         P("c", "Find the total distance traveled by the particle over $0\\le t\\le3$.",
           ["integral of speed with limits 0 and 3", "distance $\\approx4.786$"],
           ["$\\int_0^3\\sqrt{(\\ln(t^2+1)-1)^2+4\\sin^2t}\\,dt\\approx4.786$."]),
         P("d", "Find the position of the particle at $t=1$, and write an equation for the line tangent to its path at that point.",
           ["$x(1)=1+\\int_0^1x'(t)\\,dt\\approx0.264$ and $y(1)\\approx4.919$", "slope $\\frac{dy}{dx}\\approx-5.485$", "tangent line $y=4.919-5.485(x-0.264)$"],
           ["$x(1)=1+\\int_0^1(\\ln(t^2+1)-1)\\,dt\\approx0.264$; $y(1)=4+2(1-\\cos1)\\approx4.919$.",
            "$\\frac{dy}{dx}=\\frac{2\\sin1}{\\ln2-1}\\approx-5.485$.",
            "Tangent: $y=4.919-5.485(x-0.264)$."])],
        calc=True),
]
