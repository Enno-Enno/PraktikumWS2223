import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

U, I = np.genfromtxt("C01_Kennlinie.txt", unpack=True) # U in Volt I in milli Ampere

print("C01---------------------------")


I = I * 1000 # I in micro Ampere

gradient = np.ones(len(I)) * (-1)
for index in np.arange(1,len(I)):
    gradient[index-1] = (I[index] - I[index-1]) / (U[index] - U[index-1])


# curve fit für Raumkurve
def Raum(U, const, exp ):
   return const * U ** exp

U_raum = U[:4]
I_raum = I[:4]

params_Raum, covariance_matrix_Raum = curve_fit(Raum, U_raum, I_raum)

errors_Raum = np.sqrt(np.diag(covariance_matrix_Raum))
print("Parameter: ")
for name, value, error in zip('ab', params_Raum, errors_Raum):
 print(f'{name} = {value:.3f} ± {error:.3f}')

#curve fit für Sättigungsstrom
U_saet = U[4:]
I_saet = I[4:]


def saet(U, a, b, c, d):
    return  - a * np.exp(-b * (U - d ) ) + c

params_saet, covariance_matrix_saet = curve_fit(saet, U_saet, I_saet)

errors_saet = np.sqrt(np.diag(covariance_matrix_saet))
print("Parameter: ")
for name, value, error in zip('abcd', params_saet, errors_saet):
 print(f'{name} = {value:.3f} ± {error:.3f}')



# Ausgabe Tabelle mit gradient
# print("U, gradient")
# for index in np.arange(0,len(I)):
    # print(index, "  &", U[index], "\t&", I[index], "   &", gradient[index], "\\\\")
indices = np.arange(0,len(I))
print(indices[:4])
print(indices[4:])




# Plot

plt.figure(constrained_layout=True)
xplot_Raum = np.linspace(0, U[4] + 1)
xplot_saet = np.linspace(U[4] + 1, U[-1] + 1)
plt.plot(U, I, "x", label="Messwerte")
plt.plot(xplot_Raum,Raum(xplot_Raum,*params_Raum), label="Raumkurve")
plt.plot(xplot_saet,saet(xplot_saet,*params_saet), label="Sättigungskurve")
plt.xlabel("$U_A / \\unit{{\\volt}}$")
plt.ylabel("$I / \\unit{{\\micro\\ampere}}$")
plt.grid
plt.legend()

 
plt.savefig("build/C01_plot.pdf")