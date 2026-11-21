"""ACT Math Guide 6: Essential Skills (21 items)."""
import math
from fractions import Fraction as F

from act_math.quiz import Q

DOC = dict(
    slug="6", pdf="act-math-06-essential-skills.pdf", title="Guide 6: Essential Skills", h1='Essential <span style="white-space:nowrap">Skills</span>',
    sub="ACT Math &middot; Guide 6", metaline="21 four-choice drill items &middot; target 23 min",
    desc="ACT Math Guide 6 (Essential Skills): 21 drill items on percents, ratios, rates, unit conversion, applied area and volume, and multi-step problems, each with a worked explanation.",
    setup="Work each section without notes; the target time is 23 minutes.",
    rules={"1.1": ("Multipliers, not steps", 1), "2.1": ("Parts and scale factors", 2), "3.1": ("Rate &times; time = amount", 3),
           "4.1": ("Multiply by fractions equal to 1", 3), "5.1": ("Model the object, then count units", 4), "6.1": ("Name the pieces, then combine", 4)},
    sections={1: "Percents", 2: "Ratios &amp; proportions", 3: "Rates", 4: "Unit conversion", 5: "Applied area &amp; volume", 6: "Multi-step problems"},
    key="1 B 2 A 3 C 4 D 5 B 6 D 7 C 8 A 9 B 10 C 11 A 12 B 13 C 14 A 15 B 16 D 17 B 18 C 19 D 20 B 21 A",
)

assert 0.35 * 240 == 84 and 240 - 84 == 156
assert math.isclose(80 * 1.2 * 0.75, 72) and math.isclose(80 * 0.95, 76)
assert math.isclose(68 / 0.85, 80) and math.isclose(68 * 1.15, 78.2)
assert math.isclose(60 / 250, 0.24) and round(60 / 310 * 100, 1) == 19.4
assert math.isclose(2000 * 1.05 ** 3, 2315.25) and 2000 * 1.15 == 2300 and math.isclose(2000 * 1.05 * 1.11, 2331.0)
assert 32 // 8 * 5 == 20 and 32 // 8 * 3 == 12
assert 12 * 3.75 == 45 and F(2, 3) * F(30, 12) == F(5, 3)
assert math.isclose(13.5 / 6 * 10, 22.5)
assert math.isclose(240 / 3.2, 75) and math.isclose(240 / 3.12, 76.92, abs_tol=0.01)
assert 120 / (60 / 30 + 60 / 60) == 40 and (30 + 60) / 2 == 45
assert 1 / (F(1, 6) + F(1, 3)) == 2
assert 72 * 1000 / 3600 == 20
assert 270 / 9 == 30 and 270 / 3 == 90
assert math.ceil(2 * 4 * 12 * 9 / 350) == 3 and math.ceil(4 * 12 * 9 / 350) == 2
assert 12 * 15 / 0.25 == 720 and 12 * 15 / 0.5 == 360
assert round(30 * 12 * 16 / 231) == 25
assert round(math.pi * 4 * 5 / 3, 1) == 20.9 and round(math.pi * 4 * 5, 1) == 62.8
assert 40 * 15 + 6 * 22.5 == 735 and 46 * 15 == 690
N = 48
assert N - F(3, 8) * N - F(1, 3) * (N - F(3, 8) * N) == 20
assert 0.30 * 10 + 0.10 * 10 == 0.20 * 20

QS = [
    Q(1, "1.1", "What is 35% of 240?", ["68", "84", "96", "156"], "B",
      "&ldquo;$r$% of&rdquo; means multiply by $r/100$.",
      ["$0.35 \\times 240 = 84$."],
      {"A": "does not follow; $0.35 \\times 240 = 84$.",
       "C": "is 40% of 240.",
       "D": "is 65% of 240, what is left after taking 35%."}, sec=1),
    Q(2, "1.1", "A jacket priced at \\$80 is marked up 20%. Later, the new price is reduced by 25%. What is the final price?", ["\\$72", "\\$76", "\\$80", "\\$84"], "A",
      "Turn each percent change into a multiplier and multiply; successive changes do not add.",
      ["$80 \\times 1.20 = 96$, then $96 \\times 0.75 = 72$.", "Net multiplier $1.2 \\times 0.75 = 0.9$: a 10% decrease, not 5%."],
      {"B": "adds the percents ($+20 - 25 = -5\\%$); the 25% is taken from the higher price.",
       "C": "assumes the changes cancel.",
       "D": "does not follow from either multiplier order."}, sec=1),
    Q(3, "1.1", "After a 15% discount, a pair of shoes costs \\$68. What was the original price?", ["\\$57.80", "\\$78.20", "\\$80.00", "\\$83.00"], "C",
      "Reverse percent: sale price $=$ multiplier $\\times$ original, so divide by the multiplier.",
      ["$0.85P = 68 \\Rightarrow P = 68 / 0.85 = 80$."],
      {"A": "takes 15% off the sale price again.",
       "B": "adds 15% of the <i>sale</i> price; the 15% was of the original.",
       "D": "adds 15 dollars instead of reversing a percent."}, sec=1),
    Q(4, "1.1", "A store&rsquo;s daily customers rose from 250 to 310. What was the percent increase?", ["6%", "12%", "19.4%", "24%"], "D",
      "Percent change $= \\dfrac{\\text{new} - \\text{old}}{\\text{old}} \\times 100\\%$; the denominator is the original.",
      ["$\\dfrac{310 - 250}{250} = \\dfrac{60}{250} = 24\\%$."],
      {"A": "does not follow; $60/250 = 0.24 = 24\\%$.",
       "B": "halves the correct answer.",
       "C": "divides by the new value, $60/310$."}, sec=1),
    Q(5, "1.1", "A deposit of \\$2,000 earns 5% interest compounded annually. What is the balance after 3 years?", ["\\$2,300.00", "\\$2,315.25", "\\$2,331.00", "\\$2,400.00"], "B",
      "Compound growth: $A = P(1 + r)^t$; each year's interest is earned on the new balance.",
      ["$2000(1.05)^3 = 2000(1.157625) = 2315.25$."],
      {"A": "is simple interest: $2000 + 3(100)$.",
       "C": "overstates the growth; $(1.05)^3 = 1.157625$.",
       "D": "uses 20% total growth."}, sec=1),
    Q(6, "2.1", "The ratio of boys to girls in a class of 32 students is $3 : 5$. How many girls are in the class?", ["12", "15", "18", "20"], "D",
      "A ratio $a : b$ splits the whole into $a + b$ equal parts.",
      ["$3 + 5 = 8$ parts; each part is $32 \\div 8 = 4$ students.", "Girls: $5 \\times 4 = 20$."],
      {"A": "is the number of boys.",
       "B": "does not follow from 8 equal parts of 4.",
       "C": "does not follow from 8 equal parts of 4."}, sec=2),
    Q(7, "2.1", "On a map, 1 inch represents 12 miles. Two towns are 3.75 inches apart on the map. What is the actual distance between them, in miles?", ["3.2", "36", "45", "48"], "C",
      "Use one scale factor: miles $=$ inches $\\times 12$.",
      ["$3.75 \\times 12 = 45$ miles."],
      {"A": "divides 12 by 3.75 instead of multiplying.",
       "B": "uses only the whole inches, $3 \\times 12$.",
       "D": "rounds 3.75 up to 4 inches."}, sec=2),
    Q(8, "2.1", "A recipe uses $\\tfrac23$ cup of sugar to make 12 cookies. At this rate, how many cups of sugar are needed for 30 cookies?",
      ["$1\\tfrac23$", "2", "$2\\tfrac12$", "5"], "A",
      "Scaling a recipe uses one scale factor, new $\\div$ old.",
      ["Scale factor $\\dfrac{30}{12} = 2.5$.", "$\\tfrac23 \\times 2.5 = \\tfrac53 = 1\\tfrac23$ cups."],
      {"B": "does not follow; $\\tfrac23 \\times 2.5 = \\tfrac53$.",
       "C": "is the scale factor itself, not the amount of sugar.",
       "D": "check: 5 cups for 30 cookies is $\\tfrac16$ cup per cookie, but the recipe uses $\\tfrac{1}{18}$ cup per cookie."}, sec=2),
    Q(9, "3.1", "Six pounds of apples cost \\$13.50. At the same price per pound, how much do 10 pounds cost?", ["\\$20.25", "\\$22.50", "\\$24.00", "\\$27.00"], "B",
      "Find the unit rate (price per pound), then multiply by the new quantity.",
      ["$13.50 \\div 6 = \\$2.25$ per pound.", "$10 \\times 2.25 = \\$22.50$."],
      {"A": "is the cost of 9 pounds.",
       "C": "does not follow from \\$2.25 per pound.",
       "D": "is the cost of 12 pounds (twice the original)."}, sec=3),
    Q(10, "3.1", "A train travels 240 miles in 3 hours 12 minutes. What is its average speed, in miles per hour?", ["70", "72", "75", "80"], "C",
      "Convert minutes to hours before dividing: 12 minutes $= 0.2$ hour.",
      ["Time: $3 + 0.2 = 3.2$ hours.", "Speed: $240 \\div 3.2 = 75$ mph."],
      {"A": "uses a time of about 3.43 hours.",
       "B": "uses 3 hours 20 minutes (3.33 h).",
       "D": "ignores the 12 minutes: $240 \\div 3$."}, sec=3),
    Q(11, "3.1", "A driver travels 60 miles at 30 mph, then returns the same 60 miles at 60 mph. What is the average speed for the round trip, in mph?", ["40", "45", "48", "50"], "A",
      "Average speed $= \\dfrac{\\text{total distance}}{\\text{total time}}$, not the average of the two speeds.",
      ["Times: $60/30 = 2$ h and $60/60 = 1$ h.", "Average: $\\dfrac{120}{3} = 40$ mph."],
      {"B": "averages the two speeds; the slower leg takes longer, so it counts more.",
       "C": "does not follow; total time is 3 hours.",
       "D": "does not follow; total time is 3 hours."}, sec=3),
    Q(12, "3.1", "Pipe A alone fills a tank in 6 hours. Pipe B alone fills it in 3 hours. How many hours do both pipes take, working together, to fill the empty tank?", ["1.5", "2", "4.5", "9"], "B",
      "Work rates add: a job done in $a$ hours is done at $\\tfrac1a$ per hour.",
      ["Combined rate: $\\tfrac16 + \\tfrac13 = \\tfrac12$ tank per hour.", "Time: 2 hours."],
      {"A": "halves the faster pipe's time; the slower pipe helps, but not that much.",
       "C": "averages the two times.",
       "D": "adds the two times."}, sec=3),
    Q(13, "4.1", "A car travels at 72 kilometers per hour. What is this speed in meters per second?", ["1.2", "7.2", "20", "259.2"], "C",
      "Chain conversion factors that equal 1 so the units cancel.",
      ["$72\\,\\dfrac{\\text{km}}{\\text{h}} \\cdot \\dfrac{1000\\,\\text{m}}{1\\,\\text{km}} \\cdot \\dfrac{1\\,\\text{h}}{3600\\,\\text{s}} = 20\\,\\text{m/s}$."],
      {"A": "divides by 60 only (km per minute).",
       "B": "divides by 10.",
       "D": "multiplies by 3.6 instead of dividing."}, sec=4),
    Q(14, "4.1", "A floor has an area of 270 square feet. What is its area in square yards?", ["30", "90", "810", "2,430"], "A",
      "Square units convert with the factor squared: $1\\,\\text{yd}^2 = 3 \\times 3 = 9\\,\\text{ft}^2$.",
      ["$270 \\div 9 = 30\\,\\text{yd}^2$."],
      {"B": "divides by 3, the linear factor.",
       "C": "multiplies by 3.",
       "D": "multiplies by 9; going to a bigger unit gives a smaller number."}, sec=4),
    Q(15, "5.1", "A room has 4 walls, each 12 feet wide and 9 feet tall. Each wall needs 2 coats of paint. One gallon covers 350 square feet, and paint is sold only in whole gallons. What is the minimum number of gallons needed?", ["2", "3", "4", "5"], "B",
      "Find the total area to cover, divide by coverage, and round <i>up</i> when only whole units are sold.",
      ["Area: $4 \\times (12 \\times 9) = 432\\,\\text{ft}^2$; two coats: $864\\,\\text{ft}^2$.", "$864 \\div 350 \\approx 2.47$; round up to 3 gallons."],
      {"A": "rounds down (not enough paint) or forgets the second coat.",
       "C": "is more than needed; 3 gallons cover 1,050 square feet.",
       "D": "is more than needed."}, sec=5),
    Q(16, "5.1", "A rectangular floor measures 12 feet by 15 feet. How many square tiles, each 6 inches on a side, are needed to cover it?", ["30", "90", "360", "720"], "D",
      "Put both areas in the same units; a 6-inch tile is $0.5 \\times 0.5 = 0.25\\,\\text{ft}^2$.",
      ["Floor: $12 \\times 15 = 180\\,\\text{ft}^2$.", "$180 \\div 0.25 = 720$ tiles (equivalently $24 \\times 30$)."],
      {"A": "divides by 6, mixing inches and feet.",
       "B": "does not follow; each square foot holds 4 tiles.",
       "C": "divides by 0.5, treating a tile's side as its area."}, sec=5),
    Q(17, "5.1", "An aquarium is a rectangular box measuring 30 inches by 12 inches by 16 inches. One gallon is 231 cubic inches. About how many gallons does the aquarium hold when full?", ["19", "25", "30", "48"], "B",
      "Volume of a box is length $\\times$ width $\\times$ height; then convert with the given factor.",
      ["$30 \\times 12 \\times 16 = 5760\\,\\text{in}^3$.", "$5760 \\div 231 \\approx 24.9 \\approx 25$ gallons."],
      {"A": "underestimates; $19 \\times 231 = 4389$ cubic inches.",
       "C": "overestimates; $30 \\times 231 = 6930$ cubic inches.",
       "D": "overestimates; $48 \\times 231 = 11\\,088$ cubic inches."}, sec=5),
    Q(18, "5.1", "An empty cylindrical tank has radius 2 feet and height 5 feet. Water flows in at 3 cubic feet per minute. To the nearest tenth of a minute, how long will it take to fill the tank?", ["6.7", "10.5", "20.9", "62.8"], "C",
      "Volume of a cylinder is $\\pi r^2 h$; time $=$ volume $\\div$ rate.",
      ["$V = \\pi(2)^2(5) = 20\\pi \\approx 62.8\\,\\text{ft}^3$.", "$62.8 \\div 3 \\approx 20.9$ minutes."],
      {"A": "is $20 \\div 3$: it leaves out $\\pi$.",
       "B": "uses $\\pi r h$ instead of $\\pi r^2 h$ in the volume.",
       "D": "is the volume, not the time."}, sec=5),
    Q(19, "6.1", "Maria earns \\$15 per hour for the first 40 hours she works each week and 1.5 times that rate for each additional hour. How much does she earn in a week when she works 46 hours?", ["\\$690", "\\$705", "\\$720", "\\$735"], "D",
      "Split the week into its pieces: regular hours and overtime hours, each at its own rate.",
      ["Regular: $40 \\times 15 = \\$600$.", "Overtime: $6 \\times 22.50 = \\$135$. Total: \\$735."],
      {"A": "pays all 46 hours at \\$15.",
       "B": "adds only \\$15 of extra pay for the 6 overtime hours in total.",
       "C": "does not follow; overtime is $6 \\times 22.50 = 135$."}, sec=6),
    Q(20, "6.1", "In a class, $\\tfrac38$ of the students walk to school, $\\tfrac13$ of the remaining students bike, and the other 20 students ride the bus. How many students are in the class?", ["36", "48", "60", "72"], "B",
      "With fractions of a remainder, subtract before taking the next fraction.",
      ["Walk $\\tfrac38$, so $\\tfrac58$ remain. Bike $\\tfrac13 \\cdot \\tfrac58 = \\tfrac{5}{24}$.",
       "Bus $= \\tfrac58 - \\tfrac{5}{24} = \\tfrac{10}{24} = \\tfrac{5}{12}$ of the class.", "$\\tfrac{5}{12}N = 20 \\Rightarrow N = 48$."],
      {"A": "check: $\\tfrac38$ of 36 is not a whole number.",
       "C": "check: $\\tfrac38$ of 60 is not a whole number.",
       "D": "check: with 72 students, 30 would ride the bus."}, sec=6),
    Q(21, "6.1", "How many liters of a 10% salt solution must be added to 10 liters of a 30% salt solution to make a 20% salt solution?", ["10", "15", "20", "30"], "A",
      "Track the amount of the pure substance: concentration $\\times$ volume.",
      ["Salt: $0.30(10) + 0.10x = 0.20(10 + x)$.", "$3 + 0.1x = 2 + 0.2x \\Rightarrow x = 10$. (20% is exactly halfway, so equal volumes.)"],
      {"B": "check: $(3 + 1.5)/25 = 18\\%$.",
       "C": "check: $(3 + 2)/30 \\approx 16.7\\%$.",
       "D": "check: $(3 + 3)/40 = 15\\%$."}, sec=6),
]
