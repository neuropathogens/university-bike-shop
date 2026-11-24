from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Electric charge and Coulomb's law (8.1--8.2)", ["8.1", "8.2"], r"""
\begin{terms}
Charge & Comes in whole multiples of $e = 1.60\times10^{-19}$ C. Electrons carry $-e$, protons $+e$. Like charges repel, unlike attract. \\
Conservation & The net charge of an isolated system never changes; charging moves electrons, it does not create charge. \\
Conductors and insulators & In a conductor, some electrons move freely; in an insulator, charges stay put but molecules can polarize. \\
Charging by conduction & Touch a charged object: charge is shared. Two identical conducting spheres that touch end with equal charges, each half the total. \\
Charging by induction & Bring a charged rod near (no contact), ground the far side, remove the ground, then remove the rod. The object ends with charge \emph{opposite} to the rod's. \\
Polarization & A neutral object is attracted to a charged one: its near side gets the opposite charge, which is closer and so pulled harder. \\
\end{terms}
\[ F = k\frac{|q_1q_2|}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} = 8.99\times10^9\ \mathrm{N\,m^2/C^2}, \qquad \vec F_{net} = \sum\vec F_i\ \ \text{(superposition)}. \]
\begin{trap}
Add Coulomb forces as \emph{vectors}. Find each force's magnitude from $k|q_1q_2|/r^2$, give it a direction from the signs, then add components.
\end{trap}
""", checks=[
    Q("8.1 Coulomb's law scaling", r"Two point charges attract with force $F$. Both charges are doubled and the distance between them is also doubled. What is the new force?",
      r"$F$", [r"$2F$", r"$4F$", r"$F/2$"],
      r"$F \propto q_1q_2/r^2$: the charges give $\times4$, the distance $\div 4$. Net factor 1.",
      [r"$(2)(2)/(2)^2 = 1$."],
      [r"treats distance as $1/r$, not $1/r^2$.", r"forgets the change in distance.", r"doubles the effect of distance or halves the charges' effect."]),
    Q("8.2 Charging by induction", r"A negatively charged rod is held near a neutral metal sphere. With the rod still in place, the sphere is touched by a grounded wire; then the wire is removed, then the rod. What is the sphere's final charge?",
      r"Positive", [r"Negative", r"Neutral", r"It depends on how long the wire touches it"],
      r"The rod repels electrons in the sphere, which escape to ground. With the ground cut before the rod leaves, the sphere is left short of electrons: positive.",
      [r"Rod $(-)$ pushes electrons away, down the ground wire.", r"Ground removed first, so they cannot return: net $+$."],
      [r"is conduction (touching the rod), not induction.", r"would be true if the rod were removed before the ground wire.", r"charge flows until equilibrium almost instantly; the order of steps decides the result."]),
])

S2 = Sec("Electric fields (8.3)", ["8.3"], r"""
\[ \vec E = \frac{\vec F}{q_0}, \qquad \vec E_{point} = k\frac{q}{r^2}\hat r, \qquad \vec F = q\vec E. \]
The field points away from positive charges and toward negative ones. A positive charge accelerates along $\vec E$, a negative one opposite it. Field lines start on positive charges, end on negative ones, never cross, and are denser where the field is stronger. Fields from several charges add as vectors.

\begin{example}[Dipole midpoint]
Charges $+q$ and $-q$ are a distance $d$ apart. At the midpoint both fields point toward $-q$, each $kq/(d/2)^2$, so $E = 8kq/d^2$, directed toward the negative charge.
\end{example}
""", checks=[
    Q("8.3 Dipole field", r"A charge $+q$ is at $x = 0$ and a charge $-q$ at $x = d$. What is the electric field at $x = d/2$?",
      r"$8kq/d^2$, in the $+x$ direction", [r"$0$", r"$4kq/d^2$, in the $+x$ direction", r"$8kq/d^2$, in the $-x$ direction"],
      r"Both fields point toward $-q$ (the $+x$ direction): $2 \times kq/(d/2)^2 = 8kq/d^2$.",
      [r"From $+q$: away from it, $+x$, $4kq/d^2$.", r"From $-q$: toward it, $+x$, $4kq/d^2$. They add."],
      [r"assumes the fields cancel, as they would for two like charges.", r"counts only one charge.", r"has the direction reversed; the field points toward the negative charge."]),
])

S3 = Sec("Electric fields of charge distributions (8.4)", ["8.4"], r"""
For a continuous distribution, break it into point charges $dq$ and integrate, component by component:
\[ \vec E = \int k\frac{dq}{r^2}\hat r, \qquad dq = \lambda\,dl,\ \sigma\,dA,\ \text{or}\ \rho\,dV. \]
Use symmetry first: components that cancel in pairs can be dropped before integrating.
\begin{compare}{Distribution}{Field}{Where}
Ring, charge $Q$, radius $R$ & $\dfrac{kQx}{(x^2 + R^2)^{3/2}}$, along the axis & on the axis, distance $x$ from center (zero at the center) \\
Rod, charge $Q$, length $L$ & $\dfrac{kQ}{d(L + d)}$, along the rod & on the rod's axis, distance $d$ beyond one end \\
Infinite line, $\lambda$ & $\dfrac{\lambda}{2\pi\varepsilon_0 r}$, radially & distance $r$ (finite rod: close to it) \\
Infinite sheet, $\sigma$ & $\dfrac{\sigma}{2\varepsilon_0}$, perpendicular & any distance (large plate: close to it) \\
\end{compare}
Check limits: far from a ring or rod ($x \gg R$, $d \gg L$), each looks like a point charge, $kQ/x^2$.
""", checks=[
    Q("8.4 Ring of charge", r"A uniformly charged ring has total charge $Q$ and radius $R$. What is the electric field at its center?",
      r"Zero", [r"$kQ/R^2$, along the axis", r"$kQ/R^2$, toward the ring", r"$2kQ/R^2$, along the axis"],
      r"Every bit of charge has a partner directly opposite whose field at the center cancels it. Also, $kQx/(x^2 + R^2)^{3/2} = 0$ at $x = 0$.",
      [r"Symmetry: opposite elements' fields cancel.", r"The axial formula gives 0 at $x = 0$."],
      [r"treats the ring as a point charge at distance $R$.", r"the ring has no single direction to point toward from its center.", r"adds fields that actually cancel."]),
])

S4 = Sec("Electric flux (8.5)", ["8.5"], r"""
\[ \Phi_E = \int\vec E\cdot d\vec A, \qquad \text{uniform field, flat area: } \Phi_E = EA\cos\theta, \]
where $\theta$ is the angle between $\vec E$ and the area vector $\vec A$, which is \emph{perpendicular} to the surface (outward for a closed surface). Flux counts field lines through a surface: maximum when the surface faces the field, zero when the field skims along it.
\begin{trap}
If a problem gives the angle between the field and the \emph{surface}, the angle to the area vector is its complement: use $\sin$, not $\cos$.
\end{trap}
""", checks=[
    Q("8.5 Flux through a closed surface", r"A point charge sits outside a closed cubical surface. What is the net electric flux through the cube?",
      r"Zero", [r"$q/\varepsilon_0$", r"$q/(6\varepsilon_0)$", r"It depends on the distance from the charge to the cube."],
      r"Every field line from the outside charge that enters the cube also leaves it, so inward and outward flux cancel. Gauss's law: $Q_{enc} = 0$.",
      [r"Net flux $= Q_{enc}/\varepsilon_0 = 0$."],
      [r"is the flux if the charge were inside.", r"is the flux through one face for a charge at the cube's center.", r"the flux through each face depends on distance, but the net through the closed surface does not."]),
])

S5 = Sec("Gauss's law (8.6)", ["8.6"], r"""
\[ \oint\vec E\cdot d\vec A = \frac{Q_{enc}}{\varepsilon_0}. \]
Gauss's law is always true, but it gives $E$ only when symmetry lets you pull $E$ out of the integral. Pick a Gaussian surface on which $E$ is constant and perpendicular (or parallel) to the surface:
\begin{compare}{Symmetry}{Gaussian surface}{Result}
Spherical & concentric sphere, radius $r$ & $E(4\pi r^2) = Q_{enc}/\varepsilon_0$ \\
Cylindrical (long line or cylinder) & coaxial cylinder, radius $r$, length $\ell$ & $E(2\pi r\ell) = Q_{enc}/\varepsilon_0$ \\
Planar (large sheet) & pillbox through the sheet, end area $A$ & $E(2A) = \sigma A/\varepsilon_0$ \\
\end{compare}
\begin{example}[Uniformly charged solid sphere, radius $R$, charge $Q$]
Outside: $E = kQ/r^2$. Inside: $Q_{enc} = Q r^3/R^3$, so $E = \dfrac{kQr}{R^3}$, growing linearly from zero at the center to $kQ/R^2$ at the surface. For a nonuniform density $\rho(r)$, find $Q_{enc} = \int_0^r \rho(r')\,4\pi r'^2\,dr'$ first.
\end{example}
""", checks=[
    Q("8.6 Inside a charged sphere", r"A solid insulating sphere of radius $R$ has charge spread uniformly through its volume. The field at its surface is $E_0$. What is the field at $r = R/2$?",
      r"$E_0/2$", [r"$E_0/4$", r"$4E_0$", r"$0$"],
      r"Inside a uniform sphere $E = kQr/R^3 \propto r$, so halving $r$ halves $E$.",
      [r"$Q_{enc} = Q(r/R)^3 = Q/8$ at $r = R/2$.", r"$E = kQ_{enc}/r^2 = k(Q/8)/(R/2)^2 = \tfrac12 kQ/R^2$."],
      [r"assumes $E$ grows as $r^2$; inside, $Q_{enc} \propto r^3$ while the Gaussian area $\propto r^2$, so $E \propto r$.", r"applies $1/r^2$ with the full charge $Q$, as if all the charge were enclosed.", r"is true inside a conductor or a charged shell, not inside a uniformly charged solid insulator."]),
])

QS1 = [
    Q("8.1 Coulomb's law", r"A $+2.0\ \mu\mathrm{C}$ charge and a $-3.0\ \mu\mathrm{C}$ charge are 0.30 m apart. What is the magnitude of the force between them? ($k = 9.0\times10^9\ \mathrm{N\,m^2/C^2}$)",
      r"$0.60$ N", [r"$0.18$ N", r"$6.0$ N", r"$0.060$ N"],
      r"$F = k|q_1q_2|/r^2 = (9.0\times10^9)(6.0\times10^{-12})/0.090 = 0.60$ N (attractive).",
      [r"$|q_1q_2| = 6.0\times10^{-12}\ \mathrm{C^2}$.", r"$F = 0.054/0.090 = 0.60$ N."],
      [r"divides by $r$ instead of $r^2$.", r"squares $0.30$ as $0.0090$.", r"drops a factor of 10 in the arithmetic."], sort=True),
    Q("8.1 Superposition", r"A charge $+q$ is at $x = 0$ and a charge $+4q$ is at $x = 3.0$ m. Where on the $x$-axis is the net force on a third charge zero?",
      r"$x = 1.0$ m", [r"$x = 1.5$ m", r"$x = 2.0$ m", r"$x = 0.60$ m"],
      r"Between the charges the two forces oppose. Set $\dfrac{kq}{x^2} = \dfrac{k(4q)}{(3.0 - x)^2}$: $3.0 - x = 2x$, so $x = 1.0$ m, closer to the smaller charge.",
      [r"Take square roots: $\dfrac{1}{x} = \dfrac{2}{3.0 - x}$.", r"$x = 1.0$ m."],
      [r"is the midpoint, correct only for equal charges.", r"is closer to the larger charge, where its force wins.", r"forgets to take the square root of 4: $3.0 - x = 4x$."], sort=True),
    Q("8.2 Charge sharing", r"Two identical metal spheres carry $+6.0\ \mu\mathrm{C}$ and $-2.0\ \mu\mathrm{C}$. They are touched together and separated. What is the charge on each?",
      r"$+2.0\ \mu\mathrm{C}$ each", [r"$+4.0\ \mu\mathrm{C}$ each", r"$+3.0\ \mu\mathrm{C}$ and $+1.0\ \mu\mathrm{C}$", r"$+6.0\ \mu\mathrm{C}$ and $-2.0\ \mu\mathrm{C}$"],
      r"Total charge $+4.0\ \mu\mathrm{C}$ is conserved and, for identical conductors, shared equally: $+2.0\ \mu\mathrm{C}$ each.",
      [r"Net charge $= 6.0 - 2.0 = +4.0\ \mu\mathrm{C}$.", r"Identical spheres split it evenly."],
      [r"gives each sphere the whole net charge, doubling the total.", r"halves each charge separately; charge flows until the spheres match.", r"assumes no charge moves on contact; conductors share charge."]),
    Q("8.3 Superposition of fields", r"Equal charges $+q$ sit at $(a, 0)$ and $(0, a)$. What is the magnitude of the electric field at the origin?",
      r"$\sqrt2\,kq/a^2$", [r"$2kq/a^2$", r"$0$", r"$kq/(2a^2)$"],
      r"Each charge gives $kq/a^2$; one points in $-x$, the other in $-y$. They are perpendicular: $\sqrt2\,kq/a^2$.",
      [r"$\vec E = -\dfrac{kq}{a^2}\hat\imath - \dfrac{kq}{a^2}\hat\jmath$.", r"$|\vec E| = \sqrt2\,kq/a^2$."],
      [r"adds magnitudes of perpendicular vectors.", r"assumes like charges cancel; they would only if opposite each other.", r"uses the charge-to-charge distance $\sqrt2\,a$, which is not the distance to the origin."]),
    Q("8.3 Electron in a field", r"An electron is released in a uniform electric field of 1000 N/C. What is the magnitude of its acceleration? ($e = 1.6\times10^{-19}$ C, $m_e = 9.1\times10^{-31}$ kg)",
      r"$1.8\times10^{14}\ \mathrm{m/s^2}$", [r"$1.6\times10^{-16}\ \mathrm{m/s^2}$", r"$9.6\times10^{10}\ \mathrm{m/s^2}$", r"$5.7\times10^{-15}\ \mathrm{m/s^2}$"],
      r"$a = eE/m = (1.6\times10^{-19})(1000)/(9.1\times10^{-31}) = 1.8\times10^{14}\ \mathrm{m/s^2}$; gravity is negligible.",
      [r"$F = eE = 1.6\times10^{-16}$ N.", r"$a = F/m_e = 1.76\times10^{14}\ \mathrm{m/s^2}$."],
      [r"is the force in newtons.", r"uses the proton's mass ($1.67\times10^{-27}$ kg).", r"inverts $F/m$."], sort=True),
    Q("8.4 Ring on its axis", r"For a uniformly charged ring of radius $R$, $E(x) = \dfrac{kQx}{(x^2 + R^2)^{3/2}}$ along its axis. At what distance $x$ from the center is the axial field strongest?",
      r"$R/\sqrt2$", [r"$R$", r"$0$", r"$R/2$"],
      r"Set $dE/dx = 0$: $(x^2 + R^2) - 3x^2 = 0$, so $x = R/\sqrt2$.",
      [r"$\dfrac{dE}{dx} \propto (x^2 + R^2)^{-5/2}\left[(x^2 + R^2) - 3x^2\right]$.", r"Zero when $R^2 = 2x^2$."],
      [r"is a guess from the ring's size; the derivative is not zero there.", r"is where the field is zero, the minimum.", r"is not where $dE/dx$ vanishes."]),
    Q("8.4 Field of a rod", r"A thin rod of length $L$ with uniform charge $Q$ lies on the $x$-axis from $x = 0$ to $x = L$. What is the electric field at $x = L + d$?",
      r"$\dfrac{kQ}{d(L + d)}$", [r"$\dfrac{kQ}{d^2}$", r"$\dfrac{kQ}{(L + d)^2}$", r"$\dfrac{kQ}{(d + L/2)^2}$"],
      r"$E = \int_0^L \dfrac{k\lambda\,dx}{(L + d - x)^2} = k\lambda\left[\dfrac1d - \dfrac{1}{L + d}\right] = \dfrac{kQ}{d(L + d)}$ with $\lambda = Q/L$.",
      [r"$dq = (Q/L)dx$ at distance $L + d - x$.", r"Integrate: $k\lambda\,\dfrac{L}{d(L + d)}$."],
      [r"puts all the charge at the near end.", r"puts all the charge at the far end.", r"puts all the charge at the center; that is right only far away ($d \gg L$)."]),
    Q("8.4 Line of charge", r"A long straight wire carries uniform charge per length $\lambda$. At distance $r$ the field is $E$. What is the field at distance $2r$?",
      r"$E/2$", [r"$E/4$", r"$E$", r"$E/\sqrt2$"],
      r"For a long line, $E = \lambda/(2\pi\varepsilon_0 r) \propto 1/r$.",
      [r"Gauss's law with a cylinder: $E(2\pi r\ell) = \lambda\ell/\varepsilon_0$."],
      [r"is point-charge behavior ($1/r^2$).", r"is sheet behavior (independent of distance).", r"has no basis."]),
    Q("8.5 Flux through a flat surface", r"A uniform field of 500 N/C passes through a flat $0.20\ \mathrm{m} \times 0.30\ \mathrm{m}$ rectangle. The field makes a $30^\circ$ angle with the rectangle's normal (area vector). What is the flux?",
      r"$26\ \mathrm{N\,m^2/C}$", [r"$30\ \mathrm{N\,m^2/C}$", r"$15\ \mathrm{N\,m^2/C}$", r"$0$"],
      r"$\Phi = EA\cos\theta = (500)(0.060)\cos 30^\circ = 26\ \mathrm{N\,m^2/C}$.",
      [r"$A = 0.060\ \mathrm{m^2}$.", r"$\Phi = 30 \times 0.866 = 26\ \mathrm{N\,m^2/C}$."],
      [r"assumes the field is along the normal.", r"uses $\sin 30^\circ$, which is right only if the $30^\circ$ is measured from the surface.", r"is the flux through a closed surface with no charge inside, not through an open rectangle."], sort=True),
    Q("8.6 Gauss's law and symmetry", r"A point charge $q$ is at the center of a cube. What is the electric flux through one face of the cube?",
      r"$\dfrac{q}{6\varepsilon_0}$", [r"$\dfrac{q}{\varepsilon_0}$", r"$\dfrac{q}{4\pi\varepsilon_0}$", r"$0$"],
      r"The total flux through the cube is $q/\varepsilon_0$, and by symmetry each of the six faces gets an equal share.",
      [r"$\Phi_{total} = q/\varepsilon_0$.", r"Six identical faces: $q/(6\varepsilon_0)$ each."],
      [r"is the flux through the whole cube.", r"is $kq$, which has no meaning as a flux here.", r"the charge is inside, so the flux is nonzero."]),
    Q("8.6 Nonuniform charge density", r"A solid insulating sphere of radius $R$ has charge density $\rho = \rho_0 r/R$. What is the electric field at a distance $r < R$ from the center?",
      r"$\dfrac{\rho_0 r^2}{4\varepsilon_0 R}$", [r"$\dfrac{\rho_0 r}{3\varepsilon_0}$", r"$\dfrac{\rho_0 r^2}{3\varepsilon_0 R}$", r"$\dfrac{\rho_0 R^2}{4\varepsilon_0 r}$"],
      r"$Q_{enc} = \int_0^r \dfrac{\rho_0 r'}{R}4\pi r'^2\,dr' = \dfrac{\pi\rho_0 r^4}{R}$. Gauss: $E(4\pi r^2) = Q_{enc}/\varepsilon_0$, so $E = \dfrac{\rho_0 r^2}{4\varepsilon_0 R}$.",
      [r"Integrate the density over shells: $Q_{enc} = \pi\rho_0 r^4/R$.", r"Divide by $4\pi r^2\varepsilon_0$."],
      [r"is the result for a uniform density $\rho_0$.", r"uses $Q_{enc} = \rho(r)\cdot\tfrac43\pi r^3$, treating the density at $r$ as if it filled the whole inner sphere.", r"is an outside-the-sphere form ($\propto 1/r$) with the wrong total charge."]),
    Q("8.6 Charged sheet", r"A large, flat, uniformly charged sheet produces a field $E$ at 2.0 cm from its surface. What is the field 4.0 cm from the sheet (still close compared with its size)?",
      r"$E$", [r"$E/2$", r"$E/4$", r"$2E$"],
      r"A large sheet gives $E = \sigma/(2\varepsilon_0)$, independent of distance: the field lines are parallel and do not spread.",
      [r"Gauss's pillbox: $E(2A) = \sigma A/\varepsilon_0$, no $r$ dependence."],
      [r"is line-charge behavior.", r"is point-charge behavior.", r"fields from a sheet do not grow with distance."]),
]

UNIT = Unit(
    n=8, slug="charges-fields-gauss", title="Electric Charges, Fields, and Gauss's Law", weight="15--25\\%", topics="8.1--8.6",
    abstract=r"""Unit 8 opens the E\&M course. It covers charge, charging processes, and Coulomb's law with superposition (8.1--8.2); the electric field of point charges (8.3); fields of continuous distributions by integration (8.4); electric flux (8.5); and Gauss's law for spherical, cylindrical, and planar symmetry, including nonuniform charge densities (8.6). The E\&M exam has the same format as Mechanics: multiple choice for half the score and four free-response questions for the other half. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5],
    qsections=[("Charge, force, and field (8.1--8.3)", QS1[:5]), ("Charge distributions (8.4)", QS1[5:8]), ("Flux and Gauss's law (8.5--8.6)", QS1[8:])],
    frq=FRQ("Mathematical Routines", 10, r"""A very long, solid, insulating cylinder of radius $R$ has positive charge spread uniformly through its volume with charge density $\rho$. Express answers in terms of $\rho$, $R$, $r$, and physical constants.""", [
        Part("a", 3, r"Use Gauss's law to derive the magnitude of the electric field at a distance $r < R$ from the cylinder's axis.",
             r"1 pt: Gaussian surface is a coaxial cylinder of radius $r$ and length $\ell$; no flux through the end caps. 1 pt: $Q_{enc} = \rho\pi r^2\ell$. 1 pt: $E(2\pi r\ell) = \rho\pi r^2\ell/\varepsilon_0 \Rightarrow E = \dfrac{\rho r}{2\varepsilon_0}$.",
             r"Using a sphere as the Gaussian surface."),
        Part("b", 3, r"Derive the magnitude of the electric field at a distance $r > R$ from the axis.",
             r"1 pt: same coaxial surface, now outside. 1 pt: $Q_{enc} = \rho\pi R^2\ell$. 1 pt: $E = \dfrac{\rho R^2}{2\varepsilon_0 r}$.",
             r"Enclosing $\rho\pi r^2\ell$ outside the cylinder, where there is no charge."),
        Part("c", 2, r"Let $\lambda$ be the charge per unit length of the cylinder. Write $\lambda$ in terms of $\rho$ and $R$, and show that your answer to (b) matches the field of a thin line of charge $\lambda$.",
             r"1 pt: $\lambda = \rho\pi R^2$. 1 pt: substituting gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, the line-charge field.",
             r"Stating the line-charge result without substituting."),
        Part("d", 2, r"At what distance from the axis is the field strongest, and what is its value there? Justify your answer from (a) and (b).",
             r"1 pt: $E$ grows linearly inside and falls as $1/r$ outside, so it peaks at $r = R$. 1 pt: $E_{max} = \dfrac{\rho R}{2\varepsilon_0}$ (both expressions agree at $r = R$).",
             r"Saying the field is largest on the axis."),
    ]),
    frq_topic="Gauss's law for a uniformly charged cylinder",
)
