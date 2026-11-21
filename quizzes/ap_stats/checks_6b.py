"""Numerical checks for Set B: every key answer and every distractor origin named in explanations.py."""
import math
import re
from statistics import NormalDist

from . import q_6b as Q
from .ex_6b import EX

LET = "ABCD"
Z = NormalDist()
r3 = lambda x: f"{x:.3f}"

key = dict(re.findall(r"(\d+) ([A-D])", Q.ANSWERS_ONLY))
assert len(key) == 18 and [q["n"] for q in Q.MC] == list(range(1, 19))
for q in Q.MC:
    assert key[str(q["n"])] == q["answer"], q["n"]
    assert len(q["options"]) == 4, q["n"]
    assert q["topic"] in Q.TOPICS


def opt(n):
    q = Q.MC[n - 1]
    return q["options"][LET.index(q["answer"])]


s5 = math.sqrt(0.18 * 0.82 / 80)
assert opt(5) == r3(1 - Z.cdf(round((0.25 - 0.18) / s5, 2)))
assert opt(6) == r3(0.40 + Z.inv_cdf(0.90) * math.sqrt(0.24 / 150))
assert max([0.10, 0.25, 0.40, 0.50], key=lambda p: p * (1 - p)) == float(opt(7))
s8 = math.sqrt(0.3 * 0.7 / 120 + 0.45 * 0.55 / 100)
assert opt(8) == f"0.15 and {s8:.3f}"
assert 0.20 * 40 < 10 and 40 <= 0.1 * 500 and 40 <= 0.1 * 450
s10 = math.sqrt(0.12 * 0.88 / 300 + 0.08 * 0.92 / 300)
assert opt(10) == r3(Z.cdf(-0.04 / s10))
assert opt(11) == r3(1 - Z.cdf(20 / (35 / math.sqrt(12))))
assert int(opt(14)) == math.ceil((20 / 2.5) ** 2)
assert opt(15) == r3(Z.cdf(1.5) - Z.cdf(-1))
assert opt(16) == r3(math.sqrt(100 / 25 + 100 / 25))
s18 = math.sqrt(1.2 ** 2 / 6 + 1.5 ** 2 / 8)
assert opt(18) == r3(1 - Z.cdf(0.6 / s18))
# FR 19
s19 = math.sqrt(0.85 * 0.15 / 200)
assert f"{s19:.4f}" == "0.0252"
assert f"{Z.cdf((0.79 - 0.85) / s19):.4f}" == "0.0087"
binom = sum(math.comb(200, k) * 0.85 ** k * 0.15 ** (200 - k) for k in range(159))
assert f"{binom:.4f}" == "0.0140", binom
# FR 20
assert f"{18 / math.sqrt(10):.2f}" == "5.69" and f"{24 / math.sqrt(40):.2f}" == "3.79"
s20 = math.sqrt(18 ** 2 / 10 + 24 ** 2 / 40)
assert f"{s20:.2f}" == "6.84" and f"{Z.cdf(-8 / 6.84):.3f}" == "0.121"
# distractor origins named in explanations.py
def mc(n, letter):
    return Q.MC[n - 1]["options"][LET.index(letter)]


P = lambda z: 1 - Z.cdf(z)
c = lambda lo, hi, m, s: Z.cdf((hi - m) / s) - Z.cdf((lo - m) / s)
assert mc(5, "B") == r3(P(0.07 / math.sqrt(0.25 * 0.75 / 80)))
assert mc(5, "C") == r3(P(0.07 / math.sqrt(0.18 * 0.82)))
assert mc(5, "D") == r3(Z.cdf(0.07 / s5))
assert mc(6, "A") == r3(0.40 - Z.inv_cdf(0.90) * 0.04)
assert mc(6, "C") == r3(0.40 + 1.645 * 0.04) and mc(6, "D") == r3(0.40 + 2 * 0.04)
a8, b8 = math.sqrt(0.3 * 0.7 / 120), math.sqrt(0.45 * 0.55 / 100)
assert (f"{a8:.4f}", f"{b8:.4f}") == ("0.0418", "0.0497") and mc(8, "D") == f"0.15 and {a8 + b8:.4f}"
assert mc(8, "C") == f"0.15 and {s8 ** 2:.4f}"
a10, b10 = math.sqrt(0.12 * 0.88 / 300), math.sqrt(0.08 * 0.92 / 300)
assert (f"{a10:.4f}", f"{b10:.4f}", f"{a10 + b10:.4f}") == ("0.0188", "0.0157", "0.0344")
assert mc(10, "B") == r3(Z.cdf(-0.04 / (a10 + b10))) and mc(10, "D") == r3(1 - Z.cdf(-0.04 / s10))
assert f"{s10 ** 2:.6f}" == "0.000597"
assert mc(11, "A") == r3(P((2400 - 2160) / 35)) and f"{240 / 35:.2f}" == "6.86"
assert mc(11, "C") == r3(P(20 / 35)) and f"{35 * math.sqrt(12):.1f}" == "121.2"
assert mc(11, "D") == r3(Z.cdf(20 / (35 / math.sqrt(12))))
assert int(mc(14, "D")) == 20 ** 2 / 2.5 and f"{20 / math.sqrt(30):.2f}" == "3.65"
assert mc(15, "A") == r3(c(26, 31, 28, 8)) and mc(15, "B") == r3(c(26, 31, 28, 4)) and mc(15, "C") == r3(c(-1, 1, 0, 1))
assert f"{Z.cdf(1.5):.4f}" == "0.9332" and f"{Z.cdf(-1):.4f}" == "0.1587"
a18, b18 = math.sqrt(1.2 ** 2 / 6), math.sqrt(1.5 ** 2 / 8)
assert (f"{a18:.3f}", f"{b18:.3f}", f"{a18 + b18:.3f}") == ("0.490", "0.530", "1.020")
assert mc(18, "B") == r3(P(0.6 / (a18 + b18))) and mc(18, "C") == r3(P(0.6 / math.sqrt(1.2 ** 2 + 1.5 ** 2)))
assert f"{math.sqrt(1.2 ** 2 + 1.5 ** 2):.2f}" == "1.92" and mc(18, "D") == r3(Z.cdf(0.6 / s18))
for q in Q.MC:
    e = EX[q["n"]]
    assert set(e["others"]) == set(LET) - {q["answer"]}, q["n"]
assert (f"{0.12 * 0.88 / 300:.6f}", f"{0.08 * 0.92 / 300:.6f}") == ("0.000352", "0.000245")
