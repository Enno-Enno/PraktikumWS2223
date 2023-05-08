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

def Raum(U, a, b ):
   return a * U ** b

params_Raum, covariance_matrix = curve_fit(Raum, U_raum, I_raum, p0=(200, 1.5))

errors = np.sqrt(np.diag(covariance_matrix))
print("Parameter: ")
for name, value, error in zip('ab', params_Raum, errors):
 print(f'{name} = {value:.3f} \pm {error:.3f}')

# #curve fit für Sättigungsstrom
# U_saet = U[11:]
# I_saet = I[11:]

# def saet(U, a, b, c, d):
#     return np.log(- a) * ( -1* (U - d) ) + np.log(c)

# params_saet, covariance_matrix_saet = curve_fit(saet, np.log(U_saet), np.log(I_saet) ) # p0=(1,1,600,U[11])

# errors_saet = np.sqrt(np.diag(covariance_matrix_saet))
# print("Parameter: ")
# for name, value, error in zip('abcd', params_saet, errors_saet):
#  print(f'{name} = {value:.3f} ± {error:.3f}')

I_s = 600


# Plot

plt.figure(constrained_layout=True)
xplot_Raum = np.linspace(0, U[11] + 1)
xplot_saet = np.linspace(0, U[-1] + 1)
plt.plot(U, I, "x", label="Messwerte")
plt.plot(xplot_Raum,Raum(xplot_Raum,*params_Raum), label="Raumkurve")
# plt.plot(xplot_saet,np.exp(saet(xplot_saet,*params_saet)), label="Sättigungskurve")
plt.plot(xplot_saet,I_s * np.ones(len(xplot_saet)), "k--", label="$I_s$") 
plt.xlabel("$U_A / \\unit{{\\volt}}$")
plt.ylabel("$I / \\unit{{\\micro\\ampere}}$")
plt.grid()
plt.legend()

plt.savefig("build/C02_plot.pdf")