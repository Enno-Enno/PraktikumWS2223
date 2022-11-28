import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

(klein_oben, klein_unten) = np.genfromtxt("Messdaten_klKu_Zitemp.txt", unpack=True)
(gross_oben, gross_unten) = np.genfromtxt("Messdaten_grKu_Zitemp.txt", unpack=True)
(temp, temp_oben, temp_unten) = np.genfromtxt('Messdaten_grKu_steigendeTemp.txt', unpack=True)


#rho=

#Reihe 1:
mw_oben_klein = np.mean(klein_oben)
st_oben_klein = np.std(klein_oben)

o_k = ufloat(mw_oben_klein, st_oben_klein)

mw_unten_klein = np.mean(klein_unten)
st_unten_klein = np.std(klein_unten)

u_k = ufloat(mw_unten_klein, st_unten_klein)
x_klein = ufloat(10, 0)

#Reihe 2:
mw_oben_gross = np.mean(gross_oben)
st_oben_gross = np.std(gross_oben)

o_g = ufloat(mw_oben_gross, st_oben_gross)

mw_unten_gross = np.mean(gross_unten)
st_unten_gross = np.std(gross_unten)

u_g = ufloat(mw_unten_gross, st_unten_gross)
x_gross = ufloat(5, 0)


#Reihe 3:
n=10
y_oben=np.zeros(n)
y_unten=np.zeros(n)

for j in range(n):
    for i, temperature in enumerate(temp):
        if i==2*j and temp[i] == temp[i+1]:
            y_oben[j] = (temp_oben[i] + temp_oben[i+1])/2
            y_unten[j] = (temp_unten[i] + temp_unten[i+1])/2



#Ergebnisse drucken:
print("Messreihe 1:")
print("Durchschnittszeiten kleine Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_klein), "mit Fehler: ", "{:.5f}".format(st_oben_klein))
print("unten:", '{:.5f}'.format(mw_unten_klein), "mit Fehler: ", "{:.5f}".format(st_unten_klein))

print("Messreihe 2:")
print("Durchschnittszeiten grosse Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_gross), "mit Fehler: ", "{:.5f}".format(st_oben_gross))
print("unten:", '{:.5f}'.format(mw_unten_gross), "mit Fehler: ", "{:.5f}".format(st_unten_gross))



print("Messreihe 3: hier steht noch nichts")

print("Reynold:")

print("Geschwindigkeit klein oben: ", x_klein / o_k)
print("Geschwindigkeit klein unten: ", x_klein / u_k)

print("Geschwindigkeit gross oben: ", x_gross / o_g)
print("Geschwindigkeit gross unten: ", x_gross / u_g)