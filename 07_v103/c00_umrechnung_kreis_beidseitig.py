import numpy as np

x, d0, dm = np.genfromtxt("messdaten/kreis_beidseitig.txt", unpack = True)

delta_d = np.zeros(len(x))
delta_d_mm = np.zeros(len(x))

for index, value in enumerate(x): 
    x[index] /= 100 # x in cm
    delta_d[index] = (d0[index] -dm[index]) * 0.01 * 10**(-3) # delta_d in m
    delta_d_mm[index] = d0[index] -dm[index]

print("x in meter: ", x)
print("delta d in meter: ", delta_d)
print("delta d in 0.01 mm: ", delta_d_mm)
# x in meter:  [0.03 0.05 0.07 0.09 0.11 0.13 0.15 0.17 0.19 0.21 0.22 0.23 0.24 0.25
#  0.26 0.27 0.28 0.29 0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 0.4
#  0.41 0.42 0.44 0.46 0.48 0.49]
# delta d in meter:  [0.0e+00 1.0e-05 3.0e-05 3.0e-05 5.0e-05 7.0e-05 8.0e-05 9.0e-05 1.1e-04
#  1.2e-04 1.1e-04 1.3e-04 1.3e-04 1.5e-04 1.6e-04 1.6e-04 1.6e-04 1.6e-04
#  1.7e-04 1.7e-04 1.6e-04 1.5e-04 1.5e-04 1.6e-04 1.6e-04 1.6e-04 1.3e-04
#  1.4e-04 1.6e-04 1.5e-04 1.2e-04 8.0e-05 7.0e-05 8.0e-05]
# delta d in 0.01 mm:  [ 0.  1.  3.  3.  5.  7.  8.  9. 11. 12. 11. 13. 13. 15. 16. 16. 16. 16. 
#  17. 17. 16. 15. 15. 16. 16. 16. 13. 14. 16. 15. 12.  8.  7.  8.]
