import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
import c01_nulleffekt as c01
from scipy.optimize import curve_fit


x, count_ag = np.genfromtxt("messung_c03_silber1.txt", unpack = True)
delta_t = 10

t_star = 29 # mit 35 sind die Abweichungen größer
t_max  = 11 # ab 12 werden differenzen der beiden Zeiten negativ

# zerfall nach abzug des nulleffekts je 10s
zerfall_mean = count_ag - c01.mean_silber
zerfall_std = c01.std_silber #vgl. one-note bzw gaußsche fehlerfortpflanzung


#---------------------------------------------------------------------------
#langlebiges isotop

params_l, covariance_matrix_l = np.polyfit(x[t_star-1:], np.log(zerfall_mean[t_star-1:]), deg = 1, cov = True)
errors_l = np.sqrt(np.diag(covariance_matrix_l))

print("parameter langlebig:")
for name, value, error in zip('ab', params_l, errors_l):
 print(f'{name} = {value:.8f} ± {error:.8f}')
#parameter langlebig:
# a = -0.04773947 ± 0.01217383
# b = 3.87385042 ± 0.49250137

#bestimmung der halbwertszeit langlebig:
lamda_l = - ufloat(params_l[0], errors_l[0]) / delta_t # muss auf richtige Zeiteinheit bezogen werden
print("lamda_l in 1/s: ", lamda_l, "/s")
#lamda_l in 1/s:  0.0048+/-0.0012 /s
halbwertszeit_l = unp.log(2) / lamda_l
print("halbwertszeit_l in sekunden: ", halbwertszeit_l, "s")
print("halbwertszeit_l in minuten: ", halbwertszeit_l/60, "min")
#halbwertszeit_l in sekunden:  (1.5+/-0.4)e+02 s
#halbwertszeit_l in minuten:  2.4+/-0.6 min

#bestimmung von N(0)*(1-exp(...)) = exp(b) langlebig:
const_l = ufloat(unp.exp(params_l[1]), errors_l[1] * unp.exp(params_l[1])) #fehler per hand ausgerechnet: delta_c = delta_b * exp(b) (vgl onenote)
print("const_l = N(0)*(1-exp(...)) = ", const_l)
#const_l = N(0)*(1-exp(...)) =  48+/-24


#----------------------------------------------------------------------------------------
#kurzlebiges isotop


differenzen_k_l_mean = zerfall_mean[:t_max-1] - (np.exp(params_l[1]) * np.exp(params_l[0] * x[:t_max-1])) #unp.exp(params_l[1]) = mittelwert von b
differenzen_k_l = zerfall_mean[:t_max-1] - (const_l * unp.exp(- lamda_l * x[:t_max-1] * delta_t))

print("differenzen_k_l_mean: ", differenzen_k_l_mean)
print("differenzen_k_l: ", differenzen_k_l)
#differenzen_k_l_mean:  [142.02696771 105.16596992  73.20525642  50.14947575  40.00305972
#  30.77023357  16.45502555  18.06127612   6.59264673  15.05262812]
#differenzen_k_l:  [142.0269677097211+/-22.604710393462707
# 105.16596992269437+/-21.570657367080337
# 73.20525642349216+/-20.596392046112047
# 50.149475745526146+/-19.677950239755372
# 40.00305971751414+/-18.811619625530987
# 30.770233565789866+/-17.99392667197959
# 16.455025545664547+/-17.221624084632143
# 18.06127612379509+/-16.491678736667076
# 6.592646732489815+/-15.801260052358526
# 15.052628115907247+/-15.147728817726344]


params_k, covariance_matrix_l = np.polyfit(x[:t_max-1], np.log(differenzen_k_l_mean), deg = 1, cov = True)
errors_k = np.sqrt(np.diag(covariance_matrix_l))

print("parameter kurzlebig:")
for name, value, error in zip('ab', params_k, errors_k):
 print(f'{name} = {value:.8f} ± {error:.8f}')
# parameter kurzlebig:
# a = -0.29218124 ± 0.03055004
# b = 5.18875259 ± 0.18955802

#bestimmung der halbwertszeit kurzlebig:
lamda_k = - ufloat(params_k[0], errors_k[0]) / delta_t # muss auf richtige Zeiteinheit bezogen werden
print("lamda_k in 1/s: ", lamda_k, "/s")
#lamda_k in 1/s:  0.0292+/-0.0031 /s
halbwertszeit_k = unp.log(2) / lamda_k
print("halbwertszeit_k in sekunden: ", halbwertszeit_k, "s")
print("halbwertszeit_k in minuten: ", halbwertszeit_k/60, "min")
#halbwertszeit_k in sekunden:  23.7+/-2.5 s
#halbwertszeit_k in minuten:  0.40+/-0.04 min

#bestimmung von N(0)*(1-exp(...)) = exp(b) kurzlebig:
const_k = ufloat(unp.exp(params_k[1]), errors_k[1] * unp.exp(params_k[1])) #fehler per hand ausgerechnet: delta_c = delta_b * exp(b) (vgl onenote)
print("const_k = N(0)*(1-exp(...)) = ", const_k)
#const_k = N(0)*(1-exp(...)) =  179+/-34


#-----------------------------------------------------------
#ungleichung überprüfen

n_k = np.exp(params_k[0] * t_star + params_k[1])
n_l = np.exp(params_l[0] * t_star + params_l[1])
n_abw = (n_l - n_k) / n_l

print("N_kurz = ", n_k)
print("N_lang = ", n_l)
print("N_abw = ", n_abw)
# N_kurz =  0.037459183624506266
# N_lang =  11.85165335402964
# N_abw =  0.9968393284459531





y_min = unp.log(zerfall_mean - zerfall_std)
y_max = unp.log(zerfall_mean + zerfall_std)

yerr_min = unp.log(zerfall_mean) - y_min
yerr_max = y_max - unp.log(zerfall_mean)

y0 = 0.9
y1 = 5.6
xplot = np.linspace(1, 50, 1000)
xplot_l = np.linspace(t_star, 50, 1000)
xplot_k = np.linspace(1, t_max, 1000)
plt.figure(constrained_layout = True)
plt.errorbar(x, unp.log(zerfall_mean), yerr = (yerr_min, yerr_max), fmt = "x", label = "Anzahl der Zerfälle inkl. Fehlerbalken") 
plt.plot(xplot, params_l[0] * xplot + params_l[1],"g--")
plt.plot(xplot_l, params_l[0] * xplot_l + params_l[1],"g-", label = "Ausgleichsgerade (langlebig) ab $t^*$")
plt.plot(xplot, params_k[0] * xplot + params_k[1],"r--")
plt.plot(xplot_k, params_k[0] * xplot_k + params_k[1],"r-", label = "Ausgleichsgerade (kurzlebig) bis $t_\\text{max}$")
#plt.vlines(t_star, y0, y1, color="g", linestyles ="dotted", label="$t^*$")
#plt.vlines(t_max, y0, y1, color="r", linestyles ="dotted", label="$t_\\text{max}$")
plt.ylim(y0, y1)
plt.xlabel("Zeitintervall / $\\qty{10}{\\second}$")
plt.ylabel("$\\log\\left(N_{\\Delta t}(t)\\right)$") #n(t) = count_v - nulleffekt im zeitintervall
plt.grid()
plt.legend()
plt.savefig("build/c03_silber1_log.pdf")


xplot = np.linspace(1, 50, 1000)
plt.figure(constrained_layout = True)
plt.errorbar(x, zerfall_mean, yerr = zerfall_std, fmt = "x", label = "Anzahl der Zerfälle inkl. Fehlerbalken")
plt.xlabel("Zeitintervall / $\\qty{10}{\\second}$")
plt.ylabel("Zerfälle") #n(t) = count_v - nulleffekt im zeitintervall
plt.grid()
plt.legend()
plt.savefig("build/c03_silber1_err.pdf")