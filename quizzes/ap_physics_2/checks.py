"""Numeric checks for the AP Physics 2 series: every computed answer (and numeric distractor) recomputed here.

    python3 -I quizzes/ap_physics_2/checks.py

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

# Unit 9
near("9 P", 2 * R * 300 / 0.05, 1.0e5); near("9 nRT", 2 * R * 300, 5.0e3); near("9 P liters", 2 * R * 300 / 50, 1.0e2); near("9 P inv", 0.05 / (2 * R * 300), 1.0e-5)
near("9 sealed", 600 / 300, 2); near("9 sealed C", 327 / 27, 12); near("9 sealed /273", 300 / 273, 1.1)
near("9 Q water", 0.5 * 4186 * 10, 2.1e4); near("9 Q 1kg", 4186 * 10, 4.2e4); near("9 Q no 10", 0.5 * 4186, 2.1e3); near("9 c", 4186, 4.2e3)
near("9 W isobaric", -2e5 * 0.02, -4.0e3); near("9 W Vf", -2e5 * 0.03, -6.0e3); near("9 W Vi", -2e5 * 0.01, -2.0e3)
near("9 moles", 1.5e5 * 0.02 / (R * 250), 1.4, 0.05); near("9 moles inv", R * 250 / (1.5e5 * 0.02), 0.69); near("9 moles no R", 1.5e5 * 0.02 / 250, 12); near("9 molecules", 1.5e5 * 0.02 / (kB * 250), 8.7e23)
m = 4.65e-26
near("9 vrms", sqrt(3 * kB * 300 / m), 517); near("9 vrms no3", sqrt(kB * 300 / m), 298); near("9 vrms noroot", 3 * kB * 300 / m, 2.67e5); near("9 vrms 6", sqrt(6 * kB * 300 / m), 730)
near("9 WAB", -3e5 * 2e-3, -600); near("9 WAB Vf", -3e5 * 3e-3, -900); near("9 WAB Vi", -3e5 * 1e-3, -300)
near("9 net W", 0.5 * 2e-3 * 2e5, 200); near("9 QAB", 1.5 * (900 - 300) + 600, 1500)
near("9 mix", (0.2 * 80 + 0.6 * 20) / 0.8, 35); near("9 mix avg", 50, 50); near("9 mix wrong", (0.6 * 80 + 0.2 * 20) / 0.8, 65)
# Unit 10
near("10 F", k * 3e-6 * 4e-6 / 0.09, 1.2); near("10 F /r", k * 12e-12 / 0.3, 0.36); near("10 F r2 dec", k * 12e-12 / 0.009, 12); near("10 F uC", k * 12 / 0.09, 1.2e12)
near("10 E", k * 2e-9 / 0.09, 200); near("10 E /r", k * 2e-9 / 0.3, 60); near("10 kq", k * 2e-9, 18); near("10 E dec", k * 2e-9 / 0.009, 2000)
near("10 U", k * 1e-12 / 0.1, 0.090); near("10 U r2", k * 1e-12 / 0.01, 0.90)
near("10 plates", 12 / 0.02, 600); near("10 plates Vd", 12 * 0.02, 0.24); near("10 plates inv", 0.02 / 12, 1.7e-3); near("10 plates 2m", 12 / 2, 6.0)
near("10 UC", 0.5 * 10e-6 * 144, 7.2e-4); near("10 UC no half", 10e-6 * 144, 1.4e-3); near("10 UC no sq", 0.5 * 10e-6 * 12, 6.0e-5); near("10 Q", 10e-6 * 12, 1.2e-4)
mp = 1.67e-27
near("10 proton", sqrt(2 * e * 500 / mp), 3.1e5); near("10 proton noroot", 2 * e * 500 / mp, 9.6e10); near("10 proton no2", sqrt(e * 500 / mp), 2.2e5); near("10 proton me", sqrt(2 * e * 500 / me), 1.3e7)
near("10 two", k * 4e-12 / 0.01, 3.6); near("10 two /r", k * 4e-12 / 0.1, 0.36); near("10 two one", k * 2e-12 / 0.01, 1.8)
E1, E2 = k * 4e-9 / 0.15 ** 2, k * 1e-9 / 0.15 ** 2
near("10 E1", E1, 1600); near("10 E2", E2, 400); near("10 Emid", E1 + E2, 2000); near("10 Emid sub", E1 - E2, 1200)
near("10 Vmid", k * 3e-9 / 0.15, 180); near("10 Vmid abs", k * 5e-9 / 0.15, 300); near("10 Vmid r2", k * 3e-9 / 0.0225, 1200); near("10 V1", k * 4e-9 / 0.15, 240)
x0 = 0.30 / (1 - 0.5)  # 2/x = 1/(x - 0.3)
near("10 zero", x0, 0.60); near("10 zero check", 4 / x0 ** 2, 1 / (x0 - 0.3) ** 2)
near("10 W", 2e-9 * 180, 3.6e-7); near("10 W qE", 2e-9 * 2000, 4.0e-6)
near("10 electron K", e * 200, 3.2e-17); near("10 e/V", e / 200, 8.0e-22)
near("10 U5", 0.5 * 5e-6 * 400, 1.0e-3); near("10 U5 no half", 5e-6 * 400, 2.0e-3); near("10 U5 no sq", 0.5 * 5e-6 * 20, 5.0e-5); near("10 Q5", 5e-6 * 20, 1.0e-4)
near("10 p1000", sqrt(2 * e * 1000 / mp), 4.4e5); near("10 p1000 noroot", 2 * e * 1000 / mp, 1.9e11); near("10 p1000 me", sqrt(2 * e * 1000 / me), 1.9e7); near("10 p1000 no2", sqrt(e * 1000 / mp), 3.1e5)
# Unit 11
near("11 electrons", 2.0 / e, 1.25e19, 0.005); near("11 Ie", 2.0 * e, 3.2e-19); near("11 e/I", e / 2.0, 8.0e-20)
near("11 bulb R", 120 ** 2 / 60, 240); near("11 bulb I", 60 / 120, 0.50); near("11 bulb V/P", 120 / 60, 2.0); near("11 bulb PV", 60 * 120, 7200)
par = 1 / (1 / 6 + 1 / 3)
near("11 Req", 6 + par, 8.0); near("11 I", 12 / (6 + par), 1.5); near("11 I15", 12 / 15, 0.80); near("11 I3", 12 / 3, 4.0); near("11 I6", 12 / 6, 2.0)
near("11 tau", 2e3 * 50e-6, 0.10); near("11 tau pref", 2 * 50, 100); near("11 R/C", 2e3 / 50e-6, 4.0e7); near("11 C/R", 50e-6 / 2e3, 2.5e-8)
near("11 copper", 1.7e-8 * 10 / 1e-6, 0.17); near("11 copper A", 1.7e-8 * 10 * 1e-6, 1.7e-13); near("11 copper inv", 1e-6 / (1.7e-8 * 10), 5.9); near("11 copper 1m", 1.7e-8 / 1e-6, 1.7e-2)
near("11 R60", 120 ** 2 / 60, 240); near("11 R100", 120 ** 2 / 100, 144)
near("11 dryer", 120 ** 2 / 1200, 12); near("11 dryer I", 1200 / 120, 10); near("11 dryer V/P", 120 / 1200, 0.10); near("11 V2", 120 ** 2, 1.4e4)
near("11 N", 0.8 / e, 5.0e18); near("11 N Ie", 0.8 * e, 1.3e-19); near("11 N 1e-19", 0.8 / 1e-19, 8.0e18)
p23 = 1 / (1 / 6 + 1 / 12)
near("11 Rp", p23, 4.0); near("11 Req2", 4 + p23, 8.0); near("11 series", 4 + 6 + 12, 22); near("11 allpar", 1 / (1 / 4 + 1 / 6 + 1 / 12), 2.0)
I = 12 / 8
near("11 I2", I, 1.5); near("11 I 22", 12 / 22, 0.55); near("11 V3", 12 - I * 4, 6.0); near("11 V3 wrong", I * 12, 18)
near("11 I R2", 6 / 6, 1.0); near("11 I R3", 6 / 12, 0.50); near("11 remove I", 12 / 10, 1.2); near("11 remove V2", 12 - 1.2 * 4, 7.2)
near("11 P1", I ** 2 * 4, 9.0); near("11 P1 V2/R", 144 / 4, 36); near("11 Ptot", I * 12, 18)
near("11 loop", (9 - 3) / 2, 3.0); near("11 loop sum", 12 / 2, 6.0); near("11 loop 9", 9 / 2, 4.5)
near("11 Cser", 1 / (1 / 2 + 1 / 3), 1.2)
L11, R11 = [0.2, 0.4, 0.6, 0.8, 1.0], [1.1, 2.3, 3.3, 4.5, 5.6]
s11, b11 = fit(L11, R11)
A11 = pi * (0.25e-3) ** 2
near("11 FRQ slope", s11, 5.6); near("11 FRQ A", A11, 1.96e-7); near("11 FRQ rho", s11 * A11, 1.1e-6)
# Unit 12
mp = 1.67e-27
near("12 F", e * 2e5 * 0.5, 1.6e-14); near("12 F 1T", e * 2e5, 3.2e-14); near("12 vB", 2e5 * 0.5, 1.0e5)
near("12 Bwire", mu0 * 10 / (2 * pi * 0.05), 4.0e-5); near("12 B no 2pi", mu0 * 10 / 0.05, 2.5e-4); near("12 B r.1", mu0 * 10 / (2 * pi * 0.1), 2.0e-5); near("12 mu0 I", mu0 * 10, 1.3e-5, 0.05)
near("12 emf", 50 * 0.02 * 0.4 / 0.1, 4.0); near("12 emf 1", 0.02 * 0.4 / 0.1, 0.080); near("12 NdPhi", 50 * 0.02 * 0.4, 0.40); near("12 emf dt", 50 * 0.02 * 0.4 / 0.01, 40)
near("12 r", mp * 3e6 / (e * 0.5), 0.063); near("12 r inv", e * 0.5 / (mp * 3e6), 16); near("12 r me", me * 3e6 / (e * 0.5), 3.4e-5); near("12 d", 2 * mp * 3e6 / (e * 0.5), 0.13, 0.05)
B1 = mu0 * 20 / (2 * pi * 0.1)
near("12 B1", B1, 4.0e-5); near("12 B1 10A", mu0 * 10 / (2 * pi * 0.1), 2.0e-5); near("12 B1 no2pi", mu0 * 20 / 0.1, 2.5e-4); near("12 B1 half", mu0 * 20 / (2 * pi * 0.05), 8.0e-5)
near("12 F/L", 10 * B1, 4.0e-4); near("12 F/L 20", 20 * B1, 8.0e-4); near("12 F/L sym", 20 * mu0 * 10 / (2 * pi * 0.1), 4.0e-4)
xz = 20 * 0.1 / 30
near("12 zero", xz, 0.067); near("12 zero chk", 20 / xz, 10 / (0.1 - xz))
near("12 flux", 0.2 * 0.05 * 0.5, 5.0e-3); near("12 flux sin", 0.2 * 0.05 * sin(rad(60)), 8.7e-3); near("12 flux B/A", 0.2 / 0.05, 4.0)
near("12 emf2", 200 * 0.01 * 0.5 / 0.25, 4.0); near("12 emf2 1", 0.01 * 0.5 / 0.25, 0.020); near("12 emf2 NdPhi", 200 * 0.01 * 0.5, 1.0); near("12 emf2 x dt", 200 * 0.01 * 0.5 * 0.25, 0.25)
near("12 rod", 0.3 * 0.5 * 4, 0.60); near("12 rod /L", 0.3 * 4 / 0.5, 2.4); near("12 rod /v", 0.3 * 0.5 / 4, 0.038); near("12 rod BL", 0.3 * 0.5, 0.15)
D = (2 / 0.2) * sqrt(2 * 3.32e-26 * 1000 / e)
near("12 FRQ D", D, 0.20); near("12 FRQ ratio", sqrt(22 / 20), 1.05, 0.005)
# Unit 13
asin, deg = math.asin, math.degrees
near("13 snell30", deg(asin(0.5 / 1.5)), 19); near("13 snell30 x", deg(asin(0.75)), 49); near("13 snell30 div", 30 / 1.5, 20)
near("13 crit", deg(asin(1 / 1.5)), 42); near("13 crit comp", 90 - deg(asin(1 / 1.5)), 48); near("13 crit n2", deg(asin(1 / 2.25)), 26)
si = 1 / (1 / 10 - 1 / 30)
near("13 mirror si", si, 15); near("13 mirror M", -si / 30, -0.5); near("13 mirror add", 1 / (1 / 10 + 1 / 30), 7.5)
near("13 2f", 1 / (1 / 20 - 1 / 40), 40)
si2 = 1 / (1 / 15 - 1 / 10)
near("13 inside si", si2, -30); near("13 inside M", -si2 / 10, 3.0); near("13 inside add", 1 / (1 / 15 + 1 / 10), 6.0)
near("13 glass", deg(asin(sin(rad(40)) / 1.5)), 25); near("13 glass x", deg(asin(1.5 * sin(rad(40)))), 75); near("13 glass div", 40 / 1.5, 27)
near("13 v", 3e8 / 1.5, 2.0e8); near("13 v x", 3e8 * 1.5, 4.5e8); near("13 v n2", 3e8 / 2.25, 1.3e8)
near("13 lambda", 600 / 1.5, 400); near("13 lambda water", 600 / 1.333, 450)
near("13 lens si", 1 / (1 / 10 - 1 / 15), 30); near("13 lens add", 1 / (1 / 10 + 1 / 15), 6.0); near("13 lens M", -30 / 15, -2)
near("13 magnifier", 1 / (1 / 20 - 1 / 10), -20); near("13 magnifier add", 1 / (1 / 20 + 1 / 10), 6.7)
so13, si13 = [15.0, 20.0, 25.0, 30.0, 40.0], [29.6, 20.2, 16.5, 15.1, 13.4]
x13, y13 = [1 / v for v in so13], [1 / v for v in si13]
for got, want in zip(x13 + y13, (0.0667, 0.0500, 0.0400, 0.0333, 0.0250, 0.0338, 0.0495, 0.0606, 0.0662, 0.0746)):
    near("13 FRQ recip", got, want, 0.005)
s13, b13 = fit(x13, y13)
near("13 FRQ slope", s13, -1.0, 0.05); near("13 FRQ intercept", b13, 0.100, 0.02); near("13 FRQ f", 1 / b13, 10, 0.02)
# Unit 14
near("14 lambda", 340 / 680, 0.50); near("14 f/v", 680 / 340, 2.0); near("14 vf", 340 * 680, 2.3e5); near("14 sum", 340 + 680, 1020)
near("14 FM", 3e8 / 1e8, 3.0); near("14 FM inv", 1e8 / 3e8, 0.33); near("14 FM x", 3e8 * 1e8, 3.0e16); near("14 FM 100Hz", 3e8 / 100, 3.0e6)
near("14 f1", 120 / 1.2, 100); near("14 f1 L", 120 / 0.6, 200); near("14 f1 4L", 120 / 2.4, 50); near("14 vL", 120 * 0.6, 72)
near("14 fringe", 600e-9 * 2 / 0.2e-3, 6.0e-3); near("14 fringe 2mm", 600e-9 * 2 / 2e-3, 0.60e-3); near("14 fringe .02", 600e-9 * 2 / 0.02e-3, 60e-3)
near("14 rope", 4 * 1.5, 6.0); near("14 rope f/l", 4 / 1.5, 2.7); near("14 rope l/f", 1.5 / 4, 0.38); near("14 rope sum", 5.5, 5.5)
near("14 snap f", 12 / 0.8, 15); near("14 snap vl", 12 * 0.8, 9.6); near("14 snap T", 0.8 / 12, 0.067); near("14 snap 1.6", 12 / 1.6, 7.5); near("14 snap 2f", 12 / 30, 0.40)
near("14 pipe", 340 / 2.0, 170); near("14 pipe open", 340 / 1.0, 340); near("14 pipe L", 340 / 0.5, 680); near("14 pipe 8L", 340 / 4.0, 85)
near("14 slit", 1e-4 * 9e-3 / 1.5, 6.0e-7); near("14 slit mm", 1e-4 * 9 / 1.5, 6.0e-4); near("14 slit swap", 1e-4 * 1.5 / 9e-3, 1.7e-2)
near("14 film", 532 / (4 * 1.33), 100); near("14 film half", 532 / (2 * 1.33), 200); near("14 film no n", 532 / 4, 133); near("14 film lam n", 532 / 1.33, 400)
# Unit 15
hc = 1240
near("15 E500", hc / 500, 2.5); near("15 E500 inv", 500 / hc, 0.40); near("15 E500 x", hc * 500, 6.2e5); near("15 E500 J", h * c / 500e-9, 4.0e-19)
near("15 dB", h / (me * 1e6), 7.3e-10); near("15 dB x", h * me * 1e6, 6.0e-58); near("15 dB inv", me * 1e6 / h, 1.4e9); near("15 dB no v", h / me, 7.3e-4)
near("15 H line", hc / (3.40 - 1.51), 656); near("15 H 3.40", hc / 3.40, 365); near("15 H 1.51", hc / 1.51, 821)
near("15 Wien", 2.9e-3 / 5800 * 1e9, 500); near("15 Wien x", 2.9e-3 * 5800 * 1e9, 1.7e10); near("15 Wien inv", 5800 / 2.9e-3, 2.0e6)
near("15 PE K", hc / 250 - 2.3, 2.7); near("15 PE E", hc / 250, 5.0); near("15 PE add", hc / 250 + 2.3, 7.3)
near("15 I131", 80 / 8, 10); near("15 I131 /3", 80 / 3, 27)
near("15 violet", hc / 400, 3.1); near("15 violet inv", 400 / hc, 0.32); near("15 violet J", h * c / 400e-9, 5.0e-19); near("15 violet f", c / 400e-9, 7.5e14)
lv = [-10.0, -6.0, -4.0, -1.0]
gaps = sorted({round(lv[j] - lv[i], 6) for i in range(4) for j in range(i + 1, 4)})
near("15 lines", len(gaps), 6); near("15 smallest gap", min(gaps), 2.0); near("15 longest", hc / 2.0, 620); near("15 shortest", hc / 9.0, 138); near("15 4to3", hc / 3.0, 413)
fP, KP = [6, 8, 10, 12, 14], [0.20, 1.00, 1.85, 2.65, 3.50]
sP, bP = fit(fP, KP)
near("15 PE slope", sP, 0.4125, 0.005); near("15 PE icpt", bP, -2.27, 0.01); near("15 PE f0", -bP / sP, 5.5); near("15 PE h eVs", sP * 1e-14, 4.14e-15, 0.01)
near("15 mc2", 3.1e-29 * c ** 2, 2.8e-12); near("15 mc2 half", 0.5 * 3.1e-29 * c ** 2, 1.4e-12); near("15 mc", 3.1e-29 * c, 9.3e-21); near("15 MeV", 3.1e-29 * c ** 2 / 1.6e-13, 17, 0.05)
near("15 thalf", 20 / 4, 5.0); near("15 thalf /16", 20 / 16, 1.25)
near("15 FRQ Vs", hc / 300 - 2.3, 1.8); near("15 FRQ Vs150", hc / 150 - 2.3, 6.0)

if __name__ == "__main__":
    print("\n".join(fails) or "all numeric answers check")
    raise SystemExit(1 if fails else 0)
