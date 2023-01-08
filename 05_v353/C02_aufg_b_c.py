import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C01_aufg_a as C01


print("C02-----------------------------------------------------------------")
### Daten einlesen
f, Amplitude_k, Delta_t_k = np.genfromtxt("messdaten/B_C/B_C_kaestchen.txt", unpack=True) # f in 1/s, Rest in Kästchen

#print("Amplitude_k:", Amplitude_k)
#print("Delta_t_k:",Delta_t_k)
#print("f:", f)

n = len(f)

Amplitude = np.zeros(n)
Null_Amplitude = 3.1 * 0.5 # in Volt
print("Null_Amplitude:", Null_Amplitude)
Delta_t = np.zeros(n)
Delta_Phi = np.zeros(n)
T = 1/f *1000 # ms
print("T:")
for index, zeit in enumerate(T):
    print(index, zeit) #T in ms


for index, U in enumerate(Amplitude_k[:5]):
    Amplitude[index] = Amplitude_k[index] * 0.5

for index, U in enumerate(Amplitude_k[5:12]):
    Amplitude[index +5]  = Amplitude_k[index + 5] * 0.2

for index, U in enumerate(Amplitude_k[12:]):
    Amplitude[index + 12]  = Amplitude_k[index + 12] * 0.1 

print("Amplitude:")
for U in Amplitude:
    print(U) #A in Volt


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
    print(index, t) #Delta_t in ms


for index, t in enumerate(Delta_t):
    Delta_Phi[index] =  Delta_t[index]  / T[index]

print("Delta_Phi / 2 pi:")
for index, Phi in enumerate(Delta_Phi):
    print(Phi)

Delta_Phi_plot = Delta_Phi * 2 * np.pi

w_plot = f * 2 * np.pi


#### b) fit 

def A_omega(w, RC_2):
    return 1 / np.sqrt(1+ (w) ** 2 * RC_2 **2) #Variante möglich mit variabler Null_Amplitude 
                                            # -> liefert besseren Fit ist aber nicht so einfach zu erklären...

def A_omega_2(w, a, b):
    return np.exp(a * w + b)

A_plot = Amplitude / Null_Amplitude

RC_2_ergeb, cov_matrix_2 = curve_fit(A_omega, w_plot, A_plot)#, p0=(0.00281) ) #
abweichung_2 = np.sqrt(np.diag(cov_matrix_2))#
print("RC_2_ergeb:",RC_2_ergeb)
print("cov_matrix_2:", cov_matrix_2)
print("abweichung_2:", abweichung_2)

#### c) fit

def Phi_omega(w, RC_3):
    return np.arctan(-w * RC_3)

RC_3_ergeb, cov_matrix_3 = curve_fit(Phi_omega, f, Delta_Phi_plot, p0=(0.00281) )
print("RC_3_ergeb:",RC_3_ergeb)
print("cov_matrix_3:", cov_matrix_3)

### d) fit 

def A_Phi(w, Phi):
    return - np.sin(Phi)/(w* RC_2_ergeb)



x_plot= np.linspace(f[0], f[-1], 1000)
w_plot_plot= np.linspace(w_plot[0], w_plot[-1], 1000)
Phi_plot= np.linspace(Delta_Phi[0], Delta_Phi[-1], 1000)


### Die anderen drei Dateien übernehmen das plotten.