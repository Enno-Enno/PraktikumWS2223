import numpy as np
import matplotlib.pyplot as plt

(klein_oben, klein_unten) = np.genfromtxt("Messdaten_klKu_Zitemp.txt", unpack=True)
(groß_oben, klein_unten) = np.genfromtxt("Messdaten_grKu_Zitemp.txt", unpack=True)
(temp, temp_oben, temp_unten) = np.genfromtxt("Messdaten_grKu_steigendeTemp.txt", unpack=True)

