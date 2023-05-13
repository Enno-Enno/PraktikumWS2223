import numpy as np
import scipy.constants as const


k_alpha = 8.05  # KeV
k_beta = 8.91   # KeV
d = 201.4e-12

k_alpha_J = k_alpha * 1.6022e-16 #Joule
k_beta_J = k_beta * 1.6022e-16   #Joule


h = const.h
c = const.c
# print("h",h)
# print("c",c)
# print("d",d)

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

# lambda_alpha = h * c / k_alpha_J
# lambda_beta = h * c / k_beta_J


theta_alpha = theta(k_alpha)
theta_beta = theta(k_beta)

print("theta_alpha", theta_alpha )
print("theta_beta", theta_beta )
# print("theta(k_alpha)",theta(k_alpha))

