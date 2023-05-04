import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

U, I = np.genfromtxt("C02_Kennlinie.txt", unpack=True) # U in Volt I in milli Ampere

print("C02---------------------------")

I = I * 1000 # I in micro Ampere

# Ausgabe der Werte mit Gradient
print("U, gradient")

gradient = np.ones(len(U)) *(-1)
for index in np.arange(1,len(I)):
    gradient[index-1] = (I[index] - I[index-1]) / (U[index] - U[index-1])

for index in np.arange(0,len(I)):
    print(index, "  &", U[index], "\t&", I[index], "   &", gradient[index], "\\\\")


# Curve fit für die Raumkoordinaten

U_raum= U[:11]
I_raum= I[:11]

def f(U, a, b ):
   return a * U ** b

params, covariance_matrix = curve_fit(f, U_raum, I_raum, p0=(200, 1.5))

errors = np.sqrt(np.diag(covariance_matrix))
print("Parameter: ")
for name, value, error in zip('ab', params, errors):
 print(f'{name} = {value:.3f} ± {error:.3f}')




xplot = np.linspace(0, U[11])
plt.plot(U, I, "x")
plt.plot(xplot,f(xplot,*params))
plt.xlabel("U in Volt")
plt.ylabel("I in micro Ampere")

plt.savefig("build/C02_plot.pdf")