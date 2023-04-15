import numpy as np
# import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp

x_Block = 80.40
x_loch_a = np.genfromtxt("C01a_x-Loecher.txt", unpack=True)
D_loch = np.genfromtxt("C01b_D-Loecher.txt", unpack=True)
x_loch_b = x_Block - x_loch_a - D_loch

print("Tabelle Schiebelehre")
for index, x in enumerate(x_loch_a):
    print("{:.2f}".format(x), "\t& ", "{:.2f}".format(D_loch[index]), "\t &", "{:.2f}".format(x_loch_b[index]) , "\t \\\\")

