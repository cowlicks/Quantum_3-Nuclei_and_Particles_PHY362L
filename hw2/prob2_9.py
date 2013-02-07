#! /usr/bin/env python
import math
u   = 931.494e6 # eV
h   = 4.1357e-15    # eV.s
hbar= 6.582e-16
c   = 3.e8
p_e = 330.e6    # eV
theta   = 10.    # degrees
theta_rad   = (10./360)*2*math.pi
m_e = 0.511e6   # eV
m_c = 1*u
z_e = 1
z_c = 1
ee  = 1.44e-9

beta_e  = p_e / math.sqrt(p_e**2 + m_e**2)
gam_e   = math.sqrt(1 - beta_e**2)**-1.
T_e = (gam_e - 1)*m_e
beta_cm = m_e*beta_e/(m_e + m_c)
gam_cm  = 1/math.sqrt(1 - beta_cm**2)
p_e_cm  = gam_cm*(p_e - beta_cm*math.sqrt(p_e**2 + m_e**2))
brog_lam_e  = h*c/p_e_cm
q = abs(2*p_e*math.sin(theta_rad/2))
theta_cm    = 2*math.asin(q/(2*p_e_cm))
theta_cm_deg    = theta_cm * 360 /(math.pi*2)

# Terms for mott scattering cross section
ruth        = (z_e * z_c * ee /(2.*T_e))**2 * (math.sin(theta_rad/2.)**-4)

# Recoil
recoil      = 1/(1. + 2.*T_e*(math.sin(theta_rad/2)**2.)/m_c)

# spin flip term
spin_flip   = math.cos(theta_rad/2)**2

mott = ruth*recoil*spin_flip

# Correction by the cross section for black disk.
a  = 1.2*(40**(1./3.))
F_q = 3*(math.sin(q*a/hbar) - (q*a/hbar)*math.cos(q*a/hbar))/((q*a/hbar)**3)

print "Broglie Wavelength   = {0:.7g}".format(brog_lam_e)
print "momentum transfer q  = {0:.7g}".format(q)
print "theta cm             = {0:.7g}".format(theta_cm_deg)
print "mott cross section   = {0:.7g}".format(mott)
print "formfactor squared   = {0:.7g}".format(F_q**2)
print "recoil               = {0:.7g}".format(recoil)
