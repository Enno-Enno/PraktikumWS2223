import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

U, I = np.genfromtxt("C03_Kennlinie.txt", unpack=True) # U in Volt I in milli Ampere

I = I * 1000 # I in micro Ampere

gradient = np.zeros(len(I))
for index in np.arange(1,len(I)):
    gradient[index-1] = (I[index] - I[index-1]) / (U[index] - U[index-1])





print("U, gradient")
for index in np.arange(0,len(I)):
    print(index, U[index], I[index], gradient[index])

# print(gradient[:4])


plt.plot(U, I, "x")


plt.savefig("build/C03_plot.pdf")