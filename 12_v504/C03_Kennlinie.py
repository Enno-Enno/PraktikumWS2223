import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

U, I = np.genfromtxt("C03_Kennlinie.txt", unpack=True) # U in Volt I in milli Ampere

print("C03---------------------------")


I = I * 1000 # I in micro Ampere

gradient = np.ones(len(I)) * (-1)
for index in np.arange(1,len(I)):
    gradient[index-1] = (I[index] - I[index-1]) / (U[index] - U[index-1])




# Ausgabe der Werte mit Gradient
print("Nr. &  U & I &  gradient")

for index in np.arange(0,len(I)):
    print(index, "  &", U[index], "\t&", I[index], "   &", gradient[index], "\\\\")

# Curve fit für die Raumkoordinaten

U_raum= U[:18]
I_raum= I[:18]

def f(U, a, b ):
   return a * U ** b

params, covariance_matrix = curve_fit(f, U_raum, I_raum, p0=(200, 1.5))

errors = np.sqrt(np.diag(covariance_matrix))
print("Parameter: ")
for name, value, error in zip('ab', params, errors):
 print(f'{name} = {value:.3f} \pm {error:.3f}')


I_s = 2300

# Plot
plt.figure(constrained_layout=True)
xplot_saet = np.linspace(0, U[-1])
xplot = np.linspace(0, U[18]+1)
plt.plot(U, I, "x", label="Messwerte")
plt.plot(xplot,f(xplot,*params), label="Raumkurve")
# plt.plot(xplot_saet,np.exp(saet(xplot_saet,*params_saet)), label="Sättigungskurve")
plt.plot(xplot_saet,I_s * np.ones(len(xplot_saet)), "k--", label="$I_s$") 
plt.xlabel("$U_A / \\unit{{\\volt}}$")
plt.ylabel("$I / \\unit{{\\micro\\ampere}}$")
plt.grid()
plt.legend()

plt.savefig("build/C03_plot.pdf")