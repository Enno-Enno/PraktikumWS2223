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
    n[i] =1/(gew_zeiten[i]) * n[i]
    print("n_",i," = ", n[i])
# n_ 0  =  120.0
# n_ 1  =  122.66666666666666
# n_ 2  =  122.93333333333334
# n_ 3  =  120.66666666666666
print("n:", n)
#n: [ 360. 1104. 1844. 2534.]


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

dq_nach_dt_1 = np.zeros(4)

for i, value in enumerate(dif_quot_w):
    dq_nach_dt_1[i] = factor * value
    nu_real[i] = dq_nach_dt_1[i]/n[i] 
print("nu_real = ", nu_real)
#nu_real =  [166.42258663 137.75752531 103.85406526  79.75309364]
# das kann nicht sein... ca mind faktor 10 zu gross...

#nu_real =  [55.47419554 15.3063917   6.92360435  3.79776636]

################################################test
###############################################test_real = np.zeros(4)
###############################################q1 = np.zeros(4)
###############################################
###############################################for i, temperatur in enumerate(warm_kelvin):
###############################################    q1[i] = factor * temperatur
###############################################    test_real[i] = q1[i]/n[i]
###############################################
###############################################print(q1)
###############################################print(test_real)