# Explanations, AP Macroeconomics Unit 6 Practice Set, in source order.
EX = [
    # 1 current account (F)
    dict(steps=["Goods: $250 - 300 = -50$. Services: $80 - 50 = +30$.",
                "Add net investment income ($+10$) and net transfers ($-5$): $-50 + 30 + 10 - 5 = -\\$15$ billion."],
         o={"A": "counts only the goods balance.",
            "B": "stops at the balance of trade in goods and services, leaving out income and transfers.",
            "D": "adds the transfers instead of subtracting them ($-20 + 10 + 5$).",
            "E": "has the sign backward: imports exceed exports overall."}),
    # 2 factory abroad
    dict(o=["is a purchase of an asset, not a sale of goods or services.",
            "is a purchase of an asset, not of goods or services.",
            "has the direction wrong: U.S. money is going abroad to buy a foreign asset.",
            "is a one-way payment such as a gift or remittance; here the company gets an asset in return."]),
    # 3 foreign tourists
    dict(o=["has the direction wrong: foreigners are buying U.S. services.",
            "is about buying assets, not paying for hotel stays.",
            "is about buying assets, and the direction is wrong too.",
            "is a one-way payment; tourists receive services in return."]),
    # 4 current account deficit
    dict(o=["breaks the identity: the two balances must sum to zero.",
            "is about the government budget, which can be in deficit or surplus either way.",
            "does not follow; the currency can move either way.",
            "is unlikely and not required; a current account deficit usually comes with a trade deficit."]),
    # 5 inverse exchange rate (F)
    dict(steps=["If €1 $=$ \\$1.25, then \\$1 $= 1/1.25$ euros.",
                "$1/1.25 = 0.80$."],
         o={"A": "subtracts 1 from 1.25 instead of taking the reciprocal.",
            "B": "subtracts 1.25 from 2.",
            "D": "repeats the original rate instead of inverting it.",
            "E": "adds 1 to 1.25."}),
    # 6 appreciation
    dict(o=["reverses it: each dollar now buys more yen.",
            "is impossible between two currencies: if one buys more of the other, the other buys less.",
            "is impossible for the same reason.",
            "ignores that the dollar now buys 20 more yen."]),
    # 7 converting a price (F)
    dict(steps=["\\$1 buys €0.80, so €40 needs $40/0.80$ dollars.",
                "$40/0.80 = \\$50$."],
         o={"A": "multiplies by 0.80 instead of dividing.",
            "B": "ignores the exchange rate.",
            "C": "adds 20\\% instead of converting at the rate.",
            "E": "does not follow from the rate: €40 at €0.80 per dollar is \\$50."}),
    # 8 demand for dollars
    dict(o=["supplies dollars: Americans sell dollars to get foreign currency.",
            "is domestic borrowing, which does not by itself require foreign currency trades.",
            "supplies dollars, for the same reason.",
            "is not a foreign-exchange transaction."]),
    # 9 mirror market
    dict(o=["gets both effects backward: Europeans are selling euros to get dollars.",
            "gets both effects backward.",
            "is inconsistent: less demand for euros would lower their value.",
            "ignores that every dollar bought with euros is a euro supplied."]),
    # 10 axis label
    dict(o=["belongs on the horizontal axis.",
            "is upside down: the price of a peso is dollars per peso.",
            "belongs in a loanable funds or money market graph.",
            "is not a currency price."]),
    # 11 higher U.S. real rates
    dict(o=["mixes up the cause: the change is in financial flows, not goods prices.",
            "has no link to a rise in interest rates.",
            "names the wrong buyers: foreigners buy more U.S. assets.",
            "is false: capital flows also move exchange rates."]),
    # 12 U.S. income rises
    dict(o=["is wrong: foreign incomes did not change.",
            "has it backward: Americans supply more dollars to buy imports.",
            "pairs the wrong cause with the outcome.",
            "ignores the extra imports."]),
    # 13 high Canadian inflation
    dict(o=["is backward: Canadian goods get relatively more expensive.",
            "ignores the effect of relative prices on trade.",
            "gets the result backward: dearer Canadian goods lower demand for Canadian dollars.",
            "gets the reason wrong: it is Canadian goods that become relatively more expensive."]),
    # 14 Japanese buyers want U.S. cars
    dict(o=["names the wrong side: the Japanese demand dollars.",
            "is backward: the Japanese sell yen to buy dollars.",
            "is the opposite of the change.",
            "is backward: they supply more yen."]),
    # 15 dollar appreciates
    dict(o=["has the direction wrong: U.S. goods get dearer abroad.",
            "is inconsistent: lower net exports shift AD left.",
            "is inconsistent: higher net exports shift AD right.",
            "ignores the change in relative prices."]),
    # 16 who gains from depreciation
    dict(o=["lose: imports become more expensive.",
            "lose: foreign currency costs more.",
            "lose: imported inputs cost more.",
            "lose: tuition in foreign currency costs more."]),
    # 17 depreciation and AD
    dict(o=["is backward: net exports rise.",
            "puts the effect on supply; the main channel is AD.",
            "is unrelated: capacity does not change.",
            "ignores net exports, a component of AD."]),
    # 18 higher Australian real rates
    dict(o=["is backward: higher returns attract funds.",
            "is inconsistent: inflows raise demand for Australian dollars.",
            "is backward: a stronger currency reduces net exports.",
            "is backward: capital inflows add to loanable funds."]),
    # 19 capital inflow
    dict(o=["is backward: inflows add funds.",
            "puts the inflow on the wrong side of the market.",
            "puts the change on the borrowers' side.",
            "ignores the extra supply."]),
    # 20 rate hike, international channel
    dict(o=["is backward on the currency and on net exports.",
            "is inconsistent: a stronger dollar reduces net exports.",
            "is inconsistent: a weaker dollar would raise net exports.",
            "ignores capital flows toward higher U.S. rates."]),
]
