import numpy as np
import matplotlib as plt
#import C00_umrechnungen as C00


#Aufgabe a
time, amplitude = np.genfromtxt("messdaten/ampl_ged_schw_raw.txt", unpack=True)
timediv_a_sec = 20 *10**(-6) #in Sekunden
timediv_a_sec_milli = 20 # in millisekunden
voltsdiv_a = 1 #in volt
time_micro = np.zeros(14) 
for index, value in enumerate(time):
    time_micro[index] = time[index] * timediv_a_sec_milli
    time[index] *= timediv_a_sec
    amplitude[index] *= voltsdiv_a
print(time, time_micro, amplitude)
# time in s: [0.00e+00 1.40e-05 2.60e-05 3.80e-05 5.20e-05 6.40e-05 7.80e-05 9.20e-05 1.04e-04 1.18e-04 1.30e-04 1.44e-04 1.56e-04 1.70e-04] 
# time in micros: [  0.  14.  26.  38.  52.  64.  78.  92. 104. 118. 130. 144. 156. 170.]
# ampl: [2.8 2.4 2.  1.7 1.5 1.2 1.1 1.  0.9 0.8 0.7 0.6 0.4 0.4]