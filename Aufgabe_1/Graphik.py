import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
mpl.rcParams.update({            # <-- Set matplotlib options
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

def f(x,N_0,m):
    return N_0 * np.exp(m * x)



d, N = np.genfromtxt('daten.txt', unpack=True)
params, covariance_matrix = curve_fit(f , d, N) # x=d und y=N
x_lin = np.linspace(0, 5, 1000)

plt.subplot(1, 2, 1)
plt.ylabel(r'N [1/ 60 \unit{\second}]')
plt.xlabel(r'd / \unit{\cm} ')
plt.plot(d, N, 'o', label='Gemessene Werte')

plt.plot(x_lin,f(x_lin , params[0],params[1]), label='Theoretische Erwartung')

plt.legend(loc='best')


plt.subplot(1, 2, 2)
plt.plot(d, N, 'o', label='Gemessene Werte')
plt.plot(x_lin,f(x_lin , params[0],params[1]), label='Theoretische Erwartung')
plt.ylabel(r'N [1/ 60 \unit{\second}]')
plt.xlabel(r'd / \unit{\cm} ')
plt.yscale('log')

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')