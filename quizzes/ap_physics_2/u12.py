from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Magnetic fields (12.1)", ["12.1"], r"""
Every magnet has a north and a south pole; like poles repel and unlike poles attract. There are no isolated magnetic poles (monopoles): cut a bar magnet in half and you get two smaller magnets, each with both poles. A magnet is a \textbf{magnetic dipole}.

\begin{terms}
Field lines & outside a magnet they leave the north pole and enter the south pole; inside they continue from south to north, forming closed loops \\
Compass & a small dipole that lines up with the field; its north end points along $\vec B$ \\
Earth & a giant dipole whose magnetic south pole is near the geographic North Pole, which is why a compass's north end points north \\
Ferromagnets & iron, nickel and cobalt contain domains of aligned atomic dipoles; an external field aligns the domains and magnetizes the material \\
\end{terms}
The SI unit of magnetic field is the tesla, T.
""", checks=[
    Q("12.1 Breaking a magnet", r"A bar magnet is cut in half across its middle. Which is correct?",
      r"Each half is a magnet with its own north and south poles.", [r"One half is a north pole and the other is a south pole.", r"Neither half is magnetic.", r"Only the half with the original north pole is magnetic."],
      r"Magnetic poles always come in pairs; there are no magnetic monopoles.",
      [r"Every piece of a magnet is itself a dipole."],
      [r"isolated poles do not exist.",
       r"the aligned domains in each half remain aligned.",
       r"both halves keep their aligned domains."]),
])

S2 = Sec("Magnetism and moving charges (12.2)", ["12.2"], r"""
A magnetic field exerts a force only on a \emph{moving} charge:
\[ F_B = |q|vB\sin\theta , \]
where $\theta$ is the angle between $\vec v$ and $\vec B$. The force is perpendicular to both $\vec v$ and $\vec B$; its direction for a positive charge is given by the right-hand rule ($\vec v \times \vec B$), and it is reversed for a negative charge.

\begin{keyidea}[Circular motion in a uniform field]
Because the force is perpendicular to the velocity, it does no work: the speed is constant. A charge moving perpendicular to a uniform field moves in a circle with $|q|vB = mv^2/r$, so $r = \dfrac{mv}{|q|B}$. Moving parallel to the field, it feels no force at all.
\end{keyidea}

\textbf{Directions on axes.} With $\hat x \times \hat y = \hat z$, $\hat y \times \hat z = \hat x$, $\hat z \times \hat x = \hat y$ (and reversing the order flips the sign): a proton moving in $+x$ through a field in $+y$ is pushed toward $+z$.
""", checks=[
    Q("12.2 Magnetic force", r"A proton moves at $2.0 \times 10^5$ m/s perpendicular to a uniform $0.50$ T magnetic field. What is the magnitude of the magnetic force on it?",
      r"$1.6 \times 10^{-14}$ N", [r"$3.2 \times 10^{-14}$ N", r"$1.0 \times 10^{5}$ N", r"$0$"],
      r"$F = qvB = (1.6 \times 10^{-19})(2.0 \times 10^5)(0.50) = 1.6 \times 10^{-14}$ N.",
      [r"$\sin 90^\circ = 1$."],
      [r"leaves out the $0.50$ T (uses $1$ T).",
       r"is $vB$ without the charge.",
       r"the proton moves across the field, so there is a force."], sort=True),
    Q("12.2 Direction", r"A proton moves in the $+x$ direction through a magnetic field that points in the $+y$ direction. In which direction is the magnetic force on the proton?",
      r"$+z$", [r"$-z$", r"$+y$", r"$-x$"],
      r"$\vec F \propto \vec v \times \vec B = \hat x \times \hat y = +\hat z$ for a positive charge.",
      [r"Right hand: fingers along $\vec v$, curl toward $\vec B$, thumb gives $\vec F$."],
      [r"is the direction for a negative charge.",
       r"the force is perpendicular to the field, never along it.",
       r"the force is perpendicular to the velocity, so it cannot simply oppose it."]),
])

S3 = Sec("Magnetism and current-carrying wires (12.3)", ["12.3"], r"""
\textbf{Wires make fields.} A long straight wire carrying current $I$ produces a magnetic field that circles the wire (right-hand grip: thumb along $I$, fingers curl along $\vec B$), with magnitude
\[ B = \frac{\mu_0 I}{2\pi r}, \qquad \mu_0 = 4\pi \times 10^{-7}\ \mathrm{T\,m/A}. \]

\textbf{Fields push on wires.} A straight wire of length $L$ carrying current $I$ in a field $B$ feels
\[ F = ILB\sin\theta , \]
perpendicular to both the wire and the field. Two parallel wires carrying currents in the same direction attract each other; in opposite directions, they repel. The forces on the two wires are equal and opposite even if the currents differ.
""", checks=[
    Q("12.3 Field of a wire", r"A long straight wire carries a current of $10$ A. What is the magnitude of the magnetic field $0.050$ m from the wire?",
      r"$4.0 \times 10^{-5}$ T", [r"$2.5 \times 10^{-4}$ T", r"$2.0 \times 10^{-5}$ T", r"$1.3 \times 10^{-5}$ T"],
      r"$B = \mu_0 I/(2\pi r) = (4\pi \times 10^{-7})(10)/(2\pi \times 0.050) = 4.0 \times 10^{-5}$ T.",
      [r"$\mu_0/2\pi = 2 \times 10^{-7}\ \mathrm{T\,m/A}$."],
      [r"leaves out the $2\pi$.",
       r"uses $r = 0.10$ m (a diameter instead of a distance).",
       r"is $\mu_0 I$ alone, not divided by $2\pi r$."], sort=True),
])

S4 = Sec("Electromagnetic induction and Faraday's law (12.4)", ["12.4"], r"""
\textbf{Magnetic flux} through a loop of area $A$ is $\Phi_B = BA\cos\theta$, where $\theta$ is the angle between $\vec B$ and the loop's normal (unit: weber, $\mathrm{T\,m^2}$). A \emph{changing} flux induces an emf:
\[ \mathcal{E} = -N\frac{\Delta\Phi_B}{\Delta t} \quad (\text{Faraday's law}). \]
The flux can change because $B$ changes, the area changes (a rod sliding on rails sweeps out area at rate $Lv$, so $\mathcal{E} = BLv$), or the loop turns (a generator).

\begin{keyidea}[Lenz's law]
The induced current flows in the direction whose own magnetic field opposes the \emph{change} in flux. A magnet's north pole pushed toward a loop makes the loop's near face a north pole (repelling it); pulling it away makes that face a south pole (attracting it). Either way you must do work, which is where the electrical energy comes from.
\end{keyidea}
""", checks=[
    Q("12.4 Faraday's law", r"A $50$-turn coil of area $0.020\ \mathrm{m^2}$ lies perpendicular to a magnetic field that increases steadily from $0$ to $0.40$ T in $0.10$ s. What is the magnitude of the induced emf?",
      r"$4.0$ V", [r"$0.080$ V", r"$0.40$ V", r"$40$ V"],
      r"$\mathcal{E} = N\Delta\Phi/\Delta t = 50(0.020)(0.40)/0.10 = 4.0$ V.",
      [r"$\Delta\Phi = A\Delta B = 8.0 \times 10^{-3}$ Wb per turn."],
      [r"leaves out the $50$ turns.",
       r"is $N\Delta\Phi$, not yet divided by $\Delta t$.",
       r"uses $\Delta t = 0.010$ s."], sort=True),
    Q("12.4 Lenz's law", r"The north pole of a bar magnet is pushed toward a wire loop. Which describes the induced current?",
      r"It makes the loop's face toward the magnet a north pole, repelling the magnet.", [r"It makes the loop's face toward the magnet a south pole, attracting the magnet.", r"There is no induced current unless the magnet touches the loop.", r"It flows only while the magnet is at rest near the loop."],
      r"The flux from the magnet through the loop is increasing; the induced current opposes the increase by making a field that pushes back.",
      [r"Lenz: oppose the change, not the field itself."],
      [r"would help the change, giving energy for nothing.",
       r"a changing flux is all that is needed.",
       r"a magnet at rest gives no changing flux and no current."]),
])

QS = [
    Set("Fields and forces on moving charges (12.1--12.2)", [
        Q("12.1 Field lines", r"In which direction do magnetic field lines point outside a bar magnet?",
          r"from the north pole toward the south pole", [r"from the south pole toward the north pole", r"away from both poles", r"toward both poles"],
          r"Outside the magnet, field lines leave the north pole and enter the south pole; they close inside the magnet.",
          [r"A compass's north end points along the field, toward the magnet's south pole."],
          [r"reverses the convention.",
           r"that pattern would need two north poles.",
           r"that pattern would need two south poles."]),
        Q("12.2 Electron's direction", r"An electron moves in the $+x$ direction through a uniform magnetic field pointing in the $+z$ direction. In which direction is the magnetic force on it?",
          r"$+y$", [r"$-y$", r"$+z$", r"There is no force."],
          r"$\hat x \times \hat z = -\hat y$ for a positive charge; the electron's negative charge reverses it to $+\hat y$.",
          [r"Find $\vec v \times \vec B$, then flip for a negative charge."],
          [r"is the direction for a proton.",
           r"the force is perpendicular to the field.",
           r"the electron moves across the field, so there is a force."]),
        Q("12.2 Radius", r"A proton moving at $3.0 \times 10^6$ m/s enters a uniform $0.50$ T magnetic field perpendicular to its velocity. What is the radius of its circular path?",
          r"$0.063$ m", [r"$16$ m", r"$3.4 \times 10^{-5}$ m", r"$0.13$ m"],
          r"$r = mv/(qB) = (1.67 \times 10^{-27})(3.0 \times 10^6)/((1.6 \times 10^{-19})(0.50)) = 0.063$ m.",
          [r"$qvB = mv^2/r$."],
          [r"is $qB/(mv)$, upside down.",
           r"uses the electron's mass.",
           r"is the diameter, not the radius."], sort=True),
        Q("12.2 No work", r"A charged particle moves in a circle in a uniform magnetic field. Which is correct?",
          r"Its speed stays the same, because the magnetic force is always perpendicular to its velocity.", [r"It speeds up, because the magnetic force pulls it toward the center.", r"It slows down, because the field does negative work on it.", r"Its kinetic energy changes, but its speed does not."],
          r"A force perpendicular to the motion does no work, so the kinetic energy and speed are constant.",
          [r"$W = Fd\cos90^\circ = 0$."],
          [r"a centripetal force changes direction, not speed.",
           r"the magnetic force does no work.",
           r"kinetic energy depends only on speed."]),
        Q("12.2 Parallel motion", r"A charged particle moves parallel to a uniform magnetic field. The magnetic force on it is",
          r"zero", [r"maximum", r"along the field", r"opposite to its velocity"],
          r"$F = |q|vB\sin\theta$ with $\theta = 0$.",
          [r"Only the component of velocity perpendicular to $\vec B$ matters."],
          [r"the force is greatest for motion perpendicular to the field.",
           r"the magnetic force is never along the field.",
           r"the magnetic force is never along the velocity."]),
    ]),
    Set("Two parallel wires (12.3)", [
        Q("12.3 Field of wire 1", r"What is the magnitude of the magnetic field that wire 1 produces at the location of wire 2?",
          r"$4.0 \times 10^{-5}$ T", [r"$2.0 \times 10^{-5}$ T", r"$2.5 \times 10^{-4}$ T", r"$8.0 \times 10^{-5}$ T"],
          r"$B_1 = \mu_0 I_1/(2\pi r) = (2 \times 10^{-7})(20)/0.10 = 4.0 \times 10^{-5}$ T.",
          [r"Use wire 1's current, $20$ A."],
          [r"uses wire 2's current.",
           r"leaves out the $2\pi$.",
           r"uses half the separation."], sort=True),
        Q("12.3 Force per meter", r"What is the magnetic force per meter of length on wire 2?",
          r"$4.0 \times 10^{-4}$ N/m, toward wire 1", [r"$4.0 \times 10^{-4}$ N/m, away from wire 1", r"$8.0 \times 10^{-4}$ N/m, toward wire 1", r"$4.0 \times 10^{-5}$ N/m, toward wire 1"],
          r"$F/L = I_2B_1 = (10)(4.0 \times 10^{-5}) = 4.0 \times 10^{-4}$ N/m; currents in the same direction attract.",
          [r"$F = ILB$ with $\theta = 90^\circ$."],
          [r"parallel currents attract.",
           r"uses wire 1's current with wire 1's own field.",
           r"is the field, not the force per meter."]),
        Q("12.3 Third law", r"How does the force per meter on wire 1 compare with the force per meter on wire 2?",
          r"It is equal in size and points toward wire 2.", [r"It is twice as large, because wire 1 carries twice the current.", r"It is half as large.", r"It is zero, because a wire exerts no force on itself."],
          r"$F/L = I_1B_2 = (20)(2.0 \times 10^{-5})$, the same $4.0 \times 10^{-4}$ N/m: a third-law pair.",
          [r"$\mu_0I_1I_2/(2\pi r)$ is symmetric in the two currents."],
          [r"wire 1 carries more current but sits in the weaker field of wire 2.",
           r"the two forces are a third-law pair.",
           r"the force on wire 1 comes from wire 2's field."]),
        Q("12.3 Zero field", r"At what point between the wires, on the line joining them, is the total magnetic field zero?",
          r"$0.067$ m from wire 1", [r"$0.050$ m from wire 1", r"$0.033$ m from wire 1", r"There is no such point between the wires."],
          r"Between parallel currents in the same direction the fields point opposite ways. They cancel where $20/x = 10/(0.10 - x)$: $x = 0.067$ m, nearer the weaker current.",
          [r"$20(0.10 - x) = 10x$."],
          [r"the midpoint would need equal currents.",
           r"is the point closer to the stronger current, where its field wins.",
           r"between same-direction currents the fields oppose, so they can cancel."]),
    ], stim=r"Two long, straight, parallel wires are $0.10$ m apart. Wire 1 carries $20$ A and wire 2 carries $10$ A, in the same direction.",
        stim_title="Questions 6--9"),
    Set("Induction (12.4)", [
        Q("12.4 Flux", r"A loop of area $0.050\ \mathrm{m^2}$ is in a uniform $0.20$ T field. The angle between the field and the loop's normal is $60^\circ$. What is the magnetic flux through the loop?",
          r"$5.0 \times 10^{-3}$ Wb", [r"$1.0 \times 10^{-2}$ Wb", r"$8.7 \times 10^{-3}$ Wb", r"$4.0$ Wb"],
          r"$\Phi = BA\cos\theta = (0.20)(0.050)(0.50) = 5.0 \times 10^{-3}$ Wb.",
          [r"$\theta$ is measured from the normal, so use $\cos 60^\circ$."],
          [r"ignores the angle.",
           r"uses $\sin 60^\circ$.",
           r"divides $B$ by $A$."], sort=True),
        Q("12.4 Induced emf", r"A $200$-turn coil of area $0.010\ \mathrm{m^2}$ lies perpendicular to a magnetic field that decreases steadily from $0.50$ T to zero in $0.25$ s. What is the magnitude of the induced emf?",
          r"$4.0$ V", [r"$0.020$ V", r"$1.0$ V", r"$0.25$ V"],
          r"$\mathcal{E} = N\Delta\Phi/\Delta t = 200(0.010)(0.50)/0.25 = 4.0$ V.",
          [r"$\Delta\Phi = 5.0 \times 10^{-3}$ Wb per turn."],
          [r"leaves out the number of turns.",
           r"is $N\Delta\Phi$, not divided by $\Delta t$.",
           r"multiplies by $\Delta t$ instead of dividing."], sort=True),
        Q("12.4 Seen from the magnet", r"The north pole of a bar magnet is pushed toward a flat wire loop along the loop's axis. Viewed from the magnet's side, the induced current in the loop is",
          r"counterclockwise", [r"clockwise", r"zero", r"clockwise, then counterclockwise"],
          r"The flux through the loop (pointing away from the magnet) increases, so the induced field points back toward the magnet; seen from the magnet, that requires a counterclockwise current.",
          [r"Right-hand rule: counterclockwise current makes a field pointing toward the viewer."],
          [r"would add to the increasing flux.",
           r"the flux is changing, so current is induced.",
           r"the flux only increases while the magnet approaches."]),
        Q("12.4 Sliding rod", r"A metal rod $0.50$ m long slides at $4.0$ m/s along two parallel conducting rails in a uniform $0.30$ T field perpendicular to the plane of the rails. What emf is induced in the rod--rail circuit?",
          r"$0.60$ V", [r"$2.4$ V", r"$0.038$ V", r"$0.15$ V"],
          r"The enclosed area grows at $Lv = 2.0\ \mathrm{m^2/s}$, so $\mathcal{E} = B\,\Delta A/\Delta t = BLv = 0.60$ V.",
          [r"$\Delta\Phi/\Delta t = B(L v)$."],
          [r"divides by the length instead of multiplying.",
           r"divides by the speed instead of multiplying.",
           r"leaves out the speed."], sort=True),
    ]),
]

UNIT = Unit(12, "magnetism-electromagnetism", "Magnetism and Electromagnetism", "12--15\\%", "12.1--12.4",
    abstract=r"""Unit 12 covers magnetic fields and their sources (magnets, dipoles, Earth, currents), the force a magnetic field exerts on a moving charge and on a current-carrying wire, the field of a long straight wire, and electromagnetic induction: magnetic flux, Faraday's law and Lenz's law. Directions are given here on $x$, $y$, $z$ axes; the right-hand rule turns them into forces. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Mathematical Routines", 10, r"""In a mass spectrometer, singly charged positive ions (charge $+e$, mass $m$) start from rest and are accelerated through a potential difference $\Delta V$. They then enter a region of uniform magnetic field $B$ directed perpendicular to their velocity, travel a semicircle, and strike a detector a distance $D$ from the point where they entered the field.""", [
        Part("a", 2, r"Explain why the ions move along a circular path at constant speed while in the magnetic field.",
             r"1 pt: the magnetic force is perpendicular to the ions' velocity, so it does no work and the speed is constant. 1 pt: with constant speed, the force $evB$ has constant magnitude and always points toward a fixed center, so it provides a centripetal force of constant size: uniform circular motion.",
             r"Saying the force is ``centripetal'' without explaining why its size is constant."),
        Part("b", 3, r"Derive an expression for $D$ in terms of $m$, $e$, $\Delta V$, $B$ and physical constants as appropriate.",
             r"1 pt: $e\Delta V = \tfrac12 mv^2$, so $v = \sqrt{2e\Delta V/m}$. 1 pt: $evB = mv^2/r$, so $r = mv/(eB)$. 1 pt: $D = 2r = \dfrac{2}{B}\sqrt{\dfrac{2m\Delta V}{e}}$.",
             r"Setting $D = r$ instead of $2r$."),
        Part("c", 2, r"Neon-20 ions ($m = 3.32 \times 10^{-26}$ kg) are accelerated through $1000$ V into a $0.20$ T field. Calculate $D$.",
             r"1 pt: substitution consistent with (b): $2m\Delta V/e = 2(3.32 \times 10^{-26})(1000)/(1.6 \times 10^{-19}) = 4.15 \times 10^{-4}$ (SI units), whose square root is $0.0204$. 1 pt: $D = (2/0.20)(0.0204) = 0.20$ m.",
             r"Forgetting the square root, or using the proton's mass."),
        Part("d", 3, r"Neon-22 ions, with $\tfrac{22}{20}$ the mass of neon-20, pass through the same spectrometer. A student predicts they will land $10\%$ farther from the entry point than the neon-20 ions. Do you agree or disagree with the student? Justify your answer using your result from part (b).",
             r"1 pt: disagree. 1 pt: from (b), $D \propto \sqrt m$ (everything else is the same). 1 pt: $D_{22}/D_{20} = \sqrt{22/20} = 1.05$, so they land about $5\%$ farther, not $10\%$.",
             r"Agreeing because $D$ ``depends on mass'' without the square root."),
    ], mins=22),
    frq_topic="a mass spectrometer",
)
