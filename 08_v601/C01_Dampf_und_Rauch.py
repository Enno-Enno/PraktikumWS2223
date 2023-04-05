import numpy as np
# import matplotlib.pyplot as plt
# from uncertainties import ufloat

Temp_C = np.genfromtxt("C01_Temperaturen_und_so.txt")
Temp_K = Temp_C + 273 
p_set = 5.5 * 10 ** (7) * np.exp(-6876/Temp_K)
w_marked = 0.0029 / p_set 

for i, val in enumerate(Temp_C):
    print(Temp_C[i] , "&", Temp_K[i], "&", p_set[i], "&", w_marked[i] )