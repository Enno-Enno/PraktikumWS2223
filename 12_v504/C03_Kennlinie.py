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

U_raum= U[:17]
I_raum= I[:17]

def f(U, a, b ):
   return a * U ** b

params, covariance_matrix = curve_fit(f, U_raum, I_raum, p0=(200, 1.5))

errors = np.sqrt(np.diag(covariance_matrix))
print("Parameter: ")
for name, value, error in zip('ab', params, errors):
 print(f'{name} = {value:.3f} ± {error:.3f}')


# Plot

xplot = np.linspace(0, U[17])
plt.plot(U, I, "x")
plt.plot(xplot,f(xplot,*params))
plt.xlabel("U in Volt")
plt.ylabel("I in micro Ampere")


plt.savefig("build/C03_plot.pdf")