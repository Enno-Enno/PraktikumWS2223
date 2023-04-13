import numpy as np

c = 2730

nu1 = 1 * 10**6
nu2 = 2 * 10**6
nu3 = 4 * 10**6

wavelength1 = c / nu1
wavelength2 = c / nu2
wavelength3 = c / nu3


period1 = 1/nu1
period2 = 1/nu2
period3 = 1/nu3

print("lamda: ", wavelength1, wavelength2, wavelength3)
print("periode: ", period1, period2, period3)

#lamda:  0.00273 0.001365 0.0006825
#periode:  1e-06 5e-07 2.5e-07