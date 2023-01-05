import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



print("C01-----------------------------------------------------------------")
U_k, t_k = np. genfromtxt("messdaten/A/a_in_kaestchen.txt", unpack=True)

U = U_k * 0.2 # U in Volt
t = t_k * 2  # t in ms

for index,  zeit in enumerate(t):
    print(zeit, U[index])

#U_ln = np.log(abs(U))

#def U_fit(t, U_0, U_inf, RC):
#    return U_0 * np.exp(-t/ RC) + U_inf


U_inf = 3.81 * 0.2 
params, cov_matrix = np.polyfit(t , np.log(U + U_inf),deg=1, cov=True)
U_pos = np.log(U + U_inf)
abweichung = np.sqrt(np.diag(cov_matrix))


print("params", params)
print("cov_matrix:", cov_matrix)
print("abweichung:", abweichung)

print("Hier entsteht Plot 1")
fig, (ax1,ax2) = plt.subplots(2,1,constrained_layout=True, sharex=True)

x_plot = np.linspace(0, 10)
ax1.plot(t, U + U_inf,'x', label="U(t)")
#ax1.plot(x_plot, U_fit(x_plot, *params ))
#ax1.set_yscale("log")
ax1.set_xlabel("$t / \\unit{{\\milli\\s}}$")
ax1.set_ylabel("$U / \\unit{{\\volt}}$")

ax1.grid()

ax2.plot(t, U_pos, 'x')
ax2.plot(x_plot, params[0]*x_plot+ params[1])
ax2.set_xlabel("$t / \\unit{{\\milli\\s}}$")
ax2.set_ylabel("$\ln\\left(U / U\\left(\\infty \\right)\\right)$")
ax2.grid()

plt.savefig("build/C01_aufg_a.pdf")