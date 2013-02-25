#! /usr/bin/env python
import math
amu     = 931.5e6   # Mev (atomic mass unit)
mp      = 938.e6    # MeV
mpi     = 139.6e6   # Mev
md      = amu*2.014
T_p_lab = 340.e6    # MeV (p in lab)
E_p_beam    = T_p_lab + mp
inv         = math.sqrt(2*mp*(mp + E_p_beam))
E_pi_beam   = (inv**2 - mpi**2 - md**2)/(2*md)
T_pi_lab    = E_pi_beam - mpi
P_pi_beam   = math.sqrt(E_pi_beam**2 - mpi**2)
P_p_beam    = math.sqrt(E_p_beam**2 - mp**2)
P_p_f       = math.sqrt(.25*inv**2 - mp**2)
P_pi_f      = math.sqrt((.25*(inv**2 - mpi**2 - md**2)**2 - mpi**2 * md**2)/(inv**2))

# part c
sig_pi2pp   = 3.e-3
sig_pp2pi   = .09e-3
sig_r   = sig_pi2pp/sig_pp2pi
S_pi    = .5*((P_p_f**2 / P_pi_f**2)*4./(3.*sig_r) - 1)

# part d

b_pi    = math.sqrt(E_pi_beam**2 - mpi**2)/E_pi_beam
b_cm    = mpi*b_pi/(mpi + md)
g_cm    = 1./math.sqrt(1 - b_cm**2)

def p_par(deg):
    return g_cm*(P_pi_f*math.cos(deg*2*math.pi/360) + b_cm*inv)

def p_perp(deg):
    return P_pi_f*math.sin(deg*2*math.pi/360)

degs = [0., 35., 58.]
T   = []
for i in degs:
    par     = p_par(i)
    perp    = p_perp(i)
    T.append( math.sqrt(perp**2 + par**2 + mpi**2) - mpi)
