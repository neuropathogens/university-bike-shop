from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Systems and center of mass (2.1)", ["2.1"], r"""
A \textbf{system} is whatever you choose to draw a boundary around. Forces from outside the boundary are \emph{external}; forces between parts of the system are \emph{internal} and cancel in pairs. The system's \textbf{center of mass} moves as if all the mass were there and all external forces acted there:
\[ x_{cm} = \frac{\sum m_i x_i}{\sum m_i}, \qquad x_{cm} = \frac{1}{M}\int x\,dm, \qquad \sum \vec F_{ext} = M\vec a_{cm}. \]
For a rod along $x$ with linear density $\lambda(x)$ (kg/m), $dm = \lambda\,dx$ and $M = \int \lambda\,dx$.

\begin{example}
A rod of length $L$ has $\lambda = bx$. Then $M = \int_0^L bx\,dx = \tfrac12 bL^2$ and $\int_0^L x\,(bx)\,dx = \tfrac13 bL^3$, so $x_{cm} = \tfrac23 L$: the center of mass shifts toward the denser end.
\end{example}

\begin{trap}
The center of mass need not lie inside the object (a ring, a boomerang). Internal forces, such as an explosion, cannot change the motion of the center of mass.
\end{trap}
""", checks=[
    Q("2.1 Continuous center of mass", r"A thin rod of length $L$ lies along the $x$-axis from $x = 0$ to $x = L$. Its linear density is $\lambda = bx$. Where is its center of mass?",
      r"$x = 2L/3$", [r"$x = L/2$", r"$x = L/3$", r"$x = 3L/4$"],
      r"$x_{cm} = \int x\lambda\,dx \big/ \int \lambda\,dx = \tfrac13 bL^3 / \tfrac12 bL^2 = 2L/3$.",
      [r"$M = \int_0^L bx\,dx = \tfrac12 bL^2$.", r"$\int_0^L x\cdot bx\,dx = \tfrac13 bL^3$.", r"$x_{cm} = \tfrac{2}{3}L$, toward the heavier end."],
      [r"is the center of a uniform rod.", r"puts the center toward the light end; density increases with $x$.", r"is the answer for $\lambda \propto x^2$."]),
])

S2 = Sec("Forces, free-body diagrams, and Newton's laws (2.2--2.5)", ["2.2", "2.3", "2.4", "2.5"], r"""
\begin{terms}
First law (2.4) & If the net force on an object is zero, its velocity is constant (possibly zero). Constant velocity needs \emph{no} net force. \\
Second law (2.5) & $\sum \vec F = m\vec a$, applied along each axis separately. In calculus form, $\sum \vec F = \frac{d\vec p}{dt}$. \\
Third law (2.3) & Forces come in pairs: if A pushes on B, B pushes on A with an equal and opposite force. The pair acts on \emph{different} objects, so the two forces never cancel in one free-body diagram. \\
Free-body diagram (2.2) & One dot (the object), one arrow per force, each drawn from the dot and labeled with what exerts it. No components, no velocity or acceleration arrows. \\
Normal force & Perpendicular to the surface; whatever size the motion requires. It equals $mg$ only on a level surface with no other vertical forces and $a_y = 0$. \\
Tension & Same throughout an ideal (massless) string over an ideal (massless, frictionless) pulley. \\
\end{terms}

\begin{keyidea}[Method]
(1) Choose the system and draw the FBD. (2) Choose axes, one along the acceleration if you know its direction. (3) Write $\sum F = ma$ for each axis. (4) Add constraints (a string links accelerations). (5) Solve, then check units and limiting cases.
\end{keyidea}

\begin{example}[Atwood machine]
Masses $m_1 < m_2$ hang over an ideal pulley. Treating both as one system along the string: $a = \dfrac{(m_2 - m_1)g}{m_1 + m_2}$. Then from $m_1$ alone, $T - m_1 g = m_1 a$. Check: if $m_1 = m_2$, $a = 0$ and $T = mg$.
\end{example}

\textbf{Apparent weight.} A scale reads the normal force. In an elevator with acceleration $a$ (up positive), $N = m(g + a)$: heavier when accelerating up \emph{or} slowing while moving down.
""", checks=[
    Q("2.5 Apparent weight", r"A 70 kg person stands on a scale in an elevator that is moving upward at a constant $3$ m/s. What does the scale read? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$690$ N", [r"$900$ N", r"$480$ N", r"$210$ N"],
      r"Constant velocity means $a = 0$, so $N = mg = 686 \approx 690$ N; the speed does not matter.",
      [r"$N - mg = ma = 0$.", r"$N = (70)(9.8) = 686$ N."],
      [r"is $m(g + 3)$, treating the 3 m/s speed as an acceleration.", r"is $m(g - 3)$, the same mistake with the sign reversed.", r"is $m \times 3$, which uses the speed as if it were the net acceleration and ignores gravity."], sort=True),
])

S3 = Sec("Gravitational force (2.6)", ["2.6"], r"""
\[ F_g = \frac{G m_1 m_2}{r^2}, \qquad g(r) = \frac{GM}{r^2}\ \text{outside a spherical body}, \qquad G = 6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}. \]
$r$ is measured from the \emph{center} of the body. Near Earth's surface $g = GM_E/R_E^2 \approx 9.8\ \mathrm{m/s^2}$. Gravitational mass and inertial mass are equal, so all objects fall with the same acceleration.

\begin{trap}
Astronauts in orbit are not weightless because gravity vanishes: at the station's altitude $g$ is still about 90\% of its surface value. They feel weightless because they and the station fall together (no normal force).
\end{trap}
""", checks=[
    Q("2.6 Scaling g", r"Planet X has twice Earth's mass and twice Earth's radius. What is the gravitational field strength at its surface, in terms of Earth's $g$?",
      r"$g/2$", [r"$g$", r"$2g$", r"$g/4$"],
      r"$g \propto M/R^2$: doubling $M$ doubles $g$, doubling $R$ divides it by 4. Net factor $2/4 = 1/2$.",
      [r"$g_X = \dfrac{G(2M)}{(2R)^2} = \dfrac{2}{4}\dfrac{GM}{R^2} = \dfrac{g}{2}$."],
      [r"assumes the two changes cancel; radius enters squared.", r"accounts for the mass but not the radius.", r"accounts for the radius but not the mass."]),
])

S4 = Sec("Friction and spring forces (2.7--2.8)", ["2.7", "2.8"], r"""
\begin{terms}
Kinetic friction & $f_k = \mu_k N$, opposite the relative sliding velocity. \\
Static friction & $f_s \le \mu_s N$. It takes whatever value (up to the maximum) keeps the surfaces from slipping; $\mu_s N$ is only the \emph{limit}. \\
Hooke's law & $F_s = -k\,\Delta x$: the spring pulls back toward its natural length. \\
Springs in parallel & $k_{eq} = k_1 + k_2$ (stiffer). \\
Springs in series & $\dfrac{1}{k_{eq}} = \dfrac{1}{k_1} + \dfrac{1}{k_2}$ (softer); two identical springs give $k/2$. \\
\end{terms}

\begin{keyidea}[Incline at angle $\theta$]
Along the slope gravity contributes $mg\sin\theta$; perpendicular, $N = mg\cos\theta$ (if nothing else pushes into the surface). A block that slides at constant velocity has $\mu_k = \tan\theta$. A block on the verge of slipping has $\mu_s = \tan\theta$.
\end{keyidea}

\begin{trap}
Do not write $f = \mu_s N$ for a block that is simply at rest. A 4 kg block on a level floor pushed with 15 N, with $\mu_s N = 20$ N, feels exactly 15 N of static friction.
\end{trap}
""", checks=[
    Q("2.7 Static friction", r"A block of mass $m$ rests without sliding on a ramp inclined at $\theta$. The coefficient of static friction is $\mu_s$. What is the magnitude of the friction force on the block?",
      r"$mg\sin\theta$", [r"$\mu_s mg\cos\theta$", r"$\mu_s mg$", r"$mg\cos\theta$"],
      r"The block is in equilibrium, so friction exactly balances the downslope component of gravity. $\mu_s N$ is only the maximum available.",
      [r"Along the slope: $f_s - mg\sin\theta = 0$.", r"So $f_s = mg\sin\theta$, which must be $\le \mu_s mg\cos\theta$."],
      [r"is the maximum possible static friction, reached only when the block is about to slip.", r"uses $N = mg$, which is wrong on an incline, and is still only a maximum.", r"is the normal force."]),
])

S5 = Sec("Resistive forces (2.9)", ["2.9"], r"""
A drag force proportional to speed, $\vec F_d = -b\vec v$, turns Newton's second law into a differential equation. For an object falling from rest ($+$ down):
\[ m\frac{dv}{dt} = mg - bv \quad\Rightarrow\quad v(t) = \frac{mg}{b}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac{m}{b}. \]
\begin{itemize}
\item Terminal speed $v_T = mg/b$, found by setting $dv/dt = 0$; no differential equation needed.
\item Initial acceleration is $g$ (no drag at $v = 0$); the acceleration decays as $a = g\,e^{-t/\tau}$.
\item After one time constant, $v = (1 - e^{-1})v_T = 0.63\,v_T$; after $3\tau$, 95\%.
\end{itemize}
To solve: separate variables, $\int_0^v \frac{dv'}{g - (b/m)v'} = \int_0^t dt'$. For drag $\propto v^2$, terminal speed is $\sqrt{mg/c}$.
""", checks=[
    Q("2.9 Terminal speed", r"Two balls of the same size fall through the same fluid with drag force $-bv$ (same $b$). Ball 2 has twice the mass of ball 1. How do their terminal speeds compare?",
      r"$v_{T2} = 2v_{T1}$", [r"$v_{T2} = v_{T1}$", r"$v_{T2} = \sqrt2\,v_{T1}$", r"$v_{T2} = 4v_{T1}$"],
      r"At terminal speed $bv_T = mg$, so $v_T = mg/b$ is proportional to $m$.",
      [r"Set $\sum F = 0$: $mg - bv_T = 0$.", r"$v_T = mg/b \propto m$, so doubling $m$ doubles $v_T$."],
      [r"forgets that the heavier ball needs more drag to balance its weight.", r"is the scaling for drag $\propto v^2$.", r"squares the factor with no reason."]),
])

S6 = Sec("Circular motion (2.10)", ["2.10"], r"""
An object moving in a circle of radius $r$ at speed $v$ accelerates toward the center:
\[ a_c = \frac{v^2}{r} = \omega^2 r, \qquad \sum F_{\text{toward center}} = \frac{mv^2}{r}. \]
``Centripetal force'' is not a new force; it is the net inward force provided by tension, gravity, normal force, or friction. If the speed is changing too, a tangential acceleration $a_t = dv/dt$ adds at right angles.

\begin{compare}{Situation}{Inward equation}{Result}
Flat curve, friction & $\mu_s mg = mv^2/r$ & $v_{max} = \sqrt{\mu_s g r}$ \\
Banked curve, no friction & $N\sin\theta = mv^2/r$, $N\cos\theta = mg$ & $\tan\theta = v^2/(rg)$ \\
Top of vertical loop & $N + mg = mv^2/r$ & $v_{min} = \sqrt{gr}$ (when $N = 0$) \\
Bottom of vertical circle & $T - mg = mv^2/r$ & tension is largest here \\
Conical pendulum & $T\sin\theta = mv^2/r$, $T\cos\theta = mg$ & $\tan\theta = v^2/(rg)$ \\
\end{compare}
""", checks=[
    Q("2.10 Vertical loop", r"A roller-coaster car goes around the inside of a vertical loop of radius $r$. What is the minimum speed at the top for the car to stay on the track?",
      r"$\sqrt{gr}$", [r"$\sqrt{2gr}$", r"$gr$", r"$0$"],
      r"At minimum speed the track pushes with zero force, so gravity alone supplies the centripetal force: $mg = mv^2/r$.",
      [r"At the top: $N + mg = mv^2/r$ with $N \ge 0$.", r"Smallest $v$ when $N = 0$: $v = \sqrt{gr}$."],
      [r"is the speed gained falling $r$ from rest, not the condition at the top.", r"has the wrong units (m$^2$/s$^2$).", r"forgets that the car must still move in a circle; with $v = 0$ it falls."]),
])

QS1 = [
    Q("2.1 Center of mass", r"A 2.0 kg mass sits at $x = 0$ and a 6.0 kg mass at $x = 4.0$ m. Where is the center of mass of the pair?",
      r"$3.0$ m", [r"$2.0$ m", r"$1.0$ m", r"$4.0$ m"],
      r"$x_{cm} = (2.0 \cdot 0 + 6.0 \cdot 4.0)/8.0 = 3.0$ m, closer to the heavier mass.",
      [r"$\sum m_i x_i = 24$ kg$\cdot$m.", r"$x_{cm} = 24/8.0 = 3.0$ m."],
      [r"is the midpoint, correct only for equal masses.", r"swaps the masses, putting the center near the lighter one.", r"puts the center at the heavy mass itself."], sort=True),
    Q("2.1 Continuous center of mass", r"A rod 2.0 m long lies from $x = 0$ to $x = 2.0$ m. Its linear density is $\lambda = 3x^2$ (kg/m). Where is its center of mass?",
      r"$1.5$ m", [r"$1.0$ m", r"$1.3$ m", r"$2.0$ m"],
      r"$M = \int_0^2 3x^2\,dx = 8$ kg and $\int_0^2 x\cdot 3x^2\,dx = 12$ kg$\cdot$m, so $x_{cm} = 1.5$ m.",
      [r"$M = x^3\big|_0^2 = 8$ kg.", r"$\int_0^2 3x^3\,dx = \tfrac34 x^4\big|_0^2 = 12$.", r"$x_{cm} = 12/8 = 1.5$ m."],
      [r"is the geometric center; the rod is denser toward $x = 2$.", r"is $2L/3$, the result for a density that grows linearly, not quadratically.", r"is the dense end; the center of mass is a weighted average and stays inside the rod."], sort=True),
    Q("2.3 Third law", r"A loaded truck collides head-on with a small car. During the collision, how does the force the truck exerts on the car compare with the force the car exerts on the truck?",
      r"They are equal in magnitude and opposite in direction.", [r"The truck exerts the larger force because it has more mass.", r"The car exerts the larger force because it has the larger acceleration.", r"The truck exerts the larger force because it is moving faster."],
      r"Newton's third law: the two forces are a pair and are always equal and opposite. The car's larger acceleration comes from its smaller mass, $a = F/m$.",
      [r"$\vec F_{T\to C} = -\vec F_{C\to T}$ at every instant.", r"Same force, different masses: the car's acceleration is much larger."],
      [r"confuses force with effect; mass changes the acceleration, not the force.", r"reverses cause and effect; equal forces produce the larger acceleration in the smaller mass.", r"speed does not enter the third law."]),
    Q("2.5 Atwood machine", r"Masses of 3.0 kg and 5.0 kg hang from the two ends of a light string over an ideal pulley and are released. What is the tension in the string? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$37$ N", [r"$29$ N", r"$49$ N", r"$39$ N"],
      r"First $a = (5.0 - 3.0)(9.8)/8.0 = 2.45\ \mathrm{m/s^2}$. Then for the 3.0 kg mass, which accelerates upward, $T = m_1(g + a) = 3.0(12.25) = 37$ N.",
      [r"System: $a = \dfrac{(m_2 - m_1)g}{m_1 + m_2} = 2.45\ \mathrm{m/s^2}$.", r"3.0 kg mass: $T - m_1 g = m_1 a \Rightarrow T = 36.75 \approx 37$ N.",
       r"Check with the 5.0 kg mass: $m_2 g - T = m_2 a$ gives $49 - 36.75 = 12.25 = 5.0(2.45)$."],
      [r"is the weight of the 3.0 kg mass; the tension must exceed it for that mass to accelerate upward.", r"is the weight of the 5.0 kg mass; the tension must be less for that mass to accelerate downward.", r"averages the two weights; the correct value is $2m_1 m_2 g/(m_1 + m_2)$, which is not the average."], sort=True),
    Q("2.5 Apparent weight", r"A 60 kg student stands on a scale in an elevator. The elevator is moving upward but slowing down at $2.0\ \mathrm{m/s^2}$. What does the scale read? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$470$ N", [r"$590$ N", r"$710$ N", r"$120$ N"],
      r"Slowing while moving up means the acceleration is downward, $a = -2.0\ \mathrm{m/s^2}$. Then $N = m(g + a) = 60(7.8) = 468$ N.",
      [r"Take up as $+$: $N - mg = ma$ with $a = -2.0$.", r"$N = 60(9.8 - 2.0) = 468 \approx 470$ N."],
      [r"is $mg$, which assumes zero acceleration.", r"uses $a = +2.0$; the direction of motion is up, but the acceleration is down.", r"is $ma$ alone, the net force, not the normal force."], sort=True),
    Q("2.5 Time-varying force", r"A net force $F = 6t$ (newtons, $t$ in seconds) acts on a 2.0 kg block that starts from rest. What is its speed at $t = 2.0$ s?",
      r"$6.0$ m/s", [r"$12$ m/s", r"$3.0$ m/s", r"$24$ m/s"],
      r"$a = F/m = 3t$, so $v = \int_0^2 3t\,dt = \tfrac32 t^2\big|_0^2 = 6.0$ m/s.",
      [r"$a(t) = 6t/2.0 = 3t$.", r"$v(2) = \tfrac32(2.0)^2 = 6.0$ m/s."],
      [r"treats the final force, $F(2) = 12$ N, as constant: $(12/2.0)(2.0) = 12$ m/s.", r"is the average acceleration, $3.0\ \mathrm{m/s^2}$, not the speed.", r"multiplies the final force by the time without dividing by the mass."], sort=True),
    Q("2.6 Gravitational field", r"A satellite orbits at an altitude equal to Earth's radius. What is the gravitational field strength at its location? ($g = 9.8\ \mathrm{m/s^2}$ at the surface)",
      r"$2.5\ \mathrm{m/s^2}$", [r"$4.9\ \mathrm{m/s^2}$", r"$9.8\ \mathrm{m/s^2}$", r"$0\ \mathrm{m/s^2}$"],
      r"The distance from Earth's center doubles ($r = 2R_E$), and $g \propto 1/r^2$, so $g = 9.8/4 = 2.45\ \mathrm{m/s^2}$.",
      [r"$r = R_E + R_E = 2R_E$.", r"$g(2R_E) = g/2^2 = 2.45\ \mathrm{m/s^2}$."],
      [r"uses $1/r$ instead of $1/r^2$.", r"ignores the change in distance.", r"confuses the feeling of weightlessness in free fall with zero gravity."], ),
    Q("2.7 Static friction", r"A 4.0 kg crate rests on a level floor ($\mu_s = 0.50$, $\mu_k = 0.30$). A worker pushes it horizontally with 15 N. What is the friction force on the crate? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$15$ N", [r"$20$ N", r"$12$ N", r"$0$ N"],
      r"The maximum static friction is $\mu_s mg = 19.6$ N, more than 15 N, so the crate stays put and static friction just matches the push.",
      [r"$f_{s,max} = 0.50(4.0)(9.8) = 19.6$ N $> 15$ N: no sliding.", r"Equilibrium: $f_s = 15$ N, opposite the push."],
      [r"is the maximum static friction, which is not reached.", r"is kinetic friction, $\mu_k mg = 11.8$ N, but the crate is not sliding.", r"would leave a net 15 N and the crate would accelerate."], sort=True),
    Q("2.7 Constant-velocity incline", r"A block slides down a ramp inclined at $30^\circ$ at constant velocity. What is the coefficient of kinetic friction?",
      r"$0.58$", [r"$0.50$", r"$0.87$", r"$1.7$"],
      r"Constant velocity: $mg\sin\theta = \mu_k mg\cos\theta$, so $\mu_k = \tan 30^\circ = 0.58$.",
      [r"Along the slope: $mg\sin\theta - \mu_k N = 0$.", r"$N = mg\cos\theta$, so $\mu_k = \tan\theta = 0.577$."],
      [r"is $\sin 30^\circ$, which uses $N = mg$.", r"is $\cos 30^\circ$.", r"is $1/\tan 30^\circ$, the ratio upside down."], sort=True),
    Q("2.8 Springs in series", r"Two identical springs, each of constant $k$, are hooked end to end and hung from the ceiling. A block of mass $m$ hangs from the bottom and is at rest. By how much does the pair stretch in total?",
      r"$2mg/k$", [r"$mg/k$", r"$mg/(2k)$", r"$4mg/k$"],
      r"Each spring carries the full weight $mg$ and stretches $mg/k$; two in series stretch $2mg/k$. Equivalently $k_{eq} = k/2$.",
      [r"The tension is $mg$ throughout the chain.", r"Each spring: $\Delta x = mg/k$. Total: $2mg/k$."],
      [r"is the stretch of one spring alone.", r"is the result for springs side by side (parallel), $k_{eq} = 2k$.", r"double counts: each spring carries $mg$, not $2mg$."]),
    Q("2.9 Linear drag", r"A ball is dropped from rest in a fluid that exerts a drag force $-bv$. Its terminal speed is $v_T$. What is its speed at time $t = m/b$ after release?",
      r"$0.63\,v_T$", [r"$0.37\,v_T$", r"$0.50\,v_T$", r"$0.86\,v_T$"],
      r"$v(t) = v_T(1 - e^{-t/\tau})$ with $\tau = m/b$. At $t = \tau$, $v = (1 - e^{-1})v_T = 0.63\,v_T$.",
      [r"$m\,dv/dt = mg - bv$ gives $v = v_T(1 - e^{-bt/m})$.", r"$1 - e^{-1} = 0.632$."],
      [r"is $e^{-1}$, the fraction of $v_T$ still to be gained.", r"assumes linear approach to $v_T$ over $2\tau$; the approach is exponential.", r"is $1 - e^{-2}$, the speed at $t = 2\tau$."], ),
    Q("2.10 Flat curve", r"A car rounds a flat curve of radius 50 m. The coefficient of static friction between tires and road is 0.80. What is the greatest speed at which it can take the curve without skidding? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$20$ m/s", [r"$14$ m/s", r"$22$ m/s", r"$28$ m/s"],
      r"Static friction supplies the centripetal force: $\mu_s mg = mv^2/r$, so $v = \sqrt{\mu_s g r} = \sqrt{392} = 19.8$ m/s.",
      [r"$v_{max}^2 = (0.80)(9.8)(50) = 392$.", r"$v_{max} = 19.8 \approx 20$ m/s; the mass cancels."],
      [r"halves $\mu_s g r$ before the square root.", r"is $\sqrt{gr}$, which leaves out $\mu_s$.", r"is $\sqrt{2\mu_s g r}$; the factor of 2 belongs to energy problems ($v^2 = 2gh$), not to circular motion."], sort=True),
    Q("2.10 Vertical circle", r"A ball on a string is whirled in a vertical circle at nearly constant speed. Where is the string's tension greatest?",
      r"At the bottom, where tension must both balance gravity and supply the centripetal force", [r"At the top, where gravity and tension both point toward the center", r"At the sides, where gravity is perpendicular to the string", r"It is the same everywhere because the speed is constant"],
      r"At the bottom $T - mg = mv^2/r$, so $T = mg + mv^2/r$; at the top $T = mv^2/r - mg$.",
      [r"Bottom: tension points up (inward), gravity down (outward).", r"Top: gravity helps, so less tension is needed."],
      [r"is where tension is smallest, since gravity already supplies part of the inward force.", r"there $T = mv^2/r$, between the top and bottom values.", r"constant speed fixes the net inward force, not the tension; gravity's inward share changes around the circle."]),
]

UNIT = Unit(
    n=2, slug="force-dynamics", title="Force and Translational Dynamics", weight="20--25\\%", topics="2.1--2.10",
    abstract=r"""Unit 2 is the largest unit of the Mechanics exam. It covers systems and center of mass, including calculus for continuous objects (2.1); free-body diagrams and Newton's three laws (2.2--2.5); universal gravitation (2.6); static and kinetic friction and springs (2.7--2.8); velocity-dependent drag and the differential equation it produces (2.9); and circular motion (2.10). Most exam problems reduce to the same method: draw the free-body diagram, write $\sum F = ma$ along each axis, and add any constraint. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6],
    qsections=[("Systems and Newton's laws (2.1--2.5)", QS1[:6]), ("Gravity, friction, and springs (2.6--2.8)", QS1[6:10]), ("Drag and circular motion (2.9--2.10)", QS1[10:])],
    frq=FRQ("Translation Between Representations", 12, r"""A small sphere of mass $m$ is released from rest at $t = 0$ in a tall column of oil. The oil exerts a drag force of magnitude $bv$, where $b$ is a positive constant and $v$ is the sphere's speed. Ignore buoyancy. Take downward as positive.""", [
        Part("a", 2, r"Draw and label a free-body diagram of the sphere at an instant after release when it is moving downward. Represent each force with an arrow starting on the dot.",
             r"1 pt: a downward arrow labeled weight or $mg$. 1 pt: an upward arrow labeled drag, $bv$, with no extra forces (no ``net force'' or velocity arrows).",
             r"Adding a separate ``terminal force'' arrow, or drawing drag downward."),
        Part("b", 4, r"Write, but do not solve, a differential equation for $v(t)$. Then solve it, using the initial condition, to derive $v(t)$ in terms of $m$, $b$, $g$, and $t$.",
             r"1 pt: $m\,\dfrac{dv}{dt} = mg - bv$. 1 pt: separates variables, $\displaystyle\int_0^v \frac{dv'}{g - (b/m)v'} = \int_0^t dt'$. 1 pt: integrates correctly, $-\frac{m}{b}\ln\!\left(1 - \frac{bv}{mg}\right) = t$. 1 pt: $v(t) = \dfrac{mg}{b}\left(1 - e^{-bt/m}\right)$.",
             r"Writing $v = gt - (b/m)vt$, which treats $v$ as constant inside the drag term."),
        Part("c", 3, r"Sketch a graph of $v$ versus $t$. On the graph, label the terminal speed as an expression and indicate the slope of the graph at $t = 0$.",
             r"1 pt: curve starts at the origin and rises, concave down. 1 pt: approaches a horizontal asymptote labeled $v_T = mg/b$ without crossing it. 1 pt: initial slope labeled $g$ (drag is zero at $v = 0$).",
             r"A straight line up to $v_T$ that then turns flat, or a curve that overshoots $v_T$."),
        Part("d", 3, r"A second sphere of the same size, so the same $b$, but mass $2m$ is released in the same oil. On the same axes, how does its graph compare with the first? Justify your answer using your expressions from part (b).",
             r"1 pt: same initial slope $g$ (both start with only gravity acting). 1 pt: terminal speed doubles, $v_T = 2mg/b$. 1 pt: it takes longer to approach terminal speed because $\tau = 2m/b$ doubles; its curve lies above the first at every $t > 0$.",
             r"Claiming the heavier sphere has a larger initial acceleration."),
    ]),
    frq_topic="a sphere falling with linear drag",
)
