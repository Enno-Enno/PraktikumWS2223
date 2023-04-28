import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

# m = 1.02889518 +- 0.01129740
# b = -0.74787535 +- 0.50748549

alpha_1, alpha_2 = np.genfromtxt("messung_1_reflexion.txt", unpack = True)

#einfall = unp.uarray(alpha_1, 1 * np.ones(len(alpha_1)))
#einfall = unp.uarray(alpha_1, np.zeros(len(alpha_1)))
einfall = alpha_1
ausfall = unp.uarray(alpha_2, 1 * np.ones(len(alpha_2)))

#winkel in deg
# zur umrechnung zu rad: np.deg2rad(

def reflexion(alpha_1, m, b):
    return(m*alpha_1 + b)

params, covariance_matrix = curve_fit(reflexion, einfall, [i.n for i in ausfall], sigma = [i.s for i in ausfall])
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("mb", params, errors):
     print(f'{name} = {value:.8f} +- {error:.8f}')

# steigung = ufloat(params[0], error[0])

x = np.linspace(einfall[0], einfall[len(einfall)-1], 1000)
plt.figure(constrained_layout = True)
plt.errorbar(einfall, [i.n for i in ausfall], yerr = [i.s for i in ausfall], fmt = "x", label = "Messwerte inkl. Fehlerbalken")
plt.plot(x, reflexion(x, *params), label = "Ausgleichsgerade")
plt.xlabel("$\\alpha_1 / \\unit{\\degree}$")
plt.ylabel("$\\alpha_2 / \\unit{\\degree}$")
plt.grid()
plt.legend()
plt.savefig("build/c01_reflexion.pdf")