from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Electrostatics with conductors (10.1)", ["10.1"], r"""
In electrostatic equilibrium (no charges moving), a conductor obeys four rules:
\begin{enumerate}[label=(\arabic*)]
\item $\vec E = 0$ everywhere inside the material (otherwise free electrons would move).
\item Any net charge lives on the surface. A cavity with no charge inside it has no charge on its wall and no field.
\item Just outside, $\vec E$ is perpendicular to the surface with $E = \sigma/\varepsilon_0$.
\item The whole conductor is one equipotential, including its interior.
\end{enumerate}
\begin{example}[Shell around a charge]
A neutral conducting shell surrounds a point charge $+q$. A Gaussian surface inside the metal has $E = 0$, so $Q_{enc} = 0$: the inner surface holds $-q$. The shell is neutral, so the outer surface holds $+q$, and outside the field is $kq/r^2$ as if the shell were not there.
\end{example}
\begin{trap}
$E = \sigma/\varepsilon_0$ next to a conductor, but $\sigma/(2\varepsilon_0)$ next to an isolated sheet of charge. The conductor's field is all on one side.
\end{trap}
""", checks=[
    Q("10.1 Inside a conductor", r"A solid metal sphere carries net charge $+Q$ and is in electrostatic equilibrium. What is the electric field at a point inside the metal, halfway from the center to the surface?",
      r"Zero", [r"$kQ/(R/2)^2$", r"$kQ/(2R^2)$", r"$kQ/R^2$"],
      r"In equilibrium the field inside a conductor is zero, and the charge sits on the outer surface.",
      [r"Any field inside would push free electrons, so they rearrange until $E = 0$."],
      [r"treats the charge as a point at the center.", r"is the uniformly charged insulator result at $r = R/2$.", r"is the field just outside the surface."]),
])

S2 = Sec("Redistribution of charge between conductors (10.2)", ["10.2"], r"""
Conductors joined by a wire become one equipotential. Charge flows until the potentials match. For two distant spheres of radii $R_1$ and $R_2$:
\[ \frac{kq_1}{R_1} = \frac{kq_2}{R_2} \ \Rightarrow\ \frac{q_1}{q_2} = \frac{R_1}{R_2}, \qquad \frac{\sigma_1}{\sigma_2} = \frac{R_2}{R_1}. \]
The larger sphere takes more charge, but the smaller one has the larger surface charge density and stronger surface field. That is why charge crowds onto sharp points and why lightning rods are pointed. \textbf{Grounding} connects a conductor to Earth, a huge reservoir at $V = 0$, so charge flows until the conductor's potential is zero.
""", checks=[
    Q("10.2 Spheres joined by a wire", r"A metal sphere of radius $R$ and a distant metal sphere of radius $2R$ are joined by a thin wire. What is the ratio of the charge on the small sphere to the charge on the large sphere?",
      r"$1:2$", [r"$1:1$", r"$1:4$", r"$2:1$"],
      r"Equal potentials: $kq_1/R = kq_2/(2R)$, so $q_1/q_2 = 1/2$.",
      [r"Joined conductors share a potential.", r"$q \propto R$."],
      [r"equal charges would give unequal potentials.", r"makes charge proportional to surface area, $R^2$.", r"inverts the ratio; that is the ratio of surface charge densities."]),
])

S3 = Sec("Capacitors (10.3)", ["10.3"], r"""
\[ C = \frac{Q}{\Delta V}, \qquad U_C = \tfrac12 C(\Delta V)^2 = \frac{Q^2}{2C} = \tfrac12 Q\Delta V, \qquad u_E = \tfrac12\varepsilon_0E^2. \]
To find $C$ for any shape: put $\pm Q$ on the conductors, find $E$ (Gauss's law), integrate to get $\Delta V$, and divide.
\begin{compare}{Capacitor}{$C$}{Notes}
Parallel plates, area $A$, gap $d$ & $\varepsilon_0A/d$ & uniform $E = \sigma/\varepsilon_0$ between plates \\
Spherical, radii $a < b$ & $4\pi\varepsilon_0\dfrac{ab}{b - a}$ & isolated sphere: $b \to \infty$, $C = 4\pi\varepsilon_0 a$ \\
Cylindrical, radii $a < b$, length $L$ & $\dfrac{2\pi\varepsilon_0 L}{\ln(b/a)}$ & coaxial cable \\
\end{compare}
\textbf{Combinations.} Parallel: $C_{eq} = C_1 + C_2$ (same $\Delta V$, charges add). Series: $\dfrac{1}{C_{eq}} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$ (same $Q$, voltages add).
\begin{keyidea}[Connected or isolated?]
Connected to a battery, $\Delta V$ is fixed: changing $C$ changes $Q$. Disconnected (isolated), $Q$ is fixed: changing $C$ changes $\Delta V$. Decide which before you calculate anything.
\end{keyidea}
""", checks=[
    Q("10.3 Parallel-plate capacitance", r"The gap between the plates of a parallel-plate capacitor is doubled. What happens to its capacitance?",
      r"It halves.", [r"It doubles.", r"It quarters.", r"It is unchanged."],
      r"$C = \varepsilon_0A/d \propto 1/d$.",
      [r"Doubling $d$ halves $C$."],
      [r"inverts the dependence.", r"treats $d$ as squared.", r"capacitance depends on geometry, and the gap is part of it."]),
    Q("10.3 Series capacitors", r"Capacitors of $2.0\ \mu\mathrm{F}$ and $3.0\ \mu\mathrm{F}$ are connected in series. What is the equivalent capacitance?",
      r"$1.2\ \mu\mathrm{F}$", [r"$5.0\ \mu\mathrm{F}$", r"$2.5\ \mu\mathrm{F}$", r"$0.83\ \mu\mathrm{F}$"],
      r"$\dfrac{1}{C} = \dfrac12 + \dfrac13 = \dfrac56$, so $C = 1.2\ \mu\mathrm{F}$, smaller than either.",
      [r"Series: reciprocals add.", r"$C = (2.0)(3.0)/(2.0 + 3.0) = 1.2\ \mu\mathrm{F}$."],
      [r"is the parallel combination.", r"is the average.", r"is $1/C$, the reciprocal, not inverted back."], sort=True),
    Q("10.3 Energy stored", r"A $10\ \mu\mathrm{F}$ capacitor is charged to 12 V. How much energy does it store?",
      r"$7.2\times10^{-4}$ J", [r"$1.4\times10^{-3}$ J", r"$6.0\times10^{-5}$ J", r"$1.2\times10^{-4}$ J"],
      r"$U = \tfrac12 CV^2 = \tfrac12(10\times10^{-6})(144) = 7.2\times10^{-4}$ J.",
      [r"$V^2 = 144\ \mathrm{V^2}$.", r"$U = 0.72$ mJ."],
      [r"forgets the $\tfrac12$.", r"is $\tfrac12 CV$, missing a factor of $V$.", r"is $Q = CV$, the charge in coulombs."], sort=True),
])

S4 = Sec("Dielectrics (10.4)", ["10.4"], r"""
An insulating material (dielectric constant $\kappa > 1$) between the plates polarizes. Its bound surface charges partly cancel the plates' field, so for the same free charge the voltage is lower:
\[ C = \kappa C_0, \qquad E = \frac{E_0}{\kappa}\ \ (\text{same free charge}). \]
\begin{compare}{Dielectric inserted}{Battery connected ($V$ fixed)}{Isolated ($Q$ fixed)}
$C$ & $\times\kappa$ & $\times\kappa$ \\
$Q$ & $\times\kappa$ & unchanged \\
$V$ & unchanged & $\div\kappa$ \\
$U$ & $\times\kappa$ ($\tfrac12 CV^2$) & $\div\kappa$ ($Q^2/2C$); the slab is pulled in \\
\end{compare}
A slab filling half the \emph{area} acts as two capacitors in parallel; a slab filling half the \emph{gap} acts as two in series.
""", checks=[
    Q("10.4 Isolated capacitor", r"A charged parallel-plate capacitor is disconnected from its battery. A slab with dielectric constant $\kappa$ then fills the gap. What happens to the voltage across it?",
      r"It decreases by a factor of $\kappa$.", [r"It increases by a factor of $\kappa$.", r"It is unchanged.", r"It decreases by a factor of $\kappa^2$."],
      r"Isolated: $Q$ is fixed. $C$ rises to $\kappa C_0$, so $V = Q/C$ falls by $\kappa$.",
      [r"$V = Q/(\kappa C_0) = V_0/\kappa$."],
      [r"reverses the effect of a larger $C$.", r"would hold if the battery stayed connected.", r"double counts the factor."]),
])

QS1 = [
    Q("10.1 Conducting shell", r"A point charge $+q$ sits at the center of a thick, neutral, conducting spherical shell. What charges appear on the shell's inner and outer surfaces?",
      r"Inner: $-q$; outer: $+q$", [r"Inner: $0$; outer: $0$", r"Inner: $+q$; outer: $-q$", r"Inner: $-q$; outer: $0$"],
      r"A Gaussian sphere inside the metal has $E = 0$, so it encloses zero net charge: the inner surface carries $-q$. The shell is neutral, so $+q$ goes to the outer surface.",
      [r"$Q_{enc} = q + q_{inner} = 0 \Rightarrow q_{inner} = -q$.", r"$q_{inner} + q_{outer} = 0 \Rightarrow q_{outer} = +q$."],
      [r"ignores the induced charge; the field inside the metal would then not be zero.", r"has the signs reversed; the inner surface must attract toward the center charge.", r"violates the shell's neutrality."]),
    Q("10.1 Field at a conductor's surface", r"A conductor's surface carries charge density $\sigma$ at some point. What is the field just outside the surface there?",
      r"$\sigma/\varepsilon_0$, perpendicular to the surface", [r"$\sigma/(2\varepsilon_0)$, perpendicular to the surface", r"$\sigma/\varepsilon_0$, parallel to the surface", r"$0$"],
      r"A pillbox with one face inside the metal ($E = 0$) and one just outside gives $EA = \sigma A/\varepsilon_0$. Any parallel component would move surface charges, so the field is perpendicular.",
      [r"Flux only through the outer face: $EA$.", r"$E = \sigma/\varepsilon_0$."],
      [r"is the field of an isolated sheet, whose field points out from both sides.", r"a parallel field would push surface charges along; in equilibrium it is zero.", r"the field is zero inside the metal, not just outside it."]),
    Q("10.1 Potential inside a conductor", r"A metal sphere of radius $R$ carries charge $Q$. What is the electric potential at a point a distance $r < R$ from its center?",
      r"$kQ/R$", [r"$0$", r"$kQ/r$", r"$kQr/R^3$"],
      r"$E = 0$ inside, so $V$ does not change from the surface inward: it stays $kQ/R$.",
      [r"Outside: $V = kQ/r$. At the surface: $kQ/R$.", r"Inside: $\Delta V = -\int E\,dr = 0$."],
      [r"zero field does not mean zero potential.", r"applies the outside formula inside, where no field drives $V$ up.", r"has the form of the field inside a uniformly charged insulator, not a potential."]),
    Q("10.2 Sharing charge", r"Metal spheres of radii 0.10 m and 0.30 m, far apart, are joined by a thin wire and share a total charge of $8.0\ \mu\mathrm{C}$. What charge ends up on the smaller sphere?",
      r"$2.0\ \mu\mathrm{C}$", [r"$4.0\ \mu\mathrm{C}$", r"$0.80\ \mu\mathrm{C}$", r"$6.0\ \mu\mathrm{C}$"],
      r"Equal potentials make $q \propto R$: $q_1/q_2 = 1/3$, so $q_1 = \tfrac14(8.0) = 2.0\ \mu\mathrm{C}$.",
      [r"$q_1 + q_2 = 8.0$, $q_2 = 3q_1$.", r"$q_1 = 2.0\ \mu\mathrm{C}$, $q_2 = 6.0\ \mu\mathrm{C}$."],
      [r"splits the charge equally.", r"makes charge proportional to $R^2$: $8.0 \times 1/10$.", r"is the larger sphere's charge."], sort=True),
    Q("10.2 Surface field", r"For the two joined spheres in the previous question, which has the stronger electric field just outside its surface?",
      r"The smaller sphere", [r"The larger sphere", r"They are equal, because they are at the same potential", r"Neither; the field outside a conductor is zero"],
      r"$E_{surface} = kq/R^2$ and $q \propto R$, so $E \propto 1/R$: three times stronger on the small sphere.",
      [r"$E_1/E_2 = (q_1/R_1^2)/(q_2/R_2^2) = (1/3)(9) = 3$."],
      [r"more charge does not mean more field; the charge is spread over a much larger area.", r"equal potentials do not give equal fields; $V = ER$ at the surface.", r"the field is zero inside, not outside."]),
    Q("10.3 Parallel-plate capacitance", r"A parallel-plate capacitor has plates of area $0.020\ \mathrm{m^2}$ separated by 1.0 mm of air. What is its capacitance? ($\varepsilon_0 = 8.85\times10^{-12}\ \mathrm{C^2/(N\,m^2)}$)",
      r"$180$ pF", [r"$18$ pF", r"$1.8$ pF", r"$1800$ pF"],
      r"$C = \varepsilon_0A/d = (8.85\times10^{-12})(0.020)/(1.0\times10^{-3}) = 1.8\times10^{-10}$ F $= 180$ pF.",
      [r"$\varepsilon_0A = 1.77\times10^{-13}$.", r"Divide by $10^{-3}$ m: $1.77\times10^{-10}$ F."],
      [r"uses $d = 1.0$ cm.", r"uses $d = 0.10$ m.", r"uses $d = 0.10$ mm."], sort=True),
    Q("10.3 Spherical capacitor", r"A spherical capacitor has an inner conductor of radius $a$ and an outer shell of radius $b$. What is its capacitance?",
      r"$4\pi\varepsilon_0\dfrac{ab}{b - a}$", [r"$4\pi\varepsilon_0(b - a)$", r"$\dfrac{\varepsilon_0 4\pi b^2}{b - a}$", r"$4\pi\varepsilon_0\dfrac{b - a}{ab}$"],
      r"With $\pm Q$, $E = kQ/r^2$ between the spheres, so $\Delta V = kQ\left(\dfrac1a - \dfrac1b\right) = kQ\dfrac{b - a}{ab}$ and $C = Q/\Delta V$.",
      [r"$\Delta V = \int_a^b \dfrac{kQ}{r^2}dr$.", r"$C = \dfrac{ab}{k(b - a)} = 4\pi\varepsilon_0\dfrac{ab}{b - a}$."],
      [r"has the wrong units (it is missing an area over a length).", r"treats it as parallel plates of the outer area; that works only when $b - a \ll a$ and with the area $4\pi ab$.", r"is $1/C$ scaled; it is upside down."]),
    Q("10.3 Combining capacitors", r"A $4.0\ \mu\mathrm{F}$ and a $2.0\ \mu\mathrm{F}$ capacitor are in parallel, and that pair is in series with a $3.0\ \mu\mathrm{F}$ capacitor. What is the equivalent capacitance?",
      r"$2.0\ \mu\mathrm{F}$", [r"$9.0\ \mu\mathrm{F}$", r"$1.3\ \mu\mathrm{F}$", r"$4.5\ \mu\mathrm{F}$"],
      r"Parallel pair: $6.0\ \mu\mathrm{F}$. In series with 3.0: $\dfrac{(6.0)(3.0)}{9.0} = 2.0\ \mu\mathrm{F}$.",
      [r"$4.0 + 2.0 = 6.0\ \mu\mathrm{F}$.", r"$1/C = 1/6 + 1/3 = 1/2$."],
      [r"adds all three, as if all in parallel.", r"puts all three in series.", r"averages the parallel pair and the third capacitor, $(6.0 + 3.0)/2$."], sort=True),
    Q("10.3 Energy when the gap changes", r"A charged parallel-plate capacitor is disconnected from its battery, and then its plate separation is doubled. What happens to its stored energy?",
      r"It doubles.", [r"It halves.", r"It is unchanged.", r"It quadruples."],
      r"Isolated, so $Q$ is fixed; $C$ halves; $U = Q^2/(2C)$ doubles. The extra energy is the work done pulling the attracting plates apart.",
      [r"$C \to C/2$.", r"$U = Q^2/2C \to 2U$."],
      [r"uses $\tfrac12 CV^2$ with $V$ held fixed, which applies only with the battery connected.", r"ignores that pulling the plates apart takes work.", r"double counts."]),
    Q("10.3 Energy density", r"The field between a capacitor's plates is $1.0\times10^6$ V/m (air). What is the energy density of the field?",
      r"$4.4\ \mathrm{J/m^3}$", [r"$8.9\ \mathrm{J/m^3}$", r"$4.4\times10^{-6}\ \mathrm{J/m^3}$", r"$0.50\ \mathrm{J/m^3}$"],
      r"$u = \tfrac12\varepsilon_0E^2 = \tfrac12(8.85\times10^{-12})(10^{12}) = 4.4\ \mathrm{J/m^3}$.",
      [r"$E^2 = 10^{12}\ \mathrm{V^2/m^2}$."],
      [r"forgets the $\tfrac12$.", r"uses $E$ instead of $E^2$.", r"leaves out $\varepsilon_0$ and the powers of ten; the units do not work."], sort=True),
    Q("10.4 Dielectric with battery connected", r"A capacitor stays connected to a battery while a slab of dielectric constant 3 is slid in to fill the gap. Which is true afterward?",
      r"The charge triples and the voltage is unchanged.", [r"The voltage drops to one third and the charge is unchanged.", r"Both the charge and the voltage triple.", r"The charge drops to one third and the voltage is unchanged."],
      r"The battery holds $V$ fixed. $C$ triples, so $Q = CV$ triples; the battery supplies the extra charge.",
      [r"$V$ fixed by the battery.", r"$Q = (3C_0)V = 3Q_0$."],
      [r"describes an isolated capacitor.", r"the battery fixes the voltage.", r"a larger $C$ at the same $V$ means more charge."]),
    Q("10.4 Partially filled capacitor", r"A slab of dielectric constant $\kappa = 3$ fills the left half of the area between a parallel-plate capacitor's plates, across the full gap. The empty capacitor had capacitance $C_0$. What is the new capacitance?",
      r"$2C_0$", [r"$3C_0$", r"$1.5C_0$", r"$4C_0$"],
      r"Each half has area $A/2$ and the full gap, so the halves are in parallel: $C = \tfrac12 C_0 + \tfrac12\kappa C_0 = 2C_0$.",
      [r"Empty half: $C_0/2$. Filled half: $3C_0/2$.", r"Parallel: $2C_0$."],
      [r"assumes the whole gap is filled.", r"treats the halves as in series ($\kappa/(1 + \kappa) \cdot 2C_0$).", r"adds $\kappa C_0$ to the full $C_0$."]),
]

UNIT = Unit(
    n=10, slug="conductors-capacitors", title="Conductors and Capacitors", weight="10--15\\%", topics="10.1--10.4",
    abstract=r"""Unit 10 applies fields and potential to conductors and to the devices built from them. It covers conductors in electrostatic equilibrium and shielding (10.1); how charge redistributes between connected conductors (10.2); capacitance of parallel-plate, spherical, and cylindrical capacitors, energy storage, and series and parallel combinations (10.3); and dielectrics (10.4). The recurring question is whether the charge or the voltage is held fixed. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4],
    qsections=[("Conductors (10.1--10.2)", QS1[:5]), ("Capacitors (10.3)", QS1[5:10]), ("Dielectrics (10.4)", QS1[10:])],
    frq=FRQ("Translation Between Representations", 12, r"""An air-filled parallel-plate capacitor with plate area $A$ and gap $d$ is charged by a battery of voltage $V_0$. The battery is then disconnected. An insulating handle is used to pull the plates apart slowly, from separation $d$ to $2d$. Ignore edge effects.""", [
        Part("a", 2, r"Draw the capacitor at separation $d$, showing the sign of the charge on each plate and the electric field lines between and outside the plates.",
             r"1 pt: $+$ on one plate, $-$ on the other. 1 pt: evenly spaced parallel lines from $+$ to $-$ between the plates, and no field outside.",
             r"Field lines that curve or bunch between the plates, or that extend outside."),
        Part("b", 4, r"On three separate sets of axes, sketch graphs of the charge $Q$, the voltage $\Delta V$, and the field magnitude $E$ between the plates, each as a function of the separation $x$ for $d \le x \le 2d$. Label the starting and ending values in terms of $V_0$ and the starting values.",
             r"1 pt: $Q$ is a horizontal line at $Q_0 = \varepsilon_0AV_0/d$ (isolated). 1 pt: $\Delta V$ rises linearly from $V_0$ to $2V_0$ ($\Delta V = Q_0x/(\varepsilon_0A)$). 1 pt: $E$ is a horizontal line at $V_0/d$ ($E = \sigma/\varepsilon_0$ is set by the fixed charge). 1 pt: all endpoints labeled correctly.",
             r"Drawing $\Delta V$ constant, as if the battery were still connected."),
        Part("c", 3, r"Derive an expression for the work done by the person pulling the plates from $d$ to $2d$, in terms of $A$, $d$, $V_0$, and physical constants.",
             r"1 pt: $W = \Delta U$ (slow pull, no kinetic energy). 1 pt: $U_1 = \tfrac12 C_0V_0^2$, $U_2 = \dfrac{Q_0^2}{2(C_0/2)} = C_0V_0^2$. 1 pt: $W = \tfrac12 C_0V_0^2 = \dfrac{\varepsilon_0AV_0^2}{2d}$. (Equivalently: constant force $Q_0E/2$ on a plate times distance $d$.)",
             r"Using $U = \tfrac12 CV^2$ with $V$ held at $V_0$, which gives a decrease in energy."),
        Part("d", 3, r"Suppose instead the battery stays connected while the plates are pulled from $d$ to $2d$. Describe how each of your three graphs in (b) would change, and state whether the capacitor's stored energy increases or decreases. Justify.",
             r"1 pt: $\Delta V$ is now constant at $V_0$. 1 pt: $Q = CV_0$ falls to $Q_0/2$ (as $1/x$), and $E = V_0/x$ falls to $V_0/(2d)$. 1 pt: stored energy $\tfrac12 CV_0^2$ decreases (to half), because $C$ halves at fixed voltage; charge flows back into the battery.",
             r"Saying the energy increases because work is done on the plates; the battery absorbs energy as well."),
    ]),
    frq_topic="pulling apart the plates of an isolated capacitor",
)
