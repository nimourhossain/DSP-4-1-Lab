import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# উদাহরণ সিগন্যাল
x = np.array([1, 2, 3, 4])
y = np.array([0, 1, 0.5, 2])

# Cross-correlation
corr = correlate(x, y)
lags = np.arange(-len(y)+1, len(x))

# Output print
print("Cross-correlation:", corr)

# Plot
plt.stem(lags, corr, basefmt=" ")
plt.title("Cross-correlation of x(n) and y(n)")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.show()
