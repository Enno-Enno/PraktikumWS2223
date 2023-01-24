import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

radius = 1/2 * 1/100 * ufloat(1.000, 0.005) # m
laenge_kreis = 59.2/100 # m
masse_kreis = 1/1000 * ufloat(410.0, 0.1) #kg
volumen_kreis = np.pi * radius**2 * laenge_kreis # m^3
dichte_kreis_kg_m = masse_kreis/volumen_kreis # kg/m^3
dichte_kreis_g_cm = dichte_kreis_kg_m / 1000 # g/cm^3
print("dichte Kreis in kg/m^3: ", dichte_kreis_kg_m) #dichte Kreis in kg/m^3:  (8.82+/-0.09)e+03
print("dichte Kreis in g/cm^3: ", dichte_kreis_g_cm) #dichte Kreis in g/cm^3:  8.82+/-0.09

seite = 1/100 * ufloat(1.000, 0.005) # m
laenge_rechteck = 60.3/100 # m
masse_rechteck = 1/1000 * ufloat(535.9, 0.1) #kg
volumen_rechteck = seite**2 * laenge_rechteck
dichte_rechteck_kg_m = masse_rechteck/volumen_rechteck # kg/m^3
dichte_rechteck_g_cm = dichte_rechteck_kg_m / 1000 # g/cm^3
print("dichte Rechteck in kg/m^3: ", dichte_rechteck_kg_m) #dichte Rechteck in kg/m^3:  (8.89+/-0.09)e+03
print("dichte Rechteck in g/cm^3: ", dichte_rechteck_g_cm) #dichte Rechteck in g/cm^3:  8.89+/-0.09

dichte_kupfer_g_cm = 8.92 # g/cm^3
abweichung_dichte_kreis = (dichte_kreis_g_cm - dichte_kupfer_g_cm) / dichte_kupfer_g_cm
abweichung_dichte_rechteck = (dichte_rechteck_g_cm - dichte_kupfer_g_cm) / dichte_kupfer_g_cm
print("Abweichung Dichte Kreis: ", abweichung_dichte_kreis)       # Abweichung Dichte Kreis:  -0.011+/-0.010
print("Abweichung Dichte Rechteck: ", abweichung_dichte_rechteck) # Abweichung Dichte Rechteck:  -0.004+/-0.010