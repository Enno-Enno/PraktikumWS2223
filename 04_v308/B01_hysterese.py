import numpy as np
import matplotlib.pyplot as plt
print("B01-----------------------------------------------------------------------------")
strom_0, magnetfeld_0 = np.genfromtxt("messdaten/Hysterese_kurve/0_neukurve.txt", unpack=True)
strom_A, magnetfeld_A = np.genfromtxt("messdaten/Hysterese_kurve/A_zurück.txt", unpack=True)
strom_B, magnetfeld_B = np.genfromtxt("messdaten/Hysterese_kurve/B_negativ.txt", unpack=True)
strom_C, magnetfeld_C = np.genfromtxt("messdaten/Hysterese_kurve/C_zurück.txt", unpack=True)
strom_D, magnetfeld_D = np.genfromtxt("messdaten/Hysterese_kurve/D_wieder_hoch.txt", unpack=True)


def f(a, S, k, t):
    return (a * S)/(a + (S - a) * np.exp(-S *k* t))

plt.figure(constrained_layout=True)
plt.plot(strom_0, magnetfeld_0, "x")
plt.plot(strom_A, magnetfeld_A, "x")
plt.plot(strom_B, magnetfeld_B, "x")
plt.plot(strom_C, magnetfeld_C, "x")
plt.plot(strom_D, magnetfeld_D, "x")
plt.grid()



plt.savefig("build/B01_Hysteresekurve.pdf")