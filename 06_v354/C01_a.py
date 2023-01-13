import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C00_umrechnungen as c00
from uncertainties import ufloat


def einhuellende(t, a_0, mu):
    return(a_0 * np.exp(-2 * np.pi * mu * t))

params, covariance_matrix = curve_fit(einhuellende, c00.time, c00.amplitude, p0=(2.8, 10))

print("Einhüllende Parameter:")
for name, value in zip('am', params):
    print(f"{name} = {value:8.8f}")
errors = np.sqrt(np.diag(covariance_matrix))
print("Fehler:", errors)
#Einhüllende Parameter:
#a = 2.74616696 volt
#m = 1808.51036554 pro sekunde
#Fehler: [4.88081460e-02 5.55975139e+01]

mu = ufloat(params[1], errors[1]) #in 1/s
L = 10**(-3) * ufloat(10.11, 0.03) #in H
R_eff = 4 * np.pi * mu * L # in 1/s * H = ohm
print("effektiver Widerstand R = ", R_eff)
T_eff = 1/ (2* np.pi * mu) # in s
print("effektive Abklingdauer T = ", T_eff)

# R_test =2 * L / T_eff
# print("Test R: ", R_test) -> entspricht R_eff

#effektiver Widerstand R =  230+/-7 ohm
#effektive Abklingdauer T =  (8.80+/-0.27)e-05 s
R1 = ufloat(48.1, 0.1)
delta_R = R_eff/R1
print("Abweichung R = ", delta_R)

x_ms = np.linspace(c00.time_micro[0], c00.time_micro[13])
x_sec = np.linspace(c00.time[0], c00.time[13]) #--> zum einsetzen in einhüllende

y_eff = einhuellende(8.80e-05, *params)

plt.figure(constrained_layout=True)
plt.plot(c00.time_micro, c00.amplitude,"x", label="Amplitude $A$")
plt.plot(x_ms, einhuellende(x_sec, *params), "-", label = "Ausgleichsrechnung für $A$")
plt.plot(einhuellende(8.80e-05, *params), "-")
plt.grid()
plt.legend()
plt.xlabel("$t / \\mu \\unit{{\\second}}$")
plt.ylabel("$A/ \\unit{{\\volt}}$")
plt.savefig("build/C01_a.pdf")
