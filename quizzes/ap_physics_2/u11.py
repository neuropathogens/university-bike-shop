from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Electric current (11.1)", ["11.1"], r"""
\textbf{Current} is the rate at which charge passes a point:
\[ I = \frac{\Delta q}{\Delta t}, \qquad 1\ \mathrm{A} = 1\ \mathrm{C/s}. \]
By convention current points in the direction positive charge would move: out of a battery's positive terminal and around the circuit. In metal wires the moving charges are electrons, which drift slowly the other way; the current starts everywhere almost at once because the field that pushes them spreads through the circuit at nearly the speed of light.
""", checks=[
    Q("11.1 Counting electrons", r"A current of $2.0$ A flows in a wire. How many electrons pass a given point each second?",
      r"$1.25 \times 10^{19}$", [r"$3.2 \times 10^{-19}$", r"$2.0$", r"$8.0 \times 10^{-20}$"],
      r"$2.0$ C/s divided by $1.6 \times 10^{-19}$ C per electron gives $1.25 \times 10^{19}$ electrons per second.",
      [r"$N = I\Delta t/e$."],
      [r"multiplies the current by $e$.",
       r"is the charge in coulombs, not the number of electrons.",
       r"divides $e$ by the current."], sort=True),
])

S2 = Sec("Simple circuits (11.2)", ["11.2"], r"""
A circuit needs a closed conducting path and a source of emf (a battery), which does work on charges and keeps a potential difference across its terminals. In circuit diagrams, wires are ideal (no resistance), so every point on a single wire is at the same potential.

\begin{terms}
Series & one path: the same current through each element \\
Parallel & elements connected across the same two points (nodes): the same potential difference across each \\
Ammeter & measures current; connected in series, with (ideally) zero resistance \\
Voltmeter & measures potential difference; connected in parallel, with (ideally) infinite resistance \\
Open and short & an open switch or break stops current in that branch; a wire across an element (a short) takes all the current \\
\end{terms}
""", checks=[
    Q("11.2 Meters", r"A student wants to measure the current through a light bulb and the potential difference across it. How should the meters be connected?",
      r"the ammeter in series with the bulb and the voltmeter in parallel with it", [r"the ammeter in parallel with the bulb and the voltmeter in series with it", r"both meters in series with the bulb", r"both meters in parallel with the bulb"],
      r"An ammeter must carry the bulb's current, so it goes in the same path; a voltmeter compares the potentials at the bulb's two ends.",
      [r"Ideal ammeter: zero resistance in series. Ideal voltmeter: infinite resistance in parallel."],
      [r"an ammeter in parallel would short the bulb, and a voltmeter in series would block the current.",
       r"a voltmeter in series stops the current.",
       r"an ammeter in parallel shorts the bulb."]),
])

S3 = Sec("Resistance, resistivity and Ohm's law (11.3)", ["11.3"], r"""
\[ R = \frac{\rho\ell}{A}, \qquad I = \frac{\Delta V}{R} . \]
Resistance depends on the material (resistivity $\rho$, in $\Omega\,$m), the length $\ell$ and the cross-sectional area $A$. A resistor is \textbf{ohmic} if its current is proportional to the potential difference across it (a straight-line $I$--$\Delta V$ graph through the origin). A filament bulb is non-ohmic: its resistance rises as it heats up.

\begin{trap}
Doubling a wire's diameter quadruples its area ($A = \pi d^2/4$) and so divides its resistance by 4.
\end{trap}
""", checks=[
    Q("11.3 Resistivity", r"A wire is replaced by one of the same material with twice the length and twice the diameter. How does the new wire's resistance compare with the original's?",
      r"half as large", [r"the same", r"twice as large", r"four times as large"],
      r"$R = \rho\ell/A$: twice the length doubles $R$; twice the diameter quadruples $A$, dividing $R$ by 4. Net: $\tfrac12$.",
      [r"$R' = \rho(2\ell)/(4A) = R/2$."],
      [r"treats the area as proportional to the diameter.",
       r"accounts for the length only.",
       r"has the effect of the area backward."]),
])

S4 = Sec("Electric power (11.4)", ["11.4"], r"""
A resistor converts electrical energy to thermal energy (and light) at the rate
\[ P = I\Delta V = I^2R = \frac{(\Delta V)^2}{R} . \]
A bulb's brightness is set by the power it dissipates. In series, the same current flows through every bulb, so the one with the larger resistance is brighter ($P = I^2R$); in parallel, each has the same potential difference, so the one with the smaller resistance is brighter ($P = \Delta V^2/R$).
""", checks=[
    Q("11.4 Power", r"A light bulb dissipates $60$ W when connected to $120$ V. What is its resistance while lit?",
      r"$240\ \Omega$", [r"$0.50\ \Omega$", r"$2.0\ \Omega$", r"$7200\ \Omega$"],
      r"$R = (\Delta V)^2/P = 14\,400/60 = 240\ \Omega$ (and $I = 0.50$ A).",
      [r"$P = (\Delta V)^2/R$."],
      [r"is the current in amperes.",
       r"is $\Delta V/P$.",
       r"multiplies power by voltage."], sort=True),
])

S5 = Sec("Compound direct current circuits (11.5)", ["11.5"], r"""
\[ R_{series} = R_1 + R_2 + \cdots, \qquad \frac{1}{R_{parallel}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots \]
Adding a resistor in series increases the total resistance; adding one in parallel \emph{decreases} it (there is a new path). The equivalent resistance of a parallel group is smaller than its smallest member.

\begin{keyidea}[Solving a series--parallel circuit]
(1) Reduce the circuit step by step to one equivalent resistance. (2) Find the current from the battery, $I = \mathcal{E}/R_{eq}$. (3) Work back out: the series resistor gets the full current; the parallel group shares the remaining potential difference, and each branch takes $I = \Delta V/R$.
\end{keyidea}

\textbf{Real batteries.} A battery with internal resistance $r$ delivers a terminal voltage $\Delta V = \mathcal{E} - Ir$, which falls as the current rises.
""", checks=[
    Q("11.5 Equivalent resistance", r"A $6.0\ \Omega$ resistor is in series with a parallel pair of $6.0\ \Omega$ and $3.0\ \Omega$ resistors, connected to a $12$ V battery. What is the current from the battery?",
      r"$1.5$ A", [r"$0.80$ A", r"$4.0$ A", r"$2.0$ A"],
      r"The parallel pair is $2.0\ \Omega$; total $8.0\ \Omega$; $I = 12/8.0 = 1.5$ A.",
      [r"$1/R_p = 1/6.0 + 1/3.0 = 1/2.0$.", r"$R_{eq} = 6.0 + 2.0 = 8.0\ \Omega$."],
      [r"adds all three resistors in series ($15\ \Omega$).",
       r"uses only the $3.0\ \Omega$ resistor.",
       r"uses only the $6.0\ \Omega$ series resistor."], sort=True),
])

S6 = Sec("Kirchhoff's loop rule (11.6)", ["11.6"], r"""
Around any closed loop, the changes in potential add to zero:
\[ \sum \Delta V = 0 . \]
This is conservation of energy for charges going around the loop. Crossing a battery from $-$ to $+$ raises the potential by $\mathcal{E}$; crossing a resistor in the direction of the current lowers it by $IR$. Resistors in series share the battery's potential difference in proportion to their resistances.
""", checks=[
    Q("11.6 Loop rule", r"A $9.0$ V battery is connected to two resistors in series. The potential difference across the first resistor is $3.0$ V. What is the potential difference across the second?",
      r"$6.0$ V", [r"$3.0$ V", r"$9.0$ V", r"$12$ V"],
      r"The drops around the loop must total the battery's $9.0$ V: $9.0 - 3.0 = 6.0$ V.",
      [r"$\mathcal{E} - \Delta V_1 - \Delta V_2 = 0$."],
      [r"series resistors share the potential difference only equally if they are equal.",
       r"the full battery voltage is split between the two resistors.",
       r"adds instead of subtracting."], sort=True),
])

S7 = Sec("Kirchhoff's junction rule (11.7)", ["11.7"], r"""
At any junction, the total current in equals the total current out:
\[ \sum I_{in} = \sum I_{out} . \]
This is conservation of charge: charge does not pile up at a junction in a steady circuit. Currents in parallel branches add to the current in the wire that feeds them.
""", checks=[
    Q("11.7 Junction rule", r"A current of $3.0$ A enters a junction, where it splits into two branches. One branch carries $1.2$ A. What does the other carry?",
      r"$1.8$ A", [r"$4.2$ A", r"$1.2$ A", r"$1.5$ A"],
      r"Charge is conserved at the junction: $3.0 = 1.2 + I_2$, so $I_2 = 1.8$ A.",
      [r"Current in $=$ current out."],
      [r"adds the currents instead of subtracting.",
       r"branches carry equal currents only if their resistances are equal.",
       r"splits the current evenly."], sort=True),
])

S8 = Sec("Resistor--capacitor (RC) circuits (11.8)", ["11.8"], r"""
When an uncharged capacitor is connected in series with a resistor and a battery:
\begin{compare}{Moment}{Capacitor behaves like}{Current}
Just after the switch closes & a wire (no charge, no potential difference) & maximum, $\mathcal{E}/R$ \\
While charging & a growing opposition & falls exponentially \\
Long after & a break in the circuit (fully charged to $\mathcal{E}$) & zero in that branch \\
\end{compare}
The \textbf{time constant} $\tau = RC$ sets the timescale: after one time constant a charging capacitor has reached about $63\%$ of its final charge, and a discharging one has lost about $63\%$ of its charge.

\textbf{Capacitors in combination.} In parallel, capacitances add: $C_{eq} = C_1 + C_2$. In series, their reciprocals add, and the equivalent is smaller than either.
""", checks=[
    Q("11.8 Time constant", r"A $2.0\ \mathrm{k\Omega}$ resistor is in series with a $50\ \mu$F capacitor. What is the time constant of the circuit?",
      r"$0.10$ s", [r"$100$ s", r"$4.0 \times 10^{7}$ s", r"$2.5 \times 10^{-8}$ s"],
      r"$\tau = RC = (2.0 \times 10^3)(50 \times 10^{-6}) = 0.10$ s.",
      [r"Convert the prefixes: $\mathrm{k} = 10^3$, $\mu = 10^{-6}$."],
      [r"ignores the prefixes.",
       r"divides $R$ by $C$.",
       r"divides $C$ by $R$."], sort=True),
])

QS = [
    Set("Current, resistance and power (11.1--11.4)", [
        Q("11.3 A copper wire", r"A copper wire ($\rho = 1.7 \times 10^{-8}\ \Omega\,$m) is $10$ m long and has a cross-sectional area of $1.0 \times 10^{-6}\ \mathrm{m^2}$. What is its resistance?",
          r"$0.17\ \Omega$", [r"$1.7 \times 10^{-13}\ \Omega$", r"$5.9\ \Omega$", r"$1.7 \times 10^{-2}\ \Omega$"],
          r"$R = \rho\ell/A = (1.7 \times 10^{-8})(10)/(1.0 \times 10^{-6}) = 0.17\ \Omega$.",
          [r"Longer and thinner wires have more resistance."],
          [r"multiplies by the area instead of dividing.",
           r"is $A/(\rho\ell)$, upside down.",
           r"uses a length of $1.0$ m."], sort=True),
        Q("11.4 Bulbs in series", r"A $60$ W bulb and a $100$ W bulb, both rated for $120$ V, are connected in series across a $120$ V supply. Assuming their resistances do not change, which glows more brightly?",
          r"the $60$ W bulb", [r"the $100$ W bulb", r"They glow equally.", r"Neither lights, since each gets less than $120$ V."],
          r"$R = \Delta V^2/P$: $240\ \Omega$ for the $60$ W bulb and $144\ \Omega$ for the $100$ W bulb. In series they carry the same current, so $P = I^2R$ is greater for the larger resistance.",
          [r"Same current; brightness $\propto R$."],
          [r"is brighter only when each bulb gets the full $120$ V, as in parallel.",
           r"their resistances differ, so their powers differ.",
           r"both light, just more dimly than at full voltage."]),
        Q("11.4 Hair dryer", r"A hair dryer draws $1200$ W from a $120$ V outlet. What is its resistance?",
          r"$12\ \Omega$", [r"$10\ \Omega$", r"$0.10\ \Omega$", r"$1.4 \times 10^{4}\ \Omega$"],
          r"$R = \Delta V^2/P = 14\,400/1200 = 12\ \Omega$.",
          [r"The current is $P/\Delta V = 10$ A; then $R = \Delta V/I = 12\ \Omega$."],
          [r"is the current in amperes.",
           r"is $\Delta V/P$.",
           r"is $\Delta V^2$, not yet divided by the power."], sort=True),
        Q("11.1 Electrons per second", r"The current in a wire is $0.80$ A. How many electrons pass a point in the wire each second?",
          r"$5.0 \times 10^{18}$", [r"$1.3 \times 10^{-19}$", r"$0.80$", r"$8.0 \times 10^{18}$"],
          r"$N = I/e = 0.80/(1.6 \times 10^{-19}) = 5.0 \times 10^{18}$ per second.",
          [r"Each electron carries $1.6 \times 10^{-19}$ C."],
          [r"multiplies by $e$.",
           r"is the charge in coulombs.",
           r"uses $10^{-19}$ C per electron."], sort=True),
    ]),
    Set("A series--parallel circuit (11.5--11.7)", [
        Q("11.5 Equivalent resistance", r"What is the equivalent resistance of the circuit?",
          r"$8.0\ \Omega$", [r"$22\ \Omega$", r"$2.0\ \Omega$", r"$4.0\ \Omega$"],
          r"$R_2 \parallel R_3$: $1/R_p = 1/6.0 + 1/12 = 1/4.0$. Then $R_{eq} = 4.0 + 4.0 = 8.0\ \Omega$.",
          [r"Parallel first, then series."],
          [r"adds all three in series.",
           r"puts all three in parallel.",
           r"leaves out $R_1$."], sort=True),
        Q("11.5 Battery current", r"What is the current through the battery?",
          r"$1.5$ A", [r"$3.0$ A", r"$0.55$ A", r"$6.0$ A"],
          r"$I = \mathcal{E}/R_{eq} = 12/8.0 = 1.5$ A.",
          [r"All the current passes through $R_1$."],
          [r"uses only $4.0\ \Omega$.",
           r"uses $22\ \Omega$, as if all were in series.",
           r"uses $2.0\ \Omega$, as if all were in parallel."], sort=True),
        Q("11.6 Potential difference", r"What is the potential difference across $R_3$?",
          r"$6.0$ V", [r"$12$ V", r"$4.0$ V", r"$18$ V"],
          r"$R_1$ takes $1.5 \times 4.0 = 6.0$ V, leaving $12 - 6.0 = 6.0$ V across the parallel pair (and so across $R_3$).",
          [r"Loop rule: $12 = \Delta V_1 + \Delta V_p$."],
          [r"is the whole battery voltage.",
           r"splits $12$ V equally among three resistors.",
           r"multiplies the full battery current by $R_3$, but only part of it flows through $R_3$."], sort=True),
        Q("11.7 Branch current", r"What is the current through $R_2$?",
          r"$1.0$ A", [r"$1.5$ A", r"$0.50$ A", r"$0.75$ A"],
          r"$I_2 = 6.0\ \mathrm{V}/6.0\ \Omega = 1.0$ A; then $R_3$ carries $0.50$ A, and $1.0 + 0.50 = 1.5$ A.",
          [r"Junction rule check: the branches add to the battery current."],
          [r"is the total current.",
           r"is the current through $R_3$.",
           r"splits the current evenly, ignoring the different resistances."], sort=True),
        Q("11.5 Removing a branch", r"$R_3$ is removed, leaving a gap in its branch. Which is correct?",
          r"The current through $R_1$ decreases, and the potential difference across $R_2$ increases.", [r"The current through $R_1$ increases, and the potential difference across $R_2$ increases.", r"The current through $R_1$ decreases, and the potential difference across $R_2$ decreases.", r"Nothing changes in the rest of the circuit."],
          r"Removing a parallel path raises $R_{eq}$ to $10\ \Omega$, so $I = 1.2$ A; $R_1$ then takes $4.8$ V, leaving $7.2$ V (up from $6.0$ V) across $R_2$.",
          [r"Fewer paths, more resistance, less current, smaller drop across $R_1$."],
          [r"removing a path raises the total resistance and lowers the current.",
           r"less current through $R_1$ means less of the battery's voltage is used there.",
           r"every part of a series--parallel circuit is affected."]),
        Q("11.4 Power in R1", r"At what rate is energy dissipated in $R_1$?",
          r"$9.0$ W", [r"$6.0$ W", r"$36$ W", r"$18$ W"],
          r"$P = I^2R = (1.5)^2(4.0) = 9.0$ W.",
          [r"Or $P = I\Delta V = 1.5 \times 6.0$."],
          [r"is the potential difference across $R_1$, in volts.",
           r"uses the full $12$ V across $R_1$.",
           r"is the power delivered by the battery to the whole circuit."], sort=True),
    ], stim=r"A $12$ V battery with negligible internal resistance is connected in series with resistor $R_1 = 4.0\ \Omega$ and a parallel combination of $R_2 = 6.0\ \Omega$ and $R_3 = 12\ \Omega$.",
        stim_title="Questions 5--10"),
    Set("Kirchhoff's rules and RC circuits (11.6--11.8)", [
        Q("11.7 Four wires", r"Currents of $2.0$ A and $3.0$ A flow into a junction of four wires. A third wire carries $4.0$ A out of the junction. What does the fourth wire carry?",
          r"$1.0$ A out of the junction", [r"$1.0$ A into the junction", r"$9.0$ A out of the junction", r"$5.0$ A out of the junction"],
          r"In: $5.0$ A. Out so far: $4.0$ A. The fourth wire must carry the remaining $1.0$ A out.",
          [r"$\sum I_{in} = \sum I_{out}$."],
          [r"would make the total in $6.0$ A and the total out $4.0$ A.",
           r"adds all three currents.",
           r"ignores the third wire."]),
        Q("11.6 Opposing batteries", r"A single loop contains a $9.0$ V battery and a $3.0$ V battery connected so that they oppose each other, and a $2.0\ \Omega$ resistor. What is the current?",
          r"$3.0$ A", [r"$6.0$ A", r"$4.5$ A", r"$1.5$ A"],
          r"Loop rule: $9.0 - 3.0 - 2.0I = 0$, so $I = 3.0$ A.",
          [r"Opposing emfs subtract."],
          [r"adds the two emfs.",
           r"ignores the $3.0$ V battery.",
           r"uses only the smaller battery."], sort=True),
        Q("11.8 Long after", r"An uncharged capacitor, a resistor and a battery of emf $\mathcal{E}$ are connected in series and the switch is closed. Long afterward, what are the current and the potential difference across the capacitor?",
          r"zero current; $\mathcal{E}$ across the capacitor", [r"maximum current; zero across the capacitor", r"zero current; zero across the capacitor", r"maximum current; $\mathcal{E}$ across the capacitor"],
          r"When the capacitor is fully charged, its potential difference matches the battery's, so none is left for the resistor and the current stops.",
          [r"Loop rule: $\mathcal{E} = IR + \Delta V_C$; with $\Delta V_C = \mathcal{E}$, $I = 0$."],
          [r"describes the instant the switch closes.",
           r"the capacitor has charged; it holds the battery's potential difference.",
           r"a full capacitor blocks steady current."]),
        Q("11.8 Capacitors in parallel", r"Capacitors of $2.0\ \mu$F and $3.0\ \mu$F are connected in parallel. What is their equivalent capacitance?",
          r"$5.0\ \mu$F", [r"$1.2\ \mu$F", r"$6.0\ \mu$F", r"$2.5\ \mu$F"],
          r"In parallel, capacitances add, since the plate areas effectively add.",
          [r"$C_{eq} = C_1 + C_2$."],
          [r"is the series combination.",
           r"multiplies the capacitances.",
           r"averages them."], sort=True),
    ]),
]

UNIT = Unit(11, "electric-circuits", "Electric Circuits", "15--18\\%", "11.1--11.8",
    abstract=r"""Unit 11 covers direct-current circuits: current, simple circuits and meters, resistance and resistivity, Ohm's law and electric power, series and parallel combinations, Kirchhoff's loop rule (conservation of energy) and junction rule (conservation of charge), and circuits with resistors and capacitors. The circuits here are described in words; sketching each one before you start is the first step of every solution. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6, S7, S8], qsections=QS,
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students want to determine the resistivity of the nichrome wire used in a toaster. They have a $1.2$ m length of the wire, a micrometer, a meter stick, a battery, an ammeter, a voltmeter, connecting leads and two sliding clips that can connect to the wire at any point.

\medskip
They measure the wire's diameter as $0.50$ mm and record the resistance $R$ of different lengths $\ell$ between the clips.

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$\ell$ (m) & 0.20 & 0.40 & 0.60 & 0.80 & 1.00 \\ \midrule
$R$ ($\Omega$) & 1.1 & 2.3 & 3.3 & 4.5 & 5.6 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe a procedure the students could use to obtain these data. Include how the meters are connected, what is measured, and one step that reduces experimental uncertainty.",
             r"1 pt: the battery, the ammeter and the wire between the clips are connected in series, with the voltmeter across the length of wire between the clips; $R = \Delta V/I$. 1 pt: measure $\ell$ between the clips with the meter stick for several clip positions, and the diameter with the micrometer. 1 pt: average the diameter over several places along the wire, or keep the current small and the switch closed only briefly so the wire does not heat up and change its resistance.",
             r"Connecting the voltmeter in series, or measuring only one length."),
        Part("b", 2, r"Indicate what the students should graph to obtain a straight line whose slope can be used to find the resistivity $\rho$. Express $\rho$ in terms of that slope and the diameter $d$.",
             r"1 pt: graph $R$ versus $\ell$; $R = (\rho/A)\ell$ is a straight line through the origin. 1 pt: $\rho = \text{slope} \times A = \text{slope} \times \pi d^2/4$.",
             r"Using the diameter in place of the radius in $A = \pi r^2$."),
        Part("c", 3, r"Determine the slope of a best-fit line for the data and use it to calculate the resistivity of nichrome.",
             r"1 pt: slope about $5.6\ \Omega$/m (accept $5.4$--$5.8$). 1 pt: $A = \pi(0.25 \times 10^{-3})^2 = 1.96 \times 10^{-7}\ \mathrm{m^2}$. 1 pt: $\rho = (5.6)(1.96 \times 10^{-7}) \approx 1.1 \times 10^{-6}\ \Omega\,$m.",
             r"Using $d$ as the radius, which makes $\rho$ four times too large."),
        Part("d", 2, r"A second group connects their voltmeter across both the wire and the ammeter, which has a small but non-negligible resistance. Explain how this affects their graph and their value of $\rho$.",
             r"1 pt: every measured resistance is too large by the same amount (the ammeter's resistance), so the line is shifted up and has a positive vertical intercept. 1 pt: the slope is unchanged, so their value of $\rho$ is unaffected.",
             r"Saying every value of $\rho$ will be too large."),
    ], mins=28),
    frq_topic="measuring the resistivity of nichrome wire",
)
