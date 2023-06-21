import numpy as np
import matplotlib.pyplot as plt

f, u = np.genfromtxt("teil1.txt", unpack = True)

plt.plot(f, u, "x", label = "Messwerte")
plt.grid()
plt.xlabel("f/kHz")
plt.ylabel("U/V")
plt.title("Teil 1: Selektivverstärker")
plt.legend()
plt.savefig("Teil1.pdf")