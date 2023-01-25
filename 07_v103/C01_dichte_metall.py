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

# alle E's in 10^9 N/m^2 

elastizitaet_cu = 124 

elastizitaet_kreis_einseitig = ufloat(131.7, 2.6) 
abweichung_elastizitaet_kreis_einseitig = (elastizitaet_kreis_einseitig - elastizitaet_cu) / elastizitaet_cu
print("Aweichung Elastizitaet Kreis einseitig: ", abweichung_elastizitaet_kreis_einseitig)
#Aweichung Elastizitaet Kreis einseitig:  0.062+/-0.021
elastizitaet_kreis_links = ufloat(262, 5)
abweichung_elastizitaet_kreis_links = (elastizitaet_kreis_links - elastizitaet_cu) / elastizitaet_cu
print("Aweichung Elastizitaet Kreis links: ", abweichung_elastizitaet_kreis_links)
#Aweichung Elastizitaet Kreis links:  1.11+/-0.04
elastizitaet_kreis_rechts = ufloat(212, 4)
abweichung_elastizitaet_kreis_rechts = (elastizitaet_kreis_rechts - elastizitaet_cu) / elastizitaet_cu
print("Aweichung Elastizitaet Kreis rechts: ", abweichung_elastizitaet_kreis_rechts)
#Aweichung Elastizitaet Kreis rechts:  0.710+/-0.032

elastizitaet_rechteck_einseitig = ufloat(119.9, 2.4)
abweichung_elastizitaet_rechteck_einseitig = (elastizitaet_rechteck_einseitig - elastizitaet_cu) / elastizitaet_cu
print("Aweichung Elastizitaet Rechteck einseitig: ", abweichung_elastizitaet_rechteck_einseitig)
#Aweichung Elastizitaet Rechteck einseitig:  -0.033+/-0.019
elastizitaet_rechteck_links = ufloat(126.1, 2.5)
abweichung_elastizitaet_rechteck_links = (elastizitaet_rechteck_links - elastizitaet_cu) / elastizitaet_cu
print("Aweichung Elastizitaet Rechteck links: ", abweichung_elastizitaet_rechteck_links)
#Aweichung Elastizitaet Rechteck links:  0.017+/-0.020
elastizitaet_rechteck_rechts = ufloat(167.0, 3.3)
abweichung_elastizitaet_rechteck_rechts = (elastizitaet_rechteck_rechts - elastizitaet_cu) / elastizitaet_cu
print("Aweichung Elastizitaet Rechteck rechts: ", abweichung_elastizitaet_rechteck_rechts)
#Aweichung Elastizitaet Rechteck rechts:  0.347+/-0.027