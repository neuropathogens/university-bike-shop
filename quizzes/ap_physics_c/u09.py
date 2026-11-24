from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Electric potential energy (9.1)", ["9.1"], r"""
The electric force is conservative, so it has a potential energy:
\[ U = k\frac{q_1q_2}{r}\ \ \text{(pair, zero at } r\to\infty), \qquad U_{system} = \sum_{\text{pairs}} k\frac{q_iq_j}{r_{ij}}, \qquad W_{field} = -\Delta U. \]
$U$ is a scalar with a sign: positive for like charges (work was needed to push them together), negative for unlike charges (a bound pair). To assemble a set of charges from far apart, count each \emph{pair} once: three charges have three pairs, four have six.

In a uniform field the potential energy changes linearly: moving a charge $q$ a distance $d$ along $\vec E$ gives $\Delta U = -qEd$.
""", checks=[
    Q("9.1 Assembling charges", r"How much work must an external agent do to bring two charges, $+q$ and $+q$, from very far apart to a separation $r$ (starting and ending at rest)?",
      r"$kq^2/r$", [r"$-kq^2/r$", r"$kq^2/r^2$", r"$2kq^2/r$"],
      r"$W_{ext} = \Delta U = kq^2/r - 0$. Positive work is needed to push like charges together.",
      [r"$U(\infty) = 0$, $U(r) = kq^2/r$.", r"$W_{ext} = U(r) - U(\infty)$."],
      [r"is the work done by the electric field, which opposes the push.", r"is a force, not an energy.", r"counts the single pair twice."]),
])

S2 = Sec("Electric potential (9.2)", ["9.2"], r"""
Potential is potential energy per unit charge, a scalar property of a point in space:
\[ V = \frac{U}{q}, \qquad V_{point} = \frac{kq}{r}, \qquad \Delta V = V_b - V_a = -\int_a^b\vec E\cdot d\vec l, \qquad E_x = -\frac{dV}{dx}. \]
\begin{itemize}
\item Potentials from several charges add as plain numbers (with signs), not vectors. Where $V = 0$ the field need not be zero, and vice versa.
\item The field points ``downhill'' in potential, toward lower $V$. Its strength is how fast $V$ changes with distance: closely spaced equipotentials mean a strong field.
\item Equipotential surfaces are perpendicular to field lines. Moving a charge along one takes no work.
\item Uniform field: $|\Delta V| = Ed$ along the field. Ring on its axis: $V = \dfrac{kQ}{\sqrt{x^2 + R^2}}$. Continuous distributions: $V = \int\dfrac{k\,dq}{r}$, usually easier than integrating $\vec E$.
\end{itemize}
""", checks=[
    Q("9.2 Potential vs. field", r"Charges $+q$, $+q$, $-q$, $-q$ sit at the corners of a square, with the two positive charges on adjacent corners. At the center of the square, which is true?",
      r"$V = 0$, but $E \ne 0$", [r"$V = 0$ and $E = 0$", r"$V \ne 0$ and $E = 0$", r"$V \ne 0$ and $E \ne 0$"],
      r"All four corners are the same distance from the center, so the potentials ($\pm kq/r$) sum to zero. The fields do not cancel: both positive charges push toward the negative side, and both negative charges pull that way too.",
      [r"$V = \dfrac{k}{r}(q + q - q - q) = 0$.", r"The field points from the positive side toward the negative side."],
      [r"assumes zero potential means zero field.", r"the potentials cancel exactly; the fields are what survive.", r"the potentials cancel."]),
    Q("9.2 Field from potential", r"In a region, $V(x) = 3x^2 - 2x$ (volts, $x$ in meters). What is the $x$-component of the electric field at $x = 2.0$ m?",
      r"$-10$ V/m", [r"$+10$ V/m", r"$-8.0$ V/m", r"$+8.0$ V/m"],
      r"$E_x = -dV/dx = -(6x - 2) = -10$ V/m at $x = 2$.",
      [r"$dV/dx = 6x - 2 = 10$ V/m.", r"$E_x = -10$ V/m."],
      [r"forgets the minus sign.", r"is $-V(2)$, the potential with a minus sign, not its slope.", r"is $V(2) = 12 - 4 = 8.0$ V, a potential, not a field."], sort=True),
])

S3 = Sec("Conservation of electric energy (9.3)", ["9.3"], r"""
With only electric forces doing work,
\[ \tfrac12 mv_a^2 + qV_a = \tfrac12 mv_b^2 + qV_b, \qquad \Delta K = -q\Delta V. \]
Positive charges speed up moving toward lower potential; negative charges (electrons) speed up moving toward \emph{higher} potential. A particle of charge $e$ crossing a potential difference of 1 V gains $1\ \mathrm{eV} = 1.6\times10^{-19}$ J.

\begin{example}[Closest approach]
An alpha particle fired head-on at a fixed nucleus slows as it climbs the potential hill. It stops where all its kinetic energy has become potential energy: $\tfrac12 mv_0^2 = kq_1q_2/r_{min}$.
\end{example}
""", checks=[
    Q("9.3 Energy gain", r"A proton starts from rest and is accelerated through a potential difference of 100 V. How much kinetic energy does it gain?",
      r"$1.6\times10^{-17}$ J", [r"$1.6\times10^{-19}$ J", r"$100$ J", r"$6.3\times10^{20}$ J"],
      r"$\Delta K = q|\Delta V| = (1.6\times10^{-19})(100) = 1.6\times10^{-17}$ J, i.e.\ 100 eV.",
      [r"$\Delta K = e\Delta V$."],
      [r"is one electron volt, for a 1 V difference.", r"reads volts as joules; a volt is a joule per coulomb.", r"divides 100 by $e$ instead of multiplying."], sort=True),
])

QS1 = [
    Q("9.1 Energy of a system", r"Three charges $+q$ are placed at the corners of an equilateral triangle of side $a$. What is the electric potential energy of the system?",
      r"$3kq^2/a$", [r"$kq^2/a$", r"$6kq^2/a$", r"$3kq^2/a^2$"],
      r"There are three pairs, each separated by $a$: $U = 3 \times kq^2/a$.",
      [r"Pairs: AB, BC, CA.", r"$U = 3kq^2/a$."],
      [r"counts only one pair.", r"counts each pair twice (once from each charge).", r"uses $1/a^2$, the form of a force or field, not an energy."]),
    Q("9.1 Uniform field", r"A proton moves 0.050 m in the direction of a uniform electric field of 200 N/C. What is the change in the electric potential energy of the proton--field system?",
      r"$-1.6\times10^{-18}$ J", [r"$+1.6\times10^{-18}$ J", r"$-3.2\times10^{-17}$ J", r"$0$"],
      r"$\Delta U = -qEd = -(1.6\times10^{-19})(200)(0.050) = -1.6\times10^{-18}$ J: the field does positive work, so $U$ falls.",
      [r"$\Delta V = -Ed = -10$ V.", r"$\Delta U = q\Delta V = -1.6\times10^{-18}$ J."],
      [r"has the sign reversed; a positive charge moving along the field loses potential energy.", r"uses a distance of 1.0 m instead of 0.050 m.", r"would be true only for motion perpendicular to the field."], sort=True),
    Q("9.2 Potential of a point charge", r"What is the electric potential 0.30 m from a $+2.0$ nC point charge? ($k = 9.0\times10^9\ \mathrm{N\,m^2/C^2}$)",
      r"$60$ V", [r"$200$ V", r"$18$ V", r"$5.4$ V"],
      r"$V = kq/r = (9.0\times10^9)(2.0\times10^{-9})/0.30 = 60$ V.",
      [r"$kq = 18\ \mathrm{V\cdot m}$.", r"$V = 18/0.30 = 60$ V."],
      [r"divides by $r^2$, giving the field in N/C.", r"forgets to divide by $r$.", r"multiplies $kq$ by $r$ instead of dividing."], sort=True),
    Q("9.2 Dipole midpoint", r"Charges $+q$ and $-q$ are a distance $d$ apart. At the midpoint between them, which is true?",
      r"$V = 0$ and $E \ne 0$", [r"$V = 0$ and $E = 0$", r"$V \ne 0$ and $E = 0$", r"$V \ne 0$ and $E \ne 0$"],
      r"The potentials $+kq/(d/2)$ and $-kq/(d/2)$ cancel. The fields both point toward $-q$ and add to $8kq/d^2$.",
      [r"Scalar sum: $V = 0$.", r"Vector sum: $E = 8kq/d^2$ toward $-q$."],
      [r"the fields add, they do not cancel.", r"has both backwards: $V$ cancels, $E$ does not.", r"the two potentials are equal and opposite."]),
    Q("9.2 Potential difference from a field", r"The electric field along the $x$-axis is $\vec E = 4x^2\,\hat\imath$ (N/C, $x$ in m). What is $V(3.0\ \mathrm{m}) - V(0)$?",
      r"$-36$ V", [r"$+36$ V", r"$-108$ V", r"$-18$ V"],
      r"$\Delta V = -\int_0^3 4x^2\,dx = -\tfrac43(27) = -36$ V. The field points in $+x$, so the potential falls along $+x$.",
      [r"$\int_0^3 4x^2\,dx = 36$.", r"$\Delta V = -36$ V."],
      [r"drops the minus sign in $\Delta V = -\int E\,dx$.", r"uses $E(3) \times 3.0$ m, treating the final field as constant.", r"integrates $4x$ instead of $4x^2$ ($2x^2$ from 0 to 3)."], sort=True),
    Q("9.2 Field from potential", r"The potential along the $x$-axis is $V(x) = 5x^3 - 2x$ (V, $x$ in m). What is $E_x$ at $x = 1.0$ m?",
      r"$-13$ V/m", [r"$+13$ V/m", r"$+3.0$ V/m", r"$-15$ V/m"],
      r"$E_x = -dV/dx = -(15x^2 - 2) = -13$ V/m at $x = 1$.",
      [r"$dV/dx = 15x^2 - 2 = 13$.", r"$E_x = -13$ V/m."],
      [r"forgets the minus sign.", r"is $V(1) = 5 - 2 = 3$ V, the potential itself.", r"drops the $-2x$ term when differentiating."], sort=True),
    Q("9.2 Potential of a ring", r"A ring of radius $R$ carries total charge $Q$ spread unevenly around it. What is the electric potential at its center?",
      r"$kQ/R$", [r"$0$, because the charge is spread around a circle", r"$kQ/R^2$", r"It cannot be found without knowing how the charge is distributed."],
      r"Every bit of charge is the same distance $R$ from the center, and potential is a scalar: $V = \int k\,dq/R = kQ/R$, however the charge is spread.",
      [r"$V = \dfrac{k}{R}\int dq = \dfrac{kQ}{R}$."],
      [r"confuses potential with field; the field at the center of a uniform ring is zero, but the potential is not.", r"has the units of a field.", r"the distribution affects the field at the center, but not the potential, because every element is at distance $R$."]),
    Q("9.2 Equipotentials", r"Equipotential lines 10 V apart are parallel and 2.0 cm apart, with the potential increasing toward the east. What is the electric field?",
      r"$500$ V/m, pointing west", [r"$500$ V/m, pointing east", r"$5.0$ V/m, pointing west", r"$20$ V/m, pointing east"],
      r"$E = |\Delta V|/d = 10/0.020 = 500$ V/m, pointing toward lower potential, west.",
      [r"Field strength: $\Delta V/\Delta x$ in V/m.", r"Direction: downhill in potential."],
      [r"has the direction reversed; the field points toward lower potential.", r"uses 2.0 m instead of 0.020 m.", r"multiplies $\Delta V$ by $d$ in cm and gets the direction wrong."]),
    Q("9.2 Zero potential", r"At a certain point the electric potential is zero. What must be true of the electric field there?",
      r"Nothing; the field can be zero or nonzero.", [r"The field must be zero.", r"The field must be nonzero.", r"The field must point toward the nearest negative charge."],
      r"The field depends on how $V$ changes ($E = -dV/dx$), not on its value. The midpoint of a dipole has $V = 0$ and $E \ne 0$; a point far from all charges has both zero.",
      [r"Value of $V$ $\ne$ slope of $V$."],
      [r"the dipole midpoint is a counterexample.", r"far from all charges, both are zero.", r"no such rule follows from $V = 0$."]),
    Q("9.3 Accelerating an electron", r"An electron starts from rest and is accelerated through a potential difference of 500 V. What is its final speed? ($e = 1.6\times10^{-19}$ C, $m_e = 9.1\times10^{-31}$ kg)",
      r"$1.3\times10^{7}$ m/s", [r"$8.8\times10^{13}$ m/s", r"$9.4\times10^{6}$ m/s", r"$3.1\times10^{5}$ m/s"],
      r"$\tfrac12 mv^2 = e\Delta V$, so $v = \sqrt{2e\Delta V/m} = \sqrt{1.76\times10^{14}} = 1.3\times10^7$ m/s.",
      [r"$K = (1.6\times10^{-19})(500) = 8.0\times10^{-17}$ J.", r"$v = \sqrt{2K/m} = 1.33\times10^7$ m/s."],
      [r"is $e\Delta V/m$, which equals $v^2/2$, not a speed.", r"drops the 2 in $v = \sqrt{2K/m}$.", r"uses the proton's mass."], sort=True),
    Q("9.3 Closest approach", r"A particle of mass $m$ and charge $+q$ is fired with speed $v_0$ straight at a fixed charge $+Q$ from far away. How close does it get?",
      r"$\dfrac{2kqQ}{mv_0^2}$", [r"$\dfrac{kqQ}{mv_0^2}$", r"$\sqrt{\dfrac{2kqQ}{mv_0^2}}$", r"$\dfrac{mv_0^2}{2kqQ}$"],
      r"All kinetic energy becomes potential energy at the turning point: $\tfrac12 mv_0^2 = kqQ/r_{min}$.",
      [r"$r_{min} = \dfrac{kqQ}{\tfrac12 mv_0^2} = \dfrac{2kqQ}{mv_0^2}$."],
      [r"drops the $\tfrac12$ in the kinetic energy.", r"treats the potential energy as $\propto 1/r^2$ (that is the force).", r"is upside down, with units of 1/m."]),
    Q("9.3 Electron moving between potentials", r"An electron moves, with only electric forces acting, from a point at $V = 100$ V to a point at $V = 300$ V. Its kinetic energy",
      r"increases by 200 eV", [r"decreases by 200 eV", r"increases by 300 eV", r"decreases by 400 eV"],
      r"$\Delta U = q\Delta V = (-e)(+200\ \mathrm{V}) = -200$ eV, so $\Delta K = +200$ eV. Electrons gain speed moving toward higher potential.",
      [r"$\Delta V = +200$ V.", r"$\Delta K = -q\Delta V = +200$ eV for $q = -e$."],
      [r"would be true for a proton.", r"uses the final potential instead of the difference.", r"adds the potentials and reverses the sign."]),
]

UNIT = Unit(
    n=9, slug="electric-potential", title="Electric Potential", weight="10--20\\%", topics="9.1--9.3",
    abstract=r"""Unit 9 recasts electrostatics in terms of energy. It covers electric potential energy of pairs and systems of charges (9.1); electric potential, its superposition as a scalar, the integral link $\Delta V = -\int\vec E\cdot d\vec l$, the derivative link $E_x = -dV/dx$, and equipotentials (9.2); and conservation of energy for charged particles (9.3). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3],
    qsections=[("Potential energy (9.1)", QS1[:2]), ("Electric potential (9.2)", QS1[2:9]), ("Conservation of energy (9.3)", QS1[9:])],
    frq=FRQ("Qualitative/Quantitative Translation", 8, r"""Two identical positive charges $+Q$ are fixed at $x = -a$ and $x = +a$. A small particle of mass $m$ and charge $+q$ can move freely along the $x$-axis between them. Ignore gravity.""", [
        Part("a", 2, r"The particle is released from rest at $x = a/2$. Without equations, describe its subsequent motion and explain where its speed is greatest.",
             r"1 pt: the particle is pushed back toward the center, passes through $x = 0$, slows, stops at $x = -a/2$, and returns: it oscillates between $\pm a/2$. 1 pt: its speed is greatest at $x = 0$, where the net force is zero (forces from the two charges balance) and the potential, hence potential energy, is lowest along the segment.",
             r"Saying the particle stops at the center because the net force is zero there."),
        Part("b", 2, r"Write an expression for the electric potential $V(x)$ for $-a < x < a$.",
             r"1 pt: superposition of two point-charge potentials. 1 pt: $V(x) = \dfrac{kQ}{a + x} + \dfrac{kQ}{a - x}$ (equivalently $\dfrac{2kQa}{a^2 - x^2}$).",
             r"Subtracting the two terms; both charges are positive."),
        Part("c", 3, r"Derive an expression for the particle's speed as it passes $x = 0$, in terms of $k$, $Q$, $q$, $m$, and $a$.",
             r"1 pt: $V(a/2) = kQ\left(\dfrac{2}{3a} + \dfrac{2}{a}\right) = \dfrac{8kQ}{3a}$ and $V(0) = \dfrac{2kQ}{a}$. 1 pt: energy conservation, $q[V(a/2) - V(0)] = \tfrac12 mv^2$, with $V(a/2) - V(0) = \dfrac{2kQ}{3a}$. 1 pt: $v = \sqrt{\dfrac{4kQq}{3ma}}$.",
             r"Using the force at $x = a/2$ with constant-acceleration kinematics."),
        Part("d", 1, r"Explain how the expression for $V(x)$ in part (b) supports your claim in part (a) about where the speed is greatest.",
             r"1 pt: $V(x) = 2kQa/(a^2 - x^2)$ has its minimum at $x = 0$ (its slope, $-E_x$, is zero there and it rises toward both charges), so a positive charge has its lowest potential energy and greatest kinetic energy at $x = 0$.",
             r"Pointing to part (c) without referring to the shape of $V(x)$."),
    ]),
    frq_topic="a charge oscillating between two fixed charges",
)
