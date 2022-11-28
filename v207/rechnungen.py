import numpy as np
import matplotlib.pyplot as plt

(klein_oben, klein_unten) = np.genfromtxt("Messdaten_klKu_Zitemp.txt", unpack=True)
(gross_oben, gross_unten) = np.genfromtxt("Messdaten_grKu_Zitemp.txt", unpack=True)
(temp, temp_oben, temp_unten) = np.genfromtxt('Messdaten_grKu_steigendeTemp.txt', unpack=True)

t_oben_klein = np.mean(klein_oben)
t_unten_klein = np.mean(klein_unten)

t_oben_gross = np.mean(gross_oben)
t_unten_gross = np.mean(gross_unten)

print("Durchschnittszeiten kleine Kugel:")
print("oben:", '{:.5f}'.format(t_oben_klein))
print("unten:", '{:.5f}'.format(t_unten_klein))

print("Durchschnittszeiten grosse Kugel:")
print("oben:", '{:.5f}'.format(t_oben_gross))
print("unten:", '{:.5f}'.format(t_unten_gross))