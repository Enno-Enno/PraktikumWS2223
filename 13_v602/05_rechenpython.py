import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp

# Nehme Energie in keV und gebe einen Winkel in ° aus
def theta(E):
    h = const.h
    c = const.c
    d = 201.4e-12
    E_J = E * 1.6022e-16
    lam = (h *c) / E_J 
    # print("lam",lam)
    # print("d_fn",d)

    tet = np.arcsin(lam / (2 * d)) * 360 /(2*np.pi)
    print("E_fn", E)
    return tet

# Nehme eine effektive Kernzahl und die Schale n und gebe ein Energieniveau in keV aus
# def E(m, n, z_eff):
#     R_inf = 13.6 #eV Rydbergenergie
#     ene = - R* (z_eff**2 * 1/(n))


# Nehme einen Winkel in ° und gebe eine energie in KeV Aus
def Energie(theta_deg, name="kp"):
    theta = theta_deg *(2*np.pi)/(360)
    h = const.h
    c = const.c
    d = 201.4e-12
    lam = 2 *d * unp.sin(theta)
    # print(f"lambda = {lam} m bei theta = {theta_deg} ")
    E_J = (h * c)/(lam)
    E = E_J / (1.6022e-16)
    lam_pm = lam *1e12
    print(f"{name}: ({theta_deg})° & ({lam_pm}) pm & {E} keV \\\\ ")
### sin(theta) ~ 1/E : kleineres theta größeres E

#Daten sammeln
theta_2_zink, Impulse_zink =  np.genfromtxt("v602_messungen/abs_zink.txt", unpack=True)
theta_zink = theta_2_zink / 2
theta_2_brom, Impulse_brom =  np.genfromtxt("v602_messungen/abs_brom.txt", unpack=True)
theta_brom = theta_2_brom / 2
theta_2_sr, Impulse_sr =  np.genfromtxt("v602_messungen/abs_sr.txt", unpack=True)
theta_sr = theta_2_sr / 2
theta_2_zr, Impulse_zr =  np.genfromtxt("v602_messungen/abs_zr.txt", unpack=True)
theta_zr = theta_2_zr / 2

# 02, 03 Kupferspektrum
Winkel_k_beta_Kupfer=ufloat(20.25,0.05)
Winkel_k_alpha_Kupfer=ufloat(22.5,0.05)
# Winkel_peak_zink = ufloat(20.2,0.1)
# Winkel_peak_brom = 

Energie(Winkel_k_beta_Kupfer, "Kupfer_\\beta")
Energie(Winkel_k_alpha_Kupfer, "Kupfer_\\alpha")

# for index, shit in enumerate(theta_zr):
    # print(f"{index} & {theta_zr[index]} \t& {Impulse_zr[index]} ")
# print(theta_zink[19:23], Impulse_zink[19:23])

k_zink_n = np.mean(theta_zink[19:23])
k_zink_s = 0.05
k_zink = ufloat(k_zink_n, k_zink_s)

k_brom = ufloat( np.mean(theta_brom[19:27]), 0.05)
k_sr = ufloat( np.mean(theta_sr[8:14]), 0.05)
k_zr = ufloat( np.mean(theta_zr[8:14]), 0.05)


Energie(k_zink, "Zink")
Energie(k_brom, "Brom")
Energie(k_sr, "Strontium")
Energie(k_zr, "Zirconium")
