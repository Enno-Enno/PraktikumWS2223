import numpy as np
import matplotlib.pyplot as plt

print("B03-----------------------------------------------------------------")
x_6, magnetfeld_6 = np.genfromtxt("messdaten/Spulenpaar/6cm.txt", unpack=True)
x_12, magnetfeld_12 = np.genfromtxt("messdaten/Spulenpaar/12cm.txt", unpack=True)
x_24, magnetfeld_24 = np.genfromtxt("messdaten/Spulenpaar/24cm.txt", unpack=True)

x_6_innen = x_6[:4]
magnetfeld_6_innen = magnetfeld_6[:4]
mw_6 = np.mean(magnetfeld_6[:4])* np.ones(4)
mw_12 = np.mean(magnetfeld_12[7:])* np.ones(7)
mw_24 = np.mean(magnetfeld_24[:13])* np.ones(13)

mw_a_6 = np.mean(magnetfeld_6[4:]   ) * np.ones(len(magnetfeld_6[4:]))
mw_a_12 = np.mean(magnetfeld_12[:7] ) * np.ones(7)
mw_a_24 = np.mean(magnetfeld_24[13:]) * np.ones(2)



print("Hier entsteht der erste Plot")
#plt.figure(constrained_layout=True)
fig, (ax6, ax12, ax24) = plt.subplots(3,1, constrained_layout=True, sharey=True, figsize=(7,9))

#plt.subplot(3,1,1) # Magnetfeld innerhalb der Spulen 6 cm
ax6.plot(x_6[:4], magnetfeld_6[:4], 'x', label="Magnetfeldstärke innen")
ax6.plot(x_6[:4], mw_6, label="$\\overline{{B_i}}$")
ax6.plot(x_6[4:], magnetfeld_6[4:], 'x', label="Magnetfeldstärke außen")
ax6.plot(x_6[4:], mw_a_6, label="$\\overline{{B_a}}$")
ax6.grid()
ax6.set_title("$\\qty{{6}}{{cm}}$ Spulenabstand")
ax6.set_xlabel("$x/ \\unit{{cm}}$")
ax6.set_ylabel("B/ \\unit{{\\milli\\tesla}}")
ax6.legend()

#plt.subplot(3,1,2) # Magnetfeld innerhalb der Spulen 12 cm
ax12.grid()
ax12.plot(x_12[7:], magnetfeld_12[7:], 'x', label="Magnetfeldstärke innen")
ax12.plot(x_12[7:], mw_12, label="$\\overline{{B_i}}$")
ax12.plot(x_12[:7], magnetfeld_12[:7], 'x', label="Magnetfeldstärke außen")
ax12.plot(x_12[:7], mw_a_12, label="$\\overline{{B_a}}$")
ax12.set_title("$\\qty{{12}}{{cm}}$ Spulenabstand")
ax12.set_xlabel("$x/ \\unit{{cm}}$")
ax12.set_ylabel("B/ \\unit{{\\milli\\tesla}}")
ax12.legend()


#plt.subplot(2,1,1) # Magnetfeld innerhalb der Spulen 24 cm
ax24.plot(x_24[:13], magnetfeld_24[:13], 'x', label="Magnetfeldstärke innen")
ax24.plot(x_24[:13], mw_24, label="$\\overline{{B_i}}$")
ax24.plot(x_24[13:], magnetfeld_24[13:], 'x', label="Magnetfeldstärke außen")
ax24.plot(x_24[13:], mw_a_24, label="$\\overline{{B_a}}$")
ax24.grid()

ax24.set_title("$\\qty{24}{{\\centi\\meter}}$ Spulenabstand")
ax24.set_xlabel("$x/ \\unit{{cm}}$")
ax24.set_ylabel("B/ \\unit{{\\milli\\tesla}}")
ax24.legend()


plt.savefig("build/B03_innen_Spulenpaar.pdf")

#####
#fig, (ax6, ax12, ax24) = plt.subplots(3,1, constrained_layout=True, sharey=True, figsize=(7,9))
#print("Hier passiert gerade der zweite Plot")
#
##plt.subplot(3,1,1) # Magnetfeld innerhalb der Spulen 6 cm
#ax6.plot(x_6[4:], magnetfeld_6[4:], 'x', label="Magnetfeld außerhalb der Spulen")
#ax6.grid()
#ax6.set_title("$\\qty{{6}}{{cm}}$ Spulenabstand")
#ax6.set_xlabel("$x/ \\unit{{cm}}$")
#ax6.set_ylabel("B/ \\unit{{\\milli\\tesla}}")
#
##plt.subplot(3,1,2) # Magnetfeld außerhalb der Spulen 12 cm
#ax12.grid()
#ax12.plot(x_12[:7], magnetfeld_12[:7], 'x' )
#ax12.set_title("$\\qty{{12}}{{cm}}$ Spulenabstand")
#ax12.set_xlabel("$x/ \\unit{{cm}}$")
#ax12.set_ylabel("B/ \\unit{{\\milli\\tesla}}")
#
#
##plt.subplot(2,1,1) # Magnetfeld innerhalb der Spulen 24 cm
#ax24.plot(x_24[13:], magnetfeld_24[13:], 'x', label="Magnetfeld innerhalb der Spulen")
#ax24.grid()
#
#ax24.set_title("$\\qty{24}{{\\centi\\meter}}$ Spulenabstand")
#ax24.set_xlabel("$x/ \\unit{{cm}}$")
#ax24.set_ylabel("B/ \\unit{{\\milli\\tesla}}")
#
#
#plt.savefig("build/B03_aussen_Spulenpaar.pdf")
#
#
#