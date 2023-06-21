import numpy as np
# import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std

lambda_lit = ufloat(682, 2)
lambda_mes = ufloat(666.8 , 2.67)
print("Abweichung:", (lambda_lit - lambda_mes)/(lambda_lit) * 100)