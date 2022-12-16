import numpy as np
import matplotlib.pyplot as plt

print("B03-----------------------------------------------------------------")
x_6, magnetfeld_6 = np.genfromtxt("messdaten/Spulenpaar/6cm.txt", unpack=True)
x_12, magnetfeld_12 = np.genfromtxt("messdaten/Spulenpaar/12cm.txt", unpack=True)
x_24, magnetfeld_24 = np.genfromtxt("messdaten/Spulenpaar/24cm.txt", unpack=True)

#x_6_innen = x_6[:4]
#magnetfeld_6_innen = magnetfeld_6[:4]
mw_6  = np.mean(magnetfeld_6[:4]  )
mw_12 = np.mean(magnetfeld_12[7:] )
mw_24 = np.mean(magnetfeld_24[:13])
print("mw_6 :", mw_6 )
print("mw_12:", mw_12)
print("mw_24:", mw_24)

std_6  = np.std(magnetfeld_6[:4]  )
std_12 = np.std(magnetfeld_12[7:] )
std_24 = np.std(magnetfeld_24[:13])
print("std_6 :", std_6 )
print("std_12:", std_12)
print("std_24:", std_24)