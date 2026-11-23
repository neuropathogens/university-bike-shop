"""Real Analysis Vol. III (Applications): 28 problems in CS, AI/ML and physics (5/10/15 points, 280 in all), free response.

Each problem shows its subsection's "Tool -> use" box, then the PDF's full solution and the key's answer."""
import math
from fractions import Fraction as F

from college_math.quiz import FRQ, proof_rubric

DOC = dict(
    slug="applications", pdf="real-analysis-3-applications.pdf", title="Applications",
    h1="Applications", sub="Real Analysis &middot; Volume III &middot; CS, AI/ML, physics",
    metaline="28 problems &middot; 280 points (&#9733; 5, &#9733;&#9733; 10, &#9733;&#9733;&#9733; 15)",
    desc="Real Analysis Volume III: 28 problems that use the theorems on algorithms, machine learning and physics, from PageRank and gradient descent to heat flow and the Dirac delta, each with a full model solution.",
    setup="", key="", frWord="Problem",
    frIntro=("Each problem opens with the tool it uses and what that tool buys you. Work it on paper (or below), then open the model "
             "solution and mark yourself out of the problem&rsquo;s points."),
    rules={"A.i": ("Asymptotic analysis is limit theory", 2), "A.ii": ("Numerical methods are convergence proofs", 3),
           "A.iii": ("Countability limits computation", 3), "A.iv": ("PageRank is a contraction", 3),
           "B.i": ("Gradient descent: smoothness and contraction", 4), "B.ii": ("Stochastic approximation and series", 4),
           "B.iii": ("Universal approximation from uniform continuity", 4), "B.iv": ("Lipschitz networks and vanishing gradients", 5),
           "B.v": ("Reinforcement learning: the Bellman contraction", 5), "B.vi": ("Why stochastic gradients are unbiased: DCT", 5),
           "B.vii": ("Softmax and log-sum-exp", 6), "C.i": ("Taylor&rsquo;s theorem and small oscillations", 6),
           "C.ii": ("Is classical mechanics deterministic? Picard&ndash;Lindel&ouml;f", 6), "C.iii": ("Heat flow: Fourier series and uniform convergence", 7),
           "C.iv": ("Lattice sums and the Riemann rearrangement theorem", 7), "C.v": ("Feynman&rsquo;s trick is the Dominated Convergence Theorem", 7),
           "C.vi": ("Stirling&rsquo;s formula and entropy", 8), "C.vii": ("The Dirac delta: limit of functions, not a function", 8)},
)

TOOL = {
    "A.i": r"$f = O(g)$ means $\limsup f(n)/g(n) < \infty$; $f = o(g)$ means $f/g \to 0$; $f \sim g$ means $f/g \to 1$. L&rsquo;H&ocirc;pital and the ratio test settle growth comparisons. The integral test gives two-sided bounds for sums: for decreasing $f \ge 0$, $\int_1^{n+1}f \le \sum_{k=1}^nf(k) \le f(1) + \int_1^nf$. With $f(x) = 1/x$ this gives $\ln(n + 1) \le H_n \le 1 + \ln n$. That is why randomized quicksort makes $2nH_n - 4n + 2H_n \sim 2n\ln n$ expected comparisons.",
    "A.ii": r"Bisection is the Nested Interval Property plus the IVT: the error after $n$ steps is at most $(b - a)/2^n$, independent of $f$. Newton&rsquo;s method $x_{n+1} = x_n - f(x_n)/f'(x_n)$: Taylor with remainder at $x_n$ gives $e_{n+1} = \frac{f''(\xi)}{2f'(x_n)}e_n^2$, so $|e_{n+1}| \le \frac{M}{2m}e_n^2$ (quadratic convergence) where $|f''| \le M$ and $|f'| \ge m$. Trapezoid rule: the error is at most $\frac{(b - a)^3}{12n^2}\max|f''|$.",
    "A.iii": r"A program is a finite string over a finite alphabet, so there are countably many programs. A real $x$ is computable if some program outputs its digits. Cantor&rsquo;s diagonal argument (the list of all programs versus the reals) is the same move as Turing&rsquo;s proof that the halting problem is undecidable.",
    "A.iv": r"For a column-stochastic link matrix $P$ and damping $d \in (0, 1)$, define $F(x) = dPx + \frac{1 - d}{n}\mathbf 1$ on the simplex $\Delta = \{x \ge 0, \sum x_i = 1\}$. Banach&rsquo;s theorem in $(\Delta, \|\cdot\|_1)$ gives a unique ranking vector, and power iteration converges geometrically at rate $d$.",
    "B.i": r"$f$ is $L$-smooth if $\nabla f$ is $L$-Lipschitz. The FTC along a segment gives the descent lemma $f(y) \le f(x) + \nabla f(x)\cdot(y - x) + \frac L2\|y - x\|^2$. It turns every step of GD with $\eta = 1/L$ into a guaranteed decrease, and summing the steps gives the convergence rate. On a $\mu$-strongly convex quadratic, the GD map $x \mapsto x - \eta\nabla f(x)$ is a Banach contraction with factor $\max_i|1 - \eta\lambda_i|$.",
    "B.ii": r"Robbins&ndash;Monro/SGD step sizes must satisfy $\sum\alpha_k = \infty$ (so the iterates can travel any distance) and $\sum\alpha_k^2 < \infty$ (so the accumulated noise $\sum\alpha_k\xi_k$ has finite variance and converges). Both conditions are $p$-series questions.",
    "B.iii": r"A one-hidden-layer ReLU network $g(x) = c + \sum_iw_i\,\mathrm{ReLU}(x - t_i)$ is exactly a continuous piecewise-linear function with knots $t_i$. Heine&ndash;Cantor makes piecewise-linear interpolation uniformly accurate. Stone&ndash;Weierstrass gives the multivariate version for many activations.",
    "B.iv": r"Lipschitz constants multiply under composition: $\mathrm{Lip}(g\circ h) \le \mathrm{Lip}(g)\,\mathrm{Lip}(h)$. For a linear map, the constant is the operator norm $\|W\|_2$. ReLU is 1-Lipschitz and the sigmoid is $\frac14$-Lipschitz (by the MVT, $|\sigma'| \le \frac14$). A bound $\mathrm{Lip} \le K$ certifies robustness: $\|\delta\| < r$ moves the output by less than $Kr$.",
    "B.v": r"On a finite MDP, $(TV)(s) = \max_a\left[r(s, a) + \gamma\sum_{s'}P(s'|s, a)V(s')\right]$. Since $|\max_af - \max_ag| \le \max_a|f - g|$, $T$ is a $\gamma$-contraction in $\|\cdot\|_\infty$ on the complete space $\mathbb R^S$. So the optimal value $V^*$ exists, is unique, and value iteration converges geometrically.",
    "B.vi": r"SGD replaces $\nabla_\theta\,\mathbb E[\ell(\theta, Z)]$ with $\nabla_\theta\ell(\theta, Z_i)$. That is legitimate exactly when $\frac{d}{d\theta}$ and $\mathbb E$ commute. Sufficient condition: by the MVT, the difference quotients are bounded by $\sup_{|\theta' - \theta|\le1}|\partial_\theta\ell(\theta', Z)| \le G(Z)$ with $\mathbb E[G] < \infty$, and then DCT applies.",
    "B.vii": r"$\mathrm{LSE}(x) = \ln\sum_{i=1}^ne^{x_i}$ is a smooth, convex surrogate for $\max_ix_i$, and $\nabla\,\mathrm{LSE} = \mathrm{softmax}$. The squeeze theorem controls the temperature limit.",
    "C.i": r"Near a minimum $r_0$ of a potential, $V(r) = V(r_0) + \frac12V''(r_0)(r - r_0)^2 + O((r - r_0)^3)$. To second order the motion is harmonic, with $\omega = \sqrt{V''(r_0)/m}$. The Lagrange remainder says exactly how small &ldquo;small&rdquo; has to be.",
    "C.ii": r"For $y' = F(t, y)$, $y(t_0) = y_0$, the integral operator $(Ty)(t) = y_0 + \int_{t_0}^tF(s, y(s))\,ds$ is a contraction on $C[t_0 - h, t_0 + h]$ when $F$ is Lipschitz in $y$ with constant $K$ and $Kh < 1$. So Lipschitz forces give unique trajectories. Without a Lipschitz bound, uniqueness can fail; Norton&rsquo;s dome is the famous example.",
    "C.iii": r"For $u_t = \kappa u_{xx}$ on $[0, \pi]$ with $u(0, t) = u(\pi, t) = 0$ and $u(x, 0) = f(x) = \sum b_n\sin nx$, separation of variables gives $u = \sum b_ne^{-\kappa n^2t}\sin nx$. For $t \ge t_0 > 0$, the factor $e^{-\kappa n^2t_0}$ beats every polynomial in $n$. The M-test then gives uniform convergence of every termwise derivative, so $u$ is $C^\infty$ and really solves the PDE, even when $f$ is discontinuous.",
    "C.iv": r"The electrostatic energy of an ion in a crystal is $-Mq^2/a$, where the Madelung constant $M$ is a conditionally convergent sum of $\pm1/r$ terms. By Riemann&rsquo;s theorem, the order of summation changes the answer. Physically, the order is fixed by summing over charge-neutral shells or by Ewald summation. In 3D NaCl, summing over expanding spheres does not even converge, while expanding cubes do.",
    "C.v": r"$\frac{d}{db}\int g(x, b)\,dx = \int\partial_bg(x, b)\,dx$ holds when $|\partial_bg(x, b)| \le G(x)$ with $G$ integrable, for $b$ in a neighborhood. (Apply the MVT to the difference quotient, then DCT.)",
    "C.vi": r"Statistical mechanics counts microstates: $W = \binom{N}{pN}$. Stirling, $\ln N! = N\ln N - N + O(\ln N)$ (problem A.1 is the crude version), turns $\ln W$ into an extensive entropy.",
    "C.vii": r"An approximate identity $\phi_n \ge 0$ with $\int\phi_n = 1$ and mass concentrating at 0 satisfies $\int f\phi_n \to f(0)$ for bounded $f$ continuous at 0. Physicists write $\delta = \lim\phi_n$. DCT shows that no integrable function can play that role, which is why $\delta$ lives in the theory of distributions.",
}

# --- the numbers the solutions quote ---
H100 = sum(1 / k for k in range(1, 101))
assert round(H100, 4) == 5.1874 and round(100 * H100, 1) == 518.7 and round(100 * math.log(100), 1) == 460.5      # A.3
assert 2 ** 29 < 10 ** 9 < 2 ** 30                                                                                 # A.4
e, x, errs = 1.5 - math.sqrt(2), 1.5, []
for _ in range(3):
    e, x = e * e / (2 * x), x - (x * x - 2) / (2 * x); errs.append(e)
assert round(1.5 - math.sqrt(2), 4) == 0.0858 and [float(f"{v:.3g}") for v in errs] == [0.00245, 2.12e-06, 1.59e-12]  # A.5
assert math.ceil(math.sqrt(math.e * 1e6 / 12)) == 476 and round(math.sqrt(math.e * 1e6 / 12), 2) == 475.94          # A.6
assert round(math.log(2e8) / -math.log(0.85), 1) == 117.6                                                           # A.8
assert round(6 * math.log(10) / math.log(11 / 9), 2) == 68.85 and abs(1 - F(2, 11)) == abs(1 - 10 * F(2, 11)) == F(9, 11)     # B.2
assert round(math.log(1000) / -math.log(0.9), 2) == 65.56                                                           # B.8
assert round(math.sqrt(0.06), 4) == 0.2449 and round(math.degrees(math.sqrt(0.06)), 2) == 14.03                     # C.1
r0 = 2 ** (1 / 6)
assert abs(-12 * r0 ** -13 + 6 * r0 ** -7) < 1e-12 and math.isclose(4 * (156 * r0 ** -14 - 42 * r0 ** -8), 72 / 2 ** (1 / 3))  # C.2
assert math.isclose(sum(1 / n ** 2 for n in range(1, 200001, 2)), math.pi ** 2 / 8, rel_tol=1e-5)                  # C.6
assert round(2 * math.log(2), 3) == 1.386                                                                           # C.7
N = 200000
assert math.isclose(sum(((x := (i + 0.5) / N) - 1) / math.log(x) for i in range(N)) / N, math.log(2), rel_tol=1e-6)   # C.8, b = 1

S = {5: "&#9733;", 10: "&#9733;&#9733;", 15: "&#9733;&#9733;&#9733;"}


def P(n, sub, pts, prompt, answer, steps, proof=False):
    stem = f'<p class="tool"><b>Tool &rarr; use ({sub}).</b> {TOOL[sub]}</p><p>{prompt}</p>'
    return FRQ(n, sub, S[pts], stem, answer, steps, pts=pts, lead="Key idea" if proof else "Answer",
               rubric=proof_rubric(pts), ask="Your proof." if proof else "Your work and answers.")


FRS = [
    # A Computer science
    P("A.1", "A.i", 10, r"Using integral bounds on $\sum\ln k$, prove $n\ln n - n + 1 \le \ln n! \le (n + 1)\ln(n + 1) - n$. Conclude $\log_2 n! = \Theta(n\log n)$, and explain why this gives a lower bound for comparison sorting.",
      r"$\log_2 n! = \Theta(n\log n)$: sandwich $\sum\ln k$ between integrals; a decision tree with $n!$ leaves has height $\ge \log_2 n!$.",
      [r"$\ln$ is increasing, so $\int_{k-1}^k\ln x\,dx \le \ln k \le \int_k^{k+1}\ln x\,dx$. Sum over $k = 2, \dots, n$: $\int_1^n\ln x\,dx \le \ln n! \le \int_2^{n+1}\ln x\,dx \le \int_1^{n+1}\ln x\,dx$.",
       r"With $\int_1^m\ln x\,dx = m\ln m - m + 1$: $n\ln n - n + 1 \le \ln n! \le (n + 1)\ln(n + 1) - n$.",
       r"Both bounds are $\sim n\ln n$, so $\ln n! \sim n\ln n$ and $\log_2 n! = \Theta(n\log n)$.",
       r"A comparison sort is a binary decision tree that must distinguish all $n!$ input orders. A binary tree of height $h$ has at most $2^h$ leaves, so the worst case needs $h \ge \log_2 n! = \Omega(n\log n)$ comparisons."], proof=True),
    P("A.2", "A.i", 5, r"Prove $n^{100} = o(1.01^n)$.", r"The ratio of consecutive terms tends to $1/1.01 < 1$, so the terms are eventually geometric.",
      [r"Let $a_n = n^{100}/1.01^n$. Then $\dfrac{a_{n+1}}{a_n} = \dfrac{(1 + 1/n)^{100}}{1.01} \to \dfrac1{1.01} < 1$.",
       r"So for some $r < 1$ and all $n \ge N$, $a_{n+1} \le ra_n$, which gives $a_n \le a_Nr^{n-N} \to 0$."], proof=True),
    P("A.3", "A.i", 10, r"The coupon-collector time $T$ for $n$ coupons has $\mathbb E[T] = nH_n$. Show $\mathbb E[T] \sim n\ln n$, and evaluate it for $n = 100$.",
      r"$\mathbb E[T] \sim n\ln n$; $\mathbb E[T] \approx 518.7$ for $n = 100$.",
      [r"Integral test with $f(x) = 1/x$: $\ln(n + 1) \le H_n \le 1 + \ln n$.",
       r"Divide by $\ln n$: both bounds tend to 1 (squeeze), so $H_n \sim \ln n$ and $\mathbb E[T] = nH_n \sim n\ln n$.",
       r"$H_{100} \approx 5.1874$, so $\mathbb E[T] \approx 518.7$.",
       r"The crude estimate $n\ln n \approx 460.5$ misses the constant: $H_n = \ln n + \gamma + o(1)$ with $\gamma \approx 0.5772$."]),
    P("A.4", "A.ii", 5, r"Bisection on $[1, 2]$ for $x^2 - 2 = 0$: how many steps guarantee an interval of width $< 10^{-9}$ containing $\sqrt2$?", "30 steps.",
      [r"Each step halves $[a_k, b_k]$ with $f(a_k) < 0 < f(b_k)$; by the IVT a root stays inside, and by nested intervals the endpoints converge to it.",
       r"The width after $n$ steps is $2^{-n}$.",
       r"$2^{29} \approx 5.4\times10^8 < 10^9 < 2^{30} \approx 1.07\times10^9$, so 30 steps suffice and 29 do not."]),
    P("A.5", "A.ii", 10, r"For Newton&rsquo;s method on $f(x) = x^2 - 2$, show that $x_{n+1} - \sqrt2 = \frac{(x_n - \sqrt2)^2}{2x_n}$ exactly. Starting at $x_0 = 1.5$, bound the error $e_3$.",
      r"$e_3 \approx 1.6\times10^{-12}$ (the bound $e_{n+1} \le e_n^2/2.8$ gives $e_3 < 2.2\times10^{-12}$).",
      [r"$x_{n+1} = x_n - \dfrac{x_n^2 - 2}{2x_n} = \dfrac{x_n^2 + 2}{2x_n}$, so $x_{n+1} - \sqrt2 = \dfrac{x_n^2 - 2\sqrt2x_n + 2}{2x_n} = \dfrac{(x_n - \sqrt2)^2}{2x_n}$.",
       r"Every iterate after $x_0$ is $\ge \sqrt2$ (AM&ndash;GM), and $x_0 = 1.5$, so $x_n > 1.4$ and $e_{n+1} \le e_n^2/2.8$.",
       r"Numerically $e_0 = 0.0858$, $e_1 = 2.45\times10^{-3}$, $e_2 = 2.12\times10^{-6}$, $e_3 = 1.59\times10^{-12}$: the correct digits roughly double each step.",
       r"(It is the same iteration as Problem Set 1.4.)"]),
    P("A.6", "A.ii", 10, r"How many trapezoid subintervals guarantee $|E| < 10^{-6}$ for $\int_0^1e^x\,dx$?", r"$n = 476$.",
      [r"On one subinterval of width $h$, Taylor (or the interpolation error formula) gives an error of $-\dfrac{h^3}{12}f''(\xi)$.",
       r"Summing $n = 1/h$ of them: $|E| \le \dfrac{h^2}{12}\max|f''| = \dfrac{e}{12n^2}$ for $f = e^x$ on $[0, 1]$.",
       r"$\dfrac{e}{12n^2} < 10^{-6} \iff n > \sqrt{e\cdot10^6/12} \approx 475.94$, so $n = 476$."]),
    P("A.7", "A.iii", 10, r"Prove that the set of computable reals is countable and has Lebesgue measure 0. Conclude that almost every real number is uncomputable.",
      r"Programs are finite strings: a countable union of finite sets. Countable sets are null.",
      [r"Let $\Sigma$ be the finite alphabet. The programs form a subset of $\bigcup_{k\ge1}\Sigma^k$, a countable union of finite sets, so they are countable.",
       r"Each computable real is the output of at least one program, so the computable reals are the image of a countable set: countable.",
       r"Countable sets have measure 0 (Problem Sets, 8.1), so the uncomputable reals have full measure in every interval.",
       r"Diagonalizing against the list of computable reals gives a real not on the list, but that diagonal cannot be computed: the content of the halting problem."], proof=True),
    P("A.8", "A.iv", 15, r"Prove that $F$ maps $\Delta$ into $\Delta$ and is a $d$-contraction in $\|\cdot\|_1$. With $d = 0.85$, how many iterations from any starting $x_0 \in \Delta$ guarantee $\|x_k - x^*\|_1 < 10^{-8}$?",
      r"$k = 118$.",
      [r"For $x \in \Delta$: $F(x) \ge 0$ and $\mathbf 1^\top F(x) = d\,\mathbf 1^\top Px + (1 - d) = d + (1 - d) = 1$, using $\mathbf 1^\top P = \mathbf 1^\top$. So $F(\Delta) \subseteq \Delta$.",
       r"$\|Pv\|_1 = \sum_i\left|\sum_jP_{ij}v_j\right| \le \sum_j|v_j|\sum_iP_{ij} = \|v\|_1$, so $\|F(x) - F(y)\|_1 = d\|P(x - y)\|_1 \le d\|x - y\|_1$.",
       r"$\Delta$ is closed in $\mathbb R^n$, hence complete: Banach gives a unique $x^*$.",
       r"$\|x_k - x^*\|_1 \le d^k\|x_0 - x^*\|_1 \le 2d^k$ (the $\ell^1$ diameter of $\Delta$ is 2).",
       r"$2(0.85)^k < 10^{-8} \iff k > \dfrac{\ln(2\times10^8)}{-\ln 0.85} \approx 117.6$, so $k = 118$."]),
    # B AI and machine learning
    P("B.1", "B.i", 10, r"Prove the descent lemma. Deduce that GD with $\eta = 1/L$ satisfies $f(x_{k+1}) \le f(x_k) - \frac1{2L}\|\nabla f(x_k)\|^2$ and $\min_{k<K}\|\nabla f(x_k)\|^2 \le \frac{2L(f(x_0) - f^*)}{K}$.",
      r"FTC along the segment plus the Lipschitz bound; then telescope. Rate $O(1/K)$ for $\min\|\nabla f\|^2$.",
      [r"Let $h = y - x$. FTC for $t \mapsto f(x + th)$: $f(y) - f(x) - \nabla f(x)\cdot h = \int_0^1(\nabla f(x + th) - \nabla f(x))\cdot h\,dt \le \int_0^1Lt\|h\|^2\,dt = \frac L2\|h\|^2$ (Cauchy&ndash;Schwarz and the Lipschitz bound).",
       r"For GD take $y = x_k - \frac1L g$ with $g = \nabla f(x_k)$: $f(x_{k+1}) \le f(x_k) - \frac1L\|g\|^2 + \frac1{2L}\|g\|^2 = f(x_k) - \frac1{2L}\|g\|^2$.",
       r"Sum over $k < K$ (telescoping): $\frac1{2L}\sum_{k<K}\|\nabla f(x_k)\|^2 \le f(x_0) - f(x_K) \le f(x_0) - f^*$.",
       r"The minimum is at most the average, which gives the bound."], proof=True),
    P("B.2", "B.i", 10, r"Let $f(x) = \frac12x^\top Ax$ with $A$ symmetric and eigenvalues in $[1, 10]$. Find the step size $\eta$ that minimizes the contraction factor of GD, the factor itself, and the number of steps needed to shrink $\|x_k\|$ by $10^{-6}$.",
      r"$\eta^* = \tfrac2{11}$, $q = \tfrac9{11}$, $k = 69$.",
      [r"The minimizer is 0 and $x_{k+1} = (I - \eta A)x_k$. Diagonalizing, $\|x_{k+1}\| \le \max_{\lambda\in[1,10]}|1 - \eta\lambda|\,\|x_k\|$.",
       r"$\lambda \mapsto 1 - \eta\lambda$ is monotone, so the max is at an endpoint: $q(\eta) = \max(|1 - \eta|, |1 - 10\eta|)$.",
       r"Minimized where $1 - \eta = -(1 - 10\eta)$: $\eta = \tfrac2{11}$, $q = \tfrac9{11}$ (in general $\frac{L - \mu}{L + \mu}$).",
       r"$q^k < 10^{-6} \iff k > \dfrac{6\ln 10}{\ln(11/9)} \approx 68.85$, so $k = 69$."]),
    P("B.3", "B.i", 5, r"For GD on $f(x) = x^2$, find exactly which step sizes $\eta > 0$ converge.", r"$0 < \eta < 1$.",
      [r"$f'(x) = 2x$, so $x_{k+1} = (1 - 2\eta)x_k$ and $x_k = (1 - 2\eta)^kx_0$.",
       r"This tends to 0 for every $x_0$ iff $|1 - 2\eta| < 1$ iff $0 < \eta < 1$.",
       r"At $\eta = 1$, $x_k = (-1)^kx_0$ oscillates; for $\eta > 1$, $|x_k| \to \infty$. The threshold is $\eta = 2/L$ with $L = 2$."]),
    P("B.4", "B.ii", 10, r"For $\alpha_k = k^{-p}$, find all $p$ satisfying both conditions. Explain what fails at $p = \frac12$ and at $p = 2$.", r"$p \in (\tfrac12, 1]$.",
      [r"$\sum k^{-p} = \infty \iff p \le 1$, and $\sum k^{-2p} < \infty \iff 2p > 1$. Both hold iff $\tfrac12 < p \le 1$.",
       r"At $p = \tfrac12$: $\sum\alpha_k^2 = \sum\frac1k = \infty$, so the noise variance accumulates without bound and the iterates keep jittering.",
       r"At $p = 2$: $\sum\alpha_k < \infty$, so the total movement is finite and from a bad start the iterates may stop short of the optimum."]),
    P("B.5", "B.iii", 15, r"Prove that for every continuous $f: [0, 1] \to \mathbb R$ and $\varepsilon > 0$, there is a one-hidden-layer ReLU network $g$ with $\|f - g\|_\infty < \varepsilon$.",
      r"Heine&ndash;Cantor gives $\delta$; interpolate on knots spaced $< \delta$ and write the interpolant as a ReLU sum with the slope changes as weights.",
      [r"Heine&ndash;Cantor: pick $\delta$ with $|x - y| < \delta \Rightarrow |f(x) - f(y)| < \varepsilon$. Take knots $0 = t_0 < t_1 < \cdots < t_m = 1$ with spacing $< \delta$; let $L$ interpolate $f$ at the knots.",
       r"For $x \in [t_{i-1}, t_i]$, $L(x)$ is a convex combination of $f(t_{i-1})$ and $f(t_i)$, each within $\varepsilon$ of $f(x)$; so $|L(x) - f(x)| < \varepsilon$, and $\|f - L\|_\infty < \varepsilon$ by compactness.",
       r"Let $s_i$ be the slope of $L$ on $[t_{i-1}, t_i]$ and $s_0 := 0$. Then $L(x) = f(0) + \sum_{i=1}^m(s_i - s_{i-1})\,\mathrm{ReLU}(x - t_{i-1})$ on $[0, 1]$.",
       r"Both sides are continuous, agree at 0, and have the same slope on each piece. This is a one-hidden-layer ReLU network with $m$ units."], proof=True),
    P("B.6", "B.iv", 10, r"(a) Show $\sigma(x) = \frac1{1 + e^{-x}}$ has $\sup|\sigma'| = \frac14$. (b) Bound $\mathrm{Lip}(x \mapsto W_2\,\mathrm{ReLU}(W_1x))$ when $\|W_1\|_2 = 3$ and $\|W_2\|_2 = 2$. (c) For $h_{j+1} = \sigma(wh_j)$ with scalar $w$, bound $|\partial h_k/\partial h_0|$.",
      r"(a) $\tfrac14$ (b) 6 (c) $(|w|/4)^k$.",
      [r"(a) $\sigma' = \sigma(1 - \sigma)$, and $s(1 - s) \le \tfrac14$ for $s \in (0, 1)$, with equality at $s = \tfrac12$, i.e. $x = 0$. By the MVT, $\mathrm{Lip}(\sigma) = \tfrac14$.",
       r"(b) $\mathrm{Lip} \le \|W_2\|_2\cdot\mathrm{Lip}(\mathrm{ReLU})\cdot\|W_1\|_2 = 2\cdot1\cdot3 = 6$ (ReLU acts coordinatewise and is 1-Lipschitz in each coordinate).",
       r"(c) Chain rule: $\dfrac{\partial h_k}{\partial h_0} = \prod_{j<k}w\sigma'(wh_j)$, so $|\cdot| \le (|w|/4)^k$.",
       r"For $|w| < 4$ this decays exponentially in depth: the vanishing-gradient problem, and why ReLU (derivative 1 on the active side) and residual connections help."]),
    P("B.7", "B.v", 15, r"Prove $\|TV - TW\|_\infty \le \gamma\|V - W\|_\infty$ and conclude that value iteration converges to a unique $V^*$.",
      r"$|\max f - \max g| \le \max|f - g|$, and each transition row is a probability vector; then Banach.",
      [r"On a finite set, $\max f - \max g \le \max(f - g)$: if $\max f = f(a^*)$, then $\max f - \max g \le f(a^*) - g(a^*)$. By symmetry, $|\max f - \max g| \le \max|f - g|$.",
       r"Hence for each $s$: $|TV(s) - TW(s)| \le \gamma\max_a|\Delta_a(s)|$ with $\Delta_a(s) = \sum_{s'}P(s'|s, a)\,(V - W)(s')$, and $|\Delta_a(s)| \le \|V - W\|_\infty$, because each row $P(\cdot|s, a)$ is a probability vector.",
       r"$(\mathbb R^S, \|\cdot\|_\infty)$ is complete, so Banach gives a unique fixed point $V^*$ (the Bellman optimality equation).",
       r"And $V_{k+1} = TV_k \to V^*$ with $\|V_k - V^*\|_\infty \le \gamma^k\|V_0 - V^*\|_\infty$."], proof=True),
    P("B.8", "B.v", 5, r"With $\gamma = 0.9$, rewards in $[0, 1]$, and $V_0 = 0$, how many value-iteration steps guarantee $\|V_k - V^*\|_\infty < 0.01$?", r"$k = 66$.",
      [r"Rewards in $[0, 1]$ give $0 \le V^* \le \sum_t\gamma^t = \dfrac1{1 - \gamma} = 10$, so $\|V_0 - V^*\|_\infty \le 10$.",
       r"Need $10(0.9)^k < 0.01$, i.e. $k > \dfrac{\ln 1000}{-\ln 0.9} \approx 65.56$, so $k = 66$."]),
    P("B.9", "B.vi", 10, r"Let $\mathbb E[Z^2] < \infty$ and $L(\theta) = \mathbb E[(\theta - Z)^2]$. Using DCT, prove $L'(\theta) = \mathbb E[2(\theta - Z)]$, and find the minimizer.",
      r"$L'(\theta) = 2(\theta - \mathbb EZ)$; the minimizer is $\theta = \mathbb EZ$.",
      [r"For $0 < |h| \le 1$: $\dfrac{(\theta + h - Z)^2 - (\theta - Z)^2}{h} = 2(\theta - Z) + h \to 2(\theta - Z)$.",
       r"It is dominated: $|2(\theta - Z) + h| \le 2|\theta| + 2|Z| + 1 =: G$, and $\mathbb E|Z| \le (\mathbb EZ^2)^{1/2} < \infty$, so $\mathbb EG < \infty$.",
       r"DCT along any $h_k \to 0$: $L'(\theta) = \mathbb E[2(\theta - Z)] = 2(\theta - \mathbb EZ)$.",
       r"This vanishes only at $\theta = \mathbb EZ$, and $L'' = 2 > 0$: the mean minimizes squared loss, and a single-sample gradient $2(\theta - Z_i)$ is an unbiased estimate of $L'(\theta)$."]),
    P("B.10", "B.vii", 10, r"Prove $\max_ix_i \le \mathrm{LSE}(x) \le \max_ix_i + \ln n$, and deduce $\lim_{\tau\to0^+}\tau\,\mathrm{LSE}(x/\tau) = \max_ix_i$.",
      r"$e^m \le \sum e^{x_i} \le ne^m$ with $m = \max_ix_i$; scale and squeeze.",
      [r"Let $m = \max_ix_i$. Then $e^m \le \sum_ie^{x_i} \le ne^m$; take logs: $m \le \mathrm{LSE}(x) \le m + \ln n$.",
       r"Apply this to $x/\tau$ (whose max is $m/\tau$) and multiply by $\tau > 0$: $m \le \tau\,\mathrm{LSE}(x/\tau) \le m + \tau\ln n$.",
       r"Let $\tau \to 0^+$ and squeeze.",
       r"(Also $\partial_i\,\mathrm{LSE} = e^{x_i}/\sum_je^{x_j}$, the softmax; as $\tau \to 0$ it concentrates on the argmax.)"], proof=True),
    # C Physics
    P("C.1", "C.i", 5, r"Using $\theta - \frac{\theta^3}{6} \le \sin\theta \le \theta$ for $\theta \ge 0$, find the largest amplitude for which the small-angle approximation $\sin\theta \approx \theta$ has relative error below 1%.",
      r"$\theta < 0.245$ rad $\approx 14.0^\circ$.",
      [r"For $\theta > 0$ the Taylor bounds give $0 \le \dfrac{\theta - \sin\theta}{\theta} \le \dfrac{\theta^2}{6}$.",
       r"The relative error is below 1% whenever $\theta^2/6 < 0.01$, i.e. $\theta < \sqrt{0.06} = 0.2449$ rad $= 14.03^\circ$.",
       r"The bound is sharp to leading order, since $\dfrac{\theta - \sin\theta}{\theta} = \dfrac{\theta^2}{6} + O(\theta^4)$."]),
    P("C.2", "C.i", 10, r"For the Lennard-Jones potential $V(r) = 4\varepsilon\left[(\sigma/r)^{12} - (\sigma/r)^6\right]$, find the equilibrium $r_0$ and the small-oscillation frequency $\omega$ for reduced mass $m$.",
      r"$r_0 = 2^{1/6}\sigma$; $\omega = \sqrt{\dfrac{72\varepsilon}{2^{1/3}m\sigma^2}}$.",
      [r"$V'(r) = 4\varepsilon\left[-12\sigma^{12}r^{-13} + 6\sigma^6r^{-7}\right] = 0 \iff r^6 = 2\sigma^6$, so $r_0 = 2^{1/6}\sigma$.",
       r"$V''(r) = 4\varepsilon\left[156\sigma^{12}r^{-14} - 42\sigma^6r^{-8}\right]$. At $r_0$: $\sigma^{12}/r_0^{12} = \tfrac14$ and $\sigma^6/r_0^6 = \tfrac12$.",
       r"So $V''(r_0) = \dfrac{4\varepsilon}{r_0^2}(39 - 21) = \dfrac{72\varepsilon}{2^{1/3}\sigma^2} > 0$: a minimum.",
       r"Taylor: $V \approx V(r_0) + \tfrac12V''(r_0)(r - r_0)^2$, so $\omega = \sqrt{V''(r_0)/m} = \sqrt{72\varepsilon/(2^{1/3}m\sigma^2)}$."]),
    P("C.3", "C.ii", 10, r"Show that $y' = 2\sqrt{|y|}$, $y(0) = 0$ has infinitely many solutions on $[0, \infty)$, and identify the hypothesis of Picard&ndash;Lindel&ouml;f that fails.",
      r"$y_c = (t - c)^2\mathbf 1_{t\ge c}$ for every $c \ge 0$; $\sqrt{|y|}$ is not Lipschitz at $y = 0$.",
      [r"For $c \ge 0$ let $y_c(t) = 0$ for $t < c$ and $(t - c)^2$ for $t \ge c$. Then $y_c$ is $C^1$ with $y_c' = 2(t - c)$ for $t \ge c$ and 0 before.",
       r"$2\sqrt{|y_c|} = 2|t - c| = 2(t - c)$ for $t \ge c$, so every $y_c$ solves the IVP, as does $y \equiv 0$.",
       r"Picard&ndash;Lindel&ouml;f needs $F(y) = 2\sqrt{|y|}$ Lipschitz near $y_0 = 0$, but $\dfrac{F(y) - F(0)}{y} = \dfrac2{\sqrt y} \to \infty$ as $y \to 0^+$.",
       r"(Norton&rsquo;s dome is the mechanical version: a particle at rest at the apex may start sliding at any time.)"], proof=True),
    P("C.4", "C.ii", 10, r"For $y' = y$, $y(0) = 1$, compute the Picard iterates $y_{n+1} = Ty_n$ from $y_0 \equiv 1$, and show $T$ is a contraction on $C[-h, h]$ for $h < 1$.",
      r"$y_n = \sum_{k\le n}t^k/k! \to e^t$.",
      [r"$(Ty)(t) = 1 + \int_0^ty(s)\,ds$.",
       r"If $y_n = \sum_{k\le n}t^k/k!$, then $y_{n+1} = 1 + \sum_{k\le n}\dfrac{t^{k+1}}{(k + 1)!} = \sum_{k\le n+1}\dfrac{t^k}{k!}$; $y_0 = 1$ starts the induction.",
       r"On $[-h, h]$: $|(Ty)(t) - (Tz)(t)| \le \left|\int_0^t|y - z|\right| \le h\|y - z\|_\infty$, so $T$ is an $h$-contraction for $h < 1$.",
       r"Banach gives a unique solution, and the iterates converge uniformly to the exponential series $e^t$."]),
    P("C.5", "C.iii", 15, r"Solve the problem with $f \equiv 1$ on $(0, \pi)$. Prove that for $t \ge t_0 > 0$ the series and all its $x$- and $t$-derivatives converge uniformly.",
      r"$u = \sum_{n\text{ odd}}\dfrac4{n\pi}e^{-\kappa n^2t}\sin nx$.",
      [r"$b_n = \dfrac2\pi\int_0^\pi\sin nx\,dx = \dfrac2\pi\cdot\dfrac{1 - \cos n\pi}{n}$: $\dfrac4{n\pi}$ for odd $n$, 0 for even $n$.",
       r"Fix $t_0 > 0$. Any derivative $\partial_x^a\partial_t^b$ of the $n$-th term is bounded on $[0, \pi]\times[t_0, \infty)$ by $M_n = \dfrac4\pi n^{a+2b-1}\kappa^be^{-\kappa n^2t_0}$.",
       r"$\sum M_n < \infty$ (ratio test, or $n^je^{-cn^2} \le C_jn^{-2}$), so the M-test gives uniform convergence of every derivative series.",
       r"Termwise differentiation makes $u$ $C^\infty$ for $t > 0$; each term solves $u_t = \kappa u_{xx}$ and the boundary conditions, so $u$ does too.",
       r"As $t \to 0^+$, $u(\cdot, t) \to f$ in $L^2$ but not uniformly (Gibbs phenomenon at the jumps)."]),
    P("C.6", "C.iii", 10, r"Using Parseval for sine series, $\int_0^\pi g^2 = \frac\pi2\sum b_n^2$, write $E(t) = \int_0^\pi u(x, t)^2\,dx$ as a series. Show that $E$ is nonincreasing, and evaluate $E(0)$ to obtain $\sum_{n\text{ odd}}n^{-2}$.",
      r"$E(t) = \dfrac8\pi\sum_{\text{odd}}\dfrac{e^{-2\kappa n^2t}}{n^2}$; $\sum_{\text{odd}}\dfrac1{n^2} = \dfrac{\pi^2}{8}$.",
      [r"For fixed $t$, the coefficients of $u(\cdot, t)$ are $b_ne^{-\kappa n^2t}$, so $E(t) = \dfrac\pi2\sum b_n^2e^{-2\kappa n^2t} = \dfrac\pi2\sum_{\text{odd}}\dfrac{16}{n^2\pi^2}e^{-2\kappa n^2t} = \dfrac8\pi\sum_{\text{odd}}\dfrac{e^{-2\kappa n^2t}}{n^2}$.",
       r"Each term is nonincreasing in $t$, so $E$ is too: heat flow dissipates the $L^2$ energy.",
       r"$E(0) = \int_0^\pi1\,dx = \pi$, so $\pi = \dfrac8\pi\sum_{\text{odd}}n^{-2}$, i.e. $\sum_{n\text{ odd}}\dfrac1{n^2} = \dfrac{\pi^2}{8}$.",
       r"(Consistent with $\zeta(2) = \pi^2/6$: the odd terms are $\tfrac34$ of the total.)"]),
    P("C.7", "C.iv", 10, r"A 1D chain has alternating charges $\pm q$ at spacing $a$. Compute the Madelung constant $M$ for one ion, and explain why &ldquo;summing in some order&rdquo; is not enough to define it.",
      r"$M = 2\ln 2 \approx 1.386$.",
      [r"Put the reference ion $(+q)$ at 0. The ions at $\pm na$ have charge $(-1)^nq$, so $U = \sum_{n\ne0}\dfrac{q\cdot(-1)^nq}{|n|a} = -\dfrac{q^2}{a}\cdot2\sum_{n\ge1}\dfrac{(-1)^{n+1}}{n} = -\dfrac{q^2}{a}\cdot2\ln 2$ (Problem Sets, 2.5).",
       r"So $M = 2\ln 2 \approx 1.386$.",
       r"$\sum(-1)^{n+1}/n$ converges only conditionally. By Riemann&rsquo;s theorem, reordering the ions (for example, two far negative ions for every positive one) can make the sum anything.",
       r"A definite answer needs a definite rule: add charge-neutral groups in order of distance, which Ewald summation does systematically in 3D."]),
    P("C.8", "C.v", 10, r"Compute $I(b) = \int_0^1\frac{x^b - 1}{\ln x}\,dx$ for $b \ge 0$, justifying differentiation under the integral sign.", r"$I(b) = \ln(1 + b)$.",
      [r"$g(x, b) = \dfrac{x^b - 1}{\ln x}$ is bounded on $(0, 1)$ for each $b$: it tends to 0 as $x \to 0^+$ and to $b$ as $x \to 1^-$.",
       r"$\partial_bg = x^b$ and $|x^b| \le 1$ for $b \ge 0$. By the MVT the difference quotients equal $x^{b+\theta h}$, bounded by 1, which is integrable on $[0, 1]$ (for $b + h \ge 0$).",
       r"DCT gives $I'(b) = \int_0^1x^b\,dx = \dfrac1{b + 1}$.",
       r"$I(0) = 0$, so the FTC gives $I(b) = \ln(1 + b)$."]),
    P("C.9", "C.vi", 10, r"Show $\frac1N\ln\binom{N}{pN} \to H(p) = -p\ln p - (1 - p)\ln(1 - p)$ as $N \to \infty$ with $pN \in \mathbb N$.",
      r"Stirling on the three factorials: the $N\ln N$ and $-N$ terms cancel, leaving $-N[p\ln p + (1 - p)\ln(1 - p)] + O(\ln N)$.",
      [r"Write $k = pN$. Stirling, $\ln m! = m\ln m - m + O(\ln m)$, gives $\ln\binom Nk = N\ln N - N - (k\ln k - k) - ((N - k)\ln(N - k) - (N - k)) + O(\ln N)$.",
       r"$= N\ln N - pN\ln(pN) - (1 - p)N\ln((1 - p)N) + O(\ln N) = -N[p\ln p + (1 - p)\ln(1 - p)] + O(\ln N)$.",
       r"Divide by $N$; the error term $O(\ln N)/N$ tends to 0, leaving $H(p)$.",
       r"Multiplying by $k_B$ gives Boltzmann&rsquo;s $S = k_B\ln W \approx Nk_BH(p)$, the entropy of mixing."], proof=True),
    P("C.10", "C.vii", 15, r"(a) For $\phi_n = \frac n2\mathbf 1_{[-1/n,1/n]}$ and $f$ bounded and continuous at 0, prove $\int f\phi_n \to f(0)$. (b) Prove that there is no $\delta \in L^1(\mathbb R)$ with $\int f\delta = f(0)$ for every bounded continuous $f$.",
      r"(a) $\left|\int f\phi_n - f(0)\right| \le \sup_{|x|\le1/n}|f(x) - f(0)|$. (b) Tents $f_k \to \mathbf 1_{\{0\}}$, and DCT gives $\int f_k\delta \to 0 \ne 1$.",
      [r"(a) Since $\int\phi_n = 1$: $\left|\int f\phi_n - f(0)\right| = \left|\int(f(x) - f(0))\phi_n(x)\,dx\right| \le \sup_{|x|\le1/n}|f(x) - f(0)|\cdot\int\phi_n \to 0$ by continuity at 0.",
       r"(b) Suppose $\delta \in L^1$ works. Let $f_k$ be the tent of height 1 on $[-\frac1k, \frac1k]$: bounded, continuous, $f_k(0) = 1$, so $\int f_k\delta = 1$ for all $k$.",
       r"But $f_k(x) \to 0$ for every $x \ne 0$, so $f_k\delta \to 0$ a.e., and $|f_k\delta| \le |\delta| \in L^1$. DCT gives $\int f_k\delta \to 0$: contradiction.",
       r"So $\delta$ is not a function. It is the continuous linear functional $f \mapsto f(0)$: a distribution."], proof=True),
]
assert sum(f["parts"][0]["max"] for f in FRS) == 280 and len(FRS) == 28
QS = []
