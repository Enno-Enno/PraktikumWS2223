import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C01_aufg_a as C01

print("Hier entsteht Plot 1")
fig, (ax1,ax2) = plt.subplots(2,1,constrained_layout=True, sharex=True)

x_plot = np.linspace(0, 10)
ax1.plot(C01.t, C01.U + C01.U_inf,'x', label="U(t)") # t in ms
#ax1.plot(x_plot, U_fit(x_plot, *params ))
#ax1.set_yscale("log")
ax1.set_xlabel("$t / \\unit{{\\milli\\s}}$")
ax1.set_ylabel("$ \\left(  U - U \\left(\\infty \\right) \\right)/ \\unit{{\\volt}}$")

ax1.grid()



ax2.plot(C01.t, C01.U_pos, 'x')
ax2.plot(x_plot, C01.params[0]*x_plot+ C01.params[1], label="lineare Regression")
ax2.set_xlabel("$t / \\unit{{\\milli\\s}}$")
ax2.set_ylabel("$\ln\\left(U / U\\left(\\infty \\right)\\right)$")
ax2.grid()
fig.legend()

plt.savefig("build/C01_aufg_a.pdf")