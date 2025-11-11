import numpy as np
import matplotlib.pyplot as plt

sr = 100
ts = 1.0/sr

t = np.arange(0,1,ts)
f = 1

x = 8*np.sin(2*np.pi*f*t)

plt.figure(figsize=(8,6))
plt.stem(t,x,'r')
plt.show()