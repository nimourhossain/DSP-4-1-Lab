import numpy as np
import matplotlib.pyplot as plt

sr = 100
ts = 1.0 / sr
t = np.arange(0, 1, ts)

freq = 1
x = 8 * np.sin(2 * np.pi * freq * t)

plt.figure(figsize=(8, 6))
plt.stem(t, x, 'r')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('1 Hz Sine Wave')
plt.show()
