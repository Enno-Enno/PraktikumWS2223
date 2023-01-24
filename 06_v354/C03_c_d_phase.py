import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C00_umrechnungen as c00
from uncertainties import ufloat

nu = 1 / c00.schwingdauer

#berechne phi:
phi = 2 * np.pi * c00.delta_t * nu
print("phi: ", phi)
# phi:  [0.         0.16319962 0.48332195 0.48332195 0.40536679 0.6981317
#  1.00530965 1.00530965 1.30899694 1.36590985 1.63909182 1.99919533
#  1.99919533 2.3935944  2.3935944  2.51327412 2.97624567 3.14159265
#  2.95679309 3.53429174 3.5903916  3.38325363 3.14159265 3.42719199]

for index, value in enumerate(phi):
    print(index, ": ", value)

# 0 :  0.0
# 1 :  0.16319961836830094
# 2 :  0.483321946706122
# 3 :  0.483321946706122
# 4 :  0.40536679401158615
# 5 :  0.6981317007977317
# 6 :  1.0053096491487337
# 7 :  1.0053096491487337
# 8 :  1.3089969389957472
# 9 :  1.3659098493868667
# 10 :  1.6390918192642399
# 11 :  1.9991953250116863
# 12 :  1.9991953250116863
# 13 :  2.39359440273508
# 14 :  2.39359440273508
# 15 :  2.5132741228718345
# 16 :  2.9762456718219097
# 17 :  3.141592653589793
# 18 :  2.9567930857315705
# 19 :  3.5342917352885173
# 20 :  3.5903916041026207
# 21 :  3.3832536269428535
# 22 :  3.1415926535897927
# 23 :  3.427191985734319

R2 = ufloat(509.5, 0.5) #ohm
C = 10**(-9) * ufloat(2.093, 0.003) #farad
L = 10**(-3) * ufloat(10.11, 0.03) #henry

x_res = 87
y_res = np.pi/2
y0 = -0.1
x1 = 76
x2 = 95
y1 = np.pi/4
y2 = 3* np.pi/4

nu_res_theo = 1/(2* np.pi) * (1/(L*C) - R2**2/(2 * L**2))**(1/2)
print("res_freq: ", nu_res_theo)
abweichung_res = (x_res * 10**3 - nu_res_theo) /nu_res_theo
print("abweichung res: ", abweichung_res)
#res_freq:  (3.413+/-0.006)e+04
#abweichung res:  1.549+/-0.004
#ohne vorfaktor vor wurzel: res_freq:  (2.1445+/-0.0035)e+05, abweichung res:  0.4057+/-0.0007 -> noch ungenauer (vgl. Bereich)
nu1 = 1/(2* np.pi) * (- R2/(2*L) + ((R2)**2 / (4 * L**2) + 1 / (L*C))**(1/2))
nu2 = 1/(2* np.pi) * (+ R2/(2*L) + ((R2)**2 / (4 * L**2) + 1 / (L*C))**(1/2))
delta_nu1 = (x1 * 10**3 - nu1)/nu1
delta_nu2 = (x2 * 10**3 - nu2)/nu2
print("nu1 = ", nu1)
print("nu2 = ", nu2)
#nu1 =  (3.082+/-0.005)e+04
#nu2 =  (3.884+/-0.007)e+04
print("delta nu 1: ", delta_nu1)
print("delta nu 2: ", delta_nu2)
#delta nu 1:  1.466+/-0.004
#delta nu 2:  1.446+/-0.004


plt.figure(constrained_layout=True)
plt.plot(nu[1:]/1000, np.log(phi[1:]), "x", label="Messdaten")
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\ln{\\left(\\phi\\right)}$")
plt.savefig("build/C03_c_d_phase.pdf")


plt.figure(constrained_layout=True)
plt.plot(nu[:17]/1000, phi[:17], "x", label="Messdaten")
plt.vlines(x_res, y0, y_res, color="r", linestyles ="dotted", label="$\\nu_\\text{res}$")
plt.vlines(x1, y0, y1, color="g", linestyles ="dotted", label="$\\nu_1$ bzw. $\\nu_2$")
plt.vlines(x2, y0, y2, color="g", linestyles ="dotted") #, label="$\\nu_1$ bzw. $\\nu_2$")
plt.ylim(y0, np.pi)
plt.yticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], ["0", "$\\pi / 4$", "$\\pi / 2$", "$3 \\pi / 4$", "$\\pi$"])
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\phi$")
plt.savefig("build/C03_c_d_phase_linear.pdf")