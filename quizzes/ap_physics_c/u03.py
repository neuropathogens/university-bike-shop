from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Kinetic energy and work (3.1--3.2)", ["3.1", "3.2"], r"""
\[ K = \tfrac12 mv^2, \qquad W = \int_{x_1}^{x_2} F_x\,dx \;\; (1\text{D}), \qquad W = \int \vec F\cdot d\vec r, \qquad W_{net} = \Delta K. \]
\begin{terms}
Work by a constant force & $W = \vec F\cdot\Delta\vec r = Fd\cos\theta$. Positive if the force has a component along the motion, negative if against it, zero if perpendicular (normal force on a level road, the string tension in uniform circular motion). \\
Work from a graph & Area under the $F$--$x$ curve (area below the axis is negative work). \\
Work by a spring & Stretching from $x_1$ to $x_2$, the spring does $W_s = -\left(\tfrac12 kx_2^2 - \tfrac12 kx_1^2\right)$. \\
Work--energy theorem & The \emph{net} work by all forces equals the change in kinetic energy. \\
Dot product & $\vec A\cdot\vec B = A_xB_x + A_yB_y + A_zB_z = AB\cos\theta$. \\
\end{terms}

\begin{trap}
$W = Fd$ assumes a constant force along the motion. For $F(x) = 5x^2$, the work from $x = 1$ to $3$ m is $\int_1^3 5x^2\,dx = 43$ J, not $F(3)\times 2 = 90$ J.
\end{trap}
""", checks=[
    Q("3.2 Work from F(x)", r"A force $F(x) = 3x^2$ (newtons, $x$ in meters) acts along $x$ on an object that moves from $x = 0$ to $x = 2.0$ m. How much work does the force do?",
      r"$8.0$ J", [r"$12$ J", r"$24$ J", r"$2.7$ J"],
      r"$W = \int_0^2 3x^2\,dx = x^3\big|_0^2 = 8.0$ J.",
      [r"Integrate the force over the displacement.", r"$x^3$ from 0 to 2 gives 8.0 J."],
      [r"is the triangle $\tfrac12(2.0)(12)$, which assumes $F$ grows linearly; $3x^2$ curves upward, so the area is smaller.", r"is $F(2) \times 2.0$ m, which treats the largest force as constant.", r"integrates $x^2$ but drops the coefficient 3: $\tfrac13 x^3 = 2.7$."], sort=True),
])

S2 = Sec("Potential energy and energy diagrams (3.3)", ["3.3"], r"""
For a conservative force (work independent of path), define potential energy by
\[ \Delta U = -\int_{x_1}^{x_2} F_x\,dx, \qquad F_x = -\frac{dU}{dx}. \]
\begin{compare}{Force}{Potential energy}{Zero chosen at}
Uniform gravity $-mg\,\hat\jmath$ & $U = mgy$ & any convenient height \\
Spring $-kx$ & $U = \tfrac12 kx^2$ & natural length \\
Universal gravity $-\dfrac{GMm}{r^2}\hat r$ & $U = -\dfrac{GMm}{r}$ & $r \to \infty$ (so $U < 0$ for bound objects) \\
\end{compare}

\textbf{Reading a $U(x)$ graph.} The force is minus the slope, so it points ``downhill''. Equilibrium is where the slope is zero: a minimum is \emph{stable} (a nudge produces a restoring force), a maximum \emph{unstable}. With total energy $E$, the object can only be where $U(x) \le E$; turning points are where $U = E$, and $K = E - U$ everywhere else.

\begin{trap}
Near Earth's surface $\Delta U = mg\Delta h$ is an approximation. Far away use $-GMm/r$: lifting a mass from $R_E$ to $2R_E$ takes $\tfrac12 mgR_E$, not $mgR_E$.
\end{trap}
""", checks=[
    Q("3.3 Force from potential energy", r"A particle's potential energy is $U(x) = 4x^2 - x^3$ (joules, meters). What is the force on it at $x = 1.0$ m?",
      r"$-5.0$ N", [r"$+5.0$ N", r"$+3.0$ N", r"$-3.0$ N"],
      r"$F = -dU/dx = -(8x - 3x^2)$; at $x = 1$, $F = -5.0$ N (toward $-x$).",
      [r"$dU/dx = 8x - 3x^2 = 5$ at $x = 1$.", r"$F = -dU/dx = -5.0$ N."],
      [r"forgets the minus sign in $F = -dU/dx$.", r"is $U(1) = 3$ J, a potential energy, not a force.", r"is $-U(1)$; the force comes from the slope of $U$, not its value."], sort=True),
    Q("3.3 Stable equilibrium", r"On a graph of $U(x)$, where is a particle in stable equilibrium?",
      r"At a local minimum of $U$", [r"At a local maximum of $U$", r"Where $U = 0$", r"Where $U$ is steepest"],
      r"Equilibrium needs $F = -dU/dx = 0$; stability needs the force to push back toward that point, which happens at a minimum ($d^2U/dx^2 > 0$).",
      [r"Slope zero: no force.", r"At a minimum, moving either way puts the particle uphill, so the force points back."],
      [r"is equilibrium, but unstable: a nudge sends the particle downhill away from it.", r"the value of $U$ is set by an arbitrary zero; only its slope gives the force.", r"is where the force is largest, the opposite of equilibrium."]),
])

S3 = Sec("Conservation of energy (3.4)", ["3.4"], r"""
For a system, the energy changes only by work done by external forces and by non-conservative internal forces:
\[ \Delta K + \Delta U = W_{ext} + W_{nc}, \qquad \text{isolated, conservative: } K_1 + U_1 = K_2 + U_2. \]
Kinetic friction converts mechanical energy to thermal energy: $\Delta E_{th} = f_k d$ (with $d$ the sliding distance), so $K_1 + U_1 = K_2 + U_2 + f_k d$.

\begin{keyidea}[Energy or forces?]
Use energy when the question links speeds and positions and does not ask about time or direction. Use forces (Newton's second law) when it asks about acceleration, tension, normal force, or time. Many FRQs need both: energy for the speed at the bottom of a loop, then $\sum F = mv^2/r$ for the normal force there.
\end{keyidea}

\begin{example}[Escape speed]
To just escape from a planet's surface, $K + U = 0$: $\tfrac12 mv_e^2 - \dfrac{GMm}{R} = 0$, so $v_e = \sqrt{2GM/R}$, which is $\sqrt2$ times the speed of a circular orbit at the surface.
\end{example}
""", checks=[
    Q("3.4 Conservation of energy", r"A pendulum bob is released from rest $0.45$ m above its lowest point. Ignoring air resistance, how fast is it moving at the bottom? ($g = 10\ \mathrm{m/s^2}$)",
      r"$3.0$ m/s", [r"$9.0$ m/s", r"$4.5$ m/s", r"$2.1$ m/s"],
      r"$mgh = \tfrac12 mv^2$, so $v = \sqrt{2gh} = \sqrt{9.0} = 3.0$ m/s. Tension does no work (it is perpendicular to the motion).",
      [r"$v = \sqrt{2(10)(0.45)} = 3.0$ m/s."],
      [r"is $v^2$, forgetting the square root.", r"is $gh$, with no square root and no factor of 2.", r"is $\sqrt{gh}$, dropping the factor of 2."], sort=True),
])

S4 = Sec("Power (3.5)", ["3.5"], r"""
Power is the rate of energy transfer:
\[ P = \frac{dW}{dt} = \frac{dE}{dt}, \qquad P = \vec F\cdot\vec v, \qquad \bar P = \frac{\Delta E}{\Delta t}. \]
A motor that moves a load at constant speed against a resisting force $F$ delivers $P = Fv$. If a constant force accelerates an object from rest, $v$ grows with time, so the power grows too, and the instantaneous power at the end is twice the average.
""", checks=[
    Q("3.5 Power at constant speed", r"A car drives at a steady $20$ m/s on a level road. Air resistance and rolling friction together exert $500$ N. What power must the engine deliver to the wheels?",
      r"$10$ kW", [r"$25$ W", r"$5.0$ kW", r"$20$ kW"],
      r"At constant speed the driving force equals the resistance, 500 N, so $P = Fv = 500 \times 20 = 10{,}000$ W.",
      [r"$F_{drive} = 500$ N (net force zero).", r"$P = (500)(20) = 1.0\times10^4$ W."],
      [r"divides force by speed.", r"halves the correct value, as if averaging from rest.", r"doubles it; no acceleration means no extra power."], sort=True),
])

QS1 = [
    Q("3.2 Dot product", r"A constant force $\vec F = (2.0\,\hat\imath + 3.0\,\hat\jmath)$ N acts on an object that moves through $\Delta\vec r = (4.0\,\hat\imath - 1.0\,\hat\jmath)$ m. How much work does the force do?",
      r"$5.0$ J", [r"$11$ J", r"$8.0$ J", r"$15$ J"],
      r"$W = \vec F\cdot\Delta\vec r = (2.0)(4.0) + (3.0)(-1.0) = 5.0$ J.",
      [r"Multiply matching components and add.", r"$8.0 - 3.0 = 5.0$ J."],
      [r"ignores the minus sign on the $y$-displacement.", r"keeps only the $x$-components.", r"is $|\vec F||\Delta\vec r|$, which assumes the force and displacement are parallel."], sort=True),
    Q("3.2 Work from F(x)", r"A force $F(x) = 5x^2$ (N, with $x$ in m) acts along the $x$-axis as an object moves from $x = 1.0$ m to $x = 3.0$ m. How much work does it do?",
      r"$43$ J", [r"$40$ J", r"$90$ J", r"$50$ J"],
      r"$W = \int_1^3 5x^2\,dx = \tfrac53(27 - 1) = 43$ J.",
      [r"Antiderivative: $\tfrac53 x^3$.", r"$\tfrac53(27) - \tfrac53(1) = 45 - 1.67 = 43.3$ J."],
      [r"is $F(3) - F(1)$, the change in force.", r"multiplies the final force (45 N) by the 2.0 m displacement.", r"multiplies the average of the end forces (25 N) by 2.0 m; that works only if $F$ is linear in $x$."], sort=True),
    Q("3.1 Work--energy theorem", r"A 2.0 kg block moving at 3.0 m/s is pushed by a net force of 10 N in its direction of motion for 4.0 m. What is its final speed?",
      r"$7.0$ m/s", [r"$6.3$ m/s", r"$9.3$ m/s", r"$5.0$ m/s"],
      r"$\Delta K = W_{net} = 40$ J. $K_f = 9.0 + 40 = 49$ J $= \tfrac12(2.0)v^2$, so $v = 7.0$ m/s.",
      [r"$K_i = \tfrac12(2.0)(3.0)^2 = 9.0$ J.", r"$K_f = 49$ J, so $v_f = \sqrt{49} = 7.0$ m/s."],
      [r"is $\sqrt{40}$: it gives the block 40 J but forgets its initial 9.0 J.", r"adds the initial speed to $\sqrt{40}$; kinetic energies add, speeds do not.", r"is the acceleration, $10/2.0 = 5.0\ \mathrm{m/s^2}$."], sort=True),
    Q("3.3 Force from potential energy", r"A particle's potential energy is $U(x) = 3x^2 - 2x^3$ (J, with $x$ in m). What is the force on the particle at $x = 2.0$ m?",
      r"$+12$ N", [r"$-12$ N", r"$-4.0$ N", r"$0$ N"],
      r"$F = -dU/dx = -(6x - 6x^2)$. At $x = 2$: $-(12 - 24) = +12$ N.",
      [r"$dU/dx = 6x - 6x^2 = -12$ J/m at $x = 2$.", r"$F = -dU/dx = +12$ N."],
      [r"is $dU/dx$ itself; the force is its negative.", r"is $U(2) = 12 - 16 = -4$ J, the potential energy, not the force.", r"would require a flat point of $U$; the zeros of $dU/dx$ are at $x = 0$ and $1$."], sort=True),
    Q("3.3 Equilibrium", r"For the same potential energy, $U(x) = 3x^2 - 2x^3$, at which position is the particle in stable equilibrium?",
      r"$x = 0$", [r"$x = 1.0$ m", r"$x = 1.5$ m", r"$x = 0.50$ m"],
      r"Equilibria are where $dU/dx = 6x(1 - x) = 0$: $x = 0$ and $x = 1$. Since $d^2U/dx^2 = 6 - 12x$ is $+6$ at $x = 0$ (a minimum), $x = 0$ is stable.",
      [r"$dU/dx = 0$ at $x = 0$ and $x = 1$ m.", r"$U''(0) = 6 > 0$: minimum, stable. $U''(1) = -6 < 0$: maximum, unstable."],
      [r"is an equilibrium, but a maximum of $U$, so it is unstable.", r"is where $U = 0$; zero energy is not zero force.", r"is where the force is largest in magnitude between the equilibria, not where it vanishes."]),
    Q("3.3 Gravitational potential energy", r"How much work is needed to lift a satellite of mass $m$ from Earth's surface (radius $R$) to a height $R$ above the surface? Express the answer in terms of $g$ at the surface.",
      r"$\tfrac12 mgR$", [r"$mgR$", r"$2mgR$", r"$\tfrac14 mgR$"],
      r"$\Delta U = -\dfrac{GMm}{2R} - \left(-\dfrac{GMm}{R}\right) = \dfrac{GMm}{2R}$, and $GM = gR^2$, so $\Delta U = \tfrac12 mgR$.",
      [r"Use $U = -GMm/r$ at $r = R$ and $r = 2R$.", r"$\Delta U = GMm/(2R) = \tfrac12 mgR$ since $GM/R^2 = g$."],
      [r"uses $mgh$, which assumes $g$ stays $9.8\ \mathrm{m/s^2}$ all the way up; $g$ weakens with height.", r"overcounts; it uses the distance from Earth's center as the height.", r"uses the field at the top, $g/4$, as if it acted the whole way."]),
    Q("3.4 Spring launch", r"A spring ($k = 200$ N/m) compressed $0.10$ m launches a $0.050$ kg ball straight up. Ignoring air resistance, how high above its launch position does the ball rise? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$2.0$ m", [r"$4.1$ m", r"$1.0$ m", r"$41$ m"],
      r"$\tfrac12 kx^2 = mgh$: $\tfrac12(200)(0.10)^2 = 1.0$ J, so $h = 1.0/(0.050 \times 9.8) = 2.0$ m.",
      [r"Spring energy $= 1.0$ J.", r"$h = 1.0\ \mathrm{J}/0.49\ \mathrm{N} = 2.04$ m."],
      [r"forgets the $\tfrac12$ in the spring energy.", r"reads the 1.0 J of energy as a height.", r"uses the spring force $kx = 20$ N in place of the energy: $20/0.49$."], sort=True),
    Q("3.4 Friction and energy", r"A block slides from rest down a frictionless ramp from a height of 5.0 m, then across a level floor with $\mu_k = 0.25$. How far along the floor does it slide before stopping?",
      r"$20$ m", [r"$5.0$ m", r"$1.3$ m", r"$10$ m"],
      r"All the gravitational energy becomes thermal energy on the floor: $mgh = \mu_k mg d$, so $d = h/\mu_k = 20$ m.",
      [r"Top: $U = mgh$. Bottom of ramp: $K = mgh$.", r"Floor: $\mu_k mg\,d = mgh \Rightarrow d = 5.0/0.25 = 20$ m."],
      [r"sets the distance equal to the height.", r"multiplies $h$ by $\mu_k$ instead of dividing.", r"puts in a factor of $\tfrac12$ from $\tfrac12 mv^2$ that cancels out."], sort=True),
    Q("3.4 Energy and forces together", r"A pendulum of length $L$ is released from rest with the string horizontal. What is the tension in the string when the bob passes through the lowest point?",
      r"$3mg$", [r"$mg$", r"$2mg$", r"$5mg$"],
      r"Energy gives $v^2 = 2gL$ at the bottom. Then $T - mg = mv^2/L = 2mg$, so $T = 3mg$.",
      [r"$mgL = \tfrac12 mv^2 \Rightarrow mv^2/L = 2mg$.", r"$T = mg + 2mg = 3mg$."],
      [r"ignores the centripetal acceleration at the bottom.", r"is the centripetal term alone, $mv^2/L$; tension must also hold up the bob.", r"is the result for a release from the very top of the circle (height $2L$)."]),
    Q("3.4 Escape speed", r"What is the escape speed from the surface of a planet of mass $M$ and radius $R$?",
      r"$\sqrt{2GM/R}$", [r"$\sqrt{GM/R}$", r"$2GM/R$", r"$\sqrt{GM/(2R)}$"],
      r"Escaping means reaching $r \to \infty$ with $K \ge 0$: $\tfrac12 mv^2 - GMm/R = 0$.",
      [r"Total energy zero: $\tfrac12 mv_e^2 = GMm/R$.", r"$v_e = \sqrt{2GM/R}$."],
      [r"is the speed of a circular orbit at the surface, smaller by $\sqrt2$.", r"is $v^2$, not a speed.", r"puts the 2 in the denominator."]),
    Q("3.5 Power", r"An elevator motor lifts an 800 kg car at a constant $2.0$ m/s. What power does the motor deliver? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$16$ kW", [r"$1.6$ kW", r"$7.8$ kW", r"$31$ kW"],
      r"At constant speed the cable pulls with $mg = 7840$ N, so $P = Fv = 7840 \times 2.0 = 15.7$ kW.",
      [r"$F = mg = 7.84\times10^3$ N.", r"$P = Fv = 1.57\times10^4$ W."],
      [r"uses $mv = 1600$, leaving out $g$.", r"is $mg$ in newtons read as watts; it forgets to multiply by $v$.", r"doubles the correct value."], sort=True),
    Q("3.5 Instantaneous power", r"A constant net force of 10 N acts on a 2.0 kg object that starts from rest. What power does the force deliver at $t = 3.0$ s?",
      r"$150$ W", [r"$75$ W", r"$30$ W", r"$225$ W"],
      r"$v = (F/m)t = 15$ m/s at $t = 3.0$ s, so $P = Fv = 150$ W.",
      [r"$a = 5.0\ \mathrm{m/s^2}$, $v(3) = 15$ m/s.", r"$P = (10)(15) = 150$ W."],
      [r"is the average power over the 3.0 s ($225\ \mathrm{J}/3.0$ s); the power grows as the object speeds up.", r"is $Ft$, the impulse, not a power.", r"is the kinetic energy at $t = 3.0$ s, in joules."], sort=True),
]

UNIT = Unit(
    n=3, slug="work-energy-power", title="Work, Energy, and Power", weight="15--25\\%", topics="3.1--3.5",
    abstract=r"""Unit 3 replaces force-by-force analysis with energy bookkeeping. It covers kinetic energy and work, including work by variable forces as an integral and the work--energy theorem (3.1--3.2); potential energy, $F = -dU/dx$, gravitational and spring potential energy, and potential-energy diagrams with equilibrium and turning points (3.3); conservation of energy with friction (3.4); and power (3.5). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4],
    qsections=[("Work and kinetic energy (3.1--3.2)", QS1[:3]), ("Potential energy (3.3)", QS1[3:6]), ("Conservation of energy (3.4)", QS1[6:10]), ("Power (3.5)", QS1[10:])],
    frq=FRQ("Qualitative/Quantitative Translation", 8, r"""A block of mass $m$ is released from rest at height $h$ on a frictionless curved track. At the bottom the track becomes level, and the block slides into a horizontal spring of spring constant $k$ attached to a wall. The level section is also frictionless.""", [
        Part("a", 3, r"The block is now released from height $2h$ instead. Without writing or deriving equations, explain how the spring's maximum compression changes. Say whether it doubles, more than doubles, or less than doubles, and why.",
             r"1 pt: doubling the height doubles the gravitational energy converted, so the spring must store twice the energy at maximum compression. 1 pt: the spring's stored energy grows faster than its compression (it depends on the compression squared, since each extra bit of compression takes a larger force). 1 pt: so the compression increases but by less than a factor of 2.",
             r"Saying the compression doubles because the energy doubles."),
        Part("b", 3, r"Derive an expression for the maximum compression $x_{max}$ in terms of $m$, $h$, $k$, and physical constants.",
             r"1 pt: energy conservation from release to maximum compression, with zero kinetic energy at both ends. 1 pt: $mgh = \tfrac12 kx_{max}^2$. 1 pt: $x_{max} = \sqrt{2mgh/k}$.",
             r"Using force balance, $kx = mg$, which describes a hanging spring, not this situation."),
        Part("c", 2, r"Explain how your expression in part (b) is consistent with your reasoning in part (a).",
             r"1 pt: $x_{max} \propto \sqrt h$, so doubling $h$ multiplies $x_{max}$ by $\sqrt2 \approx 1.41$. 1 pt: this is an increase of less than double, as argued in (a), because the stored energy $\tfrac12 kx^2$ depends on $x$ squared.",
             r"Restating the expression without connecting $\sqrt h$ to the claim in (a)."),
    ]),
    frq_topic="a block, a curved track, and a spring",
)
