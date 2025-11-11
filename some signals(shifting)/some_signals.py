import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)
x = np.array([abs(i) if -3 <= i <= 3 else 0 for i in n])

y_a = x
y_b = np.roll(x, 1)
y_c = np.roll(x, -1)
y_d = (np.roll(x,-1) + x + np.roll(x,1))/3
y_e = np.maximum(np.maximum(np.roll(x,-1), x), np.roll(x,1))
y_f = np.cumsum(x)

results = [y_a, y_b, y_c, y_d, y_e, y_f]
titles = ['(a) y(n) = x(n)',
          '(b) y(n) = x(n - 1)',
          '(c) y(n) = x(n + 1)',
          '(d) y(n) = (1/3)[x(n+1) + x(n) + x(n - 1)]',
          '(e) y(n) = max(x(n+1), x(n), x(n - 1))',
          '(f) y(n) = cumulative sum of x(k)']

fig, axs = plt.subplots(6, 1, figsize=(8,12), sharex=True)

for i in range(6):
    axs[i].stem(n, results[i], basefmt=" ")
    axs[i].set_ylabel("y(n)")
    axs[i].set_title(titles[i])
    axs[i].grid(True)

axs[-1].set_xlabel("n")
plt.tight_layout()
plt.show()
