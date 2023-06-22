import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

#f= 31.850 kHz
print("--------------------")
print("experimentell:")

dy_ohne, dy_mit = np.genfromtxt("teil2_dy.txt", unpack = True)
gd_ohne, gd_mit = np.genfromtxt("teil2_gd.txt", unpack = True)
nd_ohne, nd_mit = np.genfromtxt("teil2_nd.txt", unpack = True)

delta_dy = (dy_ohne - dy_mit) * 5 * 10**(-3)# ohm
delta_gd = (gd_ohne - gd_mit) * 5 * 10**(-3)# ohm
delta_nd = (nd_ohne - nd_mit) * 5 * 10**(-3)# ohm

r_dy = np.mean(delta_dy)
r_gd = np.mean(delta_gd)
r_nd = np.mean(delta_nd)


masse_dy = 14.38 # g
masse_gd = 14.08 # g
masse_nd =  8.48 # g

laenge_dy = 15.2 #cm
laenge_nd = 16.5 #cm
laenge_gd = 16.5 #cm #iguess der aufkleber ist ungünstig

dichte_dy = 7.8  #g/cm^3
dichte_gd = 7.4  #g/cm^3
dichte_nd = 7.24 #g/cm^3

def querschnitt(m, l, rho):
    return(m / (l * rho))

q_dy = querschnitt(masse_dy, laenge_dy, dichte_dy) * 10**2 # mm^2
q_gd = querschnitt(masse_gd, laenge_gd, dichte_gd) * 10**2 # mm^2
q_nd = querschnitt(masse_nd, laenge_nd, dichte_nd) * 10**2 # mm^2

print("eff querschnitte in mm^2:", q_dy, q_gd, q_nd)

def chi(delta_r, q):
    r3 = 998 #ohm
    f = 86.6 #mm^2
    return(2 * delta_r * f / (r3 * q))

chi_dy = chi(r_dy, q_dy)
chi_gd = chi(r_gd, q_gd)
chi_nd = chi(r_nd, q_nd)




print("--------------------")
print("theoretisch:")

# Dy3+-Hülle neun 4f-Elektronen 
# Gd3+- sieben 4f-Elektronen
# Nd3+- drei 4f-Elektronen

S_dy = (7 - 2) * 1/2 #maximal 14/2 = 7 pro schale, 14 = maximale e anzahl
L_dy = np.absolute((3 + 2 + 1 + 0 - 1 - 2 - 3) - (3 + 2)) # erste klammer up, zweite down & negatives vz da down
J_dy = np.absolute(L_dy + S_dy) #mehr als halb voll

S_gd = 7 * 1/2
L_gd = 3 + 2 + 1 + 0 - 1 - 2 - 3 # = 0 aber zur vollständigkeit
J_gd = np.absolute(L_gd + S_gd) #halb voll

S_nd = 3 * 1/2
L_nd = 3 + 2 + 1
J_nd = np.absolute(L_nd - S_nd) #weniger als halb voll

def g_j(J, L, S):
    return (3 * J*(J+1) + S*(S+1) - L*(L+1)) / (2* J*(J+1))

g_j_dy = g_j(J_dy, L_dy, S_dy)
g_j_gd = g_j(J_gd, L_gd, S_gd)
g_j_nd = g_j(J_nd, L_nd, S_nd)

print("g_j", g_j_dy, g_j_gd, g_j_nd) #stimmt :)

mol_masse_dy = 372.998 #g/mol
mol_masse_gd = 362.5   #g/mol
mol_masse_nd = 336.48  #g/mol

z = 2 #sauerstoff voll besetzt, trägt also nicht bei. nur dy, gd, nd tragen durch 2 bei
N_dy = z * const.N_A * dichte_dy / (mol_masse_dy) * 100**(3) #m^3 (vorher cm^3)
N_gd = z * const.N_A * dichte_gd / (mol_masse_gd) * 100**(3) #m^3 (vorher cm^3)
N_nd = z * const.N_A * dichte_nd / (mol_masse_nd) * 100**(3) #m^3 (vorher cm^3)

print("N: ", N_dy, N_gd, N_nd)

def chi_theo(g_j, N, J):
    #N zahl der elemente pro volumeneinheit
    T = 273.15 + 25 #geschätzt 25deg C im Raum
    mu_b = 1/2 * (const.e / const.m_e) * const.hbar
    return(const.mu_0 * mu_b**2 * g_j**2 * N * J* (J+1) /(3 * const.k * T))

theo_dy = chi_theo(g_j_dy, N_dy, J_dy)
theo_gd = chi_theo(g_j_gd, N_gd, J_gd)
theo_nd = chi_theo(g_j_nd, N_nd, J_nd)

print("χ_exp :", chi_dy, chi_gd, chi_nd)
print("χ_theo: ", theo_dy, theo_gd, theo_nd)

# --------------------
# experimentell:
# eff querschnitte in mm^2: 12.128879892037789 11.531531531531531 7.098610413527541
# --------------------
# theoretisch:
# g_j 1.3333333333333333 2.0 0.7272727272727273
# N:  2.5186568253985275e+28 2.4586947102896555e+28 2.591553679410366e+28
# χ_exp : 0.023847639646469573 0.0126919870991984 0.004319153306613226
# χ_theo:  0.024982293146569665 0.013556600454763772 0.0029691740487337625