import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

print("B02------------------------------------------------------------------")

phi, amp_ch1, av_ch2 = np.genfromtxt("B02_messdaten.txt", unpack=True)
#amp_ch1 und av_ch2 sind schon in V

def cosinus(x, a, b, c, d):
    return(a * np.cos(b*x + c) +d)

phi_rad = phi/360 * 2 * np.pi
#umwandlung von deg in rad


#params_ch1, covariance_matrix_ch1 = curve_fit(cosinus, phi_rad, amp_ch1)
params_ch2, covariance_matrix_ch2 = curve_fit(cosinus, phi_rad, av_ch2, p0=(1, 1, 1, 100))

#print("cosinus für amp_ch1: ")
#for name, value in zip("abcd", params_ch1):
#    print(f"{name} = {value:8.8f}")
#cosinus für amp_ch1: 
#a = 0.33217717
#b = 0.81383641
#c = 1.40574449
#d = 1.06428022

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
#plt.savefig("build/B01_ausgleichsplot_channel1_mit_noise.pdf")

# ### DER PLOT IST NACH UNTEN GEWANDERT. 

#cosinus für av_ch2:
#a = -0.27466768  
#b = 0.99333910  
#c = -0.27544268  
#d = 0.08103079  
#fehler:
#[0.00545352 
# 0.01503098 
# 0.05641517 
# 0.00536591]

param_a = ufloat(-0.27466768, 0.00545352)
param_b = ufloat(0.99333910 , 0.01503098)
param_c = ufloat(-0.27544268, 0.05641517)
param_d = ufloat(0.08103079 , 0.00536591)

u_0 = ufloat(0.0100, 0.0000) #geht auch ohne ufloat aber testweise
gain = 5 * 20
u_0_noise = np.pi/2 * param_a / gain
print("U_0_noise = ", u_0_noise)
del_u_noise_abs =   u_0 -  abs(u_0_noise)
print("del_u_noise_abs =", del_u_noise_abs)
del_u_noise = del_u_noise_abs / abs(u_0_noise)
print("delta u_noise prct= ", del_u_noise)
u_0_exp = ufloat(-0.0157, 0.0004) # ???
prct_aweichung_U_0 = (del_u_noise_abs/u_0) 
print("prct_aweichung_U_0=", prct_aweichung_U_0)
# abweichung_out_noise = u_0_exp / u_0_noise
#print("abweichung out noise : ", abweichung_out_noise)
print("-------------------------------------------------------")
#CH1 ERGIBT KEINEN SINN --> CH2 VERWENDEN

#U_0_noise =  -0.00431+/-0.00009
#delta u_noise =  0.431+/-0.009


plt.figure(constrained_layout=True)
plt.plot(phi_rad, av_ch2, "x", label="$U_\\text{noise}$")
plt.plot(x, cosinus(x, *params_ch2), "-", label="Ausgleichsfunktion")
plt.grid()
plt.xlim(0, 2 * np.pi)
plt.xlabel("$\\phi / \\unit{{\\radian}}$")
plt.ylabel("$U / \\unit{{\\volt}}$")
#plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["0", "$\\frac{1}{2}\\pi$", "$\\pi$", "$\\frac{3}{2}\\pi$", "$2 \\pi$"])
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["0", "$\\pi / 2$", "$\\pi$", "$3 \\pi / 2$", "$2 \\pi$"])
plt.legend()
plt.savefig("build/B02_ausgleichsplot.pdf")
#abweichung out noise :  3.64+/-0.12