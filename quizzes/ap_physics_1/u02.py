from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

SPRING = Graph(r"Stretch $\Delta x$ (m)", r"Force $F$ (N)", x=(0, 0.20, 0.05), y=(0, 8, 2),
               series=[Series("spring", [(0, 0), (0.05, 2.0), (0.10, 4.0), (0.15, 6.0), (0.20, 8.0)])])

S1 = Sec("Systems and center of mass (2.1)", ["2.1"], r"""
A \textbf{system} is whatever you choose to analyze: one block, two blocks tied together, a person and the Earth. Forces between parts of the system are \textbf{internal} and cancel in pairs; only \textbf{external} forces change the motion of the system as a whole. Choosing the system well removes unknown internal forces from the problem.

\textbf{Center of mass.} For objects along a line,
\[ x_{cm} = \frac{\sum m_i x_i}{\sum m_i}. \]
The center of mass of a uniform, symmetric object is at its geometric center. A system's center of mass moves as if all the mass were concentrated there and all the external forces acted on it; internal forces cannot change its velocity.

\begin{trap}
Treating a system as a single object is fine for its overall motion, but the system's internal structure (how the parts move relative to one another) then drops out of the analysis.
\end{trap}
""", checks=[
    Q("2.1 Center of mass", r"A $2.0$ kg ball sits at $x = 0$ and a $6.0$ kg ball at $x = 4.0$ m. Where is the center of mass of the two balls?",
      r"$x = 3.0$ m", [r"$x = 2.0$ m", r"$x = 1.0$ m", r"$x = 4.0$ m"],
      r"$x_{cm} = (2.0 \times 0 + 6.0 \times 4.0)/8.0 = 3.0$ m, closer to the heavier ball.",
      [r"$\sum m_i x_i = 0 + 24 = 24\ \mathrm{kg\,m}$.", r"$x_{cm} = 24/8.0 = 3.0$ m."],
      [r"is the midpoint, which ignores the different masses.",
       r"is weighted toward the lighter ball, the wrong way round.",
       r"is the position of the heavier ball itself."], sort=True),
])

S2 = Sec("Forces, free-body diagrams and Newton's third law (2.2--2.3)", ["2.2", "2.3"], r"""
A force is an interaction between two objects. Contact forces (normal, friction, tension, spring) need touching; the gravitational force acts at a distance.

\begin{terms}
Free-body diagram & the object as a dot; one arrow per force, drawn from the dot in the force's direction, each labeled with what exerts it (``$F_g$, Earth on block''). No velocity or acceleration arrows, no ``$ma$'' arrow. \\
Normal force $F_N$ & perpendicular to the contact surface; only as large as needed to stop the objects passing through each other \\
Tension $F_T$ & pulls along a rope; a light rope over a light, frictionless pulley has the same tension at both ends \\
Weight $F_g = mg$ & downward, toward Earth's center \\
\end{terms}

\begin{keyidea}[Newton's third law]
If $A$ pushes on $B$, then $B$ pushes on $A$ with a force of the same size, opposite direction and same type, at the same time. The two forces act on \emph{different} objects, so they never appear on the same free-body diagram and never cancel each other.
\end{keyidea}

\begin{trap}
The normal force on a book resting on a table is not the third-law partner of the book's weight. The partner of ``Earth pulls book down'' is ``book pulls Earth up''; the partner of ``table pushes book up'' is ``book pushes table down''.
\end{trap}
""", checks=[
    Q("2.3 Third-law pairs", r"A book rests on a table. Which force is the Newton's third law partner of the upward normal force that the table exerts on the book?",
      r"the downward force of the book on the table", [r"the gravitational force of Earth on the book", r"the upward gravitational force of the book on Earth", r"the downward force of Earth on the table"],
      r"Third-law partners involve the same two objects with the roles swapped: table on book, book on table.",
      [r"Name the pair: ``table pushes book up'' $\leftrightarrow$ ``book pushes table down''."],
      [r"acts on the same object (the book), so it cannot be the partner; it is equal here only because the book is in equilibrium.",
       r"is the partner of the book's weight, not of the normal force.",
       r"involves Earth and the table, not the book."]),
    Q("2.3 Collisions", r"A large truck collides head-on with a small car. During the collision, how does the force of the truck on the car compare with the force of the car on the truck?",
      r"They are equal in size.", [r"The truck's force on the car is larger.", r"The car's force on the truck is larger.", r"It depends on which vehicle was moving faster."],
      r"The two forces are a third-law pair, equal and opposite whatever the masses or speeds.",
      [r"The car suffers more because its smaller mass gives it a larger acceleration, $a = F/m$, from the same force."],
      [r"confuses force with its effect; the car's acceleration is larger, not the force.",
       r"also violates the third law.",
       r"speeds change the size of both forces together, never one more than the other."]),
])

S3 = Sec("Newton's first and second laws (2.4--2.5)", ["2.4", "2.5"], r"""
\textbf{First law.} If the net external force on a system is zero, its velocity is constant (possibly zero). Constant velocity needs no net force; a change of speed or direction does.

\textbf{Second law.} $\vec a_{sys} = \dfrac{\sum \vec F}{m_{sys}}$. Apply it along each axis separately, choosing one axis along the acceleration.

\begin{keyidea}[A method that always works]
(1) Choose the system. (2) Draw its free-body diagram. (3) Choose axes, one along the acceleration. (4) Write $\sum F = ma$ for each axis. (5) For connected objects, write one equation per object (or treat them as one system to find $a$, then one object to find the tension).
\end{keyidea}

\textbf{Apparent weight.} A scale reads the normal force. In an elevator accelerating upward at $a$, $F_N - mg = ma$, so the scale reads $m(g + a)$, more than the weight; accelerating downward it reads $m(g - a)$, and in free fall it reads zero.
""", checks=[
    Q("2.5 Apparent weight", r"A $60$ kg student stands on a scale in an elevator that is accelerating upward at $2.0\ \mathrm{m/s^2}$. What does the scale read?",
      r"$710$ N", [r"$590$ N", r"$470$ N", r"$120$ N"],
      r"$F_N - mg = ma$, so $F_N = m(g + a) = 60(11.8) = 708 \approx 710$ N.",
      [r"Free-body diagram: $F_N$ up, $mg = 588$ N down.", r"$F_N = 588 + 60(2.0) = 708$ N."],
      [r"is the true weight, which the scale shows only when the acceleration is zero.",
       r"subtracts $ma$, which is the reading for a downward acceleration.",
       r"is $ma$ alone, as if gravity were not acting."], sort=True),
    Q("2.5 Connected blocks", r"Two blocks on a frictionless floor are joined by a light string. A $10$ N horizontal force pulls the $3.0$ kg front block, and the string pulls the $2.0$ kg block behind it. What is the tension in the string?",
      r"$4.0$ N", [r"$10$ N", r"$6.0$ N", r"$5.0$ N"],
      r"Both blocks accelerate at $10/5.0 = 2.0\ \mathrm{m/s^2}$; the string alone accelerates the rear block: $T = 2.0 \times 2.0 = 4.0$ N.",
      [r"System of both blocks: $a = 10/(3.0 + 2.0) = 2.0\ \mathrm{m/s^2}$.", r"Rear block alone: $T = m a = 4.0$ N."],
      [r"is the applied force; the string accelerates only the rear block.",
       r"uses the front block's mass: that is the net force on the front block.",
       r"splits the force evenly, ignoring the masses."], sort=True),
])

S4 = Sec("Gravitational force (2.6)", ["2.6"], r"""
Any two masses attract with
\[ F_g = \frac{G m_1 m_2}{r^2}, \qquad G = 6.67 \times 10^{-11}\ \mathrm{N\,m^2/kg^2}, \]
where $r$ is the distance between their centers. The \textbf{gravitational field} at a distance $r$ from a planet of mass $M$ is $g = GM/r^2$, the force per kilogram; at Earth's surface it is $9.8$ N/kg, which is the same thing as $9.8\ \mathrm{m/s^2}$.

\begin{terms}
Inverse square & doubling the distance between centers divides the force by 4 \\
Surface gravity & $g \propto M/R^2$: twice the mass and twice the radius gives half of $g$ \\
Weightlessness & an astronaut in orbit has weight (gravity there is about 90\% of its surface value) but feels weightless because she and her craft are in free fall together \\
Equivalence & gravitational mass and inertial mass are the same, which is why every object falls with the same $g$ \\
\end{terms}
""", checks=[
    Q("2.6 Inverse square", r"A satellite is moved from Earth's surface to an altitude equal to Earth's radius. By what factor does the gravitational force on it change?",
      r"It becomes $\tfrac14$ as large.", [r"It becomes $\tfrac12$ as large.", r"It does not change.", r"It becomes zero."],
      r"The distance from Earth's center doubles (from $R$ to $2R$), so the force falls by $2^2 = 4$.",
      [r"$F \propto 1/r^2$ and $r$ is measured from the center: $R \to 2R$."],
      [r"treats the force as inversely proportional to $r$, not $r^2$.",
       r"gravity weakens with distance.",
       r"gravity reaches arbitrarily far; it is never exactly zero."]),
])

S5 = Sec("Friction (2.7)", ["2.7"], r"""
Friction acts along the contact surface, opposing the relative motion (kinetic) or the tendency to move (static).
\[ F_{f,k} = \mu_k F_N, \qquad F_{f,s} \le \mu_s F_N . \]
Static friction is only as large as needed to prevent slipping, up to its maximum $\mu_s F_N$. For most surfaces $\mu_k < \mu_s$, and to a good approximation neither depends on the contact area or the speed.

\begin{example}
A $5.0$ kg crate rests on a floor with $\mu_s = 0.40$ and $\mu_k = 0.30$. The largest static friction is $0.40(49) = 19.6$ N. Push with $15$ N and static friction is exactly $15$ N: the crate stays put. Push with $25$ N and it slides; kinetic friction is then $0.30(49) = 14.7$ N and the net force is $10.3$ N.
\end{example}

\begin{trap}
$F_N$ is not always $mg$. On an incline $F_N = mg\cos\theta$; with a downward push or an upward pull at an angle, it changes again. Find it from the perpendicular axis first.
\end{trap}
""", checks=[
    Q("2.7 Static friction", r"A $5.0$ kg crate rests on a level floor ($\mu_s = 0.40$, $\mu_k = 0.30$). A student pushes horizontally with $15$ N and the crate does not move. What is the friction force on the crate?",
      r"$15$ N", [r"$19.6$ N", r"$14.7$ N", r"$0$"],
      r"The crate is in equilibrium, so static friction balances the push: $15$ N, which is below the $19.6$ N maximum.",
      [r"Maximum static friction: $0.40 \times 49 = 19.6$ N.", r"Needed: $15$ N $<$ $19.6$ N, so friction is $15$ N."],
      [r"is the maximum possible static friction, reached only when the crate is about to slip.",
       r"is kinetic friction, which acts only once the crate slides.",
       r"the crate is pushed, so friction must act to keep it in equilibrium."], sort=True),
])

S6 = Sec("Spring forces (2.8)", ["2.8"], r"""
An ideal spring exerts a force proportional to its stretch or compression from its natural length:
\[ \vec F_s = -k\,\Delta\vec x . \]
The minus sign says the force points back toward the natural length (a restoring force). The \textbf{spring constant} $k$ (N/m) is the slope of a graph of force versus stretch.

\textbf{Combinations.} Two identical springs side by side (parallel) act like one spring of constant $2k$; end to end (series), like one of constant $k/2$.

\begin{example}
A spring stretches $0.050$ m under a $2.0$ N load, so $k = 40$ N/m. Hung with a $0.50$ kg mass, it stretches until $k\Delta x = mg$: $\Delta x = 4.9/40 = 0.12$ m.
\end{example}
""", checks=[
    Q("2.8 Hooke's law", r"A spring with $k = 40$ N/m hangs vertically. A $0.50$ kg mass is attached and lowered gently until it hangs at rest. How far is the spring stretched?",
      r"$0.12$ m", [r"$0.0125$ m", r"$20$ m", r"$8.2$ m"],
      r"At rest $k\Delta x = mg$: $\Delta x = (0.50)(9.8)/40 = 0.12$ m.",
      [r"Equilibrium: spring force up equals weight down.", r"$\Delta x = mg/k = 4.9/40 = 0.12$ m."],
      [r"uses the mass in place of the weight: $0.50/40$.",
       r"multiplies: $0.50 \times 40$.",
       r"divides $k$ by the weight: $40/4.9$."], sort=True),
])

S7 = Sec("Circular motion (2.9)", ["2.9"], r"""
An object moving in a circle of radius $r$ at constant speed $v$ is accelerating toward the center:
\[ a_c = \frac{v^2}{r}, \qquad \sum F_{\text{toward center}} = \frac{m v^2}{r}, \qquad v = \frac{2\pi r}{T}. \]
``Centripetal force'' is not a new force: it is whichever real forces (tension, friction, normal, gravity) point toward the center, added up.

\begin{compare}{Situation}{Forces toward the center}{Result}
Car on a flat curve & static friction & $v_{max} = \sqrt{\mu_s g r}$ \\
Top of a vertical loop & $F_N + mg$ & minimum speed $\sqrt{gr}$ when $F_N = 0$ \\
Top of a hill & $mg - F_N$ & $F_N < mg$: the car feels lighter \\
Circular orbit & gravity & $v = \sqrt{GM/r}$, independent of the satellite's mass \\
\end{compare}

\begin{trap}
No outward (``centrifugal'') force appears on a free-body diagram. The feeling of being thrown outward is your inertia: your body tends to continue in a straight line.
\end{trap}
""", checks=[
    Q("2.9 Flat curve", r"A car rounds a flat curve of radius $50$ m. The coefficient of static friction between tires and road is $0.60$. What is the greatest speed at which it can round the curve without skidding?",
      r"$17$ m/s", [r"$22$ m/s", r"$5.5$ m/s", r"$294$ m/s"],
      r"Friction supplies the centripetal force: $\mu_s mg = mv^2/r$, so $v = \sqrt{\mu_s g r} = \sqrt{294} = 17$ m/s.",
      [r"$\mu_s m g = m v^2/r$; the mass cancels.", r"$v = \sqrt{0.60 \times 9.8 \times 50} = 17$ m/s."],
      [r"leaves out $\mu_s$: $\sqrt{gr}$.",
       r"leaves out $g$: $\sqrt{\mu_s r}$.",
       r"forgets the square root."], sort=True),
    Q("2.9 Top of a loop", r"A roller-coaster car goes around the top of a vertical loop at the minimum speed that keeps it on the track. At that point, which forces act on the car?",
      r"gravity only", [r"gravity and an upward normal force", r"gravity and an outward centrifugal force", r"no forces, since it is momentarily weightless"],
      r"At the minimum speed the track just stops pushing: $F_N = 0$ and gravity alone supplies $mv^2/r$.",
      [r"Top of the loop: $F_N + mg = mv^2/r$.", r"Minimum speed: $F_N = 0$, so $v = \sqrt{gr}$."],
      [r"the track is above the car at the top, so a normal force would push down, and at minimum speed it is zero.",
       r"centrifugal force is not a real force on the car.",
       r"gravity still acts; ``weightless'' describes the feeling, not the absence of gravity."]),
])

QS = [
    Set("Systems, forces and the third law (2.1--2.3)", [
        Q("2.3 Horse and cart", r"A horse pulls a cart along a level road and the two speed up together. Compared with the force of the horse on the cart, the force of the cart on the horse is",
          r"equal in size and opposite in direction", [r"smaller, which is why the cart moves forward", r"zero once the cart is moving", r"equal in size and in the same direction"],
          r"The forces are a third-law pair. The cart speeds up because the horse's pull on it exceeds the friction on the cart; the horse speeds up because the ground pushes it forward harder than the cart pulls back.",
          [r"Third-law forces act on different objects, so they never cancel."],
          [r"the third law holds whatever the motion; the forces that decide each object's motion are the ones acting on it.",
           r"the cart pulls back whenever the rope is taut.",
           r"third-law forces point in opposite directions."]),
        Q("2.1 Center of mass", r"A uniform plank $3.0$ m long with a mass of $4.0$ kg has a $2.0$ kg block on its right end. How far from the left end is the center of mass of the plank and block?",
          r"$2.0$ m", [r"$1.5$ m", r"$2.25$ m", r"$3.0$ m"],
          r"$x_{cm} = (4.0 \times 1.5 + 2.0 \times 3.0)/6.0 = 2.0$ m.",
          [r"The plank's own center of mass is at its middle, $1.5$ m.", r"$x_{cm} = (6.0 + 6.0)/6.0 = 2.0$ m."],
          [r"is the plank's center of mass alone.",
           r"averages $1.5$ m and $3.0$ m without weighting by mass.",
           r"is the block's position."], sort=True),
        Q("2.1 Choosing a system", r"Two blocks joined by a string are pulled across a frictionless floor by a horizontal force $F$ applied to the front block. If the two blocks and the string are treated as one system, which forces belong on the system's free-body diagram?",
          r"$F$, the total weight and the total normal force", [r"$F$ and the string tension only", r"the string tension only", r"$F$, the weights, the normal forces and the string tension"],
          r"The string tension is internal to this system: its pulls on the two blocks cancel.",
          [r"Only external forces act on a system: the pull, Earth's gravity and the floor's push."],
          [r"tension is internal here, and the vertical forces are left out.",
           r"tension is internal and the external pull is missing.",
           r"includes the internal tension."]),
    ]),
    Set("Newton's second law with a pulley (2.4--2.5)", [
        Q("2.5 Connected objects", r"What is the magnitude of the acceleration of the blocks?",
          r"$2.5\ \mathrm{m/s^2}$", [r"$9.8\ \mathrm{m/s^2}$", r"$3.3\ \mathrm{m/s^2}$", r"$4.9\ \mathrm{m/s^2}$"],
          r"Treat both blocks as one system: the only unbalanced external force is the hanging block's weight. $a = mg/(M + m) = 9.8/4.0 = 2.45\ \mathrm{m/s^2}$.",
          [r"Net force on the system: $mg = 9.8$ N (tension is internal).", r"Total mass $4.0$ kg, so $a = 2.45\ \mathrm{m/s^2}$."],
          [r"is free fall; the string holds the hanging block back.",
           r"divides the hanging weight by the table block's mass alone.",
           r"uses the Atwood formula $(M - m)g/(M + m)$ for two hanging blocks."], sort=True),
        Q("2.5 Tension", r"What is the tension in the string while the blocks move?",
          r"$7.4$ N", [r"$9.8$ N", r"$2.5$ N", r"$29$ N"],
          r"The string alone accelerates the table block: $T = Ma = 3.0 \times 2.45 = 7.4$ N.",
          [r"Table block: $T = Ma$.", r"Check with the hanging block: $mg - T = ma$ gives $9.8 - 7.4 = 2.45$ N $= (1.0)(2.45)$."],
          [r"is the hanging block's weight; the tension equals it only if nothing accelerates.",
           r"is the net force on the hanging block, $mg - T$.",
           r"is the table block's weight."], sort=True),
        Q("2.5 Changing the hanging mass", r"If the hanging block's mass is doubled to $2.0$ kg, the acceleration of the blocks will",
          r"increase, but by less than a factor of 2", [r"double", r"stay the same", r"decrease"],
          r"$a = mg/(M + m)$: the numerator doubles but the total mass also grows, from $4.0$ to $5.0$ kg, so $a$ rises from $2.45$ to $3.9\ \mathrm{m/s^2}$.",
          [r"$a' = (2.0)(9.8)/5.0 = 3.9\ \mathrm{m/s^2}$, a factor of $1.6$."],
          [r"forgets that the added mass must also be accelerated.",
           r"the driving force doubles, so the acceleration must change.",
           r"more pull with only slightly more mass gives more acceleration."]),
        Q("2.5 Tension vs. weight", r"While the blocks accelerate, how does the tension in the string compare with the weight of the hanging block?",
          r"The tension is less than the hanging block's weight.", [r"The tension equals the hanging block's weight.", r"The tension is greater than the hanging block's weight.", r"The tension is zero."],
          r"The hanging block accelerates downward, so the downward force on it (its weight) must exceed the upward tension.",
          [r"Hanging block: $mg - T = ma > 0$, so $T < mg$."],
          [r"would give the hanging block zero net force, so it could not accelerate.",
           r"would make the hanging block accelerate upward.",
           r"the string must pull the table block, which accelerates."]),
    ], stim=r"A block of mass $M = 3.0$ kg on a horizontal, frictionless table is connected by a light string that passes over a light, frictionless pulley at the table's edge to a hanging block of mass $m = 1.0$ kg. The blocks are released from rest.",
        stim_title="Questions 4--7"),
    Set("Gravity and friction (2.6--2.7)", [
        Q("2.6 Surface gravity", r"Planet X has twice Earth's mass and twice Earth's radius. What is the gravitational field at its surface?",
          r"$4.9\ \mathrm{m/s^2}$", [r"$9.8\ \mathrm{m/s^2}$", r"$19.6\ \mathrm{m/s^2}$", r"$2.5\ \mathrm{m/s^2}$"],
          r"$g = GM/R^2$: doubling $M$ doubles $g$, doubling $R$ divides it by 4, so $g$ is half of Earth's.",
          [r"$g_X = g_E \times 2/2^2 = 9.8/2 = 4.9\ \mathrm{m/s^2}$."],
          [r"assumes the two changes cancel; the radius is squared.",
           r"doubles $g$ for the mass and ignores the radius.",
           r"divides by 4 for the radius and ignores the mass."], sort=True),
        Q("2.6 Distance", r"The distance between the centers of two asteroids triples. The gravitational force each exerts on the other becomes",
          r"$\tfrac19$ as large", [r"$\tfrac13$ as large", r"$\tfrac16$ as large", r"$9$ times as large"],
          r"$F \propto 1/r^2$; tripling $r$ divides $F$ by $3^2 = 9$.",
          [r"$F' = F/3^2$."],
          [r"treats the force as $\propto 1/r$.",
           r"is $1/(2 \times 3)$, a mistake with the exponent.",
           r"gravity weakens with distance."]),
        Q("2.7 Friction on an incline", r"A $2.0$ kg block rests without sliding on a rough ramp inclined at $30^\circ$. What is the static friction force on the block?",
          r"$9.8$ N up the ramp", [r"$17$ N up the ramp", r"$9.8$ N down the ramp", r"$20$ N up the ramp"],
          r"Along the ramp the block is in equilibrium, so friction balances the component of gravity down the slope: $mg\sin30^\circ = 9.8$ N, pointing up the slope.",
          [r"Component of weight down the slope: $(2.0)(9.8)(0.50) = 9.8$ N.", r"Friction must point up the slope to balance it."],
          [r"uses $\cos 30^\circ$, the perpendicular component, which the normal force balances.",
           r"friction opposes the tendency to slide down, so it points up the ramp.",
           r"is the whole weight."]),
        Q("2.7 Kinetic friction", r"A horizontal $50$ N force pushes a box across a floor at constant velocity. The coefficient of kinetic friction is $0.25$. What is the mass of the box?",
          r"$20$ kg", [r"$5.1$ kg", r"$13$ kg", r"$200$ kg"],
          r"Constant velocity: friction balances the push, $\mu_k mg = 50$ N, so $m = 50/(0.25 \times 9.8) = 20$ kg.",
          [r"$\sum F = 0$: $F_f = 50$ N.", r"$F_f = \mu_k mg$, so $m = 20.4$ kg."],
          [r"treats the friction force as the box's weight.",
           r"multiplies the push by $\mu_k$.",
           r"forgets $g$: $50/0.25 = 200$ is the weight in newtons."], sort=True),
    ]),
    Set("Springs and circular motion (2.8--2.9)", [
        Q("2.8 Spring constant from a graph", r"Students measure the force needed to stretch a spring by different amounts. The graph shows their results. What is the spring constant?",
          r"$40$ N/m", [r"$0.025$ N/m", r"$0.90$ N/m", r"$400$ N/m"],
          r"$k$ is the slope of the force--stretch graph: $8.0\ \mathrm{N}/0.20\ \mathrm{m} = 40$ N/m.",
          [r"Slope $= \Delta F/\Delta x = (8.0 - 0)/(0.20 - 0)$."],
          [r"inverts the slope: stretch per newton.",
           r"multiplies a force by a stretch.",
           r"reads the stretch as $0.015$ m instead of $0.15$ m."], sort=True, fig=SPRING),
        Q("2.9 Over a hill", r"A car drives over the top of a rounded hill of radius $40$ m at $15$ m/s. At the top, how does the normal force on the car compare with its weight?",
          r"It is less than the weight.", [r"It equals the weight.", r"It is greater than the weight.", r"It is zero."],
          r"Toward the center (down): $mg - F_N = mv^2/r$, and $v^2/r = 5.6\ \mathrm{m/s^2} > 0$, so $F_N = m(9.8 - 5.6)$, less than $mg$.",
          [r"The car accelerates downward, toward the hill's center, so the net force is downward."],
          [r"would mean zero net force, but the car moves in a circle.",
           r"is the bottom of a dip, where the net force points up.",
           r"would need $v^2/r = g$, a speed of $\sqrt{gr} = 20$ m/s."]),
        Q("2.9 Maximum speed on a curve", r"What is the maximum speed at which a car can round a flat curve of radius $80$ m if the coefficient of static friction is $0.50$?",
          r"$20$ m/s", [r"$28$ m/s", r"$6.3$ m/s", r"$14$ m/s"],
          r"$\mu_s mg = mv^2/r$ gives $v = \sqrt{\mu_s g r} = \sqrt{392} = 20$ m/s.",
          [r"Static friction provides the centripetal force; the mass cancels.", r"$v = \sqrt{0.50 \times 9.8 \times 80} = 19.8$ m/s."],
          [r"leaves out $\mu_s$.",
           r"leaves out $g$.",
           r"uses half the radius."], sort=True),
        Q("2.9 Orbits", r"A satellite moves in a circular orbit around Earth at constant speed. Which statement is correct?",
          r"It accelerates toward Earth's center while its speed stays constant.", [r"It is weightless because gravity is zero at its altitude.", r"The net force on it is zero.", r"It needs a forward force to keep it moving."],
          r"Gravity supplies the centripetal force; it is perpendicular to the velocity, so it changes the direction but not the speed.",
          [r"Circular motion at constant speed still has $a = v^2/r$ toward the center."],
          [r"gravity at orbital altitudes is still most of its surface value.",
           r"zero net force would give straight-line motion.",
           r"no force is needed along the motion; inertia keeps it moving."]),
    ]),
]

UNIT = Unit(2, "force-dynamics", "Force and Translational Dynamics", "18--23\\%", "2.1--2.9",
    abstract=r"""Unit 2 explains what changes motion. It covers systems and the center of mass, forces and free-body diagrams, Newton's three laws (with connected objects and apparent weight), universal gravitation, static and kinetic friction, ideal springs, and the forces that keep objects moving in circles. It is the largest unit on the exam, along with Unit 3. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6, S7], qsections=QS,
    frq=FRQ("Mathematical Routines", 10, r"""A block of mass $m$ is pulled up a rough ramp inclined at angle $\theta$ to the horizontal by a rope parallel to the ramp. The tension in the rope is $F_T$, and the block moves up the ramp at constant speed. The coefficient of kinetic friction between block and ramp is $\mu$.""", [
        Part("a", 2, r"Draw a free-body diagram of the block, showing and labeling each force as an arrow starting on a dot that represents the block.",
             r"1 pt: four forces with correct directions: weight $mg$ straight down, normal force perpendicular to the ramp surface, tension up the slope, friction down the slope. 1 pt: no extra forces (no ``$ma$'', no ``force of motion''), each labeled.",
             r"Friction drawn up the ramp; weight drawn perpendicular to the ramp."),
        Part("b", 3, r"Derive an expression for $\mu$ in terms of $F_T$, $m$, $\theta$ and physical constants as appropriate.",
             r"1 pt: perpendicular to the ramp, $F_N = mg\cos\theta$. 1 pt: along the ramp, $F_T - mg\sin\theta - \mu F_N = 0$ (constant speed). 1 pt: $\mu = \dfrac{F_T - mg\sin\theta}{mg\cos\theta}$.",
             r"Setting $F_N = mg$; giving friction the wrong sign."),
        Part("c", 2, r"The block has mass $4.0$ kg, the ramp is inclined at $30^\circ$, and the tension is $30$ N. Calculate $\mu$.",
             r"1 pt: substitution consistent with (b): $\mu = (30 - 4.0 \times 9.8 \times 0.50)/(4.0 \times 9.8 \times 0.866)$. 1 pt: $\mu = 10.4/33.9 = 0.31$.",
             r"Using $\sin$ and $\cos$ the wrong way round."),
        Part("d", 3, r"The rope breaks while the block is moving up the ramp. A student claims that, until it stops, the block slows down at a rate of less than $g\sin\theta$. Do you agree or disagree with the student? Justify your answer.",
             r"1 pt: disagree. 1 pt: while the block still moves up the ramp, both the component of gravity along the ramp and kinetic friction point down the ramp. 1 pt: so $a = g\sin\theta + \mu g\cos\theta = 4.9 + 2.6 = 7.5\ \mathrm{m/s^2}$, greater than $g\sin\theta = 4.9\ \mathrm{m/s^2}$.",
             r"Thinking friction helps the block keep moving, or forgetting friction once the rope is gone."),
    ], mins=22),
    frq_topic="a block pulled up a rough ramp",
)
