import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C02_aufg_b_c as C02

print("Hier entsteht Plot 3")
plt.figure(constrained_layout=True)
plt.plot(C02.f, C02.Delta_Phi_plot, "x", label="Gemessene Werte")

plt.plot(C02.x_plot, C02.Phi_omega(C02.x_plot, *C02.RC_3_ergeb), label="Ausgleichskurve")
# plt.plot(C02.x_plot,C02.Phi_omega(C02.x_plot, 0.007, 0.6 ))

plt.xlabel("$f / \\unit{{\\hertz}}$")
plt.ylabel("$\\Phi / \\unit{{rad}}$")
plt.grid()
plt.legend()


plt.savefig("build/C02_aufg_c.pdf")