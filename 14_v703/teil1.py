import numpy as np
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from uncertainties import ufloat

spannung, stromstaerke, zaehlrate = np.genfromtxt("messungen/teil1.txt", unpack = True)
#spannung in V, strom in μΑ, rate pro 120 sekunden
time = 120 # sekunden

rate = unp.uarray(zaehlrate, np.sqrt(zaehlrate))
print("Zerfallsrate N mit Fehler je", time, "Sekunden: N = ")
for index, value in enumerate(stromstaerke):
    print(f"{unp.nominal_values(rate[index]):.0f} +- {unp.std_devs(rate[index]):.0f}")

def lin(x, m, b):
    return(m * x + b)
#Zerfallsrate N mit Fehler je 120 Sekunden:     Zerfallsrate N mit Fehler je Sekunde: 
#12534 +- 112                                   104 +- 10
#23067 +- 152                                   192 +- 14
#23087 +- 152                                   192 +- 14
#23431 +- 153                                   195 +- 14
#23381 +- 153                                   195 +- 14
#23602 +- 154                                   197 +- 14
#23757 +- 154                                   198 +- 14
#24082 +- 155                                   201 +- 14
#23962 +- 155                                   200 +- 14
#23780 +- 154                                   198 +- 14
#23882 +- 155                                   199 +- 14
#23846 +- 154                                   199 +- 14
#23939 +- 155                                   199 +- 14
#24139 +- 155                                   201 +- 14
#24093 +- 155                                   201 +- 14
#24385 +- 156                                   203 +- 14
#24538 +- 157                                   204 +- 14
#24902 +- 158                                   208 +- 14
#25106 +- 158                                   209 +- 14
#25519 +- 160                                   213 +- 15
#26107 +- 162                                   218 +- 15
#26633 +- 163                                   222 +- 15
#-> ich bleibe mal bei der ursprünglichen Darstellung

#HIER WEITER: AUSGLEICHSRECHNUNG FÜR PLATEAU DER ZÄHLRATE

#die Zählrate verwendet ihr zur Bestimmung des Plateaubereichs. Dafür 
#könnt ihr die Zählrate 1/s (y) gegen die Spannung (x) plotten und im 
#Bereich des Plateaus eine lineare Ausgleichsrechnung durchführen.
#
#Mit dem Strom kriegt ihr über Q = I * t die Ladung. Tragt ihr die 
#Ladung gegen die Spannung auf könnt ihr den Verlauf der 
#freigesetzten Ladung mit der zuvor durch die Zählrate dargestellten 
#Kennlinie vergleichen.
strom = unp.uarray(stromstaerke * 10**(-6), 0.05 * 10**(-6) * np.ones(len(stromstaerke)))
ladung = 120 * strom

print("ladung: ")
for index, value in enumerate(stromstaerke): 
    print(f"{unp.nominal_values(ladung[index]):.6f} +- {unp.std_devs(ladung[index]):.6f}")
#ladung: 
# 0.000012 +- 0.000006
# 0.000024 +- 0.000006
# 0.000024 +- 0.000006
# 0.000024 +- 0.000006
# 0.000036 +- 0.000006
# 0.000048 +- 0.000006
# 0.000048 +- 0.000006
# 0.000060 +- 0.000006
# 0.000060 +- 0.000006
# 0.000072 +- 0.000006
# 0.000072 +- 0.000006
# 0.000084 +- 0.000006
# 0.000084 +- 0.000006
# 0.000096 +- 0.000006
# 0.000096 +- 0.000006
# 0.000108 +- 0.000006
# 0.000120 +- 0.000006
# 0.000120 +- 0.000006
# 0.000132 +- 0.000006
# 0.000132 +- 0.000006
# 0.000144 +- 0.000006
# 0.000144 +- 0.000006

plt.figure(constrained_layout = True)
plt.errorbar(spannung, unp.nominal_values(rate), yerr = unp.std_devs(rate), fmt = "x", label = "Messrate mitsamt Fehlerbalken")
plt.xlabel("$U / \\unit{\\volt}$")
plt.ylabel("$N / 120 \\, \\unit{\\second}$") 
plt.legend()
plt.grid()
plt.savefig("build/teil1.pdf")