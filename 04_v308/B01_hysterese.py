import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
print("B01-----------------------------------------------------------------------------")
strom_0, magnetfeld_0 = np.genfromtxt("messdaten/Hysterese_kurve/0_neukurve.txt", unpack=True)
strom_A, magnetfeld_A = np.genfromtxt("messdaten/Hysterese_kurve/A_zurück.txt", unpack=True)
strom_B, magnetfeld_B = np.genfromtxt("messdaten/Hysterese_kurve/B_negativ.txt", unpack=True)
strom_C, magnetfeld_C = np.genfromtxt("messdaten/Hysterese_kurve/C_zurück.txt", unpack=True)
strom_D, magnetfeld_D = np.genfromtxt("messdaten/Hysterese_kurve/D_wieder_hoch.txt", unpack=True)


strom_ab = np.concatenate((strom_A, strom_B))
strom_auf = np.concatenate((strom_C, strom_D))
magnetfeld_ab = np.concatenate((magnetfeld_A, magnetfeld_B))
magnetfeld_auf = np.concatenate((magnetfeld_C, magnetfeld_D))

def f(t, a, b, c, d, e, f ):
    return a * t**5 +b * t**4 +c * t ** 3 + d * t **2 + e * t + f 

params_0,   covariance_matrix_0   = np.polyfit(strom_0, magnetfeld_0, deg=5, cov=True)
params_auf, covariance_matrix_auf = np.polyfit(strom_auf, magnetfeld_auf, deg=5, cov=True)
params_ab,  covariance_matrix_ab  = np.polyfit(strom_ab, magnetfeld_ab, deg=5, cov=True)
print("params_0:",  params_0  )
#print("params_auf:",params_auf)
#print("params_ab:", params_ab )
print("Fehler_0   =",np.sqrt(np.diag(covariance_matrix_0))  )
#print("Fehler_auf =",np.sqrt(np.diag(covariance_matrix_auf))  )
#print("Fehler_ab  =",np.sqrt(np.diag(covariance_matrix_ab))  )

x_plot= np.linspace(strom_auf[0],strom_auf[-1])
x_plot_0= np.linspace(0,10)


plt.figure(constrained_layout=True)
plt.plot(x_plot_0,f(x_plot_0, *params_0), label="Fit Neukurve")
#plt.plot(x_plot,f(x_plot, *params_auf))
#plt.plot(x_plot,f(x_plot, *params_ab))
plt.plot(strom_0, magnetfeld_0, "x", label="Werte Neukurve")
plt.plot(strom_ab, magnetfeld_ab, "x", label="Werte absteigend")
plt.plot(strom_auf, magnetfeld_auf, "x", label="Werte aufsteigend")
plt.grid()
plt.legend()


plt.savefig("build/B01_Hysteresekurve.pdf")