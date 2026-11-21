"""ACT Math Guide 8: Full-Length Practice Test (45 items)."""
import math
from fractions import Fraction as F

from act_math.quiz import Q

G = "/study/act/math/"
DOC = dict(
    slug="practice-test", pdf="act-math-08-practice-test.pdf", title="Guide 8: Full-Length Practice Test", h1='Full-Length <span style="white-space:nowrap">Practice Test</span>',
    sub="ACT Math &middot; Guide 8", metaline="45 questions &middot; 50 minutes &middot; calculator allowed",
    desc="ACT Math full-length practice test: 45 questions to the enhanced-ACT blueprint, with a worked explanation for every answer and a score by category.",
    setup="Set a 50-minute timer and use Exam mode for a real simulation. Answer every question: there is no penalty for wrong answers.",
    rules={"1": ("Number &amp; Quantity", 1, G + "act-math-01-number-quantity.pdf"), "2": ("Algebra", 1, G + "act-math-02-algebra.pdf"),
           "3": ("Functions", 1, G + "act-math-03-functions.pdf"), "4": ("Geometry", 1, G + "act-math-04-geometry.pdf"),
           "5": ("Statistics &amp; Probability", 1, G + "act-math-05-statistics-probability.pdf"),
           "6": ("Integrating Essential Skills", 1, G + "act-math-06-essential-skills.pdf")},
    guide=G + "act-math-00-overview.pdf", guideName="its study guide",
    topicPrefix="Guide ", topicCol="Review", guideCol="Category", byTopic="By category",
    flag={"below": 0.7, "text": "below 70%: review this guide"},
    topicNote="Any category below 70% correct is your next study priority: reread its guide, then redo the items you missed. ACT converts raw scores to the 1&ndash;36 scale with a different table for each form, so treat the raw score as a diagnostic.",
    foot=(f'From <a href="{G}act-math-08-practice-test.pdf"><i>ACT Math Guide 8: Full-Length Practice Test</i></a> (PDF). Answers and category tags are the test&rsquo;s own key (items marked +Modeling also count toward Modeling); the explanations add the method, the worked solution, and why each wrong choice is wrong. Category links open that category&rsquo;s guide. Your answers are saved only in this browser.'),
    key=("1 D 2 B 3 C 4 B 5 D 6 C 7 D 8 A 9 A 10 C 11 A 12 C 13 D 14 A 15 B 16 D 17 A 18 B 19 D 20 A 21 C 22 C 23 A 24 D 25 B "
         "26 D 27 B 28 B 29 A 30 A 31 D 32 C 33 A 34 B 35 C 36 B 37 C 38 D 39 D 40 A 41 A 42 C 43 B 44 B 45 D"),
)

assert 24 * 0.75 == 18 and (9 + 7) / 2 == 8 and abs(3 - 11) + (-2) ** 3 == 0
assert sorted([14, 9, 25, 9, 17])[2] == 14 and sum([14, 9, 25, 9, 17]) / 5 == 14.8
assert (-3) ** 2 - 5 * (-3) == 24 and 330 / (210 / 7) == 11 and 4 * 36 == 144
assert all(3 * (2 * x - 4) - 2 * (x - 5) == 4 * x - 2 for x in range(5))
assert F(9, 15) == F(3, 5) and (46 - 2 * 15) // 2 * 15 == 120
g13, h13 = (lambda x: 2 * x - 1), (lambda x: x * x + 3)
assert h13(g13(3)) == 28 and g13(h13(3)) == 23 and -3 * -1 + 1 == 4
assert math.hypot(6, 8) == 10 and math.isclose(12.6 / 3 * 50, 210)
assert (2 - 3j) ** 2 == -5 - 12j
assert 3 * 3 + 2 * 3 + 1 == 16 and 3 + 7 == 10 and 6 * 15 - 5 * 14 == 20
assert min(x * x + 8 * x + 10 for x in range(-10, 10)) == -6 and 6 / 4 * 18 == 27
assert round(5000 * 1.08 ** 2) == 5832 and 5000 * 1.16 == 5800
assert all(3 * x * x - 12 == 3 * (x - 2) * (x + 2) for x in range(5))
assert math.isclose(math.sqrt(3) / 4 * 36, 9 * math.sqrt(3)) and 7 * 6 == 42 and math.comb(7, 2) == 21
assert 2 * -2 + 1 == -3 and math.floor((60 - 12 * 3.5) / 1.25) == 14 and 60 / 1.25 == 48
assert 2 * 3 ** 4 == 162 and F(8, 17) ** 2 + F(15, 17) ** 2 == 1
assert 25 * 10 * 2 * 1000 / 500 == 1000 and F(54, 90) == F(3, 5) and F(54, 150) == F(9, 25)
assert all(math.isclose(r * r - 6 * r + 4, 0, abs_tol=1e-9) for r in (3 + math.sqrt(5), 3 - math.sqrt(5)))
assert math.log2(4) + math.log2(2) == 3
assert (1 + 2) ** 2 + (1 - 5) ** 2 == 25
assert (1000 + 2 * 250) / 500 - 5 == -2
assert 150 + 11 * 25 == 425 and 12 * (150 + 425) / 2 == 3450 and 12 * 425 == 5100
assert math.isclose(math.pi * 9 * 6 * 2 / 3, 36 * math.pi)
assert math.isqrt(100 - 36) == 8
assert math.isclose(10 * math.sin(math.radians(45)) / math.sin(math.radians(30)), 10 * math.sqrt(2))
assert 12 ** 2 / 2 == 72
assert 1.06 ** 11 < 2 <= 1.06 ** 12
p45 = lambda x: x ** 3 - 4 * x * x + x + 6
assert p45(2) == 0 and p45(3) == 0 and p45(-1) == 0

QS = [
    Q(1, "6", "A shirt that normally costs \\$24 is on sale for 25% off. What is the sale price?", ["\\$6", "\\$12", "\\$16", "\\$18"], "D",
      "A 25% discount leaves 75% of the price: multiply by 0.75.", ["$24 \\times 0.75 = \\$18$."],
      {"A": "is the discount (25% of \\$24), not the sale price.", "B": "is 50% off.", "C": "takes off a third instead of a quarter."}, tag="IES &middot; Percents"),
    Q(2, "2", "If $5x - 7 = 3x + 9$, what is the value of $x$?", ["1", "8", "12", "16"], "B",
      "Collect $x$-terms on one side and constants on the other.", ["$2x = 16 \\Rightarrow x = 8$."],
      {"A": "combines the constants incorrectly ($9 - 7 = 2$ instead of $9 + 7 = 16$).", "C": "check: $5(12) - 7 = 53$ but $3(12) + 9 = 45$.", "D": "stops at $2x = 16$."}, tag="ALG &middot; Linear equations"),
    Q(3, "1", "What is the value of $|3 - 11| + (-2)^3$?", ["$-16$", "$-8$", "0", "16"], "C",
      "Evaluate inside the absolute value first; an odd power of a negative is negative.", ["$|3 - 11| = |-8| = 8$ and $(-2)^3 = -8$.", "$8 + (-8) = 0$."],
      {"A": "treats $|-8|$ as $-8$.", "B": "drops the absolute-value term.", "D": "treats $(-2)^3$ as $+8$."}, tag="N&amp;Q &middot; Absolute value, exponents"),
    Q(4, "5", "What is the median of the data set $\\{14, 9, 25, 9, 17\\}$?", ["9", "14", "14.8", "16"], "B",
      "Sort first; the median is the middle value.", ["Sorted: 9, 9, 14, 17, 25. Median: 14."],
      {"A": "is the mode.", "C": "is the mean.", "D": "does not come from the sorted list."}, tag="S&amp;P &middot; Median"),
    Q(5, "3", "If $f(x) = x^2 - 5x$, what is $f(-3)$?", ["$-24$", "$-6$", "6", "24"], "D",
      "Substitute with parentheses: $(-3)^2 = 9$ and $-5(-3) = +15$.", ["$f(-3) = 9 + 15 = 24$."],
      {"A": "gets both signs wrong.", "B": "treats $-5(-3)$ as $-15$: $9 - 15$.", "C": "treats $(-3)^2$ as $-9$: $-9 + 15$."}, tag="FUN &middot; Evaluation"),
    Q(6, "6", "A car travels 210 miles on 7 gallons of gas. At this rate, how many gallons does it need to travel 330 miles?", ["9", "10", "11", "12"], "C",
      "Find the unit rate, then scale.", ["$210 \\div 7 = 30$ miles per gallon.", "$330 \\div 30 = 11$ gallons."],
      {"A": "check: 9 gallons go 270 miles.", "B": "check: 10 gallons go 300 miles.", "D": "check: 12 gallons go 360 miles."}, tag="IES &middot; Unit rates (+Modeling)"),
    Q(7, "4", "Two angles are supplementary. The measure of one is 4 times the measure of the other. What is the measure of the larger angle?", ["$36^\\circ$", "$72^\\circ$", "$135^\\circ$", "$144^\\circ$"], "D",
      "Supplementary angles sum to $180^\\circ$.", ["$x + 4x = 180 \\Rightarrow x = 36$.", "Larger: $4 \\times 36 = 144^\\circ$."],
      {"A": "is the smaller angle.", "B": "uses complementary angles ($x + 4x = 90$).", "C": "does not split 180 in a 1 : 4 ratio."}, tag="GEO &middot; Angle relationships"),
    Q(8, "2", "Which expression is equivalent to $3(2x - 4) - 2(x - 5)$?", ["$4x - 2$", "$4x + 2$", "$4x - 22$", "$8x - 2$"], "A",
      "Distribute carefully, including the negative sign: $-2(x - 5) = -2x + 10$.", ["$6x - 12 - 2x + 10 = 4x - 2$."],
      {"B": "gets the constant's sign wrong; $-12 + 10 = -2$.", "C": "distributes $-2$ as $-2x - 10$.", "D": "adds $2x$ instead of subtracting it."}, tag="ALG &middot; Expressions"),
    Q(9, "1", "For $x > 0$, which expression is equivalent to $x^{3/2}$?", ["$\\sqrt{x^3}$", "$\\sqrt[3]{x^2}$", "$\\dfrac{3x}{2}$", "$x^3 - x^2$"], "A",
      "$a^{m/n} = \\sqrt[n]{a^m}$: the denominator is the root, the numerator is the power.", ["$x^{3/2} = \\sqrt{x^3}$."],
      {"B": "swaps the root and the power (that is $x^{2/3}$).", "C": "treats the exponent as a multiplier.", "D": "has no connection to fractional exponents."}, tag="N&amp;Q &middot; Rational exponents"),
    Q(10, "5", "A bag holds 4 red, 6 green, and 5 blue marbles. One marble is drawn at random. What is the probability that it is NOT green?", ["$\\dfrac25$", "$\\dfrac12$", "$\\dfrac35$", "$\\dfrac23$"], "C",
      "$P(\\text{not } A) = 1 - P(A)$, or count the favorable outcomes directly.", ["Not green: $4 + 5 = 9$ of 15. $\\dfrac{9}{15} = \\dfrac35$."],
      {"A": "is $P(\\text{green}) = \\tfrac{6}{15}$.", "B": "does not follow from 9 of 15.", "D": "is $P(\\text{not blue}) = \\tfrac{10}{15}$."}, tag="S&amp;P &middot; Probability"),
    Q(11, "6", "A gym charges a one-time \\$40 sign-up fee plus \\$25 per month. Which expression gives the total cost, in dollars, of a membership for $m$ months?", ["$25m + 40$", "$40m + 25$", "$65m$", "$25(m + 40)$"], "A",
      "A per-month charge multiplies the number of months; a one-time fee is added once.", ["$25m + 40$."],
      {"B": "charges the sign-up fee every month.", "C": "charges both amounts every month.", "D": "multiplies the fee by 25."}, tag="IES &middot; Expressions in context (+Modeling)"),
    Q(12, "6", "A rectangle has a perimeter of 46 cm and a length of 15 cm. What is its area, in square centimeters?", ["31", "64", "120", "690"], "C",
      "Use the perimeter to find the width, then multiply length by width.", ["$2(15 + w) = 46 \\Rightarrow w = 8$.", "Area $= 15 \\times 8 = 120$."],
      {"A": "subtracts the length from the perimeter.", "B": "does not follow; the width is 8.", "D": "multiplies the perimeter by the length."}, tag="IES &middot; Perimeter &amp; area"),
    Q(13, "3", "If $g(x) = 2x - 1$ and $h(x) = x^2 + 3$, what is $h(g(3))$?", ["12", "19", "23", "28"], "D",
      "Work inside out.", ["$g(3) = 5$; $h(5) = 25 + 3 = 28$."],
      {"A": "is $h(3)$.", "B": "does not follow; $g(3) = 5$ and $h(5) = 28$.", "C": "is $g(h(3)) = g(12)$, the composition in the other order."}, tag="FUN &middot; Composition"),
    Q(14, "2", "Which is an equation of the line that passes through $(-1, 4)$ and has slope $-3$?", ["$y = -3x + 1$", "$y = -3x + 7$", "$y = -3x - 1$", "$y = 3x + 7$"], "A",
      "Point-slope form: $y - y_1 = m(x - x_1)$.", ["$y - 4 = -3(x + 1) \\Rightarrow y = -3x + 1$.", "Check: $-3(-1) + 1 = 4$."],
      {"B": "uses $x - 1$ instead of $x + 1$; check: $-3(-1) + 7 = 10 \\ne 4$.", "C": "check: $-3(-1) - 1 = 2 \\ne 4$.", "D": "has the wrong slope."}, tag="ALG &middot; Lines"),
    Q(15, "4", "What is the distance between the points $(1, 2)$ and $(7, 10)$?", ["8", "10", "14", "100"], "B",
      "$d = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2}$.", ["$\\sqrt{6^2 + 8^2} = \\sqrt{100} = 10$."],
      {"A": "is $\\Delta y$ alone.", "C": "adds $\\Delta x + \\Delta y$.", "D": "forgets the square root."}, tag="GEO &middot; Distance formula"),
    Q(16, "6", "On a map, 3 centimeters represent 50 kilometers. Two cities are 12.6 centimeters apart on the map. What is the actual distance between them, in kilometers?", ["150", "180", "189", "210"], "D",
      "Set up a proportion, or count how many 3-cm units fit.", ["$12.6 \\div 3 = 4.2$ units of 50 km.", "$4.2 \\times 50 = 210$ km."],
      {"A": "is 3 units (9 cm).", "B": "does not follow; $4.2 \\times 50 = 210$.", "C": "uses 15 km per cm; the scale is $50/3 \\approx 16.7$ km per cm."}, tag="IES &middot; Proportions (+Modeling)"),
    Q(17, "1", "Which of the following equals $(2 - 3i)^2$, where $i = \\sqrt{-1}$?", ["$-5 - 12i$", "$-5 + 12i$", "$13 - 12i$", "$4 - 9i$"], "A",
      "Square the binomial, then use $i^2 = -1$.", ["$(2 - 3i)^2 = 4 - 12i + 9i^2 = 4 - 12i - 9 = -5 - 12i$."],
      {"B": "gets the sign of the middle term wrong.", "C": "treats $i^2$ as $+1$.", "D": "squares each term separately, treating $(3i)^2$ as $9i$, and skips the middle term."}, tag="N&amp;Q &middot; Complex numbers"),
    Q(18, "2", "If $y = 2x + 1$ and $3x + y = 16$, what is the value of $x + y$?", ["7", "10", "13", "19"], "B",
      "Substitute the first equation into the second.", ["$3x + 2x + 1 = 16 \\Rightarrow x = 3$, so $y = 7$.", "$x + y = 10$."],
      {"A": "is $y$ alone.", "C": "does not follow; $x = 3$ and $y = 7$.", "D": "does not follow; $x = 3$ and $y = 7$."}, tag="ALG &middot; Systems"),
    Q(19, "5", "The average of 6 numbers is 15. When one number is removed, the average of the remaining 5 numbers is 14. What number was removed?", ["1", "14.5", "15", "20"], "D",
      "Work with sums: sum $=$ mean $\\times$ count.", ["Original sum: $6 \\times 15 = 90$. New sum: $5 \\times 14 = 70$.", "Removed: $90 - 70 = 20$."],
      {"A": "subtracts the averages.", "B": "averages the averages.", "C": "assumes the removed number equals the old mean."}, tag="S&amp;P &middot; Mean"),
    Q(20, "3", "What is the minimum value of $f(x) = x^2 + 8x + 10$?", ["$-6$", "$-4$", "4", "10"], "A",
      "Complete the square, or find the vertex at $x = -\\dfrac{b}{2a}$.", ["$x^2 + 8x + 10 = (x + 4)^2 - 6$.", "Minimum $-6$, at $x = -4$."],
      {"B": "is the $x$-value where the minimum occurs, not the minimum.", "C": "does not follow; $f(-4) = 16 - 32 + 10 = -6$.", "D": "is $f(0)$."}, tag="FUN &middot; Quadratic extrema"),
    Q(21, "6", "At the same time of day, a 6-foot-tall person casts a 4-foot shadow and a tree casts an 18-foot shadow. How tall is the tree, in feet?", ["12", "24", "27", "36"], "C",
      "Same time of day means similar triangles: height and shadow are proportional.", ["$\\dfrac64 = \\dfrac{h}{18} \\Rightarrow h = 27$ ft."],
      {"A": "inverts the ratio: $18 \\times \\tfrac46$.", "B": "check: $\\tfrac{24}{18} \\ne \\tfrac64$.", "D": "doubles the shadow instead of multiplying by 1.5."}, tag="IES &middot; Proportions (+Modeling)"),
    Q(22, "6", "A town&rsquo;s population of 5,000 increases by 8% each year. What will the population be after 2 years?", ["5,400", "5,800", "5,832", "10,800"], "C",
      "Percent growth compounds: multiply by 1.08 each year.", ["$5000(1.08)^2 = 5000(1.1664) = 5832$."],
      {"A": "is after 1 year.", "B": "adds 8% of the original twice (simple growth).", "D": "does not follow from 8% growth."}, tag="IES &middot; Percent growth (+Modeling)"),
    Q(23, "2", "Which of the following is the complete factorization of $3x^2 - 12$?", ["$3(x - 2)(x + 2)$", "$3(x - 2)^2$", "$3(x - 4)(x + 4)$", "$(3x - 4)(x + 3)$"], "A",
      "Take out the GCF first, then factor the difference of squares.", ["$3(x^2 - 4) = 3(x - 2)(x + 2)$."],
      {"B": "expands to $3x^2 - 12x + 12$.", "C": "expands to $3x^2 - 48$.", "D": "expands to $3x^2 + 5x - 12$."}, tag="ALG &middot; Factoring"),
    Q(24, "3", "What is the domain of $f(x) = \\dfrac{1}{x^2 - 9}$?", ["All real $x \\ne 3$", "All real $x > 3$", "All real $x \\ne 9$", "All real $x$ except $-3$ and $3$"], "D",
      "Exclude every input that makes the denominator 0.", ["$x^2 - 9 = 0$ at $x = \\pm 3$."],
      {"A": "misses $x = -3$.", "B": "treats it like a square root; negative inputs such as $x = 0$ work.", "C": "excludes the value of $x^2$ (9) instead of the values of $x$."}, tag="FUN &middot; Domain"),
    Q(25, "4", "What is the area of an equilateral triangle with side length 6?", ["9", "$9\\sqrt3$", "18", "$18\\sqrt3$"], "B",
      "Equilateral triangle: area $= \\dfrac{\\sqrt3}{4}s^2$ (the height is $\\tfrac{\\sqrt3}{2}s$).", ["$\\dfrac{\\sqrt3}{4}(36) = 9\\sqrt3$."],
      {"A": "drops the $\\sqrt3$.", "C": "uses $\\tfrac12 \\cdot 6 \\cdot 6$, taking the side as the height.", "D": "forgets the $\\tfrac12$ in the triangle area."}, tag="GEO &middot; Area"),
    Q(26, "5", "A club of 7 members will choose a president and a vice president. Two different members must fill these roles. How many different outcomes are possible?", ["13", "14", "21", "42"], "D",
      "Different roles mean order matters: $7 \\times 6$.", ["$7 \\times 6 = 42$."],
      {"A": "adds instead of multiplying.", "B": "is $7 \\times 2$.", "C": "counts unordered pairs ($_7C_2$), ignoring who is president."}, tag="S&amp;P &middot; Permutations"),
    Q(27, "1", "Let $A = \\begin{bmatrix} 1 & -2 \\\\ 0 & 3 \\end{bmatrix}$ and $B = \\begin{bmatrix} 4 & 1 \\\\ -1 & 2 \\end{bmatrix}$. What is the entry in row 1, column 2 of $2A + B$?", ["$-4$", "$-3$", "$-1$", "3"], "B",
      "Scalar multiplication and addition work entry by entry.", ["$2(-2) + 1 = -3$."],
      {"A": "is $2A$'s entry alone.", "C": "forgets to double $A$: $-2 + 1$.", "D": "does not follow; $2(-2) + 1 = -3$."}, tag="N&amp;Q &middot; Matrices"),
    Q(28, "6", "Max has at most \\$60 to spend on notebooks costing \\$3.50 each and pens costing \\$1.25 each. If he buys 12 notebooks, what is the greatest number of pens he can buy?", ["12", "14", "15", "48"], "B",
      "Subtract the fixed purchase, divide, and round <i>down</i> to stay within budget.", ["$60 - 12(3.50) = 18$.", "$18 \\div 1.25 = 14.4$: at most 14 pens."],
      {"A": "leaves money unspent; 14 pens still fit.", "C": "rounds up; 15 pens cost \\$18.75, over budget.", "D": "ignores the notebooks."}, tag="IES &middot; Inequalities in context (+Modeling)"),
    Q(29, "3", "If $f(x) = 2 \\cdot 3^x$ and $f(x) = 162$, what is the value of $x$?", ["4", "27", "54", "81"], "A",
      "Isolate the power, then match bases.", ["$3^x = 81 = 3^4$, so $x = 4$."],
      {"B": "does not follow; $3^4 = 81$.", "C": "is $162 \\div 3$.", "D": "is $3^x$, not $x$."}, tag="FUN &middot; Exponential equations"),
    Q(30, "4", "In right triangle $ABC$, angle $C$ is the right angle and $\\tan A = \\dfrac{8}{15}$. What is $\\sin A$?", ["$\\dfrac{8}{17}$", "$\\dfrac{15}{17}$", "$\\dfrac{8}{15}$", "$\\dfrac{17}{8}$"], "A",
      "Sketch the triangle from the given ratio, find the hypotenuse, then take opposite over hypotenuse.", ["Opposite 8, adjacent 15, hypotenuse 17 (8-15-17).", "$\\sin A = \\dfrac{8}{17}$."],
      {"B": "is $\\cos A$.", "C": "is $\\tan A$.", "D": "is the reciprocal of $\\sin A$."}, tag="GEO &middot; Right-triangle trig"),
    Q(31, "6", "A rectangular pool is 25 m long, 10 m wide, and 2 m deep. It is filled at 500 liters per minute ($1\\,\\text{m}^3 = 1{,}000$ L). How many minutes does it take to fill the empty pool?", ["50", "100", "500", "1,000"], "D",
      "Find the volume, convert to liters, then divide by the rate.", ["$25 \\cdot 10 \\cdot 2 = 500\\,\\text{m}^3 = 500{,}000$ L.", "$500{,}000 \\div 500 = 1{,}000$ minutes."],
      {"A": "check: 50 minutes at 500 L/min is 25,000 L, only $25\\,\\text{m}^3$.", "B": "check: 100 minutes is 50,000 L, a tenth of the pool.", "C": "is the pool&rsquo;s volume in cubic meters, not a time."}, tag="IES &middot; Volume &amp; rates (+Modeling)"),
    Q(32, "5", "The table shows survey responses from 150 students. A student who answered &ldquo;Yes&rdquo; is chosen at random. What is the probability that the student is a senior?", ["$\\dfrac{9}{25}$", "$\\dfrac25$", "$\\dfrac35$", "$\\dfrac23$"], "C",
      "&ldquo;Who answered Yes&rdquo; restricts you to the Yes column.", ["Yes: 90 students; seniors among them: 54.", "$\\dfrac{54}{90} = \\dfrac35$."],
      {"A": "uses the grand total, $\\tfrac{54}{150}$.", "B": "is the probability of a junior, $\\tfrac{36}{90}$.", "D": "check: $\\tfrac23$ of the 90 Yes answers would be 60 seniors, not 54."}, tag="S&amp;P &middot; Conditional probability",
      table='<table class="bt"><thead><tr><th scope="col"></th><th scope="col">Yes</th><th scope="col">No</th><th scope="col">Total</th></tr></thead><tbody><tr><th scope="row">Juniors</th><td>36</td><td>24</td><td>60</td></tr><tr><th scope="row">Seniors</th><td>54</td><td>36</td><td>90</td></tr><tr><th scope="row">Total</th><td>90</td><td>60</td><td>150</td></tr></tbody></table>'),
    Q(33, "2", "What are the solutions of $x^2 - 6x + 4 = 0$?", ["$3 \\pm \\sqrt5$", "$3 \\pm \\sqrt{13}$", "$6 \\pm \\sqrt5$", "$-3 \\pm \\sqrt5$"], "A",
      "Quadratic formula: $x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$.", ["$x = \\dfrac{6 \\pm \\sqrt{36 - 16}}{2} = \\dfrac{6 \\pm 2\\sqrt5}{2} = 3 \\pm \\sqrt5$."],
      {"B": "adds $4ac$ instead of subtracting: $\\sqrt{52} = 2\\sqrt{13}$.", "C": "does not divide the 6 by 2.", "D": "uses $b$ instead of $-b$."}, tag="ALG &middot; Quadratic formula"),
    Q(34, "3", "What is the solution set of $\\log_2 x + \\log_2(x - 2) = 3$?", ["$\\{-2\\}$", "$\\{4\\}$", "$\\{-2, 4\\}$", "$\\{6\\}$"], "B",
      "Combine logs with the product rule, rewrite as an exponential, and reject any value that makes a log's argument non-positive.",
      ["$\\log_2[x(x - 2)] = 3 \\Rightarrow x^2 - 2x = 8 \\Rightarrow (x - 4)(x + 2) = 0$.", "Reject $x = -2$ (the argument must be positive): $\\{4\\}$."],
      {"A": "keeps only the extraneous root.", "C": "keeps the extraneous root $-2$.", "D": "check: $\\log_2 6 + \\log_2 4 \\ne 3$."}, tag="FUN &middot; Logarithms"),
    Q(35, "4", "A circle has center $(-2, 5)$ and passes through the point $(1, 1)$. Which is an equation of the circle?",
      ["$(x - 2)^2 + (y + 5)^2 = 25$", "$(x + 2)^2 + (y - 5)^2 = 5$", "$(x + 2)^2 + (y - 5)^2 = 25$", "$(x - 2)^2 + (y + 5)^2 = 5$"], "C",
      "$(x - h)^2 + (y - k)^2 = r^2$; $r$ is the distance from the center to the point.", ["$r^2 = (1 + 2)^2 + (1 - 5)^2 = 9 + 16 = 25$.", "Center $(-2, 5)$: $(x + 2)^2 + (y - 5)^2 = 25$."],
      {"A": "flips the signs of the center.", "B": "uses $r = 5$ instead of $r^2 = 25$.", "D": "has both errors."}, tag="GEO &middot; Equation of a circle"),
    Q(36, "5", "A raffle sells 500 tickets at \\$5 each. One ticket wins \\$1,000, and two tickets each win \\$250. What is the expected net gain, in dollars, for a person who buys one ticket?", ["$-5.00$", "$-2.00$", "2.00", "3.00"], "B",
      "Expected value of the prize, minus the cost.", ["Prizes total $1000 + 2(250) = 1500$: $\\$3$ per ticket on average.", "Net: $3 - 5 = -\\$2$."],
      {"A": "counts the cost but not the prizes.", "C": "gets the sign wrong.", "D": "is the expected prize, ignoring the \\$5 cost."}, tag="S&amp;P &middot; Expected value (+Modeling)"),
    Q(37, "3", "Lena deposits \\$150 into savings in the first month and increases her deposit by \\$25 each month after that. What is the total she will have deposited after 12 months?", ["\\$425", "\\$3,300", "\\$3,450", "\\$5,100"], "C",
      "An arithmetic series: $S_n = \\dfrac{n(a_1 + a_n)}{2}$.", ["$a_{12} = 150 + 11(25) = 425$.", "$S_{12} = \\dfrac{12(150 + 425)}{2} = 3450$."],
      {"A": "is the 12th deposit, not the total.", "B": "uses 10 increases instead of 11 for the last term ($a_{12} = 400$).", "D": "multiplies the last deposit by 12."}, tag="FUN &middot; Arithmetic series (+Modeling)"),
    Q(38, "4", "A cone and a cylinder each have radius 3 and height 6. The cone sits inside the cylinder with the same base. What is the volume of the space inside the cylinder but outside the cone?", ["$12\\pi$", "$18\\pi$", "$27\\pi$", "$36\\pi$"], "D",
      "A cone is one third of the cylinder with the same base and height, so the leftover space is two thirds.", ["Cylinder: $\\pi(9)(6) = 54\\pi$; cone: $18\\pi$.", "Difference: $36\\pi$."],
      {"A": "does not follow; $54\\pi - 18\\pi = 36\\pi$.", "B": "is the cone's volume.", "C": "is half the cylinder."}, tag="GEO &middot; Volume"),
    Q(39, "2", "What is the solution set of $\\dfrac{x}{x - 3} - 2 = \\dfrac{3}{x - 3}$?", ["$\\{3\\}$", "$\\{-3\\}$", "$\\{0\\}$", "There are no real solutions."], "D",
      "Multiply by the denominator, solve, and reject any value that makes a denominator 0.", ["$x - 2(x - 3) = 3 \\Rightarrow -x + 6 = 3 \\Rightarrow x = 3$.", "But $x = 3$ makes the denominator 0: extraneous. No real solutions."],
      {"A": "keeps the extraneous solution.", "B": "check: $\\tfrac{-3}{-6} - 2 = -1.5$ but $\\tfrac{3}{-6} = -0.5$.", "C": "check: $0 - 2 = -2$ but $\\tfrac{3}{-3} = -1$."}, tag="ALG &middot; Rational equations"),
    Q(40, "1", "The vector $\\langle a, 6\\rangle$ has magnitude 10, and $a < 0$. What is the value of $a$?", ["$-8$", "$-4$", "4", "8"], "A",
      "Magnitude $= \\sqrt{a^2 + 6^2}$.", ["$a^2 + 36 = 100 \\Rightarrow a = \\pm 8$.", "$a < 0$: $a = -8$."],
      {"B": "subtracts lengths: $10 - 6$.", "C": "subtracts lengths and has the wrong sign.", "D": "has the right size but $a < 0$."}, tag="N&amp;Q &middot; Vectors"),
    Q(41, "3", "What is the range of $g(x) = -2|x + 1| + 3$?", ["$y \\le 3$", "$y \\ge 3$", "$y \\le -1$", "All real numbers"], "A",
      "$|x|$ reflected (negative coefficient) opens downward; its vertex sets the maximum.", ["Vertex $(-1, 3)$, opening down: maximum 3.", "Range: $y \\le 3$."],
      {"B": "would be right if it opened up, but the $-2$ flips it.", "C": "uses the vertex's $x$-coordinate.", "D": "an absolute-value graph has a maximum or minimum."}, tag="FUN &middot; Transformations"),
    Q(42, "4", "In $\\triangle ABC$, $m\\angle A = 30^\\circ$, $m\\angle B = 45^\\circ$, and side $a$ (opposite $\\angle A$) is 10. What is the length of side $b$, opposite $\\angle B$?", ["$5\\sqrt2$", "10", "$10\\sqrt2$", "20"], "C",
      "Law of sines: $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B}$.", ["$b = \\dfrac{10\\sin 45^\\circ}{\\sin 30^\\circ} = \\dfrac{10 \\cdot \\frac{\\sqrt2}{2}}{\\frac12} = 10\\sqrt2$."],
      {"A": "inverts the ratio of sines.", "B": "assumes $b = a$, but the angles differ.", "D": "uses $\\sin 90^\\circ$ instead of $\\sin 45^\\circ$."}, tag="GEO &middot; Law of sines"),
    Q(43, "4", "A square is inscribed in a circle of radius 6. What is the area of the region inside the circle but outside the square?", ["$36\\pi - 36$", "$36\\pi - 72$", "$36\\pi - 144$", "$12\\pi - 72$"], "B",
      "An inscribed square's diagonal is the circle's diameter; square area $= \\tfrac12 d^2$.", ["Diagonal 12: square area $\\tfrac12(144) = 72$.", "Circle: $36\\pi$. Region: $36\\pi - 72$."],
      {"A": "uses a square of side 6.", "C": "uses a square of side 12 (the diameter as the side).", "D": "uses the circumference instead of the area."}, tag="GEO &middot; Inscribed figures"),
    Q(44, "2", "An investment of \\$5,000 earns 6% interest compounded annually. What is the fewest number of whole years after which the investment will be worth at least \\$10,000?", ["10", "12", "17", "33"], "B",
      "Solve $1.06^t \\ge 2$ with logs (or by testing), and round up to a whole year.", ["$t \\ge \\dfrac{\\log 2}{\\log 1.06} \\approx 11.9$, so 12 years.", "Check: $1.06^{11} \\approx 1.90$ and $1.06^{12} \\approx 2.01$."],
      {"A": "check: $1.06^{10} \\approx 1.79$.", "C": "uses simple interest ($100\\% / 6\\% \\approx 16.7$).", "D": "far too long; it doubles well before then."}, tag="ALG &middot; Exponential equations (+Modeling)"),
    Q(45, "3", "The polynomial $p(x) = x^3 - 4x^2 + x + 6$ has a zero at $x = 2$. What are its other two zeros?", ["$-3$ and 1", "1 and 3", "$-2$ and 3", "$-1$ and 3"], "D",
      "Divide by the known factor $(x - 2)$ and factor the quadratic that remains.", ["$p(x) = (x - 2)(x^2 - 2x - 3) = (x - 2)(x - 3)(x + 1)$.", "Other zeros: 3 and $-1$."],
      {"A": "flips both signs.", "B": "check: $p(1) = 4 \\ne 0$.", "C": "check: $p(-2) = -20 \\ne 0$."}, tag="FUN &middot; Polynomial zeros"),
]
