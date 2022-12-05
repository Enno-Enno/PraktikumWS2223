import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

gew_zeiten = [3, 9, 15, 21]

#def function_3(t, a, b, c, alpha) :
#    return ((a*t**alpha)/(1 + b*t**alpha) + c)

def dif_quot(t, a, b, c, alpha) :
    return (alpha* a * t**(alpha-1)/(1 + b* t**(alpha))**2)
#in K/min

a_k = ufloat(-0.9113, 0.0742)
b_k = ufloat(0.0204, 0.0008)
c_k = ufloat(294.6660, 0.1221)
p_k = ufloat(1.1946, 0.0378)

a_w = ufloat(1.1391, 0.0429)
b_w = ufloat(0.0229, 0.0005)
c_w = ufloat(294.0467, 0.0704)
p_w = ufloat(1.2211, 0.0175)

#bestimmung differentialquotienten

dif_quot_k_0 = dif_quot(gew_zeiten[0], a_k, b_k, c_k, p_k)
dif_quot_k_1 = dif_quot(gew_zeiten[1], a_k, b_k, c_k, p_k)
dif_quot_k_2 = dif_quot(gew_zeiten[2], a_k, b_k, c_k, p_k)
dif_quot_k_3 = dif_quot(gew_zeiten[3], a_k, b_k, c_k, p_k)

dif_quot_w_0 = dif_quot(gew_zeiten[0], a_w, b_w, c_w, p_w)
dif_quot_w_1 = dif_quot(gew_zeiten[1], a_w, b_w, c_w, p_w)
dif_quot_w_2 = dif_quot(gew_zeiten[2], a_w, b_w, c_w, p_w)
dif_quot_w_3 = dif_quot(gew_zeiten[3], a_w, b_w, c_w, p_w)

print("k0: ", dif_quot_k_0)
print("k1: ", dif_quot_k_1)
print("k2: ", dif_quot_k_2)
print("k3: ", dif_quot_k_3)

print("w0: ", dif_quot_w_0)
print("w1: ", dif_quot_w_1)
print("w2: ", dif_quot_w_2)
print("w3: ", dif_quot_w_3)

#bestimmung nu_ideal:

factor = ufloat(3*4190 + 750, 0)

n_0  = ufloat(7200.0, 0) 
n_1  = ufloat(7360.0, 0) 
n_2  = ufloat(7376.0, 0) 
n_3  = ufloat(7240.0, 0) 

def guete(factor, n, quot):
    return(factor * quot / n)

nu_real_0 = guete(factor, n_0, dif_quot_w_0)
nu_real_1 = guete(factor, n_1, dif_quot_w_1)
nu_real_2 = guete(factor, n_2, dif_quot_w_2)
nu_real_3 = guete(factor, n_3, dif_quot_w_3)

print("nu real 0: ", nu_real_0)
print("nu real 1: ", nu_real_1)
print("nu real 2: ", nu_real_2)
print("nu real 3: ", nu_real_3)

#bestimmung verdampfungswärme L:

r = ufloat(8.314, 0) 
#in J/(mol*K)
m=ufloat(-2001.8141, 111.7750) 

L = -m*r
print("L in J/mol: ", L)
#L:  (1.66+/-0.09)e+04 in J/mol
mol_in_g = ufloat(18.016, 0)
L= L / mol_in_g
print("L in J/g: ", L)




# bestimmung Massendurchsatz

massendurchsatz_0 = 1/L * factor *dif_quot_k_0
massendurchsatz_1 = 1/L * factor *dif_quot_k_1
massendurchsatz_2 = 1/L * factor *dif_quot_k_2
massendurchsatz_3 = 1/L * factor *dif_quot_k_3
#in g/J * J/K * K/min = g/min 
#massendurchsatz 0:  -16.8+/-2.0
#massendurchsatz 1:  -14.7+/-1.9
#massendurchsatz 2:  -11.5+/-1.4
#massendurchsatz 3:  -9.0+/-1.0

print("massendurchsatz 0: ", massendurchsatz_0)
print("massendurchsatz 1: ", massendurchsatz_1)
print("massendurchsatz 2: ", massendurchsatz_2)
print("massendurchsatz 3: ", massendurchsatz_3)



#rechnungen für mechanische Leistung N_mech:

#dm/dt in g/min

rho_0 = ufloat(5.51, 0)
#in g/L = g/(dm)^3 = 10^3 g/m^3
#umwandlung in g/m:
rho_0 *= 10**3
#in g/m^3

rho = 

kappa = 1.14