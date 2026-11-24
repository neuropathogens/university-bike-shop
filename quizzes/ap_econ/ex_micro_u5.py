# Explanations, AP Microeconomics Unit 5 Practice Set, in source order.
EX = [
    # 1 derived demand
    dict(o=["confuses demand with supply.",
            "is not what “derived” means; wage laws are a separate issue.",
            "ignores the link to the product: the wage is only the price on the axis.",
            "is too strong: labor demand depends on bread demand but is not the same thing."]),
    # 2 MRP (F)
    dict(steps=["$MRP = MP \\times P$ for a price taker.",
                "$10 \\times \\$6 = \\$60$."],
         o={"A": "is the marginal product in units, not dollars.",
            "B": "adds MP and price instead of multiplying.",
            "C": "uses the wrong numbers; MP is 10, not 6.",
            "E": "multiplies by 3, the worker's position, as well."}),
    # 3 hiring rule (F)
    dict(steps=["$MRP = MP \\times \\$5$: \\$70, \\$60, \\$50, \\$40, \\$30.",
                "Hire while $MRP \\ge \\$45$: the third worker (\\$50) yes, the fourth (\\$40) no."],
         o={"A": "stops while workers 2 and 3 still add more than they cost.",
            "B": "stops while worker 3 still adds \\$50 against a \\$45 wage.",
            "D": "hires a worker whose MRP (\\$40) is below the wage.",
            "E": "hires two workers whose MRP is below the wage."}),
    # 4 MRP = MFC
    dict(o=["compares units with dollars; MP must be valued at its revenue.",
            "would mean hiring workers who add almost nothing.",
            "is not a profit-maximizing condition.",
            "would mean hiring workers whose cost exceeds what they add."]),
    # 5 monopolist's MRP
    dict(o=["reverses the order: $MR < P$, so $MP \\times MR$ is the lower curve.",
            "describes the supply of labor to a competitive firm.",
            "confuses demand for labor with supply.",
            "is wrong: diminishing returns and falling MR make it slope down."]),
    # 6 product demand rises
    dict(o=["puts the change on the wrong side of the market.",
            "has the direction wrong: higher product demand raises MRP.",
            "is inconsistent: more demand raises both wage and employment.",
            "ignores that higher MRP shifts labor demand."]),
    # 7 alternative occupation pays more
    dict(o=["mixes up the markets: the higher wage is for nurses.",
            "ignores that workers can move between occupations.",
            "puts the change on the demand side.",
            "has the cause wrong: the supply shift happens because nurses' pay rose."]),
    # 8 cheaper substitute input
    dict(o=["holds for a complementary input.",
            "ignores the substitution of machines for cashiers.",
            "is not the effect of a cheaper substitute.",
            "is not the expected effect."]),
    # 9 movement along labor demand
    dict(o=["raises MRP: a shift.",
            "raises MP and MRP: a shift.",
            "raises MP of labor: a shift.",
            "lowers the product price and MRP: a shift."]),
    # 10 least-cost combination
    dict(steps=["$MP_L/W = 30/10 = 3$ units per dollar; $MP_K/r = 40/20 = 2$.",
                "Labor gives more output per dollar: use more labor and less capital."],
         o=["is backward: capital gives less per dollar.",
            "would raise output and cost, not lower the cost of this output.",
            "would cut output below the target.",
            "is wrong: the ratios are not equal."]),
    # 11 profit-maximizing input use
    dict(steps=["Labor: $MRP_L/W = 30/20 = 1.5 > 1$, so hiring more adds profit.",
                "Capital: $MRP_K/r = 40/40 = 1$, already at its profit-maximizing level."],
         o=["is wrong: capital is already right, and labor should rise.",
            "is backward: the last worker adds more than he costs.",
            "is wrong: labor should rise.",
            "ignores that $MRP_L > W$."]),
    # 12 competitive firm's labor supply
    dict(o=["would mean no one would work for a higher wage.",
            "describes a monopsonist.",
            "describes the market, not one firm.",
            "is not a supply curve."]),
    # 13 immigration
    dict(o=["has both effects backward.",
            "gets employment wrong: a lower wage means more hiring.",
            "ignores the fall in the market wage.",
            "has the wage backward."]),
    # 14 monopsony MFC
    dict(o=["describes a competitive employer.",
            "is backward: the raise to existing workers makes MFC higher.",
            "holds only at the chosen employment level.",
            "describes a competitive employer."]),
    # 15 monopsony hiring (F)
    dict(steps=["Total labor cost: $10, 22, 36, 52, 70$, so MFC is $10, 12, 14, 16, 18$.",
                "Hire while $MRP \\ge MFC$: worker 3 ($18 \\ge 14$) yes, worker 4 ($15 < 16$) no.",
                "Pay the supply-curve wage for 3 workers: \\$12."],
         o={"B": "pays the MFC (\\$14) instead of the supply-curve wage.",
            "C": "is the competitive outcome, where supply meets MRP.",
            "D": "hires a fourth worker whose MRP (\\$15) is below the MFC (\\$16).",
            "E": "hires workers whose MRP is below their MFC."}),
    # 16 monopsony vs competition
    dict(o=["is backward.",
            "gets the wage wrong.",
            "gets employment wrong.",
            "gets employment wrong: the monopsony hires fewer."]),
    # 17 minimum wage in monopsony
    dict(o=["holds in a competitive market, not here.",
            "ignores that the floor makes MFC flat over a range.",
            "is wrong: hiring stays profitable.",
            "is wrong: the firm pays the minimum."]),
]
