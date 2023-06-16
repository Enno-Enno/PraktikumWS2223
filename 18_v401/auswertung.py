import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std

# λ in nm:
# 666.18 +- 2.66
# 665.07 +- 2.66
# 658.70 +- 2.63
# 664.63 +- 2.66
# 656.31 +- 2.63
# 674.53 +- 2.70
# 670.89 +- 2.68
# 662.20 +- 2.65
# 674.98 +- 2.70
# 674.53 +- 2.70
# Mittlere Wellenlänge: (666.80 +- 2.67) nm
# -------------------------------
# Teil 2: Brechungsindex:
# n: 
# 1.0003354 +- 0.0000057
# 1.0003082 +- 0.0000053
# 1.0003354 +- 0.0000057
# 1.0002901 +- 0.0000050
# 1.0001813 +- 0.0000031
# 1.0002991 +- 0.0000051
# 1.0003082 +- 0.0000053
# 1.0003263 +- 0.0000056
# 1.0002175 +- 0.0000037
# 1.0002901 +- 0.0000050
# Mittlerer Brechungsindex: 1.0002891 +- 0.0000050

print("-------------------------------")
print("Teil 1: Wellenlänge:")
impulses_wl = np.genfromtxt("messungen/01_wellenlaenge.txt", unpack = True)

hebeluebersetzung = 5.017
schraube = ufloat(5, 0.02) *10**(-3) # meter
distance = schraube/hebeluebersetzung

wavelength = 2 * distance /impulses_wl

print("λ in nm:")
for index, value in enumerate(nom(wavelength)):
    print(f"{nom(wavelength[index] * 10**9):.2f} +- {std(wavelength[index] * 10**9):.2f}")

mittel_wavelength = sum(wavelength)/len(wavelength)

print(f"Mittlere Wellenlänge: ({nom(mittel_wavelength * 10**9):.2f} +- {std(mittel_wavelength * 10**9):.2f}) nm")



print("-------------------------------")
print("Teil 2: Brechungsindex:")

normal_temperatur = 273.15 #kelvin (zimmertemperatur)
normal_druck = 1.0132 #bar
delta_druck = ufloat(600, 10) / 750.062 #torr nach bar

tag_temperatur = 273.15 + 20 #kelvin
#tag_druck = 1.0121 #bar
#nach https://wetter.heubes.de/index.php?site=90daystable

b = 50 * 10**(-3) #meter

impulse_n = np.genfromtxt("messungen/02_brechungsindex.txt", unpack = True)

#def index(p_0, T_0)
brechindex = 1 + (impulse_n * mittel_wavelength / (2 * b)) * (tag_temperatur / normal_temperatur) * (normal_druck / delta_druck)

print("n: ")
for index, value in enumerate(nom(brechindex)):
    print(f"{nom(brechindex[index]):.7f} +- {std(brechindex[index]):.7f}")

mittel_index = sum(brechindex)/len(brechindex)
print(f"Mittlerer Brechungsindex: {nom(mittel_index):.7f} +- {std(mittel_index):.7f}")
