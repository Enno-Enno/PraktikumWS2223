import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

# gruenes Licht
# 600.0 Linien pro mm
# zugehörige Gitterkonstante:  1.6666666666666667 μm
# zugehöriger Winkel:  [18.5] deg
# λ gruen bei 600.0 Linien =  [5.288410940084869e-07]
# 300.0 Linien pro mm
# zugehörige Gitterkonstante:  3.3333333333333335 μm
# zugehöriger Winkel:  [ 9.5 19.  29.5] deg
# λ gruen bei 300.0 Linien =  [5.501586862022589e-07 5.426135907619278e-07 5.471372890038524e-07]
# 100.0 Linien pro mm
# zugehörige Gitterkonstante:  10.0 μm
# zugehöriger Winkel:  [ 3.   6.5  9.5 12.5 15.5 19.5 22.5 25.5 29.5] deg
# λ gruen bei 100.0 Linien =  [5.233595624294384e-07 5.660160688395336e-07 5.501586862022589e-07
#  5.410990348452572e-07 5.344767521565138e-07 5.563447653896183e-07
#  5.46690617664414e-07 5.38138871010369e-07 5.471372890038524e-07]
# Durchschnittliche Wellenlänge:  (5.44+/-0.11)e-07
# Literaturwert:  5.32e-07
# Abweichung der Wellenlänge:  0.023+/-0.020

print("--------------------------------------------")
print("gruenes Licht")

#600 Linien
lines_600 = 600 / 10**(-3)
gitterkonst_600 = 1/lines_600
print(lines_600 * 10 **-3, "Linien pro mm")
print("zugehörige Gitterkonstante: ", gitterkonst_600 * 10**6, "μm")


maximum_600, links_600, rechts_600 = np.genfromtxt("messung_5_600_gruen.txt", unpack = True)
phi_600 = np.deg2rad((np.abs(links_600 + rechts_600))/2)
print("zugehöriger Winkel: ", phi_600[1:] / np.pi * 180, "deg")

wavelength_600 = gitterkonst_600 * unp.sin(phi_600[1:]) / maximum_600[1:]

print("λ gruen bei", lines_600 * 10**-3, "Linien = ", wavelength_600)



#300 Linien
lines_300 = 300 / 10**(-3)
gitterkonst_300 = 1/lines_300
print(lines_300 * 10 **-3, "Linien pro mm")
print("zugehörige Gitterkonstante: ", gitterkonst_300 * 10**6, "μm")


maximum_300, links_300, rechts_300 = np.genfromtxt("messung_5_300_gruen.txt", unpack = True)
phi_300 = np.deg2rad((np.abs(links_300 + rechts_300))/2)
print("zugehöriger Winkel: ", phi_300[1:] / np.pi * 180, "deg")


wavelength_300 = gitterkonst_300 * unp.sin(phi_300[1:]) / maximum_300[1:]

print("λ gruen bei", lines_300 * 10**-3, "Linien = ", wavelength_300)



#100 Linien
lines_100 = 100 / 10**(-3)
gitterkonst_100 = 1/lines_100
print(lines_100 * 10 **-3, "Linien pro mm")
print("zugehörige Gitterkonstante: ", gitterkonst_100 * 10**6, "μm")

maximum_100, links_100, rechts_100 = np.genfromtxt("messung_5_100_gruen.txt", unpack = True)
phi_100 = np.deg2rad((np.abs(links_100 + rechts_100))/2)
print("zugehöriger Winkel: ", phi_100[1:] / np.pi * 180, "deg")


wavelength_100 = gitterkonst_100 * unp.sin(phi_100[1:]) / maximum_100[1:]

print("λ gruen bei", lines_100 * 10**-3, "Linien = ", wavelength_100)

wavelength = np.concatenate((wavelength_600, wavelength_300, wavelength_100), axis = None)
lambda_exp = ufloat(np.mean(wavelength), np.std(wavelength))

print("Durchschnittliche Wellenlänge: ", lambda_exp)

#vergleich mit Literatur
lambda_lit = 532 * 10**-9 
print("Literaturwert: ", lambda_lit)

abweichung = (lambda_exp - lambda_lit) / lambda_lit
print("Abweichung der Wellenlänge: ", abweichung)