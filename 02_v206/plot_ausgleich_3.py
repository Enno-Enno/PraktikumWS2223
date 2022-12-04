import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15
    temp_w[i] += 273.15

def function_3(t, a, b, c, alpha) :
    return ((a*t**alpha)/(1 + b*t**alpha) + c)

params_k, covariance_matrix_k = curve_fit(function_3, t, temp_k, p0=(-1, 0, 21, 1))
params_w, covariance_matrix_w = curve_fit(function_3, t, temp_w, p0=(1, 0, 21, 1))

#Funktion 3 für kalt:
#a = -0.91131991
#b = 0.02042679
#c = 294.66604398
#p = 1.19462372
#Funktion 3 für warm:
#a = 1.13913900
#b = 0.02290029
#c = 294.04673712
#p = 1.22110015

print("Funktion 3 für kalt:")
for name, value in zip('abcp', params_k):
    print(f"{name} = {value:8.8f}")

print("Funktion 3 für warm:")
for name, value in zip('abcp', params_w):
    print(f"{name} = {value:8.8f}")

x=np.linspace(0, 25, 1000)
plt.plot(t, temp_k, "x", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, "x", label="$T_{{\\text{w}}}$")
plt.plot(x, function_3(x, *params_k), "-", label = "Funktion 3 für $T_{{\\text{k}}}$")
plt.plot(x, function_3(x, *params_w), "-", label = "Funktion 3 für $T_{{\\text{w}}}$")
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\kelvin}}$")
plt.savefig("build/plot_ausgleich_3.pdf")
