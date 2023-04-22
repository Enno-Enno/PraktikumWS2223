import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
import c01_nulleffekt as c01
from scipy.optimize import curve_fit


x, count_ag = np.genfromtxt("messung_c04_silber2.txt", unpack = True)
delta_t = 10




#PROBLEM: y_min = unp.log(zerfall_mean - zerfall_std) ValueError: math domain error 
# -> VERNACHLÄSSIGE ELEMENTE BEI DENEN ln(...) NICHT EXISTIERT
x = np.delete(x, 49)
x = np.delete(x, 47)
x = np.delete(x, 44)
count_ag = np.delete(count_ag, 49)
count_ag = np.delete(count_ag, 47)
count_ag = np.delete(count_ag, 44)

#for index, value in enumerate(count_ag):
#    print(x[index], ": ", value)

# zerfall nach abzug des nulleffekts je 10s
zerfall_mean = count_ag - c01.mean_silber
zerfall_std = c01.std_silber #vgl. one-note bzw gaußsche fehlerfortpflanzung

y_min = unp.log(zerfall_mean - zerfall_std)
y_max = unp.log(zerfall_mean + zerfall_std)

yerr_min = unp.log(zerfall_mean) - y_min
yerr_max = y_max - unp.log(zerfall_mean)

#xplot = np.linspace(0, 30, 1000)
plt.figure(constrained_layout = True)
plt.errorbar(x, unp.log(zerfall_mean), yerr = (yerr_min, yerr_max), fmt = "x", label = "Anzahl der Zerfälle inkl. Fehlerbalken") #log(std) da sonst nicht logaritmus des fehlers dargestellt
#plt.plot(xplot, params[0] * xplot + params[1], label = "Ausgleichsgerade")
plt.xlabel("Zeitintervall / $\\qty{10}{\\second}$")
plt.ylabel("$\\log\\left(N_{\\Delta t}(t)\\right)$") #n(t) = count_v - nulleffekt im zeitintervall
plt.grid()
plt.legend()
plt.savefig("build/c04_silber2_log.pdf")