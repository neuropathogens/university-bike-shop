from ap_physics_c.model import Q, Sec, Unit, FRQ, Part

S1 = Sec("Vectors, position, and displacement (1.1)", ["1.1"], r"""
Kinematics describes motion without asking what causes it. Every quantity is either a \textbf{scalar} (size only) or a \textbf{vector} (size and direction). In one dimension the direction is just a sign, so choose a positive direction and keep it for the whole problem.

\begin{terms}
Position $x$ & Location relative to a chosen origin. Changing the origin changes $x$ but never $\Delta x$. \\
Displacement $\Delta x = x_f - x_i$ & Vector: depends only on the start and end points. \\
Distance & Scalar: total path length. Distance $\ge |\Delta x|$, equal only if the object never reverses. \\
Speed vs.\ velocity & Speed is $|\vec v|$; average speed $=$ distance$/\Delta t$, average velocity $= \Delta x/\Delta t$. \\
Components & $A_x = A\cos\theta$, $A_y = A\sin\theta$ with $\theta$ from the $+x$ axis; $A = \sqrt{A_x^2 + A_y^2}$. \\
\end{terms}

\begin{trap}
Average speed is not the magnitude of average velocity. A runner who finishes one lap of a 400 m track in 80 s has average speed 5 m/s and average velocity zero.
\end{trap}
""", checks=[
    Q("1.1 Displacement vs. distance", r"A student walks 30 m east, then 40 m west, in a total of 50 s. What are her average speed and the magnitude of her average velocity?",
      r"$1.4$ m/s and $0.20$ m/s", [r"$1.4$ m/s and $1.4$ m/s", r"$0.20$ m/s and $1.4$ m/s", r"$1.0$ m/s and $0.20$ m/s"],
      r"Average speed uses distance (70 m); average velocity uses displacement (10 m west).",
      [r"Distance $= 30 + 40 = 70$ m, so average speed $= 70/50 = 1.4$ m/s.",
       r"Displacement $= +30 - 40 = -10$ m, so $|\bar v| = 10/50 = 0.20$ m/s."],
      [r"treats velocity like speed; the eastward and westward legs partly cancel in the displacement.",
       r"swaps the two: speed uses the 70 m path, velocity the 10 m net displacement.",
       r"uses a 50 m path, as if the legs were perpendicular ($\sqrt{30^2 + 40^2} = 50$); both legs lie on one line, so the path is 70 m."]),
])

S2 = Sec("Velocity and acceleration with calculus (1.2)", ["1.2"], r"""
Velocity is the rate of change of position, and acceleration is the rate of change of velocity:
\[ v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}, \qquad x(t) = x_0 + \int_0^t v\,dt', \qquad v(t) = v_0 + \int_0^t a\,dt'. \]
Differentiate to go \emph{down} the chain ($x \to v \to a$); integrate, and add the initial value, to go \emph{up}.

\begin{keyidea}[Constant acceleration only]
\vspace{-6pt}
\[ v = v_0 + at, \qquad x = x_0 + v_0 t + \tfrac12 a t^2, \qquad v^2 = v_0^2 + 2a(x - x_0). \]
These come from integrating a constant $a$. If $a$ changes with time, position, or velocity, they are wrong; integrate instead.
\end{keyidea}

\textbf{When $a$ depends on $v$ or $x$.} Separate variables. If $a = f(v)$, write $\frac{dv}{dt} = f(v)$, so $\int \frac{dv}{f(v)} = \int dt$. If you want $v$ as a function of $x$, use the chain rule $a = \frac{dv}{dt} = v\frac{dv}{dx}$.

\begin{example}
A boat cuts its engine at speed $v_0$ and the water slows it with $a = -kv$. Then $\frac{dv}{v} = -k\,dt$, so $v = v_0 e^{-kt}$: the boat never quite stops. Its position is $x = \frac{v_0}{k}\left(1 - e^{-kt}\right)$, which approaches $v_0/k$. The boat coasts a \emph{finite} distance $v_0/k$ in infinite time.
\end{example}

\begin{trap}
``Momentarily at rest'' means $v = 0$, not $a = 0$. At the top of a vertical throw $v = 0$ while $a = -g$.
\end{trap}
""", checks=[
    Q("1.2 Derivatives", r"A particle's position is $x(t) = 5 + 2t - t^2$ (meters, seconds). What is its acceleration at $t = 3$ s?",
      r"$-2\ \mathrm{m/s^2}$", [r"$-4\ \mathrm{m/s^2}$", r"$2\ \mathrm{m/s^2}$", r"$-6\ \mathrm{m/s^2}$"],
      r"Differentiate twice: $v = 2 - 2t$, $a = -2$ m/s$^2$ at every instant.",
      [r"$v = dx/dt = 2 - 2t$.", r"$a = dv/dt = -2\ \mathrm{m/s^2}$, independent of $t$."],
      [r"is the velocity at $t = 3$ s, $2 - 6 = -4$ m/s, not the acceleration.",
       r"drops the minus sign: the $-t^2$ term makes the acceleration negative.",
       r"is $-2t$ at $t = 3$; the derivative of $-2t$ is $-2$, not $-2t$."]),
    Q("1.2 Integrating a(t)", r"An object starts from rest with acceleration $a(t) = 4t$ (SI units). How fast is it moving at $t = 3$ s?",
      r"$18$ m/s", [r"$12$ m/s", r"$36$ m/s", r"$6$ m/s"],
      r"Integrate $a(t)$: $v = \int_0^3 4t\,dt = 2t^2\big|_0^3 = 18$ m/s.",
      [r"$v(t) = v_0 + \int_0^t 4t'\,dt' = 0 + 2t^2$.", r"$v(3) = 2(9) = 18$ m/s."],
      [r"is $a(3)$ in m/s$^2$, the acceleration at $t = 3$ s, not the speed.",
       r"is $a(3)\cdot t = 12 \times 3$, which treats the final acceleration as if it acted the whole time.",
       r"is $a(3)/2 = 6$; the average acceleration is $6$ m/s$^2$, so $v = 6 \times 3 = 18$, not 6."], sort=True),
])

S3 = Sec("Representing motion with graphs (1.3)", ["1.3"], r"""
Graphs are the calculus of kinematics drawn as pictures.

\begin{compare}{Graph}{Slope gives}{Area under curve gives}
$x$ vs.\ $t$ & velocity $v$ & (not used) \\
$v$ vs.\ $t$ & acceleration $a$ & displacement $\Delta x$ (area below the axis counts negative) \\
$a$ vs.\ $t$ & (jerk, not tested) & change in velocity $\Delta v$ \\
\end{compare}

\begin{itemize}
\item Concavity of $x(t)$ is the sign of $a$: curving up means $a > 0$.
\item The object turns around where $v$ crosses zero, i.e.\ where the $x$--$t$ graph has a horizontal tangent.
\item Speed increases when $v$ and $a$ have the same sign and decreases when they have opposite signs.
\end{itemize}

\begin{trap}
Distance from a $v$--$t$ graph adds the \emph{magnitudes} of all areas; displacement adds signed areas. Split the graph at every zero crossing.
\end{trap}
""", checks=[
    Q("1.3 Area under a-t", r"A cart moving at $4$ m/s has a constant acceleration of $2\ \mathrm{m/s^2}$ for $3$ s, shown as a horizontal line on an $a$--$t$ graph. What is its speed at the end?",
      r"$10$ m/s", [r"$6$ m/s", r"$13$ m/s", r"$9$ m/s"],
      r"The area under an $a$--$t$ graph is $\Delta v$: $2 \times 3 = 6$ m/s, added to the initial 4 m/s.",
      [r"$\Delta v = \text{area} = (2)(3) = 6$ m/s.", r"$v = 4 + 6 = 10$ m/s."],
      [r"is only the change $\Delta v$; the cart already had 4 m/s.",
       r"adds $\tfrac12 a t^2 = 9$ (a displacement) to 4; area under $a$--$t$ is a velocity change.",
       r"is $\tfrac12 a t^2 = 9$ m, a displacement, written as a speed."], sort=True),
    Q("1.3 Speeding up vs. slowing down", r"At some instant a particle has $v = -3$ m/s and $a = +2\ \mathrm{m/s^2}$. At that instant the particle is",
      r"slowing down", [r"speeding up", r"moving in the $+x$ direction", r"at rest"],
      r"Velocity and acceleration have opposite signs, so the speed is decreasing.",
      [r"Speed $= |v|$ changes at the rate $\frac{d|v|}{dt} = a \cdot \mathrm{sign}(v) = (2)(-1) < 0$."],
      [r"would need $a$ in the same direction as $v$.", r"the negative velocity means it moves in $-x$.", r"$v = -3$ m/s is not zero."]),
])

S4 = Sec("Reference frames and relative motion (1.4)", ["1.4"], r"""
Velocities measured by different observers differ by the velocity of one observer relative to the other:
\[ \vec v_{A/C} = \vec v_{A/B} + \vec v_{B/C}. \]
Read the subscripts as ``A relative to B''. The inner letters cancel like a chain. Acceleration is the same in every frame that moves at constant velocity, so Newton's laws hold in all such (inertial) frames.

\begin{example}[River crossing]
A boat moves at $2.0$ m/s relative to the water; the river flows at $0.80$ m/s. To land directly across, the boat must aim upstream so the water's velocity is cancelled: the ground speed across is $\sqrt{2.0^2 - 0.80^2} = 1.83$ m/s. To cross in the \emph{least time}, aim straight across instead: the crossing speed is the full $2.0$ m/s, and the boat lands downstream.
\end{example}
""", checks=[
    Q("1.4 Relative velocity", r"A train moves east at $30$ m/s. A passenger walks toward the back of the train at $2$ m/s relative to the train. What is the passenger's velocity relative to the ground?",
      r"$28$ m/s east", [r"$32$ m/s east", r"$2$ m/s west", r"$28$ m/s west"],
      r"$\vec v_{P/G} = \vec v_{P/T} + \vec v_{T/G} = (-2) + (+30) = +28$ m/s, east.",
      [r"Take east as $+$: $v_{P/T} = -2$ m/s, $v_{T/G} = +30$ m/s.", r"Add: $+28$ m/s, i.e.\ 28 m/s east."],
      [r"adds the speeds; walking toward the back subtracts.", r"is the velocity relative to the train, not the ground.", r"has the right size but the wrong direction; the train carries her east faster than she walks west."]),
])

S5 = Sec("Motion in two dimensions and projectiles (1.5)", ["1.5"], r"""
In two dimensions, treat $x$ and $y$ separately; they share only the time $t$. With $\vec r(t) = x(t)\,\hat\imath + y(t)\,\hat\jmath$, the velocity and acceleration are $\vec v = \frac{d\vec r}{dt}$ and $\vec a = \frac{d\vec v}{dt}$, component by component.

\begin{keyidea}[Projectile (no air resistance, $+y$ up)]
$a_x = 0$, $a_y = -g$. With launch speed $v_0$ at angle $\theta$:
$v_x = v_0\cos\theta$ (constant), $v_y = v_0\sin\theta - gt$,
$x = v_0\cos\theta\, t$, $y = v_0\sin\theta\, t - \tfrac12 g t^2$.
Peak height $H = \dfrac{(v_0\sin\theta)^2}{2g}$; level-ground range $R = \dfrac{v_0^2 \sin 2\theta}{g}$ (maximum at $45^\circ$).
\end{keyidea}

\begin{trap}
At the top of the path the velocity is horizontal, not zero, and the acceleration is still $g$ downward. Two objects released from the same height at the same time, one dropped and one launched horizontally, land together: horizontal motion does not affect vertical motion.
\end{trap}
""", checks=[
    Q("1.5 Horizontal launch", r"A ball rolls off a $1.25$ m high table at $3.0$ m/s. Ignoring air resistance ($g = 10\ \mathrm{m/s^2}$), how far from the table's edge does it land?",
      r"$1.5$ m", [r"$3.0$ m", r"$1.25$ m", r"$0.75$ m"],
      r"Fall time from $y$ alone: $t = \sqrt{2h/g} = 0.50$ s; then $x = v_x t = 1.5$ m.",
      [r"$1.25 = \tfrac12(10)t^2 \Rightarrow t = 0.50$ s.", r"$x = (3.0)(0.50) = 1.5$ m."],
      [r"assumes a 1 s fall time.", r"assumes the landing distance equals the height; no such rule.", r"uses $t = 0.25$ s, i.e.\ $h/(\tfrac12 g)$ without the square root."], sort=True),
])

QS1 = [
    Q("1.2 Derivatives", r"A particle moves along the $x$-axis with $x(t) = 4t^3 - 6t^2 + 2$, in meters and seconds. What is its velocity at $t = 2$ s?",
      r"$24$ m/s", [r"$10$ m/s", r"$36$ m/s", r"$4$ m/s"],
      r"$v = dx/dt = 12t^2 - 12t$, so $v(2) = 48 - 24 = 24$ m/s.",
      [r"Differentiate term by term: $v = 12t^2 - 12t$.", r"Substitute $t = 2$: $v = 24$ m/s."],
      [r"is the position $x(2) = 32 - 24 + 2 = 10$ m.", r"is the acceleration $a(2) = 24t - 12 = 36$ m/s$^2$.",
       r"is the average velocity from 0 to 2 s, $(10 - 2)/2 = 4$ m/s, not the instantaneous velocity."], sort=True),
    Q("1.2 Turning points", r"For the same particle, $x(t) = 4t^3 - 6t^2 + 2$, at what time $t > 0$ is it momentarily at rest?",
      r"$1.0$ s", [r"$0.50$ s", r"$1.5$ s", r"$2.0$ s"],
      r"At rest means $v = 0$: $12t^2 - 12t = 12t(t - 1) = 0$, so $t = 1.0$ s.",
      [r"$v = 12t(t-1)$ is zero at $t = 0$ and $t = 1$ s.", r"The question asks for $t > 0$: 1.0 s."],
      [r"is where $a = 24t - 12 = 0$, the time of minimum velocity, not zero velocity.",
       r"is where $x$ returns to its starting value of 2 m ($x(1.5) = 13.5 - 13.5 + 2$); position, not velocity.",
       r"is where $v = 24$ m/s, as found in the previous item."], sort=True),
    Q("1.2 Integrating a(t)", r"An object starts from rest at the origin with $a(t) = 6t$ (SI units). What is its position at $t = 2$ s?",
      r"$8$ m", [r"$12$ m", r"$24$ m", r"$48$ m"],
      r"Integrate twice: $v = 3t^2$, $x = t^3$, so $x(2) = 8$ m. The constant-acceleration formulas do not apply.",
      [r"$v = \int_0^t 6t'\,dt' = 3t^2$.", r"$x = \int_0^t 3t'^2\,dt' = t^3 = 8$ m."],
      [r"is $v(2) = 12$ m/s, a velocity.", r"uses $\tfrac12 a t^2$ with $a(2) = 12$; $a$ is not constant.", r"uses $a t^2$ with $a(2)$, which both ignores the varying $a$ and drops the $\tfrac12$."], sort=True),
    Q("1.2 Velocity-dependent acceleration", r"A puck sliding on a rough surface has $a = -kv$, where $k$ is a positive constant, and initial speed $v_0$. How far does the puck travel in total?",
      r"$v_0/k$", [r"It travels infinitely far, because it never stops.", r"$v_0^2/(2k)$", r"$v_0/(2k)$"],
      r"Use $a = v\,dv/dx$: $v\,\frac{dv}{dx} = -kv$ gives $dv/dx = -k$, so $v$ drops linearly with distance and reaches zero after $x = v_0/k$.",
      [r"$v\frac{dv}{dx} = -kv \Rightarrow dv = -k\,dx$.", r"$v = v_0 - kx$, which is zero at $x = v_0/k$.",
       r"In time, $v = v_0 e^{-kt}$ never reaches zero, but $x(t) = \frac{v_0}{k}(1 - e^{-kt})$ approaches $v_0/k$."],
      [r"confuses infinite time with infinite distance; the distances added each second shrink fast enough to sum to $v_0/k$.",
       r"is the constant-deceleration result $v_0^2/(2a)$ with $a$ replaced by $k$, but $k$ has units s$^{-1}$, so the units are wrong.",
       r"puts in a stray factor of 2 from the constant-acceleration formula."]),
    Q("1.3 Distance from v-t", r"A cart's velocity is $v(t) = 3 - 2t$ (m/s) for $0 \le t \le 3$ s. What total distance does it travel in this interval?",
      r"$4.5$ m", [r"$0$ m", r"$2.25$ m", r"$9.0$ m"],
      r"The cart reverses at $t = 1.5$ s. Add the magnitudes of the areas on each side: $2.25 + 2.25 = 4.5$ m.",
      [r"$v = 0$ at $t = 1.5$ s.", r"Area from 0 to 1.5 s: triangle $\tfrac12(1.5)(3) = 2.25$ m forward.",
       r"Area from 1.5 to 3 s: $\tfrac12(1.5)(3) = 2.25$ m backward. Distance $= 4.5$ m; displacement $= 0$."],
      [r"is the displacement; the forward and backward areas cancel, but distance counts both.", r"counts only the first leg.", r"is $3t$ at $t = 3$, which ignores the deceleration."], sort=True),
]

QS2 = [
    Q("1.4 River crossing", r"A river $60$ m wide flows east at $0.80$ m/s. A boat that moves at $2.0$ m/s relative to the water must land directly opposite its starting point. How long does the crossing take?",
      r"$33$ s", [r"$30$ s", r"$28$ s", r"$75$ s"],
      r"Aim upstream so the boat's eastward component cancels the current; the leftover northward component is $\sqrt{2.0^2 - 0.80^2} = 1.83$ m/s.",
      [r"Northward speed $= \sqrt{4.00 - 0.64} = 1.83$ m/s.", r"$t = 60/1.83 = 33$ s."],
      [r"is the time if the boat aims straight across; it then lands downstream.", r"divides by $\sqrt{2.0^2 + 0.80^2} = 2.15$ m/s, adding the current instead of cancelling it.", r"divides by the current's speed."], sort=True),
    Q("1.4 Relative velocity in 2D", r"Rain falls straight down at $8.0$ m/s relative to the ground. A car drives through it at $6.0$ m/s. How fast does the rain move relative to the driver?",
      r"$10$ m/s", [r"$14$ m/s", r"$2.0$ m/s", r"$8.0$ m/s"],
      r"$\vec v_{R/C} = \vec v_{R/G} - \vec v_{C/G}$: a downward 8.0 and a horizontal $-6.0$ are perpendicular, so the magnitude is $\sqrt{64 + 36} = 10$ m/s.",
      [r"The two velocities are perpendicular.", r"$|\vec v_{R/C}| = \sqrt{8.0^2 + 6.0^2} = 10$ m/s, slanting toward the driver."],
      [r"adds the speeds as if they were parallel.", r"subtracts the speeds as if they were parallel.", r"is the speed relative to the ground; the car's motion changes it."], sort=True),
    Q("1.4 Inertial frames", r"A ball is dropped inside a train car that moves at constant velocity. Compared with a person standing on the ground, the passenger and the person agree on the ball's",
      r"acceleration", [r"velocity", r"path shape", r"displacement during the fall"],
      r"Frames moving at constant velocity relative to each other measure the same acceleration, since $\vec a_{A/C} = \vec a_{A/B} + \vec a_{B/C}$ and $\vec a_{B/C} = 0$.",
      [r"The passenger sees a straight vertical drop; the ground observer sees a parabola.", r"Both measure $a = g$ downward."],
      [r"differs by the train's velocity.", r"is a straight line for the passenger and a parabola on the ground.", r"includes the train's horizontal travel for the ground observer."]),
]

QS3 = [
    Q("1.5 Horizontal launch", r"A ball is thrown horizontally at $15$ m/s from the top of a $20$ m cliff. Ignoring air resistance ($g = 9.8\ \mathrm{m/s^2}$), how far from the base of the cliff does it land?",
      r"$30$ m", [r"$21$ m", r"$61$ m", r"$20$ m"],
      r"The fall time comes from the vertical motion alone: $t = \sqrt{2h/g} = 2.02$ s; then $x = v_x t$.",
      [r"$t = \sqrt{2(20)/9.8} = 2.02$ s.", r"$x = 15 \times 2.02 = 30$ m."],
      [r"uses $t = \sqrt{h/g} = 1.43$ s, dropping the factor of 2.", r"uses $t = 2h/g = 4.08$ s, forgetting the square root.", r"assumes the range equals the height."], sort=True),
    Q("1.5 Peak of a trajectory", r"A projectile is launched at $40^\circ$ above level ground. At the highest point of its path, which is true? (Ignore air resistance.)",
      r"Its velocity is horizontal and its acceleration is $g$ downward.", [r"Its velocity and acceleration are both zero.", r"Its velocity is zero and its acceleration is $g$ downward.", r"Its velocity is horizontal and its acceleration is zero."],
      r"Only $v_y$ is zero at the peak; $v_x = v_0\cos 40^\circ$ never changes, and gravity acts throughout.",
      [r"At the peak $v_y = 0$, $v_x = v_0 \cos\theta \ne 0$.", r"$\vec a = -g\,\hat\jmath$ at every point of the flight."],
      [r"would mean the projectile hangs in the air; gravity never switches off.", r"forgets the constant horizontal velocity.", r"forgets that gravity still acts at the top."]),
    Q("1.5 Maximum height", r"A ball is kicked at $20$ m/s at $30^\circ$ above level ground. What is its maximum height? ($g = 9.8\ \mathrm{m/s^2}$)",
      r"$5.1$ m", [r"$15$ m", r"$20$ m", r"$10$ m"],
      r"Only the vertical component matters: $H = (v_0 \sin\theta)^2/(2g) = 10^2/19.6 = 5.1$ m.",
      [r"$v_{0y} = 20 \sin 30^\circ = 10$ m/s.", r"$H = \dfrac{10^2}{2(9.8)} = 5.1$ m."],
      [r"uses $v_0\cos 30^\circ = 17.3$ m/s, the horizontal component: $17.3^2/19.6 = 15$ m.", r"uses the full speed, $20^2/19.6 = 20.4$ m, as if kicked straight up.", r"drops the 2 in $2g$: $10^2/9.8 = 10.2$ m."], sort=True),
    Q("1.5 Vector calculus", r"A particle's position is $\vec r(t) = 3t^2\,\hat\imath + 4t\,\hat\jmath$ (meters, seconds). What is its speed at $t = 1$ s?",
      r"$7.2$ m/s", [r"$10$ m/s", r"$5.0$ m/s", r"$6.0$ m/s"],
      r"Differentiate each component: $\vec v = 6t\,\hat\imath + 4\,\hat\jmath$; at $t = 1$, speed $= \sqrt{36 + 16} = 7.2$ m/s.",
      [r"$\vec v(1) = 6\,\hat\imath + 4\,\hat\jmath$.", r"$|\vec v| = \sqrt{52} = 7.2$ m/s."],
      [r"adds the components, $6 + 4$, instead of combining them with Pythagoras.", r"is the distance from the origin, $|\vec r(1)| = \sqrt{9 + 16}$.", r"is only the $x$-component."], sort=True),
]

UNIT = Unit(
    n=1, slug="kinematics", title="Kinematics", weight="10--15\\%", topics="1.1--1.5",
    abstract=r"""Unit 1 describes motion: position, velocity, and acceleration in one and two dimensions, and how they look to observers in different reference frames. Physics C expects calculus throughout: velocity and acceleration are derivatives, displacement and velocity change are integrals, and the constant-acceleration equations are a special case you must recognize. This guide covers vectors and displacement (1.1), calculus-based kinematics including velocity-dependent acceleration (1.2), motion graphs (1.3), relative motion (1.4), and two-dimensional motion and projectiles (1.5). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5],
    qsections=[("Motion in one dimension (1.1--1.3)", QS1), ("Reference frames (1.4)", QS2), ("Motion in two dimensions (1.5)", QS3)],
    frq=FRQ("Mathematical Routines", 10, r"""A particle moves along the $x$-axis. Its acceleration is $a(t) = 12 - 6t$, in m/s$^2$ with $t$ in seconds. At $t = 0$ the particle is at $x = 0$ and at rest.""", [
        Part("a", 2, r"Derive an expression for the particle's velocity $v(t)$.",
             r"1 pt: integrates $a(t)$ with respect to time. 1 pt: $v(t) = 12t - 3t^2$, with the constant of integration set to zero by $v(0) = 0$.",
             r"Using $v = at$ with $a$ treated as constant."),
        Part("b", 2, r"Determine the particle's maximum speed for $0 \le t \le 4$ s and the time at which it occurs.",
             r"1 pt: sets $a = dv/dt = 0$ (or reads the vertex of $v(t)$), giving $t = 2$ s. 1 pt: $v(2) = 24 - 12 = 12$ m/s.",
             r"Setting $v = 0$ instead of $a = 0$."),
        Part("c", 3, r"The particle is momentarily at rest again at a time $t_1 > 0$. Calculate $t_1$ and the particle's position at that time.",
             r"1 pt: $12t - 3t^2 = 0 \Rightarrow t_1 = 4$ s. 1 pt: integrates $v(t)$ to get $x(t) = 6t^2 - t^3$. 1 pt: $x(4) = 96 - 64 = 32$ m.",
             r"Using $x = v_0 t + \tfrac12 a t^2$ with a single value of $a$."),
        Part("d", 3, r"Calculate the particle's average velocity for $0 \le t \le 4$ s. Explain, with reference to the shape of the velocity--time graph, why this value is less than the maximum speed found in part (b).",
             r"1 pt: $\bar v = \Delta x/\Delta t = 32/4 = 8$ m/s. 1 pt: the $v$--$t$ graph is a downward parabola that is zero at $t = 0$ and $t = 4$ s and peaks at 12 m/s at $t = 2$ s. 1 pt: the particle spends most of the interval moving slower than 12 m/s, so the area under the curve (32 m) is less than the rectangle $12 \times 4 = 48$ m; the average is the height of the rectangle with the same area as the curve.",
             r"Averaging the endpoint velocities, $(0 + 0)/2 = 0$, which works only for constant acceleration."),
    ]),
    frq_topic="calculus-based motion with a time-varying acceleration",
)
