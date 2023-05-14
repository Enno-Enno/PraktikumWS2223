import numpy as np
import scipy.constants as c
import astropy.constants as astro

rydberg = c.Rydberg

Z_Zn = 30
Z_Ge = 32
Z_Br = 35
Z_Rb = 37
Z_Sr = 38
Z_Zr = 40

def wavelength(energy):
    return(c.h * c.c / (energy))

E_Zn =  9.66  * 1000 * c.e # J
E_Ge = 11.10  * 1000 * c.e # J
E_Br = 13.47  * 1000 * c.e # J
E_Rb = 15.20  * 1000 * c.e # J
E_Sr = 16.10  * 1000 * c.e # J
E_Zr = 17.99  * 1000 * c.e # J

λ_Zn =  wavelength(E_Zn)  
λ_Ge =  wavelength(E_Ge)  
λ_Br =  wavelength(E_Br)  
λ_Rb =  wavelength(E_Rb)  
λ_Sr =  wavelength(E_Sr)  
λ_Zr =  wavelength(E_Zr)  

print(λ_Zn)
print(λ_Ge)
print(λ_Br)
print(λ_Rb)
print(λ_Sr)
print(λ_Zr)

n = 1

def teta(wavelength):
    return (n * wavelength/(2 * 201.4 *10**(-12)))

teta_Zn = np.rad2deg(np.arcsin(teta(λ_Zn)))
teta_Ge = np.rad2deg(np.arcsin(teta(λ_Ge)))
teta_Br = np.rad2deg(np.arcsin(teta(λ_Br)))
teta_Rb = np.rad2deg(np.arcsin(teta(λ_Rb)))
teta_Sr = np.rad2deg(np.arcsin(teta(λ_Sr)))
teta_Zr = np.rad2deg(np.arcsin(teta(λ_Zr)))

print("teta_Zn", teta_Zn)
print("teta_Ge", teta_Ge)
print("teta_Br", teta_Br)
print("teta_Rb", teta_Rb)
print("teta_Sr", teta_Sr)
print("teta_Zr", teta_Zr)


def sigma(z, energy):
    return(z - np.sqrt(energy/(13.6 * c.e) - astro.alpha**2 * z**4/4))


sigma_Zn = sigma(Z_Zn, E_Zn)
sigma_Ge = sigma(Z_Ge, E_Ge)
sigma_Br = sigma(Z_Br, E_Br)
sigma_Rb = sigma(Z_Rb, E_Rb)
sigma_Sr = sigma(Z_Sr, E_Sr)
sigma_Zr = sigma(Z_Zr, E_Zr)


print("sigma_Zn", sigma_Zn)
print("sigma_Ge", sigma_Ge)
print("sigma_Br", sigma_Br)
print("sigma_Rb", sigma_Rb)
print("sigma_Sr", sigma_Sr)
print("sigma_Zr", sigma_Zr)


# teta_Zn 18.58067369078699
# teta_Ge 16.09927954595463
# teta_Br 13.209491136899516
# teta_Rb 11.683415807687602
# teta_Sr 11.021875190709254
# teta_Zr 9.851683102895548
# sigma_Zn 3.5517350596183093
# sigma_Ge 3.676565400559749
# sigma_Br 3.847735266899239
# sigma_Rb 3.9440375141854815
# sigma_Sr 3.999052214360077
# sigma_Zr 4.101347507826553