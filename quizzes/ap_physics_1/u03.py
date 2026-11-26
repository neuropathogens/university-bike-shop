from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

FX1 = Graph(r"Position $x$ (m)", r"Force $F$ (N)", x=(0, 5, 1), y=(0, 12, 2),
            series=[Series("force", [(0, 0), (2, 10), (5, 10)], marks=False)])
FX2 = Graph(r"Position $x$ (m)", r"Net force $F$ (N)", x=(0, 6, 1), y=(0, 10, 2),
            series=[Series("force", [(0, 0), (2, 8), (4, 8), (6, 0)], marks=False)])

S1 = Sec("Translational kinetic energy (3.1)", ["3.1"], r"""
An object of mass $m$ moving at speed $v$ has kinetic energy
\[ K = \tfrac12 m v^2 . \]
Kinetic energy is a scalar and never negative; it depends on the speed, not the direction, and its value depends on the reference frame. Because $K \propto v^2$, doubling the speed quadruples the kinetic energy (and, at a given braking force, the stopping distance).
""", checks=[
    Q("3.1 Kinetic energy", r"A $1200$ kg car moving at $20$ m/s speeds up to $40$ m/s. By what factor does its kinetic energy increase?",
      r"$4$", [r"$2$", r"$8$", r"$16$"],
      r"$K \propto v^2$: doubling $v$ multiplies $K$ by $2^2 = 4$ (from $240$ kJ to $960$ kJ).",
      [r"$K_1 = \tfrac12(1200)(20)^2 = 2.4 \times 10^5$ J; $K_2 = \tfrac12(1200)(40)^2 = 9.6 \times 10^5$ J."],
      [r"treats $K$ as proportional to $v$, like momentum.",
       r"cubes the factor.",
       r"raises the factor to the fourth power."], sort=True),
])

S2 = Sec("Work (3.2)", ["3.2"], r"""
A force does \textbf{work} on an object when the object moves with a component of its displacement along the force:
\[ W = F_\parallel d = F d\cos\theta , \]
where $\theta$ is the angle between the force and the displacement. Work is a scalar measured in joules ($1\ \mathrm{J} = 1\ \mathrm{N\,m}$).

\begin{terms}
Positive work & force has a component along the motion: it adds energy (a push in the direction of travel) \\
Negative work & force has a component against the motion: it removes energy (kinetic friction, braking) \\
Zero work & force perpendicular to the motion (the normal force on a sliding block, the tension in a circular swing, gravity on an orbiting satellite), or no displacement \\
Varying force & work is the area under a graph of $F_\parallel$ versus position \\
\end{terms}

\begin{keyidea}[Work--energy theorem]
The net work done on an object equals its change in kinetic energy: $W_{net} = \Delta K$. Use it whenever forces and distances are given and speeds are wanted, or the reverse.
\end{keyidea}
""", checks=[
    Q("3.2 Work at an angle", r"A student pulls a sled $10$ m across level snow with a rope at $37^\circ$ above the horizontal. The tension is $50$ N ($\cos37^\circ = 0.80$). How much work does the tension do?",
      r"$400$ J", [r"$500$ J", r"$300$ J", r"$40$ J"],
      r"Only the component of the force along the motion does work: $W = (50)(0.80)(10) = 400$ J.",
      [r"$F_\parallel = 50\cos37^\circ = 40$ N.", r"$W = 40 \times 10 = 400$ J."],
      [r"uses the whole force, ignoring the angle.",
       r"uses $\sin 37^\circ = 0.60$, the vertical component, which does no work here.",
       r"is the horizontal component of the force, not the work."], sort=True),
    Q("3.2 Area under F-x", r"The graph shows the force on a crate, in the direction of its motion, as a function of position. How much work does the force do from $x = 0$ to $x = 5$ m?",
      r"$40$ J", [r"$50$ J", r"$30$ J", r"$10$ J"],
      r"Work is the area under the force--position graph: a triangle ($\tfrac12 \times 2 \times 10 = 10$ J) plus a rectangle ($3 \times 10 = 30$ J).",
      [r"$0$--$2$ m: $10$ J. $2$--$5$ m: $30$ J. Total $40$ J."],
      [r"uses the maximum force for the whole $5$ m.",
       r"leaves out the first $2$ m.",
       r"counts only the first $2$ m."], sort=True, fig=FX1),
])

S3 = Sec("Potential energy (3.3)", ["3.3"], r"""
\textbf{Potential energy belongs to a system}, not to one object: it is stored in the arrangement of objects that interact through conservative forces (gravity, springs). Where you set $U = 0$ is your choice; only changes in $U$ matter.

\begin{terms}
Object and Earth, near the surface & $\Delta U_g = mg\Delta y$ \\
Two spherical masses (planets, moons, stars) & $U_G = -\dfrac{G m_1 m_2}{r}$, zero at infinite separation and negative closer in \\
Ideal spring & $U_s = \tfrac12 k(\Delta x)^2$, the same for stretch and compression \\
More than two objects & add the potential energy of every pair \\
\end{terms}

\begin{trap}
If Earth is \emph{not} part of your system, there is no gravitational potential energy: gravity is an external force that does work on the system instead. Count it one way or the other, never both.
\end{trap}
""", checks=[
    Q("3.3 Spring potential energy", r"A spring with $k = 200$ N/m is compressed $0.10$ m from its natural length. How much elastic potential energy is stored?",
      r"$1.0$ J", [r"$2.0$ J", r"$20$ J", r"$10$ J"],
      r"$U_s = \tfrac12 k(\Delta x)^2 = \tfrac12(200)(0.10)^2 = 1.0$ J.",
      [r"$(0.10)^2 = 0.010\ \mathrm{m^2}$; $\tfrac12 \times 200 \times 0.010 = 1.0$ J."],
      [r"leaves out the $\tfrac12$.",
       r"is $k\Delta x$, the spring force in newtons.",
       r"is $\tfrac12 k\Delta x$ without squaring the compression."], sort=True),
])

S4 = Sec("Conservation of energy (3.4)", ["3.4"], r"""
The energy of a system changes only if external forces do work on it (or energy crosses the boundary by heating):
\[ \Delta E_{system} = W_{external}. \]
For a closed, isolated system with only conservative internal forces, mechanical energy is conserved: $K_i + U_i = K_f + U_f$. If kinetic friction acts inside the system, mechanical energy decreases and thermal energy increases by the same amount, $\Delta E_{th} = F_f d$.

\begin{keyidea}[Energy bar charts]
Draw a bar for each form of energy (kinetic, gravitational, elastic, thermal) at the start and end, plus a bar for work done by external forces. The totals must balance. Bar charts are the quickest way to plan an energy argument before writing equations.
\end{keyidea}

\begin{example}
A $20$ kg sled starts from rest at the top of a $5.0$ m high hill and reaches the bottom at $8.0$ m/s. The system (sled, hill, Earth) loses $mgh = 980$ J of gravitational energy and gains $\tfrac12 mv^2 = 640$ J of kinetic energy, so $340$ J became thermal energy through friction.
\end{example}
""", checks=[
    Q("3.4 Pendulum", r"A pendulum bob is pulled aside until it is $0.45$ m above its lowest point and released from rest. Air resistance is negligible. How fast is it moving at the lowest point?",
      r"$3.0$ m/s", [r"$8.8$ m/s", r"$2.1$ m/s", r"$4.4$ m/s"],
      r"$mgh = \tfrac12 mv^2$, so $v = \sqrt{2gh} = \sqrt{8.82} = 3.0$ m/s; the tension does no work.",
      [r"The string is always perpendicular to the motion, so only gravity changes the energy.", r"$v = \sqrt{2(9.8)(0.45)} = 2.97$ m/s."],
      [r"forgets the square root: $2gh = 8.8$.",
       r"leaves out the factor 2: $\sqrt{gh}$.",
       r"is $gh$, not a speed."], sort=True),
    Q("3.4 Thermal energy", r"A $20$ kg sled starts from rest at the top of a hill $5.0$ m high and reaches the bottom at $8.0$ m/s. How much mechanical energy was converted to thermal energy?",
      r"$340$ J", [r"$980$ J", r"$640$ J", r"$1620$ J"],
      r"Loss of gravitational energy minus gain of kinetic energy: $980 - 640 = 340$ J.",
      [r"$mgh = 20(9.8)(5.0) = 980$ J.", r"$\tfrac12 mv^2 = \tfrac12(20)(64) = 640$ J."],
      [r"is the whole loss of gravitational energy, as if the sled stopped at the bottom.",
       r"is the kinetic energy at the bottom.",
       r"adds the two energies instead of subtracting."], sort=True),
])

S5 = Sec("Power (3.5)", ["3.5"], r"""
Power is the rate at which energy is transferred or work is done:
\[ P = \frac{\Delta E}{\Delta t} = \frac{W}{\Delta t}, \qquad P = F_\parallel v \ \text{(instantaneous)}. \]
One watt is one joule per second. For an object moved at constant velocity against a force (lifting at constant speed, driving against drag), $P = Fv$ with $F$ equal to that opposing force.

\begin{trap}
Two climbers of equal mass who climb the same stairs do the same work against gravity. The faster climber has the greater power, not the greater work.
\end{trap}
""", checks=[
    Q("3.5 Lifting at constant speed", r"A motor lifts a $50$ kg crate straight up at a constant $2.0$ m/s. What power does the motor deliver to the crate?",
      r"$980$ W", [r"$100$ W", r"$250$ W", r"$490$ W"],
      r"At constant speed the motor's force equals the weight, $490$ N, so $P = Fv = 490 \times 2.0 = 980$ W.",
      [r"$F = mg = 490$ N.", r"$P = Fv = 980$ W."],
      [r"is the crate's kinetic energy in joules, $\tfrac12(50)(2.0)^2$, not a power.",
       r"divides the weight by the speed.",
       r"is the weight, not the power."], sort=True),
])

QS = [
    Set("Kinetic energy and work (3.1--3.2)", [
        Q("3.2 Work-energy theorem", r"The speed of a $0.15$ kg ball increases from $10$ m/s to $20$ m/s. How much net work was done on the ball?",
          r"$23$ J", [r"$7.5$ J", r"$30$ J", r"$1.5$ J"],
          r"$W_{net} = \Delta K = \tfrac12(0.15)(20^2 - 10^2) = 22.5$ J.",
          [r"$K_f = 30$ J, $K_i = 7.5$ J.", r"$W = 30 - 7.5 = 22.5 \approx 23$ J."],
          [r"is $\tfrac12 m(\Delta v)^2$; you must square each speed before subtracting.",
           r"is the final kinetic energy; it ignores the energy the ball already had.",
           r"is the change in momentum, $m\Delta v$, in kg$\,$m/s."], sort=True),
        Q("3.2 Sign of work", r"A box slides across a rough, level floor and comes to rest. Which force does negative work on the box while it slides?",
          r"kinetic friction", [r"the normal force", r"the gravitational force", r"no force; the box simply runs out of energy"],
          r"Friction points opposite the displacement, so $W = -F_f d$; it removes the box's kinetic energy.",
          [r"$W = Fd\cos180^\circ = -Fd$ for friction."],
          [r"is perpendicular to the motion, so it does no work.",
           r"is perpendicular to the horizontal motion, so it does no work.",
           r"energy is transferred by work; the box's kinetic energy goes into thermal energy through friction."]),
        Q("3.2 Zero work", r"A student carries a $10$ kg box at a constant height and constant speed $5.0$ m across a room. How much work does the student's upward force on the box do?",
          r"zero", [r"$490$ J", r"$50$ J", r"$-490$ J"],
          r"The student's force is vertical and the displacement is horizontal, so $\theta = 90^\circ$ and $W = 0$.",
          [r"$W = Fd\cos90^\circ = 0$; the box's energy does not change either."],
          [r"multiplies the weight by a horizontal distance.",
           r"multiplies the mass by the distance.",
           r"the force is not opposite the motion either."]),
        Q("3.2 Stopping force", r"A $2.0$ kg block moving at $6.0$ m/s slides to rest across a rough floor in $3.0$ m. What is the magnitude of the average friction force?",
          r"$12$ N", [r"$4.0$ N", r"$36$ N", r"$108$ N"],
          r"Friction removes all the kinetic energy: $F_f d = \tfrac12 mv^2 = 36$ J, so $F_f = 36/3.0 = 12$ N.",
          [r"$K_i = \tfrac12(2.0)(6.0)^2 = 36$ J.", r"$F_f = K_i/d = 12$ N."],
          [r"divides the momentum, $mv$, by the distance.",
           r"is the kinetic energy in joules, not a force.",
           r"multiplies the energy by the distance instead of dividing."], sort=True),
    ]),
    Set("A force--position graph (3.2)", [
        Q("3.2 Work from a graph", r"How much work does the net force do on the cart from $x = 0$ to $x = 6$ m?",
          r"$32$ J", [r"$48$ J", r"$16$ J", r"$24$ J"],
          r"Area under the graph: $8 + 16 + 8 = 32$ J.",
          [r"$0$--$2$ m: $\tfrac12(2)(8) = 8$ J. $2$--$4$ m: $2 \times 8 = 16$ J. $4$--$6$ m: $8$ J."],
          [r"uses the maximum force over all $6$ m.",
           r"counts only the rectangle.",
           r"stops at $x = 4$ m."], sort=True),
        Q("3.2 Speed from work", r"What is the cart's speed at $x = 6$ m?",
          r"$5.7$ m/s", [r"$4.0$ m/s", r"$11$ m/s", r"$16$ m/s"],
          r"$W_{net} = \Delta K$: $32 = \tfrac12(2.0)v^2$, so $v = \sqrt{32} = 5.7$ m/s.",
          [r"$K_f = 32$ J since $K_i = 0$.", r"$v = \sqrt{2K/m} = \sqrt{32} = 5.66$ m/s."],
          [r"leaves out the $\tfrac12$: $\sqrt{32/2}$.",
           r"multiplies by the mass inside the root instead of dividing.",
           r"is $W/m$ with no square root."], sort=True),
        Q("3.2 Greatest speed", r"Where is the cart moving fastest?",
          r"at $x = 6$ m", [r"at $x = 2$ m", r"at $x = 4$ m", r"everywhere between $x = 2$ m and $x = 4$ m"],
          r"The net force is never negative, so it does positive work all the way and the speed increases until $x = 6$ m.",
          [r"$K$ grows by the area under the graph so far, which grows until the end."],
          [r"is where the force first becomes largest; the cart keeps speeding up after that.",
           r"the force is still positive from $4$ to $6$ m, so the cart is still speeding up.",
           r"describes where the acceleration is greatest, not the speed."]),
        Q("3.2 Greatest acceleration", r"Where is the cart's acceleration greatest?",
          r"everywhere between $x = 2$ m and $x = 4$ m", [r"at $x = 6$ m", r"at $x = 0$", r"at $x = 1$ m"],
          r"$a = F/m$, so the acceleration is greatest where the force is greatest: $8$ N, giving $4.0\ \mathrm{m/s^2}$, from $2$ to $4$ m.",
          [r"Read the height of the graph, not the area."],
          [r"is where the speed is greatest; the force there is zero.",
           r"the force, and so the acceleration, is zero there.",
           r"the force is only $4$ N there."]),
    ], stim=r"A $2.0$ kg cart starts from rest at $x = 0$ on a level track. The graph shows the net horizontal force on the cart as a function of its position.",
        fig=FX2, stim_title="Questions 5--8"),
    Set("Potential energy and conservation (3.3--3.4)", [
        Q("3.3 Spring launcher", r"A spring with $k = 400$ N/m is compressed $0.10$ m and launches a $0.050$ kg ball straight up. Air resistance is negligible. How high above its release point does the ball rise?",
          r"$4.1$ m", [r"$8.2$ m", r"$40$ m", r"$82$ m"],
          r"$\tfrac12 k(\Delta x)^2 = mgh$: $2.0\ \mathrm{J} = (0.050)(9.8)h$, so $h = 4.1$ m.",
          [r"$U_s = \tfrac12(400)(0.10)^2 = 2.0$ J.", r"$h = 2.0/0.49 = 4.08$ m."],
          [r"leaves out the $\tfrac12$ in the spring energy.",
           r"forgets $g$: divides the energy by the mass only.",
           r"uses the spring force $k\Delta x = 40$ N as if it were an energy."], sort=True),
        Q("3.4 Choosing the system", r"A ball falls from rest. If the system is the ball alone (Earth is outside the system), what accounts for the increase in the system's kinetic energy?",
          r"positive work done on the ball by Earth's gravitational force", [r"a decrease in the system's gravitational potential energy", r"energy stored in the ball when it was lifted", r"nothing; energy is not conserved for this system"],
          r"With Earth outside, there is no potential energy in the system; gravity is an external force doing positive work.",
          [r"System = ball: $\Delta K = W_{gravity} = mgh$.", r"System = ball + Earth: $\Delta K = -\Delta U_g$, and no external work."],
          [r"a one-object system has no potential energy.",
           r"potential energy belongs to the ball--Earth system, which this system is not.",
           r"energy is conserved; the external work is the transfer into the system."]),
        Q("3.4 Frictionless track", r"A cart starts from rest at a height of $20$ m on a frictionless roller-coaster track. What is its speed when it is $5.0$ m above the ground?",
          r"$17$ m/s", [r"$9.9$ m/s", r"$20$ m/s", r"$22$ m/s"],
          r"It has dropped $15$ m: $v = \sqrt{2g(15)} = 17$ m/s.",
          [r"$mg(20) = mg(5.0) + \tfrac12 mv^2$.", r"$v = \sqrt{2(9.8)(15)} = 17.1$ m/s."],
          [r"uses the $5.0$ m height as the drop.",
           r"is the speed at ground level, after the full $20$ m drop.",
           r"adds the heights."], sort=True),
        Q("3.4 Energy lost to friction", r"A $30$ kg child slides from rest down a slide $4.0$ m high and reaches the bottom at $6.0$ m/s. How much mechanical energy was converted to thermal energy?",
          r"$640$ J", [r"$1200$ J", r"$540$ J", r"$1700$ J"],
          r"$mgh - \tfrac12 mv^2 = 1176 - 540 = 636 \approx 640$ J.",
          [r"$mgh = 30(9.8)(4.0) = 1176$ J.", r"$\tfrac12 mv^2 = \tfrac12(30)(36) = 540$ J."],
          [r"is the whole loss of gravitational energy.",
           r"is the kinetic energy at the bottom.",
           r"adds the two instead of subtracting."], sort=True),
    ]),
    Set("Power (3.5)", [
        Q("3.5 Elevator motor", r"An elevator motor raises a $500$ kg car at a constant $2.0$ m/s. What power must the motor deliver?",
          r"$9.8$ kW", [r"$1.0$ kW", r"$2.5$ kW", r"$0$"],
          r"Constant velocity: the motor's force equals the weight, $4900$ N, and $P = Fv = 9800$ W.",
          [r"$P = mgv = 500(9.8)(2.0) = 9.8 \times 10^3$ W."],
          [r"is the car's kinetic energy in joules; at constant speed it does not change.",
           r"divides the weight by the speed.",
           r"the net work is zero, but the motor does positive work while gravity does equal negative work."], sort=True),
        Q("3.5 Work vs. power", r"Two students of equal mass climb the same flight of stairs. Student $A$ takes $10$ s and student $B$ takes $20$ s. Which statement is correct?",
          r"They do the same work, and $A$'s power is twice $B$'s.", [r"$A$ does twice as much work and has twice the power.", r"They have the same power, but $A$ does twice the work.", r"They do the same work and have the same power."],
          r"Work against gravity is $mgh$ for both; power is work divided by time, and $A$ takes half the time.",
          [r"$W = mgh$, the same.", r"$P_A = W/10$, $P_B = W/20$."],
          [r"the work depends only on the weight and the height.",
           r"reverses the roles of work and power.",
           r"power depends on the time taken."]),
        Q("3.5 Power and drag", r"A car's engine delivers $30$ kW to the wheels while the car moves at a constant $20$ m/s on a level road. What is the total resistive force on the car?",
          r"$1.5 \times 10^3$ N", [r"$6.0 \times 10^5$ N", r"$1.5$ N", r"$0$"],
          r"At constant speed the driving force equals the resistive force, and $P = Fv$: $F = 30\,000/20 = 1500$ N.",
          [r"$F = P/v$, with $P$ in watts."],
          [r"multiplies power by speed.",
           r"uses $30$ instead of $30\,000$ W.",
           r"the net force is zero, but the resistive force alone is not; it balances the driving force."], sort=True),
    ]),
]

UNIT = Unit(3, "work-energy-power", "Work, Energy and Power", "18--23\\%", "3.1--3.5",
    abstract=r"""Unit 3 tracks energy through systems: kinetic energy, the work a force does (including the area under a force--position graph) and the work--energy theorem, potential energy as a property of a system (gravitational, both near the surface and in general, and elastic), conservation of energy with and without friction, and power. Energy arguments with bar charts are the fastest route through many exam problems. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Qualitative/Quantitative Translation", 8, r"""A small block of mass $m$ is released from rest at height $h$ on a frictionless curved ramp. At the bottom it slides onto a rough, level floor, where the coefficient of kinetic friction is $\mu$, and comes to rest after sliding a distance $d$ along the floor.""", [
        Part("a", 3, r"A second block of mass $2m$, made of the same material, is released from the same height. Student 1 says it will slide twice as far along the floor because it has twice as much energy. Student 2 says it will slide the same distance. Which student is correct? Justify your answer without deriving or using equations.",
             r"1 pt: Student 2. 1 pt: the heavier block reaches the floor with the same speed but twice the kinetic energy. 1 pt: the friction force on it is also twice as large (it presses on the floor twice as hard), so it removes twice the energy per meter, and the distance is the same.",
             r"Agreeing with Student 1 by considering only the energy and not the friction force."),
        Part("b", 3, r"Derive an expression for $d$ in terms of $h$, $\mu$ and physical constants as appropriate.",
             r"1 pt: the block reaches the floor with $\tfrac12 mv^2 = mgh$. 1 pt: friction does work $-\mu mgd$ on the floor (with $F_N = mg$). 1 pt: $mgh = \mu mgd$, so $d = h/\mu$.",
             r"Including the ramp in the friction work, or using $F_N = mg\cos\theta$ on the level floor."),
        Part("c", 2, r"Explain how your expression in part (b) supports or does not support your answer in part (a).",
             r"1 pt: the expression $d = h/\mu$ does not contain $m$. 1 pt: so blocks of any mass released from the same height slide the same distance, which supports Student 2.",
             r"Saying the expression supports (a) without naming the missing mass."),
    ], mins=18),
    frq_topic="a block sliding from a ramp onto a rough floor",
)
