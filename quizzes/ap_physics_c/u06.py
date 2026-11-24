from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Rotational kinetic energy, work, and power (6.1--6.2)", ["6.1", "6.2"], r"""
\[ K_{rot} = \tfrac12 I\omega^2, \qquad W = \int_{\theta_1}^{\theta_2}\tau\,d\theta, \qquad W_{net} = \Delta K_{rot}, \qquad P = \tau\omega. \]
These mirror the linear formulas with $m \to I$, $v \to \omega$, $F \to \tau$, $x \to \theta$. A torque does work only while the object turns; a torque that holds something still does none.
\begin{trap}
Convert rpm to rad/s before using $P = \tau\omega$: $300$ rpm $= 300 \times 2\pi/60 = 31.4$ rad/s.
\end{trap}
""", checks=[
    Q("6.1 Rotational kinetic energy", r"A uniform solid disk of mass 2.0 kg and radius 0.50 m spins at 4.0 rad/s about its central axis. What is its kinetic energy?",
      r"$2.0$ J", [r"$4.0$ J", r"$1.0$ J", r"$8.0$ J"],
      r"$I = \tfrac12 MR^2 = 0.25\ \mathrm{kg\,m^2}$, so $K = \tfrac12 I\omega^2 = \tfrac12(0.25)(16) = 2.0$ J.",
      [r"$I = \tfrac12(2.0)(0.50)^2 = 0.25\ \mathrm{kg\,m^2}$.", r"$K = 2.0$ J."],
      [r"uses $I = MR^2$, a hoop.", r"is $I\omega$, the angular momentum (in kg$\cdot$m$^2$/s).", r"uses $I = MR^2$ and also drops the $\tfrac12$ in $K$."], sort=True),
])

S2 = Sec("Angular momentum and angular impulse (6.3)", ["6.3"], r"""
\[ L = I\omega \ \ \text{(rigid body, fixed axis)}, \qquad \vec L = \vec r\times\vec p \ \ \text{(particle)}, \qquad \sum\vec\tau = \frac{d\vec L}{dt}, \qquad \int\tau\,dt = \Delta L. \]
A particle moving in a straight line has angular momentum about any point not on its line: $L = mvr_\perp$, where $r_\perp$ is the perpendicular distance from the point to the line of motion. That is why a bullet can spin up a rod it hits.

\begin{trap}
The particle's angular momentum depends on the reference point. Choose the pivot (or the rotation axis) and keep it for every object in the problem.
\end{trap}
""", checks=[
    Q("6.3 Angular momentum of a particle", r"A 2.0 kg puck slides at 3.0 m/s along the line $y = 4.0$ m, parallel to the $x$-axis. What is the magnitude of its angular momentum about the origin?",
      r"$24\ \mathrm{kg\,m^2/s}$", [r"$6.0\ \mathrm{kg\,m^2/s}$", r"$0$", r"$12\ \mathrm{kg\,m^2/s}$"],
      r"$L = mvr_\perp$ with $r_\perp = 4.0$ m: $L = (2.0)(3.0)(4.0) = 24\ \mathrm{kg\,m^2/s}$, the same at every point on the line.",
      [r"Perpendicular distance from origin to the path: 4.0 m.", r"$L = p\,r_\perp = 6.0 \times 4.0 = 24\ \mathrm{kg\,m^2/s}$."],
      [r"is the linear momentum $mv$.", r"assumes straight-line motion has no angular momentum; it does about any point off its line.", r"halves the correct value."], sort=True),
])

S3 = Sec("Conservation of angular momentum (6.4)", ["6.4"], r"""
If the net external torque on a system about an axis is zero, its angular momentum about that axis is constant:
\[ I_1\omega_1 = I_2\omega_2. \]
\begin{itemize}
\item A spinning skater who pulls in her arms lowers $I$, so $\omega$ rises. Her kinetic energy $\tfrac12 I\omega^2 = L^2/(2I)$ \emph{increases}; the extra comes from the work her muscles do.
\item Rotational ``collisions'' (a disk dropped onto a spinning disk, a person jumping onto a merry-go-round, a bullet embedding in a rod) conserve $L$ but lose kinetic energy, like perfectly inelastic collisions.
\item A pivot can exert a force (so linear momentum is \emph{not} conserved when a bullet hits a pivoted rod) but no torque about the pivot, so $L$ about the pivot is conserved.
\end{itemize}
""", checks=[
    Q("6.4 Skater", r"A spinning skater pulls in her arms, halving her rotational inertia. What happens to her rotational kinetic energy?",
      r"It doubles.", [r"It stays the same.", r"It halves.", r"It quadruples."],
      r"$L$ is conserved, so $\omega$ doubles. $K = L^2/(2I)$, so halving $I$ doubles $K$; her arms do positive work pulling inward.",
      [r"$I\omega$ constant: $\omega_2 = 2\omega_1$.", r"$K_2 = \tfrac12(I/2)(2\omega)^2 = 2K_1$."],
      [r"assumes kinetic energy is conserved; only angular momentum is.", r"applies the change in $I$ but forgets $\omega$ doubles.", r"squares the doubled $\omega$ but forgets $I$ halves."]),
])

S4 = Sec("Rolling (6.5)", ["6.5"], r"""
For rolling \textbf{without slipping}, the contact point is momentarily at rest, so
\[ v_{cm} = \omega R, \qquad a_{cm} = \alpha R, \qquad K = \tfrac12 Mv_{cm}^2 + \tfrac12 I_{cm}\omega^2 = \tfrac12 Mv_{cm}^2\left(1 + \frac{I_{cm}}{MR^2}\right). \]
Writing $I_{cm} = \beta MR^2$ ($\beta = 1$ hoop, $\tfrac12$ disk, $\tfrac25$ sphere), an object released from rest that rolls down a height $h$ reaches
\[ v = \sqrt{\frac{2gh}{1 + \beta}}, \qquad a = \frac{g\sin\theta}{1 + \beta}. \]
Smaller $\beta$ wins the race: sphere, then disk, then hoop, whatever the mass or radius.

\begin{keyidea}[Friction in rolling]
Static friction at the contact point supplies the torque that spins the object, but it does no work because the contact point does not slide. Mechanical energy is conserved. If the object slides while it rolls, kinetic friction acts and does dissipate energy, and $v \ne \omega R$ until slipping stops.
\end{keyidea}
""", checks=[
    Q("6.5 Energy split in rolling", r"A solid sphere rolls without slipping across a floor. What fraction of its kinetic energy is rotational?",
      r"$2/7$", [r"$2/5$", r"$1/2$", r"$5/7$"],
      r"$K_{rot}/K = \beta/(1 + \beta) = \tfrac{2/5}{7/5} = \tfrac27$.",
      [r"$K_{rot} = \tfrac12\left(\tfrac25 MR^2\right)(v/R)^2 = \tfrac15 Mv^2$.", r"$K = \tfrac12 Mv^2 + \tfrac15 Mv^2 = \tfrac{7}{10}Mv^2$; ratio $\tfrac{2}{7}$."],
      [r"is $\beta$ itself, the ratio $K_{rot}/K_{trans}$, not $K_{rot}/K$.", r"assumes an even split.", r"is the translational fraction."]),
])

S5 = Sec("Orbits of satellites (6.6)", ["6.6"], r"""
\begin{compare}{Quantity}{Circular orbit, radius $r$}{Comment}
Speed & $v = \sqrt{GM/r}$ & from $GMm/r^2 = mv^2/r$ \\
Period & $T^2 = \dfrac{4\pi^2}{GM}r^3$ & Kepler's third law \\
Energy & $K = \dfrac{GMm}{2r}$, $U = -\dfrac{GMm}{r}$, $E = -\dfrac{GMm}{2r}$ & $E = -K$; lower orbit $\Rightarrow$ faster but more negative $E$ \\
\end{compare}
In an elliptical orbit gravity is a central force, so it exerts no torque about the planet's center: $L = mvr_\perp$ is constant. At the closest and farthest points the velocity is perpendicular to $\vec r$, so $v_pr_p = v_ar_a$ (Kepler's second law). Mechanical energy is also conserved: $\tfrac12 mv^2 - GMm/r$ is the same everywhere on the orbit.
""", checks=[
    Q("6.6 Circular orbit speed", r"Satellite B orbits a planet at four times the orbital radius of satellite A. How does B's orbital speed compare with A's?",
      r"half as fast", [r"one fourth as fast", r"twice as fast", r"the same"],
      r"$v = \sqrt{GM/r}$, so $r \times 4$ gives $v \times 1/\sqrt4 = 1/2$.",
      [r"$v \propto r^{-1/2}$.", r"$v_B = v_A/2$."],
      [r"uses $v \propto 1/r$ (missing the square root).", r"reverses the dependence; outer satellites move slower.", r"forgets that the gravitational pull, and so the needed speed, falls with distance."]),
    Q("6.6 Elliptical orbit", r"A comet's farthest distance from the Sun is three times its closest distance. Its speed at closest approach is $v$. What is its speed at the farthest point?",
      r"$v/3$", [r"$v/9$", r"$v/\sqrt3$", r"$3v$"],
      r"Angular momentum about the Sun is conserved and $\vec v \perp \vec r$ at both points: $vr_p = v_a(3r_p)$, so $v_a = v/3$.",
      [r"$mv_pr_p = mv_ar_a$.", r"$v_a = v_p r_p/r_a = v/3$."],
      [r"uses an inverse-square scaling, as for force, not angular momentum.", r"uses the circular-orbit scaling $v \propto r^{-1/2}$, which does not apply within one elliptical orbit.", r"reverses the ratio; the comet is slowest when farthest."]),
])

QS1 = [
    Q("6.1 Work and rotational energy", r"How much work is needed to spin a flywheel with $I = 0.50\ \mathrm{kg\,m^2}$ from rest up to 20 rad/s?",
      r"$100$ J", [r"$200$ J", r"$10$ J", r"$5.0$ J"],
      r"$W = \Delta K = \tfrac12 I\omega^2 = \tfrac12(0.50)(400) = 100$ J.",
      [r"$W_{net} = \tfrac12 I\omega_f^2 - 0$."],
      [r"forgets the $\tfrac12$.", r"is the angular momentum $I\omega$.", r"is $\tfrac12 I\omega$, missing the square."], sort=True),
    Q("6.2 Rotational power", r"A motor delivers a constant torque of 12 N$\cdot$m to a shaft turning at 300 rpm. What power does it deliver?",
      r"$380$ W", [r"$3600$ W", r"$60$ W", r"$31$ W"],
      r"$\omega = 300(2\pi/60) = 31.4$ rad/s, so $P = \tau\omega = 12 \times 31.4 = 377$ W.",
      [r"Convert: 300 rpm $= 5.0$ rev/s $= 31.4$ rad/s.", r"$P = 377$ W."],
      [r"uses rpm directly.", r"uses rev/s, leaving out the $2\pi$.", r"is the angular speed in rad/s, not the power."], sort=True),
    Q("6.2 Work by a variable torque", r"A torque $\tau = 3\theta^2$ (N$\cdot$m, with $\theta$ in radians) acts on a wheel with $I = 1.0\ \mathrm{kg\,m^2}$ that starts at rest. What is its angular speed after it turns through 2.0 rad?",
      r"$4.0$ rad/s", [r"$2.8$ rad/s", r"$8.0$ rad/s", r"$16$ rad/s"],
      r"$W = \int_0^2 3\theta^2\,d\theta = 8.0$ J $= \tfrac12 I\omega^2$, so $\omega = \sqrt{16} = 4.0$ rad/s.",
      [r"$W = \theta^3\big|_0^2 = 8.0$ J.", r"$\tfrac12(1.0)\omega^2 = 8.0 \Rightarrow \omega = 4.0$ rad/s."],
      [r"is $\sqrt{8.0}$, which drops the $\tfrac12$ in $\tfrac12 I\omega^2$.", r"is the work, 8.0 J, not the angular speed.", r"is $\omega^2$."], sort=True),
    Q("6.3 Angular momentum as a cross product", r"A particle at $\vec r = (3.0\,\hat\imath + 4.0\,\hat\jmath)$ m has momentum $\vec p = 2.0\,\hat\imath$ kg$\cdot$m/s. What is its angular momentum about the origin?",
      r"$-8.0\,\hat k\ \mathrm{kg\,m^2/s}$", [r"$+8.0\,\hat k\ \mathrm{kg\,m^2/s}$", r"$+6.0\,\hat k\ \mathrm{kg\,m^2/s}$", r"$10\,\hat k\ \mathrm{kg\,m^2/s}$"],
      r"$\vec L = \vec r\times\vec p = (xp_y - yp_x)\hat k = (0 - 4.0 \times 2.0)\hat k = -8.0\,\hat k$.",
      [r"Only $p_x$ is nonzero, so $L_z = -yp_x$.", r"$L_z = -(4.0)(2.0) = -8.0\ \mathrm{kg\,m^2/s}$ (clockwise)."],
      [r"reverses the order of the cross product.", r"uses $x$ instead of $y$ as the lever arm; only the perpendicular distance to the line of motion counts.", r"multiplies $|\vec r| = 5.0$ m by $p$, ignoring the angle."]),
    Q("6.3 Angular impulse", r"A constant torque of 5.0 N$\cdot$m acts for 3.0 s on a wheel ($I = 2.5\ \mathrm{kg\,m^2}$) that starts at rest. What is its final angular speed?",
      r"$6.0$ rad/s", [r"$15$ rad/s", r"$2.0$ rad/s", r"$38$ rad/s"],
      r"Angular impulse $\tau\Delta t = 15\ \mathrm{kg\,m^2/s} = \Delta L = I\omega$, so $\omega = 15/2.5 = 6.0$ rad/s.",
      [r"$\Delta L = (5.0)(3.0) = 15$.", r"$\omega = \Delta L/I = 6.0$ rad/s."],
      [r"is the change in angular momentum, not $\omega$.", r"is the angular acceleration $\tau/I$.", r"multiplies by $I$ instead of dividing."], sort=True),
    Q("6.4 Rotational collision", r"A disk spins freely at $\omega_0$ on a frictionless axle. An identical disk, not rotating, is dropped onto it, and friction soon makes them turn together. What is the final angular speed?",
      r"$\omega_0/2$", [r"$\omega_0$", r"$\omega_0/4$", r"$\omega_0/\sqrt2$"],
      r"No external torque about the axle: $I\omega_0 = 2I\omega_f$, so $\omega_f = \omega_0/2$. Half the kinetic energy becomes thermal energy.",
      [r"$L_i = I\omega_0$; $L_f = (2I)\omega_f$.", r"$\omega_f = \omega_0/2$."],
      [r"ignores the added rotational inertia.", r"squares the ratio.", r"conserves kinetic energy instead of angular momentum; the friction between the disks dissipates energy."]),
    Q("6.4 Bullet and rod", r"A rod of mass $M = 3m$ and length $L$ lies on a frictionless table, pivoted at one end. A bullet of mass $m$ moving at speed $v$ perpendicular to the rod hits the free end and embeds. What is the angular speed just after impact?",
      r"$\dfrac{v}{2L}$", [r"$\dfrac{v}{L}$", r"$\dfrac{v}{4L}$", r"$\dfrac{3v}{4L}$"],
      r"Angular momentum about the pivot is conserved (the pivot exerts no torque about itself): $mvL = \left(\tfrac13 ML^2 + mL^2\right)\omega = 2mL^2\omega$.",
      [r"$I_{rod} = \tfrac13(3m)L^2 = mL^2$.", r"$\omega = \dfrac{mvL}{2mL^2} = \dfrac{v}{2L}$."],
      [r"ignores the rod's rotational inertia.", r"uses $I_{rod} = ML^2$ (all mass at the end).", r"uses linear momentum, $mv = (M + m)v_{end}$; the pivot's impulse means linear momentum is not conserved."]),
    Q("6.4 Skater", r"A skater spins at 2.0 rev/s with her arms out ($I = 4.0\ \mathrm{kg\,m^2}$). She pulls her arms in, reducing $I$ to $1.6\ \mathrm{kg\,m^2}$. What is her new rate of spin?",
      r"$5.0$ rev/s", [r"$0.80$ rev/s", r"$3.2$ rev/s", r"$13$ rev/s"],
      r"$I_1\omega_1 = I_2\omega_2$: $\omega_2 = (4.0/1.6)(2.0) = 5.0$ rev/s. Units of $\omega$ cancel, so rev/s is fine here.",
      [r"$L = 4.0 \times 2.0 = 8.0$ (in kg$\cdot$m$^2\cdot$rev/s).", r"$\omega_2 = 8.0/1.6 = 5.0$ rev/s."],
      [r"inverts the ratio; a smaller $I$ means faster spin.", r"conserves kinetic energy: $\omega \propto 1/\sqrt I$ gives 3.2 rev/s.", r"squares the ratio."], sort=True),
    Q("6.5 Rolling race", r"A solid sphere, a solid cylinder, and a thin hoop are released from rest at the top of the same incline and roll without slipping. In what order do they reach the bottom?",
      r"Sphere, cylinder, hoop", [r"Hoop, cylinder, sphere", r"All arrive together", r"It depends on their masses and radii"],
      r"$a = g\sin\theta/(1 + \beta)$ with $\beta = \tfrac25, \tfrac12, 1$. Less energy tied up in rotation means more speed.",
      [r"Smallest $I/(MR^2)$ has the largest acceleration.", r"Sphere ($\beta = 0.4$), cylinder (0.5), hoop (1)."],
      [r"reverses the order; the hoop has the most rotational inertia per unit mass.", r"would be true for frictionless sliding, not rolling.", r"$M$ and $R$ cancel; only the shape factor $\beta$ matters."]),
    Q("6.5 Rolling speed", r"A solid cylinder rolls without slipping from rest down a ramp, dropping a height of 1.5 m. What is its speed at the bottom? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$4.4$ m/s", [r"$5.4$ m/s", r"$3.8$ m/s", r"$4.6$ m/s"],
      r"$Mgh = \tfrac12 Mv^2(1 + \tfrac12)$, so $v = \sqrt{4gh/3} = \sqrt{19.6} = 4.4$ m/s.",
      [r"$K_{total} = \tfrac34 Mv^2$ for a rolling cylinder.", r"$v^2 = \tfrac43(9.8)(1.5) = 19.6$."],
      [r"is $\sqrt{2gh}$, sliding without friction; it gives rotation no share of the energy.", r"is the hoop's result, $\sqrt{gh}$.", r"is the solid sphere's result, $\sqrt{10gh/7}$."], sort=True),
    Q("6.5 Friction in rolling", r"A ball rolls down an incline without slipping. Which statement about the friction force on it is true?",
      r"It is static friction, it points up the incline, and it does no work on the ball.", [r"It is kinetic friction, it points up the incline, and it removes mechanical energy.", r"It is static friction, it points down the incline, and it speeds the ball up.", r"There is no friction, because the ball does not slide."],
      r"The contact point is momentarily at rest, so the friction is static and does no work. It points up the slope, providing the torque about the center that makes $\alpha = a/R$ grow as the ball speeds up.",
      [r"Without friction the ball would slide without spinning.", r"Friction's torque about the center spins it up; since the contact point does not slide, no energy is dissipated."],
      [r"rolling without slipping involves no sliding, so the friction is static and dissipates nothing.", r"a down-slope friction would spin the ball the wrong way.", r"without friction nothing would provide the torque to spin the ball up."]),
    Q("6.6 Kepler's third law", r"A satellite in a circular orbit of radius $r$ has period $T$. What is the period of a satellite in a circular orbit of radius $4r$ around the same planet?",
      r"$8T$", [r"$2T$", r"$4T$", r"$16T$"],
      r"$T^2 \propto r^3$, so $T \propto r^{3/2} = 4^{3/2} = 8$.",
      [r"$T_2/T_1 = (4)^{3/2} = 8$."],
      [r"uses $T \propto \sqrt r$.", r"uses $T \propto r$.", r"uses $T \propto r^2$."], sort=True),
    Q("6.6 Orbital energy", r"A satellite of mass $m$ moves in a circular orbit of radius $r$ around a planet of mass $M$. What is its total mechanical energy?",
      r"$-\dfrac{GMm}{2r}$", [r"$-\dfrac{GMm}{r}$", r"$+\dfrac{GMm}{2r}$", r"$0$"],
      r"$K = \tfrac12 mv^2 = \dfrac{GMm}{2r}$ (from $v^2 = GM/r$) and $U = -\dfrac{GMm}{r}$, so $E = -\dfrac{GMm}{2r}$.",
      [r"Circular orbit: $mv^2/r = GMm/r^2$.", r"$E = K + U = \tfrac12\left(-\dfrac{GMm}{r}\right)$."],
      [r"is the potential energy alone.", r"is the kinetic energy alone.", r"is the energy of an object that just escapes; a bound orbit has $E < 0$."]),
]

UNIT = Unit(
    n=6, slug="rotating-systems", title="Energy and Momentum of Rotating Systems", weight="10--15\\%", topics="6.1--6.6",
    abstract=r"""Unit 6 brings energy and momentum to rotation. It covers rotational kinetic energy, work by a torque, and rotational power (6.1--6.2); angular momentum of rigid bodies and particles, with angular impulse (6.3); conservation of angular momentum in spins and rotational collisions (6.4); rolling with and without slipping (6.5); and circular and elliptical satellite orbits (6.6). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5],
    qsections=[("Rotational energy and angular momentum (6.1--6.3)", QS1[:5]), ("Conservation of angular momentum (6.4)", QS1[5:8]), ("Rolling and orbits (6.5--6.6)", QS1[8:])],
    frq=FRQ("Translation Between Representations", 12, r"""A uniform solid cylinder of mass $M$ and radius $R$ is released from rest on a ramp inclined at angle $\theta$. It rolls down without slipping.""", [
        Part("a", 2, r"Draw a diagram of the cylinder on the ramp showing every force acting on it, each drawn as an arrow starting at the point where that force acts.",
             r"1 pt: weight $Mg$ at the center, straight down; normal force at the contact point, perpendicular to the ramp. 1 pt: static friction at the contact point, pointing up the ramp; no other forces.",
             r"Drawing all forces at the center, which hides the torque from friction."),
        Part("b", 4, r"Derive expressions for the magnitude of the cylinder's acceleration and the friction force on it, in terms of $M$, $g$, and $\theta$.",
             r"1 pt: $Mg\sin\theta - f = Ma$. 1 pt: $fR = \tfrac12 MR^2\alpha$. 1 pt: uses $a = \alpha R$ to get $a = \tfrac23 g\sin\theta$. 1 pt: $f = \tfrac13 Mg\sin\theta$.",
             r"Using $f = \mu_s N$; the friction takes whatever value rolling requires."),
        Part("c", 3, r"On one set of axes, sketch graphs of the cylinder's translational kinetic energy and its rotational kinetic energy as functions of the distance $d$ it has traveled along the ramp. Label each graph.",
             r"1 pt: both graphs are straight lines through the origin (energy gained is proportional to $d$). 1 pt: the translational line is steeper. 1 pt: the rotational line has half its slope, since $K_{rot} = \tfrac12\cdot\tfrac12 MR^2(v/R)^2 = \tfrac14 Mv^2 = \tfrac12 K_{trans}$.",
             r"Curved graphs, from confusing distance with time ($K \propto t^2$ at constant acceleration)."),
        Part("d", 3, r"The ramp is replaced with an identical one that is frictionless, and the cylinder is released from rest without spinning. How would each graph from part (c) change, and how would the total kinetic energy at a given $d$ compare? Justify your answers.",
             r"1 pt: rotational kinetic energy stays zero for all $d$, because gravity and the normal force exert no torque about the center. 1 pt: total kinetic energy at each $d$ is unchanged, $Mgd\sin\theta$, because energy is conserved in both cases (static friction did no work). 1 pt: so the translational graph is steeper, equal to the old total, slope $Mg\sin\theta$ instead of $\tfrac23 Mg\sin\theta$.",
             r"Saying the total kinetic energy is larger without friction."),
    ]),
    frq_topic="a cylinder rolling down a ramp",
)
