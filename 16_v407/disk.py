import numpy as np
from uncertainties import ufloat

perp = ufloat(1.180, 0.004)
para = ufloat(1.962, 0.008)
brew = ufloat(4.01, 0.15)
lit = 3.353

abw_perp_para = (perp-para) / para
abw_perp_lit = (lit - perp) / lit
abw_para_lit = (lit - para) / lit
abw_brew_lit = (lit - brew) / lit

#print(np.tan(np.deg2rad(76)))

print("Abweichung n perp/para: ", abw_perp_para*100, "\, \%")
print("Abweichung n perp/lit: (", abw_perp_lit*100, ") \, \%")
print("Abweichung n para/lit: (", abw_para_lit*100, ") \, \%")
print("Abweichung n brew/lit: (", abw_brew_lit*100, ") \, \%")


# Abweichung n perp/para:  -39.86+/-0.32 \, \%
# Abweichung n perp/lit: ( 64.81+/-0.12 ) \, \%
# Abweichung n para/lit: ( 41.49+/-0.24 ) \, \%
# Abweichung n brew/lit: ( -20+/-4 ) \, \%