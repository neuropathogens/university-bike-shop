# Explanations, AP Macroeconomics Unit 1 Practice Set, in source order.
# o: a note for each wrong choice (Q: in the order of the data's wrong list; F: keyed by letter). steps: optional.
EX = [
    # 1 macroeconomic question
    dict(o=["is about the price in one market (avocados), a microeconomic question.",
            "is one firm's hiring decision, which is microeconomics.",
            "asks how a tax affects a single market, which is microeconomics.",
            "concerns one firm's pricing, not the economy as a whole."]),
    # 2 opportunity cost of a highway
    dict(o=["confuses who pays with what is given up: the resources still had other uses.",
            "makes the cost depend on how the project is financed; opportunity cost does not.",
            "adds up every alternative, but only the single best alternative is forgone.",
            "is the benefit of the highway, not the cost of building it."]),
    # 3 normative statement
    dict(o=["is a measured fact that can be checked against data.",
            "is a testable cause-and-effect claim, so it is positive.",
            "is a claim about what happened, which evidence can confirm or refute.",
            "describes past data, so it is positive."]),
    # 4 point inside the PPC
    dict(o=["is an outward shift of the curve, not a point inside it.",
            "places the economy on the curve, with all resources used.",
            "would be beyond the curve's sustainable output, not inside it.",
            "describes the bowed-out shape of the curve, not where the economy operates."]),
    # 5 outward shift of the PPC
    dict(o=["moves the economy from inside the curve toward it; the curve itself stays put.",
            "is a change in prices, which does not change how much the economy can produce.",
            "lowers spending and pushes the economy inside the curve; capacity is unchanged.",
            "is a move along today's curve; it shifts the curve only in the future, as the capital is used."]),
    # 6 more capital goods now
    dict(o=["reverses the result: more capital today means more capacity later.",
            "confuses choosing a different point on the curve with leaving resources idle.",
            "is about the shape of the curve (constant opportunity cost), not growth.",
            "ignores that A invests more, so A's capacity grows faster than B's."]),
    # 7 OC of one computer (F)
    dict(steps=["The straight-line PPC trades 40 computers for 80 tons of rice.",
                "One computer costs $80 \\div 40 = 2$ tons of rice."],
         o={"A": "is the opportunity cost of a ton of rice in computers ($40 \\div 80$), the inverse.",
            "B": "assumes a one-for-one trade-off, but the endpoints are 40 and 80.",
            "D": "is the maximum number of computers, not the cost of one.",
            "E": "is the maximum rice output, not the cost of one computer."}),
    # 8 comparative advantage in grain
    dict(steps=["Arvia: 1 grain costs $50/25 = 2$ cloth. Belor: 1 grain costs $30/30 = 1$ cloth.",
                "Belor gives up less cloth per ton of grain, so it has the comparative advantage in grain."],
         o=["names an absolute advantage in cloth, which does not decide comparative advantage in grain.",
            "gets the numbers backward: Arvia gives up 2 cloth per ton of grain, Belor only 1.",
            "is wrong on the facts (Arvia has the absolute advantage in cloth) and uses the wrong test.",
            "confuses absolute and comparative advantage; one country always has the lower opportunity cost."]),
    # 9 terms of trade (F)
    dict(steps=["Belor (grain) gives up 1 cloth per ton; Arvia would give up 2 cloth to make a ton itself.",
                "A price of grain strictly between 1 and 2 cloth benefits both: only 1.5 qualifies."],
         o={"A": "is below Belor's cost of 1 cloth per ton, so Belor would lose by exporting grain.",
            "B": "equals Belor's own opportunity cost, so Belor gains nothing.",
            "D": "equals Arvia's own opportunity cost, so Arvia gains nothing.",
            "E": "is above Arvia's cost of 2 cloth, so Arvia would rather make its own grain."}),
    # 10 gains from trade
    dict(o=["confuses production with consumption: each country still produces on its own curve.",
            "is impossible: specializing means producing less of some goods.",
            "is false: specializing still has opportunity costs; trade just lowers them.",
            "describes a zero-sum view, but trade by comparative advantage benefits both sides."]),
    # 11 complements: gasoline and SUVs
    dict(o=["is the effect for a substitute, not a complement.",
            "overlooks that the price of a related good is a demand shifter.",
            "is about the slope of demand, not a shift.",
            "has no basis; the complement's price rise reduces SUV demand."]),
    # 12 expected price rise
    dict(o=["reverses the effect: buyers move purchases forward when prices are expected to rise.",
            "ignores that expectations are a demand shifter.",
            "is about the slope of the curve, not a shift.",
            "describes a movement along demand after today's price rises; here only the expected price changed."]),
    # 13 higher wages, furniture
    dict(o=["reverses the effect: higher costs reduce supply.",
            "confuses the producers' costs with buyers' demand.",
            "treats a cost change as a demand shifter; wages paid by producers shift supply.",
            "would need a change in the price of furniture itself; an input cost shifts the curve."]),
    # 14 per-unit subsidy
    dict(o=["describes a tax or a cost increase, the opposite of a subsidy.",
            "pays producers, not buyers, so it shifts supply, not demand.",
            "gets the price wrong: more supply lowers the price and raises quantity.",
            "is backward: this subsidy is paid to producers and shifts supply."]),
    # 15 price above equilibrium
    dict(o=["occurs when the price is below equilibrium.",
            "pairs a surplus with the wrong price movement: sellers cut prices to clear it.",
            "pairs a shortage with a falling price; both parts are wrong here.",
            "holds only at the equilibrium price."]),
    # 16 supply and demand both decrease
    dict(o=["may happen, but it depends on which shift is larger.",
            "may happen, but it depends on which shift is larger.",
            "is the opposite: both decreases reduce quantity.",
            "claims the price must fall, but the price change is indeterminate."]),
    # 17 demand and supply both increase
    dict(o=["is possible, but it depends on the relative sizes of the shifts.",
            "is possible, but it depends on the relative sizes of the shifts.",
            "is the opposite: both increases raise quantity.",
            "claims a certain price rise, but the price change is indeterminate."]),
]
