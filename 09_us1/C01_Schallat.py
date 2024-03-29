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

time_A_korr= time_A -1
time_B_korr= time_B -1

speed_a= np.zeros(7)
speed_b= np.zeros(7)
speed_Block= (2*(x_Block-1)/60)*10 ** (-3)/(10** (-6))
print("speed_Block: ",speed_Block)
for index, N in enumerate(Nr_time):
    speed_a[index] =2* x_loch_a[N-1]/time_A_korr[index]* 10 ** (-3)/(10** (-6)) # millimeter per micro second -> m/s
    speed_b[index] =2* x_loch_b[N-1]/time_B_korr[index]* 10 ** (-3)/(10** (-6))


print("Tabelle Laufzeiten")
for index, A in enumerate(time_A):
    print("{:.0f}".format(Nr_time[index]), "\t& ", "{:.0f}".format(time_A[index]) , "\t &","\t& ", "{:.0f}".format(time_A_korr[index]) , "\t &", "{:.0f}".format(time_B[index]) ,"\t& ", "{:.0f}".format(time_B_korr[index]) , "\t &","\t &", "{:.0f}".format(speed_a[index]),"\t &", "{:.0f}".format(speed_b[index]), "\t \\\\")


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

Nr, x_schall_b, x_schall_a = np.genfromtxt("C01d_x-Schall.txt", unpack=True)
s1 = 0.5 * 2730 * 1e-3
print("s1:",s1)
x_schall_b_korr = x_schall_b - s1
x_schall_a_korr = x_schall_a - s1

x_Block_schall = 81.5
x_Block_schall_korr = x_Block_schall - s1

D_schall= x_Block_schall_korr - x_schall_a_korr - x_schall_b_korr

print("Tabelle Schalldistanzen")
for index, A in enumerate(Nr):
    print("{:.0f}".format(Nr[index]), "\t& ", "{:.1f}".format(x_schall_a[index]) , "\t &", "{:.1f}".format(x_schall_a_korr[index]) ,#
    "\t &", "{:.1f}".format(x_schall_b[index]),"\t &", "{:.1f}".format(x_schall_b_korr[index]),"\t &",#
    "{:.1f}".format(D_schall[index]), "\t &","{:.1f}".format(D_loch[index]), "\t \\\\")

print("x_Block_schall_korr:",x_Block_schall_korr)
print("x_Block:", x_Block)

tb_Block = 60.2
x_bb, tb_schall_A = np.genfromtxt("C02c_t_schall_A.txt", unpack=True)
x_bb, tb_schall_B = np.genfromtxt("C02c_t_schall_B.txt", unpack=True)
x_bb = np.flip(x_bb)
tb_schall_A = np.flip(tb_schall_A)
tb_schall_B = np.flip(tb_schall_B)

t1 = 1
xb_schall_Block= 2730 * 0.5 *(tb_Block - t1) *1e-6 *1e3
xb_schall_A = 2730 * 0.5 *(tb_schall_A - t1) *1e-6 *1e3
xb_schall_B = 2730 * 0.5 *(tb_schall_B - t1) *1e-6 *1e3
Db_schall = xb_schall_Block - xb_schall_A - xb_schall_B


print("Tabelle B-scan")
for index, x in enumerate(x_bb):
    print("{:.0f}".format(x_bb[index]), "\t&", tb_schall_A[index], "\t&", tb_schall_B[index], "\t&", 
    "{:.1f}".format(xb_schall_A[index]), "\t&", 
    "{:.1f}".format(xb_schall_B[index]), "\t&", 
    "{:.1f}".format(Db_schall[index]), "\t\\\\")

print("xb_schall_Block:",xb_schall_Block)
# 
# 
# 