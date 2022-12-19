import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

print("B02-----------------------------------------------------------------------------")
x_lang_abgel, magnetfeld_lang = np.genfromtxt("messdaten/Spule/lange_spule.txt", unpack=True)
x_kurz_abgel, magnetfeld_kurz = np.genfromtxt("messdaten/Spule/kurze_spule.txt", unpack=True)

x_sonde = 50

laenge_lang = 16
laenge_kurz = 9

x_lang = x_lang_abgel - x_sonde + laenge_lang/2
x_kurz = x_kurz_abgel - x_sonde + laenge_kurz/2
#anpassung der x-Achse (in cm)

print("x-achsen:")
print("x_lang: ", x_lang)
print("x_kurz: ", x_kurz)
#x-achsen:
#x_lang:  [ 0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.
# 15.5 18. ]
#x_kurz:  [-0.5  0.5  1.5  3.5  4.5  5.5  6.5  7.5  8.5  9.5 10.5 11.5 12.5 13.5
# 14.5 16.5 18.5 20.5 22.5 24.5 26.5 28.5 30.5 32.5 34.5 36.5 38.5 40.5
# 42.5 44.5]

mu_0 = 4 * np.pi *10**(-7) #N/A^2


n_lang = 300  #dim.los
n_kurz = 3400 #dim.los

R_lang = 4.1 / 2 #in cm
R_kurz = 8.5 / 2 #in cm

I_lang = 1   # in A
I_kurz = 0.6 # in A

#def leiterschleife_lang(x, mu_0, n, I, R):
#    return(mu_0/2 * n * I * R**2/(R**2 + x**2)**(3/2)) * 100
#    #eigentlich in N/(A cm), durch Faktor 100 in N/(A m) = T
#
#params_lang, covariance_matrix_lang =  curve_fit(leiterschleife, x_lang, magnetfeld_lang)
#params_kurz, covariance_matrix_kurz =  curve_fit(leiterschleife, x_kurz, magnetfeld_kurz)
#
#errors_lang = np.sqrt(np.diag(covariance_matrix_lang))
#errors_kurz = np.sqrt(np.diag(covariance_matrix_kurz))


#print("Funktion Leiterschleife für lang:")
#for name, value in zip('', params_k):
#    print(f"{name} = {value:8.8f}")

#print("params_kurz: ", params_kurz)
#print("errors_kurz: ", errors_kurz)

#plot lange spule
plt.figure(constrained_layout=True)
plt.plot(x_lang, magnetfeld_lang, 'x', label = "$B_\\text{{lang}}(x)$")
#plt.plot(x_lang, -leiterschleife(x_lang, mu_0, n_lang, I_lang, R_lang), "-", label = "Funktion für Spule mit n Windungen")
plt.axvline(x=8, label = "Wechsel innen / außen")
plt.xlabel("$x/ \\unit{\\cm}$")
plt.ylabel("$B/ \\unit{\\milli\\tesla}$")
plt.grid()
plt.legend()
plt.savefig("build/B02_lange_spule.pdf")

#plot kurze Spule
plt.figure(constrained_layout=True)
plt.plot(x_kurz, magnetfeld_kurz, 'x', label = "$B_\\text{{kurz}}(x)$")
plt.axvline(x=4.5, label = "Wechsel innen / außen")
plt.xlabel("$x/ \\unit{\\cm}$")
plt.ylabel("$B/ \\unit{\\milli\\tesla}$")
plt.grid()
plt.legend()
plt.savefig("build/B02_kurze_spule.pdf")