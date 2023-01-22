import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import C00_umrechnung_rechteck_beidseitig as c00

#indexcheck für links/rechts
# print(c00.x_cm[:18])
# print(c00.x_cm[18:])
# [ 3.  5.  7.  9. 11. 13. 15. 17. 19. 21. 22. 23. 24. 25. 26. 27. 28. 29.] -> rechts
# [31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 44. 46. 48. 49.] -> links

#masse_stab_rechteck = ufloat(535.9, 0.1) / 1000 # in kg
masse_halterung = ufloat(50.4, 0.1) / 1000 # in kg
masse_gewicht_beidseitig = ufloat(501.5, 0.1) / 1000 # in kg
gesamtmasse_beidseitig = masse_halterung + masse_gewicht_beidseitig # + masse_stab_rechteck -> es geht um masse des angehängten gewichts
print("gesamtmasse_beidseitig: ", gesamtmasse_beidseitig)
#gesamtmasse_beidseitig:  0.55190+/-0.00014 kg

seite_cm = ufloat(1.000, 0.005) #in cm
seite_m = seite_cm /100 # in m
traegeheit_rechteck = seite_m **4 / 12
print("traegeheit_rechteck: ", traegeheit_rechteck)
#traegeheit_rechteck:  (8.33+/-0.08)e-06 m^4

gravitation = 9.81 #m/s^2
kraft_rechteck_beidseitig = gesamtmasse_beidseitig * gravitation
print("kraft_rechteck_beidseitig: ", kraft_rechteck_beidseitig)
#kraft_rechteck_beidseitig:  5.4141+/-0.0014 kg m/s^2 (= newton)

laenge_rechteck_beidseitig = 56 / 100 # in meter

x_links = c00.x_m[18:]
x_rechts = c00.x_m[:18]

faktor_beidseitig_rechts_m = 3 * laenge_rechteck_beidseitig**2 * x_rechts - 4 * x_rechts**3 # in m^3
faktor_beidseitig_rechts_kubik = faktor_beidseitig_rechts_m * 1000 # in 10^(-3) m^3

faktor_beidseitig_links_m = 4 * x_links**3 - 12 * laenge_rechteck_beidseitig * x_links**2 + 9 * laenge_rechteck_beidseitig**2 * x_links -laenge_rechteck_beidseitig**3 # in m^3
faktor_beidseitig_links_kubik = faktor_beidseitig_links_m * 1000 # in 10^(-3) m^3

def linear_function(faktor, s):
    return(s * faktor)

params_links, covariance_matrix_links = curve_fit(linear_function, faktor_beidseitig_links_m, c00.delta_d[18:])
errors_links = np.sqrt(np.diag(covariance_matrix_links))
print("parameter links: ")
for name, value in zip("s", params_links):
    print(f"{name} = {value:8.8f}")
print("Fehler_links: ", errors_links)

# parameter links:
# s = 0.00100612 1/m^2
# Fehler_links:  [3.40617724e-05]

# alte parameter links:
# s = 0.00107311 1/m^2
# b = -0.00000955 m
# Fehler_links:  [1.44046984e-04 1.99148559e-05]

params_rechts, covariance_matrix_rechts = curve_fit(linear_function, faktor_beidseitig_rechts_m, c00.delta_d[:18])
errors_rechts = np.sqrt(np.diag(covariance_matrix_rechts))
print("parameter rechts: ")
for name, value in zip("s", params_rechts):
    print(f"{name} = {value:8.8f}")
print("Fehler_rechts: ", errors_rechts)

# parameter rechts:
# s = 0.00102359 1/m^2
# Fehler_rechts:  [2.85539084e-05]

# alte parameter rechts:
# s = 0.00081058 1/m^2
# b = 0.00003190 m
# Fehler_rechts:  [6.62325831e-05 9.33628425e-06]


elastizitaet_links = kraft_rechteck_beidseitig/(48 * traegeheit_rechteck * params_links) # in N/(m^4* 1/m^2) = N/m^2
print("elastizitaet_links: ", elastizitaet_links)
# elastizitaet_links:  [134529493946.48233+/-2690810704.267282] N/m^2
# alte elastizitaet_links:  (1.261+/-0.025)e+11 N/m^2

elastizitaet_rechts = kraft_rechteck_beidseitig/(48 * traegeheit_rechteck * params_rechts) # in N/(m^4* 1/m^2) = N/m^2
print("elastizitaet_rechts: ", elastizitaet_rechts)
# elastizitaet_rechts:  [132233510268.6883+/-2644887261.9365697]
# alte elastizitaet_rechts:  (1.670+/-0.033)e+11

skalierungsfaktor = 100 * 10**3 # zur skalierung der y achse (meter zu 0.01 millimeter) der ausgleichsgerade


plt.figure(constrained_layout = True)
plt.plot(faktor_beidseitig_links_kubik, c00.delta_d_mm[18:], "x", label = "Messdaten links")
plt.plot(faktor_beidseitig_links_kubik, skalierungsfaktor*linear_function(faktor_beidseitig_links_m, *params_links), "-", label = "Ausgleichsgerade links") 
plt.grid()
plt.legend()
plt.xlabel("$\\left(3 L^2 x - 4 x^3\\right) / \\left(10^{-3} \\, \\unit{\\cubic\\meter}\\right)$")
plt.ylabel("$D/ (\\qty{0.01}{\\milli\\meter})$")
plt.savefig("build/C02_rechteck_beidseitig_links.pdf")

plt.figure(constrained_layout = True)
plt.plot(faktor_beidseitig_rechts_kubik, c00.delta_d_mm[:18], "x", label = "Messdaten rechts")
plt.plot(faktor_beidseitig_rechts_kubik, skalierungsfaktor*linear_function(faktor_beidseitig_rechts_m, *params_rechts), "-", label = "Ausgleichsgerade rechts")
plt.grid()
plt.legend()
plt.xlabel("$\\left(4 x^3 - 12 L x^2 + 9 L^2 x - L^3\\right) / \\left(10^{-3} \\, \\unit{\\cubic\\meter}\\right)$")
plt.ylabel("$D/ (\\qty{0.01}{\\milli\\meter})$")
plt.savefig("build/C02_rechteck_beidseitig_rechts.pdf") 