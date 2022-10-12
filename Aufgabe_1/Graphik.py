import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 


def f(x,N_0,m):
    return N_0 * np.exp(m * x)



d, N = np.genfromtxt('daten.txt', unpack=True)
params, covariance_matrix = curve_fit(f , d, N) # x=d und y=N
x_lin = np.linspace(0, 5, 1000)

plt.subplot(1, 2, 1)
plt.ylabel(r'N[1/ 60 s]')
plt.xlabel(r'd / cm ')
plt.plot(d, N, 'o', label='Gemessene Werte')

plt.plot(x_lin,f(x_lin , params[0],params[1]), label='Theoretische Erwartung')

plt.legend(loc='best')


plt.subplot(1, 2, 2)
plt.plot(d, N, 'o', label='Gemessene Werte')
plt.plot(x_lin,f(x_lin , params[0],params[1]), label='Theoretische Erwartung')
plt.ylabel(r'N[1/ 60 s]')
plt.xlabel(r'd / cm ')
plt.yscale('log')

plt.legend(loc='best')

plt.savefig('build/plot.pdf')