import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

#beta_1 =  [0.6108045927738653 0.5320652808845506 0.4397211502484149
# 0.33749646246254644 0.29455288213066827] rad =  [
#    34.99652527314942 
#    30.485095020127428 
#    25.19416607187213 
#    19.337122899699327
#    16.876636989501694] deg
#beta_2 =  [0.4363929584227323 0.515132270312047 0.6074764009481828
# 0.7097010887340511 0.7526446690659294] rad =  [
#    25.00347472685057 
#    29.51490497987257 
#    34.805833928127875 
#    40.66287710030067
#    43.1233630104983] deg
#delta =  [0.6632251157578453+/-0.017453292519943295
# 0.6108652381980153+/-0.017453292519943295
# 0.6108652381980153+/-0.017453292519943295
# 0.7330382858376183+/-0.017453292519943295
# 0.8901179185171082+/-0.017453292519943295] rad =  
# [38.00000000000001+/-1.0 
# 35.0+/-1.0 
# 35.0+/-1.0 
# 41.99999999999999+/-1.0
# 51.00000000000001+/-1.0] deg

alpha_1, alpha_2 = np.genfromtxt("messung_4_rot.txt", unpack = True)

einfall = np.deg2rad(alpha_1)
ausfall = unp.uarray(np.deg2rad(alpha_2), np.deg2rad(1) * np.ones(len(alpha_2)))

gamma = np.deg2rad(60)

index = 1.510

beta_1 = unp.arcsin(1/index * unp.sin(einfall))
beta_2 = gamma - beta_1 # wahrscheinlich nicht so fehleranfällig wegen messgenauigkeit
# beta_2 = unp.arcsin(1/index * unp.sin(ausfall))

delta_angle = (einfall + ausfall) - (beta_1 + beta_2)

print("beta_1 = ", beta_1, "rad = ", beta_1/np.pi * 180, "deg")
print("beta_2 = ", beta_2, "rad = ", beta_2/np.pi * 180, "deg")
print("delta = ", delta_angle, "rad = ", delta_angle/np.pi * 180, "deg")