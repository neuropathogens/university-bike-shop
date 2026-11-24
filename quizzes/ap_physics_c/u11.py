from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Current, resistance, and Ohm's law (11.1--11.3)", ["11.1", "11.2", "11.3"], r"""
\[ I = \frac{dQ}{dt}, \qquad R = \frac{\rho L}{A}, \qquad \Delta V = IR\ \ \text{(ohmic)}, \qquad J = \frac{I}{A} = nqv_d = \frac{E}{\rho}. \]
\begin{terms}
Current & Rate of charge flow, in amperes (C/s). Conventional current runs from $+$ to $-$ outside the battery; electrons drift the other way. \\
Drift velocity & Electrons drift slowly (mm/s), but the field that pushes them is set up along the wire almost instantly. \\
Resistivity $\rho$ & A property of the material (and temperature); resistance $R$ also depends on shape. \\
Ohmic & $I \propto \Delta V$ at fixed temperature; a straight $I$--$V$ graph through the origin. A light bulb filament is non-ohmic (its $R$ rises as it heats). \\
Simple circuit (11.2) & A closed conducting loop with a source of emf. A break anywhere stops the current everywhere in that loop. \\
\end{terms}
\begin{trap}
Stretching a wire to twice its length keeps its volume, so the area halves: $R = \rho L/A$ goes up by a factor of 4, not 2.
\end{trap}
""", checks=[
    Q("11.3 Stretching a wire", r"A wire is drawn out to twice its original length, its volume unchanged. By what factor does its resistance change?",
      r"$4$", [r"$2$", r"$1/2$", r"$1$"],
      r"$L \to 2L$ and, with fixed volume, $A \to A/2$. $R = \rho L/A \to \rho(2L)/(A/2) = 4R$.",
      [r"Volume $LA$ fixed: $A$ halves.", r"$R$ gains a factor 2 from length and 2 from area."],
      [r"accounts for the length but not the thinner cross-section.", r"inverts the effect.", r"the material is the same, but the shape is not."]),
])

S2 = Sec("Electric power (11.4)", ["11.4"], r"""
\[ P = I\Delta V = I^2R = \frac{(\Delta V)^2}{R}. \]
Pick the form that uses what is the \emph{same}: in series the current is shared, so $P = I^2R$ shows the bigger resistor dissipates more. In parallel the voltage is shared, so $P = V^2/R$ shows the smaller resistor dissipates more. The brightness of identical bulbs tracks the power each dissipates.
\begin{example}
A ``60 W, 120 V'' bulb has $R = 120^2/60 = 240\ \Omega$; a ``100 W'' bulb has $144\ \Omega$. In series across 120 V they share one current, so the 60 W bulb (larger $R$) glows brighter.
\end{example}
""", checks=[
    Q("11.4 Bulbs in series", r"A 60 W bulb and a 100 W bulb (both rated for 120 V) are connected in series across 120 V. Which glows brighter?",
      r"The 60 W bulb", [r"The 100 W bulb", r"They glow equally", r"Neither lights, because the voltage is split"],
      r"Rated power at 120 V fixes $R = V^2/P$: 240 $\Omega$ and 144 $\Omega$. In series the current is the same, so $P = I^2R$ is larger in the 240 $\Omega$ (60 W) bulb.",
      [r"$R_{60} = 240\ \Omega$, $R_{100} = 144\ \Omega$.", r"Same $I$: more power in the larger $R$."],
      [r"the 100 W rating applies only at the full 120 V across it.", r"equal current does not mean equal power when the resistances differ.", r"both carry current; each simply gets less than 120 V."]),
])

S3 = Sec("DC circuits and Kirchhoff's rules (11.5--11.7)", ["11.5", "11.6", "11.7"], r"""
\begin{compare}{}{Series}{Parallel}
Shared quantity & current & voltage \\
Equivalent resistance & $R_1 + R_2 + \cdots$ & $\left(\dfrac{1}{R_1} + \dfrac{1}{R_2} + \cdots\right)^{-1}$ \\
Adding a resistor & increases $R_{eq}$ & decreases $R_{eq}$ \\
\end{compare}
\textbf{Kirchhoff's loop rule (11.6):} around any closed loop, $\sum\Delta V = 0$ (energy conservation). Crossing a battery from $-$ to $+$ adds $\varepsilon$; crossing a resistor in the direction of the current subtracts $IR$.
\textbf{Junction rule (11.7):} current into a junction equals current out (charge conservation).

\textbf{Real batteries.} A battery with emf $\varepsilon$ and internal resistance $r$ has terminal voltage $\Delta V = \varepsilon - Ir$ while delivering current $I$. \textbf{Meters:} an ideal ammeter (zero resistance) goes in series; an ideal voltmeter (infinite resistance) goes in parallel.
\begin{keyidea}[Method for multi-loop circuits]
Label a current (with a guessed direction) in every branch. Write junction equations, then enough loop equations to have as many equations as unknowns. A negative answer just means the current flows opposite to your guess.
\end{keyidea}
""", checks=[
    Q("11.6 Terminal voltage", r"A battery with emf 12 V and internal resistance $0.50\ \Omega$ delivers 2.0 A to a circuit. What is the voltage across its terminals?",
      r"$11$ V", [r"$12$ V", r"$13$ V", r"$1.0$ V"],
      r"$\Delta V = \varepsilon - Ir = 12 - (2.0)(0.50) = 11$ V.",
      [r"Internal drop: $Ir = 1.0$ V.", r"Terminal voltage: $12 - 1.0 = 11$ V."],
      [r"ignores the internal resistance.", r"adds the internal drop; that happens only when the battery is being charged.", r"is the internal drop itself."], sort=True),
    Q("11.5 Equivalent resistance", r"Three $6.0\ \Omega$ resistors: two are in parallel, and that pair is in series with the third. What is the equivalent resistance?",
      r"$9.0\ \Omega$", [r"$18\ \Omega$", r"$2.0\ \Omega$", r"$4.0\ \Omega$"],
      r"Parallel pair: $6.0/2 = 3.0\ \Omega$. Plus 6.0 in series: $9.0\ \Omega$.",
      [r"Two equal resistors in parallel: half of one.", r"$3.0 + 6.0 = 9.0\ \Omega$."],
      [r"puts all three in series.", r"puts all three in parallel.", r"is the series third in parallel with the pair, the reverse arrangement."], sort=True),
])

S4 = Sec("RC circuits (11.8)", ["11.8"], r"""
A capacitor in a DC circuit charges or discharges exponentially with time constant $\tau = RC$.
\[ \text{Charging: } q(t) = C\varepsilon\left(1 - e^{-t/RC}\right), \qquad I(t) = \frac{\varepsilon}{R}e^{-t/RC}; \]
\[ \text{Discharging: } q(t) = Q_0e^{-t/RC}, \qquad I(t) = \frac{Q_0}{RC}e^{-t/RC}. \]
These come from the loop rule: charging, $\varepsilon - IR - q/C = 0$ with $I = dq/dt$, a separable differential equation.
\begin{compare}{Moment}{Uncharged capacitor acts like}{Current through its branch}
Just after the switch closes & a wire ($\Delta V_C = 0$) & maximum \\
Long after (steady state) & a break in the wire & zero; $\Delta V_C$ equals the voltage across its parallel branch \\
\end{compare}
After one $\tau$ a charging capacitor holds 63\% of its final charge and the current is 37\% of its initial value. The time to halve is $\tau\ln 2 = 0.69\tau$.
""", checks=[
    Q("11.8 Time constant", r"A $10\ \mathrm{k}\Omega$ resistor and a $100\ \mu\mathrm{F}$ capacitor are in series. What is the circuit's time constant?",
      r"$1.0$ s", [r"$0.10$ s", r"$10$ s", r"$1000$ s"],
      r"$\tau = RC = (1.0\times10^4)(1.0\times10^{-4}) = 1.0$ s.",
      [r"$10\ \mathrm{k}\Omega = 10^4\ \Omega$; $100\ \mu\mathrm{F} = 10^{-4}$ F."],
      [r"misplaces a power of ten.", r"misplaces a power of ten the other way.", r"uses the numbers without their prefixes, $10 \times 100$."], sort=True),
])

QS1 = [
    Q("11.1 Current as a derivative", r"The charge that has passed a point in a wire is $q(t) = 3t^2 + 2t$ (coulombs, seconds). What is the current at $t = 2.0$ s?",
      r"$14$ A", [r"$16$ A", r"$8.0$ A", r"$6.0$ A"],
      r"$I = dq/dt = 6t + 2 = 14$ A at $t = 2$.",
      [r"Differentiate: $I = 6t + 2$."],
      [r"is $q(2) = 12 + 4$, the charge in coulombs.", r"is the average current over the first 2.0 s, $16/2.0$.", r"is $dI/dt$, the rate of change of current, in A/s."], sort=True),
    Q("11.3 Resistance from resistivity", r"A nichrome wire ($\rho = 1.1\times10^{-6}\ \Omega\cdot\mathrm{m}$) is 2.0 m long with a diameter of 0.50 mm. What is its resistance?",
      r"$11\ \Omega$", [r"$2.8\ \Omega$", r"$45\ \Omega$", r"$8.8\ \Omega$"],
      r"$A = \pi r^2 = \pi(0.25\times10^{-3})^2 = 1.96\times10^{-7}\ \mathrm{m^2}$, so $R = \rho L/A = 11\ \Omega$.",
      [r"Radius $= 0.25$ mm.", r"$R = (1.1\times10^{-6})(2.0)/(1.96\times10^{-7}) = 11.2\ \Omega$."],
      [r"uses the diameter as the radius, making the area 4 times too big.", r"uses a radius of 0.125 mm, halving the radius twice.", r"uses $A = d^2$, the area of a square."], ),
    Q("11.4 Power", r"A space heater is rated at 1500 W when connected to 120 V. What is its resistance while operating?",
      r"$9.6\ \Omega$", [r"$12.5\ \Omega$", r"$0.080\ \Omega$", r"$1.8\times10^{5}\ \Omega$"],
      r"$R = V^2/P = 14400/1500 = 9.6\ \Omega$.",
      [r"$P = V^2/R \Rightarrow R = V^2/P$."],
      [r"is the current, $P/V = 12.5$ A.", r"is $V/P$, which has the wrong units.", r"is $PV$, which has no physical meaning here."], sort=True),
    Q("11.4 Bulb brightness", r"Three identical bulbs are connected to an ideal battery: bulb A is in series with a parallel pair, B and C. Which bulb is brightest?",
      r"A", [r"B", r"C", r"All are equally bright"],
      r"All the current passes through A, then splits equally between B and C. A carries twice the current, so it dissipates four times the power of B or C.",
      [r"$I_A = I$, $I_B = I_C = I/2$.", r"$P = I^2R$: $P_A = 4P_B$."],
      [r"B carries half of A's current.", r"C carries half of A's current.", r"the currents differ, so the powers differ."]),
    Q("11.5 Current in a branch", r"A $6.0\ \Omega$ resistor is in series with a parallel combination of $6.0\ \Omega$ and $3.0\ \Omega$, across an ideal 12 V battery. What is the current in the $3.0\ \Omega$ resistor?",
      r"$1.0$ A", [r"$1.5$ A", r"$0.50$ A", r"$4.0$ A"],
      r"Parallel pair: $2.0\ \Omega$; total $8.0\ \Omega$; battery current 1.5 A. The pair has $1.5 \times 2.0 = 3.0$ V across it, so $I_3 = 3.0/3.0 = 1.0$ A.",
      [r"$R_{eq} = 6.0 + 2.0 = 8.0\ \Omega$, $I = 1.5$ A.", r"$\Delta V_{pair} = 3.0$ V; $I_{3\Omega} = 1.0$ A, $I_{6\Omega} = 0.50$ A."],
      [r"is the total current, which splits at the junction.", r"is the current in the $6.0\ \Omega$ branch of the pair.", r"puts the full 12 V across the $3.0\ \Omega$ resistor."], sort=True),
    Q("11.6 Loop rule", r"A single loop contains a 12 V battery and a 4.0 V battery connected so that they oppose each other (positive terminals facing), plus resistors totaling $4.0\ \Omega$. What is the current?",
      r"$2.0$ A", [r"$4.0$ A", r"$1.0$ A", r"$3.0$ A"],
      r"Around the loop: $12 - 4.0 - I(4.0) = 0$, so $I = 2.0$ A, driven by the larger battery.",
      [r"Net emf $= 12 - 4.0 = 8.0$ V.", r"$I = 8.0/4.0 = 2.0$ A."],
      [r"adds the emfs as if they aided each other.", r"uses only the smaller emf.", r"uses only the larger emf."], ),
    Q("11.7 Two-battery circuit", r"Two nodes, top and bottom, are joined by three branches. Left: a 10 V battery (positive terminal toward the top node) in series with $2.0\ \Omega$. Middle: a $4.0\ \Omega$ resistor. Right: a 6.0 V battery (positive terminal toward the top node) in series with $2.0\ \Omega$. What is the current in the $4.0\ \Omega$ resistor?",
      r"$1.6$ A", [r"$4.0$ A", r"$2.0$ A", r"$1.0$ A"],
      r"Let $V$ be the top node's potential relative to the bottom. Junction rule: $\dfrac{10 - V}{2.0} + \dfrac{6.0 - V}{2.0} = \dfrac{V}{4.0}$, so $V = 6.4$ V and the middle current is $6.4/4.0 = 1.6$ A.",
      [r"$5 - V/2 + 3 - V/2 = V/4 \Rightarrow 8 = 1.25V$.", r"$V = 6.4$ V. Left branch 1.8 A up, right branch 0.20 A down (the 6.0 V battery is being charged)."],
      [r"adds the emfs and divides by $4.0\ \Omega$, as if all were in series.", r"is half the sum of the emfs over the $4.0\ \Omega$ with no loop analysis.", r"uses the difference of the emfs over $4.0\ \Omega$."], sort=True),
    Q("11.6 Internal resistance", r"A battery with emf 9.0 V and internal resistance $1.0\ \Omega$ is connected to a $2.0\ \Omega$ resistor. What is the terminal voltage?",
      r"$6.0$ V", [r"$9.0$ V", r"$3.0$ V", r"$4.5$ V"],
      r"$I = \varepsilon/(R + r) = 3.0$ A, so $\Delta V = \varepsilon - Ir = 9.0 - 3.0 = 6.0$ V (also $IR$).",
      [r"$I = 9.0/3.0 = 3.0$ A.", r"$\Delta V = IR = 6.0$ V."],
      [r"ignores the internal resistance.", r"is the drop inside the battery.", r"splits the emf equally."], sort=True),
    Q("11.5 Meters", r"How should an ideal voltmeter be connected to measure the voltage across a resistor, and why does it not disturb the circuit?",
      r"In parallel; its very large resistance draws almost no current", [r"In series; its very small resistance causes almost no voltage drop", r"In parallel; its very small resistance carries the current around the resistor", r"In series; its very large resistance keeps the current steady"],
      r"A voltmeter compares the potentials at two points, so it attaches across the resistor. Its huge resistance means almost no current is diverted.",
      [r"Voltmeter: parallel, $R \to \infty$.", r"Ammeter: series, $R \to 0$."],
      [r"describes an ammeter.", r"a small resistance in parallel would short the resistor.", r"a large resistance in series would choke off the current."]),
    Q("11.8 RC charging", r"A 12 V battery charges a $50\ \mu\mathrm{F}$ capacitor through a $2.0\ \mathrm{k}\Omega$ resistor, starting from zero charge. What is the current at $t = 0.10$ s?",
      r"$2.2$ mA", [r"$6.0$ mA", r"$3.8$ mA", r"$0$ mA"],
      r"$\tau = RC = 0.10$ s. $I = (\varepsilon/R)e^{-t/\tau} = (6.0\ \mathrm{mA})e^{-1} = 2.2$ mA.",
      [r"Initial current $12/2000 = 6.0$ mA.", r"At $t = \tau$: $6.0 \times 0.368 = 2.2$ mA."],
      [r"is the initial current.", r"is $6.0(1 - e^{-1})$; that growth law describes the charge, not the current.", r"is the current only after many time constants."], sort=True),
    Q("11.8 Steady state", r"A 12 V battery is in series with a $4.0\ \Omega$ resistor and a $2.0\ \Omega$ resistor. A $10\ \mu\mathrm{F}$ capacitor is connected in parallel with the $2.0\ \Omega$ resistor. Long after the circuit is connected, what is the charge on the capacitor?",
      r"$40\ \mu\mathrm{C}$", [r"$120\ \mu\mathrm{C}$", r"$80\ \mu\mathrm{C}$", r"$0$"],
      r"In steady state no current enters the capacitor, so $I = 12/6.0 = 2.0$ A through both resistors. The capacitor has the same 4.0 V as the $2.0\ \Omega$ resistor: $Q = CV = 40\ \mu\mathrm{C}$.",
      [r"$I = 2.0$ A; $\Delta V_{2\Omega} = 4.0$ V.", r"$Q = (10\ \mu\mathrm{F})(4.0\ \mathrm{V})$."],
      [r"puts the full 12 V across the capacitor.", r"uses the 8.0 V across the $4.0\ \Omega$ resistor.", r"the capacitor's branch carries no current, but it still has a voltage across it."], sort=True),
    Q("11.8 Just after closing", r"In the circuit of the previous question, the capacitor is uncharged when the switch closes. What is the current from the battery immediately afterward?",
      r"$3.0$ A", [r"$2.0$ A", r"$6.0$ A", r"$0$"],
      r"An uncharged capacitor has no voltage across it, so it acts like a wire and shorts out the $2.0\ \Omega$ resistor. $I = 12/4.0 = 3.0$ A.",
      [r"At $t = 0$: $\Delta V_C = 0$, so the $2.0\ \Omega$ resistor has no current.", r"Only $4.0\ \Omega$ remains: 3.0 A."],
      [r"is the steady-state current.", r"divides by the shorted $2.0\ \Omega$ instead of the $4.0\ \Omega$.", r"an uncharged capacitor passes current freely at first."], sort=True),
    Q("11.8 Discharging", r"A capacitor discharges through a resistor with time constant $\tau$. How long does it take for its charge to fall to half its initial value?",
      r"$\tau\ln 2$", [r"$\tau/2$", r"$\tau$", r"$2\tau$"],
      r"$Q_0e^{-t/\tau} = Q_0/2 \Rightarrow t = \tau\ln 2 \approx 0.69\tau$.",
      [r"$e^{-t/\tau} = 1/2$.", r"$t = \tau\ln 2$."],
      [r"assumes a linear decrease.", r"after one $\tau$ only 37\% remains, less than half.", r"after $2\tau$ only 14\% remains."]),
]

UNIT = Unit(
    n=11, slug="electric-circuits", title="Electric Circuits", weight="15--25\\%", topics="11.1--11.8",
    abstract=r"""Unit 11 covers direct-current circuits: current, resistivity, and Ohm's law (11.1--11.3); power and bulb brightness (11.4); series and parallel combinations, real batteries, and meters (11.5); Kirchhoff's loop and junction rules (11.6--11.7); and RC circuits, including the differential equation behind charging and discharging and the behavior just after a switch closes and long after (11.8). The free-response question is an experiment to find a battery's internal resistance. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4],
    qsections=[("Current, resistance, and power (11.1--11.4)", QS1[:4]), ("DC circuits and Kirchhoff's rules (11.5--11.7)", QS1[4:9]), ("RC circuits (11.8)", QS1[9:])],
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students want to find the emf $\varepsilon$ and the internal resistance $r$ of a battery. They have the battery, a variable resistor, an ammeter, a voltmeter, a switch, and wires. They measure the terminal voltage $\Delta V$ for several currents $I$:

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$I$ (A) & 0.20 & 0.40 & 0.60 & 0.80 & 1.00 \\ \midrule
$\Delta V$ (V) & 5.81 & 5.58 & 5.42 & 5.19 & 5.01 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe how to connect the equipment, and how the measurements are taken, so that the data in the table can be collected.",
             r"1 pt: battery, switch, ammeter, and variable resistor in one series loop. 1 pt: voltmeter connected directly across the battery terminals (in parallel). 1 pt: adjust the variable resistor to change $I$, recording the ammeter and voltmeter readings each time (switch open between readings so the battery does not heat).",
             r"Putting the voltmeter in series, or the ammeter in parallel."),
        Part("b", 2, r"Write an equation relating $\Delta V$ and $I$, and state what graph gives a straight line from which $\varepsilon$ and $r$ can be read.",
             r"1 pt: $\Delta V = \varepsilon - Ir$. 1 pt: graph $\Delta V$ versus $I$: slope $= -r$, vertical intercept $= \varepsilon$.",
             r"Graphing $\Delta V$ versus $1/I$."),
        Part("c", 3, r"Using a best-fit line for the data, determine $r$ and $\varepsilon$.",
             r"1 pt: a straight best-fit line through the data (by plot or calculator fit). 1 pt: slope $\approx -1.0$ V/A, so $r \approx 1.0\ \Omega$ (accept 0.9--1.1). 1 pt: intercept $\approx 6.0$ V, so $\varepsilon \approx 6.0$ V.",
             r"Using $r = \Delta V/I$ from one row, which gives the external resistance."),
        Part("d", 2, r"A student says the ammeter's small but nonzero resistance makes the measured value of $r$ too large. Do you agree? Explain, based on your circuit in (a).",
             r"1 pt: disagree, for the circuit in (a). 1 pt: the voltmeter is across the battery's terminals and the ammeter reads the battery's own current, so the ammeter's resistance is only part of the external load; it changes which currents occur, not the relation $\Delta V = \varepsilon - Ir$. (If the voltmeter were instead across the variable resistor alone, the ammeter's voltage drop would be counted as internal, and the student would be right.)",
             r"Agreeing without referring to where the voltmeter is connected."),
    ]),
    frq_topic="measuring a battery's emf and internal resistance",
)
