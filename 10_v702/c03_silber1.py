import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
import c01_nulleffekt as c01
from scipy.optimize import curve_fit


x, count_v = np.genfromtxt("messung_c03_silber1.txt", unpack = True)
delta_t = 10