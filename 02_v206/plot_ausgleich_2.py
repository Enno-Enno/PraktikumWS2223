import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15
    temp_w[i] += 273.15

def function_2(t, a, b, alpha) :
    return (a/(1 + b*t**alpha))

params_k, covariance_matrix_k = curve_fit(function_2, t, temp_k, p0=(300, 2, 1))
params_w, covariance_matrix_w = curve_fit(function_2, t, temp_w, p0=(300, -0.02, 1))

print("Funktion 2 für kalt:")
for name, value in zip('abp', params_k):
    print(f"{name} = {value:8.8f}")

print("Funktion 2 für warm:")
for name, value in zip('abp', params_w):
    print(f"{name} = {value:8.8f}")

#Funktion 2 für kalt:
#a = 281.45416633
#b = -54362337.91818563
#p = -2587.15903485
#Funktion 2 für warm:
#a = 292.67441477
#b = -0.00976323
#p = 0.69217610

x=np.linspace(0.0001, 25, 1000)
plt.plot(t, temp_k, "x", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, "x", label="$T_{{\\text{w}}}$")
plt.plot(x, function_2(x, *params_k), "-", label = "Funktion 2 für $T_{{\\text{k}}}$")
plt.plot(x, function_2(x, *params_w), "-", label = "Funktion 2 für $T_{{\\text{w}}}$")
plt.ylim(270, 325)
plt.grid()
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\kelvin}}$")
plt.savefig("build/plot_ausgleich_2.pdf")
