import numpy as np
import matplotlib.pyplot as plt
import math


def f(E, V, a, m):
    hbar = 6.582e-16
    kp  = (1./hbar)*(2*m*(E - V))**.5
    return (1 + (V * V * (np.sin(kp*a)**2))/(4*E*(E-V)))

t = np.arange(0.01, .5, 1.e-4)

plt.figure(1)
plt.plot(t, f(t, -100.e-6, 20.e-15, 1000.e6))
plt.show()

