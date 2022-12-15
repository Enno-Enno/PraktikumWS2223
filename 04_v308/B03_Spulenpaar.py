import numpy as np
import matplotlib.pyplot as plt

print("B03-----------------------------------------------------------------")
x_6, magnetfeld_6 = np.genfromtxt("messdaten/Spulenpaar/6cm.txt", unpack=True)
x_12, magnetfeld_12 = np.genfromtxt("messdaten/Spulenpaar/12cm.txt", unpack=True)
x_24, magnetfeld_24 = np.genfromtxt("messdaten/Spulenpaar/24cm.txt", unpack=True)
print(magnetfeld_12)

plt.figure(constrained_layout=True)
print("x_6:", x_6)

plt.subplot(2,1,1)
plt.plot(x_6[:4], magnetfeld_6[:4], 'x', label="Magnetfeld innerhalb der Spulen")
plt.grid()
plt.xlabel("$x/ \\unit{{cm}}$")
plt.ylabel("B/ \\unit{{\\milli\\tesla}}")

plt.subplot(2,1,2)
plt.plot(x_6[4:], magnetfeld_6[4:], 'x', label="Magnetfeld außerhalb der Spulen")
plt.grid()

plt.xlabel("$x/ \\unit{{cm}}$")
plt.ylabel("B/ \\unit{{\\milli\\tesla}}")

plt.savefig("build/B03_6_Spulenpaar.pdf")

plt.figure(constrained_layout=True)
print("x_12", x_12)

plt.subplot(2,1,1)
plt.grid()
plt.plot(x_12[7:], magnetfeld_12[7:], 'x', label="Magnetfeld innerhalb der Spulen")

plt.xlabel("$x/ \\unit{{cm}}$")
plt.ylabel("B/ \\unit{{\\milli\\tesla}}")

plt.subplot(2,1,2)
plt.grid()
plt.plot(x_12[:7], magnetfeld_12[:7], 'x', label="Magnetfeld außerhalb der Spulen")
plt.legend()

plt.xlabel("$x/ \\unit{{cm}}$")
plt.ylabel("B/ \\unit{{\\milli\\tesla}}")


plt.savefig("build/B03_12_Spulenpaar.pdf")

plt.figure(constrained_layout=True)
print("x_24:", x_24)
plt.subplot(2,1,1)
plt.plot(x_24[:13], magnetfeld_24[:13], 'x', label="Magnetfeld innerhalb der Spulen")
plt.grid()

plt.xlabel("$x/ \\unit{{cm}}$")
plt.ylabel("B/ \\unit{{\\milli\\tesla}}")

plt.subplot(2,1,2)
plt.plot(x_24[13:], magnetfeld_24[13:], 'x', label="Magnetfeld außerhalb der Spulen")
plt.grid()

plt.xlabel("$x/ \\unit{{cm}}$")
plt.ylabel("B/ \\unit{{\\milli\\tesla}}")

plt.savefig("build/B03_24_Spulenpaar.pdf")