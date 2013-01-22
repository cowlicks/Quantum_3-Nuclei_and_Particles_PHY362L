#! /usr/bin/env python
import math

class App_B_1:
    l_atm = 6.e3
    c = 3e8
    tau_mu = 2.197e-6
    T_half = tau_mu * math.log(2)
    beta_mu = (1 - (T_half*c/l_atm)**2)**.5

class App_B_2:
    c       = 3.e8
    m_p     = 938.3e6
    m_w     = 783.e6
    m_pi    = 139.6e6
    p_w     = .5*(2*m_p - m_w - 2*m_pi)
    E_w     = ((p_w*c)**2 + (m_w*c*c)**2)**0.5
    gamma_w = E_w / (m_w*c*c)




