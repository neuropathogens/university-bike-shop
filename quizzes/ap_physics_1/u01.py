from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

BIKE = Graph(r"Time $t$ (s)", r"Velocity $v$ (m/s)", x=(0, 12, 2), y=(0, 10, 2),
             series=[Series("bicycle", [(0, 0), (4, 8), (10, 8), (12, 0)], marks=False)])
CART = Graph(r"Time $t$ (s)", r"Velocity $v$ (m/s)", x=(0, 10, 2), y=(-6, 8, 2),
             series=[Series("cart", [(0, 0), (2, 6), (6, 6), (8, 0), (10, -4)], marks=False)])

S1 = Sec("Scalars, vectors and displacement (1.1)", ["1.1"], r"""
Kinematics describes motion without asking what causes it. A \textbf{scalar} has only a size (mass, time, distance, speed); a \textbf{vector} has a size and a direction (displacement, velocity, acceleration, force). In one dimension the direction is just a sign: choose a positive direction at the start and keep it for the whole problem.

\begin{terms}
Position $x$ & Location relative to a chosen origin. Moving the origin changes $x$ but never $\Delta x$. \\
Displacement $\Delta x = x_f - x_i$ & A vector that depends only on where the motion starts and ends. \\
Distance & A scalar: the total length of the path. Distance $\ge |\Delta x|$, equal only if the object never reverses. \\
Average speed & distance $\div$ time; never negative. \\
Average velocity & $\bar v = \Delta x/\Delta t$; its sign gives the direction. \\
\end{terms}

\begin{trap}
Average speed is not the size of the average velocity. A swimmer who swims one 50 m length and back in 60 s has an average speed of $1.7$ m/s and an average velocity of zero.
\end{trap}
""", checks=[
    Q("1.1 Distance vs. displacement", r"A jogger runs 120 m north, then 50 m south, in a total of 85 s. What are the jogger's average speed and the magnitude of the average velocity?",
      r"$2.0$ m/s and $0.82$ m/s", [r"$2.0$ m/s and $2.0$ m/s", r"$0.82$ m/s and $2.0$ m/s", r"$1.5$ m/s and $0.82$ m/s"],
      r"Average speed uses the distance (170 m); average velocity uses the displacement (70 m north).",
      [r"Distance $= 120 + 50 = 170$ m, so average speed $= 170/85 = 2.0$ m/s.",
       r"Displacement $= +120 - 50 = +70$ m, so $|\bar v| = 70/85 = 0.82$ m/s."],
      [r"treats velocity like speed: the southward leg cancels part of the northward one in the displacement.",
       r"swaps the two: speed goes with the 170 m path, velocity with the 70 m displacement.",
       r"uses a 130 m path, as if the legs were perpendicular ($\sqrt{120^2 + 50^2}$); both legs lie on one line."]),
])

S2 = Sec("Displacement, velocity and acceleration (1.2)", ["1.2"], r"""
Velocity is the rate of change of position and acceleration is the rate of change of velocity:
\[ \bar v = \frac{\Delta x}{\Delta t}, \qquad \bar a = \frac{\Delta v}{\Delta t}. \]
The \emph{instantaneous} value is the same ratio over a very short interval: the slope of the tangent on a graph.

\begin{keyidea}[Constant acceleration (on the equation sheet)]
\vspace{-6pt}
\[ v_x = v_{x0} + a_x t, \qquad x = x_0 + v_{x0}t + \tfrac12 a_x t^2, \qquad v_x^2 = v_{x0}^2 + 2a_x(x - x_0). \]
Pick the equation that leaves out the quantity you neither know nor want. They hold only while $a$ is constant; if the acceleration changes, split the motion into stages.
\end{keyidea}

\textbf{Speeding up or slowing down?} Compare signs. If $v$ and $a$ have the same sign the object speeds up; if they have opposite signs it slows down. A negative acceleration alone says nothing about slowing.

\textbf{Free fall.} Near Earth's surface, with air resistance negligible, every object accelerates downward at $g = 9.8\ \mathrm{m/s^2}$, whatever its mass and whether it is rising, at the top, or falling.

\begin{example}
A car braking from $25$ m/s with $a = -5.0\ \mathrm{m/s^2}$ stops in $t = 25/5.0 = 5.0$ s and travels $v_0^2/(2|a|) = 625/10 = 62.5$ m. At twice the speed it would need four times the distance.
\end{example}

\begin{trap}
``Momentarily at rest'' means $v = 0$, not $a = 0$. At the top of a vertical throw $v = 0$ while $a = -g$.
\end{trap}
""", checks=[
    Q("1.2 Constant acceleration", r"A car accelerates uniformly from rest to $24$ m/s in $8.0$ s. How far does it travel in that time?",
      r"$96$ m", [r"$192$ m", r"$12$ m", r"$288$ m"],
      r"With $a = 24/8.0 = 3.0\ \mathrm{m/s^2}$, $x = \tfrac12 a t^2 = 96$ m (or average velocity $12$ m/s times $8.0$ s).",
      [r"$a = \Delta v/\Delta t = 24/8.0 = 3.0\ \mathrm{m/s^2}$.", r"$x = \tfrac12(3.0)(8.0)^2 = 96$ m."],
      [r"is the final speed times the time, as if the car moved at $24$ m/s the whole way.",
       r"forgets to square the time: $\tfrac12(3.0)(8.0) = 12$.",
       r"treats $24$ m/s as the initial speed: $24(8.0) + \tfrac12(3.0)(8.0)^2$."], sort=True),
    Q("1.2 Free fall", r"A ball is dropped from rest from a height of $20$ m. Ignoring air resistance, about how fast is it moving just before it hits the ground?",
      r"$20$ m/s", [r"$14$ m/s", r"$196$ m/s", r"$2.0$ m/s"],
      r"$v^2 = 2gh = 2(9.8)(20) = 392$, so $v = 19.8 \approx 20$ m/s.",
      [r"$v^2 = v_0^2 + 2a\Delta y$ with $v_0 = 0$ and $|a| = g$.", r"$v = \sqrt{392} = 19.8$ m/s."],
      [r"leaves out the factor 2: $\sqrt{9.8 \times 20}$.",
       r"is $g \times h$ with no square root (and the wrong units).",
       r"is the time of the fall in seconds, $\sqrt{2h/g} = 2.0$ s, not the speed."], sort=True),
])

S3 = Sec("Representing motion (1.3)", ["1.3"], r"""
The exam expects you to move freely between graphs, equations and motion diagrams.

\begin{compare}{Graph}{Slope gives}{Area under the curve gives}
Position vs.\ time & velocity & (nothing useful) \\
Velocity vs.\ time & acceleration & displacement (area below the axis counts as negative) \\
Acceleration vs.\ time & (rate of change of $a$, not tested) & change in velocity \\
\end{compare}

On a position--time graph, a straight line means constant velocity; a curve that gets steeper means speeding up. On a velocity--time graph, a horizontal line means constant velocity and a straight sloped line means constant acceleration. In a \textbf{motion diagram} (dots at equal time intervals), equally spaced dots mean constant velocity and spreading dots mean speeding up.

\begin{example}
A bicycle speeds up uniformly from rest to $8$ m/s in $4$ s, rides at $8$ m/s until $t = 10$ s, then brakes uniformly to rest at $t = 12$ s. Its velocity--time graph (in the first check below) is three straight segments: the slopes give accelerations of $2.0$, $0$ and $-4.0\ \mathrm{m/s^2}$, and the area under it is the distance traveled.
\end{example}
""", checks=[
    Q("1.3 Area under v-t", r"The graph shows the velocity of a bicycle moving along a straight road. How far does it travel from $t = 0$ to $t = 12$ s?",
      r"$72$ m", [r"$96$ m", r"$64$ m", r"$48$ m"],
      r"Displacement is the area under the velocity--time graph: $16 + 48 + 8 = 72$ m.",
      [r"$0$--$4$ s: $\tfrac12(4)(8) = 16$ m.", r"$4$--$10$ s: $6 \times 8 = 48$ m.", r"$10$--$12$ s: $\tfrac12(2)(8) = 8$ m; total $72$ m."],
      [r"assumes $8$ m/s for all 12 s, ignoring the speeding up and slowing down.",
       r"stops at $t = 10$ s and leaves out the braking.",
       r"counts only the constant-speed rectangle."], sort=True, fig=BIKE),
    Q("1.3 Position-time graphs", r"An object's position--time graph is a straight line sloping downward. What does this show?",
      r"constant velocity in the negative direction", [r"constant negative acceleration", r"slowing down to rest", r"speeding up in the negative direction"],
      r"The slope of a position--time graph is the velocity; a constant negative slope is a constant negative velocity.",
      [r"Straight line: constant slope, so constant velocity and zero acceleration.", r"Downward: the velocity is negative."],
      [r"would be a straight sloped line on a velocity--time graph; on a position--time graph it is a curve.",
       r"would show as a curve that levels off.",
       r"would show as a curve that gets steeper downward."]),
])

S4 = Sec("Reference frames and relative motion (1.4)", ["1.4"], r"""
Every velocity is measured relative to some observer (a \textbf{reference frame}). If object $A$ moves relative to $B$, and $B$ moves relative to the ground $C$,
\[ \vec v_{A\text{ rel }C} = \vec v_{A\text{ rel }B} + \vec v_{B\text{ rel }C}. \]
In one dimension this is adding or subtracting with signs; in two dimensions add the vectors tip to tail, using components or the Pythagorean theorem for perpendicular velocities.

\textbf{Same acceleration in every inertial frame.} Observers moving at constant velocity relative to one another measure different velocities for an object but the same acceleration, so they agree on the forces.

\begin{example}
A boat heads straight across a river at $4.0$ m/s relative to the water while the current flows at $3.0$ m/s. Relative to the shore the boat moves at $\sqrt{4.0^2 + 3.0^2} = 5.0$ m/s, angled downstream. The crossing time depends only on the $4.0$ m/s across.
\end{example}
""", checks=[
    Q("1.4 Relative velocity", r"A train moves at $20$ m/s relative to the ground. Passenger $P$ walks toward the front at $1.5$ m/s relative to the train, and passenger $Q$ walks toward the back at $1.5$ m/s relative to the train. What is $Q$'s velocity relative to $P$?",
      r"$3.0$ m/s toward the back of the train", [r"zero, since they walk at the same speed", r"$18.5$ m/s toward the front", r"$1.5$ m/s toward the back of the train"],
      r"Relative to the ground, $P$ moves at $21.5$ m/s and $Q$ at $18.5$ m/s (forward); $Q$ relative to $P$ is $18.5 - 21.5 = -3.0$ m/s.",
      [r"$v_{Q\text{ rel }P} = v_{Q\text{ rel train}} - v_{P\text{ rel train}} = -1.5 - 1.5 = -3.0$ m/s."],
      [r"ignores direction: equal speeds in opposite directions do not give zero relative velocity.",
       r"is $Q$'s velocity relative to the ground.",
       r"is $Q$'s velocity relative to the train, as if $P$ stood still."]),
    Q("1.4 Velocities at right angles", r"A boat heads straight across a river at $4.0$ m/s relative to the water. The river flows at $3.0$ m/s. What is the boat's speed relative to the shore?",
      r"$5.0$ m/s", [r"$7.0$ m/s", r"$1.0$ m/s", r"$4.0$ m/s"],
      r"The velocities are perpendicular: $\sqrt{4.0^2 + 3.0^2} = 5.0$ m/s.",
      [r"$\vec v_{\text{boat rel shore}} = \vec v_{\text{boat rel water}} + \vec v_{\text{water rel shore}}$, at right angles."],
      [r"adds the speeds as if both pointed the same way.",
       r"subtracts them, as if the current opposed the boat head-on.",
       r"ignores the current; that is the speed relative to the water."], sort=True),
])

S5 = Sec("Vectors and motion in two dimensions (1.5)", ["1.5"], r"""
Resolve a vector into perpendicular components: $A_x = A\cos\theta$, $A_y = A\sin\theta$ for $\theta$ measured from the $+x$ axis, and $A = \sqrt{A_x^2 + A_y^2}$.

\begin{keyidea}[Projectile motion]
With air resistance negligible, a projectile has $a_x = 0$ and $a_y = -g$. The horizontal and vertical motions are independent and share only the time: horizontal velocity stays $v_0\cos\theta$, while the vertical motion is free fall that starts at $v_0\sin\theta$.
\end{keyidea}

\begin{terms}
Time of flight & set by the vertical motion alone; a horizontally launched ball falls as long as a dropped one \\
At the top & $v_y = 0$ but $v_x \ne 0$, so the speed is $v_0\cos\theta$, its minimum \\
Level ground & the path is symmetric; range is greatest at $45^\circ$ and equal for complementary angles ($30^\circ$ and $60^\circ$) \\
\end{terms}

\begin{example}
A ball rolls off a $1.25$ m high table at $2.0$ m/s. Vertically, $1.25 = \tfrac12(9.8)t^2$ gives $t = 0.51$ s; horizontally, it lands $2.0 \times 0.51 = 1.0$ m from the edge.
\end{example}
""", checks=[
    Q("1.5 Horizontal launch", r"A ball rolls off the edge of a horizontal table $1.25$ m high at $2.0$ m/s. How far from the foot of the table does it land?",
      r"$1.0$ m", [r"$0.51$ m", r"$2.5$ m", r"$2.0$ m"],
      r"The fall time is $t = \sqrt{2h/g} = 0.51$ s; the horizontal distance is $2.0 \times 0.51 = 1.0$ m.",
      [r"Vertical: $1.25 = \tfrac12(9.8)t^2$, so $t = 0.505$ s.", r"Horizontal: $x = v_x t = 2.0(0.505) = 1.0$ m."],
      [r"is the fall time in seconds, not a distance.",
       r"multiplies the speed by the height.",
       r"assumes the ball is in the air for 1.0 s."], sort=True),
    Q("1.5 Speed at the top", r"A projectile is launched over level ground at $20$ m/s at $30^\circ$ above the horizontal. What is its speed at the highest point?",
      r"$17$ m/s", [r"$0$", r"$10$ m/s", r"$20$ m/s"],
      r"At the top only the vertical component is zero; the horizontal component $20\cos 30^\circ = 17$ m/s remains.",
      [r"$v_x = 20\cos30^\circ = 17.3$ m/s throughout the flight.", r"At the top $v_y = 0$, so the speed is $17$ m/s."],
      [r"forgets the horizontal velocity, which never changes.",
       r"is the initial vertical component, $20\sin30^\circ$.",
       r"is the launch speed; the speed is $20$ m/s again only at launch height."], sort=True),
])

QS = [
    Set("Velocity and acceleration (1.1--1.2)", [
        Q("1.2 Signs of v and a", r"An object moving in the $+x$ direction has a negative acceleration. Which must be true at that instant?",
          r"Its speed is decreasing.", [r"It is moving in the $-x$ direction.", r"Its velocity is negative.", r"Its speed is increasing."],
          r"Velocity is positive and acceleration negative: opposite signs, so the object slows down.",
          [r"Same signs: speeding up. Opposite signs: slowing down."],
          [r"contradicts the question: it moves in the $+x$ direction.",
           r"confuses the sign of the acceleration with the sign of the velocity.",
           r"would need $a$ in the same direction as $v$."]),
        Q("1.2 Stopping distance", r"A train slows uniformly from $30$ m/s to $10$ m/s over a distance of $400$ m. What is its acceleration?",
          r"$-1.0\ \mathrm{m/s^2}$", [r"$-0.05\ \mathrm{m/s^2}$", r"$-2.0\ \mathrm{m/s^2}$", r"$-1.1\ \mathrm{m/s^2}$"],
          r"$v^2 = v_0^2 + 2a\Delta x$: $100 = 900 + 2a(400)$, so $a = -1.0\ \mathrm{m/s^2}$.",
          [r"No time is given, so use $v^2 = v_0^2 + 2a\Delta x$.", r"$a = (10^2 - 30^2)/(2 \times 400) = -800/800 = -1.0\ \mathrm{m/s^2}$."],
          [r"divides the change in velocity by the distance, which has the wrong units.",
           r"leaves out the factor 2 in $2a\Delta x$.",
           r"ignores the final speed, as if the train stopped: $-30^2/800$."], sort=True),
        Q("1.2 Top of a vertical throw", r"A ball is thrown straight up. Air resistance is negligible. At the highest point of its flight, what are its velocity and acceleration?",
          r"velocity zero; acceleration $9.8\ \mathrm{m/s^2}$ downward", [r"velocity zero; acceleration zero", r"velocity zero; acceleration $9.8\ \mathrm{m/s^2}$ upward", r"velocity $9.8$ m/s downward; acceleration zero"],
          r"Gravity acts throughout the flight, so $a = g$ downward even at the instant $v = 0$.",
          [r"The velocity is changing from upward to downward, so it cannot have zero rate of change."],
          [r"if $a$ were zero at the top, the ball would stay there.",
           r"gravity pulls down, so the acceleration points down.",
           r"swaps the two quantities."]),
        Q("1.1 Average speed", r"A car travels $60$ km east at $60$ km/h, then another $60$ km east at $30$ km/h. What is its average speed for the whole trip?",
          r"$40$ km/h", [r"$45$ km/h", r"$90$ km/h", r"$20$ km/h"],
          r"Total distance over total time: $120$ km in $1 + 2 = 3$ h, or $40$ km/h.",
          [r"First leg: $60/60 = 1$ h. Second leg: $60/30 = 2$ h.", r"Average speed $= 120/3 = 40$ km/h."],
          [r"averages the two speeds, but the car spends twice as long at $30$ km/h.",
           r"adds the two speeds.",
           r"divides one leg's distance by the total time."], sort=True),
    ]),
    Set("A velocity--time graph (1.3)", [
        Q("1.3 Slope of v-t", r"What is the cart's acceleration at $t = 1$ s?",
          r"$3.0\ \mathrm{m/s^2}$", [r"$6.0\ \mathrm{m/s^2}$", r"$1.5\ \mathrm{m/s^2}$", r"$0$"],
          r"Acceleration is the slope: the velocity rises $6$ m/s in $2$ s, so $a = 3.0\ \mathrm{m/s^2}$.",
          [r"Slope from $t = 0$ to $2$ s: $(6 - 0)/(2 - 0) = 3.0\ \mathrm{m/s^2}$."],
          [r"reads the velocity at $t = 2$ s rather than the slope.",
           r"is the area under the graph from $0$ to $1$ s (a displacement of $1.5$ m), not the slope.",
           r"would need a flat graph; the velocity is changing at $t = 1$ s."], sort=True),
        Q("1.3 Area under v-t", r"How far is the cart from its starting point at $t = 8$ s?",
          r"$36$ m", [r"$48$ m", r"$24$ m", r"$0$"],
          r"Displacement is the area under the graph from $0$ to $8$ s: $6 + 24 + 6 = 36$ m.",
          [r"$0$--$2$ s: $\tfrac12(2)(6) = 6$ m. $2$--$6$ s: $4 \times 6 = 24$ m. $6$--$8$ s: $\tfrac12(2)(6) = 6$ m."],
          [r"assumes $6$ m/s for all $8$ s.",
           r"counts only the constant-velocity rectangle.",
           r"confuses $v = 0$ at $t = 8$ s with being back at the start."], sort=True),
        Q("1.3 Turning point", r"At what time is the cart farthest from its starting point in the positive direction?",
          r"$t = 8$ s", [r"$t = 2$ s", r"$t = 6$ s", r"$t = 10$ s"],
          r"The cart moves in the $+$ direction while $v > 0$ (until $t = 8$ s) and back toward the start after that.",
          [r"Position keeps increasing as long as $v > 0$; it peaks where $v$ changes sign."],
          [r"is when the cart reaches its top speed; it is still moving forward.",
           r"is when the cart begins to slow; it is still moving forward.",
           r"by then it has moved $4$ m back toward the start."], sort=True),
        Q("1.3 Reading the motion", r"Which describes the cart's motion between $t = 8$ s and $t = 10$ s?",
          r"moving in the negative direction and speeding up", [r"moving in the positive direction and slowing down", r"moving in the negative direction and slowing down", r"at rest"],
          r"$v$ is negative and growing in size; $v$ and $a$ are both negative, so the cart speeds up.",
          [r"Below the axis: negative velocity. Moving away from the axis: speed increasing."],
          [r"describes $6$--$8$ s.",
           r"would need the graph to move back toward the axis.",
           r"only at the instant $t = 8$ s is $v = 0$."]),
        Q("1.3 Average velocity", r"What is the cart's average velocity from $t = 0$ to $t = 10$ s?",
          r"$3.2$ m/s", [r"$4.0$ m/s", r"$3.6$ m/s", r"$-2.0$ m/s"],
          r"Net displacement is $36 - 4 = 32$ m in $10$ s.",
          [r"Area above the axis ($0$--$8$ s): $36$ m. Area below ($8$--$10$ s): $\tfrac12(2)(4) = 4$ m, negative.", r"$\bar v = 32/10 = 3.2$ m/s."],
          [r"adds the area below the axis instead of subtracting it.",
           r"leaves out the last $2$ s of motion but still divides by $10$ s.",
           r"averages the first and last velocities, which works only for constant acceleration."], sort=True),
    ], stim=r"The graph shows the velocity $v$ of a cart moving along a straight track, with the positive direction to the right. Use it for the next five questions.",
        fig=CART, stim_title="Questions 5--9"),
    Set("Relative motion (1.4)", [
        Q("1.4 Rain and a moving car", r"Rain falls vertically at $8.0$ m/s relative to the ground. A car drives along a level road at $6.0$ m/s. What is the speed of the rain relative to the driver?",
          r"$10$ m/s", [r"$14$ m/s", r"$2.0$ m/s", r"$8.0$ m/s"],
          r"Relative to the car the rain has the $8.0$ m/s downward and $6.0$ m/s backward: $\sqrt{8.0^2 + 6.0^2} = 10$ m/s.",
          [r"$\vec v_{\text{rain rel car}} = \vec v_{\text{rain}} - \vec v_{\text{car}}$, perpendicular components."],
          [r"adds the speeds as if they were in one line.",
           r"subtracts them as if they were in one line.",
           r"is the speed relative to the ground."], sort=True),
        Q("1.4 Ball tossed on a moving cart", r"A student riding a cart that moves at constant velocity tosses a ball straight up (relative to the cart) and catches it. Air resistance is negligible. To an observer standing on the ground, the ball",
          r"follows a parabola and lands back in the student's hand", [r"moves straight up and down and lands behind the student", r"follows a parabola and lands behind the student", r"moves straight up and down and lands in the student's hand"],
          r"The ball shares the cart's horizontal velocity and keeps it, so it stays above the student while rising and falling.",
          [r"Ground frame: horizontal velocity $=$ cart's velocity, plus vertical free fall: a parabola."],
          [r"to the ground observer the ball also moves sideways with the cart.",
           r"would happen only if the ball lost its horizontal velocity, which no horizontal force removes.",
           r"is the path seen by the student, not by the ground observer."]),
    ]),
    Set("Projectile motion (1.5)", [
        Q("1.5 Independence of motions", r"Ball $A$ is dropped from the edge of a table at the same instant that ball $B$ is launched horizontally from the same edge at $3$ m/s. Air resistance is negligible. Which reaches the floor first?",
          r"They reach the floor at the same time.", [r"$A$", r"$B$", r"It depends on which ball has more mass."],
          r"Both start with zero vertical velocity and fall the same height with the same acceleration.",
          [r"Fall time depends only on the vertical motion: $h = \tfrac12 g t^2$ for both."],
          [r"the horizontal velocity of $B$ does not slow its fall.",
           r"$B$'s path is longer, but its horizontal motion does not speed up its fall either.",
           r"every object falls with acceleration $g$ when air resistance is negligible."]),
        Q("1.5 Time of flight", r"A projectile is launched over level ground at $25$ m/s at $53^\circ$ above the horizontal ($\sin 53^\circ = 0.80$, $\cos 53^\circ = 0.60$). How long is it in the air?",
          r"$4.1$ s", [r"$2.0$ s", r"$3.1$ s", r"$5.1$ s"],
          r"$v_{y0} = 25(0.80) = 20$ m/s; it returns to launch height after $2v_{y0}/g = 40/9.8 = 4.1$ s.",
          [r"Time to the top: $20/9.8 = 2.04$ s.", r"Level ground: the fall takes as long as the rise, so $t = 4.1$ s."],
          [r"is the time to the highest point only.",
           r"uses the horizontal component $15$ m/s in place of the vertical one.",
           r"uses the full launch speed in place of its vertical component."], sort=True),
        Q("1.5 Range", r"For the projectile in the previous question, what is its horizontal range?",
          r"$61$ m", [r"$82$ m", r"$31$ m", r"$102$ m"],
          r"Range $=$ horizontal velocity $\times$ time of flight $= 15 \times 4.08 = 61$ m.",
          [r"$v_x = 25(0.60) = 15$ m/s, constant.", r"$x = 15(4.08) = 61$ m."],
          [r"uses the vertical component $20$ m/s as the horizontal velocity.",
           r"uses only the time to the top.",
           r"uses the full launch speed for the horizontal velocity."], sort=True),
    ]),
]

UNIT = Unit(1, "kinematics", "Kinematics", "10--15\\%", "1.1--1.5",
    abstract=r"""Unit 1 describes motion without asking what causes it: scalars and vectors in one dimension; displacement, velocity and acceleration and the constant-acceleration equations; the three ways the exam represents motion (graphs, equations and motion diagrams); relative motion between reference frames; and projectile motion in two dimensions. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Translation Between Representations", 12, r"""A student stands at the edge of a flat roof a height $H$ above level ground and throws a ball straight up with speed $v_0$. The ball rises, falls back past the edge of the roof, and lands on the ground below. Air resistance is negligible. Take upward as positive.""", [
        Part("a", 3, r"On axes of velocity $v$ versus time $t$, sketch the ball's velocity from the moment it leaves the student's hand until just before it hits the ground. Label the time $t_1$ when the ball is at its highest point and the time $t_2$ when it passes the level of the roof on the way down.",
             r"1 pt: a single straight line with negative slope $-g$ throughout, starting at $+v_0$. 1 pt: the line crosses $v = 0$ at $t_1 = v_0/g$. 1 pt: at $t_2 = 2t_1$ the velocity is $-v_0$, and the line continues below $-v_0$ until landing.",
             r"A V-shaped graph (speed, not velocity), or a change of slope at the top."),
        Part("b", 3, r"Derive an expression for the maximum height of the ball above the ground, in terms of $v_0$, $H$ and physical constants as appropriate.",
             r"1 pt: $v^2 = v_0^2 + 2a(y - y_0)$ with $a = -g$ and $y_0 = H$. 1 pt: $v = 0$ at the highest point. 1 pt: $y_{max} = H + \dfrac{v_0^2}{2g}$.",
             r"Leaving out $H$ (finding the height above the roof only)."),
        Part("c", 3, r"Derive an expression for the speed of the ball just before it hits the ground, in terms of $v_0$, $H$ and physical constants as appropriate.",
             r"1 pt: $v^2 = v_0^2 + 2a\Delta y$ with $\Delta y = -H$ (or the fall from $y_{max}$). 1 pt: correct substitution, $v^2 = v_0^2 + 2gH$. 1 pt: $v = \sqrt{v_0^2 + 2gH}$.",
             r"Using $\Delta y = +H$, which gives $\sqrt{v_0^2 - 2gH}$."),
        Part("d", 3, r"The student now throws an identical ball straight \emph{down} from the same roof with the same speed $v_0$. A classmate claims this ball hits the ground with a greater speed than the first ball. Do you agree or disagree with the classmate? Justify your answer using your graph from part (a) or your expression from part (c).",
             r"1 pt: disagree; both balls hit the ground with the same speed. 1 pt: graph: the line has constant slope, so at $t_2$ the first ball is back at roof level moving downward at $v_0$, exactly like the second ball at release; from there the two motions are identical. 1 pt: expression: $v = \sqrt{v_0^2 + 2gH}$ depends only on $v_0^2$, not on the direction of the throw.",
             r"Agreeing because the downward throw ``starts with a head start''; or a claim with no link to (a) or (c)."),
    ], mins=28),
    frq_topic="a ball thrown upward from a roof",
)
