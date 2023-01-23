import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C00_umrechnungen as c00
from uncertainties import ufloat

u_generator = 1.7 * 0.5 #volt
u_quot = c00.spannung/u_generator

print("U_0: ", u_generator)
#U_0:  0.85

nu = 1 / c00.schwingdauer
print("nu: ",nu)
# nu:  [ 13333.33333333  25974.02597403  38461.53846154  51282.05128205
#   64516.12903226  74074.07407407  80000.          80000.
#   83333.33333333  86956.52173913  86956.52173913  90909.09090909
#   90909.09090909  95238.0952381   95238.0952381  100000.
#  105263.15789474 111111.11111111 117647.05882353 125000.
#  142857.14285714 153846.15384615 166666.66666667 181818.18181818]

R2 = ufloat(509.5, 0.5) #ohm
C = 10**(-9) * ufloat(2.093, 0.003) #farad
L = 10**(-3) * ufloat(10.11, 0.03) #henry
omega_0 = 1/(2 * np.pi) * 87 * 10**3
q_theo = 1/R2 * (L/C)**(1/2) #1/(omega_0 * C* R2)
print("q_theo: ", q_theo)
#q_theo: 4.314+/-0.008
q_abweichung = (1.88-q_theo)/q_theo
print("q_abweichung: ", q_abweichung)
#q_abweichung:  -0.5642+/-0.0008

x1 = (74+80)/2
x2 = 95
y0 = 0.2
y_wurzel = 1.9/(2**(1/2))

delta_nu = x2-x1 #kilo hertz
print("delta nu: ", delta_nu)
#delta nu:  18.0 kHz
delta_omega = 2 * np.pi * delta_nu 
print("delta_omega: ", delta_omega)
# delta_omega:  113.09733552923255 kHz
 
delta_omega_theo = R2/L
print("delta_omega_theo: ", delta_omega_theo)
#delta_omega_theo:  (5.040+/-0.016)e+04 Hz
delta_nu_theo = 1/(2 * np.pi) * delta_omega_theo
print("delta nu theo: ", delta_nu_theo)
#delta nu theo:  8021+/-25 Hz

quotient_omega = delta_omega / delta_omega_theo
quotient_nu = delta_nu / delta_nu_theo

# print(quotient_omega, quotient_nu)

abweichung_omega = (delta_omega * 10**3 -delta_omega_theo)/delta_omega_theo
print("abweichung omega: ", abweichung_omega)
#abweichung omega:  1.244+/-0.007
abweichung_nu = (delta_nu * 10**3 - delta_nu_theo)/delta_nu_theo
print("abweichung nu: ", abweichung_nu)
# abweichung nu:  1.244+/-0.007

plt.figure(constrained_layout=True)
plt.plot(nu/1000, np.log(u_quot), "x", label="Messdaten")
plt.hlines(0.63, 10, 87, color="r", linestyles ="dotted", label="$\\ln{(q)}$")
plt.xlim(10,170)
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\ln{\\left(\\frac{U_C}{U_0}\\right)}$")
plt.savefig("build/C03_c_d.pdf")


plt.figure(constrained_layout=True)
plt.plot(nu/1000, u_quot, "x", label="Messdaten")
#plt.axhline(y = 1.9/(2**(1/2)), label="$\\frac{U_C}{\\sqrt{2} U}$")
plt.hlines(y_wurzel, x1, x2, color="r", linestyles ="dotted", label="$\\frac{U_C}{\\sqrt{2} U_0}$")
plt.vlines(x1, y0, y_wurzel, color="g", linestyles ="dotted") #, label = "$\\nu_-$")
plt.vlines(x2, y0, y_wurzel, color="g", linestyles ="dotted") #, label = "$\\nu_-$")
#test weiter:
#plt.hlines(*results_wurzel[1:])
plt.xlim(73, 101)
plt.ylim(y0, 2.2)
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\frac{U_C}{U}$")
plt.savefig("build/C03_c_d_linear.pdf")