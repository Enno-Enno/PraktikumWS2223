import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

def function_2(t, a, b, alpha) :
    return (a/(1 + b*t**alpha))

params_k, covariance_matrix_k = curve_fit(function_2, t, temp_k, p0=(1, 1, 1.5))
params_w, covariance_matrix_w = curve_fit(function_2, t, temp_w, p0=(1, 1, 1.5))
#standardwerte anpassen!

print("Funktion 2 für kalt:")
for name, value in zip('abp', params_k):
    print(f"{name} = {value:8.8f}")

print("Funktion 2 für warm:")
for name, value in zip('abp', params_w):
    print(f"{name} = {value:8.8f}")

x=np.linspace(0, 25, 1000)
plt.plot(t, temp_k, "x", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, "x", label="$T_{{\\text{w}}}$")
plt.plot(x, function_2(x, *params_k), "-", label = "Funktion 2 für $T_{{\\text{k}}}$")
plt.plot(x, function_2(x, *params_w), "-", label = "Funktion 2 für $T_{{\\text{w}}}$")
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\celsius}}$")
plt.savefig("build/plot_ausgleich_2.pdf")