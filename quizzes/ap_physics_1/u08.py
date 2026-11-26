from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Internal structure and density (8.1)", ["8.1"], r"""
A fluid is a substance that flows: a liquid or a gas. Its \textbf{density} is its mass per unit volume,
\[ \rho = \frac{m}{V}, \]
in $\mathrm{kg/m^3}$ (water: $1000\ \mathrm{kg/m^3}$; air: about $1.2\ \mathrm{kg/m^3}$). In this course an \textbf{ideal fluid} is incompressible (constant density), has no viscosity (no internal friction), and flows smoothly without turbulence.

\begin{trap}
Convert volumes carefully: $1\ \mathrm{L} = 10^{-3}\ \mathrm{m^3}$ and $1\ \mathrm{cm^3} = 10^{-6}\ \mathrm{m^3}$.
\end{trap}
""", checks=[
    Q("8.1 Density", r"A $0.50$ kg block has a volume of $2.0 \times 10^{-4}\ \mathrm{m^3}$. What is its density?",
      r"$2.5 \times 10^{3}\ \mathrm{kg/m^3}$", [r"$4.0 \times 10^{-4}\ \mathrm{kg/m^3}$", r"$1.0 \times 10^{-4}\ \mathrm{kg/m^3}$", r"$2.5 \times 10^{2}\ \mathrm{kg/m^3}$"],
      r"$\rho = m/V = 0.50/(2.0 \times 10^{-4}) = 2500\ \mathrm{kg/m^3}$.",
      [r"Dividing by a small volume gives a large density."],
      [r"is $V/m$, upside down.",
       r"is $m \times V$.",
       r"drops a power of ten."], sort=True),
])

S2 = Sec("Pressure (8.2)", ["8.2"], r"""
Pressure is force per unit area, $P = F/A$, measured in pascals ($1\ \mathrm{Pa} = 1\ \mathrm{N/m^2}$). A fluid pushes perpendicular to every surface it touches. In a fluid at rest, pressure increases with depth:
\[ P = P_0 + \rho g h , \qquad P_{gauge} = P - P_{atm} = \rho g h . \]

\begin{terms}
Atmospheric pressure & $P_{atm} \approx 1.0 \times 10^5$ Pa at sea level \\
Absolute vs.\ gauge & absolute pressure includes the atmosphere; gauge pressure (a tire gauge) is the excess over it \\
Depth only & pressure at a given depth is the same everywhere in a connected fluid at rest, whatever the container's shape \\
Net force on a wall & use the pressure difference across it: a submarine hatch feels $(P_{out} - P_{in})A$ \\
\end{terms}
""", checks=[
    Q("8.2 Pressure at depth", r"What is the absolute pressure $10$ m below the surface of a freshwater lake? Take atmospheric pressure as $1.0 \times 10^5$ Pa.",
      r"$2.0 \times 10^5$ Pa", [r"$9.8 \times 10^4$ Pa", r"$1.1 \times 10^5$ Pa", r"$1.0 \times 10^5$ Pa"],
      r"$P = P_{atm} + \rho gh = 1.0 \times 10^5 + (1000)(9.8)(10) \approx 2.0 \times 10^5$ Pa.",
      [r"$\rho gh = 9.8 \times 10^4$ Pa: ten meters of water adds about one atmosphere."],
      [r"is the gauge pressure; the absolute pressure includes the atmosphere.",
       r"leaves out $g$ in $\rho g h$.",
       r"is atmospheric pressure alone; the water adds $\rho gh$."], sort=True),
])

S3 = Sec("Fluids and Newton's laws (8.3)", ["8.3"], r"""
Because pressure increases with depth, a fluid pushes up on the bottom of a submerged object harder than it pushes down on the top. The net upward force is the \textbf{buoyant force}:
\[ F_b = \rho_{fluid}\,V_{disp}\,g \qquad (\text{Archimedes' principle}), \]
the weight of the fluid the object displaces.

\begin{compare}{Case}{Condition}{Consequence}
Floating & $F_b = mg$ & fraction submerged $= \rho_{object}/\rho_{fluid}$ \\
Sinks & $\rho_{object} > \rho_{fluid}$ & a spring scale reads the apparent weight $mg - F_b$ \\
Held under & $\rho_{object} < \rho_{fluid}$ & a downward push $F_b - mg$ is needed \\
\end{compare}

\begin{trap}
The buoyant force depends on the volume of fluid displaced and the fluid's density, not on the object's mass or on how deep it is (once fully submerged).
\end{trap}
""", checks=[
    Q("8.3 Floating", r"A block of wood with density $600\ \mathrm{kg/m^3}$ floats in water. What fraction of its volume is below the surface?",
      r"$60\%$", [r"$40\%$", r"$100\%$", r"$50\%$"],
      r"Floating: $\rho_w V_{sub} g = \rho_b V g$, so $V_{sub}/V = 600/1000 = 0.60$.",
      [r"The displaced water must weigh as much as the block."],
      [r"is the fraction above the surface.",
       r"a block less dense than water floats partly out of it.",
       r"assumes every floating object is half submerged; the fraction depends on the densities."], sort=True),
    Q("8.3 Apparent weight", r"A $2.0$ kg rock with a volume of $5.0 \times 10^{-4}\ \mathrm{m^3}$ hangs from a spring scale, fully submerged in water. What does the scale read?",
      r"$15$ N", [r"$20$ N", r"$4.9$ N", r"$25$ N"],
      r"Buoyant force $= (1000)(5.0 \times 10^{-4})(9.8) = 4.9$ N; scale $= 19.6 - 4.9 = 14.7 \approx 15$ N.",
      [r"$\sum F = 0$: $F_{scale} + F_b = mg$."],
      [r"is the weight in air.",
       r"is the buoyant force alone.",
       r"adds the buoyant force instead of subtracting it."], sort=True),
])

S4 = Sec("Fluids and conservation laws (8.4)", ["8.4"], r"""
\textbf{Conservation of mass (continuity).} An incompressible fluid flowing through a pipe has the same volume flow rate everywhere:
\[ A_1 v_1 = A_2 v_2 . \]
Where the pipe narrows, the fluid speeds up.

\textbf{Conservation of energy (Bernoulli's equation).} Along a streamline in an ideal fluid,
\[ P_1 + \rho g y_1 + \tfrac12\rho v_1^2 = P_2 + \rho g y_2 + \tfrac12\rho v_2^2 . \]
Where a horizontal pipe narrows, the fluid speeds up and its pressure drops. \textbf{Torricelli's theorem} is a special case: water leaving a small hole a depth $h$ below the open surface of a large tank has speed $v = \sqrt{2gh}$, the speed of an object falling from rest through $h$.
""", checks=[
    Q("8.4 Continuity", r"Water flows at $1.5$ m/s through a hose with a cross-sectional area of $2.0\ \mathrm{cm^2}$. It leaves through a nozzle with an area of $0.50\ \mathrm{cm^2}$. How fast does it leave?",
      r"$6.0$ m/s", [r"$0.38$ m/s", r"$3.0$ m/s", r"$1.5$ m/s"],
      r"$A_1 v_1 = A_2 v_2$: $v_2 = (2.0/0.50)(1.5) = 6.0$ m/s.",
      [r"Four times smaller area, four times the speed."],
      [r"inverts the area ratio.",
       r"uses the square root of the area ratio.",
       r"the same volume per second must pass through a smaller opening."], sort=True),
    Q("8.4 Torricelli", r"A large open tank has a small hole in its side $1.25$ m below the water's surface. How fast does water leave the hole?",
      r"$4.9$ m/s", [r"$3.5$ m/s", r"$25$ m/s", r"$12$ m/s"],
      r"$v = \sqrt{2gh} = \sqrt{2(9.8)(1.25)} = 4.9$ m/s.",
      [r"Bernoulli between the surface ($v \approx 0$, $P_{atm}$) and the hole ($P_{atm}$)."],
      [r"is $\sqrt{gh}$, missing the factor 2.",
       r"is $2gh$, missing the square root.",
       r"is $gh$."], sort=True),
])

QS = [
    Set("Density and pressure (8.1--8.2)", [
        Q("8.1 Finding density", r"A $0.30$ kg object displaces $1.2 \times 10^{-4}\ \mathrm{m^3}$ of water when fully submerged. What is the object's density?",
          r"$2.5 \times 10^{3}\ \mathrm{kg/m^3}$", [r"$4.0 \times 10^{-4}\ \mathrm{kg/m^3}$", r"$3.6 \times 10^{-5}\ \mathrm{kg/m^3}$", r"$2.5 \times 10^{4}\ \mathrm{kg/m^3}$"],
          r"Fully submerged, the displaced volume is the object's volume: $\rho = 0.30/(1.2 \times 10^{-4}) = 2500\ \mathrm{kg/m^3}$.",
          [r"$\rho = m/V$."],
          [r"is $V/m$.",
           r"is $m \times V$.",
           r"is off by a factor of ten."], sort=True),
        Q("8.2 Gauge pressure", r"What is the gauge pressure at the bottom of a swimming pool $3.0$ m deep?",
          r"$2.9 \times 10^{4}$ Pa", [r"$1.3 \times 10^{5}$ Pa", r"$3.0 \times 10^{3}$ Pa", r"$9.8 \times 10^{3}$ Pa"],
          r"$P_{gauge} = \rho gh = (1000)(9.8)(3.0) = 2.9 \times 10^4$ Pa.",
          [r"Gauge pressure leaves out the atmosphere."],
          [r"is the absolute pressure.",
           r"leaves out $g$.",
           r"uses a depth of $1.0$ m."], sort=True),
        Q("8.2 Shape of the container", r"Three open containers of different shapes (a wide tank, a narrow tube and a cone) are filled with water to the same depth. How does the water pressure at the bottom compare?",
          r"It is the same in all three.", [r"It is greatest in the wide tank, which holds the most water.", r"It is greatest in the narrow tube.", r"It is greatest in the cone, whose walls slope inward."],
          r"$P = P_{atm} + \rho gh$ depends only on the depth and the fluid's density.",
          [r"Same $\rho$, same $h$, same pressure."],
          [r"more water means more weight, but it rests on a larger area (and on the walls).",
           r"the narrow tube holds less water, but the pressure depends on depth, not volume.",
           r"sloping walls carry part of the weight; the pressure still depends only on depth."]),
        Q("8.2 Force on a hatch", r"A submarine hatch has an area of $0.50\ \mathrm{m^2}$. The submarine is $100$ m below the surface of the sea ($\rho = 1000\ \mathrm{kg/m^3}$), and the air inside is at atmospheric pressure. What is the net force of the water and air on the hatch?",
          r"$4.9 \times 10^{5}$ N", [r"$9.8 \times 10^{5}$ N", r"$5.4 \times 10^{5}$ N", r"$2.0 \times 10^{6}$ N"],
          r"The atmosphere's push on the two sides cancels; the net force is the gauge pressure times the area: $(1000)(9.8)(100)(0.50) = 4.9 \times 10^5$ N.",
          [r"$F_{net} = (P_{out} - P_{in})A = \rho ghA$."],
          [r"is the gauge pressure in pascals, not a force.",
           r"uses the outside absolute pressure but ignores the air pushing back from inside.",
           r"divides the pressure by the area instead of multiplying."], sort=True),
    ]),
    Set("A buoyancy experiment (8.3)", [
        Q("8.3 Fully submerged", r"What does the spring scale read when the cylinder is fully submerged?",
          r"$6.9$ N", [r"$7.8$ N", r"$0.98$ N", r"$8.8$ N"],
          r"$F_b = \rho_w Vg = (1000)(1.0 \times 10^{-4})(9.8) = 0.98$ N, so the scale reads $7.84 - 0.98 = 6.9$ N.",
          [r"Cylinder in equilibrium: $F_{scale} + F_b = mg$."],
          [r"is the reading in air.",
           r"is the buoyant force.",
           r"adds the buoyant force."], sort=True),
        Q("8.3 Half submerged", r"What does the spring scale read when exactly half the cylinder's volume is under water?",
          r"$7.4$ N", [r"$6.9$ N", r"$3.9$ N", r"$7.8$ N"],
          r"Half the volume displaces half as much water: $F_b = 0.49$ N, and $7.84 - 0.49 = 7.35$ N.",
          [r"$F_b \propto V_{disp}$."],
          [r"is the fully submerged reading.",
           r"halves the weight instead of the buoyant force.",
           r"part of the cylinder is under water, so there is a buoyant force."], sort=True),
        Q("8.3 Deeper", r"The fully submerged cylinder is lowered farther, without touching the bottom. The buoyant force on it",
          r"stays the same", [r"increases, because the pressure is greater", r"decreases", r"becomes zero once the cylinder is deep enough"],
          r"The pressure on the top and bottom both increase by the same amount, so their difference, the buoyant force, is unchanged.",
          [r"$F_b = \rho_w V g$ has no depth in it."],
          [r"the extra pressure pushes down on the top as much as up on the bottom.",
           r"the displaced volume does not change.",
           r"a fully submerged object always displaces its own volume."]),
        Q("8.3 The balance", r"The beaker of water sits on a balance. How does the balance reading change when the cylinder goes from hanging in air to hanging fully submerged?",
          r"It increases by $0.98$ N.", [r"It does not change, because the cylinder does not touch the beaker.", r"It increases by $7.8$ N.", r"It decreases by $0.98$ N."],
          r"The water pushes up on the cylinder with $0.98$ N, so by Newton's third law the cylinder pushes down on the water with $0.98$ N, which the balance feels.",
          [r"The spring scale's reading drops by $0.98$ N and the balance's rises by the same amount."],
          [r"the cylinder pushes on the water even without touching the beaker.",
           r"the spring scale still holds most of the cylinder's weight.",
           r"has the direction reversed."]),
        Q("8.3 A different liquid", r"The water is replaced by oil of density $800\ \mathrm{kg/m^3}$. What does the spring scale read with the cylinder fully submerged in the oil?",
          r"$7.1$ N", [r"$6.9$ N", r"$7.8$ N", r"$0.78$ N"],
          r"$F_b = (800)(1.0 \times 10^{-4})(9.8) = 0.78$ N, so the scale reads $7.84 - 0.78 = 7.1$ N.",
          [r"A less dense fluid gives a smaller buoyant force."],
          [r"is the reading in water.",
           r"there is still a buoyant force in oil.",
           r"is the buoyant force in oil, not the scale reading."], sort=True),
    ], stim=r"A student hangs a $0.80$ kg metal cylinder with a volume of $1.0 \times 10^{-4}\ \mathrm{m^3}$ from a spring scale. In air the scale reads $7.8$ N. She then lowers the cylinder into a beaker of water ($\rho = 1000\ \mathrm{kg/m^3}$) that sits on a balance.",
        stim_title="Questions 5--9"),
    Set("Fluid flow (8.4)", [
        Q("8.4 Narrowing pipe", r"Water flows at $0.50$ m/s through a pipe of radius $2.0$ cm, which narrows to a radius of $1.0$ cm. What is the speed in the narrow section?",
          r"$2.0$ m/s", [r"$1.0$ m/s", r"$0.13$ m/s", r"$0.25$ m/s"],
          r"Area goes as radius squared: halving the radius quarters the area, so the speed is $4 \times 0.50 = 2.0$ m/s.",
          [r"$A_1v_1 = A_2v_2$ with $A = \pi r^2$."],
          [r"uses the ratio of radii, not areas.",
           r"inverts the area ratio.",
           r"inverts the ratio of radii."], sort=True),
        Q("8.4 Pressure in a constriction", r"Water flows steadily through a horizontal pipe that narrows and then widens again. Where is the water's pressure lowest?",
          r"in the narrow section, where it moves fastest", [r"in the narrow section, because the water is squeezed", r"in the wide sections, where it moves slowest", r"It is the same everywhere in a horizontal pipe."],
          r"Bernoulli with $y$ constant: $P + \tfrac12\rho v^2$ is constant, so the fastest flow has the lowest pressure.",
          [r"Continuity: fastest where narrowest. Bernoulli: lowest pressure where fastest."],
          [r"``squeezed'' suggests higher pressure, but the pressure there is lower.",
           r"the slow, wide sections have the highest pressure.",
           r"pressure changes wherever the speed does."]),
        Q("8.4 Leaking tank", r"Water leaks from a small hole in the side of a large open tank, $2.0$ m below the surface. How fast does it leave the hole?",
          r"$6.3$ m/s", [r"$4.4$ m/s", r"$39$ m/s", r"$20$ m/s"],
          r"Torricelli: $v = \sqrt{2gh} = \sqrt{39.2} = 6.3$ m/s.",
          [r"The same speed as an object dropped from rest through $2.0$ m."],
          [r"is $\sqrt{gh}$.",
           r"is $2gh$ without the square root.",
           r"is $gh$, missing both the factor 2 and the square root."], sort=True),
        Q("8.4 Flow rate", r"A hose with a cross-sectional area of $3.0 \times 10^{-4}\ \mathrm{m^2}$ carries water at $2.0$ m/s. What is the volume flow rate?",
          r"$6.0 \times 10^{-4}\ \mathrm{m^3/s}$", [r"$1.5 \times 10^{-4}\ \mathrm{m^3/s}$", r"$6.7 \times 10^{3}\ \mathrm{m^3/s}$", r"$6.0 \times 10^{-2}\ \mathrm{m^3/s}$"],
          r"Volume flow rate $= Av = (3.0 \times 10^{-4})(2.0) = 6.0 \times 10^{-4}\ \mathrm{m^3/s}$ ($0.60$ L/s).",
          [r"Each second a column $2.0$ m long passes any point."],
          [r"divides the area by the speed.",
           r"divides the speed by the area.",
           r"is off by a factor of $100$."], sort=True),
    ]),
]

UNIT = Unit(8, "fluids", "Fluids", "10--15\\%", "8.1--8.4",
    abstract=r"""Unit 8 applies the laws of mechanics to fluids: density and the ideal-fluid model; pressure, including how it grows with depth and the difference between absolute and gauge pressure; the buoyant force and Archimedes' principle as an application of Newton's laws; and the continuity equation and Bernoulli's equation as statements of conservation of mass and energy for a flowing fluid. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Mathematical Routines", 10, r"""A wooden block of density $\rho_b$ and volume $V$ floats in water of density $\rho_w$. A student pushes down on the top of the block with a vertical force $F$ and holds it at rest, completely under water.""", [
        Part("a", 2, r"Draw a free-body diagram of the block while it is held at rest under water, showing and labeling each force as an arrow starting on a dot.",
             r"1 pt: three forces: weight $mg$ down, the student's push $F$ down, and the buoyant force $F_b$ up; no others. 1 pt: the buoyant-force arrow is drawn longer than either downward arrow, equal to their sum.",
             r"Leaving out the buoyant force, or adding a ``water pressure'' force in addition to it."),
        Part("b", 3, r"Derive an expression for $F$ in terms of $\rho_b$, $\rho_w$, $V$ and physical constants as appropriate.",
             r"1 pt: $F_b = \rho_w Vg$. 1 pt: equilibrium: $F_b = mg + F$ with $m = \rho_b V$. 1 pt: $F = (\rho_w - \rho_b)Vg$.",
             r"Using the block's density in the buoyant force."),
        Part("c", 2, r"The block has a volume of $2.0 \times 10^{-3}\ \mathrm{m^3}$ and a density of $600\ \mathrm{kg/m^3}$. Calculate $F$.",
             r"1 pt: substitution consistent with (b): $F = (1000 - 600)(2.0 \times 10^{-3})(9.8)$. 1 pt: $F = 7.8$ N.",
             r"Answers with no units, or using $1.0\ \mathrm{g/cm^3}$ mixed with SI volume."),
        Part("d", 3, r"The student lets go. A classmate claims that, just after release, the block accelerates upward at less than $g$. Do you agree or disagree with the classmate? Justify your answer. (Neglect the drag of the water.)",
             r"1 pt: agree, for this block. 1 pt: just after release the net force is $F_b - mg = (\rho_w - \rho_b)Vg$ upward. 1 pt: $a = \dfrac{(\rho_w - \rho_b)Vg}{\rho_b V} = \left(\dfrac{\rho_w}{\rho_b} - 1\right)g = \tfrac23 g = 6.5\ \mathrm{m/s^2}$, less than $g$ (a block less than half as dense as water would accelerate at more than $g$).",
             r"Claiming the acceleration must be $g$ because the block is ``released''."),
    ], mins=22),
    frq_topic="holding a floating block under water",
)
