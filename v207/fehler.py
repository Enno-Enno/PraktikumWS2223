import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat


#drcm_klKu = 15.11
#drcm_grKu =15.78
#m_gr = 4.9528
#m_kl = 4.4531

drcm_klKu = ufloat(15.11, 0.01)
drcm_grKu = ufloat(15.78, 0.01)
m_gr = ufloat(4.9528, 0)
m_kl = ufloat(4.4531, 0)
rho_gr = ((3 * m_gr)/(4 * np.pi))* (2/drcm_grKu)**3
rho_kl = ((3 * m_kl)/(4 * np.pi))* (2/drcm_klKu)**3
print("Dichte große Kugel uncertainties",rho_gr)
print("Dichte kleine Kugel uncertainties",rho_kl)

#def dell_rho_gr(d):
#    return -(18 *m_gr)/(np.pi) * d**(-4)
#
#delta_rho_gr = np.sqrt((dell_rho_gr(drcm_grKu)**2) * (0.01)**2)
#print(delta_rho_gr)