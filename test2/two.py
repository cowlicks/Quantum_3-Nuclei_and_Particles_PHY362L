import math as m

tautau  = 290e-15
taumu   = 2.197e-6
mtau    = 1.8e9
mmu     = 104.e6
me      = 511.e3
mk      = 494.e6
hbarc   = 197e-9   # ev*m
mp      = 938.3e6   # ev/cc
ftaulab = 1080      # s
c       = 3.e8      # m/s

class a:
    br = (tautau/taumu)*((mtau-me)/(mmu-me))**5

class b:
    r  = (me/mmu)**2 * ((mk**2-me**2)/(mk**2-mmu**2))**2

class c:
    Eneutrino = 2.e6
    xsection = m.pi**2 * hbarc**3 * mp * Eneutrino / (c*ftaulab*me**5)

class d: 
    r = (0.97425/0.2252)**2
