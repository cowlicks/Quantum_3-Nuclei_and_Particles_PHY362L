import math
peak    = 25.           # mb
M       = 1820.e6       # eV/cc
mp      = 938.3e6       # eV/cc
mk      = 494e6

pcm     = math.sqrt((.25*(M**2 - mp**2 -mk**2)**2 - (mk*mp)**2)/M**2) # ev/c
lam     = 197.e6/pcm      # lambdabar in fm
lam2    = lam**2
lam2mb  = lam2*10
s1      = 0.
s2      = .5


J       = .5*((peak*(2*s2 + 1)/(4.*math.pi*lam2mb)) - 1.)
def mb(l):
    sum = 0
    for i in range(l+1):
        sum = (2*i + 1)
    return 4*math.pi*lam2mb*sum
