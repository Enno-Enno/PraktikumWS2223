import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C02_aufg_b_c as C02


print("Hier entsteht Plot 2")


plt.figure(constrained_layout=True)
plt.plot(C02.f, C02.A_plot, "x")
plt.plot(C02.x_plot, C02.A_omega(C02.x_plot, *C02.RC_2_ergeb))

plt.yscale('log')
plt.xlabel("$\\omega / \\unit{{\\hertz}}$")
plt.ylabel("$A(\\omega)/ U_0$")

plt.savefig("build/C02_aufg_b.pdf")

