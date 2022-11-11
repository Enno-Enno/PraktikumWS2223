import numpy as np
import matplotlib.pyplot as plt

(Delta_x, F) = np.genfromtxt('Hook_Daten.txt',unpack=True)

x = np.linspace(0,54)


plt.plot(Delta_x, F, 'o')
plt.xlabel('$\Delta x / \\unit{{\\cm}}$')
plt.ylabel('$ F /\\, \\unit{{\\newton}}$')


plt.savefig('build/plot.pdf')