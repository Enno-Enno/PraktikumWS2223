import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

I_Heiz = np.array([2.0,2.3,2.5])
I_error = np.ones(len(I_Heiz))* 0.05
I_Heiz = unp.uarray(I_Heiz,I_error) #Frage: Wie kriege ich das hier hin ?#

U_Heiz = np.array([4,5,5])
U_error = np.ones(len(U_Heiz))* 0.5
U_Heiz = unp.uarray(U_Heiz,U_error)

N_WL = 1
f = 0.32
eta = 0.28
sigma = 5.7e-12


T = unp.uarray(np.zeros(len(U_Heiz)),np.zeros(len(U_Heiz)))

for index in np.arange(0,len(U_Heiz)):
    T[index] = ( (I_Heiz[index] * U_Heiz[index]- N_WL)/ (f * eta * sigma))**(1/4)
    print(I_Heiz[index], " & " ,U_Heiz[index], " & " ,f"{T[index].n:.0f} \pm  {T[index].s:.0f} \\\\")


I_s = unp.uarray([40.669,600, 2300],[0.438, 10, 250])# in micro Ampere
print(I_s)

#Umrechnung in Si Einheiten
k_B = 1.381e-23
f = 0.32 / 100**2
j_s = I_s / f * 1e-6 #Umrechnung in Ampere 
h = 6.62607015e-34
e = const.e
m_e = const.m_e


W = - k_B * T * unp.log((h**3 * j_s)/(4*np.pi * e * m_e * k_B **2 * T ** 2))

for index in np.arange(0,len(W)):
    print(f"{T[index].n:.5} \pm {T[index].s:.3}  \t&   {I_s[index].n} \pm {I_s[index].s}   \t& {W[index].n:.3} \pm {W[index].s:.3} \\\\ ")

# print(unp.mean(W)) ## Frage, wie beeinflusst die Standartabweichung der Messwerte die Standartabweichung des Mittelwerts?
W_mean = np.mean(unp.nominal_values(W))
W_stdev = np.sqrt(np.sum(unp.std_devs(W)**2))/3
print(f"{W_mean:.4} \pm {W_stdev:.1}") 
