import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy import odr

# ----------------------------------
# Teil 1: eff_length - Zählrate
# a = -42.15 +- 6.69
# b = 150.59 +- 22.35
# mittlere_reichweite =  1.63+/-0.15 cm
# zugehörige Energie =  3.02+/-0.19 MeV
# ----------------------------------
# Teil 2: eff_length - energymax
# a = -0.260 +- 0.080
# b = 4.277 +- 0.100
# energieverlust = (0.00260 +- 0.00080) MeV/m


p, counts, channel, zaehlrate = np.genfromtxt("messungen/reichweite_6cm.txt", unpack = True)
time = 120 #sekunden
distance = 6 #cm

druck = unp.uarray(p, 5 * np.ones(len(p))) * 10**(-3) # druck in bar
eff_length = distance * druck / (1013 * 10**(-3)) # in cm

def lin(beta, x):
    return beta[0] * x + beta[1]




#plot 1 für zaehlrate:
print("----------------------------------")
print("Teil 1: eff_length - Zählrate")


rate = unp.uarray(zaehlrate/time, np.sqrt(zaehlrate/time)) # pro sekunde

# abschätzen der steigung: 
# print((rate[9] - rate[0])/(eff_length[9] - eff_length[0]))

data_rate = odr.RealData(nom(eff_length), nom(rate), sx = std(eff_length), sy = std(rate)) #zu plottende daten ,sx und sy sind std devs

lin_model = odr.Model(lin) #stores information about the function you wish to fit

odr_rate = odr.ODR(data_rate, lin_model, [-60, 1]) #wie curve fit, beta0 = [..., ...] entspricht p0 (startwerte)

out = odr_rate.run() # run the regression

params_rate = out.beta
errors_rate = out.sd_beta

for name, value, error in zip('ab', params_rate, errors_rate):
 print(f'{name} = {value:.2f} +- {error:.2f}')

#reichweite = (rate / 2 - params_rate[1]) / params_rate[0]
#print("reichweite: ", reichweite)
mittlere_reichweite = (rate[0] / 2 - params_rate[1]) / params_rate[0] #cm
energie_reichweite = (mittlere_reichweite * 10 / 3.1)**(2/3) #reichweite in mm und energie in MeV
print("mittlere_reichweite = ", mittlere_reichweite, "cm")
print("zugehörige Energie = ", energie_reichweite, "MeV")

x_min_rate = nom(eff_length[0])
x_max_rate = nom(eff_length[len(eff_length) - 1])
x_rate = np.linspace(x_min_rate, x_max_rate, 1000)



# vorbereitung plot 2 für die energie
print("----------------------------------")
print("Teil 2: eff_length - energymax")
#np.seterr(divide='ignore', invalid='ignore')

max_ind = 8 # für [:max_ind] darstellung, sonst channel[max_ind-1] = 699 als Grenze!
dreisatz = 4 / channel[0] #MeV pro channel
energymax = dreisatz * channel #in MeV

data_energymax = odr.RealData(nom(eff_length[:max_ind]), nom(energymax[:max_ind]), sx = std(eff_length[:max_ind])) #zu plottende daten ,sx und sy sind std devs

lin_model = odr.Model(lin) #stores information about the function you wish to fit

odr_energymax = odr.ODR(data_energymax, lin_model, [1, 1]) #wie curve fit, beta0 = [..., ...] entspricht p0 (startwerte)

out = odr_energymax.run() # run the regression

params_energymax = out.beta
errors_energymax = out.sd_beta

for name, value, error in zip('ab', params_energymax, errors_energymax):
 print(f'{name} = {value:.3f} +- {error:.3f}')

print(f"energieverlust = ({-params_energymax[0]/100 :.5f} +- {errors_energymax[0]/100:.5f}) MeV/m")


x_min_energymax = nom(eff_length[0])
x_max_energymax = nom(eff_length[max_ind -1])
x_energymax = np.linspace(x_min_energymax, x_max_energymax, 1000)


#plots: 

plt.figure(constrained_layout = True)
plt.errorbar(nom(eff_length), nom(energymax), xerr = std(eff_length), yerr = std(energymax), fmt = "x", label = "Energie mit Fehlerbalken")
plt.plot(x_energymax, lin(params_energymax, x_energymax), "-", label = "Ausgleichsgerade")
#plt.xlim(x_min - 0.25, x_max + 0.25)
plt.xlabel("$x / \\unit{\\cm}$")
plt.ylabel("$E / \\unit{\\mega\\electronvolt}$")
plt.legend()
plt.savefig("build/reichweite_6cm_energymax.pdf")

plt.figure(constrained_layout = True)
plt.errorbar(nom(eff_length), nom(rate), xerr = std(eff_length), yerr = std(rate), fmt = "x", label = "Messrate mit Fehlerbalken")
plt.plot(x_rate, lin(params_rate, x_rate), "-", label = "Ausgleichsgerade")
#plt.xlim(x_min - 0.25, x_max + 0.25)
plt.xlabel("$x / \\unit{\\cm}$")
plt.ylabel("$N/ (1 / \\unit{\\s})$")
plt.legend()
plt.savefig("build/reichweite_6cm_rate.pdf")