import numpy as np
import matplotlib.pyplot as plt

t, temp_k, druck_k, temp_w, druck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15

params, covariance_matrix = np.polyfit(1/temp_k, np.log(druck_k), deg = 1, cov=True)

print("Steigung m=", params[0])
print("achsenabschn b= ", params[1])

#Steigung m= -2001.814130953005
#achsenabschn b=  8.363939543080686

x = np.linspace(0.00339, 0.003675, 1000)

plt.figure(constrained_layout=True)
plt.plot(1/temp_k, np.log(druck_k), "x", label="$p_{{\\text{k}}}$")
plt.plot(x, (params[0] * x +params[1]), "-", label="lineare Regression")
#plt.yscale("log")
plt.legend()
plt.xlabel("$1/T_{{\\text{k}}} / \\left(\\unit{{1/ \\kelvin}}\\right)$")
plt.ylabel("$\\log\\left(\\frac{p_{{\\text{k}}}}{p_0}\\right)$")
#/ \\unit{{\\bar}}
plt.savefig("build/plot_verdampfungswaerme.pdf")