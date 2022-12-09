import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy as scp

temp, t_oben, t_unten = np.genfromtxt("Messdaten_grKu_steigendeTemp.txt", unpack=True)
n=10
artm_t_oben  =np.zeros(n)
artm_t_unten =np.zeros(n)
sdev_t_oben  =np.zeros(n)
sdev_t_unten =np.zeros(n)
single_temp  =np.zeros(n)

for j in range(n):
    for i, temperature in enumerate(temp):

        if i==2*j and temp[i] == temp[i+1]:
            artm_t_oben[j] = (t_oben[i] + t_oben[i+1])/2
            artm_t_unten[j] = (t_unten[i] + t_unten[i+1])/2
            sdev_t_oben[j] = np.std(t_oben[j:j+2])
            sdev_t_unten[j] = np.std(t_unten[j:j+2])
            single_temp[j]= temp[i]

# Hier werden paarweise die Mittewerte von den "oben" und den "unten" Messwerten berechnet

single_temp_k = single_temp + 273.16

print("artm_t_oben ",artm_t_oben)   # immer drauf achten t ist Zeit temp ist Temperatur
print("artm_t_unten",artm_t_unten)
print("sdev_t_oben ",sdev_t_oben)
print("sdev_t_unten",sdev_t_unten)
print("single_temp",single_temp)

np.savetxt('Messreihe3.txt', np.column_stack([artm_t_oben, artm_t_unten, sdev_t_oben, sdev_t_unten]), header="artm_t_oben artm_t_unten sdev_t_oben sdev_t_unten")

unc_t_oben = unp.uarray(artm_t_oben, sdev_t_oben)
unc_t_unten = unp.uarray(artm_t_unten, sdev_t_unten)



#plt.errorbar(single_temp, artm_t_oben, yerr=sdev_t_oben, fmt='o', label=r'Laufzeiten oben')
#plt.errorbar(single_temp, artm_t_unten, yerr=sdev_t_unten, fmt='o', label=r'Laufzeiten unten')
#
#plt.ylabel("t / \\unit{{\\s}}")
#plt.xlabel("T / \\unit{{\\celsius}}")
#plt.savefig("build/Messreihe3.pdf")

###  Berechnungen eta nach Temperatur und Plot dafür ###

rho_temp, rho_Wasser = np.genfromtxt('Geschke_Wasserdichte.txt',unpack = True, dtype=None)
#print('rho_temp',rho_temp)
#print('rho_Wasser',rho_Wasser)

dichten = dict()
for index in range(len(rho_temp)):
    dichten[rho_temp[index]]= rho_Wasser[index]

print(dichten)

def eta(K, rho_Kugel, rho_Wasser, t):
    return K * (rho_Kugel - rho_Wasser) * t


rho_gr_Kugel = ufloat(2.407 ,0.005)
K_gr_oben = ufloat(0.0236 , 0.0004)
K_gr_unten = ufloat(0.0231, 0.0006)

eta_oben = unp.uarray(np.zeros(n),np.zeros(n))
eta_unten = unp.uarray(np.zeros(n),np.zeros(n))


print("Viskosität nach Temperatur oben:" )
print(single_temp[0], eta(K_gr_oben,rho_gr_Kugel ,dichten[26] ,unc_t_oben[0]))
print(single_temp[1], eta(K_gr_oben,rho_gr_Kugel ,dichten[27] ,unc_t_oben[1]))
print(single_temp[2], eta(K_gr_oben,rho_gr_Kugel ,dichten[30] ,unc_t_oben[2]))
print(single_temp[3], eta(K_gr_oben,rho_gr_Kugel ,dichten[30] ,unc_t_oben[3]))
print(single_temp[4], eta(K_gr_oben,rho_gr_Kugel ,dichten[35] ,unc_t_oben[4]))
print(single_temp[5], eta(K_gr_oben,rho_gr_Kugel ,dichten[40] ,unc_t_oben[5]))
print(single_temp[6], eta(K_gr_oben,rho_gr_Kugel ,dichten[40] ,unc_t_oben[6]))
print(single_temp[7], eta(K_gr_oben,rho_gr_Kugel ,dichten[45] ,unc_t_oben[7]))
print(single_temp[8], eta(K_gr_oben,rho_gr_Kugel ,dichten[50] ,unc_t_oben[8]))
print(single_temp[9], eta(K_gr_oben,rho_gr_Kugel ,dichten[50] ,unc_t_oben[9]))

eta_oben[0] = eta(K_gr_oben,rho_gr_Kugel ,dichten[26] ,unc_t_oben[0])
eta_oben[1] = eta(K_gr_oben,rho_gr_Kugel ,dichten[27] ,unc_t_oben[1])
eta_oben[2] = eta(K_gr_oben,rho_gr_Kugel ,dichten[30] ,unc_t_oben[2])
eta_oben[3] = eta(K_gr_oben,rho_gr_Kugel ,dichten[30] ,unc_t_oben[3])
eta_oben[4] = eta(K_gr_oben,rho_gr_Kugel ,dichten[35] ,unc_t_oben[4])
eta_oben[5] = eta(K_gr_oben,rho_gr_Kugel ,dichten[40] ,unc_t_oben[5])
eta_oben[6] = eta(K_gr_oben,rho_gr_Kugel ,dichten[40] ,unc_t_oben[6])
eta_oben[7] = eta(K_gr_oben,rho_gr_Kugel ,dichten[45] ,unc_t_oben[7])
eta_oben[8] = eta(K_gr_oben,rho_gr_Kugel ,dichten[50] ,unc_t_oben[8])
eta_oben[9] = eta(K_gr_oben,rho_gr_Kugel ,dichten[50] ,unc_t_oben[9])


print("Viskosität nach Temperatur unten:" )
print(single_temp[0], eta(K_gr_unten,rho_gr_Kugel ,dichten[26] ,unc_t_unten[0]),dichten[26])
print(single_temp[1], eta(K_gr_unten,rho_gr_Kugel ,dichten[27] ,unc_t_unten[1]),dichten[27])
print(single_temp[2], eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[2]),dichten[30])
print(single_temp[3], eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[3]),dichten[30])
print(single_temp[4], eta(K_gr_unten,rho_gr_Kugel ,dichten[35] ,unc_t_unten[4]),dichten[35])
print(single_temp[5], eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[5]),dichten[40])
print(single_temp[6], eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[6]),dichten[40])
print(single_temp[7], eta(K_gr_unten,rho_gr_Kugel ,dichten[45] ,unc_t_unten[7]),dichten[45])
print(single_temp[8], eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[8]),dichten[50])
print(single_temp[9], eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[9]),dichten[50])

eta_unten[0] = eta(K_gr_unten,rho_gr_Kugel ,dichten[26] ,unc_t_unten[0])
eta_unten[1] = eta(K_gr_unten,rho_gr_Kugel ,dichten[27] ,unc_t_unten[1])
eta_unten[2] = eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[2])
eta_unten[3] = eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[3])
eta_unten[4] = eta(K_gr_unten,rho_gr_Kugel ,dichten[35] ,unc_t_unten[4])
eta_unten[5] = eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[5])
eta_unten[6] = eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[6])
eta_unten[7] = eta(K_gr_unten,rho_gr_Kugel ,dichten[45] ,unc_t_unten[7])
eta_unten[8] = eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[8])
eta_unten[9] = eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[9])

#### Nicht mehr nötig mit unp.uarray
##Mittel_eta= np.zeros(n)
##Fehler_eta= np.zeros(n)
##Mittel_eta[0] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[26] ,unc_t_unten[0]))
##Mittel_eta[1] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[27] ,unc_t_unten[1]))
##Mittel_eta[2] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[2]))
##Mittel_eta[3] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[3]))
##Mittel_eta[4] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[35] ,unc_t_unten[4]))
##Mittel_eta[5] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[5]))
##Mittel_eta[6] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[6]))
##Mittel_eta[7] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[45] ,unc_t_unten[7]))
##Mittel_eta[8] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[8]))
##Mittel_eta[9] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[9]))


##Fehler_eta[0] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[26] ,unc_t_unten[0]))
##Fehler_eta[1] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[27] ,unc_t_unten[1]))
##Fehler_eta[2] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[2]))
##Fehler_eta[3] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[30] ,unc_t_unten[3]))
##Fehler_eta[4] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[35] ,unc_t_unten[4]))
##Fehler_eta[5] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[5]))
##Fehler_eta[6] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[40] ,unc_t_unten[6]))
##Fehler_eta[7] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[45] ,unc_t_unten[7]))
##Fehler_eta[8] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[8]))
##Fehler_eta[9] = unp.nominal_values(eta(K_gr_unten,rho_gr_Kugel ,dichten[50] ,unc_t_unten[9]))

#Mittel_eta_ln = np.ln(Mittel_eta) 

x_plot = np.linspace(single_temp_k[0], single_temp_k[9], 1000)

#x_plot = np.linspace(1/single_temp_k[9], 1/single_temp_k[0], 1000)
print("eta_oben:", eta_oben)
print("eta_unten:", eta_unten)
print(unp.nominal_values(eta_oben))

eta_oben_log = unp.log(eta_oben)
eta_unten_log = unp.log(eta_unten)

print("eta_oben_log:", eta_oben_log)
print("eta_unten_log:", eta_unten_log)

#params_o, covariance_matrix = np.polyfit(1/single_temp_k , unp.nominal_values(eta_oben_log),deg=1,cov=True)
params_o, covariance_matrix = np.polyfit(1/single_temp_k , np.log(unp.nominal_values(eta_oben)),deg=1,cov=True)
params_u, covariance_matrix = np.polyfit(1/single_temp_k , np.log(unp.nominal_values(eta_unten)),deg=1,cov=True)

print("params_o:", params_o)
print("params_u:", params_u)