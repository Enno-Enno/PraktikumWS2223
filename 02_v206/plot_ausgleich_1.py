import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat


t, temp_k, druck_k, temp_w, druck_w, leistung = np.genfromtxt("messdaten.txt", unpack=True)

for i,value in enumerate(temp_k):
    temp_k[i] += 273.15
    temp_w[i] += 273.15
#umrechnung von Celsius in K

def function_1(t, a, b, c) :
    return (a*t**2 + b*t + c)

def function_1_diff_quot(t, a, b) :
    return(2*a*t + b)

gew_zeiten = [3, 9, 15, 21]

params_k, covariance_matrix_k = curve_fit(function_1, t, temp_k)
params_w, covariance_matrix_w = curve_fit(function_1, t, temp_w)

errors_k = np.sqrt(np.diag(covariance_matrix_k))
errors_w = np.sqrt(np.diag(covariance_matrix_w))

print("error kalt: ", errors_k)
print("error warm: ", errors_w)

print("Funktion 1 für kalt:")
for name, value in zip('abc', params_k):
    print(f"{name} = {value:8.8f}")

print("Funktion 1 für warm:")
for name, value in zip('abc', params_w):
    print(f"{name} = {value:8.8f}")


#plot (auskommentiert damit das alles schneller läuft hihi):

x=np.linspace(0, 25, 1000)
plt.plot(t, temp_k, "x", label="$T_{{\\text{k}}}$")
plt.plot(t, temp_w, "x", label="$T_{{\\text{w}}}$")
plt.plot(x, function_1(x, *params_k), "-", label = "Funktion 1 für $T_{{\\text{k}}}$")
plt.plot(x, function_1(x, *params_w), "-", label = "Funktion 1 für $T_{{\\text{w}}}$")
plt.grid()
plt.legend()
plt.xlabel("$t / \\unit{{\\minute}}$")
plt.ylabel("$T/ \\unit{{\\kelvin}}$")
plt.savefig("build/plot_ausgleich_1.pdf")
#min-K- Diagramm


#Funktion 1 für kalt:
#a = 0.01497863  
#b = -1.26058547 
#c = 295.01282051
#Funktion 1 für warm:
#a = -0.02154457 
#b = 1.62675092  
#c = 293.57844933

#error kalt:  
# [0.00073754 
#  0.01908795 
#  0.1030449 ]
#error warm:  
# [0.00062077
#  0.01606575
#  0.08672976]

a_k = ufloat(0.01497863  , 0.00073754)
b_k = ufloat(-1.26058547 , 0.01908795)
c_k = ufloat(295.01282051, 0.1030449 )

a_w = ufloat(-0.02154457 , 0.00062077)
b_w = ufloat(1.62675092  , 0.01606575)
c_w = ufloat(293.57844933, 0.08672976)

#a in K/(min)^2
#b in K/min
#c in K

function_1_diff_quot_k_0 = function_1_diff_quot(gew_zeiten[0], a_k, b_k)
function_1_diff_quot_k_1 = function_1_diff_quot(gew_zeiten[1], a_k, b_k)
function_1_diff_quot_k_2 = function_1_diff_quot(gew_zeiten[2], a_k, b_k)
function_1_diff_quot_k_3 = function_1_diff_quot(gew_zeiten[3], a_k, b_k)

function_1_diff_quot_w_0 = function_1_diff_quot(gew_zeiten[0], a_w, b_w)
function_1_diff_quot_w_1 = function_1_diff_quot(gew_zeiten[1], a_w, b_w)
function_1_diff_quot_w_2 = function_1_diff_quot(gew_zeiten[2], a_w, b_w)
function_1_diff_quot_w_3 = function_1_diff_quot(gew_zeiten[3], a_w, b_w)

print("diff_quot k0: ", function_1_diff_quot_k_0)
print("diff_quot k1: ", function_1_diff_quot_k_1)
print("diff_quot k2: ", function_1_diff_quot_k_2)
print("diff_quot k3: ", function_1_diff_quot_k_3)

print("diff_quot w0: ", function_1_diff_quot_w_0)
print("diff_quot w1: ", function_1_diff_quot_w_1)
print("diff_quot w2: ", function_1_diff_quot_w_2)
print("diff_quot w3: ", function_1_diff_quot_w_3)

#diff_quot k0:  -1.171+/-0.020
#diff_quot k1:  -0.991+/-0.023
#diff_quot k2:  -0.811+/-0.029
#diff_quot k3:  -0.630+/-0.040

#diff_quot w0:  1.497+/-0.016
#diff_quot w1:  1.239+/-0.020
#diff_quot w2:  0.980+/-0.025
#diff_quot w3:  0.722+/-0.031

#diff_quot in K/min


#bestimmung nu_real:

factor = ufloat(3*4190 + 750, 0)

n_0  = ufloat(7200.0, 0) 
n_1  = ufloat(7360.0, 0) 
n_2  = ufloat(7376.0, 0) 
n_3  = ufloat(7240.0, 0)
#bestimmung von Arbeit N -> s. rechnungen gueteziffer

def guete(factor, n, quot):
    return(factor * quot / n)

nu_real_0 = guete(factor, n_0, function_1_diff_quot_w_0)
nu_real_1 = guete(factor, n_1, function_1_diff_quot_w_1)
nu_real_2 = guete(factor, n_2, function_1_diff_quot_w_2)
nu_real_3 = guete(factor, n_3, function_1_diff_quot_w_3)

print("reale Gueteziffern:")
print("nu real 0: ", nu_real_0)
print("nu real 1: ", nu_real_1)
print("nu real 2: ", nu_real_2)
print("nu real 3: ", nu_real_3)
#nu real 0:  2.770+/-0.031
#nu real 1:  2.242+/-0.035
#nu real 2:  1.77+/-0.04
#nu real 3:  1.33+/-0.06

#Abweichung nu:

#nu ideal: 
# [45.85384615
#  14.1875       
#   9.29228487
#   7.39883721] -> s. rechn. guetez.

nu_ideal_0 = 45.85384615
nu_ideal_1 = 14.1875    
nu_ideal_2 =  9.29228487
nu_ideal_3 =  7.39883721

nu_abw_0 = nu_real_0 / nu_ideal_0
nu_abw_1 = nu_real_1 / nu_ideal_1
nu_abw_2 = nu_real_2 / nu_ideal_2
nu_abw_3 = nu_real_3 / nu_ideal_3

print("Abweichungen Nu: ")
print("Abw 0: ", nu_abw_0)
print("Abw 1: ", nu_abw_1)
print("Abw 2: ", nu_abw_2)
print("Abw 3: ", nu_abw_3)

#Abweichungen Nu:
#Abw 0:  0.0604+/-0.0007
#Abw 1:  0.1580+/-0.0025
#Abw 2:  0.191+/-0.005
#Abw 3:  0.180+/-0.008




#bestimmung verdampfungswärme L:

r = ufloat(8.314, 0) #gas konst
#in J/(mol*K)
m=ufloat(-2001.8141, 111.7750) # steigung aus plot verdampfungswärme

L = -m*r
print("L in J/mol: ", L)
#L:  (1.66+/-0.09)e+04 in J/mol 

mol_masse = ufloat(120.91, 0) #molare Masse von Gas in g/mol
L= L / mol_masse
print("L in J/g: ", L)

#L in J/mol:  (1.66+/-0.09)e+04
#L in J/g:  138+/-8




# bestimmung Massendurchsatz

massendurchsatz_0 = 1/L * factor * function_1_diff_quot_k_0
massendurchsatz_1 = 1/L * factor * function_1_diff_quot_k_1
massendurchsatz_2 = 1/L * factor * function_1_diff_quot_k_2
massendurchsatz_3 = 1/L * factor * function_1_diff_quot_k_3
#in g/J * J/K * K/min = g/min 
print("Massenfurchtsatz in g/min 0: ", massendurchsatz_0)
print("Massenfurchtsatz in g/min 1: ", massendurchsatz_1)
print("Massenfurchtsatz in g/min 2: ", massendurchsatz_2)
print("Massenfurchtsatz in g/min 3: ", massendurchsatz_3)

# Massenfurchtsatz in g/min 0:  -113+/-7
# Massenfurchtsatz in g/min 1:  -96+/-6
# Massenfurchtsatz in g/min 2:  -79+/-5
# Massenfurchtsatz in g/min 3:  -61+/-5




# mechanische Leiste N_mech:

for i,value in enumerate(druck_k):
    druck_k[i] *= 100000
    druck_w[i] *= 100000
#umrechnung bar in Pa


#bestimme druck im kalten reservoir zu gew_zeiten:

rho_0 = ufloat(5.51, 0) #in g/L = g/(dm)^3 = 10^3 g/m^3
#umwandlung in g/m^3:
rho_0 *= 10**3
#in g/m^3

T_0 = ufloat(273.15, 0) # in K

p_0 = ufloat(100000, 0) # in Pa

rho_k = rho_0 * T_0 * druck_k/(temp_k * p_0) # in g/m^3

print("rho: ", rho_k)
#rho:  
# [24543.13300492611+/-0 20466.517083120856+/-0 22605.388632872502+/-0
# 22713.937918024356+/-0 23342.25142167844+/-0 23439.191036511504+/-0
# 22997.911442958848+/-0 21504.553580763193+/-0 21060.787126115094+/-0
# 21134.72353870458+/-0 20141.62599049128+/-0 20212.810390528357+/-0
# 19210.081191278143+/-0 18736.253779121467+/-0 18259.383050847457+/-0
# 17773.077294685987+/-0 17824.103534900412+/-0 17327.507825148405+/-0
# 16834.476456792352+/-0 16332.680412371132+/-0 16374.141432456934+/-0
# 15862.852444121389+/-0 15349.328719723184+/-0 15382.946523088152+/-0
# 15411.07405375754+/-0 15444.96316657504+/-0]

kappa = ufloat(1.14, 0)

n_mech_3  = 1/(kappa - 1) * (druck_w[ 3] * (druck_k[ 3]/druck_w[ 3])**(1/kappa) - druck_k[ 3]) * 1/rho_k[ 3] * massendurchsatz_0
n_mech_9  = 1/(kappa - 1) * (druck_w[ 9] * (druck_k[ 9]/druck_w[ 9])**(1/kappa) - druck_k[ 9]) * 1/rho_k[ 9] * massendurchsatz_1
n_mech_15 = 1/(kappa - 1) * (druck_w[15] * (druck_k[15]/druck_w[15])**(1/kappa) - druck_k[15]) * 1/rho_k[15] * massendurchsatz_2
n_mech_21 = 1/(kappa - 1) * (druck_w[21] * (druck_k[21]/druck_w[21])**(1/kappa) - druck_k[21]) * 1/rho_k[21] * massendurchsatz_3
#n_mech in 1 * Pa * m^3/g * g/min = Pa * m^3 / min = kg /(m* s^2) * m^3 /min = kg* m^2 /(s^2 * min)

n_mech_3  /= 60
n_mech_9  /= 60
n_mech_15 /= 60
n_mech_21 /= 60
#umrechnung kg* m^2 /(s^2 * min) in kg* m^2 /(s^3) = W


print("mechanische leistung nach 3s:", n_mech_3)
print("mechanische leistung nach 9s:", n_mech_9)
print("mechanische leistung nach 15s:", n_mech_15)
print("mechanische leistung nach 21s:", n_mech_21)

#mechanische leistung nach  3s: -13.3+/-0.8
#mechanische leistung nach  9s: -19.9+/-1.2
#mechanische leistung nach 15s: -25.3+/-1.7
#mechanische leistung nach 21s: -25.5+/-2.0

#leistungsaufnahme -> s. rechnungen g.z.

leisten_notaufnahme_0  =  7200.0 / 60
leisten_notaufnahme_1  =  7360.0 / 60
leisten_notaufnahme_2  =  7376.0 / 60
leisten_notaufnahme_3  =  7240.0 / 60
#umrechnung von J//min in W


print("leisten_notaufnahme_0 : ", leisten_notaufnahme_0)
print("leisten_notaufnahme_1 : ", leisten_notaufnahme_1)
print("leisten_notaufnahme_2 : ", leisten_notaufnahme_2)
print("leisten_notaufnahme_3 : ", leisten_notaufnahme_3)

# leisten_notaufnahme_0 :  120.0
# leisten_notaufnahme_1 :  122.66666666666667
# leisten_notaufnahme_2 :  122.93333333333334
# leisten_notaufnahme_3 :  120.66666666666667

abweichung_lesitung_0 = n_mech_3  / leisten_notaufnahme_0
abweichung_lesitung_1 = n_mech_9  / leisten_notaufnahme_1
abweichung_lesitung_2 = n_mech_15 / leisten_notaufnahme_2
abweichung_lesitung_3 = n_mech_21 / leisten_notaufnahme_3

print("abweichung_lesitung_0. ", abweichung_lesitung_0)
print("abweichung_lesitung_1. ", abweichung_lesitung_1)
print("abweichung_lesitung_2. ", abweichung_lesitung_2)
print("abweichung_lesitung_3. ", abweichung_lesitung_3)

#abweichung_lesitung_0 in % :  -0.111+/-0.006
#abweichung_lesitung_1 in % :  -0.162+/-0.010
#abweichung_lesitung_2 in % :  -0.206+/-0.014
#abweichung_lesitung_3 in % :  -0.211+/-0.017