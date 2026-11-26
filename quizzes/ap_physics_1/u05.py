from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Rotational kinematics (5.1)", ["5.1"], r"""
A rigid object rotating about a fixed axis is described by angles. Angular position $\theta$ is in radians ($2\pi$ rad $= 360^\circ = 1$ revolution); angular velocity $\omega = \Delta\theta/\Delta t$ (rad/s); angular acceleration $\alpha = \Delta\omega/\Delta t$ (rad/s$^2$). The sign convention is counterclockwise positive.

\begin{keyidea}[Constant angular acceleration]
\vspace{-6pt}
\[ \omega = \omega_0 + \alpha t, \qquad \theta = \theta_0 + \omega_0 t + \tfrac12\alpha t^2, \qquad \omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0). \]
These are the linear equations with $x \to \theta$, $v \to \omega$, $a \to \alpha$. Graphs work the same way: the slope of $\omega$ versus $t$ is $\alpha$, and the area under it is $\Delta\theta$.
\end{keyidea}

\begin{example}
A wheel speeds up uniformly from rest to $12$ rad/s in $4.0$ s: $\alpha = 3.0\ \mathrm{rad/s^2}$ and $\Delta\theta = \tfrac12(3.0)(4.0)^2 = 24$ rad, just under 4 revolutions.
\end{example}
""", checks=[
    Q("5.1 Angular displacement", r"A wheel speeds up uniformly from rest to $12$ rad/s in $4.0$ s. Through what angle does it turn in that time?",
      r"$24$ rad", [r"$48$ rad", r"$3.0$ rad", r"$12$ rad"],
      r"Average angular velocity $6.0$ rad/s for $4.0$ s: $\Delta\theta = 24$ rad.",
      [r"$\alpha = 12/4.0 = 3.0\ \mathrm{rad/s^2}$.", r"$\Delta\theta = \tfrac12\alpha t^2 = \tfrac12(3.0)(16) = 24$ rad."],
      [r"uses the final angular velocity for the whole time.",
       r"is the angular acceleration in $\mathrm{rad/s^2}$.",
       r"is the final angular velocity, not an angle."], sort=True),
])

S2 = Sec("Connecting linear and rotational motion (5.2)", ["5.2"], r"""
Every point of a rigid rotating object has the same $\theta$, $\omega$ and $\alpha$. A point at distance $r$ from the axis moves along an arc with
\[ s = r\theta, \qquad v = r\omega, \qquad a_t = r\alpha , \]
with angles in radians. Points farther from the axis move faster. A point moving in a circle also has the centripetal acceleration $a_c = v^2/r = \omega^2 r$ toward the axis.
""", checks=[
    Q("5.2 Same omega, different v", r"Two children ride a merry-go-round turning at a constant rate. Child $A$ sits $1.0$ m from the center and child $B$ sits $2.0$ m from the center. Which is correct?",
      r"They have the same angular velocity, and $B$'s speed is twice $A$'s.", [r"$B$ has twice $A$'s angular velocity and the same speed.", r"They have the same speed, and $A$'s angular velocity is twice $B$'s.", r"They have the same angular velocity and the same speed."],
      r"A rigid object turns as a whole, so $\omega$ is the same; $v = r\omega$ doubles with $r$.",
      [r"$v_B/v_A = r_B/r_A = 2$."],
      [r"every point of a rigid object has the same angular velocity.",
       r"reverses the roles of speed and angular velocity.",
       r"$B$ travels a larger circle in the same time."]),
])

S3 = Sec("Torque (5.3)", ["5.3"], r"""
A \textbf{torque} is the rotational effect of a force about an axis:
\[ \tau = r_\perp F = rF\sin\theta , \]
where $r$ is the distance from the axis to the point where the force acts and $\theta$ is the angle between $\vec r$ and $\vec F$. The \textbf{lever arm} $r_\perp$ is the perpendicular distance from the axis to the force's line of action. Counterclockwise torques are positive.

\begin{terms}
Largest torque & force perpendicular to the line from the axis, applied as far from the axis as possible \\
Zero torque & force along a line through the axis ($\theta = 0$), or applied at the axis \\
Gravity & acts at the center of mass of an extended object, so a uniform beam's weight acts at its middle \\
\end{terms}
""", checks=[
    Q("5.3 Torque at an angle", r"A student pulls on the end of a $0.25$ m wrench with a $40$ N force at $30^\circ$ to the handle. What torque does the force exert about the bolt?",
      r"$5.0\ \mathrm{N\,m}$", [r"$10\ \mathrm{N\,m}$", r"$8.7\ \mathrm{N\,m}$", r"$160\ \mathrm{N\,m}$"],
      r"$\tau = rF\sin\theta = (0.25)(40)(0.50) = 5.0\ \mathrm{N\,m}$.",
      [r"$\theta$ is the angle between the handle (the line from the axis) and the force."],
      [r"assumes the force is perpendicular to the handle.",
       r"uses $\cos30^\circ$, the component along the handle, which exerts no torque.",
       r"divides the force by the distance."], sort=True),
])

S4 = Sec("Rotational inertia (5.4)", ["5.4"], r"""
\textbf{Rotational inertia} $I$ measures how hard it is to change an object's rotation. It depends on the mass and on how far that mass is from the axis:
\[ I = \sum m_i r_i^2 \quad \text{(point masses)}, \qquad I' = I_{cm} + Md^2 \quad \text{(parallel-axis theorem)}. \]

\begin{compare}{Object (mass $M$, radius $R$)}{$I$ about the central axis}{Why}
Thin hoop & $MR^2$ & all the mass at distance $R$ \\
Solid disk or cylinder & $\tfrac12 MR^2$ & much of the mass close to the axis \\
Point mass on a light rod & $mr^2$ & \\
\end{compare}

The same object has different rotational inertias about different axes. Two $2.0$ kg masses at the ends of a light $1.0$ m rod have $I = 2(2.0)(0.50)^2 = 1.0\ \mathrm{kg\,m^2}$ about the center, but $2.0(1.0)^2 = 2.0\ \mathrm{kg\,m^2}$ about one end.
""", checks=[
    Q("5.4 Axis matters", r"Two $2.0$ kg masses are fixed to the ends of a light rod $1.0$ m long. What is the rotational inertia about an axis through one end, perpendicular to the rod?",
      r"$2.0\ \mathrm{kg\,m^2}$", [r"$1.0\ \mathrm{kg\,m^2}$", r"$4.0\ \mathrm{kg\,m^2}$", r"$0.50\ \mathrm{kg\,m^2}$"],
      r"The mass on the axis contributes nothing; the other is $1.0$ m away: $I = (2.0)(1.0)^2 = 2.0\ \mathrm{kg\,m^2}$.",
      [r"$I = \sum mr^2 = 2.0(0)^2 + 2.0(1.0)^2$."],
      [r"is the rotational inertia about the center of the rod.",
       r"counts both masses at $1.0$ m.",
       r"is one mass at the center-axis distance."], sort=True),
])

S5 = Sec("Rotational equilibrium (5.5)", ["5.5"], r"""
An object is in \textbf{rotational equilibrium} when the net torque on it is zero; its angular velocity is then constant (possibly zero). A rigid object at rest needs both
\[ \sum F = 0 \quad\text{and}\quad \sum \tau = 0 \text{ about any axis}. \]

\begin{keyidea}[Choosing the axis]
Take torques about the point where an unknown force acts: that force then has zero lever arm and drops out. A beam held by a hinge and a cable is quickest solved with torques about the hinge.
\end{keyidea}

\begin{example}
A $30$ kg child sits $2.0$ m from the pivot of a seesaw. A $40$ kg child balances her by sitting at $d$ on the other side: $40d = 30(2.0)$, so $d = 1.5$ m. The heavier child sits closer.
\end{example}
""", checks=[
    Q("5.5 Seesaw", r"A $30$ kg child sits $2.0$ m from the pivot of a uniform seesaw that is balanced at its center. Where must a $40$ kg child sit on the other side to balance it?",
      r"$1.5$ m from the pivot", [r"$2.7$ m from the pivot", r"$2.0$ m from the pivot", r"$1.0$ m from the pivot"],
      r"Equal and opposite torques: $40g\,d = 30g(2.0)$, so $d = 1.5$ m.",
      [r"The seesaw's own weight acts at the pivot and exerts no torque."],
      [r"inverts the mass ratio, placing the heavier child farther out.",
       r"equal distances balance only equal weights.",
       r"halves the distance without using the masses."]),
])

S6 = Sec("Newton's second law in rotational form (5.6)", ["5.6"], r"""
A net torque produces angular acceleration:
\[ \alpha = \frac{\sum\tau}{I}. \]
For a string wrapped around a pulley of radius $R$, the string's tension exerts torque $TR$. If the pulley has mass, the tensions on its two sides differ: the difference is what turns it. A hanging block that unwinds a string from a massive pulley accelerates at less than $g$, and the tension is less than the block's weight.
""", checks=[
    Q("5.6 Angular acceleration", r"A net torque of $2.0\ \mathrm{N\,m}$ acts on a wheel whose rotational inertia is $0.50\ \mathrm{kg\,m^2}$. What is its angular acceleration?",
      r"$4.0\ \mathrm{rad/s^2}$", [r"$1.0\ \mathrm{rad/s^2}$", r"$0.25\ \mathrm{rad/s^2}$", r"$2.5\ \mathrm{rad/s^2}$"],
      r"$\alpha = \tau/I = 2.0/0.50 = 4.0\ \mathrm{rad/s^2}$.",
      [r"$\sum\tau = I\alpha$."],
      [r"multiplies torque and rotational inertia.",
       r"divides the rotational inertia by the torque.",
       r"adds the two numbers."], sort=True),
])

QS = [
    Set("Rotational kinematics (5.1--5.2)", [
        Q("5.1 Slowing fan", r"A fan's blades slow uniformly from $30$ rad/s to rest in $6.0$ s. Through what angle do they turn while slowing?",
          r"$90$ rad", [r"$180$ rad", r"$5.0$ rad", r"$45$ rad"],
          r"Average angular velocity $15$ rad/s for $6.0$ s gives $90$ rad.",
          [r"$\Delta\theta = \tfrac12(\omega_0 + \omega)t = \tfrac12(30 + 0)(6.0) = 90$ rad."],
          [r"uses the initial angular velocity for the whole time.",
           r"is the magnitude of the angular acceleration.",
           r"halves the answer twice."], sort=True),
        Q("5.1 Units", r"A turntable rotates at $33$ revolutions per minute. What is its angular velocity in rad/s?",
          r"$3.5$ rad/s", [r"$0.55$ rad/s", r"$33$ rad/s", r"$207$ rad/s"],
          r"$33\ \mathrm{rev/min} \times 2\pi\ \mathrm{rad/rev} \div 60\ \mathrm{s/min} = 3.5$ rad/s.",
          [r"$33/60 = 0.55$ rev/s; $\times 2\pi = 3.46$ rad/s."],
          [r"is revolutions per second, not radians per second.",
           r"is the original number in rev/min.",
           r"is radians per minute."], sort=True),
        Q("5.2 Tangential acceleration", r"A wheel of radius $0.30$ m has an angular acceleration of $4.0\ \mathrm{rad/s^2}$. What is the tangential acceleration of a point on its rim?",
          r"$1.2\ \mathrm{m/s^2}$", [r"$13\ \mathrm{m/s^2}$", r"$4.0\ \mathrm{m/s^2}$", r"$0.075\ \mathrm{m/s^2}$"],
          r"$a_t = r\alpha = 0.30 \times 4.0 = 1.2\ \mathrm{m/s^2}$.",
          [r"Linear quantity $=$ radius $\times$ angular quantity."],
          [r"divides by the radius instead of multiplying.",
           r"ignores the radius.",
           r"divides the radius by $\alpha$."], sort=True),
        Q("5.2 Speed on a disk", r"A disk spins at a constant rate. Point $P$ is halfway between the center and the rim, and point $Q$ is on the rim. Compared with $Q$, point $P$ has",
          r"the same angular velocity and half the linear speed", [r"half the angular velocity and half the linear speed", r"the same angular velocity and the same linear speed", r"twice the angular velocity and the same linear speed"],
          r"All points share $\omega$; $v = r\omega$ is proportional to the distance from the axis.",
          [r"$r_P = \tfrac12 r_Q$, so $v_P = \tfrac12 v_Q$."],
          [r"the angular velocity is the same everywhere on a rigid disk.",
           r"$P$ moves on a smaller circle in the same time.",
           r"a rigid disk turns as one piece."]),
    ]),
    Set("A beam in equilibrium (5.3, 5.5)", [
        Q("5.3 Torque of a weight", r"What is the magnitude of the torque exerted by the beam's weight about the hinge?",
          r"$196\ \mathrm{N\,m}$", [r"$392\ \mathrm{N\,m}$", r"$98\ \mathrm{N\,m}$", r"$49\ \mathrm{N\,m}$"],
          r"The beam's weight, $98$ N, acts at its center, $2.0$ m from the hinge: $\tau = 98 \times 2.0 = 196\ \mathrm{N\,m}$.",
          [r"Uniform beam: the weight acts at the midpoint."],
          [r"places the weight at the far end.",
           r"leaves out the lever arm.",
           r"uses a $0.50$ m lever arm."], sort=True),
        Q("5.5 Cable tension", r"What is the tension in the cable?",
          r"$98$ N", [r"$294$ N", r"$147$ N", r"$392$ N"],
          r"Torques about the hinge: $T(4.0) = 98(2.0) + 196(1.0) = 392\ \mathrm{N\,m}$, so $T = 98$ N.",
          [r"Box: $196$ N at $1.0$ m. Beam: $98$ N at $2.0$ m.", r"Cable at $4.0$ m: $T = 392/4.0 = 98$ N."],
          [r"is the total weight, as if the cable carried everything.",
           r"splits the total weight evenly between hinge and cable.",
           r"is the total torque; it must still be divided by the $4.0$ m lever arm."], sort=True),
        Q("5.5 Hinge force", r"What is the magnitude of the vertical force the hinge exerts on the beam?",
          r"$196$ N", [r"$98$ N", r"$294$ N", r"$0$"],
          r"Vertical forces balance: $F_{hinge} + 98 = 98 + 196$, so $F_{hinge} = 196$ N upward.",
          [r"$\sum F_y = 0$: hinge $+$ cable $=$ beam $+$ box."],
          [r"is the cable tension.",
           r"is the total weight, which hinge and cable share.",
           r"the box is closer to the hinge, so the hinge carries most of the load."], sort=True),
        Q("5.5 Moving the load", r"The box is slid toward the cable end of the beam. As it moves, the cable tension",
          r"increases, and the hinge force decreases", [r"decreases, and the hinge force increases", r"stays the same, and so does the hinge force", r"increases, and so does the hinge force"],
          r"The box's torque about the hinge grows with its distance, so the cable must pull harder; the two supports always share the same total weight.",
          [r"$T = (98 \times 2.0 + 196x)/4.0$ grows with $x$.", r"$F_{hinge} = 294 - T$ falls."],
          [r"reverses the effect of moving the load.",
           r"the box's lever arm about the hinge changes.",
           r"the two forces add to the fixed total weight, so both cannot grow."]),
    ], stim=r"A uniform beam $4.0$ m long with a mass of $10$ kg is attached to a wall by a hinge at its left end and held horizontal by a vertical cable attached to its right end. A $20$ kg box sits on the beam $1.0$ m from the hinge.",
        stim_title="Questions 5--8"),
    Set("Rotational inertia and dynamics (5.4--5.6)", [
        Q("5.4 Hoop vs. disk", r"A thin hoop and a solid disk have the same mass and radius. Which has the greater rotational inertia about its central axis, and why?",
          r"the hoop, because its mass is all at the greatest distance from the axis", [r"the disk, because it has more material near the axis", r"they are equal, because they have the same mass and radius", r"the disk, because it is solid"],
          r"$I = \sum mr^2$ weights each bit of mass by its distance squared; all the hoop's mass is at $R$.",
          [r"Hoop: $MR^2$. Disk: $\tfrac12 MR^2$."],
          [r"mass near the axis contributes little.",
           r"rotational inertia depends on how the mass is distributed.",
           r"being solid puts mass close to the axis, lowering $I$."]),
        Q("5.4 Changing the axis", r"Two $1.0$ kg masses are fixed to the ends of a light rod $2.0$ m long. What is the rotational inertia about an axis through one end, perpendicular to the rod?",
          r"$4.0\ \mathrm{kg\,m^2}$", [r"$2.0\ \mathrm{kg\,m^2}$", r"$8.0\ \mathrm{kg\,m^2}$", r"$1.0\ \mathrm{kg\,m^2}$"],
          r"One mass is on the axis; the other is $2.0$ m away: $I = (1.0)(2.0)^2 = 4.0\ \mathrm{kg\,m^2}$.",
          [r"Check with the parallel-axis theorem: $I_{cm} = 2(1.0)(1.0)^2 = 2.0$, and $I = 2.0 + (2.0)(1.0)^2 = 4.0\ \mathrm{kg\,m^2}$."],
          [r"is the rotational inertia about the center.",
           r"counts both masses at $2.0$ m.",
           r"is one mass at $1.0$ m."], sort=True),
        Q("5.6 Pulley", r"A string wrapped around a solid disk pulley ($M = 2.0$ kg, $R = 0.10$ m, $I = \tfrac12 MR^2$) is pulled with a constant $4.0$ N force. The pulley turns on a frictionless axle. What is its angular acceleration?",
          r"$40\ \mathrm{rad/s^2}$", [r"$20\ \mathrm{rad/s^2}$", r"$400\ \mathrm{rad/s^2}$", r"$2.0\ \mathrm{rad/s^2}$"],
          r"$\tau = FR = 0.40\ \mathrm{N\,m}$ and $I = \tfrac12(2.0)(0.10)^2 = 0.010\ \mathrm{kg\,m^2}$, so $\alpha = 40\ \mathrm{rad/s^2}$.",
          [r"$\alpha = \tau/I = 0.40/0.010$."],
          [r"uses $I = MR^2$, as for a hoop.",
           r"uses the force in place of the torque.",
           r"is $F/M$, a linear acceleration, not an angular one."], sort=True),
        Q("5.6 Where to push", r"A student pushes a door perpendicular to its surface with the same force, first at the handle, $0.80$ m from the hinges, and then at a point $0.40$ m from the hinges. How do the door's angular accelerations compare?",
          r"It is twice as large when pushed at the handle.", [r"It is four times as large when pushed at the handle.", r"It is the same, because the force is the same.", r"It is twice as large when pushed closer to the hinges."],
          r"$\alpha = \tau/I$ and $\tau = rF$; doubling $r$ doubles the torque, and $I$ (about the hinges) is unchanged.",
          [r"$\alpha_{handle}/\alpha_{near} = 0.80/0.40 = 2$."],
          [r"torque is proportional to $r$, not $r^2$.",
           r"the same force at a different distance gives a different torque.",
           r"reverses the effect of the lever arm."]),
        Q("5.5 Conditions", r"A rigid object is in rotational equilibrium. Which must be true?",
          r"The net torque on it is zero.", [r"It is not rotating.", r"The net force on it is zero.", r"All the forces on it act through one point."],
          r"Rotational equilibrium means zero net torque, so constant angular velocity; the object may still spin steadily.",
          [r"$\sum\tau = 0 \Rightarrow \alpha = 0$, so $\omega$ is constant, not necessarily zero."],
          [r"it may rotate at a constant angular velocity.",
           r"that is translational equilibrium, a separate condition.",
           r"forces may act at different points as long as their torques cancel."]),
    ]),
]

UNIT = Unit(5, "torque-rotational-dynamics", "Torque and Rotational Dynamics", "10--15\\%", "5.1--5.6",
    abstract=r"""Unit 5 carries the ideas of Units 1 and 2 over to rotation about a fixed axis: angular position, velocity and acceleration and their link to linear motion, torque and lever arms, rotational inertia (including the parallel-axis theorem), rotational equilibrium of extended objects, and Newton's second law in rotational form. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Translation Between Representations", 12, r"""A uniform board of length $L$ and mass $M$ lies horizontally on two supports: support $A$ at the board's left end and support $B$ a distance $L/4$ from its right end. A student of mass $m$ stands on the board a distance $x$ from the left end. The board does not tip.""", [
        Part("a", 3, r"Draw a force diagram of the board, representing it as a horizontal line. Draw each force as an arrow starting at the point where it acts on the board, and label each force.",
             r"1 pt: the board's weight $Mg$ downward at the center, $L/2$ from the left end. 1 pt: the student's downward push $mg$ at $x$. 1 pt: two upward support forces, $F_A$ at the left end and $F_B$ at $3L/4$.",
             r"Drawing all forces from the center, or putting the student's weight at the center."),
        Part("b", 3, r"Derive an expression for the force $F_B$ exerted by support $B$, in terms of $M$, $m$, $x$, $L$ and physical constants as appropriate.",
             r"1 pt: torques about $A$ (so $F_A$ drops out): $F_B\left(\tfrac{3L}{4}\right) - Mg\left(\tfrac{L}{2}\right) - mgx = 0$. 1 pt: correct lever arms for all three forces. 1 pt: $F_B = \dfrac{2Mg}{3} + \dfrac{4mgx}{3L}$.",
             r"Using $L$ instead of $3L/4$ for the lever arm of $F_B$."),
        Part("c", 3, r"On the same axes, sketch graphs of $F_A$ and $F_B$ as functions of $x$ from $x = 0$ to $x = L$. Label each graph.",
             r"1 pt: $F_B$ is a straight line rising from $2Mg/3$ at $x = 0$. 1 pt: $F_A$ is a straight line falling from $Mg/3 + mg$ at $x = 0$. 1 pt: the two lines have equal and opposite slopes, so $F_A + F_B = (M + m)g$ at every $x$.",
             r"Curved graphs, or $F_A$ increasing."),
        Part("d", 3, r"The student says she can walk all the way to the right end of the board without it tipping, as long as her mass is less than the board's. Do you agree or disagree? Justify your answer using your graph or your expression from part (b).",
             r"1 pt: agree. 1 pt: the board tips only if $F_A$ would have to become negative (support $A$ can only push); from (b), $F_A = (M + m)g - F_B$, which at $x = L$ is $(M - m)g/3$. 1 pt: this is positive when $m < M$, so $F_A$ stays positive all the way to the end and the board does not tip.",
             r"Arguing from where the student is relative to the center rather than relative to support $B$."),
    ], mins=28),
    frq_topic="a student walking along a board on two supports",
)
