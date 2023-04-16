import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp

x_Block = 80.40
x_loch_a = np.genfromtxt("C01a_x-Loecher.txt", unpack=True)
D_loch = np.genfromtxt("C01b_D-Loecher.txt", unpack=True)
x_loch_b = x_Block - x_loch_a - D_loch

print("Tabelle Schiebelehre")
for index, x in enumerate(x_loch_a):
    print("{:.2f}".format(x), "\t& ", "{:.2f}".format(D_loch[index]), "\t &", "{:.2f}".format(x_loch_b[index]) , "\t \\\\")

(Nr_time, time_A, time_B) = np.genfromtxt("C01c_Laufzeiten.txt", unpack=True)
Nr_time = (np.rint(Nr_time)).astype(int)

time_A= time_A -1
time_B= time_B -1

speed_a= np.zeros(7)
speed_b= np.zeros(7)
speed_Block= (2*(x_Block-1)/60)*10 ** (-3)/(10** (-6))
print("speed_Block: ",speed_Block)
for index, N in enumerate(Nr_time):
    speed_a[index] =2* x_loch_a[N-1]/time_A[index]* 10 ** (-3)/(10** (-6)) # millimeter per micro second -> m/s
    speed_b[index] =2* x_loch_b[N-1]/time_B[index]* 10 ** (-3)/(10** (-6))


print("Tabelle Laufzeiten")
for index, A in enumerate(time_A):
    print("{:.0f}".format(Nr_time[index]), "\t& ", "{:.0f}".format(A) , "\t &", "{:.0f}".format(time_B[index]) ,"\t &", "{:.0f}".format(speed_a[index]),"\t &", "{:.0f}".format(speed_b[index]), "\t \\\\")


speeds= np.concatenate((speed_a,speed_b), axis=0)
speed_mean= np.mean(speeds)
speed_std = np.std(speeds)
speed = ufloat(speed_mean,speed_std)
print("speed:", speed)


# plt.plot(Nr_time,speed_a,"x", label="speed a")
# plt.plot(Nr_time,speed_b,"x", label="speed b")
# plt.plot(Nr_time,2730*np.ones(len(Nr_time)), label="Literaturwert")
# plt.legend()
# plt.savefig("build/testfigure.pdf")

