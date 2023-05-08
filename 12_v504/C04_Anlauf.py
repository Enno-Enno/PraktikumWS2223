import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

#Daten einsammeln
U_gem, I = np.genfromtxt("C04_Anlauf.txt", unpack=True)


# Korrektur des Fehlers aufgrund des Messgeräts
R = 10 ** 6 # Ohm
U = np.zeros(len(U_gem))
for index in np.arange(0,len(I)):
    U[index] = U_gem[index] + I[index] *1e-9 *R



# Fitten einer Exponentialfunktion
def f(U, a, b):
    return a* np.exp(b*U)

params, covariance_matrix = curve_fit(f, U, I)

errors = np.sqrt(np.diag(covariance_matrix))
print("Parameter: ")
for name, value, error in zip('ab', params, errors):
 print(f'{name} = {value:.3f} \pm {error:.3f}')

# Ausgabe der Tabelle
for index in np.arange(0,len(I)):
    print(f"{U_gem[index]:.2f}  &  {U[index]:.2f} \t& {I[index]:.2f} \\\\")

#Plot
 
xplot = np.linspace(U[0],U[-1])
plt.plot(U, I, "x", label="Messwerte")
plt.plot(xplot,f(xplot,*params), label="Anlaufkurve")
plt.xlabel("$U_A / \\unit{{\\volt}}$")
plt.ylabel("$I / \\unit{{\\nano\\ampere}}  $")

plt.grid()
plt.legend()

plt.savefig("build/C04_plot.pdf")  