import numpy as np
import matplotlib.pyplot as plt

temp, t_oben, t_unten = np.genfromtxt("Messdaten_grKu_steigendeTemp.txt", unpack=True)
n=10
artm_t_oben  =np.zeros(n)
artm_t_unten =np.zeros(n)
sdev_t_oben  =np.zeros(n)
sdev_t_unten =np.zeros(n)

for j in range(n):
    for i, temperature in enumerate(temp):

        if i==2*j and temp[i] == temp[i+1]:
            artm_t_oben[j] = (t_oben[i] + t_oben[i+1])/2
            artm_t_unten[j] = (t_unten[i] + t_unten[i+1])/2
            sdev_t_oben[j] = np.std(t_oben[j:j+2])
            sdev_t_unten[j] = np.std(t_unten[j:j+2])

# Hier werden paarweise die Mittewerte von den "oben" und den "unten" Messwerten berechnet

print("artm_t_oben",artm_t_oben)
print("artm_t_unten",artm_t_oben)



plt.yscale('log')
