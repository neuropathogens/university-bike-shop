from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Momentum and impulse (4.1--4.2)", ["4.1", "4.2"], r"""
\[ \vec p = m\vec v, \qquad \sum\vec F = \frac{d\vec p}{dt}, \qquad \vec J = \int_{t_1}^{t_2}\vec F\,dt = \Delta\vec p. \]
\begin{terms}
Momentum & A vector; add components, not magnitudes. \\
Impulse & Area under the $F$--$t$ graph. Same impulse, longer contact time $\Rightarrow$ smaller average force (air bags, bending your knees, a catcher's mitt). \\
Average force & $\bar F = \Delta p/\Delta t$. \\
Rebound & A ball that bounces back has $|\Delta p| = m(v_1 + v_2)$, larger than if it stopped. \\
Variable mass & $F = \frac{dp}{dt} = v\frac{dm}{dt}$ when mass is added at constant speed: sand dropping onto a conveyor belt moving at $v$ needs an extra force $v\,dm/dt$. \\
\end{terms}

\begin{trap}
Momentum change has a direction. A 0.20 kg ball hitting a wall at 10 m/s and rebounding at 8.0 m/s has $|\Delta p| = 0.20(10 + 8.0) = 3.6$ N$\cdot$s, not $0.40$ N$\cdot$s.
\end{trap}
""", checks=[
    Q("4.2 Impulse from a graph", r"The force on a ball during a kick rises linearly from 0 to 400 N and falls linearly back to 0, a symmetric triangle lasting 0.010 s in total. What impulse does the ball receive?",
      r"$2.0$ N$\cdot$s", [r"$4.0$ N$\cdot$s", r"$1.0$ N$\cdot$s", r"$40{,}000$ N$\cdot$s"],
      r"Impulse is the area under the $F$--$t$ graph: $\tfrac12(0.010)(400) = 2.0$ N$\cdot$s.",
      [r"Triangle area $= \tfrac12 \times \text{base} \times \text{height}$.", r"$\tfrac12(0.010\ \mathrm{s})(400\ \mathrm{N}) = 2.0$ N$\cdot$s."],
      [r"uses the peak force for the whole time (a rectangle).", r"takes only half the triangle.", r"divides force by time instead of multiplying."], sort=True),
    Q("4.2 Rebound", r"A 0.20 kg ball hits a wall at 10 m/s and bounces straight back at 8.0 m/s. What is the magnitude of its change in momentum?",
      r"$3.6$ kg$\cdot$m/s", [r"$0.40$ kg$\cdot$m/s", r"$2.0$ kg$\cdot$m/s", r"$1.6$ kg$\cdot$m/s"],
      r"The velocity reverses: $\Delta p = m(v_f - v_i) = 0.20(-8.0 - 10) = -3.6$ kg$\cdot$m/s.",
      [r"Take the incoming direction as $+$: $v_i = +10$, $v_f = -8.0$ m/s.", r"$|\Delta p| = 0.20 \times 18 = 3.6$ kg$\cdot$m/s."],
      [r"subtracts the speeds, ignoring the reversal.", r"is the incoming momentum alone, as if the ball stopped.", r"is the outgoing momentum alone."], sort=True),
])

S2 = Sec("Conservation of linear momentum (4.3)", ["4.3"], r"""
If the net external force on a system is zero, its total momentum is constant:
\[ \sum_i m_i\vec v_i = \text{constant} \quad\Longleftrightarrow\quad \vec v_{cm} = \text{constant}. \]
Internal forces (collisions, explosions, a person pushing off a boat) move momentum around inside the system but cannot change the total. During a short collision, momentum is \emph{approximately} conserved even with gravity or friction acting, because their impulse over the brief contact is negligible.

\begin{example}[Explosion from rest]
A 3.0 kg object at rest splits into a 1.0 kg piece moving at 6.0 m/s east and a 2.0 kg piece. Since $\vec p_{total} = 0$, the 2.0 kg piece moves at $6.0/2.0 = 3.0$ m/s west. The center of mass stays put.
\end{example}
""", checks=[
    Q("4.3 Explosion", r"A 3.0 kg object at rest explodes into two pieces. A 1.0 kg piece moves off at 6.0 m/s east. What is the velocity of the other piece?",
      r"$3.0$ m/s west", [r"$6.0$ m/s west", r"$3.0$ m/s east", r"$2.0$ m/s west"],
      r"Total momentum stays zero: $(1.0)(6.0) + (2.0)v = 0$, so $v = -3.0$ m/s (west).",
      [r"$p_{before} = 0$.", r"$2.0\,v = -6.0 \Rightarrow v = -3.0$ m/s."],
      [r"gives both pieces the same speed, which balances momentum only for equal masses.", r"has the right speed but would make the total momentum nonzero.", r"divides by the original 3.0 kg mass instead of the 2.0 kg piece."]),
])

S3 = Sec("Elastic and inelastic collisions (4.4)", ["4.4"], r"""
Momentum is conserved in every collision of an isolated system. Kinetic energy is conserved only in \textbf{elastic} collisions.

\begin{compare}{Type}{What is conserved}{Signature}
Elastic & $\vec p$ and $K$ & objects bounce; in 1D the relative speed reverses: $v_{2f} - v_{1f} = -(v_{2i} - v_{1i})$ \\
Inelastic & $\vec p$ only & some $K$ becomes thermal energy, sound, deformation \\
Perfectly inelastic & $\vec p$ only, maximum $K$ lost & objects stick: $v_f = \dfrac{m_1v_1 + m_2v_2}{m_1 + m_2}$ \\
\end{compare}

\textbf{1D elastic collision, target at rest.} $v_{1f} = \dfrac{m_1 - m_2}{m_1 + m_2}v_{1i}$, $v_{2f} = \dfrac{2m_1}{m_1 + m_2}v_{1i}$. Equal masses exchange velocities. A light object bounces off a heavy one with nearly its original speed.

\textbf{Two dimensions.} Conserve $p_x$ and $p_y$ separately. In an elastic glancing collision between equal masses with one at rest, the two leave at $90^\circ$ to each other.

\begin{example}[Ballistic pendulum]
Split it into two stages. Collision: momentum only, $mv = (m + M)V$. Swing: energy only, $\tfrac12(m + M)V^2 = (m + M)gh$. Using energy through the collision is the classic error.
\end{example}
""", checks=[
    Q("4.4 Kinetic energy lost", r"A cart moving at speed $v$ collides with an identical cart at rest, and they stick together. What fraction of the original kinetic energy is lost?",
      r"$1/2$", [r"$0$", r"$1/4$", r"$3/4$"],
      r"Momentum gives $v_f = v/2$. Then $K_f = \tfrac12(2m)(v/2)^2 = \tfrac14 mv^2$, half of $K_i = \tfrac12 mv^2$.",
      [r"$mv = 2m\,v_f \Rightarrow v_f = v/2$.", r"$K_f/K_i = \tfrac{1}{4}mv^2 \big/ \tfrac12 mv^2 = \tfrac12$."],
      [r"would be an elastic collision; sticking always loses kinetic energy.", r"is the fraction kept by one cart, $(1/2)^2$, forgetting the second cart's mass.", r"is the fraction lost if you forget the doubled mass: $1 - 1/4$."]),
])

QS1 = [
    Q("4.2 Impulse of a variable force", r"A net force $F = 30t^2$ (newtons, $t$ in seconds) acts for 2.0 s on a 3.0 kg cart that starts from rest. What is the cart's final speed?",
      r"$27$ m/s", [r"$80$ m/s", r"$40$ m/s", r"$20$ m/s"],
      r"$J = \int_0^2 30t^2\,dt = 10t^3\big|_0^2 = 80$ N$\cdot$s, so $v = J/m = 80/3.0 = 27$ m/s.",
      [r"Impulse $= 80$ N$\cdot$s.", r"$\Delta v = 80/3.0 = 26.7$ m/s."],
      [r"is the impulse, 80 N$\cdot$s, not divided by the mass.", r"treats the force as linear (a triangle of height 120 N): $\tfrac12(120)(2.0)/3.0$.", r"uses the force at the midpoint time, $F(1) = 30$ N, as the average; for a $t^2$ force the average over 0--2 s is 40 N."], sort=True),
    Q("4.2 Average force", r"A 0.15 kg baseball arrives at 40 m/s and leaves the bat at 50 m/s in the opposite direction. The contact lasts 0.0050 s. What is the average force of the bat on the ball?",
      r"$2700$ N", [r"$300$ N", r"$1500$ N", r"$1200$ N"],
      r"$|\Delta p| = 0.15(40 + 50) = 13.5$ kg$\cdot$m/s, so $\bar F = 13.5/0.0050 = 2700$ N.",
      [r"The velocity reverses, so the speeds add in $\Delta v$.", r"$\bar F = \Delta p/\Delta t = 2.7\times10^3$ N."],
      [r"subtracts the speeds, as if the ball kept moving the same way.", r"uses only the outgoing speed.", r"uses only the incoming speed, as if the ball stopped."], sort=True),
    Q("4.2 Variable mass", r"Sand falls vertically onto a horizontal conveyor belt at 2.0 kg/s. The belt moves at a constant 3.0 m/s. What extra horizontal force must the motor supply to keep the belt's speed constant? (Ignore friction in the rollers.)",
      r"$6.0$ N", [r"$3.0$ N", r"$1.5$ N", r"$0$ N"],
      r"Each second 2.0 kg of sand must be brought from zero to 3.0 m/s horizontally: $F = v\,dm/dt = (3.0)(2.0) = 6.0$ N.",
      [r"$F = dp/dt = v\,\dfrac{dm}{dt}$ (the belt's $v$ is constant).", r"$F = 3.0 \times 2.0 = 6.0$ N."],
      [r"is half the correct value, as if the sand gained speed from an average of 1.5 m/s.", r"divides the belt speed by the mass rate; the force is their product, $v\,dm/dt$.", r"assumes constant speed needs no force; the mass on the belt keeps growing, so its momentum does too."], sort=True),
    Q("4.3 Recoil", r"A 60 kg skater at rest on frictionless ice throws a 2.0 kg ball forward at 15 m/s. How fast does the skater recoil?",
      r"$0.50$ m/s", [r"$15$ m/s", r"$2.7$ m/s", r"$0.033$ m/s"],
      r"Momentum stays zero: $60\,v = 2.0(15)$, so $v = 0.50$ m/s backward.",
      [r"$p_{before} = 0 = (2.0)(15) + (60)v$.", r"$v = -0.50$ m/s."],
      [r"gives the skater the ball's speed; equal momenta, not equal speeds.", r"sets the kinetic energies equal; energy is not shared equally in a push-off.", r"is $2.0/60$, leaving out the ball's speed."], sort=True),
    Q("4.3 Center-of-mass velocity", r"A 2.0 kg cart moves east at 3.0 m/s toward a 1.0 kg cart moving west at 3.0 m/s. What is the velocity of the two-cart system's center of mass?",
      r"$1.0$ m/s east", [r"$0$ m/s", r"$2.0$ m/s east", r"$3.0$ m/s east"],
      r"$v_{cm} = \dfrac{\sum m_iv_i}{\sum m_i} = \dfrac{(2.0)(3.0) + (1.0)(-3.0)}{3.0} = 1.0$ m/s east, before and after any collision.",
      [r"Total momentum $= 6.0 - 3.0 = 3.0$ kg$\cdot$m/s east.", r"$v_{cm} = 3.0/3.0 = 1.0$ m/s."],
      [r"assumes equal speeds cancel; the masses differ.", r"counts only the 2.0 kg cart's momentum, $6.0/3.0$; the westward cart's momentum subtracts.", r"is the speed of either cart, not the system's."], sort=True),
    Q("4.3 Explosion in flight", r"A shell fired from level ground explodes at the top of its arc into two pieces of equal mass. One piece falls straight down from rest. Where does the center of mass of the two pieces land (assuming both land at the same time)?",
      r"Where the shell would have landed without exploding", [r"Directly below the explosion", r"Halfway between the launch point and the explosion point", r"Twice as far as the shell would have gone"],
      r"The explosion's forces are internal, so the center of mass follows the original parabola. The second piece lands at 1.5 times the original range, keeping the center of mass on track.",
      [r"Only gravity (external) acts on the system; $\vec a_{cm} = \vec g$ throughout.", r"So the center of mass lands at the original range $R$; pieces land at $R/2$ and $3R/2$."],
      [r"is where the first piece lands, not the center of mass.", r"has no physical basis; the center of mass keeps moving forward.", r"is where the second piece would land only if it carried all the mass."]),
    Q("4.4 Perfectly inelastic", r"A 1500 kg car moving at 20 m/s rear-ends a 2500 kg truck at rest, and the two lock together. What is their speed just after the collision?",
      r"$7.5$ m/s", [r"$12$ m/s", r"$20$ m/s", r"$10$ m/s"],
      r"Momentum: $1500(20) = 4000\,v$, so $v = 7.5$ m/s.",
      [r"$p = 3.0\times10^4$ kg$\cdot$m/s before and after.", r"$v = 3.0\times10^4/4000 = 7.5$ m/s."],
      [r"divides by the truck's mass only.", r"assumes the car keeps its speed.", r"averages the two speeds without weighting by mass."], sort=True),
    Q("4.4 Energy in a perfectly inelastic collision", r"In the collision of the previous question, what percentage of the car's kinetic energy is lost?",
      r"$63\%$", [r"$38\%$", r"$50\%$", r"$0\%$"],
      r"For a target at rest, $K_f/K_i = m_1/(m_1 + m_2) = 1500/4000 = 0.375$, so 62.5\% is lost.",
      [r"$K_i = \tfrac12(1500)(20)^2 = 3.0\times10^5$ J.", r"$K_f = \tfrac12(4000)(7.5)^2 = 1.125\times10^5$ J.", r"Lost: $1.875\times10^5$ J, 62.5\%."],
      [r"is the fraction kept, not lost.", r"holds only for equal masses.", r"would require an elastic collision; the vehicles stuck together."], sort=True),
    Q("4.4 Elastic collision", r"A 2.0 kg ball moving at 6.0 m/s collides elastically head-on with a 4.0 kg ball at rest. What is the 4.0 kg ball's speed afterward?",
      r"$4.0$ m/s", [r"$2.0$ m/s", r"$3.0$ m/s", r"$6.0$ m/s"],
      r"$v_{2f} = \dfrac{2m_1}{m_1 + m_2}v_{1i} = \dfrac{4.0}{6.0}(6.0) = 4.0$ m/s; the 2.0 kg ball bounces back at 2.0 m/s.",
      [r"Momentum: $12 = 2.0v_{1f} + 4.0v_{2f}$.", r"Relative speed reverses: $v_{2f} - v_{1f} = 6.0$.", r"Solve: $v_{2f} = 4.0$ m/s, $v_{1f} = -2.0$ m/s. Check $K$: $36 = 4 + 32$ J."],
      [r"is the perfectly inelastic result, $12/6.0$ m/s, or the light ball's rebound speed.", r"splits the momentum equally between the balls.", r"is the equal-mass result, where velocities are exchanged."], sort=True),
    Q("4.4 Two-dimensional collision", r"Puck A (0.50 kg) slides east at 5.0 m/s and strikes identical puck B at rest. Afterward A moves at 3.0 m/s, $53^\circ$ north of east. What is B's speed afterward?",
      r"$4.0$ m/s", [r"$2.0$ m/s", r"$8.0$ m/s", r"$3.2$ m/s"],
      r"Conserve each component. A afterward: $(1.8, 2.4)$ m/s. B must carry $(5.0 - 1.8, -2.4) = (3.2, -2.4)$ m/s, a speed of 4.0 m/s.",
      [r"$v_{Ax} = 3.0\cos 53^\circ = 1.8$, $v_{Ay} = 3.0\sin 53^\circ = 2.4$ m/s.", r"$v_{Bx} = 3.2$, $v_{By} = -2.4$; $|v_B| = \sqrt{3.2^2 + 2.4^2} = 4.0$ m/s.",
       r"Kinetic energy is conserved ($25 = 9 + 16$), and the pucks leave at $90^\circ$ to each other: an elastic collision of equal masses."],
      [r"subtracts speeds as if the collision were head-on.", r"adds the speeds.", r"is only the $x$-component of B's velocity."], sort=True),
    Q("4.4 Ballistic pendulum", r"A 10 g bullet embeds in a 2.0 kg block hanging from strings. The block and bullet swing up 0.20 m. What was the bullet's speed? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$400$ m/s", [r"$2.0$ m/s", r"$28$ m/s", r"$200$ m/s"],
      r"Swing (energy): $V = \sqrt{2gh} = 1.98$ m/s. Collision (momentum): $v = \dfrac{(m + M)V}{m} = \dfrac{2.01(1.98)}{0.010} = 400$ m/s.",
      [r"$V = \sqrt{2(9.8)(0.20)} = 1.98$ m/s.", r"$0.010\,v = 2.01(1.98) \Rightarrow v \approx 400$ m/s."],
      [r"is the block's speed just after impact.", r"conserves kinetic energy through the collision, which is perfectly inelastic.", r"halves the correct value; there is no factor of 2 in the momentum step."], sort=True),
    Q("4.2 Impulse and contact time", r"An egg dropped onto a pillow survives, while the same egg dropped from the same height onto concrete breaks. Compared with the concrete, the pillow",
      r"gives the same impulse over a longer time, so the average force is smaller", [r"gives a smaller impulse over a longer time", r"gives a smaller impulse over the same time", r"gives the same impulse but a larger average force"],
      r"The egg's momentum goes from $mv$ to 0 either way, so the impulse is the same. Spreading it over a longer time lowers $\bar F = \Delta p/\Delta t$.",
      [r"Same height $\Rightarrow$ same $v$ $\Rightarrow$ same $\Delta p$.", r"Longer $\Delta t$ $\Rightarrow$ smaller $\bar F$."],
      [r"the egg stops in both cases, so $\Delta p$, and hence the impulse, is the same.", r"the pillow changes the time, not the impulse.", r"a longer time with the same impulse means a smaller force, not larger."]),
]

UNIT = Unit(
    n=4, slug="linear-momentum", title="Linear Momentum", weight="10--20\\%", topics="4.1--4.4",
    abstract=r"""Unit 4 is about momentum, a conserved vector quantity. It covers momentum and impulse, including impulse as the integral of force over time and $F = dp/dt$ for changing mass (4.1--4.2); conservation of momentum and the motion of the center of mass (4.3); and elastic, inelastic, and perfectly inelastic collisions in one and two dimensions (4.4). The free-response question is an experimental design and analysis question on a cart collision. Each guide section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3],
    qsections=[("Impulse (4.1--4.2)", QS1[:3] + [QS1[11]]), ("Conservation of momentum (4.3)", QS1[3:6]), ("Collisions (4.4)", QS1[6:11])],
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students study a collision on a level, low-friction track. Cart A, of mass $m = 0.50$ kg, is pushed so that it moves at an unknown speed $v_0$ toward cart B, of mass $M$, which is at rest. Velcro makes the carts stick together. The students repeat the trial with different values of $M$, launching cart A the same way each time, and record the speed $v_f$ of the joined carts.

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$M$ (kg) & 0.25 & 0.50 & 0.75 & 1.00 & 1.25 \\ \midrule
$v_f$ (m/s) & 0.54 & 0.41 & 0.31 & 0.27 & 0.23 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe a procedure the students could use to measure $v_f$, including the equipment and how each measurement is used. Identify one source of experimental uncertainty and its effect on the measured $v_f$.",
             r"1 pt: a valid speed measurement after the collision, e.g.\ a motion sensor or video with a ruler in frame, or a photogate timing a flag of known length. 1 pt: speed obtained correctly, e.g.\ slope of the position--time data after the collision, or flag length $\div$ gate time. 1 pt: one real source with its direction, e.g.\ friction slows the carts, so the measured $v_f$ is lower than the true speed just after impact.",
             r"Listing ``human error'' or ``measure carefully'' with no mechanism or direction."),
        Part("b", 2, r"Indicate quantities the students could graph to produce a straight line, and explain how that line relates to $v_0$. Use conservation of momentum.",
             r"1 pt: $mv_0 = (m + M)v_f$, so $\dfrac{1}{v_f} = \dfrac{1}{v_0} + \dfrac{1}{mv_0}M$. 1 pt: graph $1/v_f$ versus $M$: slope $= 1/(mv_0)$ (intercept $1/v_0$).",
             r"Graphing $v_f$ versus $M$, which is a curve."),
        Part("c", 3, r"Using the data, calculate the values to be graphed. Determine the slope of a best-fit line (by plotting or by a calculator fit).",
             r"1 pt: $1/v_f = 1.85,\ 2.44,\ 3.23,\ 3.70,\ 4.35$ s/m. 1 pt: a reasonable straight best-fit line (on a plot) or a least-squares fit. 1 pt: slope $\approx 2.5$ s/(m$\cdot$kg), accept $2.3$--$2.7$.",
             r"Calculating the slope from two data points instead of the line."),
        Part("d", 2, r"Use the slope to calculate an experimental value of $v_0$. Then state whether the intercept of your line is consistent with that value.",
             r"1 pt: $v_0 = 1/(m \times \text{slope}) = 1/(0.50 \times 2.5) = 0.80$ m/s. 1 pt: intercept $\approx 1.24$ s/m, so $1/\text{intercept} \approx 0.81$ m/s, consistent with $0.80$ m/s.",
             r"Forgetting the factor $m$ in the slope."),
    ]),
    frq_topic="graphing a cart collision to find the launch speed",
)
