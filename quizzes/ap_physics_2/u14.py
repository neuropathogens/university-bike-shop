import math

from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph

SNAP = Graph(r"Position $x$ (m)", r"Displacement $y$ (cm)", x=(0, 1.6, 0.2), y=(-3, 3, 1), series=[],
             curves=[("string", lambda x: 2.0 * math.sin(2 * math.pi * x / 0.8), 0)])

S1 = Sec("Wave pulses and periodic waves (14.1--14.2)", ["14.1", "14.2"], r"""
A wave carries energy and momentum from place to place without carrying matter along with it. \textbf{Mechanical} waves (sound, waves on strings, water waves) need a medium; electromagnetic waves do not.

\begin{terms}
Transverse & the medium moves perpendicular to the wave's direction (a string, light) \\
Longitudinal & the medium moves back and forth along the wave's direction, in compressions and rarefactions (sound) \\
Wave speed & set by the medium: $v = \sqrt{F_T/\mu}$ on a string; about $340$ m/s for sound in room-temperature air \\
Periodic wave & $v = f\lambda$, $T = 1/f$; the source sets $f$, the medium sets $v$, and so together they set $\lambda$ \\
\end{terms}

\textbf{Two graphs.} A displacement--\emph{position} graph is a snapshot of the whole wave at one instant; you read the wavelength from it. A displacement--\emph{time} graph follows one point of the medium; you read the period from it. Both show the amplitude.
""", checks=[
    Q("14.2 Wave speed", r"A $680$ Hz tone travels through air at $340$ m/s. What is its wavelength?",
      r"$0.50$ m", [r"$2.0$ m", r"$2.3 \times 10^{5}$ m", r"$1020$ m"],
      r"$\lambda = v/f = 340/680 = 0.50$ m.",
      [r"$v = f\lambda$."],
      [r"is $f/v$, upside down.",
       r"multiplies $v$ and $f$.",
       r"adds $v$ and $f$."], sort=True),
    Q("14.2 Same medium", r"A source on a stretched string doubles its frequency without changing the string's tension. What happens to the waves on the string?",
      r"The wavelength halves and the speed stays the same.", [r"The speed doubles and the wavelength stays the same.", r"The wavelength doubles and the speed stays the same.", r"Both the speed and the wavelength double."],
      r"The medium (tension and mass per length) fixes the speed; $\lambda = v/f$ then halves.",
      [r"Same string, same tension: same $v$."],
      [r"the speed depends on the medium, not the source.",
       r"a higher frequency at the same speed means shorter waves.",
       r"the speed is fixed by the string."]),
])

S2 = Sec("Boundary behavior and polarization (14.3)", ["14.3"], r"""
\textbf{At a boundary} part of a wave reflects and part is transmitted. A pulse reflecting from a fixed end comes back inverted; from a free end, upright. A wave passing into a new medium keeps its frequency (the boundary oscillates at the incoming rate) but changes speed, so its wavelength changes.

\textbf{Polarization.} A transverse wave whose oscillations all lie along one direction is polarized. A polarizing filter transmits only the component of a light wave's electric field along its axis; two filters with axes crossed at $90^\circ$ block the light. Longitudinal waves such as sound cannot be polarized, so polarization shows that light is a transverse wave.
""", checks=[
    Q("14.3 Fixed end", r"A pulse traveling along a rope reflects from the end, which is tied firmly to a wall. How does the reflected pulse compare with the incoming one?",
      r"It is inverted.", [r"It is upright and identical.", r"It is upright but twice as tall.", r"There is no reflected pulse."],
      r"The fixed end cannot move, so the wall pulls the rope the opposite way, sending back an inverted pulse.",
      [r"Fixed end: inverted. Free end: upright."],
      [r"describes reflection from a free end.",
       r"reflection does not increase the amplitude.",
       r"the wave's energy has to go somewhere; it reflects."]),
])

S3 = Sec("Electromagnetic waves (14.4)", ["14.4"], r"""
Light is an electromagnetic wave: oscillating electric and magnetic fields, perpendicular to each other and to the direction of travel, that sustain each other without a medium. In vacuum every electromagnetic wave travels at $c = 3.0 \times 10^8$ m/s, and $c = f\lambda$.

In order of increasing frequency (decreasing wavelength): radio, microwaves, infrared, visible (red to violet, about $700$ to $400$ nm), ultraviolet, X-rays, gamma rays.
""", checks=[
    Q("14.4 FM radio", r"An FM radio station broadcasts at $100$ MHz. What is the wavelength of its waves?",
      r"$3.0$ m", [r"$0.33$ m", r"$3.0 \times 10^{16}$ m", r"$3.0 \times 10^{6}$ m"],
      r"$\lambda = c/f = (3.0 \times 10^8)/(1.00 \times 10^8) = 3.0$ m.",
      [r"$100\ \mathrm{MHz} = 1.00 \times 10^8$ Hz."],
      [r"is $f/c$, upside down.",
       r"multiplies $c$ and $f$.",
       r"uses $100$ Hz instead of $100$ MHz."], sort=True),
])

S4 = Sec("The Doppler effect (14.5)", ["14.5"], r"""
When a wave source and an observer move relative to each other, the observed frequency differs from the source's frequency:
\begin{itemize}
\item moving toward each other: the observed frequency is \emph{higher} (crests arrive more often);
\item moving apart: the observed frequency is \emph{lower};
\item moving with the same velocity: no change.
\end{itemize}
The faster the relative motion, the larger the shift. The siren of a passing ambulance drops in pitch at the moment it passes. Only a qualitative treatment is required.
""", checks=[
    Q("14.5 Passing car", r"A car sounding a $400$ Hz horn drives past a listener standing at the roadside. What does the listener hear?",
      r"above $400$ Hz as the car approaches, below $400$ Hz as it moves away", [r"$400$ Hz throughout, but louder as the car approaches", r"below $400$ Hz as the car approaches, above $400$ Hz as it moves away", r"a frequency that rises steadily the whole time"],
      r"Approaching shortens the distance between arriving crests (higher frequency); receding lengthens it (lower frequency).",
      [r"The pitch drops as the car passes."],
      [r"loudness changes too, but so does the frequency.",
       r"reverses the effect.",
       r"the frequency drops once the car passes."]),
])

S5 = Sec("Wave interference and standing waves (14.6)", ["14.6"], r"""
When waves overlap, their displacements add (\textbf{superposition}). Crest meeting crest gives constructive interference; crest meeting trough gives destructive interference. Two sounds of slightly different frequencies produce \textbf{beats} at $f_{beat} = |f_1 - f_2|$.

\textbf{Standing waves} form when waves reflect back and forth in a bounded medium. Nodes (no motion) are half a wavelength apart, with antinodes midway.

\begin{compare}{System}{Allowed wavelengths}{Frequencies}
String fixed at both ends, or pipe open at both ends & $\lambda_n = 2L/n$ & $f_n = nv/(2L)$, $n = 1, 2, 3, \ldots$ \\
Pipe closed at one end & $\lambda_n = 4L/n$ & $f_n = nv/(4L)$, odd $n$ only \\
\end{compare}
A string's ends are nodes; a pipe's open end is a displacement antinode and its closed end a node.
""", checks=[
    Q("14.6 Fundamental", r"A string $0.60$ m long, fixed at both ends, carries waves at $120$ m/s. What is its fundamental frequency?",
      r"$100$ Hz", [r"$200$ Hz", r"$50$ Hz", r"$72$ Hz"],
      r"The fundamental has $\lambda = 2L = 1.2$ m, so $f_1 = v/\lambda = 100$ Hz.",
      [r"Fundamental: one antinode, nodes at both ends."],
      [r"uses $\lambda = L$.",
       r"uses $\lambda = 4L$, the closed-pipe pattern.",
       r"multiplies $v$ by $L$."], sort=True),
    Q("14.6 Beats", r"Two tuning forks of $440$ Hz and $444$ Hz are struck together. What beat frequency is heard?",
      r"$4$ Hz", [r"$442$ Hz", r"$884$ Hz", r"$2$ Hz"],
      r"$f_{beat} = |444 - 440| = 4$ Hz.",
      [r"The loudness swells and fades $4$ times each second."],
      [r"is the average, the pitch you hear, not the beat rate.",
       r"adds the frequencies.",
       r"halves the difference."], sort=True),
])

S6 = Sec("Diffraction, double slits, gratings and thin films (14.7--14.9)", ["14.7", "14.8", "14.9"], r"""
\textbf{Diffraction} is the spreading of a wave through an opening or around an edge; it is significant when the opening is not much larger than the wavelength. Sound (wavelengths near a meter) bends around doorways; light (under a micrometer) mostly does not.

\textbf{Double slits and gratings.} Light from two slits a distance $d$ apart interferes. Bright fringes appear where the path difference is a whole number of wavelengths:
\[ d\sin\theta = m\lambda, \qquad \Delta y \approx \frac{m\lambda L}{d} \ (\text{small angles, screen at distance } L). \]
A grating (many slits) gives the same bright angles, but much sharper and brighter.

\textbf{Thin films.} Light reflects from both surfaces of a thin film, and the two reflections interfere. A reflection from a medium of higher index inverts the wave (a half-wavelength shift); one from lower index does not. For a soap film in air (one inversion), reflection is bright when $2nt = (m + \tfrac12)\lambda$, so the thinnest bright film has $t = \lambda/(4n)$. Colors in soap bubbles and oil slicks come from this.
""", checks=[
    Q("14.8 Fringe spacing", r"Light of wavelength $600$ nm passes through two slits $0.20$ mm apart onto a screen $2.0$ m away. What is the distance between neighboring bright fringes?",
      r"$6.0$ mm", [r"$0.60$ mm", r"$60$ mm", r"$3.0$ mm"],
      r"$\Delta y = \lambda L/d = (600 \times 10^{-9})(2.0)/(0.20 \times 10^{-3}) = 6.0 \times 10^{-3}$ m.",
      [r"Small angles: neighboring bright fringes are $\lambda L/d$ apart."],
      [r"uses $d = 2.0$ mm.",
       r"uses $d = 0.020$ mm.",
       r"halves the spacing: that is the distance from a bright fringe to the next dark one."], sort=True),
])

QS = [
    Set("Waves and boundaries (14.1--14.3)", [
        Q("14.2 Wave on a rope", r"A wave on a rope has a frequency of $4.0$ Hz and a wavelength of $1.5$ m. What is its speed?",
          r"$6.0$ m/s", [r"$2.7$ m/s", r"$0.38$ m/s", r"$5.5$ m/s"],
          r"$v = f\lambda = 4.0 \times 1.5 = 6.0$ m/s.",
          [r"Each second, $4.0$ wavelengths of $1.5$ m pass a point."],
          [r"divides $f$ by $\lambda$.",
           r"divides $\lambda$ by $f$.",
           r"adds the two numbers."], sort=True),
        Q("14.3 Into water", r"A sound wave passes from air into water, where sound travels about four times faster. Which describes the wave in the water?",
          r"The same frequency, a greater speed and a longer wavelength", [r"A higher frequency, a greater speed and the same wavelength", r"The same frequency, a greater speed and a shorter wavelength", r"A lower frequency, the same speed and a longer wavelength"],
          r"The frequency is set by the source and does not change at the boundary; with $v$ larger, $\lambda = v/f$ is larger.",
          [r"$f$ fixed; $\lambda \propto v$."],
          [r"the frequency does not change at a boundary.",
           r"faster at the same frequency means longer waves.",
           r"the speed changes; it is set by the medium."]),
        Q("14.3 Free end", r"A pulse travels along a rope whose far end is attached to a light ring that slides freely on a vertical pole. How does the reflected pulse compare with the incoming pulse?",
          r"It is upright.", [r"It is inverted.", r"It is upright and twice as tall.", r"No pulse is reflected."],
          r"A free end overshoots and pulls the rope the same way, so the reflection is upright.",
          [r"Free end: upright; fixed end: inverted."],
          [r"describes a fixed end.",
           r"reflection does not add energy.",
           r"the pulse reflects because the rope ends."]),
        Q("14.3 Polarization", r"Which kind of wave can be polarized?",
          r"a transverse wave, such as light", [r"a longitudinal wave, such as sound", r"any wave, transverse or longitudinal", r"only waves traveling in a vacuum"],
          r"Polarization selects one direction of oscillation perpendicular to the travel; a longitudinal wave oscillates only along its travel, so it has no such direction to select.",
          [r"Polarizing filters show that light is transverse."],
          [r"longitudinal oscillations lie along the direction of travel.",
           r"only transverse waves can be polarized.",
           r"waves on strings can be polarized too."]),
    ]),
    Set("A snapshot of a wave on a string (14.2)", [
        Q("14.2 Reading the graph", r"What are the amplitude and the wavelength of the wave?",
          r"amplitude $2.0$ cm, wavelength $0.80$ m", [r"amplitude $4.0$ cm, wavelength $0.80$ m", r"amplitude $2.0$ cm, wavelength $0.40$ m", r"amplitude $2.0$ cm, wavelength $1.6$ m"],
          r"The amplitude is the greatest displacement from equilibrium, $2.0$ cm; one full cycle repeats every $0.80$ m.",
          [r"Crest to crest: $0.20$ m to $1.00$ m."],
          [r"is the crest-to-trough distance, twice the amplitude.",
           r"is the distance from a crest to the next trough, half a wavelength.",
           r"is the whole length shown, two wavelengths."]),
        Q("14.2 Frequency", r"The wave travels along the string at $12$ m/s. What is its frequency?",
          r"$15$ Hz", [r"$9.6$ Hz", r"$0.067$ Hz", r"$7.5$ Hz"],
          r"$f = v/\lambda = 12/0.80 = 15$ Hz.",
          [r"$v = f\lambda$."],
          [r"multiplies $v$ and $\lambda$.",
           r"is $\lambda/v$, the period in seconds.",
           r"uses a wavelength of $1.6$ m."], sort=True),
        Q("14.2 Doubling the frequency", r"The source's frequency is doubled while the string's tension stays the same. What is the new wavelength?",
          r"$0.40$ m", [r"$1.6$ m", r"$0.80$ m", r"$0.20$ m"],
          r"The speed is still $12$ m/s, so $\lambda = 12/30 = 0.40$ m.",
          [r"Same medium, same speed: $\lambda \propto 1/f$."],
          [r"has the effect backward.",
           r"the wavelength must change if $f$ changes and $v$ does not.",
           r"quarters the wavelength."], sort=True),
        Q("14.2 Motion of the string", r"At the instant shown, how is the point of the string at $x = 0.20$ m (a crest) moving?",
          r"It is momentarily at rest.", [r"It is moving at its greatest speed.", r"It is moving to the right at $12$ m/s.", r"It is moving with the wave toward larger $x$."],
          r"Each point of the string oscillates up and down; at a crest it is at maximum displacement, where its velocity is zero.",
          [r"The wave moves along the string; the string itself moves up and down."],
          [r"the string moves fastest at zero displacement.",
           r"$12$ m/s is the wave's speed, not the string's.",
           r"the string's points move perpendicular to the wave."]),
    ], stim=r"The graph is a snapshot of a transverse wave traveling to the right along a stretched string.",
        fig=SNAP, stim_title="Questions 5--8"),
    Set("Electromagnetic waves, Doppler, beats and pipes (14.4--14.6)", [
        Q("14.4 Spectrum", r"Which list orders these electromagnetic waves from lowest to highest frequency?",
          r"radio, infrared, visible light, X-rays", [r"X-rays, visible light, infrared, radio", r"visible light, radio, infrared, X-rays", r"infrared, radio, X-rays, visible light"],
          r"Radio waves have the longest wavelengths and lowest frequencies; X-rays the shortest and highest.",
          [r"Radio, microwave, infrared, visible, ultraviolet, X-ray, gamma."],
          [r"reverses the order.",
           r"radio waves have lower frequencies than visible light.",
           r"infrared has higher frequency than radio, and visible lower than X-rays."]),
        Q("14.6 Tuning a fork", r"A $256$ Hz tuning fork and a fork of unknown frequency produce $3$ beats per second. A small piece of tape added to the unknown fork lowers its frequency, and the beats speed up. What was the unknown fork's original frequency?",
          r"$253$ Hz", [r"$259$ Hz", r"$256$ Hz", r"$3$ Hz"],
          r"It was $253$ or $259$ Hz. Lowering it moves $253$ Hz farther from $256$ Hz (faster beats), while lowering $259$ Hz would bring it closer (slower beats).",
          [r"$f_{beat} = |f_1 - f_2|$."],
          [r"lowering $259$ Hz would slow the beats.",
           r"equal frequencies give no beats.",
           r"is the beat frequency, not the fork's frequency."], sort=True),
        Q("14.6 Closed pipe", r"A pipe $0.50$ m long is closed at one end. Sound travels at $340$ m/s. What is its fundamental frequency?",
          r"$170$ Hz", [r"$340$ Hz", r"$680$ Hz", r"$85$ Hz"],
          r"A closed pipe's fundamental has a node at the closed end and an antinode at the open end: $\lambda = 4L = 2.0$ m, $f = 340/2.0 = 170$ Hz.",
          [r"$f_1 = v/(4L)$."],
          [r"is the fundamental of a pipe open at both ends, $v/(2L)$.",
           r"uses $\lambda = L$.",
           r"uses $\lambda = 8L$."], sort=True),
        Q("14.5 Moving together", r"A cyclist rides behind a bus at exactly the bus's speed while the bus plays music. Compared with the frequencies the bus emits, the cyclist hears",
          r"the same frequencies", [r"higher frequencies", r"lower frequencies", r"higher frequencies, increasing with their common speed"],
          r"A Doppler shift requires relative motion between source and observer; here there is none.",
          [r"Same velocity: observed frequency equals the source frequency."],
          [r"would need the two to approach each other.",
           r"would need the two to move apart.",
           r"the shift depends on relative velocity, which is zero."]),
    ]),
    Set("Diffraction and interference of light (14.7--14.9)", [
        Q("14.8 Double slit", r"In a double-slit experiment, the slits are $0.10$ mm apart, the screen is $1.5$ m away, and neighboring bright fringes are $9.0$ mm apart. What is the wavelength of the light?",
          r"$6.0 \times 10^{-7}$ m", [r"$6.0 \times 10^{-4}$ m", r"$1.7 \times 10^{-2}$ m", r"$1.2 \times 10^{-6}$ m"],
          r"$\lambda = d\,\Delta y/L = (1.0 \times 10^{-4})(9.0 \times 10^{-3})/1.5 = 6.0 \times 10^{-7}$ m (600 nm).",
          [r"Rearrange $\Delta y = \lambda L/d$."],
          [r"leaves one length in millimeters.",
           r"is $dL/\Delta y$, with $L$ and $\Delta y$ swapped.",
           r"doubles the answer, as if $9.0$ mm were half the fringe spacing."], sort=True),
        Q("14.7 Diffraction", r"You can hear a radio playing in the next room through an open doorway but cannot see it. Which explains this?",
          r"Sound wavelengths are comparable to the width of the doorway, so sound diffracts around it; light's wavelengths are far smaller.", [r"Sound travels faster than light.", r"Light is a particle and cannot bend.", r"Walls absorb light but transmit sound."],
          r"Diffraction is significant only when the opening is not much larger than the wavelength.",
          [r"Sound: about $1$ m. Visible light: about $5 \times 10^{-7}$ m."],
          [r"light is about a million times faster than sound.",
           r"light shows diffraction and interference, which are wave behaviors.",
           r"the sound reaches you through the doorway, not the wall."]),
        Q("14.9 Soap film", r"A soap film ($n = 1.33$) in air looks bright green ($\lambda = 532$ nm in air) by reflected light. What is the thinnest film that gives a bright reflection at this wavelength?",
          r"$100$ nm", [r"$200$ nm", r"$133$ nm", r"$400$ nm"],
          r"One reflection (from the front surface) is inverted, so the thinnest bright film has $2nt = \lambda/2$: $t = \lambda/(4n) = 532/(4 \times 1.33) = 100$ nm.",
          [r"The wavelength in the film is $\lambda/n = 400$ nm; the round trip $2t$ must be half of that."],
          [r"is $\lambda/(2n)$, which gives a dark reflection with one inversion.",
           r"is $\lambda/4$, ignoring the film's index.",
           r"is the wavelength in the film, $\lambda/n$."], sort=True),
    ]),
]

UNIT = Unit(14, "waves-sound-physical-optics", "Waves, Sound and Physical Optics", "12--15\\%", "14.1--14.9",
    abstract=r"""Unit 14 covers mechanical and electromagnetic waves: pulses and periodic waves, $v = f\lambda$ and reading wave graphs, reflection, transmission and polarization at boundaries, the electromagnetic spectrum, the Doppler effect (qualitatively), superposition, beats and standing waves on strings and in pipes, and the wave behavior of light in diffraction, double-slit and grating patterns and thin films. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Translation Between Representations", 12, r"""A string of length $L$ is fixed at both ends. Waves travel along it at speed $v$. A mechanical oscillator drives the string at different frequencies, and at certain frequencies a standing wave forms.""", [
        Part("a", 3, r"Sketch the shape of the string when it vibrates in its third harmonic ($n = 3$). Label the nodes and the antinodes, and indicate the wavelength in terms of $L$.",
             r"1 pt: three loops along the string. 1 pt: four nodes (including both fixed ends) and three antinodes, labeled. 1 pt: $\lambda_3 = 2L/3$ (two loops make one wavelength).",
             r"Drawing the ends as antinodes."),
        Part("b", 3, r"Derive an expression for the frequency $f_n$ of the $n$th harmonic in terms of $n$, $L$ and $v$.",
             r"1 pt: the $n$th harmonic has $n$ half-wavelengths along the string: $L = n\lambda_n/2$. 1 pt: $\lambda_n = 2L/n$. 1 pt: $f_n = v/\lambda_n = \dfrac{nv}{2L}$.",
             r"Using $\lambda_n = 4L/n$, the pattern for a pipe closed at one end."),
        Part("c", 3, r"On axes of $f_n$ versus $n$, sketch the frequencies of the first five harmonics. Describe the shape of the pattern and state what its slope represents.",
             r"1 pt: five points, at $n = 1$ to $5$. 1 pt: they lie on a straight line that passes through the origin. 1 pt: slope $= v/(2L)$, the fundamental frequency.",
             r"Drawing a continuous curve with no points, or a line that does not pass through the origin."),
        Part("d", 3, r"The tension in the string is increased so that the wave speed doubles. A student says the third harmonic will now occur at the same frequency, but with nodes closer together. Do you agree or disagree with the student? Justify your answer using your expression from (b) or your graph from (c).",
             r"1 pt: disagree. 1 pt: the wavelengths are fixed by the length of the string ($\lambda_3 = 2L/3$ still), so the nodes stay in the same places. 1 pt: $f_n = nv/(2L)$ is proportional to $v$, so the third harmonic's frequency doubles; on the graph the line's slope doubles.",
             r"Keeping the frequency fixed and changing the wavelength."),
    ], mins=28),
    frq_topic="standing waves on a string",
)
