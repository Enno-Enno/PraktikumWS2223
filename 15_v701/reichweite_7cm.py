import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy import odr

print("----------------------------------")
print("MESSUNG 2 - 7cm")
# MESSUNG 2 - 7cm
# ----------------------------------
# Teil 1: eff_length - Zählrate
# a = -62.23 +- 6.85
# b = 136.86 +- 12.44
# mittlere_reichweite =  1.32+/-0.08 cm
# zugehörige Energie =  2.62+/-0.11 MeV
# ----------------------------------
# Teil 2: eff_length - energymax
# a = -0.482 +- 0.046
# b = 3.948 +- 0.058
# energieverlust = (481.87 +- 46.47) keV/cm


p, counts, channel, zaehlrate = np.genfromtxt("messungen/reichweite_7cm.txt", unpack = True)
time = 120 #sekunden
distance = 6 #cm

druck = unp.uarray(p, 5 * np.ones(len(p))) * 10**(-3) # druck in bar
eff_length = distance * druck / (1013 * 10**(-3)) # in cm

def lin(beta, x):
    return beta[0] * x + beta[1]




#plot 1 für zaehlrate:
print("----------------------------------")
print("Teil 1: eff_length - Zählrate")

max_ind = 8 #für [:max_ind] darstellung, sonst array[max_ind-1] als Grenze!

rate = unp.uarray(zaehlrate/time, np.sqrt(zaehlrate/time)) # pro sekunde
#print("rate[max_ind] : ", rate[max_ind])
#print("rate[:max_ind] : ", rate[:max_ind])
data_rate = odr.RealData(nom(eff_length[:max_ind]), nom(rate[:max_ind]), sx = std(eff_length[:max_ind]), sy = std(rate[:max_ind])) #zu plottende daten ,sx und sy sind std devs

lin_model = odr.Model(lin) #stores information about the function you wish to fit

odr_rate = odr.ODR(data_rate, lin_model, [-50, 1]) #wie curve fit, beta0 = [..., ...] entspricht p0 (startwerte)

out = odr_rate.run() # run the regression

params_rate = out.beta
errors_rate = out.sd_beta

for name, value, error in zip('ab', params_rate, errors_rate):
 print(f'{name} = {value:.2f} +- {error:.2f}')

mittlere_reichweite = (rate[0] / 2 - params_rate[1]) / params_rate[0] #cm
energie_reichweite = (mittlere_reichweite * 10 / 3.1)**(2/3) #reichweite in mm und energie in MeV
print("mittlere_reichweite = ", mittlere_reichweite, "cm")
print("zugehörige Energie = ", energie_reichweite, "MeV")




# vorbereitung plot 2 für die energie
print("----------------------------------")
print("Teil 2: eff_length - energymax")

dreisatz = 4 / channel[0] #MeV pro channel
energymax = dreisatz * channel[:max_ind] #in MeV

data_energymax = odr.RealData(nom(eff_length[:max_ind]), nom(energymax[:max_ind]), sx = std(eff_length[:max_ind])) #zu plottende daten ,sx und sy sind std devs

lin_model = odr.Model(lin) #stores information about the function you wish to fit

odr_energymax = odr.ODR(data_energymax, lin_model, [1, 1]) #wie curve fit, beta0 = [..., ...] entspricht p0 (startwerte)

out = odr_energymax.run() # run the regression

params_energymax = out.beta
errors_energymax = out.sd_beta

for name, value, error in zip('ab', params_energymax, errors_energymax):
 print(f'{name} = {value:.3f} +- {error:.3f}')

print(f"energieverlust = ({-params_energymax[0]*1000 :.2f} +- {errors_energymax[0]*1000:.2f}) keV/cm")




#plots: 

x_min = nom(eff_length[0])
x_max = nom(eff_length[max_ind - 1])
x_plot = np.linspace(x_min, x_max, 1000)
plt.figure(constrained_layout = True)
plt.errorbar(nom(eff_length[:max_ind]), nom(rate[:max_ind]), xerr = std(eff_length[:max_ind]), yerr = std(rate[:max_ind]), fmt = "x", label = "Messrate mit Fehlerbalken")
plt.plot(x_plot, lin(params_rate, x_plot), "-", label = "Ausgleichsgerade")
plt.grid()
plt.xlabel("$x / \\unit{\\cm}$")
plt.ylabel("$N/ (1 / \\unit{\\s})$")
plt.legend()
plt.savefig("build/reichweite_7cm_rate.pdf")


plt.figure(constrained_layout = True)
plt.errorbar(nom(eff_length[:max_ind]), nom(energymax), xerr = std(eff_length[:max_ind]), yerr = std(energymax), fmt = "x", label = "Energie mit Fehlerbalken")
plt.plot(x_plot, lin(params_energymax, x_plot), "-", label = "Ausgleichsgerade")
plt.grid()
plt.xlabel("$x / \\unit{\\cm}$")
plt.ylabel("$E / \\unit{\\mega\\electronvolt}$")
plt.legend()
plt.savefig("build/reichweite_7cm_energymax.pdf")