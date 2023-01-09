import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C02_aufg_b_c as C02
import C01_aufg_a as C01


print("Hier entsteht Plot 2")
#

plt.figure(constrained_layout=True)
plt.plot(C02.f, C02.A_plot, "x", label="gemessene Werte" )
plt.plot(C02.x_plot, C02.A_omega(C02.x_plot, *C02.RC_2_ergeb), label="Ausgleichskurve")
plt.plot(C02.x_plot, 0.4 * C02.A_omega(C02.x_plot, *C02.RC_2_ergeb), label="$\\text{{Ausgleichskurve}} \\cdot \\num{0.4}$ ")
#plt.plot(C02.x_plot, C02.A_omega(C02.x_plot, C01.tau), label="A(\omega) mit \\tau aus a)")
 
plt.xscale('log')
plt.xlabel("$ f / \\unit{{\\hertz}}$")
plt.ylabel("$U(\\omega)/ U_0$")
plt.grid()
plt.legend()


plt.savefig("build/C02_aufg_b.pdf")