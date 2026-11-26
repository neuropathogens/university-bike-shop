from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

# P in kPa, V in L: A (1.0 L, 300 kPa) -> B (3.0 L, 300 kPa) -> C (3.0 L, 100 kPa) -> back to A along a straight line
PV = Graph(r"Volume $V$ ($\mathrm{10^{-3}\,m^3}$)", r"Pressure $P$ ($\mathrm{10^5\,Pa}$)", x=(0, 4, 1), y=(0, 4, 1),
           series=[Series("cycle", [(1, 3), (3, 3), (3, 1), (1, 3)], marks=True)],
           notes=[(1, 3, "A", "above left"), (3, 3, "B", "above right"), (3, 1, "C", "below right")])

S1 = Sec("Kinetic theory of temperature and pressure (9.1)", ["9.1"], r"""
A gas is a huge number of molecules in random motion. \textbf{Pressure} is the average force per unit area from their collisions with the container walls. \textbf{Temperature} measures the average translational kinetic energy of the molecules:
\[ K_{avg} = \tfrac32 k_B T, \qquad v_{rms} = \sqrt{\frac{3k_BT}{m}}, \]
with $T$ in kelvins ($T_K = T_C + 273$) and $k_B = 1.38 \times 10^{-23}$ J/K. At a given temperature the molecules have a spread of speeds (the Maxwell--Boltzmann distribution); heating the gas shifts the distribution toward higher speeds and flattens it.

\begin{trap}
Doubling the Kelvin temperature doubles the average kinetic energy but multiplies the rms speed by only $\sqrt2$. And two gases at the same temperature have the same average kinetic energy per molecule, so the lighter molecules move faster.
\end{trap}
""", checks=[
    Q("9.1 Temperature and speed", r"The Kelvin temperature of a sample of helium is doubled. By what factor does the rms speed of its atoms change?",
      r"$\sqrt2$", [r"$2$", r"$4$", r"$\tfrac12$"],
      r"$v_{rms} = \sqrt{3k_BT/m} \propto \sqrt T$.",
      [r"Average kinetic energy doubles; speed goes as its square root."],
      [r"is the factor for the average kinetic energy, not the speed.",
       r"squares the factor instead of taking its root.",
       r"a hotter gas has faster atoms."]),
])

S2 = Sec("The ideal gas law (9.2)", ["9.2"], r"""
\[ PV = nRT = Nk_BT, \qquad R = 8.31\ \mathrm{J/(mol\,K)}, \]
with $P$ in pascals, $V$ in $\mathrm{m^3}$ and $T$ in kelvins. For a fixed amount of gas, $\dfrac{P_1V_1}{T_1} = \dfrac{P_2V_2}{T_2}$.

\begin{compare}{Held constant}{Relationship}{Graph}
Temperature & $P \propto 1/V$ & a hyperbola (isotherm) on a $P$--$V$ diagram; hotter isotherms lie farther from the origin \\
Volume & $P \propto T$ & a straight line through $T = 0$ K \\
Pressure & $V \propto T$ & a straight line through $T = 0$ K \\
\end{compare}

\begin{trap}
Always convert to kelvins. Heating a sealed rigid can from $27^\circ$C to $54^\circ$C does not double its pressure; it raises it from $300$ K to $327$ K, about 9\%.
\end{trap}
""", checks=[
    Q("9.2 Ideal gas law", r"$2.0$ mol of an ideal gas at $300$ K occupies $0.050\ \mathrm{m^3}$. What is its pressure?",
      r"$1.0 \times 10^5$ Pa", [r"$5.0 \times 10^{3}$ Pa", r"$1.0 \times 10^{2}$ Pa", r"$1.0 \times 10^{-5}$ Pa"],
      r"$P = nRT/V = (2.0)(8.31)(300)/0.050 = 1.0 \times 10^5$ Pa.",
      [r"$nRT = 4986$ J; divide by $0.050\ \mathrm{m^3}$."],
      [r"is $nRT$, which still has to be divided by the volume.",
       r"divides by the volume in liters ($50$ L) instead of cubic meters.",
       r"is $V/(nRT)$, upside down."], sort=True),
    Q("9.2 Heating a sealed container", r"A sealed rigid container of gas is heated from $27^\circ$C to $327^\circ$C. By what factor does the pressure increase?",
      r"$2$", [r"$12$", r"$1.1$", r"$4$"],
      r"At constant volume $P \propto T$ in kelvins: $600\ \mathrm{K}/300\ \mathrm{K} = 2$.",
      [r"$27^\circ\mathrm{C} = 300$ K; $327^\circ\mathrm{C} = 600$ K."],
      [r"uses Celsius temperatures: $327/27$.",
       r"divides the change in temperature, $300$ degrees, by $273$ instead of comparing kelvin temperatures.",
       r"squares the ratio."], sort=True),
])

S3 = Sec("Thermal energy transfer and equilibrium (9.3)", ["9.3"], r"""
\textbf{Heat} ($Q$) is energy transferred because of a temperature difference; it always flows spontaneously from hotter to colder until the objects reach \textbf{thermal equilibrium} (the same temperature). Heat is not something an object contains; an object has internal energy.

\begin{terms}
Conduction & transfer by collisions between neighboring particles, through a material or across a contact \\
Convection & transfer by bulk motion of a fluid (warm air rising) \\
Radiation & transfer by electromagnetic waves; needs no medium, so it crosses empty space \\
\end{terms}

At the microscopic level, molecules of the hotter object have greater average kinetic energy; in collisions they tend to lose energy to slower molecules, so energy spreads out until the average kinetic energies match.
""", checks=[
    Q("9.3 Feeling cold", r"A metal spoon and a wooden spoon have been in the same drawer for days. The metal spoon feels colder to the touch. Why?",
      r"Metal conducts energy away from your hand faster than wood does.", [r"The metal spoon is at a lower temperature.", r"Metal contains less heat than wood.", r"Wood radiates energy toward your hand."],
      r"Both are at room temperature; the feeling of cold is the rate at which your skin loses energy, and metal is a much better conductor.",
      [r"Thermal equilibrium: same temperature. Different conductivity: different rate of energy transfer."],
      [r"objects left together reach the same temperature.",
       r"objects contain internal energy, not heat; heat is energy in transfer.",
       r"radiation at room temperature is small and the same for both."]),
])

S4 = Sec("The first law of thermodynamics (9.4)", ["9.4"], r"""
\[ \Delta U = Q + W, \qquad W = -P\Delta V \ (\text{work done \emph{on} the gas}). \]
$Q$ is positive when energy flows into the gas by heating; $W$ is positive when the gas is compressed. For an ideal monatomic gas the internal energy is $U = \tfrac32 nRT$, so $\Delta U$ depends only on the change in temperature.

\begin{compare}{Process}{What is constant}{Consequence}
Isovolumetric & $V$ & $W = 0$, so $\Delta U = Q$ \\
Isobaric & $P$ & $W = -P\Delta V$ \\
Isothermal & $T$ & $\Delta U = 0$, so $Q = -W$ \\
Adiabatic & no heat ($Q = 0$) & $\Delta U = W$: compression heats the gas \\
Cycle & returns to the start & $\Delta U = 0$; net work is the enclosed area \\
\end{compare}

\begin{keyidea}[Reading a $P$--$V$ diagram]
The magnitude of the work is the area under the path. Moving right (expansion), the gas does work and $W$ on it is negative; moving left (compression), $W$ is positive. Going clockwise around a cycle, the gas does net positive work.
\end{keyidea}
""", checks=[
    Q("9.4 First law", r"$300$ J of work is done on a gas while it releases $100$ J of energy to its surroundings by heating. What is the change in its internal energy?",
      r"$+200$ J", [r"$+400$ J", r"$-200$ J", r"$-400$ J"],
      r"$\Delta U = Q + W = (-100) + (+300) = +200$ J.",
      [r"Work done on the gas: $W = +300$ J. Energy leaving by heating: $Q = -100$ J."],
      [r"adds the energy that leaves instead of subtracting it.",
       r"has both signs reversed.",
       r"treats both transfers as leaving the gas."]),
    Q("9.4 Isobaric work", r"A gas expands at a constant pressure of $2.0 \times 10^5$ Pa from $0.010\ \mathrm{m^3}$ to $0.030\ \mathrm{m^3}$. What is the work done on the gas?",
      r"$-4.0 \times 10^3$ J", [r"$+4.0 \times 10^3$ J", r"$-6.0 \times 10^3$ J", r"$-2.0 \times 10^3$ J"],
      r"$W = -P\Delta V = -(2.0 \times 10^5)(0.020) = -4000$ J; the gas does $4000$ J of work on its surroundings.",
      [r"$\Delta V = 0.020\ \mathrm{m^3}$."],
      [r"is the work done \emph{by} the gas; work done on an expanding gas is negative.",
       r"uses the final volume instead of the change.",
       r"uses the initial volume instead of the change."]),
])

S5 = Sec("Specific heat and thermal conductivity (9.5)", ["9.5"], r"""
\textbf{Specific heat.} The energy needed to change the temperature of a mass $m$ by $\Delta T$ is
\[ Q = mc\Delta T , \]
where $c$ is the specific heat (water: $4186\ \mathrm{J/(kg\,{}^\circ C)}$, unusually large, so water warms and cools slowly).

\textbf{Thermal conductivity.} The rate of energy transfer by conduction through a slab of area $A$ and thickness $L$ with a temperature difference $\Delta T$ across it is
\[ \frac{Q}{\Delta t} = \frac{kA\,\Delta T}{L}, \]
where $k$ is the material's thermal conductivity. Doubling the thickness halves the rate; doubling the area doubles it.
""", checks=[
    Q("9.5 Specific heat", r"How much energy is needed to raise the temperature of $0.50$ kg of water by $10^\circ$C? (The specific heat of water is $4186\ \mathrm{J/(kg\,{}^\circ C)}$.)",
      r"$2.1 \times 10^4$ J", [r"$4.2 \times 10^4$ J", r"$2.1 \times 10^3$ J", r"$4.2 \times 10^3$ J"],
      r"$Q = mc\Delta T = (0.50)(4186)(10) = 2.1 \times 10^4$ J.",
      [r"Multiply all three factors."],
      [r"leaves out the $0.50$ kg mass (uses 1 kg).",
       r"leaves out the factor of $10$.",
       r"is the specific heat alone: the energy for $1$ kg and $1^\circ$C."], sort=True),
])

S6 = Sec("Entropy and the second law of thermodynamics (9.6)", ["9.6"], r"""
\textbf{Entropy} measures how many microscopic arrangements are consistent with a system's macroscopic state; informally, how spread out its energy is. The \textbf{second law} says the total entropy of an isolated system never decreases. Consequences:
\begin{itemize}
\item Heat flows spontaneously from hot to cold, never the reverse, unless work is done (as in a refrigerator).
\item Processes such as mixing, friction and free expansion are irreversible: the reverse would lower total entropy.
\item The entropy of part of a system can decrease (water freezing) only if the entropy of the surroundings increases by at least as much.
\item No heat engine can turn all the energy it takes in from a hot reservoir into work; some must be exhausted to a cold reservoir.
\end{itemize}
""", checks=[
    Q("9.6 Second law", r"An ice cube melts in a glass of warm water inside a sealed, insulated container. Which statement about the entropy of the contents is correct?",
      r"It increases.", [r"It decreases, because the ice becomes more ordered water.", r"It stays the same, because the container is isolated.", r"It decreases, because energy leaves the warm water."],
      r"Energy spreads from the warm water to the ice; the process is irreversible, so the isolated system's entropy rises.",
      [r"Second law: an isolated system's entropy never decreases, and increases in irreversible processes."],
      [r"liquid water is less ordered than ice, so melting raises entropy.",
       r"isolated systems keep the same energy, not the same entropy.",
       r"the energy goes into the ice; the entropy gained there exceeds the entropy lost by the warm water."]),
])

QS = [
    Set("Gases and kinetic theory (9.1--9.2)", [
        Q("9.1 Two gases", r"A container holds a mixture of helium (molar mass $4$ g/mol) and argon ($40$ g/mol) at the same temperature. Which statement is correct?",
          r"The two kinds of atoms have the same average kinetic energy, and the helium atoms move faster on average.", [r"The argon atoms have more average kinetic energy because they are heavier.", r"The two kinds of atoms have the same average speed.", r"The helium atoms have more average kinetic energy because they move faster."],
          r"Temperature sets the average kinetic energy, $\tfrac32 k_BT$, the same for both; with less mass, helium needs more speed.",
          [r"$\tfrac12 m v_{rms}^2$ is the same; $v_{rms} \propto 1/\sqrt m$."],
          [r"kinetic energy per atom depends only on temperature.",
           r"equal kinetic energies with unequal masses mean unequal speeds.",
           r"the larger speed is exactly offset by the smaller mass."]),
        Q("9.2 Compressing a gas", r"A gas is compressed to half its volume while its Kelvin temperature is doubled. What happens to its pressure?",
          r"It becomes four times as large.", [r"It doubles.", r"It stays the same.", r"It is halved."],
          r"$P = nRT/V$: doubling $T$ doubles $P$, and halving $V$ doubles it again.",
          [r"$P_2/P_1 = (T_2/T_1)(V_1/V_2) = 2 \times 2$."],
          [r"accounts for only one of the two changes.",
           r"treats the two changes as cancelling; both raise the pressure.",
           r"inverts both effects."]),
        Q("9.2 Moles", r"A $0.020\ \mathrm{m^3}$ tank holds gas at $1.5 \times 10^5$ Pa and $250$ K. How many moles of gas does it hold?",
          r"$1.4$ mol", [r"$0.69$ mol", r"$12$ mol", r"$8.7 \times 10^{23}$ mol"],
          r"$n = PV/(RT)$, with $PV = 3000$ J and $RT = 2078$ J/mol, so $n = 1.4$ mol.",
          [r"$PV = 3000$ J; $RT = 2078$ J/mol."],
          [r"is $RT/PV$, upside down.",
           r"leaves out $R$: $PV/T$.",
           r"uses $k_B$ instead of $R$: that gives the number of molecules, not moles."], sort=True),
        Q("9.1 rms speed", r"What is the rms speed of nitrogen molecules ($m = 4.65 \times 10^{-26}$ kg) at $300$ K?",
          r"$517$ m/s", [r"$298$ m/s", r"$2.67 \times 10^5$ m/s", r"$730$ m/s"],
          r"$v_{rms} = \sqrt{3k_BT/m}$, with $3k_BT = 1.24 \times 10^{-20}$ J and $m = 4.65 \times 10^{-26}$ kg, so $v_{rms} = 517$ m/s.",
          [r"$3k_BT = 1.24 \times 10^{-20}$ J; divide by $m$ and take the square root."],
          [r"leaves out the factor 3.",
           r"forgets the square root.",
           r"uses $6k_BT$ (doubles the kinetic energy) inside the root."], sort=True),
    ]),
    Set("A thermodynamic cycle (9.4)", [
        Q("9.4 Work in an isobaric step", r"What is the work done on the gas during process $A \to B$?",
          r"$-600$ J", [r"$+600$ J", r"$-900$ J", r"$-300$ J"],
          r"$W = -P\Delta V = -(3.0 \times 10^5\ \mathrm{Pa})(2.0 \times 10^{-3}\ \mathrm{m^3}) = -600$ J.",
          [r"$A \to B$ is an expansion at constant pressure: the gas does work, so $W$ on it is negative."],
          [r"is the work done by the gas.",
           r"uses the final volume, $3.0 \times 10^{-3}\ \mathrm{m^3}$.",
           r"uses the initial volume, $1.0 \times 10^{-3}\ \mathrm{m^3}$."], sort=True),
        Q("9.4 Isovolumetric step", r"During process $B \to C$, which is true?",
          r"No work is done, and energy leaves the gas by heating.", [r"No work is done, and energy enters the gas by heating.", r"Work is done on the gas, and its internal energy increases.", r"The temperature of the gas stays constant."],
          r"The volume is constant, so $W = 0$; the pressure drops at constant volume, so $T$ and $U$ fall, which requires $Q < 0$.",
          [r"$\Delta U = Q$ when $W = 0$; $PV$ falls from $900$ J to $300$ J, so $T$ falls."],
          [r"the gas cools, so energy must leave.",
           r"no work is done at constant volume.",
           r"$P$ falls at constant $V$, so $T$ falls."]),
        Q("9.4 Temperatures", r"How does the temperature at $B$ compare with the temperature at $A$?",
          r"$T_B = 3T_A$", [r"$T_B = T_A$", r"$T_B = \tfrac13 T_A$", r"$T_B = 9T_A$"],
          r"$T \propto PV$: $PV$ is $300$ J at $A$ and $900$ J at $B$.",
          [r"Same pressure, three times the volume."],
          [r"an isobaric expansion is not isothermal.",
           r"inverts the ratio.",
           r"squares the ratio."]),
        Q("9.4 Net work in a cycle", r"What is the net work done by the gas during one complete cycle $A \to B \to C \to A$?",
          r"$200$ J", [r"$400$ J", r"$600$ J", r"$0$"],
          r"The net work is the area enclosed: a triangle with base $2.0 \times 10^{-3}\ \mathrm{m^3}$ and height $2.0 \times 10^5$ Pa, area $\tfrac12(2.0 \times 10^{-3})(2.0 \times 10^5) = 200$ J.",
          [r"Clockwise cycle: the gas does positive net work."],
          [r"leaves out the $\tfrac12$ for the triangle.",
           r"is the work done by the gas during $A \to B$ alone.",
           r"the internal energy returns to its starting value, but the net work is the enclosed area."], sort=True),
        Q("9.4 Heat over a cycle", r"Over one complete cycle, what is the net energy transferred to the gas by heating?",
          r"$+200$ J", [r"$-200$ J", r"$0$", r"$+1500$ J"],
          r"Over a cycle $\Delta U = 0$, so $Q = -W$; the work done on the gas is $-200$ J, so $Q = +200$ J.",
          [r"$\Delta U = Q + W = 0$."],
          [r"has the sign reversed: the gas does net work, so it must absorb net heat.",
           r"$\Delta U = 0$, not $Q = 0$.",
           r"is the heat absorbed during $A \to B$ alone; energy leaves by heating during the rest of the cycle."]),
    ], stim=r"One mole of an ideal monatomic gas is taken through the cycle $A \to B \to C \to A$ shown. State $A$ is at the upper left ($1.0 \times 10^{-3}\ \mathrm{m^3}$, $3.0 \times 10^5$ Pa), $B$ at the upper right, and $C$ at the lower right; $C \to A$ is a straight line.",
        fig=PV, stim_title="Questions 5--9"),
    Set("Heat transfer and entropy (9.3, 9.5--9.6)", [
        Q("9.5 Mixing", r"$0.20$ kg of water at $80^\circ$C is mixed with $0.60$ kg of water at $20^\circ$C in an insulated cup. What is the final temperature?",
          r"$35^\circ$C", [r"$50^\circ$C", r"$65^\circ$C", r"$20^\circ$C"],
          r"Energy lost by the hot water equals energy gained by the cold: $0.20(80 - T) = 0.60(T - 20)$, so $T = 35^\circ$C.",
          [r"$16 - 0.20T = 0.60T - 12$, so $0.80T = 28$."],
          [r"averages the temperatures without weighting by mass.",
           r"weights the hot water by the larger mass.",
           r"the cold water must warm up; it cannot stay at its starting temperature."], sort=True),
        Q("9.5 Conduction", r"A window pane is replaced by one of the same glass with twice the area and twice the thickness. With the same indoor and outdoor temperatures, the rate of energy loss through it",
          r"stays the same", [r"doubles", r"quadruples", r"is halved"],
          r"$Q/\Delta t = kA\Delta T/L$: doubling $A$ doubles the rate and doubling $L$ halves it.",
          [r"$(2A)/(2L) = A/L$."],
          [r"accounts for the area only.",
           r"treats both changes as increasing the rate.",
           r"accounts for the thickness only."]),
        Q("9.3 Radiation", r"Which way of transferring energy is the only one that can carry energy from the Sun to Earth?",
          r"radiation", [r"conduction", r"convection", r"all three equally"],
          r"Space between the Sun and Earth is nearly empty; only electromagnetic radiation needs no medium.",
          [r"Conduction needs contact; convection needs a moving fluid."],
          [r"needs particles in contact.",
           r"needs a fluid that can flow.",
           r"two of the three need matter."]),
        Q("9.6 Refrigerator", r"A refrigerator moves energy from its cold interior to the warmer kitchen. Why does this not violate the second law of thermodynamics?",
          r"The refrigerator does work, and the total entropy of the interior, the kitchen and the motor's surroundings increases.", [r"The second law applies only to heat engines.", r"The interior's entropy increases as it gets colder.", r"Energy is not conserved inside the refrigerator."],
          r"Heat flows from cold to hot only with work done; the energy dumped into the kitchen raises its entropy more than the interior's entropy falls.",
          [r"The second law forbids only a \emph{spontaneous} flow from cold to hot, with no other change."],
          [r"the second law applies to every process.",
           r"cooling the interior lowers its entropy; the kitchen's rises more.",
           r"energy is conserved; the first law holds."]),
    ]),
]

UNIT = Unit(9, "thermodynamics", "Thermodynamics", "15--18\\%", "9.1--9.6",
    abstract=r"""Unit 9 connects the microscopic and macroscopic views of matter: pressure and temperature from kinetic theory, the ideal gas law, energy transfer by conduction, convection and radiation, the first law of thermodynamics with $P$--$V$ diagrams (using the CED's convention that $W$ is the work done \emph{on} the gas), specific heat and thermal conductivity, and entropy and the second law. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Translation Between Representations", 12, r"""A cylinder with a movable, frictionless piston contains $n$ moles of an ideal monatomic gas, initially at pressure $P_0$, volume $V_0$ and temperature $T_0$ (state 1). The gas is taken through two processes:

\medskip
Process $1 \to 2$: the piston is locked and the gas is heated until its pressure is $2P_0$.

Process $2 \to 3$: the piston is released, and the gas expands at constant pressure $2P_0$ until its volume is $2V_0$.""", [
        Part("a", 3, r"On a $P$--$V$ diagram with labeled axes, sketch both processes. Label states 1, 2 and 3 and indicate the direction of each process with an arrow.",
             r"1 pt: $1 \to 2$ is a vertical line up from $(V_0, P_0)$ to $(V_0, 2P_0)$. 1 pt: $2 \to 3$ is a horizontal line from $(V_0, 2P_0)$ to $(2V_0, 2P_0)$. 1 pt: states labeled and arrows pointing up, then right.",
             r"Drawing $2 \to 3$ as a curve (isotherm)."),
        Part("b", 3, r"Derive expressions for the temperatures $T_2$ and $T_3$ in terms of $T_0$, and for the work $W$ done on the gas during process $2 \to 3$ in terms of $P_0$ and $V_0$.",
             r"1 pt: $T_2 = 2T_0$ (constant $V$, $P$ doubles). 1 pt: $T_3 = 4T_0$ ($PV$ is four times its initial value). 1 pt: $W_{2\to3} = -2P_0(2V_0 - V_0) = -2P_0V_0$.",
             r"A positive sign for the work done on an expanding gas."),
        Part("c", 3, r"Derive an expression for the energy $Q$ transferred to the gas by heating during process $2 \to 3$, in terms of $P_0$ and $V_0$.",
             r"1 pt: $\Delta U = \tfrac32 nR(T_3 - T_2) = \tfrac32 nR(2T_0) = 3P_0V_0$, using $nRT_0 = P_0V_0$. 1 pt: first law $Q = \Delta U - W$. 1 pt: $Q = 3P_0V_0 + 2P_0V_0 = 5P_0V_0$.",
             r"Writing $Q = \Delta U + W$ with $W$ the work done by the gas, which double-counts the sign."),
        Part("d", 3, r"Suppose instead the gas went from state 1 to state 3 along a straight line on the $P$--$V$ diagram. Is the energy transferred to the gas by heating along that path greater than, less than, or equal to the total for processes $1 \to 2 \to 3$? Justify your answer using your diagram.",
             r"1 pt: less than. 1 pt: $\Delta U$ is the same for both paths ($U$ depends only on the end states, $T_0$ to $4T_0$). 1 pt: the area under the straight line ($\tfrac32 P_0V_0$) is less than the area under $1 \to 2 \to 3$ ($2P_0V_0$), so the gas does less work, and $Q = \Delta U - W$ is smaller.",
             r"Saying the heat is the same because the end states are the same."),
    ], mins=28),
    frq_topic="a gas heated at constant volume, then at constant pressure",
)
