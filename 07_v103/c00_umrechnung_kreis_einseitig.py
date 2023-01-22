import numpy as np

x, d0, dm = np.genfromtxt("messdaten/kreis_einseitig.txt", unpack = True)

x_cm = np.zeros(len(x))
x_m = np.zeros(len(x))
delta_d = np.zeros(len(x))
delta_d_mm = np.zeros(len(x))

for index, value in enumerate(x): 
    x_cm[index] = value 
    x_m[index] = value / 100 # x in m
    delta_d[index] = (d0[index] -dm[index]) * 0.01 * 10**(-3) # delta_d in m
    delta_d_mm[index] = d0[index] -dm[index]

print("x in cm: ", x_cm)
print("x in meter: ", x_m)
print("delta d in meter: ", delta_d)
print("delta d in 0.01 mm: ", delta_d_mm)
# x in meter:  [0.49 0.47 0.45 0.43 0.41 0.39 0.37 0.35 0.33 0.31 0.29 0.27 0.25 0.23
#  0.21 0.19 0.17 0.15 0.13 0.11 0.09 0.07 0.05 0.03]
# delta d in meter:  [1.61e-03 1.52e-03 1.37e-03 1.23e-03 1.19e-03 1.08e-03 1.00e-03 9.30e-04
#  8.50e-04 7.80e-04 6.90e-04 6.10e-04 5.40e-04 4.70e-04 4.10e-04 3.30e-04
#  2.80e-04 2.20e-04 1.70e-04 1.30e-04 9.00e-05 6.00e-05 4.00e-05 2.00e-05]
# delta d in 0.01 mm:  [161. 152. 137. 123. 119. 108. 100.  93.  85.  78.  69.  61.  54.  47.   
#   41.  33.  28.  22.  17.  13.   9.   6.   4.   2.]
