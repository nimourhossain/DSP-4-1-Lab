import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Input signal ----------------
# Example: x[n] = [1, 2, 3] (finite-length discrete-time signal)
x = [1, 2, 3]
N = len(x)
n = sp.symbols('n', integer=True)
z = sp.symbols('z')

# ---------------- Z-transform ----------------
Xz = sum(x[k] * z**(-k) for k in range(N))
Xz = sp.simplify(Xz)
print("Z-transform X(z) =", Xz)

# ---------------- Numerator & Denominator ----------------
Xz_frac = sp.together(Xz)
num, den = sp.fraction(Xz_frac)
num_poly = sp.Poly(num, z)
den_poly = sp.Poly(den, z)
print("Numerator polynomial:", num_poly)
print("Denominator polynomial:", den_poly)

# ---------------- ROC ----------------
# For finite-length right-sided sequence, ROC is |z| > 0
roc = "|z| > 0"
print("ROC:", roc)

# ---------------- Zeros and Poles ----------------
zeros = sp.solve(num, z)
poles = sp.solve(den, z)
print("Zeros:", zeros)
print("Poles:", poles)

# Convert sympy numbers to Python complex for plotting
zeros_f = [complex(sp.re(zv), sp.im(zv)) for zv in zeros]
poles_f = [complex(sp.re(pv), sp.im(pv)) for pv in poles]

# ---------------- Plot Z-plane ----------------
fig, ax = plt.subplots(figsize=(6,6))
ax.set_title("Pole-Zero Plot with ROC")
ax.set_xlabel("Re{z}")
ax.set_ylabel("Im{z}")
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

# Unit circle
theta = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(theta), np.sin(theta), 'k--', label='Unit circle')

# Plot zeros and poles
ax.scatter([zv.real for zv in zeros_f], [zv.imag for zv in zeros_f], marker='o', s=100, color='blue', label='Zeros')
ax.scatter([pv.real for pv in poles_f], [pv.imag for pv in poles_f], marker='x', s=100, color='red', label='Poles')

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.grid(True)
ax.legend()
plt.show()
