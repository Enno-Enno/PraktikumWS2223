import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

(klein_oben, klein_unten) = np.genfromtxt("Messdaten_klKu_Zitemp.txt", unpack=True)
(gross_oben, gross_unten) = np.genfromtxt("Messdaten_grKu_Zitemp.txt", unpack=True)
(temp, temp_oben, temp_unten) = np.genfromtxt('Messdaten_grKu_steigendeTemp.txt', unpack=True)

mw_oben_klein = np.mean(klein_oben)
st_oben_klein = np.std(klein_oben)

mw_unten_klein = np.mean(klein_unten)
st_unten_klein = np.std(klein_unten)

mw_oben_gross = np.mean(gross_oben)
st_oben_gross = np.std(gross_oben)

mw_unten_gross = np.mean(gross_unten)
st_unten_gross = np.std(gross_unten)



print("Durchschnittszeiten kleine Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_klein), "mit Fehler: ", "{:.5f}".format(st_oben_klein))
print("unten:", '{:.5f}'.format(mw_unten_klein), "mit Fehler: ", "{:.5f}".format(st_unten_klein))

print("Durchschnittszeiten grosse Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_gross), "mit Fehler: ", "{:.5f}".format(st_oben_gross))
print("unten:", '{:.5f}'.format(mw_unten_gross), "mit Fehler: ", "{:.5f}".format(st_unten_gross))


drcm_klKu = ufloat(15.11, 0.01)
drcm_grKu = ufloat(15.78, 0.01)
m_gr = ufloat(4.9528, 0)
m_kl = ufloat(4.4531, 0)
rho_gr = ((3 * m_gr)/(4 * np.pi))* (2/drcm_grKu)**3
rho_kl = ((3 * m_kl)/(4 * np.pi))* (2/drcm_klKu)**3
print("Dichte große Kugel uncertainties",rho_gr)
print("Dichte kleine Kugel uncertainties",rho_kl)