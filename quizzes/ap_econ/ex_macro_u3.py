# Explanations, AP Macroeconomics Unit 3 Practice Set, in source order.
EX = [
    # 1 why AD slopes down
    dict(o=["is the substitution effect behind a single market's demand curve; when the whole price level falls, relative prices need not change.",
            "is backward: a lower price level reduces money demand and lowers interest rates (the interest-rate effect).",
            "is backward: a lower domestic price level makes domestic goods cheaper relative to imports, raising net exports.",
            "is about aggregate supply, not demand."]),
    # 2 shift AD right
    dict(o=["is a movement along AD, not a shift.",
            "makes exports dearer and imports cheaper, lowering net exports and shifting AD left.",
            "lowers disposable income and consumption, shifting AD left.",
            "lowers investment spending, shifting AD left."]),
    # 3 price level up
    dict(o=["mistakes a movement along AD for a shift; the price level is on the axis.",
            "mistakes a movement along AD for a shift.",
            "has the causation backward: a change in the price level does not shift SRAS.",
            "gets the direction wrong: a higher price level lowers the quantity of real output demanded."]),
    # 4 multiplier (F)
    dict(steps=["Multiplier $= 1/(1 - \\text{MPC}) = 1/\\text{MPS}$.",
                "$1/(1 - 0.75) = 1/0.25 = 4$."],
         o={"A": "is the MPS, $1 - 0.75$, not the multiplier.",
            "B": "is the MPC itself.",
            "C": "is $1/\\text{MPC}$; the multiplier divides by the MPS.",
            "E": "multiplies the MPC by 10, which has no basis."}),
    # 5 G increase (F)
    dict(steps=["Spending multiplier $= 1/(1 - 0.9) = 10$.",
                "$\\Delta Y = 10 \\times \\$10\\text{ billion} = \\$100$ billion."],
         o={"A": "is only the first round of extra consumption ($0.9 \\times 10$).",
            "B": "ignores the multiplier.",
            "C": "adds the first two rounds and stops.",
            "D": "uses the tax multiplier ($-0.9/0.1 = -9$, in size 9); purchases use the spending multiplier, 10."}),
    # 6 tax cut (F)
    dict(steps=["Tax multiplier $= -\\text{MPC}/\\text{MPS} = -0.8/0.2 = -4$.",
                "A tax change of $-\\$20$ billion gives $(-4)(-20) = +\\$80$ billion."],
         o={"A": "is only the first round of extra consumption ($0.8 \\times 20$).",
            "B": "ignores the multiplier.",
            "D": "uses the spending multiplier (5); a tax cut is partly saved, so its multiplier is 4.",
            "E": "gets the sign wrong: a tax cut raises spending."}),
    # 7 balanced budget (F)
    dict(steps=["Spending multiplier $1/\\text{MPS}$ minus tax multiplier $\\text{MPC}/\\text{MPS}$ $= (1 - \\text{MPC})/\\text{MPS} = 1$.",
                "So a \\$20 billion balanced change in $G$ and $T$ raises GDP by \\$20 billion, whatever the MPC."],
         o={"A": "assumes the two changes cancel, but the tax multiplier is smaller than the spending multiplier.",
            "C": "applies a multiplier of 4 to the net change; the net multiplier is 1.",
            "D": "counts the purchases (multiplier 5 with an MPC of 0.8) and ignores the tax increase.",
            "E": "gets the sign wrong: the spending effect outweighs the tax effect."}),
    # 8 closing a gap (F)
    dict(steps=["Spending multiplier $= 1/(1 - 0.8) = 5$.",
                "Required $\\Delta G = 300/5 = \\$60$ billion."],
         o={"A": "divides the gap by 8 instead of by the multiplier, 5.",
            "B": "divides by 6 instead of 5.",
            "D": "multiplies the gap by the MPC instead of dividing by the multiplier.",
            "E": "ignores the multiplier: spending \\$300 billion would overshoot."}),
    # 9 SRAS slopes up
    dict(o=["describes the long run; fully flexible prices give a vertical LRAS.",
            "is the real-wealth effect, a reason AD slopes down.",
            "is false in the short run, when output can depart from full employment.",
            "is not how fiscal policy works and does not explain the slope of SRAS."]),
    # 10 oil price shock
    dict(o=["gets the direction wrong: higher input costs reduce supply.",
            "treats a cost shock as a demand change.",
            "is wrong: a temporary input-price change does not raise long-run capacity.",
            "is a movement along SRAS caused by a demand change; the curve itself shifts here."]),
    # 11 expected inflation
    dict(o=["gets the direction wrong: higher expected costs reduce supply.",
            "is wrong: expectations do not change potential output.",
            "puts the effect on demand; the question is about wage and cost setting.",
            "ignores that expected inflation feeds into wage contracts and costs."]),
    # 12 vertical LRAS
    dict(o=["is false: the price level can change in the long run; output just does not depend on it.",
            "is not the reason; AD can shift while LRAS stays vertical.",
            "is false: firms can change output; in the long run, output is set by resources and technology.",
            "is false: at full employment, frictional and structural unemployment remain."]),
    # 13 shift LRAS right
    dict(o=["shifts AD, not potential output.",
            "is a movement along a curve, not a shift.",
            "shifts AD.",
            "shifts SRAS; long-run capacity is unchanged."]),
    # 14 output left of LRAS
    dict(o=["describes output to the right of LRAS.",
            "requires output on LRAS.",
            "pairs the right gap with the wrong unemployment: a recessionary gap raises unemployment above the natural rate.",
            "is self-contradictory: an inflationary gap means unemployment below the natural rate."]),
    # 15 inflationary gap of $1 trillion
    dict(o=["has the sign backward: output is above potential.",
            "ignores the \\$1 trillion difference.",
            "uses the level of output instead of the gap between actual and potential.",
            "is backward: output above potential means unemployment below the natural rate."]),
    # 16 investment falls
    dict(o=["describes a supply shock (SRAS left), not a demand drop.",
            "cannot happen when only AD shifts left.",
            "describes an AD increase.",
            "is impossible: lower output means fewer workers are needed."]),
    # 17 stagflation
    dict(o=["raises output, not lowers it.",
            "lowers the price level as well as output.",
            "lowers prices and raises output.",
            "raises potential output and puts downward pressure on prices."]),
    # 18 exports rise at full employment
    dict(o=["has both effects backward for a rise in AD.",
            "gets unemployment wrong: output rises, so unemployment falls.",
            "describes the long run, after SRAS has shifted back.",
            "confuses a demand increase with a rise in capacity."]),
    # 19 recessionary gap, no policy
    dict(o=["describes the adjustment from an inflationary gap.",
            "assumes AD shifts on its own; in the model, self-correction works through wages and SRAS.",
            "is wrong: potential output does not fall to meet a recession.",
            "ignores the long-run adjustment of nominal wages."]),
    # 20 inflationary gap, no policy
    dict(o=["describes the recessionary-gap adjustment.",
            "assumes AD falls on its own; the adjustment works through wages and SRAS.",
            "is wrong: capacity does not grow to meet demand.",
            "is wrong: the adjustment raises the price level further."]),
    # 21 high unemployment
    dict(o=["is contractionary: it lowers disposable income and AD.",
            "is contractionary: it lowers disposable income and AD.",
            "is a monetary tool, and a contractionary one.",
            "is a monetary tool, and a contractionary one."]),
    # 22 contractionary fiscal policy
    dict(o=["describes expansionary policy.",
            "puts the effect on SRAS; fiscal policy works through AD.",
            "confuses demand policy with a change in capacity.",
            "gets the price level wrong: AD left lowers it."]),
    # 23 fiscal lags
    dict(o=["is false: changes in $G$ and $T$ shift AD directly.",
            "confuses fiscal policy with monetary policy.",
            "is wrong: discretionary fiscal policy shifts AD in the short run.",
            "is false: the simple multiplier is greater than 1."]),
    # 24 automatic stabilizer
    dict(o=["requires a new law, so it is discretionary.",
            "requires a new law, so it is discretionary.",
            "is monetary policy, decided by the central bank.",
            "requires a new decision, so it is discretionary."]),
    # 25 progressive tax in a recession
    dict(o=["gets the direction wrong: revenue falls, which supports AD.",
            "is wrong: rates are unchanged; incomes move into lower brackets.",
            "describes discretionary policy; the stabilizer works under existing law.",
            "confuses fiscal policy with monetary policy."]),
    # 26 budget over the cycle
    dict(o=["is backward: revenue falls and transfers rise in recessions.",
            "is not guaranteed; the budget moves with the cycle.",
            "is backward: revenue rises and transfers fall in expansions.",
            "ignores how revenue and transfers respond to income."]),
]
