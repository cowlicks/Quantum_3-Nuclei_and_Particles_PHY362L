import math
peak    = 25
m       = 1820.e6
hbar    = 197.e6
lam     = hbar/m
lamcm   = lam*1.e-12
lam2mb  = lamcm**2 /(1e-27)
s2      = .5
foo     = peak*(2*.5 + 1)/(4*math.pi*lam2mb)
J       = .5*((peak*(2*s2 + 1)/(4*math.pi*lam2mb)) - 1)


