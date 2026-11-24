# Explanations, AP Macroeconomics Unit 2 Practice Set, in source order.
EX = [
    # 1 GDP from the table (F)
    dict(steps=["GDP $= C + I + G + (X - M)$.",
                "$500 + 150 + 200 + (60 - 80) = 830$. Transfer payments are not purchases of output, so they are left out."],
         o={"A": "subtracts the \\$70 billion of transfer payments; they are simply excluded, not subtracted.",
            "C": "adds the \\$70 billion of transfer payments, which buy no new output.",
            "D": "adds imports instead of subtracting them.",
            "E": "adds both imports and transfer payments."}),
    # 2 included in GDP
    dict(o=["was counted in GDP the year it was new; reselling it produces nothing new.",
            "is a financial asset; buying it transfers ownership but produces no good or service.",
            "is a transfer payment: income moves from taxpayers to retirees with nothing produced in return.",
            "is an intermediate good; its value is already in the price of the bread."]),
    # 3 final goods (F)
    dict(steps=["Wheat and flour are intermediate goods used up in making bread.",
                "Count only the final sale, \\$9. Check: value added $2 + 3 + 4 = 9$."],
         o={"A": "counts only the farmer's sale, the first stage.",
            "B": "adds the two intermediate sales, \\$2 and \\$5, and misses the final good.",
            "D": "adds the flour and the bread, counting the flour twice.",
            "E": "adds every sale, which counts the wheat and flour two or three times."}),
    # 4 investment in GDP
    dict(o=["is a financial investment; buying bonds creates no new capital.",
            "is consumption: households' purchases of goods other than new housing are C.",
            "is saving, a financial flow, not spending on new capital.",
            "buys an existing building; only newly produced capital counts."]),
    # 5 not counted in GDP
    dict(o=["is a market sale, so it is counted (consumption).",
            "is a government purchase of a service, counted in G.",
            "is new capital, counted as investment.",
            "is a market purchase from a domestic shop, counted in GDP."]),
    # 6 standard of living
    dict(o=["is inflated by prices and ignores population size.",
            "adjusts for prices but not for population; a large country can have high real GDP and low living standards.",
            "measures idle labor, not how much output each person has.",
            "measures how fast prices rise, not how much output each person has."]),
    # 7 unemployment rate (F)
    dict(steps=["Labor force $=$ employed $+$ unemployed $= 180 + 20 = 200$ million. People not in the labor force are left out.",
                "Unemployment rate $= 20/200 = 10\\%$."],
         o={"A": "divides by all 300 million adults instead of the labor force.",
            "C": "divides by the employed (180 million) instead of the labor force.",
            "D": "divides by the 100 million not in the labor force.",
            "E": "is the labor force participation rate, $200/300$."}),
    # 8 discouraged workers
    dict(o=["counts discouraged workers as unemployed, but people who stop looking leave the labor force.",
            "misses that the official rate counts only people actively looking for work.",
            "has the labor force shrinking, not growing.",
            "is wrong about the cause: nobody found a job; the unemployed count fell because people stopped looking."]),
    # 9 structural unemployment
    dict(o=["is short-term job search between jobs; her skills no longer match any available job.",
            "is caused by a recession; her job disappeared because of technology.",
            "follows a regular calendar pattern, which is not the case here.",
            "is contradictory: cyclical unemployment is not part of the natural rate."]),
    # 10 natural rate
    dict(o=["includes cyclical unemployment, which is zero at the natural rate.",
            "includes cyclical unemployment, which is zero at the natural rate.",
            "confuses full employment with zero unemployment; frictional and structural unemployment remain.",
            "would include cyclical unemployment; the natural rate is measured at full employment."]),
    # 11 CPI (F)
    dict(steps=["CPI $=$ (cost of basket this year $\\div$ cost in base year) $\\times 100$.",
                "$230/200 \\times 100 = 115$."],
         o={"A": "is the dollar increase in the basket's cost, not an index.",
            "B": "inverts the ratio: $200/230 \\times 100$.",
            "D": "adds the \\$30 increase to 100 as if it were 30\\%; the increase is 15\\%.",
            "E": "is this year's cost in dollars, not the index."}),
    # 12 inflation from CPI (F)
    dict(steps=["Inflation $= (126 - 120)/120$.",
                "$6/120 = 0.05 = 5\\%$."],
         o={"A": "divides by the later index (126) instead of the earlier one.",
            "C": "reports the 6-point change as a percent without dividing by 120.",
            "D": "divides 120 by 6, inverting the ratio.",
            "E": "measures the change from the base year (100), not over this year."}),
    # 13 real wage
    dict(o=["subtracts in the wrong order; prices rose faster than the wage.",
            "adds inflation to the nominal change instead of subtracting it.",
            "adds the two rates and gives the sum a negative sign.",
            "ignores that prices rose faster than the wage, so purchasing power fell."]),
    # 14 CPI overstates
    dict(o=["is wrong on the facts: the CPI basket is consumer goods and services, not capital goods.",
            "is backward: the CPI uses fixed base-period quantities, which is the source of substitution bias.",
            "is false: services such as rent and medical care are in the basket.",
            "is false: the CPI includes imported consumer goods (it is the GDP deflator that covers only domestic output)."]),
    # 15 unexpected inflation winners
    dict(o=["is the lender, which is repaid with money worth less than expected.",
            "has a fixed nominal income whose purchasing power falls.",
            "has a fixed nominal wage whose purchasing power falls.",
            "holds money that loses purchasing power as prices rise."]),
    # 16 menu costs
    dict(o=["are the costs of holding less cash to avoid inflation (more trips to the bank).",
            "is about money becoming a less reliable measuring stick, not reprinting price lists.",
            "is the general idea of a forgone alternative, not this specific cost of inflation.",
            "are past costs that cannot be recovered; they are unrelated to changing prices."]),
    # 17 unexpected deflation losers
    dict(o=["gain: they are repaid in dollars that buy more than expected.",
            "gain: each dollar buys more as prices fall.",
            "gain: a fixed nominal income buys more when prices fall.",
            "gain: their fixed nominal returns are worth more in real terms."]),
    # 18 real GDP from the deflator (F)
    dict(steps=["Real GDP $=$ nominal GDP $\\div$ (deflator$/100$).",
                "$1{,}200 \\div 1.20 = 1{,}000$ billion."],
         o={"B": "subtracts the deflator (120) from nominal GDP instead of dividing.",
            "C": "is nominal GDP, unadjusted for prices.",
            "D": "adds 120 to nominal GDP.",
            "E": "multiplies by 1.20 instead of dividing."}),
    # 19 real GDP growth, two goods (F)
    dict(steps=["Value both years' output at base-year (Year 1) prices.",
                "Year 1: $10(\\$2) + 5(\\$4) = \\$40$. Year 2: $12(\\$2) + 6(\\$4) = \\$48$.",
                "Real growth $= (48 - 40)/40 = 20\\%$."],
         o={"A": "is too low: the quantities of both goods rose 20\\% (10 to 12 and 5 to 6), so real output rose 20\\%.",
            "C": "is the rise in the price level (Year 2's deflator is $66/48 = 137.5$), not real growth.",
            "D": "is the increase in the price of good A (\\$2 to \\$3), not output growth.",
            "E": "is nominal growth, $(66 - 40)/40$, which mixes price increases with output growth."}),
    # 20 real from nominal and deflator
    dict(o=["adds the deflator's rise instead of subtracting it.",
            "subtracts in the wrong order.",
            "is nominal growth, ignoring that prices rose 4\\%.",
            "ignores that nominal GDP grew faster than prices."]),
    # 21 trough
    dict(o=["is the highest point, where an expansion ends.",
            "is the falling phase that leads down to the trough.",
            "is the rising phase that follows the trough.",
            "is the long-run growth path the cycle fluctuates around."]),
    # 22 negative output gap
    dict(o=["describes a positive output gap, with real GDP above potential.",
            "holds only when real GDP equals potential.",
            "is the high point of the cycle, often above potential, not below it.",
            "is impossible when output is below potential; the economy is inside its PPC."]),
    # 23 contraction on the PPC
    dict(o=["is economic growth, an increase in capacity.",
            "means lost capacity (for example, destroyed capital); a recession leaves resources idle instead.",
            "is a different choice of output mix with full employment.",
            "is unattainable with current resources."]),
]
