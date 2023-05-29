# abschätzen der steigung: 
# print((energymax[9] - energymax[0])/(eff_length[9] - eff_length[0]))

data_energymax = odr.RealData(nom(eff_length), nom(energymax), sx = std(eff_length), sy = std(energymax)) #zu plottende daten ,sx und sy sind std devs

lin_model = odr.Model(lin) #stores information about the function you wish to fit

odr_energymax = odr.ODR(data_energymax, lin_model, [-60, 1]) #wie curve fit, beta0 = [..., ...] entspricht p0 (startwerte)

out = odr_energymax.run() # run the regression

params_energymax = out.beta
errors_energymax = out.sd_beta

for name, value, error in zip('ab', params_energymax, errors_energymax):
 print(f'{name} = {value:.6f} +- {error:.6f}')


energieverlust = - params_energymax[0]
print("energieverlust : ", energieverlust, "MeV / cm" = energieverlust/100, "MeV/m")

plt.figure(constrained_layout = True)
plt.errorbar(nom(eff_length), nom(energymax), xerr = std(eff_length), yerr = std(energymax), fmt = "x", label = "Energie mit Fehlerbalken")
plt.plot(x, lin(params_energymax, x), "-", label = "Ausgleichsgerade")
plt.xlim(x_min - 0.25, x_max + 0.25)
plt.xlabel("$x / \\unit{\\cm}$")
plt.ylabel("$E / \\unit{\\mega\\electronvolt}$")
plt.legend()
plt.savefig("build/reichweite_6cm_energymax.pdf")