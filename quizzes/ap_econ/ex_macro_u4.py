# Explanations, AP Macroeconomics Unit 4 Practice Set, in source order.
EX = [
    # 1 bond prices and interest rates
    dict(o=["reverses the inverse relationship between bond prices and market rates.",
            "ignores that an old bond with a lower fixed payment must get cheaper to compete with new bonds.",
            "invents an exception; prices of existing bonds of every maturity fall when rates rise.",
            "adds a condition that has no bearing on the inverse price–yield relationship."]),
    # 2 bond yield (F)
    dict(steps=["Interest $= \\$1{,}060 - \\$1{,}000 = \\$60$.",
                "Rate $= 60/1{,}000 = 6\\%$."],
         o={"A": "misplaces the decimal: $60/1{,}000$ is 0.06, which is 6\\%.",
            "C": "does not follow from the numbers: \\$60 earned on \\$1{,}000 is exactly 6\\%.",
            "D": "is too high: it would need a payment of \\$1{,}106 a year from now.",
            "E": "misplaces the decimal the other way."}),
    # 3 money vs bonds
    dict(o=["gets the return wrong: money earns little or nothing, which is the cost of holding it.",
            "reverses both: money is the most liquid asset and bonds pay more.",
            "gets liquidity wrong: money can be spent directly; bonds must be sold first.",
            "ignores the trade-off between liquidity and return."]),
    # 4 real interest rate (F)
    dict(steps=["Real rate $\\approx$ nominal rate $-$ inflation.",
                "$7\\% - 3\\% = 4\\%$."],
         o={"A": "subtracts in the wrong order ($3 - 7$).",
            "B": "divides the nominal rate by inflation ($7/3$).",
            "D": "adds inflation instead of subtracting it.",
            "E": "multiplies the two rates."}),
    # 5 unexpected inflation and a loan
    dict(o=["is backward: higher-than-expected inflation lowers the lender's real return.",
            "ignores that the real value of the fixed repayment falls.",
            "confuses nominal and real: the dollar repayment is unchanged, and it is worth less.",
            "cannot be: what the borrower gains in real terms, the lender loses."]),
    # 6 Fisher effect
    dict(o=["gets the direction wrong: lenders demand more to make up for money losing value.",
            "is wrong: market rates on loans respond to expected inflation.",
            "is not the mechanism; lenders raise the rate they charge.",
            "misses that nominal rates rise with expected inflation even if the real rate is unchanged."]),
    # 7 unit of account
    dict(o=["is money's use in paying for goods; listing prices is measuring value.",
            "is money's use in holding purchasing power over time.",
            "is a related use (pricing future payments), not posting today's prices.",
            "is a type of money, not a function of money."]),
    # 8 M1
    dict(o=["are a loan from the card issuer, not money held.",
            "are a financial asset, not money.",
            "are a financial asset, not money.",
            "are not in M1 (and large CDs are not in M2 either)."]),
    # 9 cash withdrawal
    dict(o=["counts the cash but forgets the deposits fall by the same amount.",
            "counts the fall in deposits but forgets the cash, which is also in M1.",
            "assumes a multiplier effect; no new reserves or loans are created.",
            "assumes a multiplier effect in the other direction; the money is just changing form."]),
    # 10 excess reserves (F)
    dict(steps=["Required reserves $= 0.20 \\times \\$1{,}000 = \\$200$.",
                "Excess reserves $= \\$300 - \\$200 = \\$100$, the most it can lend."],
         o={"A": "overlooks the \\$100 of reserves above the requirement.",
            "B": "takes 20\\% of the reserves ($0.2 \\times 300$) instead of 20\\% of deposits.",
            "D": "is the required reserves, which the bank must keep.",
            "E": "lends all reserves, ignoring the requirement."}),
    # 11 cash deposit (F)
    dict(steps=["Required reserves on the new deposit: $0.2 \\times 500 = \\$100$; excess $= \\$400$.",
                "Money multiplier $= 1/0.2 = 5$; new lending can create $400 \\times 5 = \\$2{,}000$."],
         o={"A": "is the required reserve on the deposit.",
            "B": "is only the first loan, with no further rounds.",
            "C": "is the deposit itself, which swaps currency for deposits and does not change M1.",
            "E": "applies the multiplier to the whole \\$500, but \\$100 must be held as reserves."}),
    # 12 open-market purchase (F)
    dict(steps=["The bank swaps a \\$1{,}000 bond for \\$1{,}000 of reserves; deposits do not change, so all of it is excess.",
                "Money multiplier $= 1/0.10 = 10$; $1{,}000 \\times 10 = \\$10{,}000$."],
         o={"A": "takes 10\\% of the purchase, the reserve ratio, not the multiplier.",
            "B": "treats the \\$1{,}000 as a deposit and lends only 90\\% of it once.",
            "C": "ignores the multiplier.",
            "D": "treats the purchase like a cash deposit, holding back 10\\%; a bond sale by a bank creates no new deposit to reserve against."}),
    # 13 smaller actual multiplier
    dict(o=["is false, and a lower reserve ratio would make the multiplier larger, not smaller.",
            "is the multiplier's assumption, which would give the full effect.",
            "has nothing to do with deposit creation by banks.",
            "is false: deposits are the largest part of M1."]),
    # 14 price level and money demand
    dict(o=["confuses money demand with money supply; the price level does not change the money supply.",
            "gets the direction wrong: higher prices mean more money is needed for transactions.",
            "puts the change on the wrong curve.",
            "ignores that money demand shifts even though supply is vertical."]),
    # 15 vertical money supply
    dict(o=["describes money demand, which slopes downward.",
            "is false; the curve is vertical because the quantity does not respond to the rate.",
            "is not the reason; it is about who sets the quantity.",
            "describes money demand, not money supply."]),
    # 16 more money supply
    dict(o=["reverses both effects.",
            "is inconsistent: lower interest rates mean higher bond prices.",
            "is inconsistent: higher rates mean lower bond prices, and the rate falls here.",
            "ignores that the new supply meets downward-sloping money demand at a lower rate."]),
    # 17 expansionary in limited reserves
    dict(o=["drains reserves: contractionary.",
            "cuts the money multiplier: contractionary.",
            "makes borrowing reserves dearer: contractionary.",
            "pays banks more to hold reserves rather than lend: contractionary."]),
    # 18 ample reserves, lower rate
    dict(o=["raises market rates, the opposite of the goal.",
            "is contractionary and does not set the policy rate in an ample-reserves system.",
            "raises the policy rate.",
            "has little effect: reserves are already ample, so a small purchase barely moves the rate."]),
    # 19 raising rates against inflation
    dict(o=["is the effect of lower rates.",
            "puts the effect on supply; higher rates work through demand.",
            "mixes a demand policy with a supply shift; the price level should fall, not rise.",
            "is inconsistent: higher rates reduce consumption and output."]),
    # 20 recessionary gap, monetary policy
    dict(o=["gets the price level wrong: AD shifts right along SRAS, so it rises.",
            "pairs a contractionary action with expansionary results.",
            "is contractionary (it drains reserves), so it cannot raise GDP.",
            "is contractionary: it cuts lending and AD."]),
    # 21 government borrowing
    dict(o=["puts the borrowing on the wrong side of the market and gets the rate wrong.",
            "gets the direction wrong: the government borrows more.",
            "names the nominal rate and the wrong direction; the real rate rises.",
            "pairs a supply increase with a higher rate, which cannot both follow from more saving."]),
    # 22 more saving
    dict(o=["describes a fall in supply.",
            "has the rate wrong: more supply lowers the price of borrowing.",
            "has the quantity wrong: more funds are lent at the lower rate.",
            "ignores the rightward shift of supply."]),
    # 23 investment tax credit
    dict(o=["puts the change on the savers' side.",
            "gets the direction wrong: investment is now more attractive.",
            "names a fall in saving, but the policy targets borrowers.",
            "ignores that firms want to borrow more at every rate."]),
]
