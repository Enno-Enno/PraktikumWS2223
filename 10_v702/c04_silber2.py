import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
import c01_nulleffekt as c01
from scipy.optimize import curve_fit

# parameter langlebig:
# a = -0.02346305 ± 0.01272034
# b = 3.13246545 ± 0.47801445
# lamda_l in 1/s:  0.0023+/-0.0013 /s
# halbwertszeit_l in sekunden:  (3.0+/-1.6)e+02 s
# halbwertszeit_l in minuten:  4.9+/-2.7 min
# const_l = N(0)*(1-exp(...)) =  23+/-11

# parameter kurzlebig:
# a = -0.24937942 ± 0.01808827
# b = 5.09844481 ± 0.05853057
# lamda_k in 1/s:  0.0249+/-0.0018 /s
# halbwertszeit_k in sekunden:  27.8+/-2.0 s
# halbwertszeit_k in minuten:  0.463+/-0.034 min
# const_k = N(0)*(1-exp(...)) =  164+/-10
# N_kurz =  0.09+/-0.05
# N_lang =  11+/-7
# N_abw =  0.992+/-0.007

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


t_star = 30
# literatur lange halbwertszeit ca 2.3 minuten
# 28 halbwertszeit_l in minuten:  7+/-5 min
# 29 halbwertszeit_l in minuten:  5.6+/-3.3 min
# 30 halbwertszeit_l in minuten:  4.9+/-2.7 min
# 35 halbwertszeit_l in minuten:  -6+/-6 min              NEIN 33, 34, 35, 36, 37, 38, 39, ...
# 32 halbwertszeit_l in minuten:  11+/-17 min            mean- std wird negativ 32, 31


t_max  = 12 # ab 13 werden differenzen der beiden Zeiten negativ -> max 12, nehmen wa
# literaturwert kurze halbwertszeit ca. 24,56
# 12 halbwertszeit_k in sekunden:  27.8+/-2.0 s
# 11 halbwertszeit_k in sekunden:  27.8+/-2.1 s
# 10 halbwertszeit_k in sekunden:  28.0+/-2.4 s
# 9 halbwertszeit_k in sekunden:  27.9+/-2.7 s
# 8 halbwertszeit_k in sekunden:  27.9+/-3.3 s
# 7 halbwertszeit_k in sekunden:  28+/-4 s
# 6 halbwertszeit_k in sekunden:  28+/-6 s
# 5 halbwertszeit_k in sekunden:  29+/-9 s
# 4 halbwertszeit_k in sekunden:  35+/-20 s

# zerfall nach abzug des nulleffekts je 10s
zerfall_mean = count_ag - c01.mean_silber
zerfall_std = c01.std_silber #vgl. one-note bzw gaußsche fehlerfortpflanzung

array = unp.uarray(zerfall_mean, zerfall_std * np.ones(len(x))) #array = N(t) (Zerfallsanzahls)
array_log = unp.log(array)

def lin(t, a, b):
    return(a * t + b)

#---------------------------------------------------------------------------
#langlebiges isotop


params_l, covariance_matrix_l = curve_fit(lin, x[t_star-1:], [i.n for i in array_log[t_star-1:]], p0 = (-0.05, 3.87), sigma = [i.s for i in array_log[t_star-1:]])
errors_l = np.sqrt(np.diag(covariance_matrix_l))

print("parameter langlebig:")
for name, value, error in zip('ab', params_l, errors_l):
 print(f'{name} = {value:.8f} ± {error:.8f}')

a_l = ufloat(params_l[0], errors_l[0])
b_l = ufloat(params_l[1], errors_l[1])

#bestimmung der halbwertszeit langlebig:
lamda_l = - a_l / delta_t # muss auf richtige Zeiteinheit bezogen werden
print("lamda_l in 1/s: ", lamda_l, "/s")
halbwertszeit_l = unp.log(2) / lamda_l
print("halbwertszeit_l in sekunden: ", halbwertszeit_l, "s")
print("halbwertszeit_l in minuten: ", halbwertszeit_l/60, "min")


#bestimmung von N(0)*(1-exp(...)) = exp(b) langlebig:
const_l = unp.exp(b_l)
print("const_l = N(0)*(1-exp(...)) = ", const_l)



#----------------------------------------------------------------------------------------
#kurzlebiges isotop

#ARRAY MUSS IN DIFFERENZEN VERWENDET WERDEN!!



differenzen = array[:t_max-1] - (const_l * unp.exp(a_l * x[:t_max-1]))
print("differenzen: ", differenzen)
#differenzen:  [138.00123869013612+/-74.17017118498016
# 101.1606530244294+/-71.01551693579728
# 69.22663679846323+/-68.02931254255127]

differenzen_log = unp.log(differenzen)


params_k, covariance_matrix_k = curve_fit(lin, x[:t_max-1], [i.n for i in differenzen_log[:t_max-1]], p0 = (-0.05, 3.87), sigma = [i.s for i in differenzen_log[:t_max-1]])
errors_k = np.sqrt(np.diag(covariance_matrix_k))

print("parameter kurzlebig:")
for name, value, error in zip('ab', params_k, errors_k):
 print(f'{name} = {value:.8f} ± {error:.8f}')

a_k = ufloat(params_k[0], errors_k[0])
b_k = ufloat(params_k[1], errors_k[1])


#bestimmung der halbwertszeit kurzlebig:
lamda_k = - a_k / delta_t # muss auf richtige Zeiteinheit bezogen werden
print("lamda_k in 1/s: ", lamda_k, "/s")
halbwertszeit_k = unp.log(2) / lamda_k
print("halbwertszeit_k in sekunden: ", halbwertszeit_k, "s")
print("halbwertszeit_k in minuten: ", halbwertszeit_k/60, "min")

#bestimmung von N(0)*(1-exp(...)) = exp(b) kurzlebig:
const_k = unp.exp(b_k)
print("const_k = N(0)*(1-exp(...)) = ", const_k)


#-----------------------------------------------------------
#ungleichung überprüfen

n_k = unp.exp(a_k * t_star + b_k)
n_l = unp.exp(a_l * t_star + b_l)
n_abw = (n_l - n_k) / n_l

print("N_kurz = ", n_k)
print("N_lang = ", n_l)
print("N_abw = ", n_abw)





#logarithmische darstellung der fehlerbalken in kompliziert
y_min = unp.log(zerfall_mean - zerfall_std)
y_max = unp.log(zerfall_mean + zerfall_std)

yerr_min = unp.log(zerfall_mean) - y_min
yerr_max = y_max - unp.log(zerfall_mean)

x0 = 1
x1 = 50
y0 = -0.2
y1 = 5.5
xplot = np.linspace(x0, x1, 1000)
xplot_l = np.linspace(t_star, x1, 1000)
xplot_k = np.linspace(x0, t_max, 1000)
plt.figure(constrained_layout = True)
plt.axvline(x=t_star, label="t*", color='m')
plt.axvline(x=t_max, label="$t_\\text{max}$", color='k')
plt.errorbar(x, unp.log(zerfall_mean), yerr = (yerr_min, yerr_max), fmt = "x", label = "Anzahl der Zerfälle inkl. Fehlerbalken") 
plt.plot(xplot, params_l[0] * xplot + params_l[1], label = "Ausgleichsgerade (langlebig)")
plt.plot(xplot, params_k[0] * xplot + params_k[1], label = "Ausgleichsgerade (kurzlebig)")
plt.plot(xplot, unp.log(unp.exp((params_l[0]*xplot + params_l[1])) + unp.exp((params_k[0]*xplot + params_k[1]))), label='Summe beider Ausgleichsgeraden')
plt.xlim(x0-1, x1+1)
plt.ylim(y0, y1)
plt.xlabel("Zeitintervall / $\\qty{10}{\\second}$")
plt.ylabel("$\\log\\left(N_{\\Delta t}(t)\\right)$")
plt.grid()
plt.legend()
plt.savefig("build/c04_silber2_log.pdf")