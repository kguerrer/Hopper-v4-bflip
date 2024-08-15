import numpy as np
import matplotlib.pyplot as plt

def gauss(x, mu, sigma):
    return np.exp(-((x - mu) / sigma) ** 2)

def hea(x, threshold=0.0):
    return 1 if x > threshold else 0.0

def inv_hea(x, threshold=0.0):
    return 1 if x < threshold else 0.0

def porte(x, a, b):
    return hea(x, a) + hea(-x, -b)

def gaussp(x, mu, sigma):
    return np.exp(-((x - mu) / sigma) ** 2) * porte(x, -sigma/2, sigma/2)