import numpy as np
import matplotlib.pyplot as plt
import math

def p(E, m, gam):
    return gam/(2 * math.pi * ((E - m)**2 + (gam/2)**2))

t = np.arange(1., 3000., 1.)

plt.figure(1)
plt.plot(t, p(t, 1230., 110.))
plt.show()
