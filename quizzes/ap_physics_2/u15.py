from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

PE = Graph(r"Frequency $f$ ($10^{14}$ Hz)", r"$K_{max}$ (eV)", x=(0, 16, 2), y=(0, 4, 1),
           series=[Series("data", [(6, 0.20), (8, 1.00), (10, 1.85), (12, 2.65), (14, 3.50)], fit=(0.4125, -2.27))], legend=False)

S1 = Sec("Quantum theory and wave--particle duality (15.1)", ["15.1"], r"""
Light comes in \textbf{photons}, packets of energy
\[ E = hf = \frac{hc}{\lambda}, \qquad h = 6.63 \times 10^{-34}\ \mathrm{J\,s}, \qquad hc = 1240\ \mathrm{eV\,nm}. \]
Matter also behaves as a wave: a particle of momentum $p = mv$ has a \textbf{de Broglie wavelength}
\[ \lambda = \frac{h}{p} . \]
Light shows wave behavior (interference, diffraction) and particle behavior (the photoelectric effect); electrons show particle behavior (tracks, collisions) and wave behavior (diffraction by crystals). Which shows up depends on the experiment. Wave effects of matter are noticeable only when $\lambda$ is comparable to the size of what the particle interacts with, which is why they matter for electrons in atoms and not for baseballs.
""", checks=[
    Q("15.1 Photon energy", r"What is the energy of a photon of wavelength $500$ nm?",
      r"$2.5$ eV", [r"$0.40$ eV", r"$6.2 \times 10^{5}$ eV", r"$4.0 \times 10^{-19}$ eV"],
      r"$E = hc/\lambda = 1240\ \mathrm{eV\,nm}/500\ \mathrm{nm} = 2.48$ eV.",
      [r"In joules: $(6.63 \times 10^{-34})(3.0 \times 10^8)/(500 \times 10^{-9}) = 4.0 \times 10^{-19}$ J."],
      [r"is $\lambda/hc$, upside down.",
       r"multiplies $hc$ by $\lambda$.",
       r"is the energy in joules, labeled in electron volts."], sort=True),
    Q("15.1 de Broglie wavelength", r"What is the de Broglie wavelength of an electron ($m = 9.11 \times 10^{-31}$ kg) moving at $1.0 \times 10^6$ m/s?",
      r"$7.3 \times 10^{-10}$ m", [r"$6.0 \times 10^{-58}$ m", r"$1.4 \times 10^{9}$ m", r"$7.3 \times 10^{-4}$ m"],
      r"$\lambda = h/(mv) = (6.63 \times 10^{-34})/((9.11 \times 10^{-31})(1.0 \times 10^6)) = 7.3 \times 10^{-10}$ m, about the spacing of atoms in a crystal.",
      [r"$p = mv = 9.1 \times 10^{-25}\ \mathrm{kg\,m/s}$."],
      [r"multiplies $h$ by the momentum.",
       r"is $p/h$, upside down.",
       r"leaves out the speed."], sort=True),
])

S2 = Sec("The Bohr model, emission and absorption spectra (15.2--15.3)", ["15.2", "15.3"], r"""
Electrons in atoms occupy only certain \textbf{energy levels}. In the Bohr model of hydrogen, $E_n = -13.6\ \mathrm{eV}/n^2$; the negative values mean the electron is bound, and $0$ is the ionization threshold. (In the Bohr picture the allowed orbits are those that fit a whole number of de Broglie wavelengths.)

\begin{keyidea}[Transitions]
An atom drops from a higher level to a lower one by emitting a photon with exactly the energy difference, $hf = E_{upper} - E_{lower}$; it rises by absorbing a photon with exactly that energy. So each element has its own line spectrum: bright lines in emission (a hot gas), dark lines at the same wavelengths in absorption (cool gas in front of a continuous source).
\end{keyidea}

\textbf{Counting lines.} Atoms in level $n$ can cascade down by any route, so they can emit up to $n(n-1)/2$ different photon energies (fewer if two gaps happen to be equal). The largest gap gives the shortest wavelength.
""", checks=[
    Q("15.3 Hydrogen line", r"A hydrogen atom drops from $n = 3$ ($-1.51$ eV) to $n = 2$ ($-3.40$ eV). What is the wavelength of the emitted photon?",
      r"$656$ nm", [r"$365$ nm", r"$1.89$ nm", r"$821$ nm"],
      r"$\Delta E = 3.40 - 1.51 = 1.89$ eV, so $\lambda = 1240/1.89 = 656$ nm, the red line of hydrogen.",
      [r"$\lambda = hc/\Delta E$."],
      [r"uses the $n = 2$ energy alone ($3.40$ eV).",
       r"is the energy in eV, not a wavelength.",
       r"uses the $n = 3$ energy alone ($1.51$ eV)."], sort=True),
])

S3 = Sec("Blackbody radiation (15.4)", ["15.4"], r"""
Every object emits electromagnetic radiation with a continuous spectrum set by its temperature. As the temperature rises:
\begin{itemize}
\item the object emits more at every wavelength; the total power grows as $T^4$ (Stefan--Boltzmann law, $P = \sigma AT^4$);
\item the peak shifts to shorter wavelengths (Wien's law, $\lambda_{max}T = 2.9 \times 10^{-3}\ \mathrm{m\,K}$), so a heated metal glows red, then orange, then white.
\end{itemize}
Explaining the shape of this spectrum is what first required energy to be quantized (Planck, 1900).
""", checks=[
    Q("15.4 Wien's law", r"The Sun's surface temperature is about $5800$ K. At about what wavelength does its emission peak?",
      r"$500$ nm", [r"$1.7 \times 10^{10}$ nm", r"$2.0 \times 10^{6}$ nm", r"$5800$ nm"],
      r"$\lambda_{max} = (2.9 \times 10^{-3})/5800 = 5.0 \times 10^{-7}$ m $= 500$ nm, in the visible.",
      [r"$\lambda_{max}T = 2.9 \times 10^{-3}\ \mathrm{m\,K}$."],
      [r"multiplies Wien's constant by the temperature instead of dividing.",
       r"is $T$ divided by Wien's constant.",
       r"takes the temperature as the wavelength."], sort=True),
])

S4 = Sec("The photoelectric effect (15.5)", ["15.5"], r"""
Light shining on a metal can eject electrons. The observations that the wave model could not explain:
\begin{itemize}
\item below a \textbf{threshold frequency} no electrons are ejected, however bright the light;
\item above it, electrons appear at once, even in dim light;
\item the maximum kinetic energy of the electrons depends on the frequency, not the intensity; brighter light ejects more electrons.
\end{itemize}
Einstein's explanation: each electron absorbs one photon. With $\phi$ the metal's \textbf{work function} (the least energy needed to free an electron),
\[ K_{max} = hf - \phi, \qquad f_0 = \phi/h . \]
A graph of $K_{max}$ versus $f$ is a straight line of slope $h$ that crosses the frequency axis at $f_0$; extended back, it meets the energy axis at $-\phi$. The \textbf{stopping potential} $\Delta V_s$ that just stops the fastest electrons satisfies $e\Delta V_s = K_{max}$.
""", checks=[
    Q("15.5 Kinetic energy", r"Light of wavelength $250$ nm shines on sodium, whose work function is $2.3$ eV. What is the maximum kinetic energy of the ejected electrons?",
      r"$2.7$ eV", [r"$5.0$ eV", r"$7.3$ eV", r"$0$"],
      r"$hf = 1240/250 = 4.96$ eV, so $K_{max} = 4.96 - 2.3 = 2.7$ eV.",
      [r"$K_{max} = hc/\lambda - \phi$."],
      [r"is the photon energy, before subtracting the work function.",
       r"adds the work function.",
       r"the photon energy is above the work function, so electrons are ejected."], sort=True),
    Q("15.5 Intensity", r"Red light does not eject electrons from a certain metal. What happens if the red light is made ten times brighter?",
      r"Still no electrons are ejected.", [r"Electrons are ejected, with ten times as much kinetic energy.", r"Electrons are ejected after a delay while energy builds up.", r"Electrons are ejected, but slowly."],
      r"Each electron absorbs a single photon; brighter red light means more photons, each still with too little energy.",
      [r"Photon energy depends on frequency, not intensity."],
      [r"intensity changes the number of photons, not their energy.",
       r"electrons cannot store up energy from several photons in this model.",
       r"no photon has enough energy, so none are ejected."]),
])

S5 = Sec("Compton scattering (15.6)", ["15.6"], r"""
A photon carries momentum as well as energy:
\[ p = \frac{h}{\lambda} = \frac{E}{c}. \]
When an X-ray photon scatters off a nearly free electron, the electron recoils, carrying away some energy and momentum. The scattered photon therefore has less energy and a \emph{longer} wavelength; the shift is larger at larger scattering angles. Compton's measurements (1923) showed that the collision obeys conservation of energy and momentum exactly as a particle collision would, strong evidence that photons carry momentum.
""", checks=[
    Q("15.6 Scattered photon", r"An X-ray photon scatters off an electron that was at rest. Compared with the incident photon, the scattered photon has",
      r"a longer wavelength and less energy", [r"a shorter wavelength and more energy", r"the same wavelength, but a new direction", r"a lower speed"],
      r"The recoiling electron takes some of the photon's energy, so $E = hc/\lambda$ falls and $\lambda$ rises.",
      [r"Energy conservation: $E_{photon,i} = E_{photon,f} + K_{electron}$."],
      [r"the electron gains energy, so the photon cannot.",
       r"the photon must give the recoiling electron some energy.",
       r"photons always travel at $c$."]),
])

S6 = Sec("Fission, fusion and nuclear decay (15.7--15.8)", ["15.7", "15.8"], r"""
A nucleus ${}^{A}_{Z}\mathrm{X}$ has $Z$ protons and $A - Z$ neutrons. In every nuclear reaction the total nucleon number $A$ and the total charge $Z$ are conserved.

\begin{compare}{Decay}{What is emitted}{Change in the nucleus}
Alpha & a helium nucleus ${}^4_2\alpha$ & $A - 4$, $Z - 2$ \\
Beta-minus & an electron and an antineutrino & a neutron becomes a proton: $Z + 1$ \\
Beta-plus & a positron and a neutrino & a proton becomes a neutron: $Z - 1$ \\
Gamma & a high-energy photon & no change in $A$ or $Z$; the nucleus drops to a lower energy state \\
\end{compare}

\textbf{Mass and energy.} A nucleus has less mass than its separate nucleons; the difference (mass defect) times $c^2$ is its binding energy. In fission (a heavy nucleus splitting) and fusion (light nuclei joining), the products are more tightly bound and have less total mass, and $\Delta E = \Delta m\,c^2$ is released.

\textbf{Half-life.} Decay is random for each nucleus, but a large sample decays predictably: after each half-life $t_{1/2}$, half the remaining nuclei have decayed, $N = N_0\left(\tfrac12\right)^{t/t_{1/2}}$.
""", checks=[
    Q("15.8 Alpha decay", r"Radium-226 (${}^{226}_{88}\mathrm{Ra}$) undergoes alpha decay. What is the daughter nucleus?",
      r"${}^{222}_{86}\mathrm{Rn}$", [r"${}^{222}_{88}\mathrm{Ra}$", r"${}^{226}_{86}\mathrm{Rn}$", r"${}^{224}_{87}\mathrm{Fr}$"],
      r"An alpha particle carries away $A = 4$ and $Z = 2$: $226 - 4 = 222$ and $88 - 2 = 86$ (radon).",
      [r"Conserve $A$ and $Z$ separately."],
      [r"removes the nucleons but not the charge; the element must change.",
       r"removes the charge but not the nucleons.",
       r"removes only half of each."]),
    Q("15.7 Half-life", r"A sample contains $80$ mg of iodine-131, which has a half-life of $8.0$ days. How much iodine-131 remains after $24$ days?",
      r"$10$ mg", [r"$27$ mg", r"$20$ mg", r"$0$"],
      r"$24$ days is three half-lives: $80 \to 40 \to 20 \to 10$ mg.",
      [r"$N = 80\left(\tfrac12\right)^{24/8.0} = 80/8$."],
      [r"divides by $3$ instead of halving three times.",
       r"stops after two half-lives.",
       r"decay never removes every nucleus in a finite number of half-lives."], sort=True),
])

QS = [
    Set("Photons and matter waves (15.1)", [
        Q("15.1 Violet photon", r"What is the energy of a photon of violet light with a wavelength of $400$ nm?",
          r"$3.1$ eV", [r"$0.32$ eV", r"$5.0 \times 10^{-19}$ eV", r"$7.5 \times 10^{14}$ eV"],
          r"$E = 1240\ \mathrm{eV\,nm}/400\ \mathrm{nm} = 3.1$ eV.",
          [r"$hc = 1240$ eV nm."],
          [r"is $\lambda/hc$, upside down.",
           r"is the energy in joules, labeled as eV.",
           r"is the frequency in hertz."], sort=True),
        Q("15.1 Comparing wavelengths", r"An electron and a proton move at the same speed. Which has the longer de Broglie wavelength?",
          r"the electron, because it has less momentum", [r"the proton, because it has more mass", r"They have the same wavelength, because they have the same speed.", r"Neither has a wavelength; only light has one."],
          r"$\lambda = h/(mv)$; at the same speed, the much lighter electron has much less momentum and so a longer wavelength.",
          [r"$\lambda_e/\lambda_p = m_p/m_e \approx 1800$."],
          [r"more mass means more momentum and a shorter wavelength.",
           r"the wavelength depends on momentum, not speed alone.",
           r"all matter has a de Broglie wavelength."]),
        Q("15.1 Wave nature of electrons", r"Which observation shows the wave nature of electrons?",
          r"A beam of electrons passing through a thin crystal produces a diffraction pattern.", [r"Electrons are ejected from a metal by ultraviolet light.", r"Electrons leave curved tracks in a magnetic field.", r"An electron and a positron annihilate into two photons."],
          r"Diffraction and interference are wave behaviors; the crystal's atomic spacing is comparable to the electrons' de Broglie wavelength.",
          [r"Davisson and Germer (1927)."],
          [r"is the photoelectric effect, which shows the particle nature of light.",
           r"is the behavior of charged particles.",
           r"shows mass--energy conversion."]),
    ]),
    Set("An energy-level diagram (15.2--15.3)", [
        Q("15.3 Number of lines", r"A gas of these atoms is excited so that many atoms are in level $n = 4$. How many different photon energies can the gas emit as the atoms return to the ground state?",
          r"$6$", [r"$3$", r"$4$", r"$10$"],
          r"Every pair of levels gives a transition: $4\to3$, $4\to2$, $4\to1$, $3\to2$, $3\to1$, $2\to1$, with energies $3.0$, $5.0$, $9.0$, $2.0$, $6.0$ and $4.0$ eV, all different.",
          [r"$n(n-1)/2 = 6$ pairs."],
          [r"counts only the single steps down.",
           r"counts the levels, not the transitions between them.",
           r"would need five levels."], sort=True),
        Q("15.3 Longest wavelength", r"What is the longest wavelength these atoms can emit, and which transition produces it?",
          r"$620$ nm, from $n = 3$ to $n = 2$", [r"$138$ nm, from $n = 4$ to $n = 1$", r"$413$ nm, from $n = 4$ to $n = 3$", r"$1240$ nm, from $n = 4$ to $n = 3$"],
          r"The longest wavelength comes from the smallest energy gap: $3 \to 2$, $2.0$ eV, giving $\lambda = 1240/2.0 = 620$ nm.",
          [r"$\lambda = hc/\Delta E$: smallest gap, longest wavelength."],
          [r"is the shortest wavelength, from the largest gap.",
           r"is the $4 \to 3$ transition ($3.0$ eV), not the smallest gap.",
           r"uses $1.0$ eV, the energy of level 4 itself."]),
        Q("15.3 Absorption", r"A photon with an energy of $7.0$ eV strikes one of these atoms in its ground state. What happens?",
          r"It is not absorbed, because no transition from the ground state needs exactly $7.0$ eV.", [r"It is absorbed, and the atom goes to level 3 with $1.0$ eV left over as kinetic energy.", r"It is absorbed, ionizing the atom.", r"It is absorbed, and the atom goes to level 4."],
          r"From $n = 1$ the possible absorptions are $4.0$, $6.0$ and $9.0$ eV (and $10.0$ eV or more to ionize); a photon is absorbed only if its energy matches.",
          [r"A photon is absorbed whole or not at all."],
          [r"a photon cannot be partly absorbed by a bound transition.",
           r"ionization from the ground state needs at least $10.0$ eV.",
           r"reaching level 4 takes $9.0$ eV."]),
        Q("15.2 Ionization", r"What is the minimum energy needed to ionize one of these atoms from its ground state?",
          r"$10.0$ eV", [r"$9.0$ eV", r"$1.0$ eV", r"$4.0$ eV"],
          r"Ionization takes the electron from $-10.0$ eV to $0$.",
          [r"$0 - (-10.0) = 10.0$ eV."],
          [r"only lifts the electron to level 4, still bound.",
           r"ionizes an atom already in level 4.",
           r"only lifts the electron to level 2."], sort=True),
    ], stim=r"""An atom has the four energy levels listed below. Level 1 is the ground state; an electron with energy $0$ is free (the atom is ionized).

\medskip
\begin{tabular}{@{}lcccc@{}}\toprule
Level $n$ & 1 & 2 & 3 & 4 \\ \midrule
Energy (eV) & $-10.0$ & $-6.0$ & $-4.0$ & $-1.0$ \\ \bottomrule
\end{tabular}""", stim_title="Questions 4--7"),
    Set("Photoelectric data (15.5)", [
        Q("15.5 Threshold", r"What is the threshold frequency for this metal?",
          r"about $5.5 \times 10^{14}$ Hz", [r"about $2.3 \times 10^{14}$ Hz", r"about $14 \times 10^{14}$ Hz", r"zero"],
          r"The best-fit line crosses $K_{max} = 0$ at about $5.5 \times 10^{14}$ Hz; below that frequency no electrons are ejected.",
          [r"Threshold: where the line meets the frequency axis."],
          [r"reads the work function's value as a frequency.",
           r"is the highest frequency tested.",
           r"light below the threshold ejects no electrons, so there is a nonzero threshold."]),
        Q("15.5 Slope", r"What does the slope of the best-fit line represent?",
          r"Planck's constant", [r"the work function", r"the charge of the electron", r"the speed of light"],
          r"$K_{max} = hf - \phi$ is a straight line in $f$ with slope $h$. Here, about $0.41$ eV per $10^{14}$ Hz, or $4.1 \times 10^{-15}$ eV s.",
          [r"Compare with $y = mx + b$."],
          [r"is the magnitude of the vertical intercept.",
           r"only converts joules to electron volts.",
           r"does not appear in $K_{max} = hf - \phi$."]),
        Q("15.5 Work function", r"What is the work function of the metal?",
          r"about $2.3$ eV", [r"about $5.5$ eV", r"about $0.41$ eV", r"about $3.5$ eV"],
          r"Extending the line back to $f = 0$ gives an intercept of about $-2.3$ eV, so $\phi \approx 2.3$ eV (also $hf_0 = (4.14 \times 10^{-15})(5.5 \times 10^{14}) = 2.3$ eV).",
          [r"$\phi = hf_0$."],
          [r"reads the threshold frequency's number as an energy.",
           r"is the slope.",
           r"is the greatest kinetic energy measured."]),
    ], fig=PE, stim=r"Students shine light of different frequencies on a metal surface and measure the maximum kinetic energy $K_{max}$ of the ejected electrons. Their data and a best-fit line are shown.",
        stim_title="Questions 8--10"),
    Set("Nuclear physics and Compton scattering (15.6--15.8)", [
        Q("15.8 Beta decay", r"Carbon-14 (${}^{14}_{6}\mathrm{C}$) undergoes beta-minus decay. What is the daughter nucleus?",
          r"${}^{14}_{7}\mathrm{N}$", [r"${}^{14}_{5}\mathrm{B}$", r"${}^{13}_{6}\mathrm{C}$", r"${}^{10}_{4}\mathrm{Be}$"],
          r"In beta-minus decay a neutron becomes a proton (emitting an electron and an antineutrino): $Z$ rises by 1 and $A$ is unchanged.",
          [r"Charge: $6 = 7 + (-1)$. Nucleons: $14 = 14$."],
          [r"is beta-plus decay.",
           r"would require losing a neutron.",
           r"is alpha decay."]),
        Q("15.7 Mass and energy", r"In a nuclear reaction, the products have $3.1 \times 10^{-29}$ kg less mass than the reactants. How much energy is released?",
          r"$2.8 \times 10^{-12}$ J", [r"$1.4 \times 10^{-12}$ J", r"$9.3 \times 10^{-21}$ J", r"$0$"],
          r"$\Delta E = \Delta m\,c^2 = (3.1 \times 10^{-29})(3.0 \times 10^8)^2 = 2.8 \times 10^{-12}$ J, about $17$ MeV.",
          [r"$c^2 = 9.0 \times 10^{16}\ \mathrm{m^2/s^2}$."],
          [r"includes a factor of $\tfrac12$ that does not belong.",
           r"multiplies by $c$ instead of $c^2$.",
           r"the lost mass appears as released energy."], sort=True),
        Q("15.7 Half-life", r"A radioactive sample's activity falls to $\tfrac1{16}$ of its starting value in $20$ hours. What is the half-life?",
          r"$5.0$ h", [r"$1.25$ h", r"$10$ h", r"$80$ h"],
          r"$\tfrac1{16} = \left(\tfrac12\right)^4$: four half-lives in $20$ h, so $t_{1/2} = 5.0$ h.",
          [r"Count halvings: $1 \to \tfrac12 \to \tfrac14 \to \tfrac18 \to \tfrac1{16}$."],
          [r"divides $20$ h by $16$ instead of by the number of half-lives.",
           r"assumes two half-lives.",
           r"multiplies instead of dividing."], sort=True),
        Q("15.6 Photon momentum", r"Which conclusion did Compton scattering experiments support?",
          r"Photons carry momentum and collide with electrons like particles, conserving energy and momentum.", [r"Light is purely a wave, since its wavelength changes.", r"Electrons absorb several photons before being ejected.", r"Photons slow down after hitting an electron."],
          r"The wavelength shift matched exactly what energy and momentum conservation predict for a particle-like collision.",
          [r"$p_{photon} = h/\lambda$."],
          [r"the shift could not be explained by a classical wave model.",
           r"describes a multi-photon process, not Compton scattering.",
           r"photons always move at $c$; they lose energy, not speed."]),
    ]),
]

UNIT = Unit(15, "modern-physics", "Modern Physics", "12--15\\%", "15.1--15.8",
    abstract=r"""Unit 15 covers the quantum and nuclear physics of the twentieth century: photons and de Broglie waves, the Bohr model and line spectra, blackbody radiation, the photoelectric effect, Compton scattering and photon momentum, and nuclear physics (fission, fusion, the types of radioactive decay, mass--energy equivalence and half-life). Energies are given in electron volts where that is simpler; $hc = 1240$ eV nm. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Mathematical Routines", 10, r"""Light of wavelength $\lambda$ shines on a metal surface whose work function is $\phi$. Electrons are ejected, and a stopping potential $\Delta V_s$ applied across the tube just prevents the fastest of them from reaching the collecting electrode.""", [
        Part("a", 2, r"Using the photon model of light, explain why light below a certain frequency ejects no electrons from the metal, no matter how intense it is.",
             r"1 pt: each electron absorbs the energy of a single photon, $hf$. 1 pt: if $hf < \phi$, no photon has enough energy to free an electron; more intense light only supplies more photons of the same energy.",
             r"Saying dim light ``doesn't have enough energy'' without the one-photon, one-electron idea."),
        Part("b", 3, r"Derive an expression for $\Delta V_s$ in terms of $\lambda$, $\phi$ and physical constants as appropriate.",
             r"1 pt: $K_{max} = hc/\lambda - \phi$. 1 pt: $e\Delta V_s = K_{max}$. 1 pt: $\Delta V_s = \dfrac{1}{e}\left(\dfrac{hc}{\lambda} - \phi\right)$.",
             r"Leaving out the work function."),
        Part("c", 2, r"For $\lambda = 300$ nm and $\phi = 2.3$ eV, calculate $\Delta V_s$.",
             r"1 pt: $hc/\lambda = 1240/300 = 4.13$ eV, so $K_{max} = 1.83$ eV. 1 pt: $\Delta V_s = 1.8$ V.",
             r"Answering in eV for a potential, or mixing joules and electron volts."),
        Part("d", 3, r"A student claims that halving the wavelength of the light will double the stopping potential. Do you agree or disagree? Justify your answer using your expression from part (b), and support it with a calculation for the values in part (c).",
             r"1 pt: disagree. 1 pt: halving $\lambda$ doubles $hc/\lambda$, but the work function is subtracted, so $\Delta V_s$ is not proportional to $1/\lambda$. 1 pt: at $150$ nm, $hc/\lambda = 8.27$ eV and $\Delta V_s = 6.0$ V, more than three times $1.8$ V.",
             r"Agreeing because ``energy is proportional to frequency''."),
    ], mins=22),
    frq_topic="the photoelectric effect and stopping potential",
)
