import numpy as np
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

spannung, stromstaerke, zaehlrate = np.genfromtxt("messungen/teil1.txt", unpack = True)
#spannung in V, strom in μΑ, rate pro 120 sekunden
time = 120 # sekunden

#Abweichungscheck:  maximal 0.9% Abweichung bei Intervallen von 120 Sekunden
#rate_je_120 = unp.uarray(zaehlrate, np.sqrt(zaehlrate))
#print("Zerfallsrate N mit Fehler je", time, "Sekunden: N = ")
#for index, value in enumerate(stromstaerke):
#    print(f"{unp.nominal_values(rate_je_120[index]):.0f} +- {unp.std_devs(rate_je_120[index]):.0f}, prozentuale Abweichung: {unp.std_devs(rate_je_120[index])/unp.nominal_values(rate_je_120[index]):.5f}")


#von hier an pro Sekunde
zaehlrate /= time
rate = unp.uarray(zaehlrate, np.sqrt(zaehlrate))
print("Zerfallsrate N mit Fehler je Sekunde: N = ")
for index, value in enumerate(stromstaerke):
    print(f"{unp.nominal_values(rate[index]):.0f} +- {unp.std_devs(rate[index]):.0f}, prozentuale Abweichung: {unp.std_devs(rate[index])/unp.nominal_values(rate[index]):.5f}")

def lin(x, m, b):
    return(m * x + b)

#indexwahl für plateau bereich:
plateau_min =  1
plateau_max = 16

spannung_plateau = spannung[plateau_min : plateau_max] # 330 bis 670 V
rate_plateau = rate[plateau_min : plateau_max]

params_plateau, covariance_matrix_plateau = curve_fit(lin, spannung_plateau, unp.nominal_values(rate_plateau), sigma = unp.std_devs(rate_plateau))
errors_plateau = np.sqrt(np.diag(covariance_matrix_plateau))
print("Parameter des Plateaus: ")
for name, value, error in zip('mb', params_plateau, errors_plateau):
 print(f'{name} = {value:.6f} +- {error:.6f}')


#Mit dem Strom kriegt ihr über Q = I * t die Ladung. Tragt ihr die 
#Ladung gegen die Spannung auf könnt ihr den Verlauf der 
#freigesetzten Ladung mit der zuvor durch die Zählrate dargestellten 
#Kennlinie vergleichen.
#strom = unp.uarray(stromstaerke[plateau_min : plateau_max] * 10**(-6), 0.05 * 10**(-6) * np.ones(len(stromstaerke[plateau_min : plateau_max])))
strom = unp.uarray(stromstaerke * 10**(-6), 0.05 * 10**(-6) * np.ones(len(stromstaerke)))
ladung = time * strom # ladung in 120 sekunden
#ladung *= time # pro sekunde
ladungszahl = ladung  / const.e

print("ladungszahl pro Sekunde: ")
for index, value in enumerate(spannung): 
    print(f"{unp.nominal_values(ladungszahl[index]):.6f} +- {unp.std_devs(ladungszahl[index]):.6f}")

params_ladungszahl, covariance_matrix_ladungszahl = curve_fit(lin, spannung, unp.nominal_values(ladungszahl), p0 = (1e14, 0.5e14), sigma = unp.std_devs(ladungszahl))
errors_ladungszahl = np.sqrt(np.diag(covariance_matrix_ladungszahl))
print("Parameter für die Ladungsanzahl: ")
for name, value, error in zip('mb', params_ladungszahl, errors_ladungszahl):
 print(f'{name} = {value:.6f} +- {error:.6f}')

steigung = strom
for index, value in enumerate(strom):
    steigung[index] = ufloat(params_ladungszahl[0], errors_ladungszahl[0]) * const.e * (index + 1) / (value * time)
print("Steigung in neuer Größenordnung: ", steigung)

steigung_ufl = sum(steigung) / len(steigung)
print(steigung_ufl)

abweichung_steigung = (ufloat(params_plateau[0], errors_plateau[0]) - steigung_ufl) / steigung_ufl
print("abweichung der steigung in Prozent:", abweichung_steigung * 100, "\, \%")


x_rate = np.linspace(spannung[plateau_min], spannung[plateau_max], 1000)
x_ladungszahl= np. linspace(spannung[0], spannung[21], 1000)
x_min = 290
x_max = 750
y_min =  90
y_max = 245

plt.figure(constrained_layout = True)
plt.errorbar(spannung, unp.nominal_values(rate), yerr = unp.std_devs(rate), fmt = "x", label = "Messrate mitsamt Fehlerbalken")
plt.plot(x_rate, lin(x_rate, *params_plateau), "-", label = "Ausgleichsgerade des Plateaus")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel("$U / \\unit{\\volt}$")
plt.ylabel("$N / \\unit{\\second}$") 
plt.legend()
plt.grid()
plt.savefig("build/teil1_rate.pdf")

plt.figure(constrained_layout = True)
plt.errorbar(spannung, unp.nominal_values(ladungszahl), yerr = unp.std_devs(ladungszahl), fmt = "x", label = "Ladungsanzahl mitsamt Fehlerbalken")
plt.plot(x_ladungszahl, lin(x_ladungszahl, *params_ladungszahl), "-", label = "Ausgleichsgerade der Ladungszahl")
plt.xlim(x_min, x_max)
#plt.ylim(y_min, y_max)
plt.xlabel("$U / \\unit{\\volt}$")
plt.ylabel("$Z / \\unit{\\second}$") 
plt.legend()
plt.grid()
plt.savefig("build/teil1_ladungszahl.pdf")


# Zerfallsrate N mit Fehler je Sekunde: N = 
# 104 +- 10, prozentuale Abweichung: 0.09785
# 192 +- 14, prozentuale Abweichung: 0.07213
# 192 +- 14, prozentuale Abweichung: 0.07210
# 195 +- 14, prozentuale Abweichung: 0.07156
# 195 +- 14, prozentuale Abweichung: 0.07164
# 197 +- 14, prozentuale Abweichung: 0.07130
# 198 +- 14, prozentuale Abweichung: 0.07107
# 201 +- 14, prozentuale Abweichung: 0.07059
# 200 +- 14, prozentuale Abweichung: 0.07077
# 198 +- 14, prozentuale Abweichung: 0.07104
# 199 +- 14, prozentuale Abweichung: 0.07089
# 199 +- 14, prozentuale Abweichung: 0.07094
# 199 +- 14, prozentuale Abweichung: 0.07080
# 201 +- 14, prozentuale Abweichung: 0.07051
# 201 +- 14, prozentuale Abweichung: 0.07057
# 203 +- 14, prozentuale Abweichung: 0.07015
# 204 +- 14, prozentuale Abweichung: 0.06993
# 208 +- 14, prozentuale Abweichung: 0.06942
# 209 +- 14, prozentuale Abweichung: 0.06914
# 213 +- 15, prozentuale Abweichung: 0.06857
# 218 +- 15, prozentuale Abweichung: 0.06780
# 222 +- 15, prozentuale Abweichung: 0.06712
# Parameter des Plateaus:
# m = 0.032425 +- 0.004192
# b = 182.769876 +- 1.998106
# ladungszahl pro Sekunde:
# 74898108893529.156250 +- 37449054446764.578125
# 149796217787058.312500 +- 37449054446764.578125
# 149796217787058.312500 +- 37449054446764.578125
# 149796217787058.312500 +- 37449054446764.578125
# 224694326680587.468750 +- 37449054446764.578125
# 299592435574116.625000 +- 37449054446764.578125
# 299592435574116.625000 +- 37449054446764.578125
# 374490544467645.750000 +- 37449054446764.578125
# 374490544467645.750000 +- 37449054446764.578125
# 449388653361174.937500 +- 37449054446764.578125
# 449388653361174.937500 +- 37449054446764.578125
# 524286762254704.062500 +- 37449054446764.578125
# 524286762254704.062500 +- 37449054446764.578125
# 599184871148233.250000 +- 37449054446764.578125
# 599184871148233.250000 +- 37449054446764.578125
# 674082980041762.375000 +- 37449054446764.578125
# 748981088935291.500000 +- 37449054446764.578125
# 748981088935291.500000 +- 37449054446764.578125
# 823879197828820.750000 +- 37449054446764.578125
# 823879197828820.750000 +- 37449054446764.578125
# 898777306722349.875000 +- 37449054446764.578125
# 898777306722349.875000 +- 37449054446764.578125
# Parameter für die Ladungsanzahl:
# m = 2010957130865.852783 +- 39616477067.084023
# b = -552051081251977.250000 +- 21204994539153.195312
# Steigung in neuer Größenordnung:  [0.02684923772540791+/-0.013435035069376235
#  0.02684923772540791+/-0.0067331176737614835
#  0.04027385658811187+/-0.010099676510642225
#  0.05369847545081582+/-0.013466235347522967
#  0.04474872954234651+/-0.0075100421035665665
#  0.04027385658811187+/-0.005096370071887211
#  0.04698616601946384+/-0.005945765083868414
#  0.042958780360652656+/-0.004378446517818224