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
def Energie(theta_deg):
    theta = theta_deg *(2*np.pi)/(360)
    h = const.h
    c = const.c
    d = 201.4e-12
    lam = 2 *d * unp.sin(theta)
    # print(f"lambda = {lam} m bei theta = {theta_deg} ")
    E_J = (h * c)/(lam)
    E = E_J / (1.6022e-16)
    lam_pm = lam *1e12
    print(f"({theta_deg})° & ({lam_pm}) pm & {E} keV \\\\ ")


# 02, 03 Kupferspektrum
Winkel_k_beta_Kupfer=ufloat(20.25,0.1)
Winkel_k_alpha_Kupfer=ufloat(20.25,0.1)
Winkel_

Energie(Winkel_k_beta_Kupfer)
Ener
