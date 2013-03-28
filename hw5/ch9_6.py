import math

# Part a
# _l denotes lab frame.
pk_l    = 390e6
mk      = 494e6
mp      = 938.3e6
Ek_l    = math.sqrt(mk**2 + pk_l**2)
Ep_l    = mp
# invariant
M       = math.sqrt((Ek_l + Ep_l)**2 - pk_l**2)


