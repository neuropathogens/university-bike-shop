from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

FT1 = Graph(r"Time $t$ (s)", r"Force $F$ (N)", x=(0, 0.010, 0.002), y=(0, 1400, 200),
            series=[Series("force", [(0, 0), (0.005, 1200), (0.010, 0)], marks=False)])
FT2 = Graph(r"Time $t$ (ms)", r"Force $F$ (N)", x=(0, 10, 2), y=(0, 1000, 200),
            series=[Series("force", [(0, 0), (4, 800), (8, 0), (10, 0)], marks=False)])

S1 = Sec("Linear momentum (4.1)", ["4.1"], r"""
The \textbf{momentum} of an object is the product of its mass and velocity:
\[ \vec p = m\vec v . \]
Momentum is a vector in the direction of the velocity, measured in $\mathrm{kg\,m/s}$ (the same as $\mathrm{N\,s}$). The momentum of a system is the vector sum of its parts' momenta, which equals the total mass times the velocity of the center of mass: $\vec p_{sys} = m_{total}\,\vec v_{cm}$.

\begin{trap}
Momentum and kinetic energy both grow with speed, but momentum is a vector ($\propto v$) and kinetic energy a scalar ($\propto v^2$). Two carts moving toward each other at equal speeds have zero total momentum but plenty of kinetic energy.
\end{trap}
""", checks=[
    Q("4.1 Comparing momenta", r"Which has the greater momentum: a $0.15$ kg ball thrown at $40$ m/s, or a $60$ kg runner jogging at $0.10$ m/s?",
      r"They have equal momenta.", [r"the ball", r"the runner", r"It cannot be compared without knowing the directions."],
      r"Ball: $0.15 \times 40 = 6.0\ \mathrm{kg\,m/s}$. Runner: $60 \times 0.10 = 6.0\ \mathrm{kg\,m/s}$.",
      [r"$p = mv$ for each."],
      [r"its large speed is offset by its small mass.",
       r"its large mass is offset by its small speed.",
       r"the question compares the magnitudes, which do not depend on direction."]),
])

S2 = Sec("Change in momentum and impulse (4.2)", ["4.2"], r"""
A net force acting over a time interval changes an object's momentum. The \textbf{impulse} is
\[ \vec J = \vec F_{avg}\,\Delta t = \Delta\vec p , \]
the area under a graph of force versus time. This is Newton's second law in the form $\vec F_{net} = \Delta \vec p/\Delta t$.

\begin{keyidea}[Same change in momentum, different force]
To stop a moving object you must remove a fixed amount of momentum. Stretching the stopping time (air bags, padded floors, bending your knees on landing) makes the average force smaller; a short, hard stop makes it larger.
\end{keyidea}

\begin{trap}
A ball that bounces back has a larger change in momentum than one that stops dead: $\Delta p = m(v_f - v_i)$ with the signs kept. A $0.50$ kg ball hitting a wall at $6.0$ m/s and rebounding at $4.0$ m/s has $|\Delta p| = 0.50(4.0 + 6.0) = 5.0\ \mathrm{kg\,m/s}$, not $1.0$.
\end{trap}
""", checks=[
    Q("4.2 Rebound", r"A $0.50$ kg ball hits a wall at $6.0$ m/s and rebounds along the same line at $4.0$ m/s. The contact lasts $0.020$ s. What is the average force of the wall on the ball?",
      r"$250$ N", [r"$50$ N", r"$100$ N", r"$5.0$ N"],
      r"$|\Delta p| = 0.50(4.0 - (-6.0)) = 5.0\ \mathrm{kg\,m/s}$, so $F = 5.0/0.020 = 250$ N.",
      [r"Take the rebound direction as positive: $v_i = -6.0$ m/s, $v_f = +4.0$ m/s.", r"$F_{avg} = \Delta p/\Delta t = 250$ N."],
      [r"uses the difference in speeds, $2.0$ m/s, ignoring the reversal.",
       r"uses only the final speed.",
       r"is the impulse in $\mathrm{N\,s}$, not the force."], sort=True),
    Q("4.2 Impulse from a graph", r"The graph shows the force a racket exerts on a $0.12$ kg ball that was at rest (a toss at the top of its rise). What is the ball's speed when it leaves the racket?",
      r"$50$ m/s", [r"$100$ m/s", r"$0.72$ m/s", r"$6.0$ m/s"],
      r"Impulse $=$ area $= \tfrac12(0.010)(1200) = 6.0\ \mathrm{N\,s}$, and $v = J/m = 6.0/0.12 = 50$ m/s.",
      [r"Triangle area: $\tfrac12 \times$ base $\times$ height.", r"$\Delta p = J$ and $p_i = 0$."],
      [r"leaves out the $\tfrac12$ in the triangle's area.",
       r"multiplies the impulse by the mass instead of dividing.",
       r"is the impulse, not the speed."], sort=True, fig=FT1),
])

S3 = Sec("Conservation of linear momentum (4.3)", ["4.3"], r"""
If the net external force on a system is zero, its total momentum stays constant:
\[ \sum \vec p_{before} = \sum \vec p_{after}. \]
Internal forces (the push between two skaters, the forces in a collision or an explosion) come in third-law pairs, so they move momentum between parts of the system but never change the total. Equivalently, the system's center of mass keeps a constant velocity.

\begin{terms}
Choose the system & include every object that exerts the large forces on one another (both carts, both skaters) \\
External forces & if they are small or brief compared with the internal ones (friction during a $0.01$ s collision), treat momentum as conserved just before and just after \\
Recoil & a system at rest has zero momentum; after it pushes apart, $m_1 v_1 = -m_2 v_2$ \\
Not conserved & the momentum of a falling ball alone changes (Earth pulls it); the ball--Earth system's momentum does not \\
\end{terms}
""", checks=[
    Q("4.3 Recoil", r"Two skaters stand at rest on frictionless ice. The $60$ kg skater pushes the $40$ kg skater, who moves off at $3.0$ m/s. What is the velocity of the $60$ kg skater?",
      r"$2.0$ m/s in the opposite direction", [r"$3.0$ m/s in the opposite direction", r"$4.5$ m/s in the opposite direction", r"zero, since she did the pushing"],
      r"Total momentum stays zero: $60v = -(40)(3.0)$, so $v = -2.0$ m/s.",
      [r"$0 = m_1 v_1 + m_2 v_2$.", r"$v_1 = -(40 \times 3.0)/60 = -2.0$ m/s."],
      [r"equal speeds would need equal masses.",
       r"inverts the mass ratio.",
       r"by the third law the pushed skater pushes back equally."]),
])

S4 = Sec("Elastic and inelastic collisions (4.4)", ["4.4"], r"""
In every collision between isolated objects momentum is conserved. Kinetic energy may or may not be.

\begin{compare}{Type}{Kinetic energy}{Example}
Elastic & conserved & steel spheres, a cart bouncing off another with magnets \\
Inelastic & some converted to thermal energy, sound, deformation & a tennis ball on a racket \\
Perfectly inelastic & the greatest possible loss: the objects stick and move together & Velcro carts; a car crash where the cars lock \\
\end{compare}

\textbf{Two useful results.} In a head-on elastic collision between equal masses with one at rest, the objects exchange velocities. In a perfectly inelastic collision, $m_1 v_1 + m_2 v_2 = (m_1 + m_2)v_f$, and kinetic energy is \emph{not} conserved, so never use it there.

\begin{example}
A $2.0$ kg cart at $3.0$ m/s hits a $1.0$ kg cart at rest and they stick: $v_f = 6.0/3.0 = 2.0$ m/s. Kinetic energy falls from $9.0$ J to $6.0$ J; the missing $3.0$ J becomes internal energy.
\end{example}
""", checks=[
    Q("4.4 Sticking together", r"A $2.0$ kg cart moving at $3.0$ m/s collides with a $1.0$ kg cart at rest, and the two stick together. How much kinetic energy is converted to other forms?",
      r"$3.0$ J", [r"$0$", r"$6.0$ J", r"$9.0$ J"],
      r"$v_f = (2.0)(3.0)/3.0 = 2.0$ m/s. $K$ goes from $\tfrac12(2.0)(9.0) = 9.0$ J to $\tfrac12(3.0)(4.0) = 6.0$ J.",
      [r"Momentum: $6.0 = 3.0\,v_f$.", r"Loss $= 9.0 - 6.0 = 3.0$ J."],
      [r"momentum is conserved, but kinetic energy is not when the carts stick.",
       r"is the kinetic energy that remains.",
       r"is all the initial kinetic energy; the carts are still moving."], sort=True),
])

QS = [
    Set("Momentum and impulse (4.1--4.2)", [
        Q("4.2 Cushioning", r"An egg dropped onto a pillow survives, while one dropped from the same height onto a floor breaks. Which explains the difference?",
          r"The pillow makes the collision last longer, so the force is smaller for the same change in momentum.", [r"The pillow reduces the egg's change in momentum.", r"The pillow exerts no force on the egg.", r"The egg has less momentum just before it hits the pillow."],
          r"Both eggs go from the same momentum to zero, so the impulse is the same; spreading it over more time lowers $F = \Delta p/\Delta t$.",
          [r"Same height, same speed, same $\Delta p$.", r"Longer $\Delta t$ means smaller average force."],
          [r"both eggs stop, so the change in momentum is the same.",
           r"the pillow must exert a force to stop the egg.",
           r"both fall the same height, so they arrive with the same momentum."]),
        Q("4.2 Bat and ball", r"A $0.20$ kg ball moving horizontally at $15$ m/s is struck by a bat and leaves at $25$ m/s in the opposite direction. The contact lasts $0.0050$ s. What is the average force of the bat on the ball?",
          r"$1600$ N", [r"$400$ N", r"$8.0$ N", r"$1000$ N"],
          r"$|\Delta p| = 0.20(25 + 15) = 8.0\ \mathrm{kg\,m/s}$; $F = 8.0/0.0050 = 1600$ N.",
          [r"The velocity reverses, so the speeds add.", r"$F_{avg} = \Delta p/\Delta t$."],
          [r"subtracts the speeds, ignoring the reversal.",
           r"is the impulse, not the force.",
           r"uses only the final velocity."], sort=True),
        Q("4.1 Total momentum", r"Two $1.0$ kg carts move toward each other, each at $2.0$ m/s. What is the total momentum of the two carts?",
          r"zero", [r"$4.0\ \mathrm{kg\,m/s}$", r"$2.0\ \mathrm{kg\,m/s}$", r"$8.0\ \mathrm{kg\,m/s}$"],
          r"Momentum is a vector: $+2.0$ and $-2.0\ \mathrm{kg\,m/s}$ add to zero.",
          [r"$p = (1.0)(2.0) + (1.0)(-2.0) = 0$."],
          [r"adds the magnitudes, ignoring direction.",
           r"is one cart's momentum.",
           r"is the total kinetic energy in joules, plus a factor of 2."]),
        Q("4.2 Impulse and speed", r"A constant net force of $10$ N acts for $3.0$ s on a $2.0$ kg object that starts at rest. What is its final speed?",
          r"$15$ m/s", [r"$60$ m/s", r"$5.0$ m/s", r"$30$ m/s"],
          r"$J = F\Delta t = 30\ \mathrm{N\,s} = m v$, so $v = 30/2.0 = 15$ m/s.",
          [r"Impulse $= \Delta p$; $p_i = 0$."],
          [r"multiplies the impulse by the mass.",
           r"is the acceleration, $F/m$, in $\mathrm{m/s^2}$.",
           r"is the impulse, not the speed."], sort=True),
    ]),
    Set("A force--time graph (4.2)", [
        Q("4.2 Impulse from area", r"What impulse does the foot deliver to the ball?",
          r"$3.2\ \mathrm{N\,s}$", [r"$6.4\ \mathrm{N\,s}$", r"$3.2 \times 10^3\ \mathrm{N\,s}$", r"$1.6\ \mathrm{N\,s}$"],
          r"Area of the triangle: $\tfrac12(0.0080\ \mathrm{s})(800\ \mathrm{N}) = 3.2\ \mathrm{N\,s}$.",
          [r"Convert milliseconds: $8$ ms $= 0.0080$ s.", r"$J = \tfrac12 \times 0.0080 \times 800 = 3.2\ \mathrm{N\,s}$."],
          [r"leaves out the $\tfrac12$.",
           r"uses $8$ instead of $0.0080$ s.",
           r"counts only the rising half of the triangle."], sort=True),
        Q("4.2 Final speed", r"How fast is the ball moving when it leaves the foot?",
          r"$8.0$ m/s", [r"$1.3$ m/s", r"$16$ m/s", r"$4.0$ m/s"],
          r"$v = J/m = 3.2/0.40 = 8.0$ m/s.",
          [r"$\Delta p = J$ and the ball starts at rest."],
          [r"multiplies by the mass instead of dividing.",
           r"uses the impulse without the $\tfrac12$.",
           r"uses only half the impulse."], sort=True),
        Q("4.2 Average force", r"What is the average force of the foot on the ball during the contact?",
          r"$400$ N", [r"$800$ N", r"$3.2$ N", r"$200$ N"],
          r"$F_{avg} = J/\Delta t = 3.2/0.0080 = 400$ N, half the peak for a triangular pulse.",
          [r"The contact lasts from $0$ to $8$ ms."],
          [r"is the peak force, reached only for an instant.",
           r"is the impulse, in $\mathrm{N\,s}$.",
           r"divides by twice the contact time."], sort=True),
        Q("4.2 Spreading the impulse", r"Suppose the same impulse were delivered over twice the contact time. How would the ball's speed after the kick compare?",
          r"It would be the same.", [r"It would be half as large.", r"It would be twice as large.", r"It would be a quarter as large."],
          r"The final momentum equals the impulse, so the same impulse gives the same speed; only the average force halves.",
          [r"$mv_f = J$, unchanged."],
          [r"the force halves, but it acts twice as long.",
           r"a longer contact with the same impulse does not add momentum.",
           r"nothing here depends on the square of the time."]),
    ], stim=r"A $0.40$ kg ball at rest on the ground is kicked. The graph shows the force of the foot on the ball as a function of time; the friction from the ground is negligible during the kick.",
        fig=FT2, stim_title="Questions 5--8"),
    Set("Conservation and collisions (4.3--4.4)", [
        Q("4.3 Throwing a ball", r"A $50$ kg skater at rest on frictionless ice throws a $2.0$ kg ball forward at $10$ m/s. What is the skater's speed afterward?",
          r"$0.40$ m/s", [r"$10$ m/s", r"$250$ m/s", r"$0$"],
          r"The system starts with zero momentum: $50v = 2.0 \times 10$, so $v = 0.40$ m/s backward.",
          [r"$m_{skater}v_{skater} = -m_{ball}v_{ball}$."],
          [r"equal speeds would need equal masses.",
           r"inverts the mass ratio.",
           r"the total stays zero because skater and ball move in opposite directions, not because both stay still."], sort=True),
        Q("4.4 Rear-end collision", r"A $1000$ kg car moving at $20$ m/s rear-ends a $1500$ kg car at rest, and the two lock together. What is their speed just after the collision?",
          r"$8.0$ m/s", [r"$13$ m/s", r"$10$ m/s", r"$20$ m/s"],
          r"$(1000)(20) = (2500)v_f$, so $v_f = 8.0$ m/s.",
          [r"Momentum before $= 2.0 \times 10^4\ \mathrm{kg\,m/s}$.", r"Combined mass $2500$ kg."],
          [r"divides by the struck car's mass only.",
           r"averages the two speeds without weighting by mass.",
           r"the moving car must share its momentum with the extra mass."], sort=True),
        Q("4.4 Energy in a crash", r"For the collision in the previous question, how much kinetic energy is converted to other forms?",
          r"$1.2 \times 10^5$ J", [r"$0$", r"$8.0 \times 10^4$ J", r"$2.0 \times 10^5$ J"],
          r"$K_i = \tfrac12(1000)(20)^2 = 2.0 \times 10^5$ J; $K_f = \tfrac12(2500)(8.0)^2 = 8.0 \times 10^4$ J; the difference is $1.2 \times 10^5$ J.",
          [r"Perfectly inelastic: kinetic energy is not conserved."],
          [r"conserving momentum does not conserve kinetic energy.",
           r"is the kinetic energy that remains.",
           r"is all the initial kinetic energy; the cars keep moving."], sort=True),
        Q("4.4 Equal masses", r"A billiard ball moving at $2.0$ m/s strikes an identical ball at rest head-on. The collision is elastic. What happens?",
          r"The first ball stops, and the second moves off at $2.0$ m/s.", [r"Both balls move forward at $1.0$ m/s.", r"The first ball bounces back at $2.0$ m/s, and the second stays at rest.", r"Both balls move forward at $2.0$ m/s."],
          r"For equal masses in a head-on elastic collision, the velocities are exchanged; this is the only outcome that conserves both momentum and kinetic energy.",
          [r"Check: momentum $2.0m$ before and after; kinetic energy $2.0m$ before and after."],
          [r"conserves momentum but halves the kinetic energy: that would be perfectly inelastic.",
           r"the second ball must move off, or momentum would reverse.",
           r"doubles the momentum."]),
        Q("4.4 Classifying a collision", r"A $1.0$ kg cart moving at $4.0$ m/s hits a $3.0$ kg cart at rest. Afterward the $1.0$ kg cart moves at $2.0$ m/s backward and the $3.0$ kg cart moves at $2.0$ m/s forward. Which describes the collision?",
          r"Momentum and kinetic energy are both conserved: it is elastic.", [r"Momentum is conserved but kinetic energy is not: it is inelastic.", r"Neither momentum nor kinetic energy is conserved.", r"Kinetic energy is conserved but momentum is not."],
          r"Momentum: $4.0 = -2.0 + 6.0$. Kinetic energy: $8.0\ \mathrm{J} = 2.0 + 6.0$ J. Both totals match.",
          [r"Before: $p = 4.0\ \mathrm{kg\,m/s}$, $K = 8.0$ J.", r"After: $p = (1.0)(-2.0) + (3.0)(2.0) = 4.0$; $K = \tfrac12(1.0)(4.0) + \tfrac12(3.0)(4.0) = 8.0$ J."],
          [r"the kinetic energy totals match.",
           r"both totals match.",
           r"the momentum totals match once the backward velocity is negative."]),
        Q("4.3 Center of mass", r"Two carts collide on a level, frictionless track. Which quantity is the same before, during and after the collision?",
          r"the velocity of the two-cart system's center of mass", [r"each cart's momentum", r"the total kinetic energy of the carts", r"each cart's velocity"],
          r"With no net external force, total momentum $= m_{total}v_{cm}$ is constant, so $v_{cm}$ is too.",
          [r"$\vec p_{sys} = m_{total}\vec v_{cm}$."],
          [r"momentum moves between the carts; only the total is constant.",
           r"kinetic energy dips during the collision even when it is elastic, and is lost when it is not.",
           r"the carts' velocities change; that is what a collision does."]),
    ]),
]

UNIT = Unit(4, "linear-momentum", "Linear Momentum", "10--15\\%", "4.1--4.4",
    abstract=r"""Unit 4 introduces momentum: momentum as a vector, impulse and the area under a force--time graph, conservation of momentum for systems with no net external force, and the difference between elastic and inelastic collisions. Momentum questions are often paired with energy (Unit 3): momentum is conserved in every isolated collision, kinetic energy only in elastic ones. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students want to test whether momentum is conserved when a moving cart collides with a cart at rest and the two stick together. They have a level, low-friction track, two carts with Velcro on facing ends, extra masses that can be added to either cart, a motion sensor, and a balance.

\medskip
In their final experiment, cart $A$ (mass $m_A = 0.50$ kg) is always pushed toward cart $B$ at about the same speed $v_i$, and the mass $m_B$ of cart $B$ is changed between trials. For each trial they record the ratio $v_f/v_i$, where $v_f$ is the speed of the joined carts just after the collision.

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$m_B$ (kg) & 0.25 & 0.50 & 0.75 & 1.00 & 1.50 \\ \midrule
$v_f/v_i$ & 0.66 & 0.51 & 0.40 & 0.34 & 0.25 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe a procedure the students could use to measure $v_i$ and $v_f$ for one trial. Include what is measured, the equipment used, and one step that reduces experimental uncertainty.",
             r"1 pt: measure both carts' masses with the balance. 1 pt: place the motion sensor at the end of the track behind cart $A$; record cart $A$'s velocity just before the collision and the joined carts' velocity just after (from the velocity--time graph, or from the slope of the position--time graph on each side of the collision). 1 pt: repeat each trial several times and average, or read velocities from the straight portions of the graph just before and just after impact.",
             r"Timing the carts with a stopwatch over the whole track; no step that reduces uncertainty."),
        Part("b", 2, r"Momentum conservation predicts $v_f/v_i = m_A/(m_A + m_B)$. Indicate what the students should graph to obtain a straight line, and state the slope and vertical intercept that the prediction gives.",
             r"1 pt: graph $v_i/v_f$ versus $m_B$ (since $v_i/v_f = 1 + m_B/m_A$). 1 pt: predicted slope $1/m_A = 2.0\ \mathrm{kg^{-1}}$ and intercept $1$.",
             r"Graphing $v_f/v_i$ versus $m_B$, which is a curve."),
        Part("c", 3, r"Calculate the values needed for your graph, determine the slope of the best-fit line, and state whether the data support momentum conservation.",
             r"1 pt: $v_i/v_f = 1.52,\ 1.96,\ 2.50,\ 2.94,\ 4.00$. 1 pt: best-fit slope about $1.9$--$2.1\ \mathrm{kg^{-1}}$ with intercept near 1. 1 pt: this agrees with the predicted $2.0\ \mathrm{kg^{-1}}$ and $1$, so the data support conservation of momentum.",
             r"Finding a slope from two raw data points with no linearization."),
        Part("d", 2, r"For the trial with $m_B = 0.50$ kg, determine the fraction of the initial kinetic energy that remains after the collision, and explain where the rest went.",
             r"1 pt: $K_f/K_i = \dfrac{(m_A + m_B)v_f^2}{m_A v_i^2} = \dfrac{1.00}{0.50}(0.51)^2 \approx 0.52$, about half. 1 pt: the rest became internal energy (thermal energy and deformation of the Velcro, sound); momentum is still conserved because no net external horizontal force acts.",
             r"Concluding that because energy was lost, momentum was not conserved."),
    ], mins=28),
    frq_topic="testing momentum conservation with colliding carts",
)
