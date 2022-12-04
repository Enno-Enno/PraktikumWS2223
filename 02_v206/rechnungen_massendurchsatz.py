import numpy as np
import matplotlib.pyplot as plt

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15
    temp_w[i] += 273.15

gew_zeiten = [3, 9, 15, 21]

#bestimme L:




#bestimme difquot:

#parameter für kalt:
a_k = -0.91131991
b_k = 0.02042679
c_k = 294.66604398
alpha_k = 1.19462372

def dif_quot(t, a, b, c, alpha) :
    return (alpha* a * t**(alpha-1)/(1 + b* t**(alpha))**2)
#in K/min

#kaltes reservoir:
dif_quot_k = np.zeros(4)
print("kaltes Reservoir:")
for i, time in enumerate(gew_zeiten):
    dif_quot_k[i] = dif_quot(time, a_k, b_k, c_k, alpha_k)
    print("dif_quot_k_",i,"=",dif_quot_k[i])
#dif_quot_k_ 0 = -1.1647318102435604
#dif_quot_k_ 1 = -1.0159749249040468
#dif_quot_k_ 2 = -0.799224014090223
#dif_quot_k_ 3 = -0.6243740742879325


#weiter mit q2/t..., t_2 entspricht t_k

m1_cw = 3 * 4190
mk_ck = 750
factor = m1_cw + mk_ck
#in J/K

dq_nach_dt_1 = np.zeros(4)

for i, value in enumerate(dif_quot_w):
    dq_nach_dt_1[i] = factor * value
    nu_real[i] = dq_nach_dt_1[i]/n[i] 
print("nu_real = ", nu_real)

#nu_real =  [2.77370978 2.29595876 1.73090109 1.32921823]

ideal = [45.9, 14.2, 9.3, 7.4]
real = [2.8, 2.3, 1.7, 1.3]

abweichung = np.zeros(4)

for i, value in enumerate(ideal):
    abweichung[i] = 1 - (real[i] / ideal[i])

print("Abweichung nu: ", abweichung)