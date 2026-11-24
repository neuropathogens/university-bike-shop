# Explanations, AP Macroeconomics Unit 5 Practice Set, in source order.
EX = [
    # 1 G up, bonds sold: interest rate
    dict(steps=["More government spending raises money demand (and borrowing): upward pressure on rates.",
                "Selling bonds drains reserves and shrinks the money supply: upward pressure on rates.",
                "Both push the same way, so the rate rises for certain; only the effect on AD is unclear."],
         o=["is the opposite of what both policies do to rates.",
            "ignores that both actions push rates up.",
            "applies to AD and output, where the policies conflict, not to the interest rate.",
            "adds a condition that does not matter; the rate rises either way."]),
    # 2 tax cut plus lower rates
    dict(o=["gets the price level wrong: AD shifts right along SRAS, so prices rise.",
            "is wrong: the central bank is lowering rates.",
            "is the opposite of two expansionary policies.",
            "is the opposite: more AD raises the price level."]),
    # 3 money in the long run
    dict(o=["reverses long-run neutrality: money changes prices, not real output.",
            "describes the short run; in the long run output returns to full employment.",
            "is wrong: output returns to $Y_f$, not below it.",
            "ignores that the price level rises permanently."]),
    # 4 AD increase on the Phillips curve
    dict(o=["is the effect of a fall in AD.",
            "is the effect of a supply shock or higher expected inflation.",
            "is wrong: the long-run curve sits at the natural rate and does not move with demand.",
            "would need a change in the natural rate, not in demand."]),
    # 5 negative supply shock
    dict(o=["is the effect of a favorable supply shock.",
            "describes the long-run curve, not the short-run one.",
            "describes a demand change; a supply shock moves the curve itself.",
            "is wrong: a temporary energy shock does not change the natural rate."]),
    # 6 vertical LRPC
    dict(o=["is impossible: frictional and structural unemployment always remain.",
            "is not a level of unemployment; the curve is vertical at a single unemployment rate.",
            "confuses the vertical line with the short-run curve's position, which expected inflation sets.",
            "would be below the natural rate, a short-run outcome."]),
    # 7 higher expected inflation
    dict(o=["is the effect of lower expected inflation.",
            "describes a change in slope, but expectations shift the curve up.",
            "ignores that expectations set the curve's height.",
            "describes neither curve: the long-run curve is vertical at the natural rate."]),
    # 8 MV = PY (F)
    dict(steps=["Quantity equation: $MV = PY$, and $PY$ is nominal GDP.",
                "$400 \\times 5 = \\$2{,}000$ billion."],
         o={"A": "divides $M$ by $V$ instead of multiplying.",
            "B": "adds $M$ and $V$.",
            "C": "uses a velocity of 2.",
            "E": "uses a velocity of 10."}),
    # 9 quantity theory growth rates (F)
    dict(steps=["In growth rates: $\\%\\Delta M + \\%\\Delta V = \\%\\Delta P + \\%\\Delta Y$.",
                "$5 + 0 = \\%\\Delta P + 3$, so $\\%\\Delta P = 2\\%$."],
         o={"A": "subtracts in the wrong order ($3 - 5$).",
            "C": "is real GDP growth, not inflation.",
            "D": "is money growth; part of it is absorbed by real growth.",
            "E": "adds the two rates instead of subtracting."}),
    # 10 neutrality of money
    dict(o=["reverses it: real output is unaffected in the long run.",
            "is too strong: the price level does change.",
            "is not the claim; the theory treats velocity as roughly stable.",
            "reverses it: nominal rates move with inflation, real rates do not."]),
    # 11 national debt (F)
    dict(steps=["Deficits add to the debt; a surplus subtracts from it.",
                "$500 + 40 + 60 - 20 = \\$580$ billion."],
         o={"A": "leaves out the \\$60 billion deficit.",
            "B": "leaves out the \\$40 billion deficit and the surplus.",
            "D": "leaves out the \\$20 billion surplus.",
            "E": "adds the surplus instead of subtracting it."}),
    # 12 smaller deficit
    dict(o=["confuses the change in the deficit with a change in the debt; only a surplus lowers the debt.",
            "treats the new deficit as debt repayment.",
            "ignores that the \\$60 billion deficit must be borrowed.",
            "adds the old and new deficits; only this year's \\$60 billion is new borrowing."]),
    # 13 deficit in a recession
    dict(o=["is backward: incomes and tax revenue fall in a recession.",
            "is backward: transfer payments rise automatically.",
            "ignores the automatic stabilizers.",
            "is the opposite of what happens in a downturn."]),
    # 14 crowding out sequence
    dict(o=["has the interest rate moving the wrong way.",
            "describes neither crowding out nor the likely effect of a tax cut.",
            "is wrong: a bond purchase lowers interest rates.",
            "confuses fiscal and monetary policy; borrowing does not create money."]),
    # 15 long-run crowding out
    dict(o=["is backward: less investment means slower growth.",
            "is backward for the same reason.",
            "ignores that investment builds the capital stock.",
            "is backward: crowding out comes from higher real rates."]),
    # 16 smallest crowding out
    dict(o=["is when crowding out is largest: no slack and strong competition for funds.",
            "means more private borrowing to displace, so more crowding out.",
            "pushes rates up further, adding to the crowding out.",
            "is the worst case: a boom with strong private demand for funds."]),
    # 17 rule of 70 (F)
    dict(steps=["Years to double $\\approx 70 \\div$ growth rate.",
                "$70/2 = 35$ years."],
         o={"A": "divides 70 by 5 instead of 2.",
            "B": "would need growth of 3.5\\% a year ($70/3.5$), not 2\\%.",
            "D": "forgets to divide by the growth rate.",
            "E": "multiplies 70 by 2 instead of dividing."}),
    # 18 labor productivity
    dict(o=["is a nominal change, not more output per worker.",
            "lowers output without making workers more productive.",
            "moves income around without adding tools, skills, or technology.",
            "is a demand-side policy with no effect on productivity."]),
    # 19 long-run growth
    dict(o=["raises spending, not capacity.",
            "is a short-run response to demand.",
            "is recovery from a recession, not growth in capacity.",
            "is about inflation expectations or supply shocks, not long-run growth."]),
    # 20 pro-growth policy
    dict(o=["raises spending now without raising capacity.",
            "discourages investment, slowing capital accumulation.",
            "distorts markets and creates shortages; it does not build capacity.",
            "restricts lending, which can reduce investment."]),
    # 21 job training
    dict(o=["is not the effect: training spending raises AD, if anything, and its lasting effect is on capacity.",
            "is backward: more productive workers lower costs.",
            "is backward: training reduces skill mismatches, lowering structural unemployment.",
            "ignores the gain in human capital."]),
    # 22 investment tax credit
    dict(o=["has both effects backward.",
            "misses the demand effect now and the capacity effect later.",
            "misses that the new equipment adds to capacity.",
            "is backward: the borrowing finances new capital, which raises LRAS."]),
]
