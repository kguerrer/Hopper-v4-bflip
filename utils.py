import numpy as np
import matplotlib.pyplot as plt

def gauss(x, mu, sigma):
    return np.exp(-((x - mu) / sigma) ** 2)

def hea(x, threshold=0.0):
    return 1 if x > threshold else 0.0

def inv_hea(x, threshold=0.0):
    return 1 if x < threshold else 0.0


A = np.linspace(-4*np.pi, 4*np.pi, 1000)
Y = []
for a in A:
    y = (inv_hea(a, -2*np.pi) + hea(a, -2*np.pi) * gauss(a, -2*np.pi, 0.2*2*np.pi))
    Y.append(y)
plt.figure()
plt.plot(A, Y)
plt.show()
