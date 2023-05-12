import numpy as np
import matplotlib.pyplot as plt

#Daten sammeln
theta_2, R_Impulse_s =  np.genfromtxt("v602_messungen/BraggBedingung.txt", unpack=True)

#print(theta_2,R_Impulse_s)






#Plot
plt.figure(constrained_layout=True)
plt.plot(theta_2, R_Impulse_s, "x")

plt.savefig("build/01_plot.pdf")
