import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy as scp

temp, t_oben, t_unten = np.genfromtxt("Messdaten_grKu_steigendeTemp.txt", unpack=True)
n=10
artm_t_oben  =np.zeros(n)   #arithmetische Mittel
artm_t_unten =np.zeros(n)
sdev_t_oben  =np.zeros(n)   #standardabweichungen 
sdev_t_unten =np.zeros(n)
single_temp  =np.zeros(n)   #array mit Temperaturen, aber jede Temperatur nur einmal

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


plt.errorbar(single_temp, artm_t_oben, yerr=sdev_t_oben, fmt='x', label=r'Laufzeiten oben')
plt.errorbar(single_temp, artm_t_unten, yerr=sdev_t_unten, fmt='x', label=r'Laufzeiten unten')

plt.ylabel("t / \\unit{{\\s}}")
plt.xlabel("T / \\unit{{\\celsius}}")
plt.savefig("build/Messreihe3.pdf")
###  Berechnungen eta nach Temperatur und Plot dafür ###