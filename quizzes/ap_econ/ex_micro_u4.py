# Explanations, AP Microeconomics Unit 4 Practice Set, in source order.
EX = [
    # 1 not a barrier to entry
    dict(o=["is a legal barrier: no one else may sell the product.",
            "is a barrier: rivals cannot get the input.",
            "is a barrier: one large firm can supply the market more cheaply than several small ones.",
            "is a legal barrier: entrants need permission."]),
    # 2 MR below price
    dict(o=["is about cost, not revenue.",
            "describes a price taker, whose MR equals price.",
            "is about cost, not revenue.",
            "is about profit, not why MR falls below price."]),
    # 3 MR from linear demand (F)
    dict(steps=["$TR = PQ = 20Q - 2Q^2$.",
                "$MR = dTR/dQ = 20 - 4Q$: same intercept, twice the slope."],
         o={"A": "halves the slope instead of doubling it.",
            "B": "is the demand curve itself.",
            "D": "halves the intercept instead of doubling the slope.",
            "E": "doubles the intercept too; only the slope doubles."}),
    # 4 never on inelastic demand
    dict(o=["is backward: MR is positive where demand is elastic.",
            "is wrong: MR is zero there, not profit.",
            "gets the reason wrong: MR, not MC, is negative there.",
            "is backward: the monopolist produces on the elastic part."]),
    # 5 monopoly Q and P (F)
    dict(steps=["$MR = 24 - 4Q$. Set $MR = MC$: $24 - 4Q = 4$, so $Q = 5$.",
                "Price from demand: $P = 24 - 2(5) = \\$14$."],
         o={"A": "has the right quantity but charges MC; a monopolist charges what demand allows.",
            "C": "is the competitive outcome ($P = MC$).",
            "D": "is not where $MR = MC$: at $Q = 6$, $MR = 0$.",
            "E": "pairs the competitive quantity with the monopoly price, which is not on the demand curve."}),
    # 6 deadweight loss (F)
    dict(steps=["Efficient output: $24 - 2Q = 4$, so $Q = 10$.",
                "DWL $= \\tfrac12 \\times (10 - 5) \\times (14 - 4) = \\$25$."],
         o={"A": "is the gap between price and MC, not an area.",
            "B": "halves the triangle again.",
            "C": "uses the wrong base or height.",
            "E": "is the monopolist's profit, $(14 - 4) \\times 5$."}),
    # 7 lump-sum tax
    dict(o=["treats the fee like a per-unit tax that raises MC.",
            "has no basis: costs went up, not down.",
            "is wrong: a fixed fee does not change MC.",
            "is not how a monopolist chooses output."]),
    # 8 fair-return price
    dict(o=["describes no regulation outcome: at $P = ATC$ profit is zero, and the efficient output is at $P = MC$.",
            "describes the socially optimal price ($P = MC$), which causes a loss for a natural monopoly.",
            "has the output wrong: the regulated price is lower, so more is sold.",
            "is wrong: at $P = ATC$ the firm supplies what is demanded."]),
    # 9 monopoly vs competition
    dict(o=["is backward.",
            "is wrong: the monopolist restricts output.",
            "is inconsistent: less output comes with a higher price.",
            "is wrong: a higher price means less output and a deadweight loss."]),
    # 10 conditions for price discrimination
    dict(o=["is wrong: a price taker has no power to set different prices.",
            "is backward: groups must differ in elasticity.",
            "is not needed.",
            "is not needed; the firm sells to separate groups."]),
    # 11 perfect price discrimination
    dict(o=["is backward: output rises and deadweight loss disappears.",
            "is wrong: each buyer pays a different price.",
            "gets consumer surplus wrong: the firm captures all of it.",
            "is backward: it captures all surplus, so profit rises."]),
    # 12 student discount
    dict(o=["is backward: the less elastic group pays more.",
            "is wrong: with equal elasticities there is no gain from different prices.",
            "would justify a higher price, not a discount.",
            "is not the condition; elasticity is."]),
    # 13 monopolistic competition long run
    dict(o=["is wrong: entry removes economic profit.",
            "is wrong: $P > MC$ because demand slopes down.",
            "is wrong: output is below the minimum-ATC level (excess capacity).",
            "describes perfect competition."]),
    # 14 entry shifts demand
    dict(o=["describes the response to losses.",
            "is wrong: products stay differentiated.",
            "is wrong: each firm's demand falls.",
            "is wrong: entry takes customers away."]),
    # 15 monopolistic vs perfect competition
    dict(o=["describes oligopoly.",
            "describes monopoly.",
            "is wrong: entry removes long-run profit.",
            "describes perfect competition."]),
    # 16 dominant strategy
    dict(o=["is backward: not advertising pays less in both cases.",
            "is wrong: advertising is better whatever Beta does.",
            "is wrong: Alpha should advertise either way.",
            "is wrong: Alpha should advertise either way."]),
    # 17 Nash equilibrium
    dict(steps=["Beta: advertising gives 30 vs. 20 (if Alpha advertises) and 50 vs. 40 (if not), so it is dominant too.",
                "Both advertise: (40, 30). Neither wants to change alone."],
         o=["is better for both, but each would gain by advertising: not stable.",
            "is not stable: Beta gains by advertising (30 > 20).",
            "is not stable: Alpha gains by advertising (40 > 30).",
            "is wrong: both playing their dominant strategy is a Nash equilibrium."]),
    # 18 fee on Alpha
    dict(steps=["Alpha's advertising payoffs fall by 15: 25 vs. 30 and 45 vs. 50, so not advertising is now dominant.",
                "Beta still advertises (dominant). Result: (30, 50)."],
         o=["ignores the fee, which makes advertising worse for Alpha.",
            "is wrong: Beta still prefers to advertise.",
            "is backward: the fee falls on Alpha.",
            "is wrong: each firm has a dominant strategy."]),
    # 19 oligopoly
    dict(o=["describes monopoly.",
            "describes perfect and monopolistic competition.",
            "describes perfect competition.",
            "describes perfect and monopolistic competition."]),
    # 20 cartel instability
    dict(o=["is wrong: a working cartel earns monopoly profit.",
            "is wrong: cartels raise prices.",
            "is not the reason.",
            "is not the reason."]),
]
