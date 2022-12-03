import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15
    temp_w[i] += 273.15

def function_1(t, a, b, c) :
    return (a*t**2 + b*t + c)

params_k, covariance_matrix_k = curve_fit(function_1, t, temp_k)
params_w, covariance_matrix_w = curve_fit(function_1, t, temp_w)

print("Funktion 1 für kalt:")
for name, value in zip('abc', params_k):
    print(f"{name} = {value:8.8f}")

print("Funktion 1 für warm:")
for name, value in zip('abc', params_w):
    print(f"{name} = {value:8.8f}")

#Funktion 1 für kalt:
#a = 0.01497863
#b = -1.26058547
#c = 295.01282051
#Funktion 1 für warm:
#a = -0.02154457
#b = 1.62675092
#c = 293.57844933

x=np.linspace(0, 25, 1000)
plt.plot(t, temp_k, "x", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, "x", label="$T_{{\\text{w}}}$")
plt.plot(x, function_1(x, *params_k), "-", label = "Funktion 1 für $T_{{\\text{k}}}$")
plt.plot(x, function_1(x, *params_w), "-", label = "Funktion 1 für $T_{{\\text{w}}}$")
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\kelvin}}$")
plt.savefig("build/plot_ausgleich_1.pdf")
