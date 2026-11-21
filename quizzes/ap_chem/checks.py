"""Numerical checks for AP Chemistry Unit 5 Practice Sets A and B: every computed key answer, every
computed distractor named in the explanations, and the free-response values."""
import math

r = lambda x, n: float(f"{x:.{n}g}")
ln2 = math.log(2)

# ---------------- Set A
assert math.isclose(3 * 0.0060, 0.018) and math.isclose(0.0060 / 3, 0.0020) and math.isclose(2 * 0.0060, 0.012)
rateA = (0.84 - 0.60) / 40
assert math.isclose(rateA, 6.0e-3) and math.isclose(rateA / 2, 3.0e-3) and math.isclose(rateA * 2, 1.2e-2) and math.isclose(0.60 / 40, 1.5e-2)
assert math.isclose(2.16e-3 / 2.40e-4, 9) and math.isclose(7.20e-4 / 2.40e-4, 3)            # 2nd in ClO2, 1st in OH-
assert 2 ** 2 * 0.5 == 2 and 2 ** 2 == 4 and 2 ** 3 == 8
k6 = 2.40e-4 / (0.020 ** 2 * 0.030)
assert math.isclose(k6, 20) and math.isclose(2.40e-4 / (0.020 * 0.030), 0.40) and math.isclose(2.40e-4 / 0.020 ** 2, 0.60)
assert round(ln2 / 0.0115) == 60 and round(1 / 0.0115) == 87 and round(ln2 / 0.0115 / 2) == 30 and r(ln2 * 0.0115, 2) == 0.0080
assert math.isclose(0.80 - 0.020 * 15, 0.50) and r(0.80 * math.exp(-0.020 * 15), 2) == 0.59 and math.isclose(0.020 * 15, 0.30)
assert math.isclose(0.80 / (2 * 0.020), 20)                                                   # zero-order t1/2 = 20 s > 15 s
assert math.isclose(1 / (0.040 * 0.50), 50) and round(ln2 / 0.040) == 17 and r(0.50 / (2 * 0.040), 2) == 6.2  # 6.25 -> "6.3"
inv = [1 / x for x in (0.400, 0.200, 0.133, 0.100)]
assert [round(x, 1) for x in inv] == [2.5, 5.0, 7.5, 10.0] and math.isclose((inv[-1] - inv[0]) / 300, 0.025)
assert r(ln2 / 100, 2) == 0.0069 and math.isclose(0.2 / 100, 2.0e-3)
assert 49.2 / 12.3 == 4 and 0.5 ** 4 == 1 / 16
assert 0.5 ** 2 == 0.25 and 0.5 ** 3 == 0.125                                                # 75 % done = 2 t1/2; 87.5 % = 3
assert 75 - 20 == 55 and 75 + 20 == 95
assert 90 - 0 == 90 and 70 - 20 == 50 and 45 < 50                                            # Q27-28 barriers
# FR 31
kA = 1.92e-5 / (0.080 * 0.040)
assert math.isclose(kA, 6.0e-3) and math.isclose(2 * 1.92e-5, 3.84e-5)
assert math.isclose(3.84e-5 / 1.92e-5, 2)
# FR 32
lns = [math.log(x) for x in (0.800, 0.566, 0.400, 0.283)]
assert [round(x, 3) for x in lns] == [-0.223, -0.569, -0.916, -1.262]
assert all(round(lns[i] - lns[i + 1], 3) in (0.346, 0.347) for i in range(3))
k32 = ln2 / 20
assert round(k32, 4) == 0.0347 and round(0.800 * math.exp(-k32 * 50), 3) == 0.141 and round(0.800 / 2 ** 2.5, 3) == 0.141

# ---------------- Set B
assert math.isclose(2 * 0.015, 0.030) and math.isclose(0.015 / 2, 0.0075) and math.isclose(4 * 0.015, 0.060)
assert math.isclose(3.6e-4 / 4.0e-5, 9)                                                        # 2nd in A; B zero order
kB = 4.0e-5 / 0.10 ** 2
assert math.isclose(kB, 4.0e-3) and math.isclose(4.0e-5 / 0.10, 4.0e-4) and math.isclose(4.0e-5 / (0.10 ** 2 * 0.20), 2.0e-2)
assert math.isclose(kB * 0.20 ** 2, 1.6e-4) and math.isclose(kB * 0.20 ** 2 * 3, 4.8e-4)
assert math.isclose(kB * 0.20, 8.0e-4) and math.isclose(kB * 0.20 ** 2 * 0.60, 9.6e-5)
assert r(0.60 * math.exp(-0.050 * 20), 2) == 0.22 and r(0.60 * math.exp(0.050 * 20), 2) == 1.6
assert math.isclose(1 / 0.20 + 0.15 * 20, 8.0) and math.isclose(1 / 8.0, 0.125) and r(1 / (0.15 * 20), 2) == 0.33
assert round(ln2 / 2.31e-3) == 300 and 0.50 / 0.0625 == 8 and 0.5 ** 3 == 0.0625 / 0.50
assert r(3 * 5730, 2) == 1.7e4 and r(2 * 5730, 2) == 1.1e4 and r(4 * 5730, 2) == 2.3e4 and 0.5 ** 3 == 0.125
assert 180 - 120 == 60 and 30 - 120 == -90 and 180 - 30 == 150
assert 40 - 0 == 40 and 55 - (-10) == 65
# FR 31
assert round((0.0100 - 0.00667) / 100, 7) == 3.33e-5 and round((0.0100 - 0.00667) / 200, 7) == 1.67e-5
invB = [1 / x for x in (0.0100, 0.00800, 0.00667, 0.00571, 0.00500)]
assert [round(x) for x in invB] == [100, 125, 150, 175, 200]
assert math.isclose((1 / 0.00250 - 1 / 0.0100) / 0.50, 600) and math.isclose(1 / (0.50 * 0.00500), 400)
# FR 32
assert 120 - (-50) == 170 and 60 > 70 - 20
print("AP Chem numeric checks passed")
