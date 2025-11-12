import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

z = sp.symbols('z')
x = [1, 2, 5, 0, 6, 3]

Xz = sum(x[n] * z**(-n) for n in range(len(x)))

print("Z-transform X(z):", Xz.simplify())

Xz_poly = sp.together(Xz * z**(len(x)-1)).as_numer_denom()[0]

print("Polynomial form:", Xz_poly)

coeffs = sp.Poly(Xz_poly, z).all_coeffs()
coeffs = [complex(c) for c in coeffs]

zeros = np.roots(coeffs)
poles = [0]*(len(x)-1)

plt.figure(figsize=(6,6))
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
plt.xlabel("Real")
plt.ylabel("Imag")
plt.title("Pole-Zero Plot")
plt.legend()
plt.grid(True)
plt.show()
