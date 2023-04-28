import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

# Teil 2: Brechungsgesetz
# n = 1.49702650 +- 0.00626929
# b = 0.00198052 +- 0.00195368
# Brechungsindex: n =  1.497+/-0.006
# Abweichung zur Literatur:  0.005+/-0.004
# Lichtgeschwindigkeit in Plexiglas: v =  (2.003+/-0.008)e+08  m/s =  0.6680+/-0.0028  c 

# Teil 3: Strahlversatz
# Strahlversatz : s =  
# [0.5177265243031446+/-0.1016890274635045
#  0.6810564443122777+/-0.10147428935944072
#  1.1309472733837191+/-0.09951092473453996
#  1.6228084471524857+/-0.09600872518565101
#  2.221939290047947+/-0.08932428325308159
#  2.979866388540225+/-0.07702490505550862
#  3.876971492684826+/-0.05782021861223494] cm
# neu gerechnetes beta: β =  
# [0.17376183799045458+/-0.0007350981920326408
#  0.23050205167403742+/-0.0009827704997573978
#  0.34053924999584023+/-0.0014839310629197642
#  0.4438019961178242+/-0.0019910345212903018
#  0.537174721815124+/-0.0024942530415351227
#  0.6168849138261443+/-0.0029700785203662775
#  0.6786029088706705+/-0.0033768700296112984] rad =  
# [9.955819957289018+/-0.04211802393116764  
#  13.206794730028756+/-0.05630860186606159
#  19.511461783312082+/-0.0850229869936647
#  25.427981317032675+/-0.11407787493478454
#  30.77784442112068+/-0.14291017231763134
#  35.344902007529555+/-0.17017296403944804
#  38.88108264359024+/-0.1934804006609447] deg
# Strahlversatz die Zweite: s =  
# [0.5222185400199149+/-0.004281779028244064
#  0.7107729910151951+/-0.005700010449844021
#  1.129806619908172+/-0.008461915238928518
#  1.6297187297376368+/-0.010939367518440959
#  2.241737153147955+/-0.01270626664757905
#  2.991789803323222+/-0.013057180380057095
#  3.8838357932126644+/-0.011149617241589785] cm
# Strahlversatz Abweichung :  
# [-0.008601792875065229+/-0.1948946322580831
#  -0.04180877309430861+/-0.14297274687324923
#  0.0010096006302741068+/-0.08839634923931533
#  -0.004240168845739101+/-0.05928918706357141
#  -0.008831482795477099+/-0.04024010905345669
#  -0.003985378508126771+/-0.026109824150291686
#  -0.0017674023551238513+/-0.015160703557230005]

alpha, beta = np.genfromtxt("messung_2_brechung.txt", unpack = True)

einfall = np.deg2rad(alpha)
ausfall = unp.uarray(np.deg2rad(beta), np.deg2rad(1) * np.ones(len(beta)))
# zur umrechnung zu rad: np.deg2rad(

def sin_beta(sin_alpha, n, b):
    return(sin_alpha / n + b)

params, covariance_matrix = curve_fit(sin_beta, unp.sin(einfall), [i.n for i in unp.sin(ausfall)], sigma = [i.s for i in unp.sin(ausfall)])
errors = np.sqrt(np.diag(covariance_matrix))

print("Teil 2: Brechungsgesetz")
for name, value, error in zip("nb", params, errors):
     print(f'{name} = {value:.8f} +- {error:.8f}')


#brechungsindex
index_exp = ufloat(params[0], errors[0])
index_lit = 1.49
index_abweichung = (index_exp - index_lit) / index_lit
print("Brechungsindex: n = ", index_exp)
print("Abweichung zur Literatur: ", index_abweichung)

#lichtgeschwindigkeit
speed = 1/index_exp * const.c
print("Lichtgeschwindigkeit in Plexiglas: v = ", speed, " m/s = ", speed/const.c, " c")





print("Teil 3: Strahlversatz")

d = 5.85 #breite in cm

s_1 = d * unp.sin(einfall - ausfall) / unp.cos(ausfall)
print("Strahlversatz : s = ", s_1, "cm")

beta_new = unp.arcsin(1/index_exp * unp.sin(einfall))
print("neu gerechnetes beta: β = ", beta_new, "rad = ", beta_new/(2*np.pi) * 360, "deg")

s_2 = d * unp.sin(einfall - beta_new) / unp.cos(beta_new)
print("Strahlversatz die Zweite: s = ", s_2, "cm")

s_abweichung = (s_1 - s_2)/s_2
print("Strahlversatz Abweichung : ", s_abweichung)


x = np.linspace(unp.sin(einfall[0]), unp.sin(einfall[len(einfall)-1]), 1000)
plt.figure(constrained_layout = True)
plt.errorbar(unp.sin(einfall), [i.n for i in unp.sin(ausfall)], yerr = [i.s for i in unp.sin(ausfall)], fmt = "x", label = "Messwerte inkl. Fehlerbalken")
plt.plot(x, sin_beta(x, *params), label = "Ausgleichsfunktion")
plt.xlabel("$\\sin(\\alpha)")# / \\unit{\\degree}$")
plt.ylabel("$\\sin(\\beta)")# / \\unit{\\degree}$")
plt.grid()
plt.legend()
plt.savefig("build/c02_brechung.pdf")

