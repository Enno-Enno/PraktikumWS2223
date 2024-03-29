import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
import c01_nulleffekt as c01
from scipy.optimize import curve_fit


x, count_v = np.genfromtxt("messung_c02_vanadium.txt", unpack = True)
delta_t = 35

# zerfall nach abzug des nulleffekts je 35s
zerfall_mean = count_v - c01.mean_vanadium
zerfall_std = c01.std_vanadium #vgl. one-note bzw gaußsche fehlerfortpflanzung

array = unp.uarray(zerfall_mean, zerfall_std * np.ones(len(x)))
array = unp.log(array)
def lin(t, a, b):
    return(a * t + b)

params, covariance_matrix = curve_fit(lin, x, [i.n for i in array], p0 = (-0.1, 5.2), sigma = [i.s for i in array]) 
#n = nominal_value = nominale werte = mittelwert, s = standardabweichung des ufloats
errors = np.sqrt(np.diag(covariance_matrix))
print("Parameter: ")
for name, value, error in zip('ab', params, errors):
 print(f'{name} = {value:.8f} ± {error:.8f}')


###### NEUE PARAMETER MIT BESSEREN ABWEICHUNGEN
# a = -0.10603542 ± 0.00534514
# b = 5.36902879 ± 0.03755019
# lamda in 1/s:  0.00303+/-0.00015 /s
# halbwertszeit in sekunden:  229+/-12 s
# halbwertszeit in minuten:  3.81+/-0.19 min
# const = N(0)*(1-exp(...)) =  215+/-8

####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........params, covariance_matrix = np.polyfit(x, np.log(zerfall_mean), deg = 1, cov = True)
####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........errors = np.sqrt(np.diag(covariance_matrix))
####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........
####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........for name, value, error in zip('ab', params, errors):
####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........ print(f'{name} = {value:.8f} ± {error:.8f}')
####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........# a = -0.10153046 ± 0.00483896
####### hab ich jetzt auch mitsamt der standardabweichung des nulleffekts........# b = 5.29056262 ± 0.08590575

#bestimmung der halbwertszeit:
lamda = - ufloat(params[0], errors[0]) / delta_t # muss auf richtige Zeiteinheit bezogen werden
print("lamda in 1/s: ", lamda, "/s")
#lamda in 1/s:  0.00290+/-0.00014 /s
halbwertszeit = unp.log(2) / lamda
print("halbwertszeit in sekunden: ", halbwertszeit, "s")
print("halbwertszeit in minuten: ", halbwertszeit/60, "min")
# halbwertszeit in sekunden:  239+/-11 s
# halbwertszeit in minuten:  3.98+/-0.19 min


#bestimmung von N(0)*(1-exp(...)) = exp(b):
const = ufloat(unp.exp(params[1]), errors[1] * unp.exp(params[1])) #fehler per hand ausgerechnet: delta_c = delta_b * exp(b) (vgl onenote)
print("const = N(0)*(1-exp(...)) = ", const)
#const = N(0)*(1-exp(...)) =  198+/-17


y_min = unp.log(zerfall_mean - zerfall_std)
y_max = unp.log(zerfall_mean + zerfall_std)

yerr_min = unp.log(zerfall_mean) - y_min
yerr_max = y_max - unp.log(zerfall_mean)

xplot = np.linspace(1, 30, 1000)
plt.figure(constrained_layout = True)
plt.errorbar(x, unp.log(zerfall_mean), yerr = (yerr_min, yerr_max), fmt = "x", label = "Anzahl der Zerfälle inkl. Fehlerbalken") #log(std) da sonst nicht logaritmus des fehlers dargestellt
plt.plot(xplot, params[0] * xplot + params[1], label = "Ausgleichsgerade")
plt.xlabel("Zeitintervall / $\\qty{35}{\\second}$")
plt.ylabel("$\\log\\left(N_{\\Delta t}(t)\\right)$") #n(t) = count_v - nulleffekt im zeitintervall
plt.grid()
plt.legend()
plt.savefig("build/c02_vanadium_log.pdf")


xplot = np.linspace(1, 30, 1000)
plt.figure(constrained_layout = True)
plt.errorbar(x, zerfall_mean, yerr = zerfall_std, fmt = "x", label = "Anzahl der Zerfälle inkl. Fehlerbalken")
plt.xlabel("Zeitintervall / $\\qty{35}{\\second}$")
plt.ylabel("Zerfälle") #n(t) = count_v - nulleffekt im zeitintervall
plt.grid()
plt.legend()
plt.savefig("build/c02_vanadium_err.pdf")