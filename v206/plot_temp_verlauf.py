import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

plt.figure()
plt.plot(t, temp_k, "x", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, "x", label="$T_{{\\text{w}}}$")
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\celsius}}$")
#plt.title("Temperaturverlauf beider Reservoire")
plt.savefig("build/plot_temp_verlauf.pdf")
