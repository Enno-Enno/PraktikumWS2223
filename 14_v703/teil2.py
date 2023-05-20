import numpy as np
from uncertainties import ufloat


print("ABLESEN AM OSZI:")
minimum = ufloat(-4.5, 0.5) * 10e-6 #sekunden
null = ufloat(5.0, 0.5) * 10e-6
totzeit_oszi = null - minimum
print("totzeit_oszi", totzeit_oszi, "s")


print("ZWEI QUELLEN METHODE:")

def totzeit(n1, n2, n12):
    return((n1 + n2 - n12)/(n12 **2 - n1 **2 - n2 **2))

full_interval = 67000
time = 120

a = (2 * full_interval + 32042)  / time
b = (1 * full_interval + 38553)  / time
c = (3 * full_interval + 47200)  / time

n1  = ufloat(a, np.sqrt(a))
n2  = ufloat(b, np.sqrt(b))
n12 = ufloat(c, np.sqrt(c))

print("n1: ", n1)
print("n2: ", n2)
print("n12: ", n12)

totzeit_calc = totzeit(n1, n2, n12)
print("totzeit_calc", totzeit_calc)

abweichung_totzeit = (totzeit_oszi - totzeit_calc) / totzeit_calc

print("Abweichung: ", abweichung_totzeit)


# ABLESEN AM OSZI:
# totzeit_oszi (9.5+/-0.7)e-05 s
# ZWEI QUELLEN METHODE:
# n1:  (1.38+/-0.04)e+03
# n2:  880+/-30
# n12:  (2.07+/-0.05)e+03
# totzeit_calc 0.00012+/-0.00006
# Abweichung:  -0.2+/-0.4