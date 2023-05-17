import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt

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
    lam = 2 *d * unp.sin(theta) # in m
    # print(f"lambda = {lam} m bei theta = {theta_deg} ")
    E_J = (h * c)/(lam) # in J
    E = E_J / (1.6022e-16) # in keV (da e-16 statt e-19)
    lam_pm = lam *1e12
    print(f"{name}: ({theta_deg})° & ({lam_pm}) pm & {E} keV \\\\ ")
    return E
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
theta_2, R_Impulse_s =  np.genfromtxt("v602_messungen/detail.txt", unpack=True)
theta = theta_2 / 2


#### 02, 03 Kupferspektrum
Winkel_k_beta_Kupfer = ufloat(20.25,0.05)
Winkel_k_alpha_Kupfer= ufloat(22.5,0.05)
# Winkel_peak_zink = ufloat(20.2,0.1)
# Winkel_peak_brom = 


E_Cu_beta  =  Energie(Winkel_k_beta_Kupfer , "Kupfer_\\beta")
E_Cu_alpha =  Energie(Winkel_k_alpha_Kupfer, "Kupfer_\\alpha")

P1_links  = ufloat(theta[10] + .23* np.abs(theta[11]-theta[10]), 0.05)
P1_rechts = ufloat(theta[14] + .41* np.abs(theta[15]-theta[14]), 0.05)
P2_links  = ufloat(theta[33] + .01* np.abs(theta[33]-theta[34]), 0.05)
P2_rechts = ufloat(theta[37] + .20* np.abs(theta[37]-theta[38]), 0.05)

print("P1_links :",P1_links )
print("P1_rechts:",P1_rechts)
print("P2_links :",P2_links )
print("P2_rechts:",P2_rechts)

print("Delta_theta_beta:",np.abs(P1_links - P1_rechts))
print("Delta_theta_alpha:",np.abs(P2_links - P2_rechts))

A_beta  = Winkel_k_beta_Kupfer  / np.abs(P1_links - P1_rechts)
A_alpha = Winkel_k_alpha_Kupfer / np.abs(P2_links - P2_rechts)
print("A_beta :", A_beta)
print("A_alpha:", A_alpha)

P1_height = 713.5
P1 = np.array([P1_links.n,P1_rechts.n])
P2_height = 2364.5
P2 = np.array([P2_links.n,P2_rechts.n])
E_grenz = Energie(ufloat(5.4,0.05), "Grenzwinkel")
U_B = 35000 #Volt
print(f"Erwartete Grenzwellenlänge = {(const.h * const.c)/(const.e * U_B)* 10 **12} pm"  )

# for index, shit in enumerate(theta_zr):
    # print(f"{index} & {theta_zr[index]} \t& {Impulse_zr[index]} ")

k_zink_n = np.mean(theta_zink[19:23])
k_zink_s = 0.05
k_zink = ufloat(k_zink_n, k_zink_s)

k_brom = ufloat(np.mean(theta_brom[19:27]), 0.05)
k_sr   = ufloat(np.mean(theta_sr[8:14]), 0.05)
k_zr   = ufloat(np.mean(theta_zr[11:20]), 0.05)


E_k_zink =  Energie(k_zink, "Zink")   
E_k_brom =  Energie(k_brom, "Brom")   
E_k_sr   =  Energie(k_sr, "Strontium")
E_k_zr   =  Energie(k_zr, "Zirconium")



####  Absorptions sigmas
E_Abs_Cu = ufloat(8.9805, 0.0010)  # keV
Z_Cu = 29
E_Ryd = 0.0136 # in keV

sigma_Cu_1 = Z_Cu - unp.sqrt(E_Abs_Cu/E_Ryd)
sigma_Cu_2 = Z_Cu - unp.sqrt((4*(E_Abs_Cu -E_Cu_alpha))/(E_Ryd))
sigma_Cu_3 = Z_Cu - unp.sqrt((9*(E_Abs_Cu -E_Cu_beta))/(E_Ryd))
print("sigma_Cu_1:",sigma_Cu_1)
print("sigma_Cu_2:",sigma_Cu_2)
print("sigma_Cu_3:",sigma_Cu_3)

def sigma_k(Z, E_k):
    alpha = const.alpha
    return Z - unp.sqrt( E_k/E_Ryd - (alpha**2 * Z**4)/(4) ) # alpha und E_Ryd passen


print("Sigma_k:")


print("Zink     ", sigma_k(30,E_k_zink) )   
print("Brom     ", sigma_k(35,E_k_brom) )   
print("Strontium", sigma_k(38,E_k_sr  ) )
print("Zirconium", sigma_k(40,E_k_zr  ) )

theorie_zink = 3.55
theorie_brom = 3.85
theorie_sr   = 4.00 
theorie_zr   = 4.10


abw_zink = (theorie_zink - sigma_k(30,E_k_zink)) / theorie_zink
abw_brom = (theorie_brom - sigma_k(35,E_k_brom)) / theorie_brom
abw_sr   = (theorie_sr   - sigma_k(38,E_k_sr  )) / theorie_sr  
abw_zr   = (theorie_zr   - sigma_k(40,E_k_zr  )) / theorie_zr   


print("abw_zink", abw_zink)
print("abw_brom", abw_brom)
print("abw_sr  ", abw_sr  )
print("abw_zr  ", abw_zr  )

Z = np.array([30,35,38,40])
E = np.array([E_k_zink.n ,E_k_brom.n ,E_k_sr.n ,E_k_zr.n] ) * 1000

params, covariance_Matrix = np.polyfit( np.sqrt(E), Z, 1, cov=True)
print(params)
errors = np.sqrt(np.diag(covariance_Matrix))
print(errors)

print(f"a = {params[0]:.3f} \pm {errors[0]:.3f}")
print(f"b = {params[1]:.3f} \pm {errors[1]:.3f}")
a = ufloat(params[0], errors[0])
print(1/a**2)



#Plot
xplot = np.linspace(np.sqrt(E[0]), np.sqrt(E[3]) )
plt.figure(constrained_layout=True)
plt.plot(np.sqrt(E) ,Z, "x", label="Absorptionsenergien")
plt.plot(xplot, params[0]*(xplot) + params[1], label="Ausgleichsrechnung")



plt.xlabel(r"$\sqrt{E_k/ \unit{\eV}} $")
plt.ylabel(r"$Z$")


plt.savefig("build/05_plot.pdf")