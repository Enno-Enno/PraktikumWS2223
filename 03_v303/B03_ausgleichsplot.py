import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

print("B03------------------------------------------------------------------")

index, position, voltage = np.genfromtxt("B03_messdaten.txt", unpack=True)

#print("abstand: ", position-5)

for i, ort in enumerate(position):
    position[i] -= 5
    position[i] /= 100
#umwandlung cm in m

def function(x, a, b):
    return(a * 1/(x**2) + b)

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

plt.figure(constrained_layout=True)
x = np.linspace(position[0], 1.51, 1000)
plt.plot(position, voltage, "x", label = "$U_\\text{r}$")
plt.plot(x, function(x, *params), "-", label = "Ausgleichsfunktion")
#plt.plot(x, function_exp(x, *params_exp), "-", label = "Ausgleichsfunktion_exp")
plt.grid()
plt.xlabel("$r / \\unit{\\meter}$")
plt.ylabel("$U / \\unit{\\volt}$")
plt.legend()
plt.savefig("build/B03_ausgleichsplot.pdf")

#a = 0.01125850
#b = 0.02540392
#fehler:  [0.00014112 0.01423447]