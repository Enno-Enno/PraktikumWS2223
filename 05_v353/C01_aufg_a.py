import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



print("C01-----------------------------------------------------------------")
U_k, t_k = np. genfromtxt("messdaten/A/a_in_kaestchen.txt", unpack=True)

U = U_k * 0.2 # U in Volt
t = t_k * 2  # t in ms
U_inf = 3.81 * 0.2 

print("U_inf:", U_inf)
for index,  zeit in enumerate(t):
    print(zeit, U[index] + U_inf)


#U_ln = np.log(abs(U))

#def U_fit(t, U_0, U_inf, RC):
#    return U_0 * np.exp(-t/ RC) + U_inf


params, cov_matrix = np.polyfit(t , np.log(U + U_inf),deg=1, cov=True)
U_pos = np.log(U + U_inf)
abweichung = np.sqrt(np.diag(cov_matrix))

U_0_neu = U[0] + U_inf
tau = params[0] / np.log(U_0_neu)
tau_abw = abweichung[0] / np.log(U_0_neu)
print("U_0_neu:", U_0_neu)
print("tau = RC_1:", tau) #in ms
print("tau_abw = RC_1_abw:", tau_abw) #in ms

print("params", params)
print("cov_matrix:", cov_matrix)
print("abweichung:", abweichung)
print("np.exp(params[0]*0+ params[1])/np.exp(params[0] * params[0] + params[1]) soll = 1/e",np.exp(params[0]*0+ params[1])/np.exp(params[0] * params[0] + params[1]))


