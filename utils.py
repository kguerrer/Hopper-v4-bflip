import numpy

def gauss(x, mu, sigma):
    return numpy.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * numpy.sqrt(2 * numpy.pi))