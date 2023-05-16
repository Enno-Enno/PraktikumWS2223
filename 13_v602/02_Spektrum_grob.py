import numpy as np
import matplotlib.pyplot as plt

#Daten sammeln
theta_2, R_Impulse_s =  np.genfromtxt("v602_messungen/ohne_detail.txt", unpack=True)
theta = theta_2 / 2

print(len(theta))
for index, shit in enumerate(theta[:25]):
    if index < 11 :
        print(f"{theta[index]} & {R_Impulse_s[index]} \t & {theta[index+25]} & {R_Impulse_s[index+25]} \t & {theta[index+50]} & {R_Impulse_s[index+50]} \t& {theta[index+75]} & {R_Impulse_s[index+75]} \t \t& {theta[index+100]} & {R_Impulse_s[index+100]}\\\\")
    else:
        print(f"{theta[index]} & {R_Impulse_s[index]} \t & {theta[index+25]} & {R_Impulse_s[index+25]} \t & {theta[index+50]} & {R_Impulse_s[index+50]} \t& {theta[index+75]} & {R_Impulse_s[index+75]} &  & \\\\")
        




#Plot
plt.figure(constrained_layout=True)
plt.plot(theta, R_Impulse_s, "x", label="Emissionsspektrum")
plt.plot(12.0,247,"rx", label="Bremsberg")
#Beschriftungen
plt.xlabel("$\\theta / \\unit{{\degree}}$")
plt.ylabel("$N / \\frac{{1}}{{5\\unit{{\\s}}}}$")

plt.legend()

plt.savefig("build/02_plot.pdf")
