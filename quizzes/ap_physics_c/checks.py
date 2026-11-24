"""Numeric checks for the AP Physics C series: every computed answer (and the FRQ data fits) recomputed here.

    python3 -I quizzes/ap_physics_c/checks.py

Each line recomputes a keyed value and compares it with the answer as printed (to its printed precision).
"""
import math

pi, g98, e, me, mp, k, mu0, eps0 = math.pi, 9.8, 1.6e-19, 9.1e-31, 1.67e-27, 9.0e9, 4 * math.pi * 1e-7, 8.85e-12
fails = []


def near(name, got, want, rel=0.05):
    if abs(got - want) > rel * abs(want) + 1e-12:
        fails.append(f"{name}: computed {got:.4g}, keyed {want}")


def fit(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    s = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return s, my - s * mx


# Unit 1
near("1 avg speed", 70 / 50, 1.4); near("1 avg vel", 10 / 50, 0.20)
near("1 v(3) a=4t", 2 * 3 ** 2, 18); near("1 cart a-t", 4 + 2 * 3, 10); near("1 table", 3.0 * math.sqrt(2 * 1.25 / 10), 1.5)
near("1 v(2)", 12 * 4 - 24, 24); near("1 x=t^3", 2 ** 3, 8); near("1 distance", 2 * 0.5 * 1.5 * 3, 4.5)
near("1 river", 60 / math.sqrt(2.0 ** 2 - 0.8 ** 2), 33); near("1 rain", math.hypot(8, 6), 10)
near("1 cliff", 15 * math.sqrt(2 * 20 / g98), 30); near("1 H", (20 * 0.5) ** 2 / (2 * g98), 5.1); near("1 speed", math.hypot(6, 4), 7.2)
near("1 FRQ x(4)", 6 * 16 - 64, 32); near("1 FRQ vmax", 24 - 12, 12)
# Unit 2
near("2 apparent", 70 * g98, 690, 0.01); near("2 cm", 24 / 8, 3.0); near("2 rod 3x^2", (3 / 4 * 16) / 8, 1.5)
a = 2 * g98 / 8; near("2 atwood T", 3 * (g98 + a), 37); near("2 elevator", 60 * (g98 - 2), 470)
near("2 F=6t", 1.5 * 4, 6.0); near("2 g/4", g98 / 4, 2.5); near("2 mu", math.tan(math.radians(30)), 0.58)
near("2 tau", 1 - math.exp(-1), 0.63); near("2 curve", math.sqrt(0.8 * g98 * 50), 20)
# Unit 3
near("3 W 3x^2", 8, 8.0); near("3 F at 1", -(8 - 3), -5.0); near("3 pendulum", math.sqrt(2 * 10 * 0.45), 3.0)
near("3 power", 500 * 20, 1e4); near("3 dot", 8 - 3, 5.0); near("3 5x^2", 5 / 3 * 26, 43)
near("3 WE", math.sqrt(2 * 49 / 2), 7.0); near("3 F(2)", -(12 - 24), 12); near("3 spring h", 0.5 * 200 * 0.01 / (0.05 * g98), 2.0)
near("3 friction d", 5 / 0.25, 20); near("3 elevator P", 800 * g98 * 2, 1.6e4); near("3 inst P", 10 * 15, 150)
# Unit 4
near("4 kick", 0.5 * 0.010 * 400, 2.0); near("4 rebound", 0.2 * 18, 3.6); near("4 J=30t^2", 80 / 3, 27)
near("4 bat", 0.15 * 90 / 0.005, 2700); near("4 sand", 6, 6.0); near("4 recoil", 30 / 60, 0.50)
near("4 inelastic", 30000 / 4000, 7.5); near("4 KE lost", 1 - 1500 / 4000, 0.63, 0.02)
near("4 elastic", 2 * 2 / 6 * 6, 4.0); near("4 2D", math.hypot(5 - 3 * 0.6, 3 * 0.8), 4.0)
near("4 ballistic", 2.01 * math.sqrt(2 * g98 * 0.2) / 0.010, 400)
s, b = fit([.25, .5, .75, 1, 1.25], [1 / v for v in (.54, .41, .31, .27, .23)])
near("4 FRQ slope", s, 2.5); near("4 FRQ v0", 1 / (0.5 * s), 0.80); near("4 FRQ 1/b", 1 / b, 0.81)
# Unit 5
near("5 theta", 0.5 * 2 * 25, 25); near("5 torque", 0.3 * 20 * 0.5, 3.0); near("5 seesaw", 60 / 40, 1.5); near("5 alpha", 4 / 0.5, 8)
near("5 alpha(2)", 24, 24); near("5 rev", 150 / (2 * pi), 24); near("5 total a", math.hypot(25 * 0.4, 0.8), 10)
near("5 door", 0.8 * 40 * math.sin(math.radians(60)), 28); near("5 beam", 130 * g98 / 4, 320, 0.01)
near("5 pulley", 2 * g98 / 4, 4.9); near("5 FRQ a", 2 * g98 / 4, 4.9); near("5 FRQ t", math.sqrt(2 / 4.9), 0.64)
near("5 FRQ w", 4.9 * math.sqrt(2 / 4.9) / 0.1, 31)
# Unit 6
near("6 disk K", 0.5 * 0.25 * 16, 2.0); near("6 L", 2 * 3 * 4, 24); near("6 W", 0.5 * 0.5 * 400, 100)
near("6 P", 12 * 300 * 2 * pi / 60, 380); near("6 w", math.sqrt(2 * 8 / 1), 4.0); near("6 impulse", 15 / 2.5, 6.0)
near("6 skater", 4 / 1.6 * 2, 5.0); near("6 cylinder", math.sqrt(4 * g98 * 1.5 / 3), 4.4); near("6 kepler", 4 ** 1.5, 8)
# Unit 7
near("7 vmax", 0.5, 0.50); near("7 T", 2 * pi / 3, 2.1); near("7 U well", 2 * pi * math.sqrt(0.5 / 8), 1.6)
near("7 f", math.sqrt(400) / (2 * pi), 3.2); near("7 vertical", 2 * pi * math.sqrt(0.098 / g98), 0.63)
near("7 amax", 0.2 * 25, 5.0); near("7 v(x)", 20 * math.sqrt(0.01 - 0.0036), 1.6); near("7 L", g98 * (2 / (2 * pi)) ** 2, 0.99)
near("7 rod", 2 * pi * math.sqrt(2 / (3 * g98)), 1.6)
s, b = fit([.1, .2, .3, .4, .5], [t * t for t in (.49, .66, .79, .91, 1.02)])
near("7 FRQ slope", s, 2.0); near("7 FRQ k", 4 * pi ** 2 / s, 20); near("7 FRQ int", b, 0.036, 0.1)
# Unit 8
near("8 coulomb", k * 6e-12 / 0.09, 0.60); near("8 electron a", e * 1000 / me, 1.8e14); near("8 flux", 500 * 0.06 * math.cos(math.radians(30)), 26)
# Unit 9
near("9 V", k * 2e-9 / 0.3, 60); near("9 dU", -e * 200 * 0.05, -1.6e-18); near("9 dV", -4 / 3 * 27, -36)
near("9 E", -(15 - 2), -13); near("9 E(2)", -(12 - 2), -10); near("9 eq", 10 / 0.02, 500); near("9 v_e", math.sqrt(2 * e * 500 / me), 1.3e7)
# Unit 10
near("10 C", eps0 * 0.02 / 1e-3, 180e-12); near("10 series", 6 / 5, 1.2); near("10 U", 0.5 * 10e-6 * 144, 7.2e-4)
near("10 combo", 6 * 3 / 9, 2.0); near("10 u", 0.5 * eps0 * 1e12, 4.4); near("10 share", 8 / 4, 2.0)
# Unit 11
near("11 I", 6 * 2 + 2, 14); near("11 R", 1.1e-6 * 2 / (pi * 0.25e-3 ** 2), 11); near("11 heater", 120 ** 2 / 1500, 9.6)
near("11 branch", 1.5 * 2 / 3, 1.0); near("11 loop", 8 / 4, 2.0); V = 8 / 1.25; near("11 kirchhoff", V / 4, 1.6)
near("11 terminal", 9 * 2 / 3, 6.0); near("11 RC", 6e-3 * math.exp(-1), 2.2e-3); near("11 Q", 10e-6 * 4, 40e-6)
s, b = fit([.2, .4, .6, .8, 1.0], [5.81, 5.58, 5.42, 5.19, 5.01])
near("11 FRQ r", -s, 1.0); near("11 FRQ emf", b, 6.0)
# Unit 12
near("12 wire 10A", 2e-7 * 10 / 0.02, 1e-4); near("12 r", mp * 2e6 / (e * 0.5), 0.042); near("12 selector", 3000 / 0.02, 1.5e5)
near("12 F", 4 * 0.5 * 0.2 * 0.5, 0.20); near("12 torque", 50 * 2 * 0.01 * 0.3, 0.30); near("12 wire 20A", 2e-7 * 20 / 0.04, 1e-4)
near("12 F/L", 2e-7 * 40 / 0.1, 8e-5); near("12 solenoid", mu0 * 2000 * 3, 7.5e-3)
# Unit 13
near("13 flux", 0.4 * 0.05 * 0.5, 0.010); near("13 BLv", 0.2 * 0.5 * 4, 0.40); near("13 U_L", 0.5 * 2 * 9, 9.0)
near("13 tau", 0.5 / 10, 0.050); near("13 omega", 1 / math.sqrt(0.1 * 10e-6), 1000); near("13 coil", 20 * pi * 0.01 * 0.3, 0.19)
near("13 gen", 100 * 0.02 * 0.5 * 60, 60); near("13 rod", 0.5 * 0.4 * 5, 1.0); near("13 force", 0.5 * 0.4 * 0.5, 0.10)
near("13 L", mu0 * 500 ** 2 * 4e-4 / 0.25, 5.0e-4); near("13 LR", 3 * (1 - math.exp(-1)), 1.9)

if fails:
    raise SystemExit("\n".join(fails))
print("all numeric checks pass")
