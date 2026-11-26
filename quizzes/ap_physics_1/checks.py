"""Numeric checks for the AP Physics 1 series: every computed answer recomputed here.

    python3 -I quizzes/ap_physics_1/checks.py

Each line recomputes a keyed value and compares it with the answer as printed (to its printed precision).
"""
import math

g = 9.8
fails = []
sin, cos, rad, sqrt = math.sin, math.cos, math.radians, math.sqrt


def near(name, got, want, rel=0.03):
    if abs(got - want) > rel * abs(want) + 1e-12:
        fails.append(f"{name}: computed {got:.4g}, keyed {want}")


# Unit 1
near("1 jog speed", 170 / 85, 2.0); near("1 jog vel", 70 / 85, 0.82)
near("1 car x", 0.5 * (24 / 8) * 8 ** 2, 96); near("1 car x no sq", 0.5 * 3 * 8, 12); near("1 car x v0", 24 * 8 + 96, 288)
near("1 drop v", sqrt(2 * g * 20), 20); near("1 drop no2", sqrt(g * 20), 14); near("1 drop t", sqrt(2 * 20 / g), 2.0)
near("1 bike", 16 + 48 + 8, 72); near("1 boat", math.hypot(4, 3), 5.0)
near("1 table t", sqrt(2 * 1.25 / g), 0.51); near("1 table x", 2.0 * sqrt(2 * 1.25 / g), 1.0)
near("1 top", 20 * cos(rad(30)), 17); near("1 top vy", 20 * sin(rad(30)), 10)
near("1 train a", (10 ** 2 - 30 ** 2) / (2 * 400), -1.0); near("1 train no2", -800 / 400, -2.0); near("1 train vf0", -30 ** 2 / 800, -1.1)
near("1 avg speed", 120 / 3, 40)
near("1 cart a", 6 / 2, 3.0); near("1 cart x8", 6 + 24 + 6, 36); near("1 cart avg", (36 - 4) / 10, 3.2); near("1 cart wrong", 36 / 10, 3.6)
near("1 rain", math.hypot(8, 6), 10)
vy, vx = 25 * 0.8, 25 * 0.6
near("1 flight", 2 * vy / g, 4.1); near("1 flight top", vy / g, 2.0); near("1 flight vx", 2 * vx / g, 3.1); near("1 flight v", 2 * 25 / g, 5.1)
near("1 range", vx * 2 * vy / g, 61); near("1 range vy", vy * 2 * vy / g, 82); near("1 range top", vx * vy / g, 31); near("1 range v", 25 * 2 * vy / g, 102)
# Unit 2
near("2 cm", 24 / 8, 3.0); near("2 elevator", 60 * (g + 2), 710); near("2 elev down", 60 * (g - 2), 470); near("2 elev ma", 120, 120)
near("2 string", 2 * 10 / 5, 4.0); near("2 static max", 0.4 * 5 * g, 19.6); near("2 kinetic", 0.3 * 5 * g, 14.7)
near("2 spring", 0.5 * g / 40, 0.12); near("2 spring m/k", 0.5 / 40, 0.0125); near("2 spring k/w", 40 / (0.5 * g), 8.2)
near("2 curve 50", sqrt(0.6 * g * 50), 17); near("2 curve no mu", sqrt(g * 50), 22); near("2 curve no g", sqrt(0.6 * 50), 5.5)
near("2 plank cm", (4 * 1.5 + 2 * 3) / 6, 2.0)
a = 1 * g / 4
near("2 pulley a", a, 2.5); near("2 pulley mg/M", g / 3, 3.3); near("2 atwood", 2 * g / 4, 4.9)
near("2 tension", 3 * a, 7.4); near("2 net hang", g - 3 * a, 2.5); near("2 Mg", 3 * g, 29); near("2 doubled", 2 * g / 5, 3.9)
near("2 planet", g * 2 / 4, 4.9); near("2 ramp", 2 * g * 0.5, 9.8); near("2 ramp cos", 2 * g * cos(rad(30)), 17)
near("2 box", 50 / (0.25 * g), 20); near("2 box w", 50 / g, 5.1); near("2 box mu", 50 * 0.25, 12.5)  # printed as the distractor 13
near("2 k", 8 / 0.2, 40); near("2 hill ac", 15 ** 2 / 40, 5.6); near("2 loop min", sqrt(g * 40), 20)
near("2 curve 80", sqrt(0.5 * g * 80), 20); near("2 curve80 no mu", sqrt(g * 80), 28); near("2 curve80 no g", sqrt(0.5 * 80), 6.3); near("2 curve80 half", sqrt(0.5 * g * 40), 14)
mu = (30 - 4 * g * 0.5) / (4 * g * cos(rad(30)))
near("2 FRQ mu", mu, 0.31); near("2 FRQ decel", g * 0.5 + mu * g * cos(rad(30)), 7.5)
# Unit 3
near("3 K ratio", (40 / 20) ** 2, 4); near("3 K1", 0.5 * 1200 * 400, 2.4e5); near("3 K2", 0.5 * 1200 * 1600, 9.6e5)
near("3 sled rope", 50 * 0.8 * 10, 400); near("3 sled sin", 50 * 0.6 * 10, 300); near("3 F-x", 0.5 * 2 * 10 + 3 * 10, 40)
near("3 Us", 0.5 * 200 * 0.1 ** 2, 1.0); near("3 Us k dx", 200 * 0.1, 20); near("3 Us no sq", 0.5 * 200 * 0.1, 10)
near("3 pendulum", sqrt(2 * g * 0.45), 3.0); near("3 pend 2gh", 2 * g * 0.45, 8.8); near("3 pend gh", sqrt(g * 0.45), 2.1); near("3 pend gh2", g * 0.45, 4.4)
near("3 sled mgh", 20 * g * 5, 980); near("3 sled K", 0.5 * 20 * 64, 640); near("3 sled th", 980 - 640, 340)
near("3 motor", 50 * g * 2, 980); near("3 motor K", 0.5 * 50 * 4, 100); near("3 motor mg/v", 50 * g / 2, 250); near("3 motor mg", 50 * g, 490)
near("3 ball W", 0.5 * 0.15 * (400 - 100), 23); near("3 ball dv", 0.5 * 0.15 * 100, 7.5); near("3 ball Kf", 0.5 * 0.15 * 400, 30); near("3 ball p", 0.15 * 10, 1.5)
near("3 stop F", 0.5 * 2 * 36 / 3, 12); near("3 stop p", 2 * 6 / 3, 4.0); near("3 stop F*d", 36 * 3, 108)
near("3 graph W", 8 + 16 + 8, 32); near("3 graph v", sqrt(2 * 32 / 2), 5.7); near("3 graph no half", sqrt(32 / 2), 4.0); near("3 graph m in", sqrt(2 * 32 * 2 / 1) / 1, 11.3); near("3 graph a", 8 / 2, 4.0)
near("3 launcher", 0.5 * 400 * 0.01 / (0.05 * g), 4.1); near("3 launch no half", 400 * 0.01 / (0.05 * g), 8.2); near("3 launch no g", 2.0 / 0.05, 40); near("3 launch kx", 40 / (0.05 * g), 82)
near("3 coaster", sqrt(2 * g * 15), 17); near("3 coaster 5", sqrt(2 * g * 5), 9.9); near("3 coaster 20", sqrt(2 * g * 20), 20); near("3 coaster 25", sqrt(2 * g * 25), 22)
near("3 slide th", 30 * g * 4 - 0.5 * 30 * 36, 640); near("3 slide mgh", 30 * g * 4, 1200); near("3 slide sum", 1176 + 540, 1700)
near("3 elevator", 500 * g * 2, 9800); near("3 elev K", 0.5 * 500 * 4, 1000); near("3 elev mg/v", 500 * g / 2, 2500)
near("3 car drag", 30000 / 20, 1500); near("3 car Pv", 30000 * 20, 6.0e5)
# Unit 4
near("4 ball p", 0.15 * 40, 6.0); near("4 runner p", 60 * 0.1, 6.0)
near("4 wall F", 0.5 * 10 / 0.02, 250); near("4 wall dv", 0.5 * 2 / 0.02, 50); near("4 wall vf", 0.5 * 4 / 0.02, 100); near("4 wall J", 0.5 * 10, 5.0)
near("4 racket v", 0.5 * 0.010 * 1200 / 0.12, 50); near("4 racket no half", 0.010 * 1200 / 0.12, 100); near("4 racket J*m", 6 * 0.12, 0.72)
near("4 skaters", 40 * 3 / 60, 2.0); near("4 skaters inv", 60 * 3 / 40, 4.5)
near("4 stick v", 6 / 3, 2.0); near("4 stick dK", 0.5 * 2 * 9 - 0.5 * 3 * 4, 3.0)
near("4 bat", 0.2 * 40 / 0.005, 1600); near("4 bat sub", 0.2 * 10 / 0.005, 400); near("4 bat vf", 0.2 * 25 / 0.005, 1000)
near("4 impulse v", 10 * 3 / 2, 15); near("4 impulse a", 10 / 2, 5.0)
J = 0.5 * 0.008 * 800
near("4 kick J", J, 3.2); near("4 kick v", J / 0.4, 8.0); near("4 kick v*m", J * 0.4, 1.3); near("4 kick no half", 2 * J / 0.4, 16); near("4 kick half", J / 2 / 0.4, 4.0)
near("4 kick F", J / 0.008, 400); near("4 kick F 2t", J / 0.016, 200)
near("4 throw", 2 * 10 / 50, 0.40); near("4 throw inv", 50 * 10 / 2, 250)
near("4 crash v", 20000 / 2500, 8.0); near("4 crash 1500", 20000 / 1500, 13); near("4 crash Ki", 0.5 * 1000 * 400, 2.0e5); near("4 crash Kf", 0.5 * 2500 * 64, 8.0e4); near("4 crash dK", 2.0e5 - 8.0e4, 1.2e5)
near("4 elastic p", -2 + 6, 4.0); near("4 elastic K", 0.5 * 4 + 0.5 * 3 * 4, 8.0)
xs, ys = [0.25, 0.5, 0.75, 1.0, 1.5], [1 / r for r in (0.66, 0.51, 0.40, 0.34, 0.25)]
for got, want in zip(ys, (1.52, 1.96, 2.50, 2.94, 4.00)):
    near("4 FRQ vi/vf", got, want, 0.005)
mx, my = sum(xs) / 5, sum(ys) / 5
s = sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
near("4 FRQ slope", s, 2.0); near("4 FRQ intercept", my - s * mx, 1.0); near("4 FRQ K ratio", (1.0 / 0.5) * 0.51 ** 2, 0.52)
# Unit 5
near("5 wheel dtheta", 0.5 * 3 * 16, 24); near("5 wheel 48", 12 * 4, 48)
near("5 wrench", 0.25 * 40 * 0.5, 5.0); near("5 wrench cos", 0.25 * 40 * cos(rad(30)), 8.7); near("5 wrench perp", 0.25 * 40, 10); near("5 wrench F/r", 40 / 0.25, 160)
near("5 rod end", 2 * 1 ** 2, 2.0); near("5 rod center", 2 * 2 * 0.5 ** 2, 1.0); near("5 rod both", 2 * 2 * 1, 4.0); near("5 rod half", 2 * 0.25, 0.50)
near("5 seesaw", 30 * 2 / 40, 1.5); near("5 seesaw inv", 40 * 2 / 30, 2.7)
near("5 alpha", 2 / 0.5, 4.0)
near("5 fan", 0.5 * 30 * 6, 90); near("5 fan alpha", 30 / 6, 5.0)
near("5 turntable", 33 * 2 * math.pi / 60, 3.5); near("5 rev/s", 33 / 60, 0.55); near("5 rad/min", 33 * 2 * math.pi, 207)
near("5 at", 0.3 * 4, 1.2); near("5 at div", 4 / 0.3, 13); near("5 r/alpha", 0.3 / 4, 0.075)
near("5 beam torque", 10 * g * 2, 196); near("5 beam far", 10 * g * 4, 392); near("5 beam half", 10 * g * 0.5, 49)
T = (10 * g * 2 + 20 * g * 1) / 4
near("5 cable", T, 98); near("5 total w", 30 * g, 294); near("5 half w", 15 * g, 147); near("5 hinge", 30 * g - T, 196)
near("5 rod2 end", 1 * 2 ** 2, 4.0); near("5 rod2 center", 2 * 1 * 1 ** 2, 2.0); near("5 rod2 both", 2 * 1 * 4, 8.0)
I = 0.5 * 2 * 0.1 ** 2
near("5 pulley", 4 * 0.1 / I, 40); near("5 pulley hoop", 4 * 0.1 / (2 * 0.01), 20); near("5 pulley F/I", 4 / I, 400); near("5 pulley F/M", 4 / 2, 2.0)
# Unit 6
near("6 Krot", 0.5 * 0.2 * 100, 10); near("6 Iw", 0.2 * 10, 2.0); near("6 Iw half", 0.5 * 0.2 * 10, 1.0)
near("6 work w", sqrt(2 * 5 * 4 / 0.1), 20); near("6 work no root", 2 * 20 / 0.1, 400); near("6 work no 2", sqrt(20 / 0.1), 14); near("6 W/I", 20 / 0.1, 200)
near("6 ang impulse", 3 * 2 / 0.5, 12); near("6 L*I", 6 * 0.5, 3.0); near("6 tau/t", 3 / 2, 1.5)
near("6 skater", 4 * 2 / 1.6, 5.0); near("6 skater inv", 1.6 * 2 / 4, 0.80); near("6 skater K", 2 * sqrt(4 / 1.6), 3.2)
near("6 roll K", 0.5 * 3 * 4 + 0.25 * 3 * 4, 9.0); near("6 roll hoop", 3 * 4, 12)
near("6 flywheel", 0.5 * 2 * 900, 900); near("6 fly Iw", 2 * 30, 60); near("6 fly stop", 900 / 15, 60); near("6 fly time", 60 / 15, 4.0)
near("6 motor", sqrt(2 * 8 * 2 * math.pi / 0.5), 14); near("6 motor 1rad", sqrt(2 * 8 / 0.5), 5.7); near("6 motor noroot", 2 * 8 * 2 * math.pi / 0.5, 200); near("6 motor no2", sqrt(8 * 2 * math.pi / 0.5), 10)
near("6 stool", 3 * 2 / 1.2, 5.0); near("6 stool inv", 1.2 * 2 / 3, 0.80); near("6 stool K", 2 * sqrt(3 / 1.2), 3.2)
near("6 stool Ki", 0.5 * 3 * 4, 6.0); near("6 stool Kf", 0.5 * 1.2 * 25, 15); near("6 brake", 6 / 1.5, 4.0); near("6 brake P", 1.5 * 2, 3.0)
near("6 cyl", sqrt(4 * g * 1.5 / 3), 4.4); near("6 slide", sqrt(2 * g * 1.5), 5.4); near("6 hoop", sqrt(g * 1.5), 3.8); near("6 sphere", sqrt(10 * g * 1.5 / 7), 4.6)
near("6 comet sqrt", sqrt(5), 2.2)
# Unit 7
near("7 T spring", 2 * math.pi * sqrt(0.5 / 50), 0.63); near("7 T no 2pi", sqrt(0.01), 0.10); near("7 T inv", 2 * math.pi * sqrt(50 / 0.5), 63); near("7 f", 1 / (2 * math.pi * 0.1), 1.6)
near("7 E", 0.5 * 200 * 0.01, 1.0); near("7 E kA/2", 0.5 * 200 * 0.1, 10); near("7 kA", 200 * 0.1, 20)
near("7 moon", 2 * sqrt(9.8 / 1.6), 4.9); near("7 moon x6", 2 * 9.8 / 1.6, 12); near("7 moon div", 2 / sqrt(9.8 / 1.6), 0.81)
near("7 k", 4 * math.pi ** 2 * 0.2 / 0.16, 49); near("7 k 2pi m/T", 2 * math.pi * 0.2 / 0.4, 3.1); near("7 k /T", 4 * math.pi ** 2 * 0.2 / 0.4, 20); near("7 k no 4pi2", 0.2 / 0.16, 1.25)  # printed as the distractor 1.3
near("7 f", 30 / 45, 0.67); near("7 T", 45 / 30, 1.5); near("7 omega", 2 * math.pi * 30 / 45, 4.2); near("7 1/45", 1 / 45, 0.022)
near("7 graph k", 4 * math.pi ** 2 * 0.5 / 4, 4.9); near("7 graph 2pi m/T", 2 * math.pi * 0.5 / 2, 1.6); near("7 graph /T", 4 * math.pi ** 2 * 0.5 / 2, 9.9); near("7 graph T=1", 4 * math.pi ** 2 * 0.5, 20)
near("7 vmax", 2 * math.pi * 0.1 / 2, 0.31); near("7 vmax T1", 2 * math.pi * 0.1, 0.63); near("7 A/T", 0.1 / 2, 0.050)
near("7 vmax E", 0.1 * sqrt(200 / 0.5), 2.0); near("7 no root", 0.01 * 200 / 0.5, 4.0); near("7 no 2", sqrt(1.0 / 0.5), 1.4); near("7 sqrt k/m", sqrt(200 / 0.5), 20)
L7, T7 = [0.2, 0.4, 0.6, 0.8, 1.0], [0.90, 1.27, 1.55, 1.80, 2.01]
T2 = [x * x for x in T7]
for got, want in zip(T2, (0.81, 1.61, 2.40, 3.24, 4.04)):
    near("7 FRQ T^2", got, want, 0.005)
mx, my = sum(L7) / 5, sum(T2) / 5
s7 = sum((a - mx) * (b - my) for a, b in zip(L7, T2)) / sum((a - mx) ** 2 for a in L7)
near("7 FRQ slope", s7, 4.04, 0.01); near("7 FRQ g", 4 * math.pi ** 2 / s7, 9.8, 0.01)
near("7 FRQ 40deg", 1 + rad(40) ** 2 / 16, 1.03, 0.005)
# Unit 8
near("8 rho", 0.5 / 2e-4, 2500); near("8 V/m", 2e-4 / 0.5, 4e-4); near("8 mV", 0.5 * 2e-4, 1e-4)
near("8 P10", 1e5 + 1000 * g * 10, 2.0e5); near("8 gauge10", 1000 * g * 10, 9.8e4); near("8 no g", 1e5 + 1000 * 10, 1.1e5)
near("8 rock Fb", 1000 * 5e-4 * g, 4.9); near("8 rock scale", 2 * g - 4.9, 15); near("8 rock add", 2 * g + 4.9, 25)
near("8 nozzle", 2.0 / 0.5 * 1.5, 6.0); near("8 nozzle inv", 0.5 / 2.0 * 1.5, 0.38); near("8 nozzle sqrt", sqrt(4) * 1.5, 3.0)
near("8 torr", sqrt(2 * g * 1.25), 4.9); near("8 torr gh", sqrt(g * 1.25), 3.5); near("8 torr 2gh", 2 * g * 1.25, 25); near("8 torr gh2", g * 1.25, 12)
near("8 rho2", 0.3 / 1.2e-4, 2500); near("8 rho2 V/m", 1.2e-4 / 0.3, 4e-4); near("8 rho2 mV", 0.3 * 1.2e-4, 3.6e-5)
near("8 pool", 1000 * g * 3, 2.9e4); near("8 pool abs", 1.013e5 + 1000 * g * 3, 1.3e5); near("8 pool no g", 1000 * 3, 3e3); near("8 pool 1m", 1000 * g, 9.8e3)
near("8 hatch", 1000 * g * 100 * 0.5, 4.9e5); near("8 hatch P", 1000 * g * 100, 9.8e5); near("8 hatch abs", (1000 * g * 100 + 1e5) * 0.5, 5.4e5); near("8 hatch /A", 1000 * g * 100 / 0.5, 2.0e6)
Fb = 1000 * 1e-4 * g
near("8 cyl Fb", Fb, 0.98); near("8 cyl scale", 0.8 * g - Fb, 6.9); near("8 cyl add", 0.8 * g + Fb, 8.8); near("8 cyl half", 0.8 * g - Fb / 2, 7.4); near("8 cyl halfw", 0.8 * g / 2, 3.9)
near("8 oil", 0.8 * g - 800 * 1e-4 * g, 7.1); near("8 oil Fb", 800 * 1e-4 * g, 0.78)
near("8 pipe", 0.5 * 4, 2.0); near("8 pipe r", 0.5 * 2, 1.0); near("8 pipe inv", 0.5 / 4, 0.125); near("8 pipe rinv", 0.5 / 2, 0.25)
near("8 leak", sqrt(2 * g * 2), 6.3); near("8 leak gh", sqrt(g * 2), 4.4); near("8 leak 2gh", 2 * g * 2, 39); near("8 leak gh2", g * 2, 20)
near("8 flow", 3e-4 * 2, 6e-4); near("8 flow A/v", 3e-4 / 2, 1.5e-4); near("8 flow v/A", 2 / 3e-4, 6.7e3)
near("8 FRQ F", 400 * 2e-3 * g, 7.8); near("8 FRQ a", (1000 / 600 - 1) * g, 6.5)

if __name__ == "__main__":
    print("\n".join(fails) or "all numeric answers check")
    raise SystemExit(1 if fails else 0)
