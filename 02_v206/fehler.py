import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

gew_zeiten = [3, 9, 15, 21]

#def function_3(t, a, b, c, alpha) :
#    return ((a*t**alpha)/(1 + b*t**alpha) + c)

def dif_quot(t, a, b, c, alpha) :
    return ((alpha* a * t**(alpha-1))/((1 + b* t**(alpha))**2))
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

r = ufloat(8.314, 0) #gas konst
#in J/(mol*K)
m=ufloat(-2001.8141, 111.7750) 

L = -m*r
print("L in J/mol: ", L)
#L:  (1.66+/-0.09)e+04 in J/mol 

# mol_in_g = ufloat(18.016, 0) #von Wasser
mol_in_g = ufloat(120.91, 0)
L= L / mol_in_g
print("L in J/g: ", L)
#L in J/g:  138+/-8




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

import numpy as np
import matplotlib.pyplot as plt

t, temp_k, druck_k, temp_w, druck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15
#in K

for i,value in enumerate(druck_k):
    druck_k[i] *= 100000
#in Pa

for i,value in enumerate(druck_k):
    druck_w[i] *= 100000
#in Pa


rho_0 = ufloat(5.51, 0)
#in g/L = g/(dm)^3 = 10^3 g/m^3
#umwandlung in g/m^3:
rho_0 *= 10**3
#in g/m^3

T_0 = ufloat(273.15, 0) # in K

p_0 = ufloat(100000, 0) # in Pa

rho_k = rho_0 * T_0 * druck_k/(temp_k * p_0) # in g/m^3

print("rho: ", rho_k)
#rho:  
# [24543.13300492611+/-0 20466.517083120856+/-0 22605.388632872502+/-0
# 22713.937918024356+/-0 23342.25142167844+/-0 23439.191036511504+/-0
# 22997.911442958848+/-0 21504.553580763193+/-0 21060.787126115094+/-0
# 21134.72353870458+/-0 20141.62599049128+/-0 20212.810390528357+/-0
# 19210.081191278143+/-0 18736.253779121467+/-0 18259.383050847457+/-0
# 17773.077294685987+/-0 17824.103534900412+/-0 17327.507825148405+/-0
# 16834.476456792352+/-0 16332.680412371132+/-0 16374.141432456934+/-0
# 15862.852444121389+/-0 15349.328719723184+/-0 15382.946523088152+/-0
# 15411.07405375754+/-0 15444.96316657504+/-0]

#dm/dt in g/min

#p_a = p_k, p_b = p_w, T_2 = T_k

kappa = ufloat(1.14, 0)


n_mech_3 = 1/(kappa - 1) * (druck_w[3] * (druck_k[3]/druck_w[3])**(1/kappa) - druck_k[3]) * 1/rho_k[3] * massendurchsatz_0
n_mech_9 = 1/(kappa - 1) * (druck_w[9] * (druck_k[9]/druck_w[9])**(1/kappa) - druck_k[9]) * 1/rho_k[9] * massendurchsatz_1
n_mech_15 = 1/(kappa - 1) * (druck_w[15] * (druck_k[15]/druck_w[15])**(1/kappa) - druck_k[15]) * 1/rho_k[15] * massendurchsatz_2
n_mech_21 = 1/(kappa - 1) * (druck_w[21] * (druck_k[21]/druck_w[21])**(1/kappa) - druck_k[21]) * 1/rho_k[21] * massendurchsatz_3
#n_mech in 1 * Pa * m^3/g * g/min = Pa * m^3 / min = kg /(m* s^2) * m^3 /min = kg* m^2 /(s^2 * min)

n_mech_3  /= 60
n_mech_9  /= 60
n_mech_15 /= 60
n_mech_21 /= 60


print("mechanische leistung nach 3s:", n_mech_3)
print("mechanische leistung nach 9s:", n_mech_9)
print("mechanische leistung nach 15s:", n_mech_15)
print("mechanische leistung nach 21s:", n_mech_21)

#mechanische leistung nach 3s pro minute: -119+/-14
#mechanische leistung nach 3s: -1.98+/-0.24
#mechanische leistung nach 9s: -3.0+/-0.4
#mechanische leistung nach 15s: -3.7+/-0.4
#mechanische leistung nach 21s: -3.8+/-0.4