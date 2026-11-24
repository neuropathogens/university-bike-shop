from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Rotational kinematics and the link to linear motion (5.1--5.2)", ["5.1", "5.2"], r"""
A rigid body rotating about a fixed axis is described by one angle $\theta$ (in radians):
\[ \omega = \frac{d\theta}{dt}, \qquad \alpha = \frac{d\omega}{dt}, \qquad \text{constant } \alpha:\ \ \omega = \omega_0 + \alpha t,\ \ \theta = \theta_0 + \omega_0 t + \tfrac12\alpha t^2,\ \ \omega^2 = \omega_0^2 + 2\alpha\Delta\theta. \]
Every point at distance $r$ from the axis shares $\omega$ and $\alpha$, but its linear quantities scale with $r$:
\[ s = r\theta, \qquad v = r\omega, \qquad a_t = r\alpha, \qquad a_c = \frac{v^2}{r} = \omega^2 r, \qquad a = \sqrt{a_t^2 + a_c^2}. \]
\begin{trap}
These relations need radians. Convert: 1 rev $= 2\pi$ rad, and rpm $\times\,2\pi/60$ gives rad/s. A point on a wheel spinning at constant $\omega$ still accelerates (centripetally) even though $\alpha = 0$.
\end{trap}
""", checks=[
    Q("5.1 Constant angular acceleration", r"A wheel starts from rest with a constant angular acceleration of $2.0\ \mathrm{rad/s^2}$. Through what angle does it turn in the first 5.0 s?",
      r"$25$ rad", [r"$10$ rad", r"$50$ rad", r"$4.0$ rad"],
      r"$\theta = \tfrac12\alpha t^2 = \tfrac12(2.0)(25) = 25$ rad.",
      [r"From rest: $\theta = \tfrac12\alpha t^2$.", r"$\theta = 25$ rad (about 4.0 revolutions)."],
      [r"is the final angular speed, $\alpha t = 10$ rad/s.", r"forgets the $\tfrac12$.", r"is the number of revolutions, $25/2\pi \approx 4.0$, not radians."], sort=True),
])

S2 = Sec("Torque (5.3)", ["5.3"], r"""
Torque measures how effectively a force turns an object about an axis:
\[ \vec\tau = \vec r\times\vec F, \qquad \tau = rF\sin\theta = r_\perp F = rF_\perp, \]
where $\vec r$ runs from the axis to the point where the force acts and $\theta$ is the angle between $\vec r$ and $\vec F$. The \textbf{lever arm} $r_\perp$ is the perpendicular distance from the axis to the force's line of action. A force through the axis gives no torque. Use the right-hand rule for direction: $\hat\imath\times\hat\jmath = \hat k$; counterclockwise in the $xy$-plane is $+\hat k$. The weight of an extended object acts at its center of mass.
""", checks=[
    Q("5.3 Torque", r"A mechanic pulls with 20 N on a wrench 0.30 m from the bolt. The force makes a $30^\circ$ angle with the wrench handle. What torque does she exert?",
      r"$3.0$ N$\cdot$m", [r"$6.0$ N$\cdot$m", r"$5.2$ N$\cdot$m", r"$67$ N$\cdot$m"],
      r"$\tau = rF\sin\theta = (0.30)(20)\sin 30^\circ = 3.0$ N$\cdot$m.",
      [r"Only the component of $F$ perpendicular to the handle turns the bolt: $F\sin 30^\circ = 10$ N.", r"$\tau = 0.30 \times 10 = 3.0$ N$\cdot$m."],
      [r"assumes the force is perpendicular to the handle.", r"uses $\cos 30^\circ$, the component along the handle, which pulls on the bolt without turning it.", r"divides $F$ by $r$."], sort=True),
])

S3 = Sec("Rotational inertia (5.4)", ["5.4"], r"""
Rotational inertia plays the role of mass for rotation; it depends on how mass is distributed relative to the axis:
\[ I = \sum m_i r_i^2, \qquad I = \int r^2\,dm, \qquad I = I_{cm} + Md^2 \ \ \text{(parallel-axis theorem)}. \]
\begin{compare}{Object (mass $M$)}{Axis}{$I$}
Thin rod, length $L$ & through center, perpendicular & $\tfrac{1}{12}ML^2$ \\
Thin rod, length $L$ & through one end, perpendicular & $\tfrac13 ML^2$ \\
Hoop or thin ring, radius $R$ & central axis & $MR^2$ \\
Solid disk or cylinder & central axis & $\tfrac12 MR^2$ \\
Solid sphere & through center & $\tfrac25 MR^2$ \\
Thin spherical shell & through center & $\tfrac23 MR^2$ \\
\end{compare}
\begin{example}[Integral]
For a uniform rod about one end, $dm = (M/L)\,dx$ and $I = \int_0^L x^2 \frac{M}{L}\,dx = \tfrac13 ML^2$. The parallel-axis theorem agrees: $\tfrac1{12}ML^2 + M(L/2)^2 = \tfrac13 ML^2$.
\end{example}
\begin{trap}
The parallel-axis theorem starts from the axis through the \emph{center of mass}, never from another off-center axis.
\end{trap}
""", checks=[
    Q("5.4 Parallel-axis theorem", r"A uniform rod has $I_{cm} = \tfrac1{12}ML^2$ about its center. What is its rotational inertia about a parallel axis through one end?",
      r"$\tfrac13 ML^2$", [r"$\tfrac14 ML^2$", r"$\tfrac{13}{12}ML^2$", r"$\tfrac16 ML^2$"],
      r"$I = I_{cm} + Md^2$ with $d = L/2$: $\tfrac1{12}ML^2 + \tfrac14 ML^2 = \tfrac13 ML^2$.",
      [r"$Md^2 = M(L/2)^2 = \tfrac14 ML^2$.", r"$\tfrac{1}{12} + \tfrac{3}{12} = \tfrac{4}{12} = \tfrac13$."],
      [r"is the $Md^2$ term alone.", r"uses $d = L$ instead of $L/2$.", r"doubles $I_{cm}$, which has no basis."]),
])

S4 = Sec("Rotational equilibrium and Newton's second law for rotation (5.5--5.6)", ["5.5", "5.6"], r"""
\begin{keyidea}[Static equilibrium (5.5)]
$\sum\vec F = 0$ and $\sum\tau = 0$ about \emph{any} axis. Choose the axis through an unknown force to remove it from the torque equation.
\end{keyidea}
\[ \sum\tau = I\alpha \quad \text{(fixed axis, 5.6)}. \]
A rotating object with net torque obeys this exactly as a block obeys $\sum F = ma$. In problems that combine both, write $\sum F = ma$ for each block, $\sum\tau = I\alpha$ for each pulley or wheel, and link them with $a = \alpha R$ for a string that does not slip.

\begin{example}[Massive pulley]
A block of mass $m$ hangs from a string wrapped around a solid disk pulley ($M$, $R$) on a fixed axle. Block: $mg - T = ma$. Pulley: $TR = \tfrac12 MR^2(a/R)$, so $T = \tfrac12 Ma$. Together, $a = \dfrac{mg}{m + M/2}$: the pulley acts like extra inertia $I/R^2$.
\end{example}

\begin{trap}
With a massive pulley the tension is different on the two sides; the difference in tensions is what makes the pulley spin up.
\end{trap}
""", checks=[
    Q("5.5 Balance", r"A 30 kg child sits 2.0 m from the pivot of a seesaw. Where must a 40 kg child sit, on the other side, to balance? (Ignore the board's mass, or assume it is centered on the pivot.)",
      r"$1.5$ m from the pivot", [r"$2.0$ m from the pivot", r"$2.7$ m from the pivot", r"$1.0$ m from the pivot"],
      r"Torques balance: $30g(2.0) = 40g\,d$, so $d = 1.5$ m. The heavier child sits closer.",
      [r"$\sum\tau = 0$ about the pivot.", r"$d = 60/40 = 1.5$ m."],
      [r"equal distances balance only equal weights.", r"inverts the ratio and puts the heavier child farther out.", r"has no basis in the torque balance."]),
    Q("5.6 Rotational second law", r"A constant torque of 4.0 N$\cdot$m acts on a wheel with rotational inertia $0.50\ \mathrm{kg\,m^2}$. What is its angular acceleration?",
      r"$8.0\ \mathrm{rad/s^2}$", [r"$2.0\ \mathrm{rad/s^2}$", r"$0.13\ \mathrm{rad/s^2}$", r"$4.5\ \mathrm{rad/s^2}$"],
      r"$\alpha = \tau/I = 4.0/0.50 = 8.0\ \mathrm{rad/s^2}$.",
      [r"$\sum\tau = I\alpha \Rightarrow \alpha = \tau/I$."],
      [r"multiplies $\tau$ by $I$.", r"divides $I$ by $\tau$.", r"adds the two numbers."], sort=True),
])

QS1 = [
    Q("5.1 Angular kinematics", r"A turntable's angular position is $\theta(t) = 2t^3 - 3t$ (radians, seconds). What is its angular acceleration at $t = 2.0$ s?",
      r"$24\ \mathrm{rad/s^2}$", [r"$21\ \mathrm{rad/s^2}$", r"$10\ \mathrm{rad/s^2}$", r"$12\ \mathrm{rad/s^2}$"],
      r"$\omega = 6t^2 - 3$, $\alpha = 12t$, so $\alpha(2) = 24\ \mathrm{rad/s^2}$.",
      [r"$\omega = d\theta/dt = 6t^2 - 3$.", r"$\alpha = d\omega/dt = 12t = 24\ \mathrm{rad/s^2}$ at $t = 2$."],
      [r"is $\omega(2) = 24 - 3 = 21$ rad/s.", r"is $\theta(2) = 16 - 6 = 10$ rad.", r"is $\alpha(1)$, or the coefficient 12 without the factor $t$."], sort=True),
    Q("5.1 Revolutions", r"A wheel spinning at 30 rad/s slows uniformly to rest in 10 s. How many revolutions does it make while stopping?",
      r"$24$", [r"$150$", r"$48$", r"$3.0$"],
      r"$\Delta\theta = \bar\omega t = \tfrac12(30)(10) = 150$ rad $= 150/2\pi \approx 24$ rev.",
      [r"Average angular speed $= 15$ rad/s.", r"$\Delta\theta = 150$ rad; divide by $2\pi$: 23.9 rev."],
      [r"is the angle in radians, not revolutions.", r"uses $\omega_0 t = 300$ rad without averaging, then converts.", r"is the angular deceleration in rad/s$^2$."], sort=True),
    Q("5.2 Total acceleration", r"A point on the rim of a wheel of radius 0.40 m has $\omega = 5.0$ rad/s and $\alpha = 2.0\ \mathrm{rad/s^2}$ at some instant. What is the magnitude of its acceleration?",
      r"$10\ \mathrm{m/s^2}$", [r"$0.80\ \mathrm{m/s^2}$", r"$11\ \mathrm{m/s^2}$", r"$2.0\ \mathrm{m/s^2}$"],
      r"$a_c = \omega^2 r = 10\ \mathrm{m/s^2}$ and $a_t = \alpha r = 0.80\ \mathrm{m/s^2}$ are perpendicular: $a = \sqrt{10^2 + 0.80^2} = 10.0\ \mathrm{m/s^2}$.",
      [r"$a_c = (5.0)^2(0.40) = 10\ \mathrm{m/s^2}$; $a_t = (2.0)(0.40) = 0.80\ \mathrm{m/s^2}$.", r"Combine at right angles: $10.03\ \mathrm{m/s^2}$."],
      [r"is the tangential part only.", r"adds the components as if parallel ($10.8$).", r"is the speed $v = \omega r$ in m/s, or $\alpha$ itself."], sort=True),
    Q("5.3 Torque as a cross product", r"A force $\vec F = 3.0\,\hat\jmath$ N acts at $\vec r = 2.0\,\hat\imath$ m from a pivot at the origin. What is the torque about the origin?",
      r"$+6.0\,\hat k$ N$\cdot$m", [r"$-6.0\,\hat k$ N$\cdot$m", r"$+6.0\,\hat\imath$ N$\cdot$m", r"$0$"],
      r"$\vec\tau = \vec r\times\vec F = (2.0)(3.0)(\hat\imath\times\hat\jmath) = 6.0\,\hat k$ N$\cdot$m (counterclockwise seen from $+z$).",
      [r"$\hat\imath\times\hat\jmath = +\hat k$.", r"Magnitude $rF\sin 90^\circ = 6.0$ N$\cdot$m."],
      [r"computes $\vec F\times\vec r$; the order matters.", r"torque is perpendicular to both $\vec r$ and $\vec F$, so it cannot point along $\hat\imath$.", r"would need $\vec F$ parallel to $\vec r$; here they are perpendicular."]),
    Q("5.3 Torque on a door", r"A 40 N force is applied to a door 0.80 m from the hinges, at $60^\circ$ to the plane of the door. What torque does it exert about the hinge line?",
      r"$28$ N$\cdot$m", [r"$32$ N$\cdot$m", r"$16$ N$\cdot$m", r"$50$ N$\cdot$m"],
      r"$\tau = rF\sin\theta = (0.80)(40)\sin 60^\circ = 27.7$ N$\cdot$m.",
      [r"The angle between $\vec r$ (along the door) and $\vec F$ is $60^\circ$.", r"$\tau = 32 \times 0.866 = 27.7$ N$\cdot$m."],
      [r"assumes a perpendicular push.", r"uses $\cos 60^\circ$, the component along the door.", r"divides $F$ by $r$."], sort=True),
    Q("5.4 Parallel-axis theorem", r"What is the rotational inertia of a uniform rod (mass $M$, length $L$) about a perpendicular axis a distance $L/4$ from one end?",
      r"$\tfrac{7}{48}ML^2$", [r"$\tfrac13 ML^2$", r"$\tfrac1{12}ML^2$", r"$\tfrac1{16}ML^2$"],
      r"The axis is $L/4$ from the center: $I = \tfrac1{12}ML^2 + M(L/4)^2 = \left(\tfrac{4}{48} + \tfrac{3}{48}\right)ML^2 = \tfrac{7}{48}ML^2$.",
      [r"Distance from center to axis: $L/2 - L/4 = L/4$.", r"$I = I_{cm} + Md^2 = \tfrac{7}{48}ML^2$."],
      [r"is the value about the end.", r"is the value about the center.", r"is the $Md^2$ term alone."]),
    Q("5.4 Rotational inertia by integration", r"A rod of length $L$ lies along the $x$-axis from $x = 0$ to $x = L$ and has linear density $\lambda = kx$. Its total mass is $M$. What is its rotational inertia about the $y$-axis (through $x = 0$)?",
      r"$\tfrac12 ML^2$", [r"$\tfrac13 ML^2$", r"$\tfrac14 ML^2$", r"$\tfrac23 ML^2$"],
      r"$I = \int_0^L x^2(kx)\,dx = \tfrac14 kL^4$ and $M = \int_0^L kx\,dx = \tfrac12 kL^2$, so $I = \tfrac12 ML^2$.",
      [r"$I = kL^4/4$.", r"Eliminate $k = 2M/L^2$: $I = \tfrac{2M}{L^2}\cdot\tfrac{L^4}{4} = \tfrac12 ML^2$."],
      [r"is the uniform-rod result; extra mass near the far end raises $I$.", r"is $kL^4/4$ with $k$ replaced by $M$, ignoring that $k = 2M/L^2$.", r"is $M\,x_{cm}L$ with $x_{cm} = 2L/3$; rotational inertia is $\int r^2\,dm$, not built from the center-of-mass position."]),
    Q("5.4 Comparing inertias", r"A hoop and a solid disk have the same mass and radius. The same torque is applied to each about its central axis, starting from rest. Which statement is true?",
      r"The disk has the greater angular acceleration.", [r"The hoop has the greater angular acceleration.", r"They have equal angular accelerations.", r"The hoop has the smaller rotational inertia."],
      r"$I_{hoop} = MR^2 > I_{disk} = \tfrac12 MR^2$; with equal torque, $\alpha = \tau/I$ is larger for the disk (twice the hoop's).",
      [r"The hoop's mass is all at $R$; the disk's is spread inward.", r"$\alpha_{disk}/\alpha_{hoop} = I_{hoop}/I_{disk} = 2$."],
      [r"reverses the inertias.", r"same mass and radius do not mean the same $I$; distribution matters.", r"the hoop's mass is farther from the axis, so its $I$ is larger."]),
    Q("5.5 Supported beam", r"A uniform 4.0 m beam of mass 20 kg rests on supports at its two ends. A 30 kg child stands 1.0 m from the left end. What force does the left support exert? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$320$ N", [r"$170$ N", r"$250$ N", r"$490$ N"],
      r"Torques about the right end: $N_L(4.0) = 20g(2.0) + 30g(3.0) = 130g$, so $N_L = 32.5g = 320$ N.",
      [r"About the right support: the beam's weight acts 2.0 m away, the child 3.0 m away.", r"$N_L = 130(9.8)/4.0 = 318$ N.", r"Check: $N_R = 50g - 32.5g = 17.5g = 172$ N."],
      [r"is the right support's force.", r"splits the total weight equally, ignoring where the child stands.", r"is the total weight, which the two supports share."], sort=True),
    Q("5.5 Meter stick", r"A uniform meter stick balances on a pivot at its 50 cm mark. A 100 g mass hangs at the 20 cm mark. Where must a 200 g mass hang to keep the stick balanced?",
      r"At the 65 cm mark", [r"At the 80 cm mark", r"At the 35 cm mark", r"At the 70 cm mark"],
      r"Balance torques about the pivot: $(100)(30\ \mathrm{cm}) = (200)\,d$, so $d = 15$ cm on the other side: the 65 cm mark.",
      [r"The 100 g mass is 30 cm left of the pivot.", r"$d = 3000/200 = 15$ cm to the right: 65 cm."],
      [r"mirrors the position, which balances only equal masses.", r"puts both masses on the same side, so the torques add.", r"uses 20 cm instead of 15 cm."]),
    Q("5.6 Massive pulley", r"A 2.0 kg block hangs from a light string wrapped around a uniform solid-disk pulley of mass 4.0 kg and radius 0.10 m that turns on a frictionless fixed axle. What is the block's acceleration? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$4.9\ \mathrm{m/s^2}$", [r"$9.8\ \mathrm{m/s^2}$", r"$3.3\ \mathrm{m/s^2}$", r"$6.5\ \mathrm{m/s^2}$"],
      r"Block: $mg - T = ma$. Pulley: $TR = \tfrac12 MR^2(a/R)$, so $T = \tfrac12 Ma$. Then $a = \dfrac{mg}{m + M/2} = \dfrac{19.6}{4.0} = 4.9\ \mathrm{m/s^2}$.",
      [r"$T = \tfrac12(4.0)a = 2.0a$.", r"$2.0(9.8) - 2.0a = 2.0a \Rightarrow a = 4.9\ \mathrm{m/s^2}$."],
      [r"is free fall; the pulley's inertia resists.", r"treats the pulley as a hoop, $I = MR^2$: $19.6/6.0$.", r"uses $I = \tfrac14 MR^2$: $19.6/3.0$."], sort=True),
    Q("5.6 Falling rod", r"A uniform rod is pivoted at one end and held horizontal, then released. Just after release, what is the linear acceleration of its free end?",
      r"$\tfrac32 g$", [r"$g$", r"$\tfrac12 g$", r"$\tfrac34 g$"],
      r"$\alpha = \tau/I = \dfrac{Mg(L/2)}{\tfrac13 ML^2} = \dfrac{3g}{2L}$, so the free end has $a = \alpha L = \tfrac32 g$, faster than free fall.",
      [r"Torque from weight at the center: $MgL/2$.", r"$\alpha = 3g/(2L)$; end: $a_t = \alpha L = 1.5g$."],
      [r"assumes nothing can fall faster than $g$; the pivot's force lets the end exceed $g$.", r"has no basis in $\sum\tau = I\alpha$.", r"is the acceleration of the center of mass, $\alpha(L/2)$, not the end."]),
]

UNIT = Unit(
    n=5, slug="torque-rotational-dynamics", title="Torque and Rotational Dynamics", weight="10--15\\%", topics="5.1--5.6",
    abstract=r"""Unit 5 extends Newton's laws to rigid bodies that rotate about a fixed axis. It covers angular kinematics and the link between angular and linear quantities (5.1--5.2), torque as a cross product (5.3), rotational inertia by summation, integration, and the parallel-axis theorem (5.4), static equilibrium (5.5), and $\sum\tau = I\alpha$, including systems that combine blocks and massive pulleys (5.6). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4],
    qsections=[("Rotational kinematics and torque (5.1--5.3)", QS1[:5]), ("Rotational inertia (5.4)", QS1[5:8]), ("Equilibrium and dynamics (5.5--5.6)", QS1[8:])],
    frq=FRQ("Mathematical Routines", 10, r"""Block 1 ($m_1 = 1.0$ kg) sits on a level, frictionless table. A light string attached to it runs over a pulley at the table's edge to block 2 ($m_2 = 2.0$ kg), which hangs below. The pulley is a uniform solid disk of mass $M = 2.0$ kg and radius $R = 0.10$ m on a frictionless axle, and the string does not slip. The system is released from rest. Use $g = 9.8\ \mathrm{m/s^2}$.""", [
        Part("a", 4, r"Derive an expression for the magnitude $a$ of the blocks' acceleration in terms of $m_1$, $m_2$, $M$, and $g$.",
             r"1 pt: block 1: $T_1 = m_1 a$. 1 pt: block 2: $m_2 g - T_2 = m_2 a$. 1 pt: pulley: $(T_2 - T_1)R = \tfrac12 MR^2\alpha$ with $\alpha = a/R$. 1 pt: $a = \dfrac{m_2 g}{m_1 + m_2 + M/2}$.",
             r"Using one tension for both sides of the pulley."),
        Part("b", 3, r"Calculate $a$ and the tensions $T_1$ (horizontal segment) and $T_2$ (vertical segment).",
             r"1 pt: $a = \dfrac{2.0(9.8)}{4.0} = 4.9\ \mathrm{m/s^2}$. 1 pt: $T_1 = m_1a = 4.9$ N. 1 pt: $T_2 = m_2(g - a) = 9.8$ N (and $T_2 > T_1$).",
             r"Equal tensions, or $T_2 = m_2 g$."),
        Part("c", 3, r"Block 2 falls 1.0 m. Calculate the time this takes and the pulley's angular speed at that moment.",
             r"1 pt: $t = \sqrt{2d/a} = \sqrt{2(1.0)/4.9} = 0.64$ s. 1 pt: $v = at = 3.1$ m/s (or $v = \sqrt{2ad}$). 1 pt: $\omega = v/R = 31$ rad/s.",
             r"Using $g$ instead of $a$ for the fall."),
    ]),
    frq_topic="a block, a hanging mass, and a massive pulley",
)
