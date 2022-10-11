import matplotlib.pyplot as plt
import numpy as np



#x_d = np.linspace(0, 5, 1000)
#y_N = N_0 * np.exp(-m * x_d)
#plt.plot(x_d,y_N, label='Theoretische Erwartung')


d, N = np.genfromtxt('daten.txt', unpack=True)
plt.plot(d, N, 'o', label='gemessene Werte')

#plt.ylabel(r'$\text{N}[1/ 60 \unit{\second}]$')
#plt.xlabel(r'$d / [\unit{\centimeter}] $')

plt.legend(loc='best')
plt.savefig('build/plot.pdf')