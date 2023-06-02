import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy import odr

alpha, parallel, senkrecht, dunkel = np.genfromtxt("messungen/intensitaet.txt", unpack=True)

senkrecht_err = np.zeros(len(senkrecht))
parallel_err = np.zeros(len(parallel))
dunkel_err = np.zeros(len(parallel))

print("senkrecht")
for index, intensitaet in enumerate(senkrecht):
    if intensitaet < 10:
        senkrecht_err[index] = 0.1
        continue
    if intensitaet < 100:
        senkrecht_err[index] = 0.5
        continue
    senkrecht_err[index] = 5

for index, intensitaet in enumerate(senkrecht):
    print(rf"{intensitaet} \pm {senkrecht_err[index]} ")


print("parallel")
for index, intensitaet in enumerate(parallel):
    if intensitaet < 10:
        parallel_err[index] = 0.1
        continue
    if intensitaet < 100:
        parallel_err[index] = 0.5
        continue
    parallel_err[index] = 5

for index, intensitaet in enumerate(parallel):
    print(rf"{intensitaet} \pm {parallel_err[index]} ")


print("dunkel")
for index, intensitaet in enumerate(dunkel):
    if intensitaet < 10:
        dunkel_err[index] = 0.1
        continue
    if intensitaet < 100:
        dunkel_err[index] = 0.5
        continue
    dunkel_err[index] = 5

for index, intensitaet in enumerate(dunkel):
    print(rf"{intensitaet} \pm {dunkel_err[index]} ")

parallel = unp.uarray(parallel, parallel_err)
senkrecht = unp.uarray(senkrecht, senkrecht_err)

parallel_korrigiert = parallel - dunkel 
senkrecht_korrigiert = senkrecht - dunkel 




def n_senkrecht(E_r_senkrecht, E_e_senkrecht, alpha):
    c = E_r_senkrecht
    b = E_e_senkrecht
    return unp.sqrt(2*b*unp.cos(2*alpha)+b**2+c**2)/unp.sqrt(b**2-2*b*c+c**2)
    # Wolfram alpha output:
# -Divide[sqrt\(40)Power[b,2] + Power[c,2] + 2 b c cos\(40)2 a\(41)\(41),sqrt\(40)Power[b,2] - 2 b c + Power[c,2]\(41)]

E_e_senkrecht = ufloat(1800,50)


print("n_senkrecht")
n_senkrecht_values = n_senkrecht(senkrecht_korrigiert,E_e_senkrecht,alpha) 
for index, _stuff in enumerate(nom(n_senkrecht_values)):
    print(n_senkrecht_values[index])

# Für n_parallel:
# solve Divide[b,c] =  Divide[Power[x,2]cos\(40)a\(41) -sqrt\(40)Power[x,2]- Power[sin\(40)a\(41),2]\(41) ,Power[x,2] cos\(40)a\(41) + sqrt\(40)Power[x,2]- Power[sin\(40)a\(41),2]\(41)]
# in wolfram alpha eingeben

print("n_parallel")
def n_parallel(E_r_parallel, E_e_parallel, alpha):
    g = E_r_parallel / E_e_parallel
    return unp.sqrt(0.5 * ((g+1)/((g-1)* unp.cos(alpha)) )**2 + unp.sqrt(0.25 * ((g+1)/((g-1)* unp.cos(alpha)))**4 - ((g + 1)/(g -1) * unp.tan(alpha))**2  ) )

E_e_parallel = ufloat(1000,50)

n_parallel_values = n_parallel(parallel_korrigiert,E_e_parallel,alpha) 
for index, _stuff in enumerate(nom(n_parallel_values)):
    print(alpha[index], "° :", n_parallel_values[index])





plt.errorbar(alpha, nom(parallel_korrigiert) ,  yerr=std(parallel_korrigiert), fmt="x", label=r"Parallel Polarisiertes Licht mit Korrektur") 
plt.errorbar(alpha, nom(senkrecht_korrigiert) ,  yerr=std(senkrecht_korrigiert), fmt="x", label=r"Senkrecht Polarisiertes Licht mit Korrektur") 
# plt.plot(alpha, parallel,"x", label=r"Parallel Polarisiertes Licht ohne Korrektur") 
# plt.plot(alpha, senkrecht, "x", label=r"Senkrecht Polarisiertes Licht ohne Korrektur") 

plt.grid()
plt.legend()
plt.savefig("build/01_plot.pdf")


