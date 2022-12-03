import numpy as np
import matplotlib.pyplot as plt

t, temp_k, durck_k, temp_w, durck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

gew_zeiten = [3, 9, 15, 21]

# bestimme N:
n = np.zeros(4)

for i, zeit in enumerate(gew_zeiten):
    print("i = ", i)
    j=0
    while j <= zeit:
        n[i] += leistung[j]
        print("n_",i,"=", n[i])
        j += 1

for i, value in enumerate(n):
    n[i] =1/gew_zeiten[i] * n[i]
    print("n_",i," = ", n[i])
#n_ 0  =  120.0
#n_ 1  =  122.66666666666666
#n_ 2  =  122.93333333333334
#n_ 3  =  120.66666666666666


#bestimme difquot:

a_k = -0.91132029
b_k = 0.02042680
c_k = 21.51604450
alpha_k = 1.19462353

a_w = 1.13913878
b_w = 0.02290029
c_w = 20.89673747
alpha_w = 1.22110022

def dif_quot(t, a, b, c, alpha) :
    return (alpha* a * t**(alpha-1)/(1 + b* t**(alpha))**2)

dq_k = np.zeros(4)
print("kaltes Reservoir:")
for i, time in enumerate(gew_zeiten):
    dq_k = dif_quot(time, a_k, b_k, c_k, alpha_k)
    print("dif_quot_",i,"=",dq_k)
#kaltes Reservoir:
#dif_quot_ 0 = -1.1647318214013536
#dif_quot_ 1 = -1.0159747306020086
#dif_quot_ 2 = -0.7992238226522068
#dif_quot_ 3 = -0.6243739226614388

dq_w = np.zeros(4)
print("warmes Reservoir:")
for i, time in enumerate(gew_zeiten):
    dq_w = dif_quot(time, a_w, b_w, c_w, alpha_w)
    print("dif_quot_",i,"=", dq_w)
#warmes Reservoir:
#dif_quot_ 0 = 1.4993024753884312
#dif_quot_ 1 = 1.2686377956376398
#dif_quot_ 2 = 0.9584928863838236
#dif_quot_ 3 = 0.7224878918480877


#weiter mit q1/t...