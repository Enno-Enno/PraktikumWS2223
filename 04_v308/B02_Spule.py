import numpy as np
import matplotlib.pyplot as plt
print("B02-----------------------------------------------------------------------------")
x_l_abs, magnetfeld_l = np.genfromtxt("messdaten/Spule/lange_spule.txt", unpack=True)
x_k_abs, magnetfeld_k = np.genfromtxt("messdaten/Spule/kurze_spule.txt", unpack=True)

x_l = x_l_abs - 50 + 8
x_k = x_k_abs - 50 + 4.5

plt.figure(constrained_layout=True)
plt.plot(x_l, magnetfeld_l, 'x')
plt.savefig("build/B02_lange_spule.pdf")
plt.figure(constrained_layout=True)
plt.plot(x_k, magnetfeld_k, 'x')
plt.savefig("build/B02_kurze_spule.pdf")