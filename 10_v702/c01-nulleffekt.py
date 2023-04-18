import numpy as np

x, null-count = np.genfromtxt("messung-nulleffekt.txt", unpack = True)

for index, value in enumerate(count):
    count[index] /= 35 # umrechnung von zerfall pro 35s zu ZERFALL PRO SEKUNDE

#durchschnittlicher nulleffekt je sekunde:
nulleffekt = 0