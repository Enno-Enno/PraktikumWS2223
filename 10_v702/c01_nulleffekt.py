import numpy as np

x, count = np.genfromtxt("messung_c01_nulleffekt.txt", unpack = True)

count_vanadium = count # anzahl pro 35s
count_silber = np.zeros(len(count)) #anzahl pro 35s

for index, value in enumerate(count):
    count_silber = count * 10/35 #umrechnung zu anzahl pro 10 sekunden
#print(count_silber)


#durchschnittlicher nulleffekt + fehler vanadium je 35 sekunden:
mean_vanadium = np.mean(count_vanadium)
std_vanadium = np.std(count_vanadium)

print("nulleffekt beim vanadium zerfall je 35 sekunden: ", mean_vanadium, "+- ", std_vanadium)
#nulleffekt beim vanadium zerfall je 35 sekunden:  14.3125 +-  3.459023525505428



#durchschnittlicher nulleffekt + fehler silber je 10 sekunden:
mean_silber = np.mean(count_silber)
std_silber = np.std(count_silber)

print("nulleffekt beim silber zerfall je 10 sekunden: ", mean_silber, "+- ", std_silber)
#nulleffekt beim silber zerfall je 10 sekunden:  4.089285714285714 +-  0.9882924358586936

