#! /usr/bin/env python
import math
R   = 1.e5
b   = 1.e-24
cse = 2.e-6 * b
csc = 7.e-3 * b
csf = 20.e-3 * b

Na  = 6.022e23  # avogadro's
pd  = 0.1       # kg/(m*m)
pd  = pd*Na*(1./100.**2)/(0.235)

cs_tot = cse + csc + csf

A = 1 - pd*cs_tot

# Rate of fissions
R_fis = R*pd*csf

# Flux per unit area from scattering 10 m away
F_e = R*pd*cse/(4*math.pi*(10**2))
