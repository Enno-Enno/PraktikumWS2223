import numpy as np
import matplotlib.pyplot as plt

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

gew_zeiten = [3, 9, 15, 21]
warm_kelvin = np.zeros(4)
kalt_kelvin = np.zeros(4)
nu_ideal = np.zeros(4)
nu_real = np.zeros(4)

for i, zeit in enumerate(gew_zeiten):
    warm_kelvin[i] = 273.15 + temp_w[zeit]
    kalt_kelvin[i] = 273.15 + temp_k[zeit]
    nu_ideal[i] = warm_kelvin[i]/(warm_kelvin[i]-kalt_kelvin[i])
#umrechrechnung der 4 Zeitpunkte in kelvin


print("nu ideal:", nu_ideal)
#nu ideal: [45.85384615 14.1875      9.29228487  7.39883721]


# bestimme N:
n = np.zeros(4)

for i, zeit in enumerate(gew_zeiten):
    #print("i = ", i)
    j=0
    while j <= zeit:
        n[i] += leistung[j]
        #print("additon: n_",i,"=", n[i])
        j += 1

for i, value in enumerate(n):
    n[i] = 60*n[i]
#umrechnung von J/s in J/min

for i, value in enumerate(n):
    n[i] =1/(gew_zeiten[i]) * n[i]
    print("n_",i," = ", n[i])
#n_ 0  =  7200.0
#n_ 1  =  7360.0
#n_ 2  =  7376.0
#n_ 3  =  7240.0
#n_k in J/min


#bestimme difquot:

#parameter für kalt:
a_k = -0.91131991
b_k = 0.02042679
c_k = 294.66604398
alpha_k = 1.19462372
#parameter für warm:
a_w = 1.13913900
b_w = 0.02290029
c_w = 294.04673712
alpha_w = 1.22110015

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


#warmes Reservoir:
dif_quot_w = np.zeros(4)
print("warmes Reservoir:")
for i, time in enumerate(gew_zeiten):
    dif_quot_w[i] = dif_quot(time, a_w, b_w, c_w, alpha_w)
    print("dif_quot_w_",i,"=", dif_quot_w[i])
#dif_quot_w_ 0 = 1.4993025822691834
#dif_quot_w_ 1 = 1.2686378707296608
#dif_quot_w_ 2 = 0.9584929746374173
#dif_quot_w_ 3 = 0.7224879854278933



#weiter mit q1/t..., t_1 entspricht t_w

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