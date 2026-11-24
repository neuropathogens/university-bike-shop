from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Magnetic fields (12.1)", ["12.1"], r"""
Magnetic fields are produced by moving charges: currents, and the spins and orbits of electrons in magnetic materials. Field lines leave a magnet's north pole and enter its south pole, but unlike electric field lines they never start or end: they form closed loops. There are no magnetic monopoles, so
\[ \oint\vec B\cdot d\vec A = 0 \quad \text{(Gauss's law for magnetism)}. \]
The SI unit is the tesla, $1\ \mathrm{T} = 1\ \mathrm{N/(A\cdot m)}$. Earth's field is about $5\times10^{-5}$ T; a classroom bar magnet, about $10^{-2}$ T near its poles.
\begin{trap}
Cutting a bar magnet in half gives two smaller magnets, each with both poles, never an isolated pole.
\end{trap}
""", checks=[
    Q("12.1 Magnetic flux through a closed surface", r"A closed surface encloses only the north-pole end of a bar magnet. What is the net magnetic flux through the surface?",
      r"Zero", [r"Positive, because field lines leave the north pole", r"Negative, because field lines enter the south pole", r"It depends on the magnet's strength"],
      r"Magnetic field lines form closed loops; every line that leaves the surface also enters it somewhere (inside the magnet the lines run from S to N). Net flux is always zero.",
      [r"$\oint\vec B\cdot d\vec A = 0$ for every closed surface."],
      [r"forgets the lines running back through the magnet inside the surface.", r"the south pole is not inside this surface, and the net is zero anyway.", r"the law holds for any magnet: there are no monopoles."]),
])

S2 = Sec("Magnetic forces on moving charges and currents (12.2)", ["12.2"], r"""
\[ \vec F = q\vec v\times\vec B, \qquad F = |q|vB\sin\theta, \qquad \vec F = I\vec L\times\vec B\ \ \text{(straight wire)}. \]
\begin{itemize}
\item The force is perpendicular to both $\vec v$ and $\vec B$ (right-hand rule; flip it for negative charges). Because $\vec F \perp \vec v$, a magnetic force does \textbf{no work} and never changes a particle's speed.
\item A charge moving perpendicular to a uniform $\vec B$ moves in a circle: $qvB = mv^2/r$, so $r = \dfrac{mv}{qB}$, and the period $T = \dfrac{2\pi m}{qB}$ does not depend on speed.
\item Crossed $\vec E$ and $\vec B$ fields pass undeflected only particles with $v = E/B$ (velocity selector).
\item A current loop in a uniform field feels no net force but a torque $\vec\tau = \vec\mu\times\vec B$, with magnetic moment $\mu = NIA$ along the loop's normal (right-hand rule with the current).
\end{itemize}
""", checks=[
    Q("12.2 Direction of force", r"A proton moves in the $+x$ direction through a magnetic field that points in the $+y$ direction. Which way is the magnetic force on it?",
      r"$+z$", [r"$-z$", r"$+y$", r"$-x$"],
      r"$\vec F = q\vec v\times\vec B \propto \hat\imath\times\hat\jmath = +\hat k$; the proton is positive, so the force is $+z$.",
      [r"$\hat\imath\times\hat\jmath = \hat k$."],
      [r"would be the force on an electron.", r"the force is perpendicular to $\vec B$, never along it.", r"the force is perpendicular to the velocity, so it cannot slow the proton directly."]),
    Q("12.2 Work by a magnetic force", r"A charged particle moves through a region with only a uniform magnetic field. What happens to its speed?",
      r"It stays constant.", [r"It increases.", r"It decreases.", r"It increases if the charge is positive and decreases if negative."],
      r"The magnetic force is always perpendicular to the velocity, so it does no work: it changes direction, not speed.",
      [r"$P = \vec F\cdot\vec v = 0$ for $\vec F = q\vec v\times\vec B$."],
      [r"magnetic forces do no work.", r"magnetic forces do no work.", r"the sign of the charge only reverses the direction of the deflection."]),
])

S3 = Sec("Fields of currents and the Biot--Savart law (12.3)", ["12.3"], r"""
\[ d\vec B = \frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}, \qquad \mu_0 = 4\pi\times10^{-7}\ \mathrm{T\,m/A}. \]
\begin{compare}{Source}{Field}{Where}
Long straight wire & $\dfrac{\mu_0 I}{2\pi r}$, circling the wire & distance $r$ \\
Circular loop, radius $R$ & $\dfrac{\mu_0 I}{2R}$, along the axis & at the center \\
Arc of angle $\theta$ (rad) & $\dfrac{\mu_0 I\theta}{4\pi R}$ & at the center of the arc \\
Straight segment pointing at the point & $0$ & any point on its line ($d\vec l \parallel \hat r$) \\
\end{compare}
\textbf{Parallel wires} exert forces per length $\dfrac{F}{L} = \dfrac{\mu_0 I_1I_2}{2\pi d}$: currents in the same direction attract, opposite directions repel (the reverse of charges).
\begin{trap}
Use the right-hand grip rule for direction: thumb along the current, fingers curl the way $\vec B$ circles the wire.
\end{trap}
""", checks=[
    Q("12.3 Long straight wire", r"A long straight wire carries 10 A. What is the magnetic field 2.0 cm from it?",
      r"$1.0\times10^{-4}$ T", [r"$1.0\times10^{-6}$ T", r"$3.1\times10^{-4}$ T", r"$5.0\times10^{-3}$ T"],
      r"$B = \dfrac{\mu_0 I}{2\pi r} = \dfrac{(2\times10^{-7})(10)}{0.020} = 1.0\times10^{-4}$ T.",
      [r"$\mu_0/2\pi = 2\times10^{-7}$ T$\cdot$m/A.", r"$B = 2\times10^{-6}/0.020 = 1.0\times10^{-4}$ T."],
      [r"uses $r = 2.0$ m.", r"uses $\mu_0 I/(2r)$, the field at the center of a loop.", r"divides by $r^2$."], sort=True),
    Q("12.3 Parallel currents", r"Two long parallel wires carry currents in opposite directions. The wires",
      r"repel each other", [r"attract each other", r"exert no force on each other", r"twist to become perpendicular"],
      r"Opposite currents repel; same-direction currents attract. Check with the right-hand rule: the field of one wire, crossed with the other's current, points away.",
      [r"$F/L = \mu_0 I_1I_2/(2\pi d)$; direction from $I\vec L\times\vec B$."],
      [r"is the case for currents in the same direction.", r"each wire sits in the other's field and carries current, so each feels a force.", r"parallel wires feel forces along the line joining them, not torques."]),
])

S4 = Sec(r"Amp\`ere's law (12.4)", ["12.4"], r"""
\[ \oint\vec B\cdot d\vec l = \mu_0 I_{enc}. \]
Like Gauss's law, it always holds but gives $B$ only with symmetry: choose an Amp\`erian loop along which $B$ is constant and parallel to the path (or perpendicular, contributing nothing).
\begin{compare}{Current distribution}{Amp\`erian loop}{Result}
Long wire (outside) & circle of radius $r$ & $B = \mu_0 I/(2\pi r)$ \\
Inside a long wire, uniform current, radius $R$ & circle $r < R$; $I_{enc} = Ir^2/R^2$ & $B = \dfrac{\mu_0 Ir}{2\pi R^2}$ \\
Long solenoid, $n$ turns per length & rectangle, one side inside & $B = \mu_0 nI$ inside, $\approx 0$ outside \\
Toroid, $N$ turns & circle inside the core & $B = \dfrac{\mu_0 NI}{2\pi r}$ \\
\end{compare}
A coaxial cable with equal and opposite currents has $I_{enc} = 0$ outside it, so no field leaks out.
""", checks=[
    Q("12.4 Solenoid", r"A long solenoid's number of turns per meter is doubled while the current stays the same. What happens to the field inside?",
      r"It doubles.", [r"It halves.", r"It quadruples.", r"It is unchanged."],
      r"$B = \mu_0 nI \propto n$.",
      [r"Ampère's law with a rectangular loop gives $B\ell = \mu_0(n\ell)I$."],
      [r"inverts the dependence.", r"squares the factor.", r"more turns enclose more current, so the field grows."]),
])

QS1 = [
    Q("12.1 Field lines", r"Which statement about magnetic field lines is true?",
      r"They form closed loops with no beginning or end.", [r"They start on north poles and end on south poles.", r"They can cross where two magnets' fields meet.", r"They point in the direction of the magnetic force on a moving charge."],
      r"There are no magnetic monopoles, so field lines close on themselves (running S to N inside a magnet).",
      [r"$\oint\vec B\cdot d\vec A = 0$ for every closed surface."],
      [r"outside a magnet they run N to S, but they continue inside, closing the loop.", r"the field has one direction at each point, so lines never cross.", r"the force is perpendicular to $\vec B$."]),
    Q("12.2 Force on an electron", r"An electron moves in the $+x$ direction in a magnetic field pointing in the $+z$ direction. What is the direction of the magnetic force on it?",
      r"$+y$", [r"$-y$", r"$+z$", r"$-x$"],
      r"$\hat\imath\times\hat k = -\hat\jmath$; the electron's negative charge flips it to $+\hat\jmath$.",
      [r"$\vec v\times\vec B \propto \hat\imath\times\hat k = -\hat\jmath$.", r"$q < 0$: $\vec F$ along $+\hat\jmath$."],
      [r"is the force on a proton.", r"the force is perpendicular to $\vec B$.", r"the force is perpendicular to $\vec v$."]),
    Q("12.2 Radius of circular motion", r"A proton moving at $2.0\times10^6$ m/s enters a uniform 0.50 T field perpendicular to its velocity. What is the radius of its path? ($m_p = 1.67\times10^{-27}$ kg, $e = 1.6\times10^{-19}$ C)",
      r"$4.2$ cm", [r"$0.0023$ cm", r"$2.1$ cm", r"$8.4$ cm"],
      r"$r = \dfrac{mv}{qB} = \dfrac{(1.67\times10^{-27})(2.0\times10^6)}{(1.6\times10^{-19})(0.50)} = 0.042$ m.",
      [r"$qvB = mv^2/r$.", r"$r = 3.34\times10^{-21}/8.0\times10^{-20} = 0.042$ m."],
      [r"uses the electron's mass.", r"is half the radius, as if $B$ were doubled.", r"is the diameter."], sort=True),
    Q("12.2 Cyclotron period", r"A charged particle circles in a uniform magnetic field. If its speed is doubled, its period of revolution",
      r"stays the same", [r"doubles", r"halves", r"quadruples"],
      r"$T = 2\pi r/v = 2\pi m/(qB)$: the radius doubles with the speed, so the time per lap does not change.",
      [r"$r \propto v$, so $T = 2\pi r/v$ is independent of $v$."],
      [r"forgets that the radius grows too.", r"forgets that the radius grows too.", r"has no basis."]),
    Q("12.2 Velocity selector", r"Perpendicular fields $E = 3000$ V/m and $B = 0.020$ T are crossed so that their forces on a moving charge oppose. What speed passes through undeflected?",
      r"$1.5\times10^{5}$ m/s", [r"$60$ m/s", r"$6.7\times10^{-6}$ m/s", r"$1.5\times10^{3}$ m/s"],
      r"Balance: $qE = qvB$, so $v = E/B = 3000/0.020 = 1.5\times10^5$ m/s.",
      [r"Electric force $qE$; magnetic force $qvB$.", r"$v = E/B$."],
      [r"multiplies $E$ by $B$.", r"is $B/E$.", r"drops a factor of 100 in the division."], sort=True),
    Q("12.2 Force on a wire", r"A 0.50 m wire carrying 4.0 A lies at $30^\circ$ to a uniform 0.20 T field. What is the magnitude of the force on it?",
      r"$0.20$ N", [r"$0.40$ N", r"$0.35$ N", r"$0.80$ N"],
      r"$F = ILB\sin\theta = (4.0)(0.50)(0.20)\sin 30^\circ = 0.20$ N.",
      [r"$ILB = 0.40$ N; times $\sin 30^\circ = 0.5$."],
      [r"assumes the wire is perpendicular to the field.", r"uses $\cos 30^\circ$.", r"leaves out the wire's length: $IB = 0.80$."], sort=True),
    Q("12.2 Torque on a coil", r"A square coil of 50 turns, 0.10 m on a side, carries 2.0 A in a 0.30 T field. The plane of the coil is parallel to the field. What is the torque on it?",
      r"$0.30$ N$\cdot$m", [r"$0$", r"$0.0060$ N$\cdot$m", r"$3.0$ N$\cdot$m"],
      r"With the plane parallel to $\vec B$, the magnetic moment (normal to the plane) is perpendicular to $\vec B$: $\tau = NIAB = (50)(2.0)(0.010)(0.30) = 0.30$ N$\cdot$m, the maximum.",
      [r"$\mu = NIA = 1.0\ \mathrm{A\,m^2}$.", r"$\tau = \mu B\sin 90^\circ = 0.30$ N$\cdot$m."],
      [r"would be true with the plane perpendicular to the field (moment parallel to $\vec B$).", r"counts only one turn.", r"uses side length instead of area."], sort=True),
    Q("12.3 Field of a long wire", r"A long straight wire carries 20 A. What is the magnetic field 4.0 cm away?",
      r"$1.0\times10^{-4}$ T", [r"$3.1\times10^{-4}$ T", r"$5.0\times10^{-5}$ T", r"$2.5\times10^{-3}$ T"],
      r"$B = \mu_0I/(2\pi r) = (2\times10^{-7})(20)/0.040 = 1.0\times10^{-4}$ T.",
      [r"$B = 4.0\times10^{-6}/0.040$."],
      [r"uses $\mu_0I/(2r)$, the loop-center formula.", r"uses 8.0 cm, the diameter of the circle.", r"divides by $r^2$."], sort=True),
    Q("12.3 Semicircular wire", r"A wire runs along a straight line toward a point P, around a semicircle of radius $R$ centered on P, and away from P along the same line. It carries current $I$. What is the magnetic field at P?",
      r"$\dfrac{\mu_0 I}{4R}$", [r"$\dfrac{\mu_0 I}{2R}$", r"$\dfrac{\mu_0 I}{2\pi R}$", r"$0$"],
      r"The straight parts point along the line through P, so $d\vec l\times\hat r = 0$ for them. The semicircle gives half a full loop's field: $\tfrac12 \cdot \dfrac{\mu_0 I}{2R}$.",
      [r"Arc: $B = \dfrac{\mu_0 I\theta}{4\pi R}$ with $\theta = \pi$.", r"Straight leads aimed at P contribute nothing."],
      [r"is a full loop.", r"is a long straight wire at distance $R$.", r"the straight parts give zero, but the arc does not."]),
    Q("12.3 Force between wires", r"Two long parallel wires 0.10 m apart carry 5.0 A and 8.0 A in the same direction. What is the force per meter between them?",
      r"$8.0\times10^{-5}$ N/m, attractive", [r"$8.0\times10^{-5}$ N/m, repulsive", r"$1.6\times10^{-4}$ N/m, attractive", r"$8.0\times10^{-6}$ N/m, attractive"],
      r"$F/L = \mu_0 I_1I_2/(2\pi d) = (2\times10^{-7})(40)/0.10 = 8.0\times10^{-5}$ N/m. Same-direction currents attract.",
      [r"$I_1I_2 = 40\ \mathrm{A^2}$.", r"$F/L = 8.0\times10^{-5}$ N/m."],
      [r"has the right size but the wrong direction; parallel currents attract.", r"doubles the force (uses $\mu_0/\pi$).", r"uses $d = 1.0$ m."]),
    Q("12.4 Solenoid field", r"A long solenoid has 2000 turns per meter and carries 3.0 A. What is the field inside? ($\mu_0 = 4\pi\times10^{-7}$ T$\cdot$m/A)",
      r"$7.5\times10^{-3}$ T", [r"$3.8\times10^{-3}$ T", r"$1.2\times10^{-3}$ T", r"$1.5\times10^{-2}$ T"],
      r"$B = \mu_0 nI = (4\pi\times10^{-7})(2000)(3.0) = 7.5\times10^{-3}$ T.",
      [r"$nI = 6000$ A/m.", r"$B = 7.54\times10^{-3}$ T."],
      [r"halves it, as for the field at the end of a solenoid.", r"divides by $2\pi$, mixing in the straight-wire formula.", r"doubles it with no basis."], sort=True),
    Q("12.4 Inside a thick wire", r"A long cylindrical wire of radius $R$ carries current $I$ spread uniformly over its cross-section. What is the magnetic field at $r = R/2$?",
      r"$\dfrac{\mu_0 I}{4\pi R}$", [r"$\dfrac{\mu_0 I}{\pi R}$", r"$\dfrac{\mu_0 I}{2\pi R}$", r"$0$"],
      r"$I_{enc} = I(r/R)^2 = I/4$. Ampère: $B(2\pi r) = \mu_0 I/4$ with $r = R/2$, so $B = \dfrac{\mu_0 I}{4\pi R}$.",
      [r"Enclosed current scales with area.", r"$B = \dfrac{\mu_0 Ir}{2\pi R^2}$ at $r = R/2$."],
      [r"uses the full current $I$ at $r = R/2$.", r"is the field at the surface, $r = R$.", r"the enclosed current is not zero inside the wire."]),
    Q("12.4 Coaxial cable", r"A coaxial cable carries current $I$ along its central wire and the same current back along its outer conductor. What is the magnetic field outside the cable?",
      r"Zero", [r"$\dfrac{\mu_0 I}{2\pi r}$", r"$\dfrac{\mu_0 I}{\pi r}$", r"$\mu_0 I$"],
      r"An Ampèrian circle outside encloses $I - I = 0$, and by symmetry $B$ is the same all around it, so $B = 0$.",
      [r"$I_{enc} = 0 \Rightarrow B(2\pi r) = 0$."],
      [r"counts only the central wire.", r"adds the two currents instead of letting them cancel.", r"has the units of $B\cdot$length."]),
]

UNIT = Unit(
    n=12, slug="magnetic-fields", title="Magnetic Fields and Electromagnetism", weight="10--20\\%", topics="12.1--12.4",
    abstract=r"""Unit 12 covers magnetism produced by and acting on moving charges. It covers magnetic fields and Gauss's law for magnetism (12.1); the force $q\vec v\times\vec B$ on moving charges and $I\vec L\times\vec B$ on currents, circular motion, velocity selectors, and torque on current loops (12.2); the Biot--Savart law for wires, loops, and arcs (12.3); and Ampère's law for wires, solenoids, toroids, and coaxial cables (12.4). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4],
    qsections=[("Magnetic forces (12.1--12.2)", QS1[:7]), ("Fields of currents (12.3--12.4)", QS1[7:])],
    frq=FRQ("Mathematical Routines", 10, r"""In a mass spectrometer, an ion of charge $+q$ and unknown mass $m$ starts from rest and is accelerated through a potential difference $\Delta V$. It then enters a region of uniform magnetic field $B$, directed perpendicular to its velocity, travels a semicircle, and strikes a detector a distance $D$ from the point where it entered the field. Ignore gravity.""", [
        Part("a", 2, r"Derive an expression for the ion's speed $v$ as it enters the magnetic field.",
             r"1 pt: energy conservation, $q\Delta V = \tfrac12 mv^2$. 1 pt: $v = \sqrt{2q\Delta V/m}$.",
             r"Using $v = E/B$ from a velocity selector, which is not part of this device."),
        Part("b", 3, r"Derive an expression for the radius $r$ of the ion's path in terms of $q$, $m$, $\Delta V$, and $B$.",
             r"1 pt: magnetic force supplies the centripetal force, $qvB = mv^2/r$. 1 pt: $r = mv/(qB)$. 1 pt: substitutes (a): $r = \dfrac{1}{B}\sqrt{\dfrac{2m\Delta V}{q}}$.",
             r"Setting $qvB$ equal to $mv^2$ (dropping $r$) or to $mg$."),
        Part("c", 2, r"Derive an expression for $m$ in terms of $q$, $B$, $\Delta V$, and $D$.",
             r"1 pt: $D = 2r$ (the detector is a diameter away). 1 pt: $m = \dfrac{qB^2D^2}{8\Delta V}$.",
             r"Using $D = r$."),
        Part("d", 3, r"Derive an expression for the time the ion spends in the magnetic field, and show that it does not depend on $\Delta V$.",
             r"1 pt: time is half a period, $t = \pi r/v$. 1 pt: with $r = mv/(qB)$, $t = \dfrac{\pi m}{qB}$. 1 pt: $\Delta V$ (hence $v$) cancels: a faster ion travels a proportionally larger semicircle.",
             r"Using $t = D/v$, a straight-line distance."),
    ]),
    frq_topic="a mass spectrometer",
)
