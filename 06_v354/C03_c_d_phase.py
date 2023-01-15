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

#x1 = (74+80)/2
#x2 = 95
#y0 = 0.2
#y_wurzel = 1.9/(2**(1/2))

#delta_nu = x2-x1 #kilo hertz
#print("delta nu: ", delta_nu)
##delta nu:  18.0 kHz
#delta_nu_theo = R2/L
#print("delta nu theo: ", delta_nu_theo)
#abweichung_nu = delta_nu * 10**3/delta_nu_theo
#print("abweichung nu: ", abweichung_nu)

plt.figure(constrained_layout=True)
plt.plot(nu[1:]/1000, np.log(phi[1:]), "x", label="Messdaten")
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\ln{\\left(\\phi\\right)}$")
plt.savefig("build/C03_c_d_phase.pdf")


plt.figure(constrained_layout=True)
plt.plot(nu[:17]/1000, phi[:17], "x", label="Messdaten")
#plt.axhline(y = 1.9/(2**(1/2)), label="$\\frac{U_C}{\\sqrt{2} U}$")
#plt.hlines(y_wurzel, x1, x2, color="r", linestyles ="dotted", label="$\\frac{U_C}{\\sqrt{2} U}$")
#plt.vlines(x1, y0, y_wurzel, color="g", linestyles ="dotted")
#plt.vlines(x2, y0, y_wurzel, color="g", linestyles ="dotted")
#test weiter:
#plt.hlines(*results_wurzel[1:])
#plt.xlim(73, 101)
#plt.ylim(y0, 2.2)
plt.yticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], ["0", "$\\pi / 4$", "$\\pi / 2$", "$3 \\pi / 4$", "$\\pi$"])
plt.grid()
plt.legend()
plt.xlabel("$\\nu / \\unit{{\\kilo\\hertz}}$")
plt.ylabel("$\\phi$")
plt.savefig("build/C03_c_d_phase_linear.pdf")