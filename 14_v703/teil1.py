import numpy as np
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from uncertainties import ufloat

spannung, strom, zaehlrate = np.genfromtxt("messungen/teil1.txt", unpack = True)
#spannung in V, strom in μΑ, rate pro 120 sekunden
time = 120 # sekunden
#zaehlrate /= 2
#print(zaehlrate)

rate = unp.uarray(zaehlrate, np.sqrt(zaehlrate))
print("Zerfallsrate N mit Fehler je", time, "Sekunden: N = ")
for index, value in enumerate(strom):
    print(f"{unp.nominal_values(rate[index]):.0f} +- {unp.std_devs(rate[index]):.0f}")
#Zerfallsrate N mit Fehler je 120 Sekunden: N = 
#12534 +- 112
#23067 +- 152
#23087 +- 152
#23431 +- 153
#23381 +- 153
#23602 +- 154
#23757 +- 154
#24082 +- 155
#23962 +- 155
#23780 +- 154
#23882 +- 155
#23846 +- 154
#23939 +- 155
#24139 +- 155
#24093 +- 155
#24385 +- 156
#24538 +- 157
#24902 +- 158
#25106 +- 158
#25519 +- 160
#26107 +- 162
#26633 +- 163

plt.figure(constrained_layout = True)
plt.errorbar(spannung, unp.nominal_values(rate), yerr = unp.std_devs(rate), fmt = "x", label = "Messrate mitsamt Fehlerbalken")
plt.xlabel("$U / \\unit{\\volt}$")
plt.ylabel("$N / 120 \\, \\unit{\\second}$")
plt.legend()
plt.grid()
plt.savefig("build/teil1.pdf")