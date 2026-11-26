from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Rotational kinetic energy (6.1)", ["6.1"], r"""
A rigid object rotating with angular velocity $\omega$ about a fixed axis has rotational kinetic energy
\[ K_{rot} = \tfrac12 I\omega^2 . \]
It is the sum of $\tfrac12 mv^2$ over every bit of the object, using $v = r\omega$. An object that both moves and spins (a rolling wheel) has total kinetic energy $\tfrac12 Mv_{cm}^2 + \tfrac12 I_{cm}\omega^2$.
""", checks=[
    Q("6.1 Rotational kinetic energy", r"A disk with rotational inertia $0.20\ \mathrm{kg\,m^2}$ spins at $10$ rad/s. What is its rotational kinetic energy?",
      r"$10$ J", [r"$2.0$ J", r"$20$ J", r"$1.0$ J"],
      r"$K = \tfrac12 I\omega^2 = \tfrac12(0.20)(100) = 10$ J.",
      [r"Square $\omega$ first: $\omega^2 = 100\ \mathrm{rad^2/s^2}$."],
      [r"is $I\omega$, the angular momentum.",
       r"leaves out the $\tfrac12$.",
       r"is $\tfrac12 I\omega$, with $\omega$ not squared."], sort=True),
])

S2 = Sec("Torque and work (6.2)", ["6.2"], r"""
A torque that turns an object through an angle does work:
\[ W = \tau\,\Delta\theta \quad (\text{constant torque, } \Delta\theta \text{ in radians}), \]
and for a varying torque, $W$ is the area under a graph of torque versus angular position. The rotational work--energy theorem says the net work done by torques equals the change in rotational kinetic energy: $W_{net} = \Delta K_{rot}$.
""", checks=[
    Q("6.2 Work by a torque", r"A constant net torque of $5.0\ \mathrm{N\,m}$ turns a wheel ($I = 0.10\ \mathrm{kg\,m^2}$), initially at rest, through $4.0$ rad. What is the wheel's final angular velocity?",
      r"$20$ rad/s", [r"$400$ rad/s", r"$14$ rad/s", r"$200$ rad/s"],
      r"$W = \tau\Delta\theta = 20$ J $= \tfrac12 I\omega^2$, so $\omega = \sqrt{2(20)/0.10} = 20$ rad/s.",
      [r"$W = 5.0 \times 4.0 = 20$ J.", r"$\omega = \sqrt{2W/I} = \sqrt{400}$."],
      [r"forgets the square root.",
       r"leaves out the factor 2: $\sqrt{W/I}$.",
       r"is $W/I$, with no root and no factor 2."], sort=True),
])

S3 = Sec("Angular momentum and angular impulse (6.3)", ["6.3"], r"""
\begin{terms}
Rigid object & $L = I\omega$ \\
Point object moving in a line & $L = mvr_\perp$ about a chosen point, where $r_\perp$ is the perpendicular distance from the point to the line of motion; an object need not move in a circle to have angular momentum \\
Angular impulse & $\tau\,\Delta t = \Delta L$; the area under a torque--time graph \\
\end{terms}
Angular momentum is the rotational partner of linear momentum, and angular impulse the partner of impulse: a net torque acting for a time changes $L$, just as a net force acting for a time changes $p$.
""", checks=[
    Q("6.3 Angular impulse", r"A net torque of $3.0\ \mathrm{N\,m}$ acts for $2.0$ s on a wheel at rest whose rotational inertia is $0.50\ \mathrm{kg\,m^2}$. What is the wheel's final angular velocity?",
      r"$12$ rad/s", [r"$3.0$ rad/s", r"$6.0$ rad/s", r"$1.5$ rad/s"],
      r"$\Delta L = \tau\Delta t = 6.0\ \mathrm{kg\,m^2/s} = I\omega$, so $\omega = 6.0/0.50 = 12$ rad/s.",
      [r"$L_i = 0$, so $I\omega = 6.0$."],
      [r"multiplies $L$ by $I$ instead of dividing.",
       r"is the angular momentum, not the angular velocity.",
       r"divides the torque by $\Delta t$."], sort=True),
])

S4 = Sec("Conservation of angular momentum (6.4)", ["6.4"], r"""
If the net external torque on a system is zero, its total angular momentum is constant. When a rotating system changes shape, $I_i\omega_i = I_f\omega_f$.

\begin{keyidea}[A spinning skater]
A skater who pulls in her arms reduces $I$, so $\omega$ increases. Her rotational kinetic energy $\tfrac12 I\omega^2 = L^2/(2I)$ \emph{increases}: her muscles do work pulling her arms inward. Angular momentum is conserved; kinetic energy is not.
\end{keyidea}

\begin{trap}
Angular momentum is conserved only about an axis with no external torque. A wheel spinning on a rough axle loses angular momentum to the friction torque.
\end{trap}
""", checks=[
    Q("6.4 Skater", r"A skater spins at $2.0$ rad/s with rotational inertia $4.0\ \mathrm{kg\,m^2}$, then pulls in her arms, reducing it to $1.6\ \mathrm{kg\,m^2}$. Friction is negligible. What is her new angular velocity?",
      r"$5.0$ rad/s", [r"$0.80$ rad/s", r"$3.2$ rad/s", r"$2.0$ rad/s"],
      r"$I_i\omega_i = I_f\omega_f$: $(4.0)(2.0) = (1.6)\omega_f$, so $\omega_f = 5.0$ rad/s.",
      [r"No external torque about the vertical axis, so $L$ is constant."],
      [r"inverts the ratio: a smaller $I$ means faster spin.",
       r"conserves kinetic energy, which is not conserved here.",
       r"$\omega$ must change when $I$ does."], sort=True),
])

S5 = Sec("Rolling (6.5)", ["6.5"], r"""
An object rolls \textbf{without slipping} when the point touching the ground is momentarily at rest. Then
\[ v_{cm} = \omega R, \qquad K = \tfrac12 Mv_{cm}^2 + \tfrac12 I_{cm}\omega^2 . \]
Static friction acts at the contact point but does no work (the point does not slide), so mechanical energy is conserved for rolling without slipping.

\begin{compare}{Object}{$I_{cm}$}{Speed after rolling down height $h$}
Solid sphere & $\tfrac25 MR^2$ & $\sqrt{10gh/7}$ (fastest) \\
Solid cylinder or disk & $\tfrac12 MR^2$ & $\sqrt{4gh/3}$ \\
Thin hoop & $MR^2$ & $\sqrt{gh}$ (slowest) \\
Frictionless sliding block & -- & $\sqrt{2gh}$ \\
\end{compare}
The more of the kinetic energy that goes into rotation, the less is left for translation. None of these speeds depends on the mass or the radius.

\begin{trap}
If the object slips (skids), kinetic friction does work and $v_{cm} \ne \omega R$; the rolling equations no longer hold.
\end{trap}
""", checks=[
    Q("6.5 Kinetic energy of rolling", r"A $3.0$ kg solid disk ($I = \tfrac12 MR^2$) rolls without slipping at $2.0$ m/s. What is its total kinetic energy?",
      r"$9.0$ J", [r"$6.0$ J", r"$12$ J", r"$3.0$ J"],
      r"Translational $\tfrac12(3.0)(4.0) = 6.0$ J plus rotational $\tfrac12(\tfrac12 MR^2)(v/R)^2 = \tfrac14 Mv^2 = 3.0$ J.",
      [r"$\omega = v/R$, so $\tfrac12 I\omega^2 = \tfrac14 Mv^2$."],
      [r"leaves out the rotational energy.",
       r"uses $I = MR^2$, as for a hoop.",
       r"is the rotational part only."], sort=True),
])

S6 = Sec("Motion of orbiting satellites (6.6)", ["6.6"], r"""
For a satellite of mass $m$ orbiting a much larger mass $M$, gravity is the only force, and it points toward $M$'s center, so it exerts no torque about that center.

\begin{terms}
Circular orbit & $\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}$, so $v = \sqrt{GM/r}$: closer orbits are faster \\
Elliptical orbit & the satellite's angular momentum about the central body is conserved: at the closest and farthest points $v_1 r_1 = v_2 r_2$, so it moves fastest when closest \\
Energy & the satellite--planet system's mechanical energy $\tfrac12 mv^2 - GMm/r$ is conserved; kinetic and potential energy trade off around an ellipse \\
Escape & a satellite escapes if its total energy is zero or more: $v_{esc} = \sqrt{2GM/r}$ \\
\end{terms}
""", checks=[
    Q("6.6 Elliptical orbit", r"A satellite in an elliptical orbit is $2R$ from the center of a planet at its closest point and $6R$ at its farthest. How does its speed at the closest point compare with its speed at the farthest point?",
      r"It is $3$ times as fast.", [r"It is $9$ times as fast.", r"It is $\tfrac13$ as fast.", r"It is the same."],
      r"Angular momentum about the planet's center is conserved: $v_1 r_1 = v_2 r_2$, so $v_1/v_2 = 6R/2R = 3$.",
      [r"At those two points the velocity is perpendicular to the radius, so $L = mvr$."],
      [r"squares the ratio.",
       r"inverts the ratio: the satellite is fastest when closest.",
       r"the speed changes around an ellipse."]),
])

QS = [
    Set("Rotational energy and work (6.1--6.2)", [
        Q("6.1 Flywheel energy", r"A flywheel with rotational inertia $2.0\ \mathrm{kg\,m^2}$ spins at $30$ rad/s. What is its rotational kinetic energy?",
          r"$900$ J", [r"$60$ J", r"$1800$ J", r"$30$ J"],
          r"$K = \tfrac12(2.0)(30)^2 = 900$ J.",
          [r"$\omega^2 = 900$; $\tfrac12 \times 2.0 \times 900 = 900$ J."],
          [r"is $I\omega$, the angular momentum.",
           r"leaves out the $\tfrac12$.",
           r"is $\tfrac12 I\omega$."], sort=True),
        Q("6.2 Stopping a flywheel", r"The flywheel in the previous question is slowed to rest by a constant friction torque of $15\ \mathrm{N\,m}$. Through what angle does it turn while stopping?",
          r"$60$ rad", [r"$4.0$ rad", r"$120$ rad", r"$30$ rad"],
          r"The friction torque does $-\tau\Delta\theta$ of work, which must remove all $900$ J: $\Delta\theta = 900/15 = 60$ rad.",
          [r"$\tau\Delta\theta = \Delta K$."],
          [r"is the stopping time in seconds, $I\omega/\tau$.",
           r"doubles the energy.",
           r"halves the energy."], sort=True),
        Q("6.1 Hoop vs. disk", r"A hoop and a solid disk have the same mass and radius and spin about their central axes at the same angular velocity. Which has more rotational kinetic energy?",
          r"the hoop, with twice the disk's", [r"the disk, with twice the hoop's", r"They have the same kinetic energy.", r"the hoop, with four times the disk's"],
          r"$K = \tfrac12 I\omega^2$ with the same $\omega$: $I_{hoop} = MR^2$ is twice $I_{disk} = \tfrac12 MR^2$.",
          [r"$K_{hoop}/K_{disk} = I_{hoop}/I_{disk} = 2$."],
          [r"reverses the rotational inertias.",
           r"kinetic energy depends on $I$, not just $M$ and $R$.",
           r"$K$ is proportional to $I$, not $I^2$."]),
        Q("6.2 Motor", r"A motor exerts a constant torque of $8.0\ \mathrm{N\,m}$ on a wheel ($I = 0.50\ \mathrm{kg\,m^2}$) that starts at rest. Friction is negligible. What is the wheel's angular velocity after one revolution?",
          r"$14$ rad/s", [r"$5.7$ rad/s", r"$200$ rad/s", r"$10$ rad/s"],
          r"One revolution is $2\pi$ rad: $W = 8.0(2\pi) = 50$ J $= \tfrac12(0.50)\omega^2$, so $\omega = 14$ rad/s.",
          [r"$W = \tau\Delta\theta$ with $\Delta\theta$ in radians.", r"$\omega = \sqrt{2W/I} = \sqrt{201}$."],
          [r"uses $1$ rad for one revolution.",
           r"forgets the square root.",
           r"leaves out the factor 2 in $\sqrt{2W/I}$."], sort=True),
    ]),
    Set("A rotating stool (6.3--6.4)", [
        Q("6.4 Pulling in", r"What is the student's angular speed after pulling the dumbbells in?",
          r"$5.0$ rad/s", [r"$0.80$ rad/s", r"$2.0$ rad/s", r"$3.2$ rad/s"],
          r"$L$ is conserved: $3.0 \times 2.0 = 1.2\,\omega_f$, so $\omega_f = 5.0$ rad/s.",
          [r"No external torque about the stool's axis."],
          [r"inverts the ratio.",
           r"$I$ changed, so $\omega$ must.",
           r"conserves kinetic energy instead of angular momentum."], sort=True),
        Q("6.4 Energy when pulling in", r"How does the rotational kinetic energy of the system change when the student pulls the dumbbells in?",
          r"It increases by $9.0$ J, from work done by the student's muscles.", [r"It does not change, because no external torque acts.", r"It decreases by $9.0$ J.", r"It increases, because the angular momentum increases."],
          r"$K_i = \tfrac12(3.0)(2.0)^2 = 6.0$ J and $K_f = \tfrac12(1.2)(5.0)^2 = 15$ J.",
          [r"$K = L^2/(2I)$: same $L$, smaller $I$, larger $K$."],
          [r"no external torque conserves $L$, not $K$.",
           r"has the sign wrong.",
           r"the angular momentum stays the same."]),
        Q("6.4 Dropping the dumbbells", r"Suppose instead that, with arms still outstretched, the student simply lets go of the dumbbells, which fall to the floor. Just after release, the student's angular speed",
          r"stays the same", [r"increases", r"decreases", r"becomes zero"],
          r"Each dumbbell leaves with the velocity it had, carrying away its own angular momentum; the student's $I$ and $L$ drop in the same proportion, so $\omega$ is unchanged.",
          [r"Releasing involves no torque on the student, so her own $\omega$ does not change."],
          [r"would need the student to reduce her own rotational inertia.",
           r"would need a torque opposing her rotation.",
           r"the dumbbells take only their own share of the angular momentum."]),
        Q("6.3 Braking", r"Later, the student (with $L = 6.0\ \mathrm{kg\,m^2/s}$) is stopped by a brake that exerts a constant torque of $1.5\ \mathrm{N\,m}$. How long does it take to stop?",
          r"$4.0$ s", [r"$9.0$ s", r"$0.25$ s", r"$3.0$ s"],
          r"Angular impulse: $\tau\Delta t = \Delta L$, so $\Delta t = 6.0/1.5 = 4.0$ s.",
          [r"$|\Delta L| = 6.0\ \mathrm{kg\,m^2/s}$."],
          [r"multiplies instead of dividing.",
           r"inverts the ratio.",
           r"is $\tau\omega$ at the start, a power in watts."], sort=True),
    ], stim=r"A student sits on a stool that rotates freely with negligible friction, holding a dumbbell in each outstretched hand. With arms out, the rotational inertia of the student, stool and dumbbells is $3.0\ \mathrm{kg\,m^2}$, and they rotate at $2.0$ rad/s. The student then pulls the dumbbells in close to her body, reducing the rotational inertia to $1.2\ \mathrm{kg\,m^2}$.",
        stim_title="Questions 5--8"),
    Set("Rolling and orbits (6.5--6.6)", [
        Q("6.5 Ramp race", r"A solid sphere ($\tfrac25 MR^2$), a solid cylinder ($\tfrac12 MR^2$) and a thin hoop ($MR^2$) are released together from rest at the top of the same incline and roll without slipping. In what order do they reach the bottom?",
          r"sphere, then cylinder, then hoop", [r"hoop, then cylinder, then sphere", r"all at the same time", r"it depends on their masses"],
          r"The smaller the fraction of $I$ to $MR^2$, the less energy goes into spin and the faster the object moves.",
          [r"$v = \sqrt{2gh/(1 + I/MR^2)}$: sphere $1.4$, cylinder $1.5$, hoop $2$ in the denominator."],
          [r"reverses the order: the hoop puts the most energy into rotation.",
           r"would be true for frictionless sliding, not rolling.",
           r"mass cancels from the energy equation."]),
        Q("6.5 Rotational fraction", r"A solid cylinder ($I = \tfrac12 MR^2$) rolls without slipping. What fraction of its total kinetic energy is rotational?",
          r"$\tfrac13$", [r"$\tfrac12$", r"$\tfrac23$", r"$\tfrac14$"],
          r"$K_{rot} = \tfrac14 Mv^2$ and $K_{trans} = \tfrac12 Mv^2$, so $K_{rot}/K_{total} = \tfrac14/\tfrac34 = \tfrac13$.",
          [r"$\tfrac12(\tfrac12 MR^2)(v/R)^2 = \tfrac14 Mv^2$."],
          [r"would be true for a hoop.",
           r"is the translational fraction.",
           r"compares rotational energy with $Mv^2$, not with the total."]),
        Q("6.5 Speed at the bottom", r"A solid cylinder is released from rest at the top of a ramp $1.5$ m high and rolls without slipping. What is its speed at the bottom?",
          r"$4.4$ m/s", [r"$5.4$ m/s", r"$3.8$ m/s", r"$4.6$ m/s"],
          r"$Mgh = \tfrac34 Mv^2$, so $v = \sqrt{4gh/3} = \sqrt{19.6} = 4.4$ m/s.",
          [r"Total $K = \tfrac12 Mv^2 + \tfrac14 Mv^2 = \tfrac34 Mv^2$."],
          [r"is $\sqrt{2gh}$, the speed of a frictionless sliding block.",
           r"is $\sqrt{gh}$, the speed of a rolling hoop.",
           r"is $\sqrt{10gh/7}$, the speed of a rolling solid sphere."], sort=True),
        Q("6.6 Comet", r"A comet's distance from the Sun is $1.0$ AU at its closest point and $5.0$ AU at its farthest. What is the ratio of its speed at the closest point to its speed at the farthest point?",
          r"$5.0$", [r"$25$", r"$0.20$", r"$2.2$"],
          r"Angular momentum about the Sun is conserved, and at both points $v \perp r$: $v_1(1.0) = v_2(5.0)$.",
          [r"$v_1/v_2 = r_2/r_1 = 5.0$."],
          [r"squares the ratio.",
           r"inverts the ratio.",
           r"takes a square root that does not belong."], sort=True),
        Q("6.6 Conserved quantities", r"A satellite moves in an elliptical orbit around Earth. Which quantities are constant?",
          r"the satellite--Earth system's mechanical energy and the satellite's angular momentum about Earth's center", [r"the satellite's speed and kinetic energy", r"the satellite's linear momentum", r"the satellite's kinetic energy and the system's potential energy"],
          r"Gravity points at Earth's center (no torque about it) and is conservative, so $L$ and $K + U$ are constant while $K$ and $U$ trade off.",
          [r"Close in: larger $K$, more negative $U$. Far out: smaller $K$, less negative $U$."],
          [r"the speed varies around an ellipse.",
           r"gravity is a net force on the satellite, so its momentum changes direction and size.",
           r"each changes; only their sum is constant."]),
    ]),
]

UNIT = Unit(6, "rotating-systems", "Energy and Momentum of Rotating Systems", "5--8\\%", "6.1--6.6",
    abstract=r"""Unit 6 applies energy and momentum to rotation: rotational kinetic energy, the work done by a torque, angular momentum and angular impulse, conservation of angular momentum, rolling without slipping, and satellites in circular and elliptical orbits. The theme is the same as in Units 3 and 4: identify the system, then ask which quantities are conserved. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Qualitative/Quantitative Translation", 8, r"""Two identical solid cylinders, each of mass $M$, radius $R$ and rotational inertia $\tfrac12 MR^2$, are released from rest at the same height $h$ on two inclines of the same angle. Cylinder 1 rolls without slipping down a rough incline. Cylinder 2 slides without rotating down an incline so smooth that friction is negligible.""", [
        Part("a", 3, r"Which cylinder has the greater speed at the bottom of its incline, or do they have the same speed? Justify your answer without deriving or using equations.",
             r"1 pt: cylinder 2 (sliding) is faster. 1 pt: both systems convert the same gravitational energy, $Mgh$, into kinetic energy (static friction on the rolling cylinder does no work). 1 pt: the rolling cylinder's kinetic energy is shared between translation and rotation, so less of it is translational, and only translational kinetic energy sets the speed.",
             r"Claiming the rolling cylinder loses energy to friction."),
        Part("b", 3, r"Derive expressions for the speed of each cylinder at the bottom, in terms of $h$ and physical constants as appropriate.",
             r"1 pt: sliding: $Mgh = \tfrac12 Mv_2^2$, so $v_2 = \sqrt{2gh}$. 1 pt: rolling: $Mgh = \tfrac12 Mv_1^2 + \tfrac12\left(\tfrac12 MR^2\right)\omega^2$ with $\omega = v_1/R$. 1 pt: $v_1 = \sqrt{4gh/3}$.",
             r"Leaving out the rotational term, or using $\omega = vR$."),
        Part("c", 2, r"A third solid cylinder has the same mass as cylinder 1 but twice its radius. Using your result from part (b), explain whether it would reach the bottom of the rough incline faster than, slower than, or at the same speed as cylinder 1.",
             r"1 pt: the same speed, because $v_1 = \sqrt{4gh/3}$ contains neither $R$ nor $M$. 1 pt: doubling $R$ quadruples $I$ but halves $\omega$ at a given speed, so the rotational kinetic energy $\tfrac12 I\omega^2 = \tfrac14 Mv^2$ is unchanged.",
             r"Saying the larger cylinder is slower because it has more rotational inertia, without noting that $\omega$ is smaller."),
    ], mins=18),
    frq_topic="a rolling cylinder and a sliding cylinder",
)
