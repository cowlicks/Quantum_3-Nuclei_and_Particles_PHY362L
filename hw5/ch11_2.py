u   = 931.494061e6   # ev/cc
mar = 36.96677632*u
mcl = 36.96590259*u
me  = .510998910e6 
c   = 3e8           # m/s

dm  = mar + me - mcl
mz  = mcl

v   = dm*c/mz
vcmus   = v*1e-4
