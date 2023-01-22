import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import c00_umrechnung_kreis_einseitig as c00


# masse_stab_kreis = ufloat(412.0, 0.1) / 1000 # in kg -> brauchen wa nicht :P
masse_halterung = ufloat(50.4, 0.1) / 1000 # in kg
masse_gewicht_einseitig = ufloat(199.3, 0.1) / 1000 # in kg
gesamtmasse_einseitig = masse_halterung + masse_gewicht_einseitig
print("gesamtmasse_einseitig: ", gesamtmasse_einseitig)
#gesamtmasse_einseitig:  0.24970+/-0.00014 kg

radius_cm = ufloat(1.000, 0.005) #in cm
radius_m = radius_cm /100 # in m
traegeheit_kreis = np.pi * radius_m **4 / 4
print("traegeheit_kreis: ", traegeheit_kreis)
#traegeheit_kreis:  (7.85+/-0.16)e-09 m^4

gravitation = 9.81 #m/s^2
kraft_kreis_einseitig = gesamtmasse_einseitig * gravitation
print("kraft_kreis_einseitig: ", kraft_kreis_einseitig)
#kraft_kreis_einseitig:  2.4496+/-0.0014 # kg m/s^2 (= newton)

laenge_kreis_einseitig = 50.5 / 100 # in meter
faktor_einseitig_m = laenge_kreis_einseitig * c00.x_m **2 - (c00.x_m **3)/3 # in m^3
faktor_einseitig_kubik = faktor_einseitig_m * 1000 # in 10^(-3) m^3
print("faktor_einseitig_m: ", faktor_einseitig_m)
# faktor_einseitig_m:  [0.08203417 0.07694683 0.0718875  0.06687217 0.06191683 0.0570375
#  0.05225017 0.04757083 0.0430155  0.03860017 0.03434083 0.0302535
#  0.02635417 0.02265883 0.0191835  0.01594417 0.01295683 0.0102375
#  0.00780217 0.00566683 0.0038475  0.00236017 0.00122083 0.0004455 ]
print("faktor_einseitig_kubik: ", faktor_einseitig_kubik)
# faktor_einseitig_kubik:  [82.03416667 76.94683333 71.8875     66.87216667 61.91683333 57.0375
#  52.25016667 47.57083333 43.0155     38.60016667 34.34083333 30.2535
#  26.35416667 22.65883333 19.1835     15.94416667 12.95683333 10.2375
#   7.80216667  5.66683333  3.8475      2.36016667  1.22083333  0.4455    ]

def linear_function(faktor, s):
    return(s * faktor)

params, covariance_matrix = curve_fit(linear_function, faktor_einseitig_m, c00.delta_d)
errors = np.sqrt(np.diag(covariance_matrix))
print("parameter: ")
for name, value in zip("s", params):
    print(f"{name} = {value:8.8f}")
print("Fehler: ", errors)
# parameter:
# s = 0.01943850 1/m^2
# Fehler: [0.00012869] 1/m^2


elastizitaet = kraft_kreis_einseitig/(2 * traegeheit_kreis * params) # in N/(m^4* 1/m^2) = N/m^2
print("elastizitaet: ", elastizitaet)
#elastizitaet:  [8022411628.9529705+/-160512553.2876061] N/m^2

skalierungsfaktor = 100 * 10**3 # zur skalierung der y achse (meter zu 0.01 millimeter) der ausgleichsgerade


plt.figure(constrained_layout = True)
plt.plot(faktor_einseitig_kubik, c00.delta_d_mm, "x", label = "Messdaten")
plt.plot(faktor_einseitig_kubik, skalierungsfaktor*linear_function(faktor_einseitig_m, *params), "-", label = "Ausgleichsgerade") 
plt.grid()
plt.legend()
plt.xlabel("$\\left(L x^2 - \\frac{x^3}{3}\\right) / \\left(10^{-3} \\, \\unit{\\cubic\\meter}\\right)$")
plt.ylabel("$D/ (\\qty{0.01}{\\milli\\meter})$")
plt.savefig("build/C02_kreis_einseitig.pdf")