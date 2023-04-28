import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

# delta =  [0.6632251157578453+/-0.017453292519943295
#  0.6108652381980153+/-0.017453292519943295
#  0.6283185307179588+/-0.017453292519943295
#  0.7504915783575619+/-0.017453292519943295
#  0.9250245035569946+/-0.017453292519943295] rad =  
# [38.00000000000001+/-1.0 
# 35.0+/-1.0 
# 36.000000000000014+/-1.0
#  43.000000000000014+/-1.0 
# 53.0+/-1.0] deg

alpha_1, alpha_2 = np.genfromtxt("messung_4_gruen.txt", unpack = True)

einfall = np.deg2rad(alpha_1)
ausfall = unp.uarray(np.deg2rad(alpha_2), np.deg2rad(1) * np.ones(len(alpha_2)))

gamma = np.deg2rad(60)

index = 1.510

beta_1 = unp.arcsin(1/index * unp.sin(einfall))
beta_2 = gamma - beta_1 # wahrscheinlich nicht so fehleranfällig wegen messgenauigkeit
# beta_2 = unp.arcsin(1/index * unp.sin(ausfall))

delta_angle = (einfall + ausfall) - (beta_1 + beta_2)

print("delta = ", delta_angle, "rad = ", delta_angle/np.pi * 180, "deg")