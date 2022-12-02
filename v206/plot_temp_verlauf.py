import numpy as np
import matplotlib.pyplot as plt

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

plt.plot(t, temp_k, ".", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, ".", label="$T_{{\\text{w}}}$")
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\celsius}}$")
plt.savefig("build/plot_temp_verlauf.pdf")