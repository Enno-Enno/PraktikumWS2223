import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import C00_umrechnung_kreis_beidseitig as c00

#indexcheck für links/rechts
# print(c00.x_cm[:18])
# [ 3.  5.  7.  9. 11. 13. 15. 17. 19. 21. 22. 23. 24. 25. 26. 27. 28. 29.] -> rechts
# print(c00.x_cm[18:])
# [31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 44. 46. 48. 49.] -> links

#links: [:18], von 31-49; L/2<x<L
#rechts: [18:] von 3-29; 0<x<L/2

#masse_stab_kreis = ufloat(535.9, 0.1) / 1000 # in kg
masse_halterung = ufloat(50.4, 0.1) / 1000 # in kg
masse_gewicht_beidseitig = ufloat(501.5, 0.1) / 1000 # in kg
gesamtmasse_beidseitig = masse_halterung + masse_gewicht_beidseitig # + masse_stab_kreis -> es geht um masse des angehängten gewichts
print("gesamtmasse_beidseitig: ", gesamtmasse_beidseitig)
#gesamtmasse_beidseitig:  0.55190+/-0.00014 kg

radius_cm = 1/2 * ufloat(1.000, 0.005) #in cm
radius_m = radius_cm /100 # in m
traegeheit_kreis = np.pi * radius_m **4 / 4
print("traegeheit_kreis: ", traegeheit_kreis)
#traegeheit_kreis:  (4.91+/-0.10)e-10 m^4

gravitation = 9.81 #m/s^2
kraft_kreis_beidseitig = gesamtmasse_beidseitig * gravitation
print("kraft_kreis_beidseitig: ", kraft_kreis_beidseitig)
#kraft_kreis_beidseitig:  5.4141+/-0.0014 kg m/s^2 (= newton)

laenge_kreis_beidseitig = 56 / 100 # in meter

x_links = c00.x_m[18:]
x_rechts = c00.x_m[:18]

faktor_beidseitig_rechts_m = 3 * laenge_kreis_beidseitig**2 * x_rechts - 4 * x_rechts**3 # in m^3
faktor_beidseitig_rechts_kubik = faktor_beidseitig_rechts_m * 1000 # in 10^(-3) m^3

faktor_beidseitig_links_m = 4 * x_links**3 - 12 * laenge_kreis_beidseitig * x_links**2 + 9 * laenge_kreis_beidseitig**2 * x_links -laenge_kreis_beidseitig**3 # in m^3
faktor_beidseitig_links_kubik = faktor_beidseitig_links_m * 1000 # in 10^(-3) m^3

def linear_function(faktor, s, b): # ohne b ist rechte Ausgleichsgerade ungenauer
    return(s * faktor + b)

params_links, covariance_matrix_links = curve_fit(linear_function, faktor_beidseitig_links_m, c00.delta_d[18:])
errors_links = np.sqrt(np.diag(covariance_matrix_links))
print("parameter links: ")
for name, value in zip("sb", params_links):
    print(f"{name} = {value:8.8f}")
print("Fehler_links: ", errors_links)

# parameter links:
# s = 0.00087826 1/m^2
# b = 0.00002034 m
# Fehler_links:  [1.04203935e-04 1.44064544e-05]

params_rechts, covariance_matrix_rechts = curve_fit(linear_function, faktor_beidseitig_rechts_m, c00.delta_d[:18])
errors_rechts = np.sqrt(np.diag(covariance_matrix_rechts))
print("parameter rechts: ")
for name, value in zip("sb", params_rechts):
    print(f"{name} = {value:8.8f}")
print("Fehler_rechts: ", errors_rechts)


# parameter rechts:
# s = 0.00108506 1/m^2
# b = -0.00004673 m
# Fehler_rechts:  [6.64784236e-05 9.37093844e-06]


elastizitaet_links = kraft_kreis_beidseitig/(48 * traegeheit_kreis * params_links[0]) # in N/(m^4* 1/m^2) = N/m^2
print("elastizitaet_links: ", elastizitaet_links)
# elastizitaet_links:  (2.62+/-0.05)e+11 N/m^2

elastizitaet_rechts = kraft_kreis_beidseitig/(48 * traegeheit_kreis * params_rechts[0]) # in N/(m^4* 1/m^2) = N/m^2
print("elastizitaet_rechts: ", elastizitaet_rechts)
# elastizitaet_rechts:  (2.12+/-0.04)e+11

elastizitaet_kreis_einseitig = ufloat(1.317, 0.026)* 10**11

abweichung_links = (elastizitaet_links - elastizitaet_kreis_einseitig) / elastizitaet_kreis_einseitig
abweichung_rechts = (elastizitaet_rechts - elastizitaet_kreis_einseitig) / elastizitaet_kreis_einseitig
abweichung_rechts_links = (elastizitaet_rechts - elastizitaet_links) / elastizitaet_rechts

print("abweichung_links: ", abweichung_links)
# abweichung_links:  0.99+/-0.06
print("abweichung_rechts: ", abweichung_rechts)
# abweichung_rechts:  0.61+/-0.04
print("abweichung_rechts_links: ", abweichung_rechts_links)
# abweichung_rechts_links: -0.235470533236481899264+/-0.000000000000000000031


skalierungsfaktor = 100 * 10**3 # zur skalierung der y achse (meter zu 0.01 millimeter) der ausgleichsgerade


plt.figure(constrained_layout = True)
plt.plot(faktor_beidseitig_links_kubik, c00.delta_d_mm[18:], "x", label = "Messdaten links, Kreis")
plt.plot(faktor_beidseitig_links_kubik, skalierungsfaktor*linear_function(faktor_beidseitig_links_m, *params_links), "-", label = "Ausgleichsgerade links") 
plt.grid()
plt.legend()
plt.xlabel("$\\left(4 x^3 - 12 L x^2 + 9 L^2 x - L^3\\right) / \\left(10^{-3} \\, \\unit{\\cubic\\meter}\\right)$")
plt.ylabel("$D/ (\\qty{0.01}{\\milli\\meter})$")
plt.savefig("build/C02_kreis_beidseitig_links.pdf")

plt.figure(constrained_layout = True)
plt.plot(faktor_beidseitig_rechts_kubik, c00.delta_d_mm[:18], "x", label = "Messdaten rechts, Kreis")
plt.plot(faktor_beidseitig_rechts_kubik, skalierungsfaktor*linear_function(faktor_beidseitig_rechts_m, *params_rechts), "-", label = "Ausgleichsgerade rechts")
plt.grid()
plt.legend()
plt.xlabel("$\\left(3 L^2 x - 4 x^3\\right) / \\left(10^{-3} \\, \\unit{\\cubic\\meter}\\right)$")
plt.ylabel("$D/ (\\qty{0.01}{\\milli\\meter})$")
plt.savefig("build/C02_kreis_beidseitig_rechts.pdf") 