from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Magnetic flux, Faraday's law, and Lenz's law (13.1--13.2)", ["13.1", "13.2"], r"""
\[ \Phi_B = \int\vec B\cdot d\vec A\ \ (= BA\cos\theta \text{ for uniform } B), \qquad \varepsilon = -N\frac{d\Phi_B}{dt}, \qquad \oint\vec E\cdot d\vec l = -\frac{d\Phi_B}{dt}. \]
An emf is induced whenever the flux through a loop changes: by changing $B$, the area, or the angle. \textbf{Lenz's law} sets the direction: the induced current makes a field that opposes the \emph{change} in flux (not the flux itself).
\begin{terms}
Motional emf & A rod of length $L$ moving at $v$ perpendicular to $B$: $\varepsilon = BLv$. The magnetic force on its charges drives them along the rod. \\
Generator & A coil of $N$ turns and area $A$ spinning at $\omega$: $\varepsilon = NBA\omega\sin\omega t$, peak $NBA\omega$. \\
Induced electric field & A changing $B$ creates a circulating $\vec E$ even with no wire present. Inside a solenoid of radius $R$, $E = \dfrac{r}{2}\dfrac{dB}{dt}$ for $r < R$. \\
\end{terms}
\begin{keyidea}[Lenz's law in three steps]
(1) Which way does the external field point through the loop, and is its flux increasing or decreasing? (2) The induced field points opposite if increasing, the same way if decreasing. (3) Right-hand rule: curl your fingers with the current so your thumb points along the induced field.
\end{keyidea}
""", checks=[
    Q("13.1 Magnetic flux", r"A loop of area $0.050\ \mathrm{m^2}$ sits in a uniform 0.40 T field that makes a $60^\circ$ angle with the loop's normal. What is the flux through it?",
      r"$0.010$ Wb", [r"$0.020$ Wb", r"$0.017$ Wb", r"$8.0$ Wb"],
      r"$\Phi = BA\cos\theta = (0.40)(0.050)\cos 60^\circ = 0.010$ Wb.",
      [r"$BA = 0.020$ Wb; times $\cos 60^\circ = 0.50$."],
      [r"assumes the field is along the normal.", r"uses $\sin 60^\circ$.", r"divides $B$ by $A$."], sort=True),
    Q("13.2 Lenz's law", r"The north pole of a bar magnet is pushed toward a loop of wire. Seen from the magnet's side, which way does the induced current circulate?",
      r"Counterclockwise", [r"Clockwise", r"There is no current, because the magnet does not touch the loop", r"It alternates direction"],
      r"The magnet's field points away from its north pole, through the loop, and grows as the magnet approaches. The loop opposes the increase by making its own field pointing back toward the magnet: seen from the magnet, that is counterclockwise (the loop's near face becomes a north pole and repels).",
      [r"External field through the loop: away from the magnet, increasing.", r"Induced field: toward the magnet.", r"Right-hand rule seen from the magnet: counterclockwise."],
      [r"would strengthen the increasing flux, which Lenz's law forbids.", r"changing flux induces a current; no contact is needed.", r"the flux only increases while the magnet approaches, so the current keeps one direction."]),
])

S2 = Sec("Induced currents and magnetic forces (13.3)", ["13.3"], r"""
An induced current in a magnetic field feels a force, and Lenz's law guarantees that force opposes the motion that caused it: magnetic braking.

\begin{example}[Rod on rails]
A rod of length $L$ slides at $v$ on frictionless rails joined by a resistor $R$, in a field $B$ perpendicular to the plane. Then $\varepsilon = BLv$, $I = BLv/R$, and the field pushes back on the rod with $F = ILB = \dfrac{B^2L^2v}{R}$. Keeping $v$ constant requires a pulling force of that size, and its power $Fv = \dfrac{B^2L^2v^2}{R} = I^2R$ appears as heat in the resistor. Left alone, the rod slows exponentially: $m\,\dfrac{dv}{dt} = -\dfrac{B^2L^2}{R}v$.
\end{example}
A magnet falling through a copper tube or a loop falling out of a field is slowed the same way, and reaches a terminal speed where the magnetic force balances gravity.
""", checks=[
    Q("13.2 Motional emf", r"A 0.50 m rod moves at 4.0 m/s perpendicular to a 0.20 T field. What emf is induced between its ends?",
      r"$0.40$ V", [r"$0.80$ V", r"$0.10$ V", r"$2.0$ V"],
      r"$\varepsilon = BLv = (0.20)(0.50)(4.0) = 0.40$ V.",
      [r"Multiply the three perpendicular quantities."],
      [r"leaves out the length: $Bv = 0.80$.", r"leaves out the speed: $BL = 0.10$.", r"leaves out the field: $Lv = 2.0$."], sort=True),
])

S3 = Sec("Inductance (13.4)", ["13.4"], r"""
A coil opposes changes in its own current. Its self-inductance $L$ links flux to current:
\[ L = \frac{N\Phi_B}{I}, \qquad \varepsilon_L = -L\frac{dI}{dt}, \qquad U_L = \tfrac12 LI^2, \qquad u_B = \frac{B^2}{2\mu_0}. \]
For a long solenoid of $N$ turns, length $\ell$, and area $A$: $L = \mu_0 N^2A/\ell$. The unit is the henry, $1\ \mathrm{H} = 1\ \mathrm{V\,s/A}$.
\begin{trap}
An inductor resists \emph{changes} in current, not current itself. It has no voltage across it when its current is steady (an ideal inductor is then just a wire).
\end{trap}
""", checks=[
    Q("13.4 Energy in an inductor", r"A 2.0 H inductor carries a steady 3.0 A. How much energy is stored in its magnetic field?",
      r"$9.0$ J", [r"$18$ J", r"$6.0$ J", r"$3.0$ J"],
      r"$U = \tfrac12 LI^2 = \tfrac12(2.0)(9.0) = 9.0$ J.",
      [r"$I^2 = 9.0\ \mathrm{A^2}$."],
      [r"forgets the $\tfrac12$.", r"is $LI$, the flux linkage, not an energy.", r"is $\tfrac12 LI$, missing a factor of $I$."], sort=True),
])

S4 = Sec("LR circuits (13.5)", ["13.5"], r"""
In a series circuit of a battery $\varepsilon$, resistor $R$, and inductor $L$, the loop rule gives $\varepsilon - IR - L\,\dfrac{dI}{dt} = 0$, so
\[ I(t) = \frac{\varepsilon}{R}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac{L}{R}; \qquad \text{when the battery is removed: } I = I_0e^{-t/\tau}. \]
\begin{compare}{Moment}{Inductor acts like}{Current}
Just after the switch closes & an open circuit (its current cannot jump) & zero; $\Delta V_L = \varepsilon$ \\
Long after & a plain wire & $\varepsilon/R$; $\Delta V_L = 0$ \\
\end{compare}
These are the opposite of a capacitor's: a capacitor starts as a wire and ends as a break.
""", checks=[
    Q("13.5 LR time constant", r"A 0.50 H inductor is in series with a $10\ \Omega$ resistor and a battery. What is the circuit's time constant?",
      r"$0.050$ s", [r"$5.0$ s", r"$20$ s", r"$0.50$ s"],
      r"$\tau = L/R = 0.50/10 = 0.050$ s.",
      [r"Units: H/$\Omega$ = s."],
      [r"is $LR$, the RC-style product.", r"is $R/L$, upside down.", r"is $L$ alone."], sort=True),
])

S5 = Sec("LC circuits (13.6)", ["13.6"], r"""
A charged capacitor connected across an inductor (no resistance) oscillates: energy passes back and forth between the capacitor's electric field and the inductor's magnetic field.
\[ \frac{d^2q}{dt^2} = -\frac{1}{LC}q, \qquad \omega = \frac{1}{\sqrt{LC}}, \qquad q = Q_0\cos\omega t, \qquad I_{max} = \omega Q_0, \qquad \frac{Q_0^2}{2C} = \tfrac12 LI_{max}^2. \]
This is the mass--spring oscillator again, with $q \leftrightarrow x$, $L \leftrightarrow m$, and $1/C \leftrightarrow k$. When the capacitor's charge is zero, the current is maximum, and vice versa.
""", checks=[
    Q("13.6 LC frequency", r"An LC circuit has $L = 0.10$ H and $C = 10\ \mu\mathrm{F}$. What is its angular frequency of oscillation?",
      r"$1000$ rad/s", [r"$160$ rad/s", r"$1.0\times10^{6}$ rad/s", r"$1.0\times10^{-3}$ rad/s"],
      r"$\omega = 1/\sqrt{LC} = 1/\sqrt{1.0\times10^{-6}} = 1000$ rad/s.",
      [r"$LC = (0.10)(1.0\times10^{-5}) = 1.0\times10^{-6}\ \mathrm{s^2}$."],
      [r"is the frequency $f = \omega/2\pi$ in Hz.", r"is $1/(LC)$, missing the square root.", r"is $\sqrt{LC}$, upside down."], sort=True),
])

QS1 = [
    Q("13.2 Faraday's law", r"A 20-turn circular coil of radius 0.10 m lies perpendicular to a uniform field $B(t) = 0.20 + 0.30t$ (tesla, seconds). What emf is induced in the coil at $t = 1.0$ s?",
      r"$0.19$ V", [r"$0.0094$ V", r"$1.9$ V", r"$0.31$ V"],
      r"$\varepsilon = NA\,\dfrac{dB}{dt} = (20)(\pi)(0.10)^2(0.30) = 0.19$ V, the same at every instant.",
      [r"$A = \pi r^2 = 0.0314\ \mathrm{m^2}$.", r"$dB/dt = 0.30$ T/s.", r"$\varepsilon = 20(0.0314)(0.30) = 0.188$ V."],
      [r"counts only one turn.", r"uses $\pi r$ instead of $\pi r^2$ for the area.", r"uses $B(1) = 0.50$ T instead of $dB/dt$; emf comes from the rate of change."], sort=True),
    Q("13.2 Lenz's law near a wire", r"A long straight wire carries a steady current upward (toward the top of the page). A rectangular loop to its right, in the plane of the page, moves away from the wire to the right. What is the direction of the induced current in the loop?",
      r"Clockwise", [r"Counterclockwise", r"No current; the wire's current is steady", r"Clockwise on the near side and counterclockwise on the far side"],
      r"To the right of an upward current, $\vec B$ points into the page. Moving away, the loop's inward flux decreases. The induced current tries to keep it, making an into-page field inside the loop: clockwise.",
      [r"External field: into the page, weakening.", r"Induced field: into the page.", r"Right-hand rule: clockwise."],
      [r"would oppose the existing flux instead of the change.", r"the flux through the moving loop changes even though the current is steady.", r"a single loop carries one current all the way around."]),
    Q("13.2 Generator", r"A 100-turn coil of area $0.020\ \mathrm{m^2}$ spins at 60 rad/s in a 0.50 T field. What is the peak emf?",
      r"$60$ V", [r"$0.60$ V", r"$9.5$ V", r"$120$ V"],
      r"$\varepsilon_{max} = NBA\omega = (100)(0.50)(0.020)(60) = 60$ V.",
      [r"$\Phi = NBA\cos\omega t$, so $\varepsilon = NBA\omega\sin\omega t$."],
      [r"counts only one turn.", r"uses the frequency in Hz ($60/2\pi$) in place of $\omega$.", r"doubles the peak; the emf swings from $-60$ to $+60$ V, a 120 V range."], sort=True),
    Q("13.2 Induced electric field", r"The uniform field inside a long solenoid of radius $R$ is increasing at the rate $dB/dt$. What is the magnitude of the induced electric field at a distance $r < R$ from the axis?",
      r"$\dfrac{r}{2}\dfrac{dB}{dt}$", [r"$r\dfrac{dB}{dt}$", r"$\dfrac{R^2}{2r}\dfrac{dB}{dt}$", r"$0$"],
      r"$\oint\vec E\cdot d\vec l = E(2\pi r) = \dfrac{d}{dt}(B\pi r^2)$, so $E = \dfrac{r}{2}\dfrac{dB}{dt}$.",
      [r"Circular path of radius $r$; flux $B\pi r^2$.", r"$E = \dfrac{\pi r^2}{2\pi r}\dfrac{dB}{dt}$."],
      [r"drops the factor of $\tfrac12$ from $\pi r^2/2\pi r$.", r"is the field outside the solenoid ($r > R$).", r"a changing magnetic field induces an electric field even where there is no wire."]),
    Q("13.2 Motional emf", r"A 0.40 m metal rod slides at 5.0 m/s across rails, perpendicular to a 0.50 T field. What emf is induced?",
      r"$1.0$ V", [r"$0.20$ V", r"$2.0$ V", r"$2.5$ V"],
      r"$\varepsilon = BLv = (0.50)(0.40)(5.0) = 1.0$ V.",
      [r"Flux through the circuit grows at $BLv$."],
      [r"leaves out the speed: $BL$.", r"leaves out the field: $Lv$.", r"leaves out the length: $Bv$."], sort=True),
    Q("13.3 Force on the rod", r"The rails in the previous question are joined by a $2.0\ \Omega$ resistor (the rod and rails have negligible resistance). What force must be applied to keep the rod moving at a constant 5.0 m/s?",
      r"$0.10$ N", [r"$0.50$ N", r"$0.25$ N", r"$0$"],
      r"$I = \varepsilon/R = 0.50$ A, and the field pushes back on the rod with $ILB = (0.50)(0.40)(0.50) = 0.10$ N, which the applied force must balance.",
      [r"$I = 1.0/2.0 = 0.50$ A.", r"$F = ILB = 0.10$ N. Check: $Fv = 0.50$ W $= I^2R$."],
      [r"is the power $I^2R$ in watts, not a force.", r"is $IB$, leaving out the rod's length.", r"constant velocity needs zero \emph{net} force; the applied force must cancel the magnetic drag."], sort=True),
    Q("13.3 Terminal speed", r"A horizontal rod of mass $m$ and length $L$ slides down frictionless vertical rails joined at the top by a resistor $R$, in a horizontal field $B$ perpendicular to the rails' plane. What is its terminal speed?",
      r"$\dfrac{mgR}{B^2L^2}$", [r"$\dfrac{mg}{BL}$", r"$\dfrac{mgR}{BL}$", r"$\sqrt{\dfrac{mgR}{B^2L^2}}$"],
      r"At terminal speed the magnetic force balances gravity: $\dfrac{B^2L^2v}{R} = mg$.",
      [r"$I = BLv/R$; $F = ILB = B^2L^2v/R$.", r"Set equal to $mg$."],
      [r"is a current ($mg = ILB$), not a speed.", r"is the induced emf at terminal speed, in volts.", r"comes from a drag force $\propto v^2$; the magnetic drag here is $\propto v$."]),
    Q("13.3 Magnetic braking", r"A strong magnet is dropped down a vertical copper pipe and falls much more slowly than a dropped stone. Why?",
      r"Its moving field induces currents in the copper whose fields oppose its motion.", [r"The copper is attracted to the magnet like iron.", r"Air trapped in the pipe slows the magnet.", r"The copper shields the magnet from Earth's gravity."],
      r"As the magnet falls, the flux through each ring of copper changes; the induced (eddy) currents make fields that repel the approaching pole and attract the departing one, both opposing the fall.",
      [r"Changing flux $\Rightarrow$ eddy currents.", r"Lenz's law: their fields oppose the change, slowing the magnet."],
      [r"copper is not ferromagnetic; a stationary magnet does not stick to it.", r"the effect happens in an open pipe and depends on the metal's conductivity.", r"nothing shields gravity."]),
    Q("13.4 Solenoid inductance", r"A solenoid has 500 turns, length 0.25 m, and cross-sectional area $4.0\times10^{-4}\ \mathrm{m^2}$. What is its self-inductance? ($\mu_0 = 4\pi\times10^{-7}$ T$\cdot$m/A)",
      r"$5.0\times10^{-4}$ H", [r"$1.0\times10^{-6}$ H", r"$3.1\times10^{-5}$ H", r"$2.0\times10^{-3}$ H"],
      r"$L = \mu_0N^2A/\ell = (4\pi\times10^{-7})(2.5\times10^5)(4.0\times10^{-4})/0.25 = 5.0\times10^{-4}$ H.",
      [r"$N^2 = 2.5\times10^5$.", r"$L = 0.50$ mH."],
      [r"uses $N$ instead of $N^2$.", r"multiplies by the length instead of dividing.", r"divides by $\ell^2$."], sort=True),
    Q("13.4 Self-induced emf", r"The current in a 0.20 H inductor is decreasing at 50 A/s. What is the induced emf?",
      r"10 V, in the direction that tends to keep the current flowing", [r"10 V, opposing the current", r"250 V, in the direction that tends to keep the current flowing", r"4.0 mV, opposing the current"],
      r"$|\varepsilon| = L|dI/dt| = (0.20)(50) = 10$ V. A falling current induces an emf that pushes the same way, to oppose the decrease.",
      [r"$\varepsilon = -L\,dI/dt$ with $dI/dt = -50$ A/s gives $+10$ V, along the current."],
      [r"has the size right but would apply to a growing current.", r"divides 50 by 0.20.", r"divides $L$ by $dI/dt$."]),
    Q("13.5 LR circuit", r"A 12 V battery, a $4.0\ \Omega$ resistor, and a 0.80 H inductor are connected in series at $t = 0$. What is the current at $t = 0.20$ s?",
      r"$1.9$ A", [r"$3.0$ A", r"$1.1$ A", r"$0$"],
      r"$\tau = L/R = 0.20$ s and $I_{final} = 3.0$ A. At $t = \tau$, $I = 3.0(1 - e^{-1}) = 1.9$ A.",
      [r"$I = \dfrac{\varepsilon}{R}(1 - e^{-t/\tau})$.", r"$3.0 \times 0.632 = 1.9$ A."],
      [r"is the final current.", r"is $3.0e^{-1}$, the decay law, not growth.", r"is the current only at $t = 0$."], sort=True),
    Q("13.5 Just after closing", r"In the LR circuit of the previous question, what is the voltage across the inductor immediately after the switch closes?",
      r"$12$ V", [r"$0$", r"$6.0$ V", r"$9.6$ V"],
      r"The current starts at zero, so there is no drop across the resistor; the whole emf appears across the inductor, which opposes the sudden change.",
      [r"$I(0) = 0 \Rightarrow \Delta V_R = 0$.", r"Loop rule: $\Delta V_L = \varepsilon = 12$ V."],
      [r"describes the inductor long after, when the current is steady.", r"splits the emf equally with no basis.", r"is $L\varepsilon$, which has no meaning here."], sort=True),
    Q("13.6 LC oscillation", r"A capacitor $C$ with charge $Q_0$ is connected across an inductor $L$ at $t = 0$. What is the maximum current in the circuit?",
      r"$\dfrac{Q_0}{\sqrt{LC}}$", [r"$Q_0\sqrt{LC}$", r"$\dfrac{Q_0}{LC}$", r"$\dfrac{Q_0}{2\sqrt{LC}}$"],
      r"Energy: $\dfrac{Q_0^2}{2C} = \tfrac12 LI_{max}^2$, so $I_{max} = Q_0/\sqrt{LC} = \omega Q_0$.",
      [r"All the capacitor's energy becomes inductor energy when $q = 0$."],
      [r"multiplies by $\sqrt{LC}$ instead of dividing.", r"has units of A/s.", r"puts in a stray $\tfrac12$."]),
]

UNIT = Unit(
    n=13, slug="electromagnetic-induction", title="Electromagnetic Induction", weight="10--20\\%", topics="13.1--13.6",
    abstract=r"""Unit 13 closes the course with changing magnetic flux. It covers magnetic flux and Faraday's and Lenz's laws, including motional emf, generators, and induced electric fields (13.1--13.2); forces on induced currents and magnetic braking (13.3); self-inductance and magnetic energy (13.4); LR circuits (13.5); and LC oscillations (13.6). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5],
    qsections=[("Faraday's and Lenz's laws (13.1--13.2)", QS1[:5]), ("Induced currents and forces (13.3)", QS1[5:8]), ("Inductance and LR, LC circuits (13.4--13.6)", QS1[8:])],
    frq=FRQ("Qualitative/Quantitative Translation", 8, r"""A square loop of wire with side length $s$ and resistance $R$ is pulled at constant speed $v$ to the right. It starts in a region with no magnetic field, moves completely into a region of uniform field $B$ directed into the page, travels through it, and then leaves on the far side. The field region is wider than the loop.""", [
        Part("a", 3, r"Without equations, describe the current in the loop (whether there is one and its direction) while it is entering the field, while it is entirely inside, and while it is leaving. Explain using the change in flux.",
             r"1 pt: entering: inward flux increases, so a counterclockwise current makes an outward field to oppose it. 1 pt: entirely inside: the flux is constant, so there is no current. 1 pt: leaving: inward flux decreases, so a clockwise current makes an inward field to oppose the decrease.",
             r"Saying the current is largest while the loop is fully inside, where $B$ is strongest."),
        Part("b", 3, r"Derive expressions for the current in the loop and the force needed to pull it at constant speed while it is entering the field.",
             r"1 pt: $\varepsilon = Bsv$ (only the leading edge cuts the field). 1 pt: $I = Bsv/R$. 1 pt: $F = IsB = \dfrac{B^2s^2v}{R}$, to the right (balancing the magnetic drag on the leading edge).",
             r"Including force on the top and bottom edges; those forces cancel."),
        Part("c", 2, r"The loop is now pulled at speed $2v$. Using your results, determine how the energy dissipated in the loop during entry changes, and explain why this agrees with your description in (a).",
             r"1 pt: energy $= F\cdot s = \dfrac{B^2s^3v}{R}$, which doubles at $2v$ (the force doubles over the same distance). 1 pt: faster entry changes the flux faster, so the induced emf and current are larger, as the reasoning in (a) implies; the time is halved but the power quadruples.",
             r"Saying the energy is unchanged because the flux change $Bs^2$ is the same."),
    ]),
    frq_topic="a square loop pulled through a magnetic field",
)
