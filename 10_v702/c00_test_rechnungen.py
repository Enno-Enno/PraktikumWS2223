import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
import c01_nulleffekt as c01
from scipy.optimize import curve_fit

#print(zerfall_ufl)
# 190.6875+/-3.459023525505428 206.6875+/-3.459023525505428
# 135.6875+/-3.459023525505428 124.6875+/-3.459023525505428
# 101.6875+/-3.459023525505428 97.6875+/-3.459023525505428
#  93.6875+/-3.459023525505428 100.6875+/-3.459023525505428
#  81.6875+/-3.459023525505428 85.6875+/-3.459023525505428
#  61.6875+/-3.459023525505428 57.6875+/-3.459023525505428
#  52.6875+/-3.459023525505428 44.6875+/-3.459023525505428
#  41.6875+/-3.459023525505428 31.6875+/-3.459023525505428
#  44.6875+/-3.459023525505428 22.6875+/-3.459023525505428
#  30.6875+/-3.459023525505428 29.6875+/-3.459023525505428
#  21.6875+/-3.459023525505428 23.6875+/-3.459023525505428
#  21.6875+/-3.459023525505428 18.6875+/-3.459023525505428
#  22.6875+/-3.459023525505428 12.6875+/-3.459023525505428
#  6.6875+/-3.459023525505428  9.6875+/-3.459023525505428
#  8.6875+/-3.459023525505428  17.6875+/-3.459023525505428]

print("ln(190.6875+/-3.459023525505428): ",unp.log(190.6875-3.459023525505428), unp.log(190.6875+3.459023525505428))
#ln(190.6875+/-3.459023525505428):  5.2323296703940425 5.268613149890681
print("ln(6.6875+/-3.459023525505428):  ", unp.log(6.6875-3.459023525505428), unp.log(6.6875+3.459023525505428))
#ln(6.6875+/-3.459023525505428):   1.1720103462356495 2.317131137015496