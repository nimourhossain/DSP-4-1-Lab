import numpy as np

x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])

N = len(x)
M = len(h)
L = N + M - 1
pad = M - 1

x_padded = np.pad(x, (pad, pad))

conv = np.zeros(L)
corr = np.zeros(L)

for n in range(L):
    for k in range(M):
        conv[n] = conv[n] + x_padded[n + k] * h[M - 1 - k]

    for k in range(M):
        corr[n] = corr[n] + x_padded[n + k] * h[k]

print("Convolution:", conv.tolist())
print("Correlation:", corr.tolist())
