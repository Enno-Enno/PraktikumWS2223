import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

# rotes Licht
# 600.0 Linien pro mm
# zugehörige Gitterkonstante:  1.6666666666666667 μm
# zugehöriger Winkel:  [22.5] deg
# λ rot bei 600.0 Linien =  [6.37805720608483e-07]
# 300.0 Linien pro mm
# zugehörige Gitterkonstante:  3.3333333333333335 μm
# zugehöriger Winkel:  [11.5 23.  36. ] deg
# λ rot bei 300.0 Linien =  [6.645597813906573e-07 6.51218547482123e-07 6.530947247694146e-07]
# 100.0 Linien pro mm
# zugehörige Gitterkonstante:  10.0 μm
# zugehöriger Winkel:  [ 3.5  7.5 11.5 15.  19.  23.5 27.5] deg
# λ rot bei 100.0 Linien =  [6.104853953485688e-07 6.526309611002579e-07 6.645597813906573e-07
#  6.470476127563019e-07 6.511363089143134e-07 6.645817815420771e-07
#  6.596408760500485e-07]
# Durchschnittliche Wellenlänge:  (6.51+/-0.15)e-07
# Literaturwert:  6.350000000000001e-07
# Abweichung der Wellenlänge:  0.025+/-0.024

print("--------------------------------------------")
print("rotes Licht")

#600 Linien
lines_600 = 600 / 10**(-3)
gitterkonst_600 = 1/lines_600
print(lines_600 * 10 **-3, "Linien pro mm")
print("zugehörige Gitterkonstante: ", gitterkonst_600 * 10**6, "μm")


maximum_600, links_600, rechts_600 = np.genfromtxt("messung_5_600_rot.txt", unpack = True)
phi_600 = np.deg2rad((np.abs(links_600 + rechts_600))/2)
print("zugehöriger Winkel: ", phi_600[1:] / np.pi * 180, "deg")


wavelength_600 = gitterkonst_600 * unp.sin(phi_600[1:]) / maximum_600[1:]

print("λ rot bei", lines_600 * 10**-3, "Linien = ", wavelength_600)



#300 Linien
lines_300 = 300 / 10**(-3)
gitterkonst_300 = 1/lines_300
print(lines_300 * 10 **-3, "Linien pro mm")
print("zugehörige Gitterkonstante: ", gitterkonst_300 * 10**6, "μm")


maximum_300, links_300, rechts_300 = np.genfromtxt("messung_5_300_rot.txt", unpack = True)
phi_300 = np.deg2rad((np.abs(links_300 + rechts_300))/2)
print("zugehöriger Winkel: ", phi_300[1:] / np.pi * 180, "deg")


wavelength_300 = gitterkonst_300 * unp.sin(phi_300[1:]) / maximum_300[1:]

print("λ rot bei", lines_300 * 10**-3, "Linien = ", wavelength_300)



#100 Linien
lines_100 = 100 / 10**(-3)
gitterkonst_100 = 1/lines_100
print(lines_100 * 10 **-3, "Linien pro mm")
print("zugehörige Gitterkonstante: ", gitterkonst_100 * 10**6, "μm")

maximum_100, links_100, rechts_100 = np.genfromtxt("messung_5_100_rot.txt", unpack = True)
phi_100 = np.deg2rad((np.abs(links_100 + rechts_100))/2)
print("zugehöriger Winkel: ", phi_100[1:] / np.pi * 180, "deg")

wavelength_100 = gitterkonst_100 * unp.sin(phi_100[1:]) / maximum_100[1:]

print("λ rot bei", lines_100 * 10**-3, "Linien = ", wavelength_100)

wavelength = np.concatenate((wavelength_600, wavelength_300, wavelength_100), axis = None)
lambda_exp = ufloat(np.mean(wavelength), np.std(wavelength))

print("Durchschnittliche Wellenlänge: ", lambda_exp)

#vergleich mit Literatur
lambda_lit = 635 * 10**-9 
print("Literaturwert: ", lambda_lit)

abweichung = (lambda_exp - lambda_lit) / lambda_lit
print("Abweichung der Wellenlänge: ", abweichung)