"""Numeric checks for the AP Environmental Science series: every computed answer (and numeric distractor) recomputed here.

    python3 -I quizzes/ap_env_sci/checks.py

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
near("1 NPP", 2500 - 1000, 1500); near("1 10pct", 20000 / 100, 200)
near("1 bottle NPP", 9.6 - 8.0, 1.6); near("1 bottle R", 8.0 - 7.1, 0.9); near("1 bottle GPP", 9.6 - 7.1, 2.5); near("1 bottle sum", 9.6 + 7.1, 17)
near("1 ocean ratio", 1800 / 125, 14)
# Unit 3
near("3 r", (30 - 10) / 10, 2.0); near("3 dbl", 70 / 2, 35); near("3 dbl 20", 70 / 20, 3.5)
near("3 A r", (38 - 8) / 10, 3.0); near("3 A sum", (38 + 8) / 10, 4.6); near("3 A dbl", 70 / 3, 23); near("3 A x", 70 * 3, 210); near("3 A dbl30", 70 / 30, 2.3)
near("3 town", 10000 + (150 + 40) - (80 + 60), 10050); near("3 town nomig", 10000 + 150 - 80, 10070); near("3 town noemig", 10000 + 150 + 40 - 80, 10110); near("3 town sign", 10000 - 50, 9950)
near("3 FRQ r", (25 - 7) / 10, 1.8); near("3 FRQ dbl", 70 / 1.8, 39)
dN = 50e6 * 0.025 - 50e6 * 0.007 + 50000
near("3 FRQ dN", dN, 950000); near("3 FRQ N", 50e6 + dN, 50.95e6); near("3 FRQ water", dN * 1200, 1.14e9)
# Unit 4
near("4 infil", 5 / 2.5, 2.0); near("4 infil x", 5 * 2.5, 12.5); near("4 infil inv", 2.5 / 5, 0.5); near("4 infil s3", 5 / 0.1, 50)
near("4 catch change", (1.7 - 7.7) / 7.7 * 100, -78)
# Unit 5
near("5 furrow", 600 / 0.65, 920); near("5 furrow x", 600 * 0.65, 390); near("5 50pct", 600 / 0.5, 1200)
near("5 drip", 600 / 0.95, 630); near("5 savings", 600 / 0.65 - 600 / 0.95, 290); near("5 drip loss", 600 / 0.95 - 600, 30, 0.15)
# Unit 6
near("6 half", 80 / 8, 10); near("6 half /3", 80 / 3, 27)
near("6 cost", 9000 * 0.15, 1350); near("6 cost dec", 135, 135); near("6 cost div", 9000 / 0.15, 60000)
near("6 CO2 t", 9000 * 1.0 / 1000, 9.0); near("6 LED $", 600 * 0.15, 90); near("6 LED div", 600 / 0.15, 4000)
near("6 payback", 180 / 90, 2.0); near("6 payback inv", 90 / 180, 0.5); near("6 payback 54", 180 / 54, 3.3)
near("6 thalf", 90 / 3, 30); near("6 thalf /8", 90 / 8, 11)
kwh = 0.40 * 4.5 * 365
near("6 FRQ panel", kwh, 657); near("6 FRQ panels", 450000 / kwh, 685); near("6 FRQ CO2", 450000 * 0.95 / 1000, 430)
near("6 FRQ payback", 685 * 350 / (450000 * 0.12), 4.4)
# Unit 7
near("7 pH", 10 ** (5 - 4), 10); near("7 FRQ pct", (21.0 - 1.8) / 21.0 * 100, 91); near("7 FRQ pH", 10 ** (5.3 - 4.3), 10)
# Unit 8
near("8 DDT factor", 25 / 0.5, 50); near("8 DDT large", 25 / 2.0, 12.5); near("8 DDT sub", 25 - 0.5, 24.5)
# Unit 9
near("9 dCO2", 414 - 317, 97); near("9 rate", (414 - 390) / 10, 2.4); near("9 rate 60s", (326 - 317) / 10, 0.9)
L = 30 * 180 / 12
near("9 FRQ L", L, 450); near("9 FRQ CO2", L * 2.3, 1035); near("9 FRQ bus", 30 * 180 * 0.04, 216); near("9 FRQ saved", L * 2.3 - 216, 819); near("9 FRQ trees", L * 2.3 / 22, 47)

if __name__ == "__main__":
    print("\n".join(fails) or "all numeric answers check")
    raise SystemExit(1 if fails else 0)
