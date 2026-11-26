from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Electric charge and electric force (10.1)", ["10.1"], r"""
Electric charge comes in two kinds; like charges repel and unlike charges attract. Charge is quantized in units of $e = 1.6 \times 10^{-19}$ C. The force between two point charges is given by \textbf{Coulomb's law}:
\[ F_E = k\frac{|q_1q_2|}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\ \mathrm{N\,m^2/C^2}. \]
It acts along the line joining the charges, obeys Newton's third law, and falls off as $1/r^2$ like gravity, but is enormously stronger. With several charges, find each force separately and add them as vectors (superposition).

\begin{trap}
Convert prefixes before substituting: $1\ \mu\mathrm C = 10^{-6}$ C, $1$ nC $= 10^{-9}$ C. And square the distance.
\end{trap}
""", checks=[
    Q("10.1 Coulomb's law", r"Two point charges of $+3.0\ \mu$C and $+4.0\ \mu$C are $0.30$ m apart. What is the magnitude of the force each exerts on the other?",
      r"$1.2$ N", [r"$0.36$ N", r"$12$ N", r"$1.2 \times 10^{12}$ N"],
      r"$F = (9.0 \times 10^9)(3.0 \times 10^{-6})(4.0 \times 10^{-6})/(0.30)^2 = 1.2$ N.",
      [r"$q_1q_2 = 1.2 \times 10^{-11}\ \mathrm{C^2}$; $r^2 = 0.090\ \mathrm{m^2}$."],
      [r"divides by $r$ instead of $r^2$.",
       r"uses $r^2 = 0.0090\ \mathrm{m^2}$, misplacing the decimal.",
       r"forgets to convert microcoulombs to coulombs."], sort=True),
    Q("10.1 Distance", r"The distance between two point charges is halved. By what factor does the electric force between them change?",
      r"It becomes $4$ times as large.", [r"It becomes $2$ times as large.", r"It becomes $\tfrac14$ as large.", r"It does not change."],
      r"$F \propto 1/r^2$: halving $r$ multiplies $F$ by $2^2$.",
      [r"$F' = F/(1/2)^2 = 4F$."],
      [r"treats the force as $\propto 1/r$.",
       r"has the change backward: closer charges push harder.",
       r"the force depends on the separation."]),
])

S2 = Sec("Conservation of charge and charging (10.2)", ["10.2"], r"""
Charge is conserved: it moves from object to object but is never created or destroyed. Usually it is electrons that move.

\begin{terms}
Conductors & charges move freely (metals); excess charge spreads over the outer surface \\
Insulators & charges stay put (plastic, glass, rubber) \\
Charging by friction & rubbing transfers electrons from one material to another; the two gain equal and opposite charges \\
Charging by conduction & touching a charged object shares the charge; identical conducting spheres end up with equal charges \\
Charging by induction & a charged object brought near (not touching) pushes charges within a conductor apart; grounding the far side and then removing the ground leaves the conductor with the opposite charge \\
Polarization & in an insulator, the charges in each molecule shift slightly; a charged balloon sticks to a neutral wall because the near opposite charges are attracted more than the far like charges are repelled \\
\end{terms}
""", checks=[
    Q("10.2 Sharing charge", r"Two identical conducting spheres carry charges of $+6.0\ \mu$C and $-2.0\ \mu$C. They are touched together and then separated. What is the charge on each?",
      r"$+2.0\ \mu$C", [r"$+4.0\ \mu$C", r"$+3.0\ \mu$C", r"$+6.0\ \mu$C and $-2.0\ \mu$C, unchanged"],
      r"The total, $+4.0\ \mu$C, is conserved and shared equally by identical spheres.",
      [r"Total charge: $+6.0 + (-2.0) = +4.0\ \mu$C; each gets half."],
      [r"is the total, which the two spheres share.",
       r"ignores the negative charge.",
       r"charge flows between conductors that touch."]),
])

S3 = Sec("Electric fields (10.3)", ["10.3"], r"""
The \textbf{electric field} at a point is the force per unit charge on a small positive test charge placed there:
\[ \vec E = \frac{\vec F_E}{q}, \qquad E = k\frac{|q|}{r^2} \ (\text{point charge}). \]
The field points away from positive charges and toward negative ones. Field lines start on positive charges and end on negative ones; they are close together where the field is strong and never cross. Between large parallel plates with opposite charges, the field is uniform, pointing from the positive plate to the negative plate.

\begin{keyidea}[Superposition]
To find the field from several charges, find each charge's field at the point (size and direction) and add them as vectors. Midway between two equal like charges the fields cancel; midway between equal unlike charges they add, pointing toward the negative charge.
\end{keyidea}
""", checks=[
    Q("10.3 Field of a point charge", r"What is the magnitude of the electric field $0.30$ m from a $2.0$ nC point charge?",
      r"$200$ N/C", [r"$60$ N/C", r"$18$ N/C", r"$2000$ N/C"],
      r"$E = kq/r^2 = (9.0 \times 10^9)(2.0 \times 10^{-9})/(0.090) = 200$ N/C.",
      [r"$kq = 18\ \mathrm{N\,m^2/C}$; divide by $r^2 = 0.090\ \mathrm{m^2}$."],
      [r"divides by $r$ instead of $r^2$.",
       r"is $kq$ alone.",
       r"uses $r^2 = 0.0090\ \mathrm{m^2}$."], sort=True),
])

S4 = Sec("Electric potential energy (10.4)", ["10.4"], r"""
A system of charges has electric potential energy because of their arrangement:
\[ U_E = k\frac{q_1q_2}{r}, \]
with the signs of the charges included. $U_E$ is positive for like charges (you must do positive work to push them together) and negative for unlike charges; it is zero when they are infinitely far apart. For more than two charges, add the potential energy of every pair. In a uniform field, moving a charge $q$ through a potential difference $\Delta V$ changes the system's potential energy by $\Delta U_E = q\Delta V$.
""", checks=[
    Q("10.4 Bringing charges together", r"Two $+1.0\ \mu$C charges are brought from very far apart to $0.10$ m apart. By how much does the electric potential energy of the pair change?",
      r"It increases by $0.090$ J.", [r"It decreases by $0.090$ J.", r"It increases by $0.90$ J.", r"It does not change, since the total charge is the same."],
      r"$U_E = kq_1q_2/r = (9.0 \times 10^9)(1.0 \times 10^{-12})/0.10 = 0.090$ J, up from zero.",
      [r"Like charges: pushing them together stores positive potential energy."],
      [r"like charges gain potential energy as they are pushed together.",
       r"divides by $r^2$: that gives a force-like quantity, not energy.",
       r"potential energy depends on the separation, not just the charges."]),
])

S5 = Sec("Electric potential (10.5)", ["10.5"], r"""
\textbf{Electric potential} is potential energy per unit charge, a scalar measured in volts ($1$ V $= 1$ J/C):
\[ V = k\frac{q}{r} \ (\text{point charge, with sign}), \qquad \Delta U_E = q\Delta V, \qquad |E| = \left|\frac{\Delta V}{\Delta x}\right| \ (\text{uniform field}). \]

\begin{terms}
Direction & the field points from high potential to low potential; positive charges speed up moving toward lower $V$, negative charges toward higher $V$ \\
Equipotentials & surfaces of constant $V$, always perpendicular to field lines; no work is done moving a charge along one \\
Superposition & add the potentials of several charges as numbers (with signs), not as vectors \\
Electron volt & $1\ \mathrm{eV} = 1.6 \times 10^{-19}$ J, the energy gained by one elementary charge crossing $1$ V \\
\end{terms}
""", checks=[
    Q("10.5 Uniform field", r"Two large parallel plates $0.020$ m apart have a potential difference of $12$ V between them. What is the magnitude of the electric field between them?",
      r"$600$ V/m", [r"$0.24$ V/m", r"$1.7 \times 10^{-3}$ V/m", r"$6.0$ V/m"],
      r"$E = \Delta V/d = 12/0.020 = 600$ V/m (the same as N/C).",
      [r"Uniform field: $E = |\Delta V/\Delta x|$."],
      [r"multiplies instead of dividing.",
       r"is $d/\Delta V$, upside down.",
       r"uses $2.0$ m instead of $0.020$ m."], sort=True),
])

S6 = Sec("Capacitors (10.6)", ["10.6"], r"""
A capacitor stores separated charge, $+Q$ on one plate and $-Q$ on the other:
\[ C = \frac{Q}{\Delta V}, \qquad C = \frac{\kappa\varepsilon_0 A}{d} \ (\text{parallel plates}), \qquad U_C = \tfrac12 Q\Delta V = \tfrac12 C(\Delta V)^2 . \]
Capacitance depends only on the geometry and the material between the plates: larger plates, a smaller gap, or a dielectric (dielectric constant $\kappa > 1$) all increase $C$.

\begin{keyidea}[Connected or disconnected?]
Connected to a battery, $\Delta V$ stays fixed, so a change in $C$ changes $Q$. Disconnected (isolated), $Q$ stays fixed, so a change in $C$ changes $\Delta V$. For example, pulling the plates of an isolated capacitor apart halves $C$, doubles $\Delta V$ and doubles the stored energy; the extra energy is the work done pulling the attracting plates apart.
\end{keyidea}
""", checks=[
    Q("10.6 Stored energy", r"A $10\ \mu$F capacitor is charged to $12$ V. How much energy does it store?",
      r"$7.2 \times 10^{-4}$ J", [r"$1.4 \times 10^{-3}$ J", r"$6.0 \times 10^{-5}$ J", r"$1.2 \times 10^{-4}$ J"],
      r"$U = \tfrac12 C(\Delta V)^2 = \tfrac12(10 \times 10^{-6})(144) = 7.2 \times 10^{-4}$ J.",
      [r"Square the potential difference."],
      [r"leaves out the $\tfrac12$.",
       r"is $\tfrac12 C\Delta V$, without squaring.",
       r"is the charge $C\Delta V$ in coulombs, not an energy."], sort=True),
    Q("10.6 Isolated capacitor", r"A charged parallel-plate capacitor is disconnected from its battery, and its plates are then pulled apart to twice their original separation. Which is correct?",
      r"The potential difference and the stored energy both double.", [r"The charge halves and the potential difference stays the same.", r"The potential difference halves and the stored energy halves.", r"Nothing changes, because the capacitor is disconnected."],
      r"Isolated: $Q$ is fixed. $C \propto 1/d$ halves, so $\Delta V = Q/C$ doubles and $U = \tfrac12 Q\Delta V$ doubles.",
      [r"Fixed $Q$; $C$ halves."],
      [r"that would happen only if the battery stayed connected.",
       r"has the effect of separation backward.",
       r"the capacitance changes with the separation."]),
])

S7 = Sec("Conservation of electric energy (10.7)", ["10.7"], r"""
When only electric forces do work, the total energy of a system of charges is conserved: $K_i + U_i = K_f + U_f$. A particle of charge $q$ and mass $m$ that starts from rest and moves through a potential difference $\Delta V$ gains kinetic energy $|q\Delta V|$:
\[ \tfrac12 mv^2 = |q\Delta V| \quad\Rightarrow\quad v = \sqrt{\frac{2|q\Delta V|}{m}} . \]
An electron and a proton crossing the same potential difference gain the same kinetic energy, but the much lighter electron ends up far faster.
""", checks=[
    Q("10.7 Accelerated proton", r"A proton ($m = 1.67 \times 10^{-27}$ kg) is accelerated from rest through a potential difference of $500$ V. What is its final speed?",
      r"$3.1 \times 10^{5}$ m/s", [r"$9.6 \times 10^{10}$ m/s", r"$2.2 \times 10^{5}$ m/s", r"$1.3 \times 10^{7}$ m/s"],
      r"$K = \tfrac12 mv^2 = e\Delta V = 8.0 \times 10^{-17}$ J, so $v = \sqrt{2K/m} = 3.1 \times 10^5$ m/s.",
      [r"$K = e\Delta V = 8.0 \times 10^{-17}$ J."],
      [r"forgets the square root.",
       r"leaves out the factor 2.",
       r"uses the electron's mass."], sort=True),
])

QS = [
    Set("Charge and force (10.1--10.2)", [
        Q("10.1 Two charges", r"Two $+2.0\ \mu$C point charges are $0.10$ m apart. What is the electric force each exerts on the other?",
          r"$3.6$ N, repulsive", [r"$3.6$ N, attractive", r"$0.36$ N, repulsive", r"$1.8$ N, repulsive"],
          r"$F = (9.0 \times 10^9)(2.0 \times 10^{-6})^2/(0.10)^2 = 3.6$ N; like charges repel.",
          [r"$q_1q_2 = 4.0 \times 10^{-12}\ \mathrm{C^2}$; $r^2 = 0.010\ \mathrm{m^2}$."],
          [r"like charges repel.",
           r"divides by $r$ instead of $r^2$.",
           r"uses only one of the charges."]),
        Q("10.2 Induction", r"A negatively charged rod is held near, but not touching, a neutral metal sphere on an insulating stand. The far side of the sphere is briefly touched with a grounded wire, which is then removed, and then the rod is taken away. What is the sphere's final charge?",
          r"positive", [r"negative", r"zero", r"It depends on how long the wire touched it."],
          r"The rod repels electrons in the sphere; with the ground connected, some leave to ground. Removing the ground traps the electron deficit, so the sphere is left positive.",
          [r"Induction gives the opposite sign to the inducing charge."],
          [r"conduction (touching) would give the same sign; here the rod never touches.",
           r"electrons left through the ground wire and could not return.",
           r"the charge left is set once the ground is removed."]),
        Q("10.2 Touching spheres", r"Identical metal spheres $A$ ($+8.0$ nC) and $B$ ($-2.0$ nC) are touched together and separated. What is the charge on $A$ afterward?",
          r"$+3.0$ nC", [r"$+5.0$ nC", r"$+4.0$ nC", r"$+6.0$ nC"],
          r"The total, $+6.0$ nC, is shared equally between identical spheres.",
          [r"$(+8.0 - 2.0)/2 = +3.0$ nC."],
          [r"averages the magnitudes, ignoring the sign of $B$'s charge.",
           r"halves $A$'s charge and ignores $B$.",
           r"is the total, which the two spheres share."], sort=True),
        Q("10.2 Polarization", r"A balloon rubbed on hair sticks to a neutral wall. Which explains this?",
          r"The balloon polarizes the wall's molecules, and the nearby opposite charges are attracted more strongly than the slightly farther like charges are repelled.", [r"The wall has a net charge opposite to the balloon's.", r"Charge flows from the balloon into the insulating wall until both are neutral.", r"Gravity between the balloon and the wall holds it in place."],
          r"The wall stays neutral overall, but its charges shift slightly; the force falls off with distance, so attraction wins.",
          [r"Neutral but polarized: unequal distances give a net attraction."],
          [r"the wall is neutral.",
           r"an insulator does not let charge flow freely; the balloon stays charged.",
           r"gravity between them is far too weak."]),
    ]),
    Set("Two point charges (10.3--10.5)", [
        Q("10.3 Field at the midpoint", r"What is the electric field at the midpoint between the charges, $x = 0.15$ m?",
          r"$2.0 \times 10^3$ N/C in the $+x$ direction", [r"$1.2 \times 10^3$ N/C in the $+x$ direction", r"$2.0 \times 10^3$ N/C in the $-x$ direction", r"$1.6 \times 10^3$ N/C in the $+x$ direction"],
          r"$q_1$ gives $1600$ N/C away from it ($+x$); $q_2$ gives $400$ N/C toward it (also $+x$); they add to $2000$ N/C.",
          [r"$E_1 = (9.0 \times 10^9)(4.0 \times 10^{-9})/(0.15)^2 = 1600$ N/C.", r"$E_2 = (9.0 \times 10^9)(1.0 \times 10^{-9})/(0.15)^2 = 400$ N/C."],
          [r"subtracts the fields, but between unlike charges they point the same way.",
           r"the field points away from the positive charge and toward the negative one, both $+x$ here.",
           r"leaves out the negative charge's field."]),
        Q("10.5 Potential at the midpoint", r"What is the electric potential at the midpoint, $x = 0.15$ m, taking $V = 0$ far away?",
          r"$180$ V", [r"$300$ V", r"$1200$ V", r"$240$ V"],
          r"Potentials add as signed numbers: $V = k(4.0 \times 10^{-9} - 1.0 \times 10^{-9})/0.15 = 180$ V.",
          [r"$V_1 = 240$ V, $V_2 = -60$ V."],
          [r"adds the magnitudes, ignoring the negative charge's sign.",
           r"divides by $r^2$, which gives the field, not the potential.",
           r"leaves out the negative charge."], sort=True),
        Q("10.3 Zero field", r"At what position on the $x$-axis (other than far away) is the electric field zero?",
          r"$x = 0.60$ m", [r"$x = 0.20$ m", r"$x = -0.30$ m", r"There is no such point."],
          r"Between the charges the fields point the same way, so the zero is outside, nearer the smaller charge: $4.0/x^2 = 1.0/(x - 0.30)^2$ gives $x = 0.60$ m.",
          [r"Take the square root: $2.0/x = 1.0/(x - 0.30)$, so $x = 0.60$ m."],
          [r"between unlike charges the fields add; they cannot cancel there.",
           r"beyond the larger charge, its field always wins.",
           r"beyond the smaller charge, the larger, more distant charge's field can balance it."]),
        Q("10.5 Work", r"How much work must an external agent do to bring a $+2.0$ nC charge at constant speed from very far away to the midpoint?",
          r"$3.6 \times 10^{-7}$ J", [r"$-3.6 \times 10^{-7}$ J", r"$4.0 \times 10^{-6}$ J", r"$0$"],
          r"$W = q\Delta V = (2.0 \times 10^{-9})(180 - 0) = 3.6 \times 10^{-7}$ J.",
          [r"The potential rises from $0$ to $180$ V; pushing a positive charge uphill takes positive work."],
          [r"is the work done by the field.",
           r"uses the field ($2000$ N/C) instead of the potential.",
           r"the potential at the midpoint is not zero."]),
    ], stim=r"Point charge $q_1 = +4.0$ nC is fixed at $x = 0$ and point charge $q_2 = -1.0$ nC is fixed at $x = 0.30$ m.",
        stim_title="Questions 5--8"),
    Set("Potential, capacitors and energy (10.5--10.7)", [
        Q("10.5 Equipotentials", r"A charge is moved along an equipotential surface. How much work does the electric field do on it?",
          r"zero", [r"$qV$, where $V$ is the surface's potential", r"$qEd$, where $d$ is the distance moved", r"It depends on the path."],
          r"The field is perpendicular to an equipotential, and $W = -q\Delta V = 0$ when $\Delta V = 0$.",
          [r"No potential difference, no work."],
          [r"work depends on a potential difference, not on the potential itself.",
           r"the field is perpendicular to the motion along an equipotential.",
           r"the electric force is conservative; with $\Delta V = 0$ every path gives zero."]),
        Q("10.7 Electron", r"An electron is accelerated from rest through a potential difference of $200$ V. What kinetic energy does it gain?",
          r"$3.2 \times 10^{-17}$ J", [r"$1.6 \times 10^{-19}$ J", r"$200$ J", r"$8.0 \times 10^{-22}$ J"],
          r"$K = |q\Delta V| = (1.6 \times 10^{-19})(200) = 3.2 \times 10^{-17}$ J, which is $200$ eV.",
          [r"$1$ eV $= 1.6 \times 10^{-19}$ J."],
          [r"is the charge's energy per volt, for $1$ V.",
           r"confuses electron volts with joules.",
           r"divides the charge by the potential difference."], sort=True),
        Q("10.6 Connected capacitor", r"A parallel-plate capacitor stays connected to a battery while its plate separation is halved. What happens to the charge on its plates?",
          r"It doubles.", [r"It is halved.", r"It stays the same.", r"It quadruples."],
          r"Halving $d$ doubles $C$; with $\Delta V$ fixed by the battery, $Q = C\Delta V$ doubles.",
          [r"Connected: $\Delta V$ fixed."],
          [r"has the effect of the separation backward.",
           r"would be true for an isolated capacitor.",
           r"$C \propto 1/d$, not $1/d^2$."]),
        Q("10.6 Energy", r"How much energy does a $5.0\ \mu$F capacitor store when charged to $20$ V?",
          r"$1.0 \times 10^{-3}$ J", [r"$2.0 \times 10^{-3}$ J", r"$5.0 \times 10^{-5}$ J", r"$1.0 \times 10^{-4}$ J"],
          r"$U = \tfrac12 C(\Delta V)^2 = \tfrac12(5.0 \times 10^{-6})(400) = 1.0 \times 10^{-3}$ J.",
          [r"$(\Delta V)^2 = 400\ \mathrm{V^2}$."],
          [r"leaves out the $\tfrac12$.",
           r"is $\tfrac12 C\Delta V$.",
           r"is the charge $C\Delta V$ in coulombs."], sort=True),
        Q("10.7 Proton between plates", r"A proton is released from rest at the positive plate of a parallel-plate capacitor with $1000$ V between its plates, $5.0$ mm apart. How fast is it moving when it reaches the negative plate?",
          r"$4.4 \times 10^{5}$ m/s", [r"$1.9 \times 10^{11}$ m/s", r"$1.9 \times 10^{7}$ m/s", r"$3.1 \times 10^{5}$ m/s"],
          r"$K = \tfrac12 mv^2 = e\Delta V = 1.6 \times 10^{-16}$ J, so $v = \sqrt{2K/m} = 4.4 \times 10^5$ m/s. The gap does not matter.",
          [r"Energy: $K = e\Delta V = 1.6 \times 10^{-16}$ J."],
          [r"forgets the square root.",
           r"uses the electron's mass.",
           r"leaves out the factor 2."], sort=True),
    ]),
]

UNIT = Unit(10, "electric-force-field-potential", "Electric Force, Field and Potential", "15--18\\%", "10.1--10.7",
    abstract=r"""Unit 10 builds electrostatics from Coulomb's law: charge and its conservation, charging by friction, conduction and induction, the electric field (and superposition of fields), electric potential energy and electric potential, equipotentials and uniform fields, capacitors, and conservation of energy for charged particles. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6, S7], qsections=QS,
    frq=FRQ("Qualitative/Quantitative Translation", 8, r"""Two large parallel plates a distance $d$ apart are connected to a battery that keeps a potential difference $\Delta V$ between them. An electron (mass $m$, charge $-e$) is released from rest next to the negative plate and accelerates across the gap to the positive plate. Gravity is negligible.""", [
        Part("a", 3, r"The plates are moved apart to a separation of $2d$ while the battery stays connected, and the experiment is repeated. Will the electron reach the positive plate with a greater speed, a smaller speed, or the same speed as before? Justify your answer without deriving or using equations.",
             r"1 pt: the same speed. 1 pt: the battery keeps the potential difference the same, and the energy the electron gains depends only on its charge and the potential difference it crosses. 1 pt: the field between the plates is weaker, but it acts over a longer distance, and the two effects balance.",
             r"Saying the speed is smaller because the field is weaker, without accounting for the longer distance."),
        Part("b", 3, r"Derive expressions for the electron's speed $v$ when it reaches the positive plate and for the time $t$ it takes to cross the gap, in terms of $e$, $m$, $\Delta V$, $d$ and physical constants as appropriate.",
             r"1 pt: energy: $\tfrac12 mv^2 = e\Delta V$. 1 pt: $v = \sqrt{2e\Delta V/m}$. 1 pt: the acceleration is $a = eE/m = e\Delta V/(md)$, constant, so $d = \tfrac12 at^2$ gives $t = d\sqrt{2m/(e\Delta V)}$ (or $t = 2d/v$).",
             r"Using $E = \Delta V$ without dividing by $d$."),
        Part("c", 2, r"Explain how your expressions in part (b) support or do not support your answer to part (a), and what they predict for the crossing time when the separation is $2d$.",
             r"1 pt: $v = \sqrt{2e\Delta V/m}$ does not contain $d$, so the speed is the same, which supports (a). 1 pt: $t \propto d$, so the crossing takes twice as long at $2d$.",
             r"Stating the expression supports (a) without naming the missing variable."),
    ], mins=18),
    frq_topic="an electron crossing a capacitor gap",
)
