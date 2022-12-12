import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

print("B03------------------------------------------------------------------")

index, position, voltage = np.genfromtxt("B03_messdaten.txt", unpack=True)

for i, ort in enumerate(position):
    position[i] /= 100
#umwandlung cm in m

def function(x, a):
    return(a * 1/(x**2))

#def function_exp(x, c, d, e):
#    return(c*np.exp(-d*x) + e)

params, covariance_matrix = curve_fit(function, position, voltage) #p0=(1000, 1) liefert gleiches ergebnis
#params_exp, covariance_matrix_exp = curve_fit(function_exp, position, voltage)

for name, value in zip("ab", params): 
        print(f"{name} = {value:8.8f}")

#for name, value in zip("cde", params_exp): 
#        print(f"{name} = {value:8.8f}")

error = np.sqrt(np.diag(covariance_matrix))
print("fehler: ", error)

x = np.linspace(0.09, 1.51, 1000)
plt.plot(position, voltage, "x", label = "U_\\text{r}")
plt.plot(x, function(x, *params), "-", label = "Ausgleichsfunktion")
#plt.plot(x, function_exp(x, *params_exp), "-", label = "Ausgleichsfunktion_exp")
plt.grid()
plt.xlabel("$r / \\unit{\\meter}$")
plt.ylabel("$U_\\text{r} / \\unit{\\volt}$")
plt.legend()
plt.savefig("build/B03_ausgleichsplot.pdf")

#a = 0.04240297
#b = -0.11438584
#fehler:  [0.00221999 0.06151657]