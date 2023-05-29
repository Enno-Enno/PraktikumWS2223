import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std

y, zaehlrate = np.genfromtxt("messungen/statistik.txt", unpack = True)

rate = unp.uarray(zaehlrate, np.sqrt(zaehlrate)) #je 10 sekunden

ohne_wurzel_mean = np.mean(zaehlrate)
ohne_wurzel_std = np.std(zaehlrate)
print(f"ohne wurzel: {ohne_wurzel_mean} +- {ohne_wurzel_std}")

mean = sum(rate)/len(rate)
print(f"Mittelwert & Standardabw: {nom(mean):.2f} +- {std(mean):.2f}")
mittel = np.round(nom(mean))
stand = np.round(std(mean))
print(f"gerundete Werte: {mittel:.0f} +- {stand:.0f}")
breite = 100/ohne_wurzel_std
print(f"Breite: {breite}")

gauss = np.random.normal(mittel, ohne_wurzel_std, 100)
poisson = np.random.poisson(mittel, 100)

faktor = 100
zaehlrate_test = zaehlrate
#for index, value in enumerate(zaehlrate_test):
#    zaehlrate_test[index] *= 10
gauss_test = np.random.normal(mittel*faktor, ohne_wurzel_std, 100*faktor)
poisson_test = np.random.poisson(mittel*faktor, 100*faktor)


# plt.figure(constrained_layout = True)
# plt.hist([poisson_test/faktor, zaehlrate_test/faktor, gauss_test], bins = 10, label = ["Poissonverteilung", "Messwerte", "Gaußverteilung"])
# plt.xlabel("$N [1/(10\\unit{\\s})]$")
# plt.ylabel("Häufigkeit")
# plt.legend()
# plt.savefig("build/statistik_test.pdf")
#lassen wir das ....

plt.figure(constrained_layout = True)
plt.hist([poisson, zaehlrate, gauss], bins = 10, label = ["Poissonverteilung", "Messwerte", "Gaußverteilung"])
plt.xlabel("$N [1/(10\\unit{\\s})]$")
plt.ylabel("Häufigkeit")
plt.legend()
plt.savefig("build/statistik.pdf")