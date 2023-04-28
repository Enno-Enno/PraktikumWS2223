import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import scipy.constants as const

#λ rot =  [5.288410940084869e-07]

lines = 600 / 10**(-3)
gitterkonst = 1/lines

maximum, links, rechts = np.genfromtxt("messung_5_600_rot.txt", unpack = True)

phi = np.deg2rad((np.abs(links + rechts))/2)

wavelength = gitterkonst * unp.sin(phi) / maximum[1:]

print("λ rot = ", wavelength[1:])