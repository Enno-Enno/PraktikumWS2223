import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy import odr


p, counts, channel, zaehlrate = np.genfromtxt("messungen/reichweite_6cm.txt", unpack = True)
time = 120 #sekunden
distance = 6 #cm


druck = unp.uarray(p, 5 * np.ones(len(p))) * 10**(-3) # druck in bar
rate = unp.uarray(zaehlrate/time, np.sqrt(zaehlrate/time)) # pro sekunde

eff_length = distance * druck / (1013 * 10**(-3)) # in cm

dreisatz = 4 / counts[0] #MeV pro channel
energymax = dreisatz * channel #in MeV

# abschätzen der steigung: print((rate[9] - rate[0])/(eff_length[9] - eff_length[0]))


def lin(beta, x):
    return beta[0] * x + beta[1]

data_rate = odr.RealData(nom(eff_length), nom(rate), sx = std(eff_length), sy = std(rate)) #zu plottende daten ,sx und sy sind std devs

lin_model = odr.Model(lin) #stores indormation about the function you wish to fit

odr_rate = odr.ODR(data_rate, lin_model, [-60, 1]) #wie curve fit, beta0 entspricht p0 (startwerte)

out = odr_rate.run() # run the regression

params_rate = out.beta
errors_rate = out.sd_beta


for name, value, error in zip('ab', params_rate, errors_rate):
 print(f'{name} = {value:.6f} +- {error:.6f}')


#plot 1 für zaehlrate:

x = np.linspace(nom(eff_length[0]), nom(eff_length[len(eff_length)-1]))

x_min = nom(eff_length[0]) - 1
x_max = nom(eff_length[len(eff_length) - 1]) + 1

plt.figure(constrained_layout = True)
plt.errorbar(nom(druck), nom(rate), xerr = std(druck), yerr = std(rate), fmt = "x", label = "Messrate mit Fehlerbalken")
plt.plot(x, params_rate[0] * x + params_rate[1], "-", label = "Ausgleichsgerade")
plt.xlim(x_min, x_max)
plt.legend()
plt.savefig("build/reichweite_6cm_rate.pdf")