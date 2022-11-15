import numpy as np
import matplotlib.pyplot as plt

(Delta_x, F) = np.genfromtxt('Hook_Daten.txt',unpack=True)

sum = 0
for index in range(len(Delta_x)):
    #if index == 0: 
    #    print('{--}')
    #else:
        print('{:.4f}'.format(F[index] / Delta_x[index]))
        sum += F[index] / Delta_x[index]
print('Summe D: ', '{:.4f}'.format(sum))
print('Mittelwert D: ', '{:.4f}'.format(sum/10))

mx=np.sum(Delta_x)/len(Delta_x)
mf=np.sum(F)/len(F)
print('Mittelwert der Auslenkung: ', '{:.4f}'.format(mx))
print('Mittelwert der Kraft:', '{:.4f}'.format(mf))