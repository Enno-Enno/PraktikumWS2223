import numpy as np
import matplotlib.pyplot as plt

#Daten sammeln
theta_2, R_Impulse_s =  np.genfromtxt("v602_messungen/detail.txt", unpack=True)
theta = theta_2 / 2

for index, shit in enumerate(theta):
    print(f"{theta[index]} \t& {R_Impulse_s[index]} \\\\")



#Plot
plt.figure(constrained_layout=True)
plt.plot(theta, R_Impulse_s, "x")
#Beschriftungen
plt.xlabel("$\\theta / \\unit{{\degree}}$")
plt.ylabel("$N / \\frac{{1}}{{5\\unit{{\\s}}}}$")

plt.savefig("build/03_plot.pdf")
