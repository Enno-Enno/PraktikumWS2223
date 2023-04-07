import numpy as np
# import matplotlib.pyplot as plt
from uncertainties import ufloat
import scipy.constants as const

Temp_C = np.genfromtxt("C01_Temperaturen_und_so.txt")
Temp_K = Temp_C + 273 
p_set = 5.5 * 10 ** (7) * np.exp(-6876/Temp_K)
w_marked = 0.0029 / p_set 

print("Dampfdruck und so ----------------------")
for i, val in enumerate(Temp_C):
    print(Temp_C[i] , "&", Temp_K[i], "&", p_set[i], "&", w_marked[i] )

K = 10 - (8+2*23/49)

print(8+2*23/49)
print("Frack-Hertz-Auswertung -------------------")
C_Dist = np.genfromtxt("Franck_C.txt", unpack=True)
C_Skala = [36,38,35,37,37,37]
C_skala_mean = np.mean(C_Skala)
C_skala_stddev = np.std(C_Skala)
C_dist_mean = np.mean(C_Dist)
C_dist_stddev = np.std(C_Dist)

print("C_skala_mean",C_skala_mean)
print("C_skala_stddev",C_skala_stddev)
print("C_dist_mean",C_dist_mean)
print("C_dist_stddev",C_dist_stddev)

C_u_skala = ufloat(C_skala_mean,C_skala_stddev)
C_u_dist = ufloat(C_dist_mean,C_dist_stddev)
C_u_dist_real = (C_u_dist / C_u_skala) * 5 # in Volt

print("C_u_skala",C_u_skala)
print("C_u_dist",C_u_dist)
print("C_u_dist_real",C_u_dist_real)

print("Messung D ----------------")

D_Dist = np.genfromtxt("Franck_D.txt", unpack=True)
D_Skala = [19,23,21,20,18,21,20]
D_skala_mean = np.mean(D_Skala)
D_skala_stddev = np.std(D_Skala)
D_dist_mean = np.mean(D_Dist)
D_dist_stddev = np.std(D_Dist)

print("D_skala_mean",D_skala_mean)
print("D_skala_stddev",D_skala_stddev)
print("D_dist_mean",D_dist_mean)
print("D_dist_stddev",D_dist_stddev)

D_u_skala = ufloat(D_skala_mean,D_skala_stddev)
D_u_dist = ufloat(D_dist_mean,D_dist_stddev)
D_u_dist_real = (D_u_dist / D_u_skala) * 5 # in Volt

print("D_u_skala",D_u_skala)
print("D_u_dist",D_u_dist)
print("D_u_dist_real",D_u_dist_real)
print()
print("Berechnung Wellenlänge")
print("h", const.h)
print("c", const.c)

C_lambda = const.h * const.c / C_u_dist_real
D_lambda = const.h * const.c / D_u_dist_real

print("C_lambda", C_lambda)
print("D_lambda", D_lambda)