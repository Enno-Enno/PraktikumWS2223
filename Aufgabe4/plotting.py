import numpy as np
import matplotlib.pyplot as plt

(Delta_x, F) = np.genfromtxt('Hook_Daten.txt',unpack=True)

x = np.linspace(0,54)
sum = 0
for index in range(len(Delta_x)):
    if index == 0: 
        print('{--}')
    else:
        print('{:.4f}'.format(F[index] / Delta_x[index]))
        sum += F[index] / Delta_x[index]
print('Summe D: ', '{:.4f}'.format(sum))
print('Mittelwert D: ', '{:.4f}'.format(sum/10))

plt.plot(Delta_x, F, 'o')
plt.xlabel('$ \Delta x  [\\unit{{\\cm}}] $')
plt.ylabel('$ F [\\unit{{\\newton}}] $')


plt.savefig('build/plot.pdf')