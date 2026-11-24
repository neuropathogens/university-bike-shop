# Explanations, AP Microeconomics Unit 3 Practice Set, in source order.
EX = [
    # 1 diminishing marginal returns (F)
    dict(steps=["Marginal product: $8, 12, 10, 6, 2$ for workers 1 to 5.",
                "MP rises through the second worker and first falls with the third."],
         o={"A": "is where MP starts (8); it then rises to 12.",
            "B": "is where MP peaks; diminishing returns start with the next worker.",
            "D": "is a later decline; MP already fell with the third worker.",
            "E": "is a later decline; MP already fell with the third worker."}),
    # 2 MP of fourth worker (F)
    dict(steps=["$MP_4 = TP_4 - TP_3 = 36 - 30 = 6$."],
         o={"A": "is the marginal product of the fifth worker ($38 - 36$).",
            "C": "is the average product of four workers ($36/4$).",
            "D": "is the marginal product of the third worker ($30 - 20$).",
            "E": "is total product, not marginal product."}),
    # 3 MP above AP
    dict(o=["is the case when marginal product is below the average.",
            "holds only when marginal equals average.",
            "is impossible here: both are positive.",
            "has no basis; average product is positive and rising."]),
    # 4 short run
    dict(o=["describes the long run.",
            "describes the long run.",
            "is false: firms change output by changing variable inputs.",
            "is false: some costs are fixed in the short run."]),
    # 5 AVC (F)
    dict(steps=["$VC = TC - FC = 130 - 50 = 80$.",
                "$AVC = 80/4 = \\$20$."],
         o={"A": "is average fixed cost ($50/4$).",
            "C": "is average total cost ($130/4$).",
            "D": "is total fixed cost.",
            "E": "is total variable cost, not the average."}),
    # 6 MC meets ATC
    dict(o=["is wrong: ATC is U-shaped and has no maximum on the relevant range.",
            "is wrong: AFC falls forever and has no minimum.",
            "is wrong: MC crosses ATC on MC's rising part, after MC's minimum.",
            "is wrong: the relationship holds in the short run."]),
    # 7 rent increase
    dict(o=["names variable-cost curves, which a fixed cost does not affect.",
            "wrongly includes MC and AVC.",
            "is wrong: AVC does not depend on fixed costs.",
            "is wrong: MC and AVC do not change."]),
    # 8 MC = w / MP (F)
    dict(steps=["Each extra hour of labor costs \\$20 and adds 4 units.",
                "$MC = 20/4 = \\$5$ per unit."],
         o={"A": "inverts the ratio ($4/20$).",
            "B": "is the marginal product, not a cost.",
            "D": "subtracts instead of dividing.",
            "E": "multiplies instead of dividing."}),
    # 9 economies of scale
    dict(o=["would mean output rises less than in proportion to inputs.",
            "would mean output exactly doubles.",
            "is a short-run idea with a fixed input; here all inputs change.",
            "is a short-run cost idea; with all inputs doubling, long-run average cost falls."]),
    # 10 diseconomies of scale
    dict(o=["is a source of economies of scale.",
            "is a source of economies of scale.",
            "is a source of falling average cost.",
            "is diminishing marginal returns, a short-run idea."]),
    # 11 minimum efficient scale
    dict(o=["is a short-run point, not the bottom of the long-run curve.",
            "is a short-run point.",
            "is capacity, not efficiency.",
            "describes long-run equilibrium in competition, not a property of costs."]),
    # 12 normal profit
    dict(o=["is wrong: normal profit means accounting profit just covers implicit costs.",
            "is above normal profit.",
            "is below normal profit.",
            "describes an economic loss."]),
    # 13 economic profit vs alternative
    dict(o=["ignores the \\$50{,}000 she gives up.",
            "adds the forgone salary instead of subtracting it.",
            "gets the sign wrong.",
            "is wrong: zero would need the shop to earn exactly \\$50{,}000."]),
    # 14 economic vs accounting profit
    dict(o=["is backward: subtracting more costs makes it smaller.",
            "is wrong when the owner supplies resources with other uses.",
            "is wrong: it can be positive or negative.",
            "leaves out the explicit costs."]),
    # 15 output choice (F)
    dict(steps=["MC of units 1 to 6: $30, 20, 16, 24, 35, 49$.",
                "Produce while $MC \\le P = 40$: unit 5 costs \\$35, unit 6 costs \\$49. Produce 5."],
         o={"A": "stops while units 4 and 5 still cost less than \\$40.",
            "B": "stops while unit 5 still costs less than \\$40 ($MC = 35$).",
            "D": "includes unit 6, whose MC (\\$49) exceeds the price.",
            "E": "is wrong: the price covers average variable cost, and the firm makes a profit."}),
    # 16 maximum profit (F)
    dict(steps=["At 5 units: $TR = 5 \\times 40 = 200$, $TC = 185$.",
                "Profit $= \\$15$ (compare \\$10 at 4 units and \\$6 at 6)."],
         o={"A": "is the gain from the fifth unit alone ($40 - 35$).",
            "C": "does not match any output: profit is at most \\$15.",
            "D": "is the price, not profit.",
            "E": "is too high: total cost at 5 units is \\$185."}),
    # 17 MR = MC everywhere
    dict(o=["is too narrow: the rule holds in every structure.",
            "is too narrow: the rule holds in every structure.",
            "is wrong: the rule also minimizes losses.",
            "is wrong: it applies in the short run too."]),
    # 18 MR in perfect competition
    dict(o=["describes a firm with market power.",
            "is impossible for a price taker.",
            "holds only in long-run equilibrium, not at every quantity.",
            "has no basis: MR equals the price, which is positive."]),
    # 19 shutdown (fixed cost $60, P = $20)
    dict(steps=["AVC at outputs 1 to 6: $30, 25, 22, 22.50, 25, 29$; minimum \\$22.",
                "Price \\$20 is below minimum AVC, so any output loses more than the \\$60 fixed cost. Shut down."],
         o=["loses \\$66, more than the \\$60 from shutting down.",
            "loses \\$70, more than shutting down.",
            "loses \\$85, more than shutting down.",
            "loses \\$70, more than shutting down."]),
    # 20 between AVC and ATC
    dict(o=["ignores that shutting down still costs the fixed cost.",
            "is impossible for a price taker.",
            "is not the rule; produce where $P = MC$.",
            "confuses the short run with the long run."]),
    # 21 short-run supply curve
    dict(o=["includes the part below minimum AVC, where the firm shuts down.",
            "is the wrong curve; output is set by MC.",
            "is the wrong curve; output is set by MC.",
            "is the demand the firm faces, not its supply curve."]),
    # 22 losses in the long run
    dict(o=["describes the response to profits.",
            "is inconsistent: exit lowers supply, raising the price.",
            "is not part of the model.",
            "ignores exit."]),
    # 23 long-run equilibrium
    dict(o=["would mean allocative inefficiency, which competition removes.",
            "means the firm should produce more.",
            "means losses, which cause exit.",
            "means losses, which cause exit in the long run."]),
    # 24 firm's demand curve
    dict(o=["would mean buyers pay any price, but they switch to rivals.",
            "describes the market, not one firm.",
            "describes a firm with some market power.",
            "describes supply."]),
    # 25 constant-cost industry, demand up
    dict(o=["holds in an increasing-cost industry, not a constant-cost one.",
            "has the number of firms wrong: profit attracts entry.",
            "has no basis: costs do not change, so price returns to minimum ATC.",
            "is wrong: entry removes the profit."]),
    # 26 positive economic profit
    dict(o=["describes the response to losses.",
            "names a demand change; the adjustment comes through entry.",
            "is not the adjustment; costs are given.",
            "is impossible for a price taker."]),
]
