from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Reflection (13.1)", ["13.1"], r"""
\textbf{Law of reflection:} the angle of reflection equals the angle of incidence, both measured from the \textbf{normal} (the line perpendicular to the surface), and the incident ray, reflected ray and normal lie in one plane. A smooth surface gives specular (mirror-like) reflection; a rough surface scatters light in many directions (diffuse reflection), though each tiny patch still obeys the law.

\textbf{Plane mirror.} The image is virtual (light does not actually come from it), upright, the same size as the object, and as far behind the mirror as the object is in front. To see your whole body you need a mirror only half your height.

\begin{trap}
Angles are measured from the normal, not from the surface. A ray that makes $25^\circ$ with a mirror's surface has an angle of incidence of $65^\circ$.
\end{trap}
""", checks=[
    Q("13.1 Angle of reflection", r"A ray of light strikes a plane mirror, making an angle of $25^\circ$ with the mirror's surface. What is the angle of reflection?",
      r"$65^\circ$", [r"$25^\circ$", r"$50^\circ$", r"$130^\circ$"],
      r"Measured from the normal, the angle of incidence is $90^\circ - 25^\circ = 65^\circ$, and the angle of reflection equals it.",
      [r"Convert from the surface to the normal first."],
      [r"is measured from the surface; the law uses angles from the normal.",
       r"is the angle between the surface-measured rays.",
       r"is the angle between incident and reflected rays measured from the normal."], sort=True),
])

S2 = Sec("Images formed by mirrors (13.2)", ["13.2"], r"""
A \textbf{concave} (converging) mirror brings parallel rays to a real focal point at $f = R/2$; a \textbf{convex} (diverging) mirror spreads them as if from a virtual focal point behind it.
\[ \frac{1}{s_i} + \frac{1}{s_o} = \frac{1}{f}, \qquad M = \frac{h_i}{h_o} = -\frac{s_i}{s_o}. \]
Signs: $f > 0$ for concave, $f < 0$ for convex; $s_i > 0$ for a real image (in front of the mirror), $s_i < 0$ for a virtual image (behind it); $M < 0$ means inverted.

\begin{compare}{Object position (concave mirror)}{Image}{Example}
Beyond $2f$ & real, inverted, smaller, between $f$ and $2f$ & \\
At $2f$ & real, inverted, same size, at $2f$ & \\
Between $f$ and $2f$ & real, inverted, larger, beyond $2f$ & a projector \\
Inside $f$ & virtual, upright, larger, behind the mirror & a shaving mirror \\
Any position, convex mirror & virtual, upright, smaller & a car's side mirror \\
\end{compare}

\textbf{Ray diagrams.} Use two of the three principal rays: in parallel to the axis, out through the focal point; in through the focal point, out parallel; in toward the center of curvature, straight back. The image is where the reflected rays (or their extensions) cross.
""", checks=[
    Q("13.2 Concave mirror", r"An object is $30$ cm in front of a concave mirror with a focal length of $10$ cm. Where is the image, and what is it like?",
      r"$15$ cm in front of the mirror; real, inverted and half the object's size", [r"$15$ cm behind the mirror; virtual, upright and half size", r"$7.5$ cm in front of the mirror; real, inverted and a quarter size", r"$30$ cm in front of the mirror; real, inverted and the same size"],
      r"$1/s_i = 1/10 - 1/30 = 1/15$, so $s_i = +15$ cm (real); $M = -15/30 = -0.5$.",
      [r"Positive $s_i$: real, in front of the mirror. Negative $M$: inverted."],
      [r"a positive $s_i$ means a real image in front of the mirror.",
       r"adds the reciprocals instead of subtracting.",
       r"would need the object at $2f = 20$ cm."]),
])

S3 = Sec("Refraction (13.3)", ["13.3"], r"""
Light travels more slowly in a medium than in vacuum; the \textbf{index of refraction} is $n = c/v \ge 1$. At a boundary, light changes direction according to \textbf{Snell's law}:
\[ n_1\sin\theta_1 = n_2\sin\theta_2 . \]
Entering a medium of higher $n$, light bends toward the normal; entering lower $n$, away from it. The frequency stays the same, so the wavelength shrinks: $\lambda_n = \lambda_0/n$.

\textbf{Total internal reflection.} Going from higher $n$ to lower $n$, the refracted ray bends away from the normal; beyond the \textbf{critical angle}, $\sin\theta_c = n_2/n_1$, no light is transmitted and all of it reflects. Optical fibers rely on this.

\textbf{Dispersion.} $n$ depends slightly on wavelength (larger for violet than red in glass), so a prism spreads white light into colors.
""", checks=[
    Q("13.3 Snell's law", r"Light in air strikes a glass surface ($n = 1.50$) at an angle of incidence of $30^\circ$. What is the angle of refraction?",
      r"$19^\circ$", [r"$30^\circ$", r"$49^\circ$", r"$20^\circ$"],
      r"$\sin\theta_2 = \sin30^\circ/1.50 = 0.333$, so $\theta_2 = 19^\circ$, bent toward the normal.",
      [r"$1.00\sin30^\circ = 1.50\sin\theta_2$."],
      [r"light changes direction entering glass at an angle.",
       r"multiplies by $n$: bending away from the normal.",
       r"divides the angle, not its sine, by $n$."], sort=True),
    Q("13.3 Critical angle", r"What is the critical angle for light inside glass ($n = 1.50$) meeting a boundary with air?",
      r"$42^\circ$", [r"$48^\circ$", r"$26^\circ$", r"$90^\circ$"],
      r"$\sin\theta_c = n_2/n_1 = 1.00/1.50 = 0.667$, so $\theta_c = 42^\circ$.",
      [r"Beyond $42^\circ$ the light is totally reflected."],
      [r"is the complement, measured from the surface.",
       r"uses $\sin\theta_c = 1/1.50^2$.",
       r"is where the refracted ray grazes the surface, not the angle of incidence that produces it."], sort=True),
])

S4 = Sec("Images formed by lenses (13.4)", ["13.4"], r"""
A \textbf{converging} lens (thicker in the middle) brings parallel rays to a focus at $f > 0$; a \textbf{diverging} lens (thinner in the middle) spreads them, $f < 0$. The thin-lens equation and magnification are the same as for mirrors:
\[ \frac{1}{s_i} + \frac{1}{s_o} = \frac{1}{f}, \qquad M = -\frac{s_i}{s_o}, \]
but a real image ($s_i > 0$) forms on the \emph{opposite} side of the lens from the object, and a virtual image ($s_i < 0$) on the same side.

\begin{terms}
Converging, object beyond $f$ & real, inverted image that can be projected on a screen (cameras, projectors, the eye) \\
Converging, object inside $f$ & virtual, upright, enlarged image (a magnifying glass) \\
Diverging, any object & virtual, upright, smaller image \\
Covering part of a lens & every part of the lens forms the whole image, so the image is complete but dimmer \\
\end{terms}
""", checks=[
    Q("13.4 Magnifier", r"An object is $10$ cm from a converging lens with a focal length of $20$ cm. Describe the image.",
      r"virtual, upright and twice the object's size, $20$ cm from the lens on the object's side", [r"real, inverted and twice the object's size, $20$ cm beyond the lens", r"virtual, upright and half size, $6.7$ cm from the lens", r"no image forms"],
      r"$1/s_i = 1/20 - 1/10 = -1/20$, so $s_i = -20$ cm (virtual) and $M = -(-20)/10 = +2$.",
      [r"Object inside $f$: the lens acts as a magnifying glass."],
      [r"the negative $s_i$ means a virtual image on the object's side.",
       r"adds the reciprocals instead of subtracting.",
       r"an image forms; it is virtual."]),
])

QS = [
    Set("Reflection and mirrors (13.1--13.2)", [
        Q("13.1 Full-length mirror", r"A person $1.8$ m tall wants to see her whole body in a vertical plane mirror. What is the shortest mirror that will do?",
          r"$0.90$ m", [r"$1.8$ m", r"$0.45$ m", r"$3.6$ m"],
          r"Rays from her feet and the top of her head reach her eyes by reflecting halfway between, so the mirror needs half her height, whatever her distance from it.",
          [r"Law of reflection: the reflection point for each ray is midway in height between the eye and that body part."],
          [r"a mirror as tall as she is would work, but half that is enough.",
           r"is a quarter of her height.",
           r"is twice her height."], sort=True),
        Q("13.2 Object at 2f", r"An object is $40$ cm in front of a concave mirror with a focal length of $20$ cm. Which describes the image?",
          r"real, inverted, the same size, $40$ cm in front of the mirror", [r"virtual, upright, the same size, $40$ cm behind the mirror", r"real, inverted, twice the size, $80$ cm in front of the mirror", r"no image forms, because the object is at the focal point"],
          r"The object is at $2f$ (the center of curvature): $1/s_i = 1/20 - 1/40 = 1/40$, so $s_i = 40$ cm and $M = -1$.",
          [r"At $2f$ the image is at $2f$, inverted and the same size."],
          [r"a concave mirror forms a real image of a distant object.",
           r"would need the object between $f$ and $2f$.",
           r"the focal point is at $20$ cm, not $40$ cm."]),
        Q("13.2 Convex mirror", r"Convex mirrors are used as car side mirrors. What kind of image do they always form of objects in front of them?",
          r"virtual, upright and smaller than the object", [r"real, inverted and smaller", r"virtual, upright and larger", r"real, upright and the same size"],
          r"A diverging mirror spreads reflected rays, which appear to come from a small upright image behind it; it shows a wide field of view.",
          [r"$f < 0$ gives $s_i < 0$ and $0 < M < 1$ for every real object."],
          [r"a diverging mirror cannot make reflected rays converge.",
           r"enlarged virtual images come from concave mirrors with the object inside $f$.",
           r"real images formed by a single mirror are inverted."]),
        Q("13.2 Inside the focal point", r"An object is $10$ cm in front of a concave mirror with a focal length of $15$ cm. Where is the image, and what is its magnification?",
          r"$30$ cm behind the mirror; magnification $+3.0$", [r"$6.0$ cm in front of the mirror; magnification $-0.60$", r"$30$ cm in front of the mirror; magnification $-3.0$", r"$5.0$ cm behind the mirror; magnification $+0.50$"],
          r"$1/s_i = 1/15 - 1/10 = -1/30$, so $s_i = -30$ cm (virtual, behind the mirror) and $M = -(-30)/10 = +3.0$.",
          [r"Object inside $f$: virtual, upright, enlarged."],
          [r"adds the reciprocals.",
           r"drops the minus sign: the image is virtual.",
           r"subtracts the distances instead of the reciprocals."]),
    ]),
    Set("Light entering glass (13.3)", [
        Q("13.3 Angle of refraction", r"What is the angle of refraction in the glass?",
          r"$25^\circ$", [r"$40^\circ$", r"$75^\circ$", r"$27^\circ$"],
          r"$\sin\theta_2 = \sin40^\circ/1.50 = 0.429$, so $\theta_2 = 25^\circ$.",
          [r"$1.00\sin40^\circ = 1.50\sin\theta_2$."],
          [r"the ray bends at the surface.",
           r"multiplies $\sin40^\circ$ by $1.50$: bending the wrong way.",
           r"divides the angle itself by $1.50$."], sort=True),
        Q("13.3 Speed in glass", r"What is the speed of light in the glass?",
          r"$2.0 \times 10^8$ m/s", [r"$4.5 \times 10^8$ m/s", r"$3.0 \times 10^8$ m/s", r"$1.3 \times 10^8$ m/s"],
          r"$v = c/n = (3.0 \times 10^8)/1.50 = 2.0 \times 10^8$ m/s.",
          [r"$n = c/v$."],
          [r"multiplies by $n$; light is slower in glass.",
           r"is the speed in vacuum.",
           r"divides by $n^2$."], sort=True),
        Q("13.3 Wavelength", r"The light has a wavelength of $600$ nm in air. What is its wavelength in the glass?",
          r"$400$ nm", [r"$900$ nm", r"$600$ nm", r"$450$ nm"],
          r"The frequency is unchanged and the speed drops by $1.50$, so $\lambda = 600/1.50 = 400$ nm.",
          [r"$\lambda_n = \lambda_0/n$."],
          [r"multiplies by $n$.",
           r"the wavelength changes; it is the frequency that stays the same.",
           r"uses the index of water, $1.33$."], sort=True),
        Q("13.3 Total internal reflection", r"Light travelling inside the glass strikes the glass--air boundary. For which angle of incidence is it totally internally reflected?",
          r"$45^\circ$", [r"$30^\circ$", r"$35^\circ$", r"$40^\circ$"],
          r"The critical angle is $\sin^{-1}(1/1.50) = 42^\circ$; only angles larger than that reflect totally.",
          [r"$\theta > \theta_c$ for total internal reflection."],
          [r"is below the critical angle: some light escapes.",
           r"is below the critical angle.",
           r"is just below the $42^\circ$ critical angle."], sort=True),
    ], stim=r"A ray of light in air strikes the flat surface of a block of glass with index of refraction $n = 1.50$, at an angle of incidence of $40^\circ$.",
        stim_title="Questions 5--8"),
    Set("Lenses (13.4)", [
        Q("13.4 Real image", r"An object is $15$ cm from a converging lens with a focal length of $10$ cm. Where does the image form?",
          r"$30$ cm from the lens, on the opposite side", [r"$6.0$ cm from the lens, on the opposite side", r"$30$ cm from the lens, on the same side as the object", r"$5.0$ cm from the lens, on the opposite side"],
          r"$1/s_i = 1/10 - 1/15 = 1/30$, so $s_i = +30$ cm: a real image beyond the lens.",
          [r"Positive $s_i$ for a lens: opposite side, real."],
          [r"adds the reciprocals.",
           r"a positive image distance means a real image on the far side.",
           r"subtracts the distances instead of their reciprocals."]),
        Q("13.4 Magnification", r"For the image in the previous question, which describes its orientation and size?",
          r"inverted and twice as tall as the object", [r"upright and twice as tall", r"inverted and half as tall", r"upright and half as tall"],
          r"$M = -s_i/s_o = -30/15 = -2$.",
          [r"Negative $M$: inverted. $|M| = 2$: twice as tall."],
          [r"real images from a single lens are inverted.",
           r"inverts the ratio of distances.",
           r"real images are inverted, and this one is enlarged."]),
        Q("13.4 Magnifying glass", r"To use a converging lens as a magnifying glass, where must the object be placed?",
          r"closer to the lens than its focal point", [r"exactly at the focal point", r"between $f$ and $2f$ from the lens", r"farther than $2f$ from the lens"],
          r"Inside the focal point, the lens forms a virtual, upright, enlarged image on the object's side.",
          [r"$s_o < f$ gives $s_i < 0$ and $M > 1$."],
          [r"at the focal point the refracted rays are parallel and no image forms.",
           r"gives a real, inverted, enlarged image (a projector).",
           r"gives a real, inverted, smaller image (a camera)."]),
        Q("13.4 Diverging lens", r"Which describes every image formed by a single diverging lens of a real object?",
          r"virtual, upright and smaller than the object", [r"real, inverted and smaller", r"virtual, upright and larger", r"real or virtual, depending on the object's distance"],
          r"A diverging lens spreads rays so they never meet; they appear to come from an upright, reduced image on the object's side.",
          [r"$f < 0$ always gives $s_i < 0$ and $0 < M < 1$."],
          [r"the refracted rays never actually meet.",
           r"enlarged virtual images come from converging lenses.",
           r"a diverging lens makes only virtual images of real objects."]),
        Q("13.4 Covering half a lens", r"A converging lens forms a sharp real image of a candle on a screen. A card is then placed over the top half of the lens. What happens to the image?",
          r"The whole image still forms, but it is dimmer.", [r"The top half of the image disappears.", r"The bottom half of the image disappears.", r"The image becomes blurred but stays as bright."],
          r"Rays from every point of the candle pass through every part of the lens; blocking half the lens removes half the light from each image point.",
          [r"Each part of a lens forms a complete image."],
          [r"each point of the image gets light through the uncovered half too.",
           r"each point of the image gets light through the uncovered half too.",
           r"the remaining rays still meet at the same image points."]),
    ]),
]

UNIT = Unit(13, "geometric-optics", "Geometric Optics", "12--15\\%", "13.1--13.4",
    abstract=r"""Unit 13 treats light as rays: the law of reflection and plane mirrors, images formed by concave and convex mirrors (ray diagrams and the mirror equation), refraction, Snell's law, total internal reflection and dispersion, and images formed by converging and diverging lenses. Sign conventions are set out in the guide and used throughout. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Experimental Design and Analysis", 10, r"""Students want to determine the focal length of a converging lens. They have an optical bench with a meter scale, a lamp with an arrow-shaped cutout to act as an object, the lens in a holder, and a white screen.

\medskip
They record object distances $s_o$ and the image distances $s_i$ at which the image on the screen is sharpest.

\medskip
\begin{tabular}{@{}lccccc@{}}\toprule
$s_o$ (cm) & 15.0 & 20.0 & 25.0 & 30.0 & 40.0 \\ \midrule
$s_i$ (cm) & 29.6 & 20.2 & 16.5 & 15.1 & 13.4 \\ \bottomrule
\end{tabular}""", [
        Part("a", 3, r"Describe a procedure the students could use to collect these data. Include what is measured and one step that reduces experimental uncertainty.",
             r"1 pt: place the lit object, the lens and the screen along the optical bench, with the lens between the object and the screen. 1 pt: for each object distance, move the screen until the image is sharpest, and read $s_o$ and $s_i$ from the bench scale, measured to the center of the lens. 1 pt: repeat the focusing several times for each position (approaching the sharpest image from both sides) and average, and use several object distances, all greater than $f$.",
             r"Measuring to the edge of the lens holder; no step to reduce uncertainty."),
        Part("b", 2, r"Indicate what quantities the students should graph to obtain a straight line from which the focal length can be found, and explain how to find $f$ from the graph.",
             r"1 pt: graph $1/s_i$ versus $1/s_o$ (from $1/s_i = -1/s_o + 1/f$). 1 pt: the vertical intercept is $1/f$ (the slope should be $-1$), so $f = 1/\text{intercept}$.",
             r"Graphing $s_i$ versus $s_o$, which is a curve."),
        Part("c", 3, r"Calculate the values needed for your graph, determine the best-fit line, and use it to determine $f$.",
             r"1 pt: $1/s_o$ (in $\mathrm{cm^{-1}}$): 0.0667, 0.0500, 0.0400, 0.0333, 0.0250; and $1/s_i$: 0.0338, 0.0495, 0.0606, 0.0662, 0.0746. 1 pt: a best-fit line with slope close to $-1$ and vertical intercept about $0.100\ \mathrm{cm^{-1}}$ (accept $0.098$--$0.102$). 1 pt: $f = 1/0.100 = 10$ cm.",
             r"Averaging $f$ from a single pair of distances without a graph."),
        Part("d", 2, r"One student suggests also taking a reading with the object $5.0$ cm from the lens. Explain why the students cannot get a data point this way.",
             r"1 pt: $5.0$ cm is inside the focal length, so the lens forms a virtual image on the same side as the object. 1 pt: light does not actually converge to a virtual image, so it cannot be focused on the screen (the image distance would be negative).",
             r"Saying the image would be too small or too dim to see."),
    ], mins=28),
    frq_topic="finding the focal length of a lens",
)
