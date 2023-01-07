import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


print("C02-----------------------------------------------------------------")
f, Amplitude_k, Delta_t_k = np.genfromtxt("messdaten/B_C/B_C_kaestchen.txt", unpack=True)

#print("Amplitude_k:", Amplitude_k)
#print("Delta_t_k:",Delta_t_k)
#print("f:", f)

n = len(f)

Amplitude = np.zeros(n)
Null_Amplitude = 3.1 * 0.5
Delta_t = np.zeros(n)
Delta_Phi = np.zeros(n)
T = 1/f * 1000 # ms
print("T:")
for index, zeit in enumerate(T):
    print(index, zeit)

for index, U in enumerate(Amplitude_k[:5]):
    Amplitude[index] = Amplitude_k[index] * 0.5

for index, U in enumerate(Amplitude_k[5:12]):
    Amplitude[index +5]  = Amplitude_k[index + 5] * 0.2

for index, U in enumerate(Amplitude_k[12:]):
    Amplitude[index + 12]  = Amplitude_k[index + 12] * 0.1


print("Amplitude:")
for U in Amplitude:
    print(U)


for index, U in enumerate(Delta_t_k[:1]):
    Delta_t[index] = Delta_t_k[index] * 5

for index, U in enumerate(Delta_t_k[1:7]):
    Delta_t[index + 1]  = Delta_t_k[index + 1] * 2

for index, U in enumerate(Delta_t_k[7:14]):
    Delta_t[index + 7]  = Delta_t_k[index + 7] * 0.5

for index, U in enumerate(Delta_t_k[14:]):
    Delta_t[index + 14]  = Delta_t_k[index + 14] * 0.2

print("Delta_t:")
for index, t in enumerate(Delta_t):
    print(index, t)

for index, t in enumerate(Delta_t):
    Delta_Phi[index] =  Delta_t[index]  / T[index]

print("Delta_Phi:")
for index, Phi in enumerate(Delta_Phi):
    print(Phi)

Delta_Phi = Delta_Phi * 2 * np.pi


#### b) fit 

def A_omega(w, RC_2):
    return 1 / np.sqrt(1+ w * RC_2)

A_plot = Amplitude / Null_Amplitude

params, cov_matrix = curve_fit(A_omega, f, A_plot)
print("params:",params)
print("cov_matrix:", cov_matrix)


print("Hier entsteht Plot 2")

x_plot= np.linspace(f[0], f[-1])
plt.figure(constrained_layout=True)
plt.plot(f, A_plot, "x")
plt.plot(x_plot, A_omega(x_plot, params))

plt.yscale('log')
plt.xlabel("$\\omega / \\unit{{\\hertz}}$")
plt.ylabel("$A(\\omega)/ U_0$")

plt.savefig("build/C02_aufg_b.pdf")