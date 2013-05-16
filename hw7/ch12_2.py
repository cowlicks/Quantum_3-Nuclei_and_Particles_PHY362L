import math
mp = 938.272
me = 0.511
mn = 939.565
msig = 1189.
msigm = 1197.
msigo = 1193.
mlam = 1115.
taun = 881.5
taulam = 2.63e-10
tausig = 0.8e-10
tausigm = 1.48e-10
tausigo = 7.4e-20
hbar = 6.582e-22

def bwidth(E0, N):
    h = math.sqrt(E0**2 - me**2)/N
    integral = 0

    def f(p,E0):
        E = math.sqrt(me**2 + p**2)
        return p*p*(E - E0)**2

    for i in range(N+1):
        integral += h*f(i*h, E0)

    return integral
        
mD = 1865
mK = 494
mpi = 139.6
cabibo = (math.pi*2/360.)*13.04

brkbrpi = ((mD-mK)/(mD-mpi))**10 * (math.cos(cabibo)/math.sin(cabibo))**2
