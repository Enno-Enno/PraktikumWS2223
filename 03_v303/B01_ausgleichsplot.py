import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

print("B01------------------------------------------------------------------")
phi, amp_ch1, av_ch2 = np.genfromtxt("B01_messdaten.txt", unpack=True)
gain = 1 * 20

def cosinus(x, a, b, c, d):
    return(a * np.cos(b*x + c) +d)

phi_rad = phi/360 * 2 * np.pi
#umwandlung von deg in rad

amp_ch1 /= 1000
av_ch2 /= 1000
#Umwandlung mV in V

print("phi in rad:")
print(phi_rad)

params_ch1, covariance_matrix_ch1 = curve_fit(cosinus, phi_rad, amp_ch1)
params_ch2, covariance_matrix_ch2 = curve_fit(cosinus, phi_rad, av_ch2, p0=(1, 1, 1, 100))

#print("cosinus für amp_ch1: ")
#for name, value in zip("abcd", params_ch1):
#    print(f"{name} = {value:8.8f}")
#cosinus für amp_ch1:
#a = 0.28351930
#b = 0.97349138
#c = 1.12537889
#d = 0.81485474

print("cosinus für av_ch2: ")
for name, value in zip("abcd", params_ch2):
    print(f"{name} = {value:8.8f}")

error = np.sqrt(np.diag(covariance_matrix_ch2))
print("fehler:")
print(error)

x = np.linspace(0,2*np.pi,1000)

#plt.figure(constrained_layout=True)
#plt.plot(phi_rad, amp_ch1, "x", label="Amplitude $A$")
#plt.plot(x, cosinus(x, *params_ch1), "-", label="Ausgleichsfunktion")
#plt.xlim(0, 2 * np.pi)
#plt.xlabel("$\\phi / \\unit{{\\radian}}$")
#plt.ylabel("$U / \\unit{{\\volt}}$")
#plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["0", "$\\pi / 2$", "$\\pi$", "$3 \\pi / 2$", "$2 \\pi$"])
#plt.legend()
#plt.savefig("build/B01_ausgleichsplot_channel1.pdf")

plt.figure(constrained_layout=True)
plt.plot(phi_rad, av_ch2, "x", label="$U_\\text{out}$")
plt.plot(x, cosinus(x, *params_ch2), "-", label="Ausgleichsfunktion")
plt.xlim(0, 2 * np.pi)
plt.xlabel("$\\phi / \\unit{{\\radian}}$")
plt.ylabel("$U / \\unit{{\\volt}}$")
#plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["0", "$\\frac{1}{2}\\pi$", "$\\pi$", "$\\frac{3}{2}\\pi$", "$2 \\pi$"])
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["0", "$\\pi / 2$", "$\\pi$", "$3 \\pi / 2$", "$2 \\pi$"])
plt.legend()
plt.savefig("build/B01_ausgleichsplot.pdf")

# cosinus für av_ch2:
# a = -0.20018493
# b =  0.99376117
# c = -0.27683892
# d =  0.08687120
#fehler:
#[0.00549263
# 0.02075618 
# 0.07790146 
# 0.0054004 ]

param_a = ufloat(-0.20018493, 0.00549263)
param_b = ufloat( 0.99376117, 0.02075618)
param_c = ufloat(-0.27683892, 0.07790146)
param_d = ufloat( 0.08687120, 0.0054004 )

u_0 = np.pi/2 * param_a /gain
print("U_0 = ", u_0)
#U_0 =  -0.0157+/-0.0004
print("-------------------------------------------------------")
#CH1 ERGIBT KEINEN SINN --> CH2 VERWENDEN