from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Defining simple harmonic motion (7.1)", ["7.1"], r"""
Simple harmonic motion (SHM) happens whenever the net force (or torque) is proportional to the displacement from equilibrium and points back toward it:
\[ F = -kx \quad\Rightarrow\quad \frac{d^2x}{dt^2} = -\frac{k}{m}x = -\omega^2 x, \qquad x(t) = A\cos(\omega t + \phi). \]
To show a system is in SHM, get its equation of motion into the form $\ddot x = -(\text{positive constant})\,x$; the constant is $\omega^2$. Near the bottom of \emph{any} smooth potential-energy well, $U \approx \tfrac12 U''(x_0)(x - x_0)^2$, so small oscillations are SHM with effective $k = U''(x_0)$.

\begin{terms}
Amplitude $A$ & Maximum displacement; set by the initial conditions, not by the system. \\
Angular frequency $\omega$ & rad/s; $\omega = 2\pi f = 2\pi/T$. \\
Phase constant $\phi$ & Sets where the motion starts: released from rest at $x = +A$ gives $\phi = 0$. \\
\end{terms}
""", checks=[
    Q("7.1 Condition for SHM", r"Which net force, acting on a mass on a frictionless surface, produces simple harmonic motion? ($x$ is the displacement from $x = 0$.)",
      r"$F = -4x$", [r"$F = 4x$", r"$F = -4x^2$", r"$F = -4$"],
      r"SHM needs a restoring force proportional to $x$: $F = -kx$ with $k > 0$.",
      [r"$F = -4x$ gives $\ddot x = -(4/m)x$, so $\omega = \sqrt{4/m}$."],
      [r"pushes the mass away from equilibrium, so it runs off rather than oscillating.", r"is not proportional to $x$ (and points the same way on both sides).", r"is constant, giving uniform acceleration, not oscillation."]),
])

S2 = Sec("Frequency and period (7.2)", ["7.2"], r"""
\[ \text{Mass on a spring: } \omega = \sqrt{\frac{k}{m}}, \qquad T = 2\pi\sqrt{\frac{m}{k}}, \qquad f = \frac{1}{T}. \]
\begin{itemize}
\item The period does not depend on amplitude (for an ideal spring), so a larger push gives a faster, not longer, oscillation.
\item A vertical spring has the same period as a horizontal one. Gravity only shifts the equilibrium, by $\Delta x = mg/k$; this also gives $T = 2\pi\sqrt{\Delta x/g}$.
\item Springs that share the load side by side add ($k_1 + k_2$). A mass between two springs attached to opposite walls also feels $k_1 + k_2$.
\end{itemize}
""", checks=[
    Q("7.2 Scaling the period", r"A block on a spring has period $T$. The block is replaced by one with four times the mass. What is the new period?",
      r"$2T$", [r"$4T$", r"$T/2$", r"$T$"],
      r"$T = 2\pi\sqrt{m/k} \propto \sqrt m$, so $\sqrt4 = 2$.",
      [r"$T_2/T_1 = \sqrt{4m/m} = 2$."],
      [r"forgets the square root.", r"inverts the dependence; heavier blocks oscillate more slowly.", r"assumes the period is set by the spring alone."]),
])

S3 = Sec("Representing and analyzing SHM (7.3)", ["7.3"], r"""
Differentiate $x = A\cos(\omega t + \phi)$:
\[ v = -A\omega\sin(\omega t + \phi), \qquad a = -A\omega^2\cos(\omega t + \phi) = -\omega^2 x, \qquad v_{max} = A\omega, \qquad a_{max} = A\omega^2. \]
\begin{compare}{Position}{Speed}{Acceleration}
$x = \pm A$ (turning points) & zero & maximum, pointing toward equilibrium \\
$x = 0$ (equilibrium) & maximum & zero \\
\end{compare}
On graphs, $v(t)$ is a quarter cycle ahead of $x(t)$, and $a(t)$ is the mirror image of $x(t)$. Velocity is the slope of the $x$--$t$ graph.
""", checks=[
    Q("7.3 Maximum speed", r"A block's position is $x(t) = 0.050\cos(10t)$, in meters and seconds. What is its maximum speed?",
      r"$0.50$ m/s", [r"$5.0$ m/s", r"$0.050$ m/s", r"$0.080$ m/s"],
      r"$v_{max} = A\omega = (0.050)(10) = 0.50$ m/s.",
      [r"Amplitude 0.050 m, $\omega = 10$ rad/s.", r"$v_{max} = 0.50$ m/s."],
      [r"is the maximum acceleration, $A\omega^2$, in m/s$^2$.", r"is the amplitude.", r"is $Af$, using the frequency $f = \omega/2\pi = 1.6$ Hz in place of $\omega$."], sort=True),
])

S4 = Sec("Energy of simple harmonic oscillators (7.4)", ["7.4"], r"""
\[ E = \tfrac12 kA^2 = \tfrac12 mv^2 + \tfrac12 kx^2, \qquad v(x) = \pm\omega\sqrt{A^2 - x^2}. \]
Energy sloshes between kinetic and potential twice each cycle; the total is fixed by the amplitude. At $x = A/2$, $U = \tfrac14 E$ and $K = \tfrac34 E$. Doubling the amplitude quadruples the energy and doubles $v_{max}$ and $a_{max}$, but leaves the period unchanged.
""", checks=[
    Q("7.4 Energy split", r"A block oscillates on a spring with amplitude $A$. What fraction of the total energy is kinetic when the block is at $x = A/2$?",
      r"$3/4$", [r"$1/2$", r"$1/4$", r"$\sqrt3/2$"],
      r"$U = \tfrac12 k(A/2)^2 = \tfrac14\left(\tfrac12 kA^2\right)$, so $U = E/4$ and $K = 3E/4$.",
      [r"Potential energy scales as $x^2$: $(1/2)^2 = 1/4$.", r"$K = E - U = \tfrac34 E$."],
      [r"assumes energy splits evenly at half the amplitude.", r"is the potential-energy fraction.", r"is the speed fraction $v/v_{max}$, not the energy fraction."]),
])

S5 = Sec("Simple and physical pendulums (7.5)", ["7.5"], r"""
For small angles ($\sin\theta \approx \theta$, good to about $15^\circ$), a pendulum's restoring torque is proportional to its angle, giving SHM:
\[ \text{Simple: } T = 2\pi\sqrt{\frac{L}{g}}, \qquad \text{Physical: } T = 2\pi\sqrt{\frac{I}{mgd}}, \]
where $I$ is the rotational inertia about the pivot and $d$ the distance from the pivot to the center of mass. A simple pendulum is the special case $I = mL^2$, $d = L$. The period is independent of the mass and (for small angles) of the amplitude.
\begin{example}
A uniform rod of length $L$ swinging from one end: $I = \tfrac13 mL^2$, $d = L/2$, so $T = 2\pi\sqrt{\dfrac{2L}{3g}}$, shorter than a simple pendulum of the same length.
\end{example}
""", checks=[
    Q("7.5 Pendulum on the Moon", r"A pendulum clock is taken to the Moon, where $g$ is one sixth of Earth's. By what factor does its period change?",
      r"It becomes $\sqrt6$ times longer.", [r"It becomes 6 times longer.", r"It becomes $\sqrt6$ times shorter.", r"It does not change."],
      r"$T = 2\pi\sqrt{L/g} \propto 1/\sqrt g$; dividing $g$ by 6 multiplies $T$ by $\sqrt6 \approx 2.4$.",
      [r"$T_{Moon}/T_{Earth} = \sqrt{g_E/g_M} = \sqrt6$."],
      [r"forgets the square root.", r"reverses the dependence; weaker gravity means slower swings.", r"the period depends on $g$ (it is a mass on a spring whose period does not)."]),
    Q("7.5 Physical pendulum", r"A uniform rod of length $L$ swings with small amplitude about a pivot at one end. What is its period?",
      r"$2\pi\sqrt{2L/(3g)}$", [r"$2\pi\sqrt{L/g}$", r"$2\pi\sqrt{L/(2g)}$", r"$2\pi\sqrt{L/(3g)}$"],
      r"$T = 2\pi\sqrt{I/(mgd)}$ with $I = \tfrac13 mL^2$ and $d = L/2$: $\dfrac{I}{mgd} = \dfrac{2L}{3g}$.",
      [r"$I/(mgd) = \dfrac{\frac13 mL^2}{mg(L/2)} = \dfrac{2L}{3g}$."],
      [r"treats the rod as a point mass at its far end.", r"treats it as a point mass at its center.", r"uses $d = L$ instead of $L/2$."]),
])

QS1 = [
    Q("7.1 Equation of motion", r"An object's motion obeys $\dfrac{d^2x}{dt^2} = -9.0\,x$ (SI units). What is its period?",
      r"$2.1$ s", [r"$0.33$ s", r"$0.70$ s", r"$19$ s"],
      r"Comparing with $\ddot x = -\omega^2 x$: $\omega = 3.0$ rad/s, so $T = 2\pi/3.0 = 2.1$ s.",
      [r"$\omega^2 = 9.0 \Rightarrow \omega = 3.0$ rad/s.", r"$T = 2\pi/\omega = 2.09$ s."],
      [r"is $1/\omega$, which drops the $2\pi$.", r"uses $\omega = 9.0$: $2\pi/9.0$.", r"is $2\pi\omega$, upside down."], sort=True),
    Q("7.1 Small oscillations in a potential well", r"Near its equilibrium point, a 0.50 kg particle's potential energy is $U(x) = 4.0x^2$ (J, with $x$ in m). What is the period of small oscillations?",
      r"$1.6$ s", [r"$2.2$ s", r"$0.64$ s", r"$4.0$ s"],
      r"Match $U = \tfrac12 kx^2$: $k = 8.0$ N/m. Then $T = 2\pi\sqrt{m/k} = 2\pi\sqrt{0.50/8.0} = 1.6$ s.",
      [r"$k = d^2U/dx^2 = 8.0$ N/m.", r"$\omega = \sqrt{8.0/0.50} = 4.0$ rad/s; $T = 2\pi/4.0 = 1.57$ s."],
      [r"uses $k = 4.0$ N/m, missing the $\tfrac12$ in $U = \tfrac12 kx^2$.", r"is the frequency $f = \omega/2\pi$ in Hz, not the period.", r"is $\omega$ in rad/s, not the period."], sort=True),
    Q("7.2 Frequency", r"A 0.40 kg block oscillates on a spring with $k = 160$ N/m. What is its frequency?",
      r"$3.2$ Hz", [r"$20$ Hz", r"$0.31$ Hz", r"$400$ Hz"],
      r"$\omega = \sqrt{k/m} = 20$ rad/s, and $f = \omega/2\pi = 3.2$ Hz.",
      [r"$\omega = \sqrt{160/0.40} = 20$ rad/s.", r"$f = 20/2\pi = 3.18$ Hz."],
      [r"is $\omega$ in rad/s, not $f$ in Hz.", r"is the period in seconds.", r"is $\omega^2$."], sort=True),
    Q("7.2 Vertical spring", r"A block hung from a spring stretches it 9.8 cm at equilibrium. The block is then pulled down slightly and released. What is the period of its oscillation? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$0.63$ s", [r"$0.10$ s", r"$0.20$ s", r"$6.3$ s"],
      r"At equilibrium $k\Delta x = mg$, so $k/m = g/\Delta x$ and $T = 2\pi\sqrt{\Delta x/g} = 2\pi\sqrt{0.098/9.8} = 0.63$ s.",
      [r"$\sqrt{\Delta x/g} = \sqrt{0.010} = 0.10$ s.", r"$T = 2\pi(0.10) = 0.63$ s."],
      [r"is $\sqrt{\Delta x/g}$, leaving out $2\pi$.", r"is $2\sqrt{\Delta x/g}$, using 2 instead of $2\pi$.", r"uses the stretch in centimeters as if it were meters: $2\pi\sqrt{9.8/9.8}$."], sort=True),
    Q("7.2 Two springs", r"A block on a frictionless table is attached between two walls by two springs, $k_1$ on its left and $k_2$ on its right. Both springs are at natural length when the block is at rest. What is the period of oscillation?",
      r"$2\pi\sqrt{m/(k_1 + k_2)}$", [r"$2\pi\sqrt{m(k_1 + k_2)/(k_1k_2)}$", r"$2\pi\sqrt{m/|k_1 - k_2|}$", r"$2\pi\sqrt{2m/(k_1 + k_2)}$"],
      r"Displace the block by $x$: the left spring stretches and pulls back with $k_1x$, the right one compresses and pushes back with $k_2x$. Net force $-(k_1 + k_2)x$.",
      [r"Both springs push the block toward equilibrium.", r"$k_{eff} = k_1 + k_2$."],
      [r"uses the series combination, which applies to springs hooked end to end on one side.", r"assumes the springs oppose each other; both restore.", r"has a stray factor of 2."]),
    Q("7.3 Maximum acceleration", r"A particle moves as $x(t) = 0.20\cos(5.0t + \pi/2)$, in meters and seconds. What is the magnitude of its maximum acceleration?",
      r"$5.0\ \mathrm{m/s^2}$", [r"$1.0\ \mathrm{m/s^2}$", r"$25\ \mathrm{m/s^2}$", r"$0.20\ \mathrm{m/s^2}$"],
      r"$a_{max} = A\omega^2 = (0.20)(25) = 5.0\ \mathrm{m/s^2}$; the phase does not change the maximum.",
      [r"$A = 0.20$ m, $\omega = 5.0$ rad/s.", r"$a_{max} = 5.0\ \mathrm{m/s^2}$."],
      [r"is $v_{max} = A\omega$.", r"is $\omega^2$ alone.", r"is the amplitude."], sort=True),
    Q("7.3 Phase", r"A block on a spring is pulled to $x = +A$ and released from rest at $t = 0$. At $t = T/4$, the block is",
      r"at $x = 0$, moving in the $-x$ direction at maximum speed", [r"at $x = 0$, momentarily at rest", r"at $x = -A$, momentarily at rest", r"at $x = 0$, moving in the $+x$ direction at maximum speed"],
      r"$x = A\cos(\omega t)$; at $\omega t = \pi/2$, $x = 0$ and $v = -A\omega\sin(\pi/2) = -A\omega$.",
      [r"A quarter cycle takes it from $+A$ to equilibrium.", r"It is heading toward $-A$, so $v < 0$, with $|v| = v_{max}$."],
      [r"equilibrium is where the speed is largest, not zero.", r"is where it is at $t = T/2$.", r"has the direction wrong; it moves from $+A$ toward $-A$."]),
    Q("7.3 Acceleration at equilibrium", r"For a mass on a spring in SHM, what is the acceleration as it passes through the equilibrium position?",
      r"Zero", [r"Maximum, toward the center", r"Equal to $g$", r"Maximum, in the direction of motion"],
      r"$a = -\omega^2 x$, and $x = 0$ at equilibrium. The net force is zero there; the mass coasts through at maximum speed.",
      [r"At $x = 0$: $F = -kx = 0$, so $a = 0$."],
      [r"describes the turning points.", r"has no basis for a horizontal spring; even vertically the net force at equilibrium is zero.", r"would mean the speed is still increasing past equilibrium; it peaks there."]),
    Q("7.4 Speed from energy", r"A 0.50 kg block on a spring ($k = 200$ N/m) oscillates with amplitude 0.10 m. What is its speed when $x = 0.060$ m?",
      r"$1.6$ m/s", [r"$2.0$ m/s", r"$1.2$ m/s", r"$0.80$ m/s"],
      r"$v = \omega\sqrt{A^2 - x^2}$ with $\omega = 20$ rad/s: $v = 20\sqrt{0.010 - 0.0036} = 20(0.080) = 1.6$ m/s.",
      [r"Energy: $\tfrac12 kA^2 = \tfrac12 mv^2 + \tfrac12 kx^2$.", r"$v = \sqrt{(k/m)(A^2 - x^2)} = 1.6$ m/s."],
      [r"is the maximum speed, $A\omega$, reached at $x = 0$.", r"is $\omega x$, which has no physical meaning here.", r"is $\omega(A - x)$, subtracting before squaring."], sort=True),
    Q("7.4 Changing amplitude", r"The amplitude of a mass--spring oscillator is doubled. Which statement is true?",
      r"The total energy quadruples and the period is unchanged.", [r"The total energy doubles and the period doubles.", r"The total energy quadruples and the period doubles.", r"The maximum speed quadruples and the period is unchanged."],
      r"$E = \tfrac12 kA^2 \propto A^2$; $T = 2\pi\sqrt{m/k}$ does not involve $A$; $v_{max} = A\omega$ doubles.",
      [r"$E \propto A^2$: factor 4.", r"$T$ independent of $A$."],
      [r"energy depends on $A^2$, and the period is independent of $A$.", r"the period does not depend on amplitude.", r"$v_{max} = A\omega$ only doubles."]),
    Q("7.5 Simple pendulum", r"What length of simple pendulum has a period of 2.0 s? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$0.99$ m", [r"$3.1$ m", r"$0.50$ m", r"$2.0$ m"],
      r"$L = g\left(\dfrac{T}{2\pi}\right)^2 = 9.8\left(\dfrac{2.0}{2\pi}\right)^2 = 0.99$ m.",
      [r"$T/2\pi = 0.318$ s; squared, 0.101 s$^2$.", r"$L = 9.8 \times 0.101 = 0.99$ m."],
      [r"forgets to square $T/2\pi$: $9.8(0.318)$.", r"squares $2\pi$ but not $T$: $9.8(2.0)/(2\pi)^2$.", r"assumes $L$ (m) equals $T$ (s)."], sort=True),
    Q("7.5 Physical pendulum", r"A uniform meter stick (1.00 m) swings with small amplitude about a pivot at one end. What is its period? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$1.6$ s", [r"$2.0$ s", r"$1.4$ s", r"$1.2$ s"],
      r"$T = 2\pi\sqrt{I/(mgd)} = 2\pi\sqrt{2L/(3g)} = 2\pi\sqrt{0.0680} = 1.6$ s.",
      [r"$I = \tfrac13 mL^2$, $d = 0.50$ m.", r"$T = 2\pi\sqrt{\dfrac{2(1.00)}{3(9.8)}} = 1.64$ s."],
      [r"is a simple pendulum 1.00 m long, which puts all the mass at the end.", r"is a simple pendulum 0.50 m long, which puts all the mass at the center.", r"uses $d = L$ with $I = \tfrac13 mL^2$."], sort=True),
]

UNIT = Unit(
    n=7, slug="oscillations", title="Oscillations", weight="10--15\\%", topics="7.1--7.5",
    abstract=r"""Unit 7 studies simple harmonic motion: what makes motion harmonic (7.1), the period and frequency of mass--spring systems (7.2), the functions and graphs of position, velocity, and acceleration (7.3), energy in an oscillator (7.4), and simple and physical pendulums (7.5). The calculus is central: SHM is any motion whose equation reduces to $\ddot x = -\omega^2 x$. The free-response question is an experiment on a spring's period. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5],
    qsections=[("SHM and its period (7.1--7.2)", QS1[:5]), ("Analyzing SHM (7.3--7.4)", QS1[5:10]), ("Pendulums (7.5)", QS1[10:])],
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students want to find the spring constant $k$ of a spring by timing oscillations. They hang the spring from a rod, attach a mass $m$, set it oscillating vertically, and determine the period $T$. They repeat this for several masses.

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$m$ (kg) & 0.10 & 0.20 & 0.30 & 0.40 & 0.50 \\ \midrule
$T$ (s) & 0.49 & 0.66 & 0.79 & 0.91 & 1.02 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe how the students should measure each period to reduce uncertainty. Explain why your method reduces uncertainty.",
             r"1 pt: time many oscillations (e.g.\ 10 or 20) with a stopwatch and divide by the number. 1 pt: repeat each timing several times and average, or start timing as the mass passes equilibrium. 1 pt: reaction-time error is fixed per measurement, so spreading it over many cycles makes it a small fraction of the total; the mass moves fastest at equilibrium, so the instant is sharper.",
             r"``Time one oscillation carefully''; no explanation of why."),
        Part("b", 2, r"Indicate what the students should graph to get a straight line whose slope can be used to find $k$. Express $k$ in terms of the slope.",
             r"1 pt: $T^2 = \dfrac{4\pi^2}{k}m$, so graph $T^2$ versus $m$. 1 pt: $k = 4\pi^2/\text{slope}$.",
             r"Graphing $T$ versus $m$, which is not linear."),
        Part("c", 3, r"Calculate the quantities to be graphed, determine the slope of the best-fit line, and use it to calculate $k$.",
             r"1 pt: $T^2 = 0.240,\ 0.436,\ 0.624,\ 0.828,\ 1.04$ s$^2$. 1 pt: slope $\approx 2.0$ s$^2$/kg from a best-fit line (accept 1.9--2.1). 1 pt: $k = 4\pi^2/2.0 \approx 20$ N/m.",
             r"Using one data pair, e.g.\ $k = 4\pi^2(0.50)/1.02^2$."),
        Part("d", 2, r"The best-fit line does not pass through the origin; its $T^2$-intercept is about $0.036\ \mathrm{s^2}$. Suggest a physical reason for this, and explain how it affects (or does not affect) the value of $k$ found from the slope.",
             r"1 pt: the spring itself has mass, so part of it oscillates too; the effective mass is $m + m_{eff}$ (here $m_{eff} = 0.036 \times k/4\pi^2 \approx 0.018$ kg), shifting every $T^2$ up by the same amount. 1 pt: the shift changes the intercept but not the slope, so $k$ from the slope is unaffected.",
             r"Blaming air resistance, which would not add a constant to $T^2$."),
    ]),
    frq_topic="graphing the period of a mass on a spring",
)
