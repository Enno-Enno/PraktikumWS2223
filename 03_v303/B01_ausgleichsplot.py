import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

phi, amp_ch1, av_ch2 = np.genfromtxt("B01_messdaten.txt", unpack=True)

def cosinus(x, a, b, c, d):
    return(a * np.cos(b*x + c) +d)

phi_rad = phi/360 * 2 * np.pi
#umwandlung von deg in rad

av_ch2 /= 1000
#mV in V

print("phi in rad:")
print(phi_rad)

#params_ch1, covariance_matrix_ch1 = curve_fit(cosinus, phi, amp_ch1)
params_ch2, covariance_matrix_ch2 = curve_fit(cosinus, phi_rad, av_ch2, p0=(1, 1, 1, 100))

#print("cosinus für amp_ch1: ")
#for name, value in zip("abcd", params_ch1):
#    print(f"{name} = {value:8.8f}")

print("cosinus für av_ch2: ")
for name, value in zip("abcd", params_ch2):
    print(f"{name} = {value:8.8f}")

x = np.linspace(0,2*np.pi,1000)

#plt.plot(phi, amp_ch1, "x", label="Amplitude, Ch1 huhuuuuuuuuuuuuuuuu")
#plt.plot(x, cosinus(x, *params_ch1), "-", label="cos")
#plt.legend()
#plt.savefig("build/B01_ausgleichsplot.pdf")

plt.plot(phi_rad, av_ch2, "x", label="Amplitude, Ch2")
plt.plot(x, cosinus(x, *params_ch2), "-", label="cos")
plt.legend()
plt.savefig("build/B01_ausgleichsplot.pdf")