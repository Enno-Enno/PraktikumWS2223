import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

(klein_oben, klein_unten) = np.genfromtxt("Messdaten_klKu_Zitemp.txt", unpack=True)
(gross_oben, gross_unten) = np.genfromtxt("Messdaten_grKu_Zitemp.txt", unpack=True)
#in s

rho_fl = ufloat(0.99841, 0)
rho_52 = ufloat(0.988, 0)
rho_klein = ufloat(2.2359, 0.005)
rho_groß = ufloat(2.4073, 0.005)
#in gramm pro kubik cm

r_klein = ufloat(15.61/2 *0.1 , 0.01/2 * 0.1)
r_groß = ufloat(15.78/2 * 0.1 , 0.01/2 * 0.1)
#in cm


#Reihe 1:
mw_oben_klein = np.mean(klein_oben)
st_oben_klein = np.std(klein_oben)

o_k = ufloat(mw_oben_klein, st_oben_klein)

mw_unten_klein = np.mean(klein_unten)
st_unten_klein = np.std(klein_unten)

u_k = ufloat(mw_unten_klein, st_unten_klein)

x_klein = ufloat(10, 0)
#in cm

k_klein = ufloat(0.07640 * 10**(-3), 0)

eta_klein_oben = k_klein*(rho_klein - rho_fl) * o_k
eta_klein_unten = k_klein*(rho_klein - rho_fl) * u_k


#Reihe 2:
mw_oben_gross = np.mean(gross_oben)
st_oben_gross = np.std(gross_oben)

o_g = ufloat(mw_oben_gross, st_oben_gross)

mw_unten_gross = np.mean(gross_unten)
st_unten_gross = np.std(gross_unten)

u_g = ufloat(mw_unten_gross, st_unten_gross)
x_gross = ufloat(5, 0)

#Reihe 3

mw_t_oben_52 = ufloat(19.56 , 0)
mw_t_unten_52 = ufloat(19.13 , 0)


# Reynoldszahl
vko=x_klein / o_k
vku=x_klein / u_k

vgo=x_gross / o_g
vgu=x_gross / u_g

v52o = x_gross / mw_t_oben_52
v52u = x_gross / mw_t_unten_52

rey_klein_oben = rho_fl * vko * r_groß / eta_klein_oben
rey_klein_unten = rho_fl * vku * r_groß / eta_klein_unten

rey_gross_oben = rho_fl * vgo * r_groß / eta_klein_oben
rey_gross_unten = rho_fl * vgu * r_groß / eta_klein_unten


k_gross_oben = eta_klein_oben/((rho_groß - rho_fl)*o_g) 
k_gross_unten = eta_klein_unten/((rho_groß - rho_fl)*u_g) 


eta_52_o = k_gross_oben * (rho_groß - rho_52) * mw_t_oben_52
eta_52_u = k_gross_unten * (rho_groß - rho_52) * mw_t_unten_52

rey_52_o = rho_52 * v52o * r_groß / eta_52_o
rey_52_u = rho_52 * v52u * r_groß / eta_52_u


#Ergebnisse drucken:
print("Messreihe 1:")
print("Durchschnittszeiten kleine Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_klein), "mit Fehler: ", "{:.5f}".format(st_oben_klein))
print("unten:", '{:.5f}'.format(mw_unten_klein), "mit Fehler: ", "{:.5f}".format(st_unten_klein))

print("Messreihe 2:")
print("Durchschnittszeiten grosse Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_gross), "mit Fehler: ", "{:.5f}".format(st_oben_gross))
print("unten:", '{:.5f}'.format(mw_unten_gross), "mit Fehler: ", "{:.5f}".format(st_unten_gross))

#print("Messreihe 3: hier steht noch nichts")

print("eta klein oben: ", eta_klein_oben)
print("eta klein unten: ", eta_klein_unten)

print("K oben und gross: ", k_gross_oben)
print("K unten und gross: ", k_gross_unten)

print("Reynold:")

print("Geschwindigkeit klein oben: ", vko)
print("Geschwindigkeit klein unten: ", vku)

print("Geschwindigkeit gross oben: ", vgo)
print("Geschwindigkeit gross unten: ", vgu)


print("rey klein oben: ", rey_klein_oben)
print("rey klein unten: ", rey_klein_unten)

print("rey gross oben: ", rey_gross_oben)
print("rey gross unten: ", rey_gross_unten)

print("v52o:", v52o)
print("v52u:", v52u)

print("rey_52_o:", rey_52_o)
print("rey_52_u:", rey_52_u)