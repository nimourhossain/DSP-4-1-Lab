import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Input signal ----------------
x = [1, 2, 3]       # your discrete signal
N = len(x)
z = sp.symbols('z')

# ---------------- Z-transform ----------------
Xz = sum(x[k] * z**(-k) for k in range(N))
Xz = sp.simplify(Xz)

# ---------------- Denominator ----------------
Xz_frac = sp.together(Xz)
_, den = sp.fraction(Xz_frac)
den_poly = sp.Poly(den, z)

# ---------------- Poles ----------------
poles = sp.solve(den, z)
print("Poles:", poles)

# ---------------- ROC ----------------
# For finite-length right-sided (causal) signal
roc_radius = max([abs(p) for p in poles])
roc = f"|z| > {roc_radius}"
print("ROC:", roc)

# ---------------- Convert poles to float ----------------
poles_f = [complex(sp.re(pv), sp.im(pv)) for pv in poles]

# ---------------- Plot Z-plane with ROC ----------------
fig, ax = plt.subplots(figsize=(6,6))
ax.set_title("Poles and ROC in Z-plane")
ax.set_xlabel("Re{z}")
ax.set_ylabel("Im{z}")
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

# Unit circle
theta = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(theta), np.sin(theta), 'k--', label='Unit circle')

# Poles
ax.scatter([pv.real for pv in poles_f], [pv.imag for pv in poles_f], marker='x', s=100, color='red', label='Poles')

# ROC shading (circle outside max pole)
roc_circle = plt.Circle((0,0), roc_radius, color='green', alpha=0.2, label='ROC')
ax.add_patch(roc_circle)

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.grid(True)
ax.legend()
plt.show()
