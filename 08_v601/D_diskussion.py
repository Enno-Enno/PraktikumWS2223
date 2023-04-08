import numpy as np
from uncertainties import ufloat
# import matplotlib.pyplot as plt
# import scipy.constants as const

lit = 4.9

messung_c = ufloat(4.94, 0.22)
messung_d = ufloat(4.8, 0.4)

abweichung_c = (messung_c-lit)/messung_c
abweichung_d = (messung_d-lit)/messung_d

print("abwe c: ", abweichung_c)
print("abwe d: ", abweichung_d)

#abwe c:  0.01+/-0.04
#abwe d:  -0.02+/-0.09
