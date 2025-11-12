import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,6)
t = np.linspace(0, 2, 200)

unit_sample = np.array([1 if i==0 else 0 for i in n])
unit_step = np.array([1 if i>=0 else 0 for i in n])
discrete_signal = n**2
continuous_signal = np.sin(2*np.pi*t)
exponential_signal = np.exp(0.5*n)
sinusoidal_signal = np.sin(np.pi*n/4)

print("n =", n)
print("Unit Sample delta[n] =", unit_sample)
print("Unit Step u[n] =", unit_step)
print("Discrete Signal n^2 =", discrete_signal)
print("Continuous Signal sin(2*pi*t) =", continuous_signal)
print("Exponential Signal e^(0.5*n) =", exponential_signal)
print("Sinusoidal Signal sin(pi*n/4) =", sinusoidal_signal)

plt.figure(figsize=(12,10))

plt.subplot(3,2,1)
plt.stem(n, unit_sample, basefmt=" ")
plt.title("Unit Sample delta[n]")

plt.subplot(3,2,2)
plt.stem(n, unit_step, basefmt=" ")
plt.title("Unit Step u[n]")

plt.subplot(3,2,3)
plt.stem(n, discrete_signal, basefmt=" ")
plt.title("Discrete Signal n^2")

plt.subplot(3,2,4)
plt.plot(t, continuous_signal)
plt.title("Continuous Signal sin(2πt)")

plt.subplot(3,2,5)
plt.stem(n, exponential_signal, basefmt=" ")
plt.title("Exponential Signal e^(0.5n)")

plt.subplot(3,2,6)
plt.stem(n, sinusoidal_signal, basefmt=" ")
plt.title("Sinusoidal Signal sin(πn/4)")

plt.tight_layout()
plt.show()
