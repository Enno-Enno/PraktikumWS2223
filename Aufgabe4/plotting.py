import numpy as np
import matplotlib.pyplot as plt

(Delta_x, F) = np.genfromtxt('Hook_Daten.txt',unpack=True)

x = np.linspace(0,54)

for index in range(len(Delta_x)):
    if index == 0: 
        print('{--}')
    else:
        print('{:.4f}'.format(F[index] / Delta_x[index]))


plt.plot(Delta_x, F, 'o')
plt.xlabel('$ \Delta x  [\\unit{{\\cm}}] $')
plt.ylabel('$ F [\\unit{{\\newton}}] $')


plt.savefig('build/plot.pdf')