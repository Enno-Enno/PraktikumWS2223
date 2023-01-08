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

Delta_Phi_plot = Delta_Phi * 2 * np.pi


#### b) fit 

def A_omega(w, RC_2):
    return 1 / np.sqrt(1+ w ** 2 * RC_2 **2) #Variante möglich mit variabler Null_Amplitude 
                                            # -> liefert besseren Fit ist aber nicht so einfach zu erklären...

A_plot = Amplitude / Null_Amplitude

RC_2_ergeb, cov_matrix_2 = curve_fit(A_omega, f, A_plot, p0=(0.00281) )
print("RC_2_ergeb:",RC_2_ergeb)
print("cov_matrix_2:", cov_matrix_2)

#### c) fit

def Phi_omega(w, RC_3):
    return np.arctan(-w * RC_3)

RC_3_ergeb, cov_matrix_3 = curve_fit(Phi_omega, f, Delta_Phi_plot, p0=(0.00281) )
print("RC_3_ergeb:",RC_3_ergeb)
print("cov_matrix_3:", cov_matrix_3)


x_plot= np.linspace(f[0], f[-1])

### Die anderen beiden Dateien übernehmen das plotten.