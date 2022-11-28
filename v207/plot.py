import numpy as np
import matplotlib.pyplot as plt

temp, temp_oben, temp_unten = np.genfromtxt("Messdaten_grKu_steigendeTemp.txt", unpack=True)
n=10
y_oben=np.zeros(n)
y_unten=np.zeros(n)

for j in range(n):
    for i, temperature in enumerate(temp):

        if i==2*j and temp[i] == temp[i+1]:
            y_oben[j] = (temp_oben[i] + temp_oben[i+1])/2
            y_unten[j] = (temp_unten[i] + temp_unten[i+1])/2

#print(y_oben)

plt.plot(temp, np.exp(1/(np.exp(temp))), 'b.')
plt.yscale('log')

plt.show()
