import numpy as np
import matplotlib.pyplot as plt

#Daten sammeln
theta_2_zink, Impulse_zink =  np.genfromtxt("v602_messungen/abs_zink.txt", unpack=True)
theta_zink = theta_2_zink / 2
theta_2_brom, Impulse_brom =  np.genfromtxt("v602_messungen/abs_brom.txt", unpack=True)
theta_brom = theta_2_brom / 2
theta_2_sr, Impulse_sr =  np.genfromtxt("v602_messungen/abs_sr.txt", unpack=True)
theta_sr = theta_2_sr / 2
theta_2_zr, Impulse_zr =  np.genfromtxt("v602_messungen/abs_zr.txt", unpack=True)
theta_zr = theta_2_zr / 2

print("Zink")
for index, shit in enumerate(theta_zink):
    print(f"{index}    {theta_zink[index]} \t& {Impulse_zink[index]} ")

print("Brom")
for index, shit in enumerate(theta_brom):
    print(f"& {theta_brom[index]} \t& {Impulse_brom[index]} ")

print("Strontium")
for index, shit in enumerate(theta_sr):
    print(f"& {theta_sr[index]} \t& {Impulse_sr[index]} ")

print("Zirconium")
for index, shit in enumerate(theta_zink):
    print(f"& {theta_zink[index]} \t& {Impulse_zink[index]} \\\\")




#Plot
# plt.figure(constrained_layout=True)
# plt.subplot(2,2,1, label="Brom")
# plt.plot(theta_2_brom, Impulse_brom, "x")
# plt.subplot(2,2,2, label="Strontium")
# plt.plot(theta_2_sr, Impulse_sr, "x")
# plt.subplot(2,2,3, label="Zink")
# plt.plot(theta_2_zink, Impulse_zink, "x")
# plt.subplot(2,2,4, label="Zirconium")
# plt.plot(theta_2_zr, Impulse_zr, "x")


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, constrained_layout=True)

ax1.plot(theta_zink, Impulse_zink, "x")
ax1.set_title('Zink')
ax1.set_xlabel('Theta °')
ax1.set_ylabel("$N / \\frac{{1}}{{20\\unit{{\\s}}}}$")
ax1.axvline(20.05, color="k")

ax2.plot(theta_brom, Impulse_brom, "x")
ax2.set_title('Brom')
ax2.set_xlabel('Theta °')
ax2.set_ylabel('$N / \\frac{{1}}{{20\\unit{{\\s}}}}$')
ax2.axvline(13.25, color="k")

ax3.plot(theta_sr, Impulse_sr, "x")
ax3.set_title('Strontium')
ax3.set_xlabel('Theta °')
ax3.set_ylabel('$N / \\frac{{1}}{{20\\unit{{\\s}}}}$')
ax3.axvline(11.05, color="k")

ax4.plot(theta_zr, Impulse_zr, "x")
ax4.set_title('Zirconium')
ax4.set_xlabel('Theta °')
ax4.set_ylabel('$N / \\frac{{1}}{{20\\unit{{\\s}}}}$')
ax4.axvline(10.00, color="k")


plt.savefig("build/04_plot.pdf") 