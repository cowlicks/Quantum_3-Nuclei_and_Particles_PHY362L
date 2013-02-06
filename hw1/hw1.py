#! /usr/bin/env python
'''
QQQQQQ:
    errant sign in 5 a? E_o => E_o + (i*gam/2)
'''

import math

class Con:
    """ Constants in eV, s, m, c units
    """
    c       = 3.e8
    hbar    = 4.136e-15


class App_B_1:
    l_atm   = 6.e3
    c       = 3e8
    tau_mu  = 2.197e-6
    T_half  = tau_mu * math.log(2)
    beta_mu = (1 - (T_half*c/l_atm)**2)**.5

class App_B_2(Con):
    def __init__(self):
        dongs = 'schlongs'
    # Part A
    m_p     = 938.3e6
    m_w     = 783.e6
    m_pi    = 139.6e6
    inv_m   = 2 * m_p
    A   = (inv_m**2 - m_w**2 - 4*m_pi**2)
    B    = (m_pi**2 + .25*m_w**2)
    C     = (m_w * m_pi)**2
    # The momentum of the w meson:
    p_w     = ((A**2 - 16*C) / (16*B + 4*A))**.5 

    # Part B
    G_w     = 8.49e6
    tau_w   = Con.hbar / G_w
    E_w     = (p_w**2 + m_w**2)**.5
    g_w     = E_w / m_w
    tau_cm  = g_w * tau_w
    beta_w  = p_w / E_w
    dist    = beta_w * tau_cm * Con.c
    
    # Part C
    def max_momentum_cm(self, m1, m2, inv_m):
        """ gives the max momentum of a particle with m1 mass produced in the 
        cm frame with the invariant mass = inv_m and the byproducts having mass
        m2.
        """
        A   = inv_m**2 - m1**2 - m2**2
        B   = m1**2 + m2**2
        C   = (m1 * m2)**2
        P   = ( (A*A - 4*C) / (4*B + 4*A) )**.5
        return P

    m_pio = 134.98e6
    p_pio = 326e6
    p_w_lab = 100e6
    # p_pio in the lab frame
    p_pio_lab = (p_pio + p_w_lab) * (p_w_lab**2 + m_w**2)**.5 / m_w


