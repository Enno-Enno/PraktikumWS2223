import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from uncertainties import ufloat
import C05_rechenpython as C05


#Daten sammeln
theta_2, R_Impulse_s =  np.genfromtxt("v602_messungen/detail.txt", unpack=True)
theta = theta_2 / 2

# for index, shit in enumerate(theta):
    # print(f"{theta[index]} \t& {R_Impulse_s[index]} \\\\")

peaks, _ = signal.find_peaks(R_Impulse_s, height=500)
print(peaks)

widths = signal.peak_widths(R_Impulse_s,peaks)
print(widths)

P1_links  = ufloat(theta[10] + .23* np.abs(theta[11]-theta[10]), 0.05)
P1_rechts = ufloat(theta[14] + .41* np.abs(theta[15]-theta[14]), 0.05)
P2_links  = ufloat(theta[33] + .01* np.abs(theta[33]-theta[34]), 0.05)
P2_rechts = ufloat(theta[37] + .20* np.abs(theta[37]-theta[38]), 0.05)
# 
# print("P1_links :",P1_links )
# print("P1_rechts:",P1_rechts)
# print("P2_links :",P2_links )
# print("P2_rechts:",P2_rechts)

# A_beta  = np.abs(P1_links - P1_rechts)
# A_alpha = np.abs(P2_links - P2_rechts)
# print("A_beta :", A_beta)
# print("A_alpha:", A_alpha)

P1_height = 713.5
P1 = np.array([P1_links.n,P1_rechts.n])
P2_height = 2364.5
P2 = np.array([P2_links.n,P2_rechts.n])


#Plot 
plt.figure(constrained_layout=True)
plt.plot(theta, R_Impulse_s, "x")
#Beschriftungen
plt.vlines(P1,0 , P1_height, color="y" ,label=r"$K_{\beta,\text{FWHM}}$")
plt.hlines(P1_height, P1[0], P1[1] , color="y")
plt.vlines(P2,0 , P2_height, color="g" ,label=r"$K_{\alpha,\text{FWHM}}$")
plt.hlines(P2_height, P2[0], P2[1] , color="g")
plt.xlabel(r"$\theta / \unit{\degree}$")
plt.ylabel(r"$N / \frac{1}{5\unit{\s}}$")

plt.grid()
plt.legend()

plt.savefig("build/03_plot.pdf")
