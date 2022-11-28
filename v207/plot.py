import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp

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

print("artm_t_oben ",artm_t_oben)
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


rho_temp, rho_Wasser = np.genfromtxt('Geschke_Wasserdichte.txt',unpack = True, dtype=None)
print('rho_temp',rho_temp)
print('rho_Wasser',rho_Wasser)

dichten = dict()
for index in range(len(rho_temp)):
    dichten[rho_temp[index]]= rho_Wasser[index] 

print(dichten)

def eta(K, rho_Kugel, rho_Wasser, t):
    return K * (rho_Kugel - rho_Wasser) * t


#Messreihe 1:
#Durchschnittszeiten kleine Kugel:
#oben: 12.32400 mit Fehler:  0.15500
#unten: 12.24800 mit Fehler:  0.18405
#Messreihe 2:
#Durchschnittszeiten grosse Kugel:
#oben: 35.02400 mit Fehler:  0.29574
#unten: 35.60000 mit Fehler:  0.75913
#Reynold:
#Geschwindigkeit klein oben:  0.811+/-0.010
#Geschwindigkeit klein unten:  0.816+/-0.012
#Geschwindigkeit gross oben:  0.1428+/-0.0012
#Geschwindigkeit gross unten:  0.1404+/-0.0030
#eta empirisch klein:  0.001152+/-0.000018
#K oben und gross:  (2.33+/-0.04)e-05
#K unten und gross:  (2.30+/-0.06)e-05