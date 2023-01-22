import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import C00_umrechnung_rechteck_einseitig as c00


#masse_stab_rechteck = ufloat(535.9, 0.1) / 1000 # in kg
masse_halterung = ufloat(50.4, 0.1) / 1000 # in kg
masse_gewicht_einseitig = ufloat(199.3, 0.1) / 1000 # in kg
gesamtmasse_einseitig = masse_halterung + masse_gewicht_einseitig # + masse_stab_rechteck -> es geht um masse des angehängten gewichts
print("gesamtmasse_einseitig: ", gesamtmasse_einseitig)
#gesamtmasse_einseitig:  0.24970+/-0.00014 kg

seite_cm = ufloat(1.000, 0.005) #in cm
seite_m = seite_cm /100 # in m
traegeheit_rechteck = seite_m **4 / 12
print("traegeheit_rechteck: ", traegeheit_rechteck)
#traegeheit_rechteck:  (8.33+/-0.08)e-06 m^4

gravitation = 9.81 #m/s^2
kraft_rechteck_einseitig = gesamtmasse_einseitig * gravitation
print("kraft_rechteck_einseitig: ", kraft_rechteck_einseitig)
#kraft_rechteck_einseitig:  2.4496+/-0.0014 kg m/s^2 (= newton)

laenge_rechteck_einseitig = 51.5 / 100 # in meter
faktor_einseitig_m = laenge_rechteck_einseitig * c00.x_m **2 - (c00.x_m **3)/3 # in m^3
faktor_einseitig_kubik = faktor_einseitig_m * 1000 # in 10^(-3) m^3
print("faktor_einseitig_m: ", faktor_einseitig_m)
# faktor_einseitig_m # in m^3:  [0.08443517 0.07915583 0.0739125  0.06872117 0.06359783 0.0585585
#  0.05361917 0.04879583 0.0441045  0.03956117 0.03518183 0.0309825
#  0.02697917 0.02318783 0.0196245  0.01630517 0.01324583 0.0104625
#  0.00797117 0.00578783 0.0039285  0.00240917 0.00124583 0.0004545 ]
print("faktor_einseitig_kubik: ", faktor_einseitig_kubik)
# faktor_einseitig_kubik in 10^(-3) m^3:  [84.43516667 79.15583333 73.9125     68.72116667 63.59783333 58.5585
#  53.61916667 48.79583333 44.1045     39.56116667 35.18183333 30.9825
#  26.97916667 23.18783333 19.6245     16.30516667 13.24583333 10.4625
#   7.97116667  5.78783333  3.9285      2.40916667  1.24583333  0.4545    ]

def linear_function(faktor, s):
    return(s * faktor)

params, covariance_matrix = curve_fit(linear_function, faktor_einseitig_m, c00.delta_d)
errors = np.sqrt(np.diag(covariance_matrix))
print("parameter: ")
for name, value in zip("s", params):
    print(f"{name} = {value:8.8f}")
print("Fehler: ", errors)
# parameter:
# s = 0.01260312 1/m^2
# Fehler:  [0.00016094] 1/m^2

# parameter: -> nicht verwendet
# s = 0.01225490
# b = 0.00001901
# Fehler:  [2.49712761e-04 1.07332779e-05]

elastizitaet = kraft_rechteck_einseitig/(2 * traegeheit_rechteck * params) # in N/(m^4* 1/m^2) = N/m^2
print("elastizitaet: ", elastizitaet)
#elastizitaet:  [116616696514.27222+/-2333268919.524976] N/m^2

skalierungsfaktor = 100 * 10**3 # zur skalierung der y achse (meter zu 0.01 millimeter) der ausgleichsgerade


plt.figure(constrained_layout = True)
plt.plot(faktor_einseitig_kubik, c00.delta_d_mm, "x", label = "Messdaten")
plt.plot(faktor_einseitig_kubik, skalierungsfaktor*linear_function(faktor_einseitig_m, *params), "-", label = "Ausgleichsgerade") 
plt.grid()
plt.legend()
plt.xlabel("$\\left(L x^2 - \\frac{x^3}{3}\\right) / \\left(10^{-3} \\, \\unit{\\cubic\\meter}\\right)$")
plt.ylabel("$D/ (\\qty{0.01}{\\milli\\meter})$")
plt.savefig("build/C02_rechteck_einseitig.pdf")