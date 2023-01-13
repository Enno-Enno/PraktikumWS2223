import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

L = 10**(-3) * ufloat(10.11, 0.03)
C = 10**(-9) * ufloat(2.093, 0.003)

R_ap_theo = 2* (L / C)**(1/2)
print("R_ap_theo = ", R_ap_theo)
# R_ap_theo =  4396+/-7

R_ap = 3.54 * 10**3

abweichung = R_ap/R_ap_theo
print("abweichung = ", abweichung)
#abweichung =  0.8053+/-0.0013