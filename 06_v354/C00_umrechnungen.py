import numpy as np


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
#print(time, time_micro, amplitude)
# time in s: [0.00e+00 1.40e-05 2.60e-05 3.80e-05 5.20e-05 6.40e-05 7.80e-05 9.20e-05 1.04e-04 1.18e-04 1.30e-04 1.44e-04 1.56e-04 1.70e-04] 
# time in micros: [  0.  14.  26.  38.  52.  64.  78.  92. 104. 118. 130. 144. 156. 170.]
# ampl: [2.8 2.4 2.  1.7 1.5 1.2 1.1 1.  0.9 0.8 0.7 0.6 0.4 0.4]



#Aufgabe b und c
spannung, schwingdauer, delta_t = np.genfromtxt("messdaten/spannung_phase_raw.txt", unpack=True)

timediv_cd = 50 * 10**(-6) # in sekunden
voltsdiv_cd = 0.5 # in volt
for index, value in enumerate(spannung):
    if index >= 1:
        timediv_cd = 5 *10**(-6)
        if index >= 5:
            voltsdiv_cd = 1
            if index >= 19:
                voltsdiv_cd = 0.5
                if index >= 22:
                    voltsdiv_cd = 0.2
    # print(index, ": timediv: ", timediv_cd, "voltsdiv: ", voltsdiv_cd) # sollte so richtig sein ->s.u. zum vergleich 
    spannung[index] *= voltsdiv_cd
    schwingdauer[index] *= timediv_cd
    delta_t[index] *= timediv_cd
    # print(index, ": spannung", spannung[index], "schwdauer: ", schwingdauer[index], "delta t: ", delta_t[index]) # passt auch hoffentlich s.u.



#U_c T delta_t index
# 1.7 1.5 0.0     0
# 1.8 7.7 0.2   /  1 
# 1.7 5.2 0.4     2 
# 2.2 3.9 0.3     3 
# 3.4 3.1 0.2     4 
# 1.0 2.7 0.3   /  5 
# 1.3 2.5 0.4     6 
# 1.4 2.5 0.4     7 
# 1.5 2.4 0.5     8 
# 1.6 2.3 0.5     9 
# 1.5 2.3 0.6    10
# 1.4 2.2 0.7    11
# 1.3 2.2 0.7    12
# 1.2 2.1 0.8    13
# 1.0 2.1 0.8    14
# 0.9 2.0 0.8    15
# 0.8 1.9 0.9    16
# 0.8 1.8 0.9    17
# 0.5 1.7 0.8    18
# 1.3 1.6 0.9  /  19
# 1.0 1.4 0.8    20
# 0.7 1.3 0.7    21
# 1.5 1.2 0.6  /  22
# 1.2 1.1 0.6    23

#0 : timediv:  4.9999999999999996e-05 voltsdiv:  0.5
#1 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#2 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#3 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#4 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#5 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#6 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#7 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#8 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#9 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#10 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#11 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#12 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#13 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#14 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#15 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#16 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#17 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#18 : timediv:  4.9999999999999996e-06 voltsdiv:  1
#19 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#20 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#21 : timediv:  4.9999999999999996e-06 voltsdiv:  0.5
#22 : timediv:  4.9999999999999996e-06 voltsdiv:  0.2
#23 : timediv:  4.9999999999999996e-06 voltsdiv:  0.2

# 0 : spannung 0.85 schwdauer:  7.5e-05 delta t:  0.0
# 1 : spannung 0.9 schwdauer:  3.85e-05 delta t:  1e-06
# 2 : spannung 0.85 schwdauer:  2.6e-05 delta t:  2e-06
# 3 : spannung 1.1 schwdauer:  1.9499999999999996e-05 delta t:  1.4999999999999998e-06
# 4 : spannung 1.7 schwdauer:  1.55e-05 delta t:  1e-06
# 5 : spannung 1.0 schwdauer:  1.35e-05 delta t:  1.4999999999999998e-06
# 6 : spannung 1.3 schwdauer:  1.2499999999999999e-05 delta t:  2e-06
# 7 : spannung 1.4 schwdauer:  1.2499999999999999e-05 delta t:  2e-06
# 8 : spannung 1.5 schwdauer:  1.1999999999999999e-05 delta t:  2.4999999999999998e-06
# 9 : spannung 1.6 schwdauer:  1.1499999999999998e-05 delta t:  2.4999999999999998e-06
# 10 : spannung 1.5 schwdauer:  1.1499999999999998e-05 delta t:  2.9999999999999997e-06
# 11 : spannung 1.4 schwdauer:  1.1e-05 delta t:  3.4999999999999995e-06
# 12 : spannung 1.3 schwdauer:  1.1e-05 delta t:  3.4999999999999995e-06
# 13 : spannung 1.2 schwdauer:  1.05e-05 delta t:  4e-06
# 14 : spannung 1.0 schwdauer:  1.05e-05 delta t:  4e-06
# 15 : spannung 0.9 schwdauer:  9.999999999999999e-06 delta t:  4e-06
# 16 : spannung 0.8 schwdauer:  9.499999999999999e-06 delta t:  4.5e-06
# 17 : spannung 0.8 schwdauer:  9e-06 delta t:  4.5e-06
# 18 : spannung 0.5 schwdauer:  8.499999999999998e-06 delta t:  4e-06
# 19 : spannung 0.65 schwdauer:  8e-06 delta t:  4.5e-06
# 20 : spannung 0.5 schwdauer:  6.999999999999999e-06 delta t:  4e-06
# 21 : spannung 0.35 schwdauer:  6.5e-06 delta t:  3.4999999999999995e-06
# 22 : spannung 0.30000000000000004 schwdauer:  5.999999999999999e-06 delta t:  2.9999999999999997e-06
# 23 : spannung 0.24 schwdauer:  5.5e-06 delta t:  2.9999999999999997e-06