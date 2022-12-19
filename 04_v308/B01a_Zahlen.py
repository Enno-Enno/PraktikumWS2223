import numpy as np
import matplotlib.pyplot as plt
print("B01-----------------------------------------------------------------------------")
strom_0, magnetfeld_0 = np.genfromtxt("messdaten/Hysterese_kurve/0_neukurve.txt", unpack=True)
strom_A, magnetfeld_A = np.genfromtxt("messdaten/Hysterese_kurve/A_zurück.txt", unpack=True)
strom_B, magnetfeld_B = np.genfromtxt("messdaten/Hysterese_kurve/B_negativ.txt", unpack=True)
strom_C, magnetfeld_C = np.genfromtxt("messdaten/Hysterese_kurve/C_zurück.txt", unpack=True)
strom_D, magnetfeld_D = np.genfromtxt("messdaten/Hysterese_kurve/D_wieder_hoch.txt", unpack=True)


strom = np.concatenate((strom_0,strom_A,strom_B,strom_C,strom_D)) # Ampere
magnetfeld = np.concatenate((magnetfeld_0,magnetfeld_A,magnetfeld_B,magnetfeld_C,magnetfeld_D)) # milli Tesla

n = 595
r_t = 0.135  #m
mu_0 = 4 * np.pi * 10 ** (-7)  # Newton /Ampere^2
#    
H =  n / ( 2 * np.pi * r_t * mu_0) * strom * 10 ** 3 # milli A/m
moment = (magnetfeld / mu_0) - H #milli

for index, I in enumerate(strom):
    print(I, magnetfeld[index])