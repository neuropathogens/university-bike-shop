"""Numeric checks for the AP Biology series: every computed answer (and numeric distractor) recomputed here.

    python3 -I quizzes/ap_biology/checks.py

Each line recomputes a keyed value and compares it with the answer as printed (to its printed precision).
"""
import math

g = 9.8
k, e, h, c, R, kB, mu0, eps0, me = 9.0e9, 1.6e-19, 6.63e-34, 3.0e8, 8.31, 1.38e-23, 4 * math.pi * 1e-7, 8.85e-12, 9.11e-31
fails = []
sin, cos, rad, sqrt, pi = math.sin, math.cos, math.radians, math.sqrt, math.pi


def near(name, got, want, rel=0.03):
    if abs(got - want) > rel * abs(want) + 1e-12:
        fails.append(f"{name}: computed {got:.4g}, keyed {want}")


def fit(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    s = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return s, my - s * mx

# Unit 1
near("1 hydrolysis", 10 - 1, 9); near("1 dehydration", 50 - 1, 49); near("1 guanine", (100 - 2 * 30) / 2, 20)
# Unit 2
Rb = 0.0831
near("2 SA/V 1", 6 / 1, 6); near("2 SA/V 2", 6 / 2, 3)
near("2 psi 0.1", -0.1 * Rb * 295, -2.5); near("2 psi C", -0.1 * Rb * 22, -0.18); near("2 psi NaCl", -2 * 0.1 * Rb * 295, -4.9)
near("2 psi 0.2", -0.2 * Rb * 295, -4.9); near("2 psi 0.2 C", -0.2 * Rb * 22, -0.37)
iso = 0.2 + 0.2 * 7 / 10
near("2 FRQ iso", iso, 0.34); near("2 FRQ psi", -iso * Rb * 295, -8.3)
# Unit 4
near("4 mitosis", 40 / 200 * 20, 4.0); near("4 interphase", 160 / 200 * 20, 16); near("4 half", 0.1 * 20, 2.0); near("4 ratio", 200 / 40, 5.0)
# Unit 5
near("5 combos", 2 ** 23, 8.4e6); near("5 aabb", 1 / 16, 0.0625); near("5 three", (3 / 4) ** 3, 27 / 64)
near("5 recomb", (206 + 185) / 2300, 0.17); near("5 parental", (965 + 944) / 2300, 0.83)
obs, exp = [891, 302, 290, 117], [900, 300, 300, 100]
near("5 chi2", sum((o - e) ** 2 / e for o, e in zip(obs, exp)), 3.33, 0.01); near("5 total", sum(obs), 1600)
# Unit 6
near("6 PCR", 2 ** 10, 1024); near("6 lac fold", 980 / 2, 490)
# Unit 7
q = sqrt(0.09)
near("7 carriers", 2 * q * (1 - q), 0.42); near("7 p2", (1 - q) ** 2, 0.49)
q = sqrt(160 / 1000); p_ = 1 - q
near("7 q", q, 0.40); near("7 p", p_, 0.60); near("7 het", 2 * p_ * q * 1000, 480); near("7 pq", p_ * q * 1000, 240); near("7 BB", p_ ** 2 * 1000, 360)
near("7 FRQ 2pq", 2 * 0.47 * 0.53, 0.50)
# Unit 8
near("8 tertiary", 10000 / 1000, 10); near("8 secondary", 50000 / 100, 500)
near("8 dN/dt", 0.5 * 400 * (1000 - 400) / 1000, 120); near("8 exp", 0.5 * 400, 200); near("8 N/K", 0.5 * 400 * 400 / 1000, 80); near("8 K-N", 0.5 * 600, 300)
near("8 simpson", 1 - (0.5 ** 2 + 0.3 ** 2 + 0.2 ** 2), 0.62)
for t_, n in ((0, 20), (2, 62), (4, 165), (6, 335), (8, 484), (10, 560), (12, 587), (14, 596)):
    near(f"8 logistic t={t_}", 600 / (1 + 29 * math.exp(-0.6 * t_)), n, 0.01)
near("8 fastest t", math.log(29) / 0.6, 5.6)

if __name__ == "__main__":
    print("\n".join(fails) or "all numeric answers check")
    raise SystemExit(1 if fails else 0)
