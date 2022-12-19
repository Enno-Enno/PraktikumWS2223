import numpy as np
import matplotlib.pyplot as plt
print("B01-----------------------------------------------------------------------------")
strom_0, magnetfeld_0 = np.genfromtxt("messdaten/Hysterese_kurve/0_neukurve.txt", unpack=True) #milli Tesla
strom_A, magnetfeld_A = np.genfromtxt("messdaten/Hysterese_kurve/A_zurück.txt", unpack=True)
strom_B, magnetfeld_B = np.genfromtxt("messdaten/Hysterese_kurve/B_negativ.txt", unpack=True)
strom_C, magnetfeld_C = np.genfromtxt("messdaten/Hysterese_kurve/C_zurück.txt", unpack=True)
strom_D, magnetfeld_D = np.genfromtxt("messdaten/Hysterese_kurve/D_wieder_hoch.txt", unpack=True)


strom_ab = np.concatenate((strom_A, strom_B))
strom_auf = np.concatenate((strom_C, strom_D))
magnetfeld_ab = np.concatenate((magnetfeld_A, magnetfeld_B))
magnetfeld_auf = np.concatenate((magnetfeld_C, magnetfeld_D))

strom = np.concatenate((strom_0,strom_A,strom_B,strom_C,strom_D)) # Ampere
magnetfeld = np.concatenate((magnetfeld_0,magnetfeld_A,magnetfeld_B,magnetfeld_C,magnetfeld_D)) # milli Tesla

n = 595
r_t = 0.135  #m
mu_0 = 4 * np.pi * 10 ** (-7)  # Newton /Ampere^2
#
def H(I):
    return  n / ( 2 * np.pi * r_t ) * I


#H =  n / ( 2 * np.pi * r_t ) * strom #  A/m
H_0 =  n / ( 2 * np.pi * r_t )  * strom_0  #  A/m
B_0 = mu_0 * H_0
H_ab =  n / ( 2 * np.pi * r_t ) * strom_ab  #  A/m
H_auf =  n / ( 2 * np.pi * r_t ) * strom_auf  # A/m
#moment = (magnetfeld / mu_0) - H #milli

rel_B = np.array([142,16,117,21])
mw_rel_B = np.mean(rel_B)
std_rel_B = np.std(rel_B)
print("mw_rel_B:",mw_rel_B)
print("std_rel_B:",std_rel_B)

rel_I = np.array([0,0.5,0.5,1])
mw_rel_I = np.mean(rel_I)
std_rel_I = np.std(rel_I)
print("mw_rel_H:", H(mw_rel_I))
print("std_rel_I:",H(std_rel_I))
