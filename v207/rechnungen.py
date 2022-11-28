import numpy as np
import matplotlib.pyplot as plt

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

print("Durchschnittszeiten gross Kugel:")
print("oben:", '{:.5f}'.format(mw_oben_gross), "mit Fehler: ", "{:.5f}".format(st_oben_gross))
print("unten:", '{:.5f}'.format(mw_unten_gross), "mit Fehler: ", "{:.5f}".format(st_unten_gross))