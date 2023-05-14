import numpy as np
import astropy.constants as c
import astropy.units as u

energy_k_alpha = 8.04 * u.keV
energy_k_beta = 8.94 * u.keV

print("Energie alpha = ", energy_k_alpha)
print("Energie beta = ", energy_k_beta)

lambda_k_alpha = c.h * c.c  / (energy_k_alpha)
print("lambda_k_alpha = ", lambda_k_alpha.to(u.picometer))

lambda_k_beta = c.h * c.c  / (energy_k_beta)
print("lambda_k_beta = ", lambda_k_beta.to(u.picometer))

def theta(wavelength, gitter):
    return(np.arcsin(wavelength/(2 * gitter)))

d_LiF = 201.4 * u.pm

theta_alpha = theta(lambda_k_alpha, d_LiF)
theta_beta = theta(lambda_k_beta, d_LiF)
print("theta_alpha: ", theta_alpha.to(u.deg))
print("theta_beta: ", theta_beta.to(u.deg))


# Energie alpha =  8.04 keV
# Energie beta =  8.94 keV
# lambda_k_alpha =  154.20920203134364 pm
# lambda_k_beta =  138.6847857194634 pm
# theta_alpha:  22.509902591224215 deg
# theta_beta:  20.139184010738617 deg