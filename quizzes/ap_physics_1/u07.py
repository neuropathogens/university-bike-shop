import math

from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph

XT = Graph(r"Time $t$ (s)", r"Position $x$ (m)", x=(0, 4, 0.5), y=(-0.15, 0.15, 0.05), series=[],
           curves=[("cart", lambda t: 0.10 * math.cos(math.pi * t), 0)])

S1 = Sec("Defining simple harmonic motion (7.1)", ["7.1"], r"""
\textbf{Simple harmonic motion} (SHM) happens whenever the net force on an object (its restoring force) is proportional to its displacement from equilibrium and points back toward equilibrium:
\[ F_{net} = -kx . \]
A mass on an ideal spring obeys this exactly. A simple pendulum obeys it approximately for small angles (less than about $15^\circ$), since the component of gravity along the arc, $-mg\sin\theta$, is close to $-mg\theta$.

\begin{terms}
Equilibrium position & where the net force is zero; for a hanging spring, where it is stretched by $mg/k$, not its natural length \\
Amplitude $A$ & the greatest displacement from equilibrium \\
Period $T$ and frequency $f$ & time for one full cycle; cycles per second, $f = 1/T$ (Hz) \\
\end{terms}

\begin{trap}
A ball bouncing on a floor repeats its motion but is \emph{not} SHM: the force on it (gravity, then a sudden push from the floor) is not proportional to its displacement.
\end{trap}
""", checks=[
    Q("7.1 Restoring force", r"For which net force $F$ on an object, with displacement $x$ from equilibrium, will the object undergo simple harmonic motion?",
      r"$F = -kx$", [r"$F = -k$", r"$F = kx$", r"$F = -kx^2$"],
      r"SHM needs a restoring force proportional to the displacement and opposite to it.",
      [r"Proportional to $x$: the force grows linearly with displacement.", r"Minus sign: it points back toward equilibrium."],
      [r"a constant force does not depend on displacement; it gives constant acceleration.",
       r"points away from equilibrium, pushing the object farther away.",
       r"is not proportional to $x$ (and pushes the same way on both sides)."]),
])

S2 = Sec("Frequency and period of SHM (7.2)", ["7.2"], r"""
\[ T_s = 2\pi\sqrt{\frac{m}{k}} \ \ (\text{mass on a spring}), \qquad T_p = 2\pi\sqrt{\frac{\ell}{g}} \ \ (\text{simple pendulum}), \qquad f = \frac1T . \]

\begin{compare}{Change}{Spring--mass period}{Pendulum period}
Mass $\times 4$ & $\times 2$ & no change \\
Spring constant or $g$ $\times 4$ & $\div 2$ & $\div 2$ (for $g$) \\
Length $\times 4$ & -- & $\times 2$ \\
Amplitude doubled & no change & no change (small angles) \\
\end{compare}

\begin{trap}
The period of SHM does not depend on the amplitude. A larger swing covers more distance but moves faster, and the two effects cancel exactly.
\end{trap}
""", checks=[
    Q("7.2 Spring period", r"A $0.50$ kg mass oscillates on a spring with $k = 50$ N/m. What is the period?",
      r"$0.63$ s", [r"$0.10$ s", r"$63$ s", r"$1.6$ s"],
      r"$T = 2\pi\sqrt{m/k} = 2\pi\sqrt{0.010} = 2\pi(0.10) = 0.63$ s.",
      [r"$m/k = 0.50/50 = 0.010\ \mathrm{s^2}$."],
      [r"is $\sqrt{m/k}$ without the $2\pi$.",
       r"inverts the ratio inside the root: $2\pi\sqrt{k/m}$.",
       r"is the frequency, $1/T$, in Hz."], sort=True),
    Q("7.2 Pendulum length", r"A pendulum's length is increased to four times its original value. What happens to its period?",
      r"It doubles.", [r"It quadruples.", r"It is halved.", r"It does not change."],
      r"$T \propto \sqrt{\ell}$, so $\sqrt4 = 2$.",
      [r"$T' = 2\pi\sqrt{4\ell/g} = 2T$."],
      [r"forgets the square root.",
       r"a longer pendulum swings more slowly.",
       r"the period depends on the length."]),
])

S3 = Sec("Representing and analyzing SHM (7.3)", ["7.3"], r"""
Starting from maximum displacement at $t = 0$, position varies as a cosine:
\[ x(t) = A\cos(2\pi f t). \]
The velocity and acceleration graphs are also sinusoids with the same period, shifted by a quarter cycle.

\begin{compare}{Position}{Speed}{Acceleration (and net force)}
Equilibrium, $x = 0$ & maximum & zero \\
Turning points, $x = \pm A$ & zero & maximum size, pointing toward equilibrium \\
In between & & $a = -\tfrac{k}{m}x$: opposite to the displacement \\
\end{compare}

On a position--time graph, the speed is greatest where the curve is steepest (crossing $x = 0$), and the acceleration is greatest at the peaks and troughs, where the curve bends most sharply.
""", checks=[
    Q("7.3 Turning point", r"An object in simple harmonic motion is at its maximum displacement from equilibrium. Which quantity is zero at that instant?",
      r"its velocity", [r"its acceleration", r"the net force on it", r"the system's potential energy"],
      r"At a turning point the object momentarily stops before reversing; the restoring force and acceleration are at their largest.",
      [r"$v = 0$ at $x = \pm A$; $|a|$ is maximum there."],
      [r"is greatest at the turning points.",
       r"is greatest at the turning points: $F = -kA$.",
       r"is greatest at the turning points: $U = \tfrac12 kA^2$."]),
])

S4 = Sec("Energy of simple harmonic oscillators (7.4)", ["7.4"], r"""
For a spring--mass system with no friction, the total mechanical energy is constant and set by the amplitude:
\[ E = \tfrac12 kA^2 = \tfrac12 mv_{max}^2 = \tfrac12 mv^2 + \tfrac12 kx^2 . \]
Energy moves back and forth between kinetic (all of it at equilibrium) and potential (all of it at the turning points). Doubling the amplitude quadruples the energy and doubles the maximum speed. For a pendulum the same trade-off is between kinetic and gravitational potential energy.

\begin{example}
A $0.50$ kg cart on a spring with $k = 200$ N/m oscillates with amplitude $0.10$ m: $E = \tfrac12(200)(0.10)^2 = 1.0$ J, so $v_{max} = \sqrt{2E/m} = 2.0$ m/s.
\end{example}
""", checks=[
    Q("7.4 Total energy", r"A cart on a spring ($k = 200$ N/m) oscillates with amplitude $0.10$ m. What is the total mechanical energy of the system?",
      r"$1.0$ J", [r"$2.0$ J", r"$10$ J", r"$20$ J"],
      r"$E = \tfrac12 kA^2 = \tfrac12(200)(0.010) = 1.0$ J.",
      [r"All the energy is elastic at the turning point."],
      [r"leaves out the $\tfrac12$.",
       r"is $\tfrac12 kA$, without squaring $A$.",
       r"is $kA$, the maximum force in newtons."], sort=True),
])

QS = [
    Set("Period and frequency (7.1--7.2)", [
        Q("7.2 Changing the mass", r"The mass on a spring is replaced by one four times as large. What happens to the period of oscillation?",
          r"It doubles.", [r"It quadruples.", r"It is halved.", r"It does not change."],
          r"$T = 2\pi\sqrt{m/k} \propto \sqrt m$.",
          [r"$\sqrt4 = 2$."],
          [r"forgets the square root.",
           r"a heavier mass oscillates more slowly.",
           r"that is true for a pendulum, not a spring."]),
        Q("7.2 Pendulum on the Moon", r"A pendulum has a period of $2.0$ s on Earth. What is its period on the Moon, where $g = 1.6\ \mathrm{m/s^2}$?",
          r"$4.9$ s", [r"$12$ s", r"$0.81$ s", r"$2.0$ s"],
          r"$T \propto 1/\sqrt g$: $T_{Moon} = 2.0\sqrt{9.8/1.6} = 4.9$ s.",
          [r"$\sqrt{9.8/1.6} = 2.47$."],
          [r"forgets the square root.",
           r"divides by the factor instead of multiplying: weaker gravity means a longer period.",
           r"the pendulum period depends on $g$."], sort=True),
        Q("7.2 Amplitude", r"A mass on a spring oscillates with amplitude $A$. It is set oscillating again with amplitude $2A$. The period",
          r"stays the same", [r"doubles", r"is halved", r"increases by a factor of $\sqrt2$"],
          r"$T = 2\pi\sqrt{m/k}$ has no amplitude in it.",
          [r"Twice the distance, but twice the speed at each point."],
          [r"the larger distance is covered at higher speed.",
           r"the period does not depend on amplitude.",
           r"the period does not depend on amplitude."]),
        Q("7.2 Spring constant", r"A $0.20$ kg mass on a spring oscillates with a period of $0.40$ s. What is the spring constant?",
          r"$49$ N/m", [r"$3.1$ N/m", r"$20$ N/m", r"$1.3$ N/m"],
          r"$k = 4\pi^2 m/T^2 = 4\pi^2(0.20)/(0.16) = 49$ N/m.",
          [r"Square $T = 2\pi\sqrt{m/k}$: $T^2 = 4\pi^2 m/k$."],
          [r"is $2\pi m/T$.",
           r"divides by $T$ instead of $T^2$.",
           r"leaves out the $4\pi^2$."], sort=True),
        Q("7.2 Frequency", r"A pendulum completes $30$ full oscillations in $45$ s. What is its frequency?",
          r"$0.67$ Hz", [r"$1.5$ Hz", r"$4.2$ Hz", r"$0.022$ Hz"],
          r"$f = 30/45 = 0.67$ oscillations per second.",
          [r"$T = 45/30 = 1.5$ s and $f = 1/T$."],
          [r"is the period in seconds.",
           r"is $2\pi f$ in rad/s, not the frequency.",
           r"divides $1$ by the total time, ignoring the number of oscillations."], sort=True),
    ]),
    Set("A position--time graph (7.3)", [
        Q("7.3 Reading the graph", r"What are the period and the amplitude of the motion?",
          r"period $2.0$ s, amplitude $0.10$ m", [r"period $1.0$ s, amplitude $0.10$ m", r"period $2.0$ s, amplitude $0.20$ m", r"period $4.0$ s, amplitude $0.20$ m"],
          r"The cart returns to $x = +0.10$ m at $t = 2.0$ s; the amplitude is measured from equilibrium ($x = 0$) to a peak.",
          [r"One cycle: peak to peak, $0$ to $2.0$ s.", r"Amplitude: $0.10$ m, not the $0.20$ m peak-to-trough distance."],
          [r"is the time from a peak to the next trough, half a period.",
           r"is the peak-to-trough distance, twice the amplitude.",
           r"is the whole time shown and the peak-to-trough distance."]),
        Q("7.3 Greatest speed", r"At which of these times is the cart moving fastest?",
          r"$t = 0.5$ s", [r"$t = 0$", r"$t = 1.0$ s", r"$t = 2.0$ s"],
          r"The speed is greatest where the graph is steepest, which is where it crosses $x = 0$.",
          [r"At $t = 0.5$ s the cart passes through equilibrium."],
          [r"the graph is flat at a peak: the cart is momentarily at rest.",
           r"the graph is flat at a trough: momentarily at rest.",
           r"another peak: momentarily at rest."], sort=True),
        Q("7.3 Acceleration", r"At $t = 1.0$ s, the cart's acceleration is",
          r"greatest in size and in the $+x$ direction", [r"zero", r"greatest in size and in the $-x$ direction", r"small and in the $-x$ direction"],
          r"At $t = 1.0$ s the cart is at $x = -0.10$ m, its greatest displacement in the $-x$ direction; the restoring force, and so the acceleration, is largest and points toward $+x$.",
          [r"$a = -\tfrac{k}{m}x$ with $x = -A$."],
          [r"the acceleration is zero at equilibrium, not at the turning points.",
           r"the acceleration points opposite the displacement.",
           r"the acceleration is largest at the turning points."]),
        Q("7.2 Spring constant from the graph", r"What is the spring constant?",
          r"$4.9$ N/m", [r"$1.6$ N/m", r"$9.9$ N/m", r"$20$ N/m"],
          r"$k = 4\pi^2 m/T^2 = 4\pi^2(0.50)/(2.0)^2 = 4.9$ N/m.",
          [r"Period from the graph: $2.0$ s."],
          [r"is $2\pi m/T$.",
           r"divides by $T$, not $T^2$.",
           r"uses a period of $1.0$ s."], sort=True),
        Q("7.4 Maximum speed", r"What is the cart's maximum speed?",
          r"$0.31$ m/s", [r"$0.10$ m/s", r"$0.63$ m/s", r"$0.050$ m/s"],
          r"$v_{max} = A\sqrt{k/m} = 2\pi A/T = 2\pi(0.10)/2.0 = 0.31$ m/s.",
          [r"Energy: $\tfrac12 kA^2 = \tfrac12 mv_{max}^2$, so $v_{max} = A\sqrt{k/m}$."],
          [r"is the amplitude divided by $1$ s.",
           r"uses a period of $1.0$ s.",
           r"is $A/T$, without the $2\pi$."], sort=True),
    ], stim=r"A $0.50$ kg cart attached to a horizontal spring oscillates on a level track with negligible friction. The graph shows its position $x$ as a function of time $t$, with $x = 0$ at equilibrium.",
        fig=XT, stim_title="Questions 6--10"),
    Set("Energy in SHM (7.4)", [
        Q("7.4 Maximum speed from energy", r"A $0.50$ kg mass on a spring with $k = 200$ N/m oscillates with amplitude $0.10$ m. What is its maximum speed?",
          r"$2.0$ m/s", [r"$4.0$ m/s", r"$1.4$ m/s", r"$20$ m/s"],
          r"$\tfrac12 kA^2 = \tfrac12 mv_{max}^2$: $v_{max} = A\sqrt{k/m} = 0.10\sqrt{400} = 2.0$ m/s.",
          [r"$E = 1.0$ J; $v = \sqrt{2E/m}$."],
          [r"forgets the square root.",
           r"drops the factor 2 inside the root: $\sqrt{E/m}$.",
           r"is $\sqrt{k/m}$, which still has to be multiplied by $A$."], sort=True),
        Q("7.4 Equal energies", r"A mass on a spring oscillates with amplitude $A$. At what displacement from equilibrium are its kinetic energy and the elastic potential energy equal?",
          r"$x = A/\sqrt2$", [r"$x = A/2$", r"$x = A/4$", r"$x = 0$"],
          r"Equal shares means $U = \tfrac12 E$: $\tfrac12 kx^2 = \tfrac14 kA^2$, so $x = A/\sqrt2 \approx 0.71A$.",
          [r"$U \propto x^2$, so half the energy needs $x^2 = A^2/2$."],
          [r"at $A/2$ the potential energy is only a quarter of the total.",
           r"at $A/4$ the potential energy is $1/16$ of the total.",
           r"at equilibrium all the energy is kinetic."]),
        Q("7.4 Doubling the amplitude", r"The amplitude of a spring--mass oscillator is doubled. Its total mechanical energy",
          r"quadruples", [r"doubles", r"stays the same", r"increases by a factor of $\sqrt2$"],
          r"$E = \tfrac12 kA^2 \propto A^2$.",
          [r"$2^2 = 4$."],
          [r"energy goes as $A^2$, not $A$.",
           r"the stretch at the turning point is larger, so more energy is stored.",
           r"energy goes as $A^2$."]),
    ]),
]

UNIT = Unit(7, "oscillations", "Oscillations", "5--8\\%", "7.1--7.4",
    abstract=r"""Unit 7 is about simple harmonic motion: what makes motion simple harmonic (a restoring force proportional to displacement), the period and frequency of a mass on a spring and of a simple pendulum, reading and sketching graphs of position, velocity and acceleration, and the exchange of kinetic and potential energy in an oscillator. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students want to determine the gravitational field $g$ in their classroom using a simple pendulum. They have string, a small metal bob, a clamp stand, a meter stick, a protractor and a stopwatch.

\medskip
Their data for five lengths $\ell$ (each period found by timing 10 oscillations) are below.

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$\ell$ (m) & 0.20 & 0.40 & 0.60 & 0.80 & 1.00 \\ \midrule
$T$ (s) & 0.90 & 1.27 & 1.55 & 1.80 & 2.01 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe a procedure the students could use to collect these data. Include how each quantity is measured and at least one step that reduces experimental uncertainty.",
             r"1 pt: measure $\ell$ with the meter stick from the pivot to the center of the bob. 1 pt: release from a small angle (below about $15^\circ$, checked with the protractor) and time several full oscillations (e.g.\ 10), dividing by the number. 1 pt: repeat with different lengths, and repeat each timing several times and average.",
             r"Timing a single swing, or measuring $\ell$ to the bottom of the bob only."),
        Part("b", 2, r"Indicate what quantities the students should graph to obtain a straight line whose slope can be used to determine $g$. Express $g$ in terms of that slope.",
             r"1 pt: since $T^2 = (4\pi^2/g)\ell$, graph $T^2$ versus $\ell$. 1 pt: $g = 4\pi^2/\text{slope}$.",
             r"Graphing $T$ versus $\ell$, which is not linear."),
        Part("c", 3, r"Calculate the values needed for your graph, determine the slope of a best-fit line, and use it to calculate $g$.",
             r"1 pt: $T^2 = 0.81,\ 1.61,\ 2.40,\ 3.24,\ 4.04\ \mathrm{s^2}$. 1 pt: slope about $4.0\ \mathrm{s^2/m}$ (accept $3.9$--$4.1$). 1 pt: $g = 4\pi^2/4.04 \approx 9.8\ \mathrm{m/s^2}$.",
             r"Using a single data pair, which ignores the scatter."),
        Part("d", 2, r"Another group releases their pendulum from about $40^\circ$ every time and otherwise follows the same method. Their measured periods are all slightly longer. Explain how this affects the value of $g$ they find.",
             r"1 pt: at large angles the restoring force is less than proportional to the displacement ($\sin\theta < \theta$), so the period is longer than $2\pi\sqrt{\ell/g}$. 1 pt: longer periods give a larger slope of $T^2$ versus $\ell$, so their calculated $g = 4\pi^2/\text{slope}$ is too small.",
             r"Saying the amplitude does not affect the period without noting the small-angle condition."),
    ], mins=28),
    frq_topic="finding g from a pendulum",
)
