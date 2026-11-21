"""Numerical checks for Set C: every key answer, FR value, and distractor origin named in explanations.py."""
import itertools
import math
from statistics import NormalDist

from . import q_6c as Q

LET = "ABCD"
Z = NormalDist()
r3 = lambda x: f"{x:.3f}"
P = lambda z: 1 - Z.cdf(z)
ncdf = lambda lo, hi, m, s: NormalDist(m, s).cdf(hi) - NormalDist(m, s).cdf(lo)


def mc(n, letter):
    return Q.MC[n - 1]["options"][LET.index(letter)]


# Q1: sample maximum over all six samples of size 2
pop = [2, 4, 6, 8]
maxima = [max(s) for s in itertools.combinations(pop, 2)]
assert maxima == [4, 6, 8, 6, 8, 8] and sum(maxima) == 40
assert mc(1, "C") == f"{sum(maxima) / 6:.2f}" and mc(1, "A") == f"{sum(pop) / 4:.2f}"
assert mc(1, "B") == f"{sum(set(maxima)) / 3:.2f}" and mc(1, "D") == f"{max(pop):.2f}"
# Q5
assert 100 * 0.92 >= 10 and round(100 * 0.08) == 8
# Q6
s6 = math.sqrt(0.45 * 0.55 / 600)
assert f"{s6:.4f}" == "0.0203" and f"{0.03 / s6:.2f}" == "1.48"
assert mc(6, "B") == r3(2 * Z.cdf(0.03 / s6) - 1) == r3(ncdf(0.42, 0.48, 0.45, 0.02031))
assert r3(2 * Z.cdf(1.48) - 1) == "0.861"
assert mc(6, "A") == r3(Z.cdf(0.03 / s6) - 0.5) and mc(6, "C") == r3(Z.cdf(0.03 / s6))
assert 0.03 / s6 < 1.96
# Q7
s7 = math.sqrt(0.2 * 0.8 / 250)
assert f"{s7:.4f}" == "0.0253" and f"{0.04 / s7:.2f}" == "1.58" and 60 / 250 == 0.24
assert mc(7, "A") == r3(P(0.04 / s7)) == r3(1 - NormalDist(0.2, 0.0253).cdf(0.24)) == r3(P(1.58))
assert f"{math.sqrt(40):.2f}" == "6.32" and f"{10 / math.sqrt(40):.2f}" == "1.58"
assert f"{math.sqrt(0.2 / 250):.4f}" == "0.0283" and f"{math.sqrt(50):.2f}" == "7.07"
assert mc(7, "B") == r3(P(0.04 / math.sqrt(0.2 / 250))) and f"{0.04 / math.sqrt(0.2 / 250):.2f}" == "1.41"
assert mc(7, "C") == r3(P(10 / 40)) and mc(7, "D") == r3(Z.cdf(0.04 / s7))
# Q10
v10 = (0.48 * 0.52 / 200, 0.40 * 0.60 / 200)
assert (f"{v10[0]:.6f}", f"{v10[1]:.4f}", f"{sum(v10):.6f}") == ("0.001248", "0.0012", "0.002448")
s10 = math.sqrt(sum(v10))
assert f"{s10:.4f}" == "0.0495" and f"{0.07 / s10:.2f}" == "1.41"
assert mc(10, "B") == r3(P(0.07 / s10)) == r3(1 - NormalDist(0.08, 0.0495).cdf(0.15))
assert mc(10, "A") == r3(P(0.15 / s10)) and f"{0.15 / s10:.2f}" == "3.03"
a10, b10 = (math.sqrt(v) for v in v10)
assert (f"{a10:.5f}", f"{b10:.5f}", f"{a10 + b10:.4f}") == ("0.03533", "0.03464", "0.0700")
assert mc(10, "C") == r3(P(0.07 / (a10 + b10))) and f"{0.07 / (a10 + b10):.2f}" == "1.00"
assert mc(10, "D") == r3(Z.cdf(0.07 / s10))
# Q12
assert mc(12, "A") == r3(Z.cdf((85 - 94) / (40 / 8))) and mc(12, "B") == r3(Z.cdf((85 - 94) / 40))
assert mc(12, "C") == r3(P((85 - 94) / 5))
# Q13
assert mc(13, "D").endswith(r3(P((530 - 500) / 20)) + "$") and mc(13, "C").endswith(r3(P(30 / 100)) + "$")
assert 1 / P(1.5) < 16 and 1 / P(1.5) > 14
# Q14
z95, z975 = Z.inv_cdf(0.95), Z.inv_cdf(0.975)
assert mc(14, "B") == f"{72 + z95 * 2:.2f}" and mc(14, "A") == f"{72 - z95 * 2:.2f}"
assert mc(14, "C") == f"{72 + z975 * 2:.2f}" and mc(14, "D") == f"{72 + z95 * 6:.2f}"
# Q17
assert (4.2 ** 2, round(4.2 ** 2 / 36, 10), 9 / 25) == (17.64, 0.49, 0.36)
assert mc(17, "C") == r3(math.sqrt(0.85)) and mc(17, "A") == r3(math.sqrt(0.13))
assert mc(17, "B") == r3(0.85) and mc(17, "D") == r3(4.2 / 6 + 3.0 / 5)
# Q18
s18 = math.sqrt(36 / 9 + 81 / 9)
assert f"{s18:.3f}" == "3.606" and f"{5 / s18:.2f}" == "1.39" and f"{10 / s18:.2f}" == "2.77"
assert mc(18, "B") == r3(P(5 / s18)) == r3(1 - NormalDist(5, 3.606).cdf(10)) and r3(P(1.39)) == "0.082"
assert mc(18, "A") == r3(P(10 / s18)) and mc(18, "C") == r3(P((10 - 5) / (6 / 3 + 9 / 3)))
assert mc(18, "D") == r3(Z.cdf(5 / s18))
# FR 19
s19 = 3.0 / math.sqrt(40)
assert f"{s19:.3f}" == "0.474" and f"{0.3 / s19:.2f}" == "0.63" and 180 / 40 == 4.5
assert r3(P(0.3 / s19)) == "0.264" == r3(P(0.63)) == r3(1 - NormalDist(4.2, 0.4743).cdf(4.5))
assert r3(1 - NormalDist(4.2, 0.474).cdf(4.5)) == "0.263"
assert f"{math.sqrt(40) * 3:.2f}" == "18.97" and r3(1 - NormalDist(168, math.sqrt(40) * 3).cdf(180)) == "0.264"
assert r3(P(0.3 / 3.0)) == "0.460" and r3(Z.cdf(0.3 / s19)) == "0.736"
# FR 20
v20 = (0.30 * 0.70 / 150, 0.22 * 0.78 / 120)
assert (f"{v20[0]:.5f}", f"{v20[1]:.5f}") == ("0.00140", "0.00143")
s20 = math.sqrt(sum(v20))
assert f"{s20:.4f}" == "0.0532" and f"{-0.1 / s20:.2f}" == "-1.88"
assert r3(Z.cdf(-0.1 / s20)) == "0.030" == r3(NormalDist(0.08, 0.0532).cdf(-0.02)) and r3(P(-0.1 / s20)) == "0.970"
assert min(150 * 0.30, 150 * 0.70, 120 * 0.22, 120 * 0.78) >= 10
print("Set C numeric checks passed")
