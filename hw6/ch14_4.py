import constants as c
import math as m

p1      = 300.
p2      = 330.   
p2_max  = 330. + 150. 
theta   = 67.*2.*m.pi/360.
mpi     = 139.

pk  = m.sqrt((p1 + p2*m.cos(theta))**2 +  (p2*m.sin(theta))**2)
pk_max  = m.sqrt((p1 + p2_max*m.cos(theta))**2 +  (p2_max*m.sin(theta))**2)

E1 = m.sqrt(mpi**2 + p1**2)
E2 = m.sqrt(mpi**2 + p2**2)
E2_max = m.sqrt(mpi**2 + p2_max**2)

mk = m.sqrt((E1 + E2)**2 - pk**2)
mk_max = m.sqrt((E2_max + E1)**2 - pk_max**2)

beta_k = pk/m.sqrt(pk**2 + mk**2)
v_k = beta_k *3.e8
dL = 1.9e-2

tau_lab = dL/ v_k
lorentz = 1./m.sqrt(1 - beta_k)
tau_cm = tau_lab * lorentz
