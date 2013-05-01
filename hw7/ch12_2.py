import math
mp = 938.272
me = 0.511
mn = 939.565
msig = 1189.
mlam = 1115.
en = mn - (mp + me)

def bdecay(e, m=me):
    val = (1./3)*(m*m + e*e)*(e*e - m*m)**(3./2) 
    val2 =  (-.25*e*e*(e*e - m*m)**.5)*(2*e*e - m*m) 
    val3 = (.25*e*m**4 * math.log(e + (e*e - m*m)**.5)) 
    val4 = (1./5)*(e*e - m*m)**(5./2) + .25*e*m**4 * math.log(m)
    print val, val2, val3, val4
    return val + val2 + val3 + val4

mD = 1865
mK = 494
mpi = 139.6
cabibo = (math.pi*2/360.)*13.04

brkbrpi = ((mD-mK)/(mD-mpi))**10 * (math.cos(cabibo)/math.sin(cabibo))**2
