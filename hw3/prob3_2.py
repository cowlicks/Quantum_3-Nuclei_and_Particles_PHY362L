#! /usr/bin/env python
import math
amu     = 931.5e6   # Mev (atomic mass unit)
mp      = 938.e6    # MeV
mpi     = 139.6e6   # Mev
md      = amu*2.014
T_p_lab = 340.e6    # MeV (p in lab)
E_p_beam    = T_p_lab + mp
inv     = math.sqrt(2*mp*(mp + E_p_beam))
E_pi_beam   = (inv**2 - mpi**2 - md**2)/(2*md)
T_pi_lab    = E_pi_beam - mpi
P_pi_beam   = math.sqrt(E_pi_beam**2 - mpi**2)
P_p_beam    = math.sqrt(E_p_beam**2 - mp**2)
P_p_f       = math.sqrt(.25*inv**2 - mp**2)
P_pi_f      = math.sqrt((.25*(inv**2 - mpi**2 - md**2)**2 - mpi**2 * md**2)/(inv**2))
