import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 2, 6])
N = len(x)
print(f"Length of x: {N}")

X = np.fft.fft(x)
n = np.arange(N)

plt.figure(figsize=(12,6))
plt.subplot(2,2,1)
plt.stem(n, x, basefmt=" ")
plt.title("Original signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(2,2,2)
plt.stem(np.arange(N), np.abs(X), basefmt=" ")
plt.title("DFT Magnitude |X[k]|")
plt.xlabel("k")
plt.ylabel("Magnitude")

plt.subplot(2,2,4)
plt.stem(np.arange(N), np.angle(X), basefmt=" ")
plt.title("DFT Phase ∠X[k]")
plt.xlabel("k")
plt.ylabel("Phase")

plt.tight_layout()
plt.show()

t = np.arange(N)
plt.figure(figsize=(10,6))
for k in range(N):
    component = (1/N) * X[k] * np.exp(1j*2*np.pi*k*t/N)
    print(component.real)
    plt.subplot(N, 1, k+1)
    plt.stem(t, component.real, basefmt=" ")
    plt.title(f"Frequency Component k={k}, f={k/N}")
    plt.ylabel("Real part")

plt.xlabel("n")
plt.tight_layout()
plt.show()
