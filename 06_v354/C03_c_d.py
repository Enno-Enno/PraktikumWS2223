import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C00_umrechnungen as c00
from uncertainties import ufloat

u_generator = 1.7 * 0.5 #volt
u_quot = c00.spannung/u_generator

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
omega_0 = 87 * 10**3
q_theo = 1/(omega_0 * C* R2)
print("q_theo: ", q_theo)
#q_theo:  10.779+/-0.019
q_abweichung = 1.9/q_theo
print("q_abweichung: ", q_abweichung)
# q_abweichung:  0.17627+/-0.00031

plt.figure(constrained_layout=True)
plt.plot(nu/1000, np.log(u_quot), "x", label="Messdaten")
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\ln{\\left(\\frac{U_C}{U}\\right)}$")
plt.savefig("build/C03_c_d.pdf")

plt.figure(constrained_layout=True)
plt.plot(nu/1000, u_quot, "x", label="Messdaten")
plt.axhline(y = 1.9/(2**(1/2)), label="$\\frac{U_C}{\\sqrt{2} U}$")
plt.grid()
plt.legend()
plt.show()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\frac{U_C}{U}$")
plt.savefig("build/C03_c_d_linear.pdf")