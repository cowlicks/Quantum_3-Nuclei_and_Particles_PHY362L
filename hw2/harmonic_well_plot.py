#! /usr/bin/env python
import math
import numpy 
import pylab

hbar    = 6.58212e-16 # eV*s
def F(theta):
    alph    = 4./3.
    a       = 1.64e-15
    po      = 1.        #### must change to 420 MeV then rescale.
    const   = 2. /(a**3 * math.sqrt(3) * (2 + 3*alph))
    q       = 2. * po * math.sin(theta/2)
    f       = const * math.exp(-q**2 * (a/hbar)**2 /4)*(1 - (q**2 * (a/hbar)**2 * alph)/(4 + 6*alph))
    return abs(f)**2

q = numpy.arange(0.0, 3., 1.e-4)
s = []
for i in q:
    s.append(F(i))
pylab.plot(q, s)
pylab.yscale('log')
pylab.xlabel('q in ev/c')
pylab.ylabel('F(q**2)')
pylab.grid(True)
pylab.savefig('prob10plot')

pylab.show()
