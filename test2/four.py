import math as m


ppi = 1140.
mp = 938.3
mn = 939.6
mpi = 139.6

# part a
Epi = m.sqrt(mpi**2 + ppi**2)
Ep = mp
Minv = m.sqrt((Epi + Ep)**2 - ppi**2)
mx1 = 135.
pstar = 446.
mx2 = 546.
def pcm(M, m1, m2):
    return m.sqrt((.25*(M**2 - m1**2 - m2**2)**2 - (m1*m2)**2)/M**2)

pcm1 = pcm(Minv, mn, mx1)
pcm2 = pcm(Minv, mn, mx2)

b1 = pcm1/m.sqrt(pcm1**2 + mx1**2)
b2 = pcm2/m.sqrt(pcm2**2 + mx2**2)

gam1 = m.sqrt(mx1**2 + pcm1**2)/mx1
gam2 = m.sqrt(mx2**2 + pcm2**2)/mx2

def openangle(theta, gam, beta):
    num = gam**2*(beta**2 - m.cos(theta)**2) - m.sin(theta)**2
    denom = (2*gam*beta*m.sin(theta))
    result = m.pi/2 - m.atan(num/denom)
    return result
