import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 0]
x = np.array(x, dtype=complex)
if len(x) < 4:
    x = np.pad(x, (0, 4-len(x)))
else:
    x = x[:4]

X = np.fft.fft(x, n=4)
mag = np.abs(X)
phase = np.angle(X)
real_part = X.real
imag_part = X.imag

print("x[n] =", x)
print("X[k] =", X)
print("Magnitude =", mag)
print("Phase =", phase)
print("Real part =", real_part)
print("Imag part =", imag_part)

k = np.arange(4)
plt.figure(figsize=(8,6))
plt.subplot(2,2,1)
plt.stem(k, real_part, basefmt=" ")
plt.title("Real Part of X[k]")

plt.subplot(2,2,2)
plt.stem(k, imag_part, basefmt=" ")
plt.title("Imaginary Part of X[k]")

plt.subplot(2,2,3)
plt.stem(k, mag, basefmt=" ")
plt.title("Magnitude |X[k]|")

plt.subplot(2,2,4)
plt.stem(k, phase, basefmt=" ")
plt.title("Phase ∠X[k]")

plt.tight_layout()
plt.show()
