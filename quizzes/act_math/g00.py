"""ACT Math Guide 0: Overview & Strategy (10 items)."""
import math

from act_math.quiz import Q

DOC = dict(
    slug="0", pdf="act-math-00-overview.pdf", title="Guide 0: Overview &amp; Strategy", h1='Overview <span style="white-space:nowrap">&amp; Strategy</span>',
    sub="ACT Math &middot; Guide 0", metaline="10 four-choice strategy drills &middot; target 11 min",
    desc="ACT Math Guide 0 (Overview & Strategy): 10 drill items on backsolving, picking numbers, the calculator, estimating and guessing, each with a worked explanation.",
    setup="Work the drills with the strategy each rule teaches; the target time is 11 minutes.",
    rules={"2.1": ("Plug the answers into the question", 2), "3.1": ("Replace variables or percents with easy numbers", 3),
           "4.1": ("Graph it, then read the answer", 3), "5.1": ("Round first, compute only if necessary", 4), "6.1": ("Expected value of a guess", 4)},
    sections={1: "Backsolving", 2: "Picking numbers", 3: "The calculator", 4: "Estimate and eliminate", 5: "Guessing and pacing"},
    key="1 C 2 D 3 A 4 B 5 A 6 D 7 B 8 C 9 C 10 B",
)

assert 44 + 46 + 48 == 138
assert 3 * 6.5 - 8 == 6.5 + 5
assert all((x * x + x) % 2 == 0 and (3 * x + 2) % 2 == 1 for x in (1, 3, 5, 7))
assert math.isclose(100 * 1.5 * 0.5, 75)
assert math.isclose(0.40 * 0.25, 0.10)
f = lambda x: x ** 3 - 3 * x + 1
assert sum(1 for a, b in [(-2, -1), (0, 1), (1, 2)] if f(a) * f(b) < 0) == 3
lo, hi = 2.0, 3.0  # bisection for 2^x = x + 3 on [2, 3]
for _ in range(60):
    mid = (lo + hi) / 2
    if 2 ** mid - (mid + 3) < 0:
        lo = mid
    else:
        hi = mid
assert round(lo, 1) == 2.4
assert round(19.8 * 0.51 / 4.03, 1) == 2.5
assert 12 / 4 == 3 and (50 - 5) * 60 / 45 == 60 and 50 * 60 / 45 > 66

QS = [
    Q(1, "2.1", "The sum of three consecutive even integers is 138. What is the largest of the three integers?", ["44", "46", "48", "50"], "C",
      "Backsolving: when the choices are numbers, test them in the problem. Start in the middle so one test eliminates about half the choices.",
      ["Test C: largest 48, so the integers are 44, 46, 48. Sum: 138. Done.", "Directly: $x + (x + 2) + (x + 4) = 138 \\Rightarrow x = 44$; the largest is 48."],
      {"A": "is the smallest of the three, not the largest.",
       "B": "is the middle one.",
       "D": "check: $46 + 48 + 50 = 144$."}, sec=1),
    Q(2, "2.1", "A number is tripled and then decreased by 8. The result is 5 more than the original number. What is the original number?", ["3", "4.5", "5", "6.5"], "D",
      "Translate the words into an equation, or backsolve by testing the choices.",
      ["$3n - 8 = n + 5 \\Rightarrow 2n = 13 \\Rightarrow n = 6.5$.", "Check: $3(6.5) - 8 = 11.5 = 6.5 + 5$."],
      {"A": "check: $3(3) - 8 = 1$, but $3 + 5 = 8$.",
       "B": "check: $3(4.5) - 8 = 5.5$, but $4.5 + 5 = 9.5$.",
       "C": "check: $3(5) - 8 = 7$, but $5 + 5 = 10$."}, sec=1),
    Q(3, "3.1", "If $x$ is a positive odd integer, which of the following must be even?", ["$x^2 + x$", "$x^2$", "$3x + 2$", "$2x + 1$"], "A",
      "Pick numbers: try an easy odd value in every choice. For &ldquo;must be&rdquo; questions, one counterexample eliminates a choice.",
      ["Let $x = 3$: $x^2 + x = 12$ (even); $x^2 = 9$, $3x + 2 = 11$, $2x + 1 = 7$ (all odd).",
       "In general $x^2 + x = x(x + 1)$, a product of consecutive integers, so it is always even."],
      {"B": "odd times odd is odd.",
       "C": "$3x$ is odd, and odd plus 2 is odd.",
       "D": "$2x$ is even, and even plus 1 is odd."}, sec=2),
    Q(4, "3.1", "A price is increased by 50%, and then the new price is decreased by 50%. The final price is what percent of the original price?", ["50%", "75%", "100%", "125%"], "B",
      "With percents and no starting amount, start at 100.",
      ["$100 \\to 150$ (up 50%) $\\to 75$ (down 50% of 150).", "75 is 75% of 100. (Multipliers: $1.5 \\times 0.5 = 0.75$.)"],
      {"A": "takes 50% off the original instead of off the new price.",
       "C": "assumes the two changes cancel; the 50% decrease is taken from a larger number.",
       "D": "does not follow; the decrease (75) is bigger than the increase (50)."}, sec=2),
    Q(5, "3.1", "If $a$ is 40% of $b$, and $b$ is 25% of $c$, then $a$ is what percent of $c$?", ["10%", "15%", "65%", "160%"], "A",
      "Pick an easy value for $c$ and follow the chain, or multiply the percents as decimals.",
      ["Let $c = 100$: $b = 25$, $a = 0.40 \\times 25 = 10$.", "$a$ is 10% of $c$ ($0.40 \\times 0.25 = 0.10$)."],
      {"B": "subtracts the percents.",
       "C": "adds the percents.",
       "D": "divides 40 by 25 instead of multiplying."}, sec=2),
    Q(6, "4.1", "How many real solutions does $x^3 - 3x + 1 = 0$ have?", ["0", "1", "2", "3"], "D",
      "Graph $y = f(x)$ and count the $x$-intercepts. (A cubic always has at least one.)",
      ["$f(-2) = -1$, $f(-1) = 3$, $f(0) = 1$, $f(1) = -1$, $f(2) = 3$.", "The sign changes three times, so the graph crosses the $x$-axis three times."],
      {"A": "is impossible for a cubic: its ends go in opposite directions, so it must cross at least once.",
       "B": "misses two crossings; a window that is too small can hide them.",
       "C": "would need a tangent (touching) zero; this graph crosses three times."}, sec=3),
    Q(7, "4.1", "For $x > 0$, the graphs of $y = 2^x$ and $y = x + 3$ intersect at one point. To the nearest tenth, what is the $x$-coordinate of that point?", ["1.4", "2.4", "3.0", "4.4"], "B",
      "Solve $f(x) = g(x)$ by graphing both and finding the intersection.",
      ["At $x = 2$: $2^2 = 4 < 5$. At $x = 3$: $2^3 = 8 > 6$. The crossing is between 2 and 3.",
       "The calculator's intersect feature gives $x \\approx 2.44$, so 2.4."],
      {"A": "check: $2^{1.4} \\approx 2.6$, but $1.4 + 3 = 4.4$.",
       "C": "check: $2^3 = 8$, but $3 + 3 = 6$; the curves have already crossed.",
       "D": "check: $2^{4.4} \\approx 21$, far above $4.4 + 3$."}, sec=3),
    Q(8, "5.1", "Which of the following is closest to $\\dfrac{(19.8)(0.51)}{4.03}$?", ["0.25", "1.25", "2.5", "25"], "C",
      "Round every number to something easy; choices spaced this far apart only need an estimate.",
      ["$\\dfrac{(20)(0.5)}{4} = \\dfrac{10}{4} = 2.5$."],
      {"A": "is off by a factor of 10.",
       "B": "is half the estimate.",
       "D": "is off by a factor of 10."}, sec=4),
    Q(9, "6.1", "A student runs out of time and guesses randomly on the last 12 questions. What is the expected number of those 12 that the student answers correctly?", ["2", "2.4", "3", "4"], "C",
      "With 4 choices, each blind guess is right with probability $\\tfrac14$; expected correct $= n \\cdot \\tfrac14$.",
      ["$12 \\times \\tfrac14 = 3$."],
      {"A": "uses $\\tfrac16$ per guess.",
       "B": "uses $\\tfrac15$ per guess, the old 5-choice format.",
       "D": "uses $\\tfrac13$ per guess, as if one choice had been eliminated on each."}, sec=5),
    Q(10, "6.1", "A student plans to save the last 5 minutes of the 50-minute section for review. To finish all 45 questions in the remaining time, what is the average number of seconds the student can spend per question?", ["54", "60", "66.7", "72"], "B",
      "Convert the available time to seconds and divide by the number of questions.",
      ["Remaining time: $45$ minutes $= 2700$ seconds.", "$2700 \\div 45 = 60$ seconds per question."],
      {"A": "takes off more time than the 5 minutes planned.",
       "C": "uses all 50 minutes, ignoring the 5 minutes saved for review.",
       "D": "does not follow; 45 minutes over 45 questions is 1 minute each."}, sec=5),
]
