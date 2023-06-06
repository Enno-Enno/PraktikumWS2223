import numpy as np
import scipy.constants as const

theta = np.deg2rad([15, 30, 60])

c_p = 2730 #m/s 
# nach https://www.olympus-ims.com/de/ndt-tutorials/thickness-gauge/appendices-velocities/

c_l = 1800 #m/s
#nach Anleitung

alpha = np.pi/2 - np.arcsin(np.sin(theta) * c_l/c_p)

theta = np.rad2deg(theta)
alpha = np.rad2deg(alpha)

for index, value in enumerate(alpha):
    print(f"θ = {theta[index]:.0f} deg, α = {value:.2f} deg")

# θ = 15 deg, α = 80.17 deg
# θ = 30 deg, α = 70.75 deg
# θ = 60 deg, α = 55.18 deg