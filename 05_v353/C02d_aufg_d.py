import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import C02_aufg_b_c as C02

print('Hier entsteht der Polarplot')
print(C02.A_plot)
plt.figure(constrained_layout=True)
plt.polar(C02.Delta_Phi_plot, C02.A_plot, 'x')
plt.polar(C02.Phi_omega(C02.x_plot, *C02.RC_3_ergeb),  0.4 * C02.A_omega(C02.x_plot, *C02.RC_2_ergeb))


plt.savefig("build/C02_aufg_d.pdf")