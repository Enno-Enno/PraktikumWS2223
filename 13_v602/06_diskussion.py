import numpy as np
from uncertainties import ufloat

bragg_exp = ufloat(14.25, 0.05)
bragg_lit = 14
bragg_abw = (bragg_exp - bragg_lit) / bragg_lit
print("bragg: ", bragg_abw)

energy_alpha_exp = ufloat(8.043, 0.017)
energy_alpha_lit = 8.04
energy_alpha_abw = (energy_alpha_exp - energy_alpha_lit) / energy_alpha_lit
print("energy_alpha: ", energy_alpha_abw)

energy_beta_exp = ufloat(8.893, 0.021)
energy_beta_lit = 8.94
energy_beta_abw = (energy_beta_exp - energy_beta_lit) / energy_beta_lit
print("energy_beta: ", energy_beta_abw)

zink_exp = ufloat(8.978, 0.021)
zink_lit = 9.66
zink_abw = (zink_exp - zink_lit) / zink_lit
print("zink: ", zink_abw)

brom_exp = ufloat(13.43, 0.05)
brom_lit = 13.47
brom_abw = (brom_exp - brom_lit) / brom_lit
print("brom: ", brom_abw)

stron_exp = ufloat(16.06, 0.07)
stron_lit = 16.10
stron_abw = (stron_exp - stron_lit) / stron_lit
print("stron: ", stron_abw)

zr_exp = ufloat(18.55, 0.10)
zr_lit = 17.99
zr_abw = (zr_exp - zr_lit) / zr_lit
print("zr: ", zr_abw)