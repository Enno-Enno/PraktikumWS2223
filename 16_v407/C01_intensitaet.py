import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy import odr


def darstellung(alpha, array, name):
    print(name)
    for index, _stuff in enumerate(alpha):
        print(alpha[index], "° :", array[index])


alpha, senkrecht, parallel, dunkel = np.genfromtxt(
    "messungen/intensitaet.txt", unpack=True
)

senkrecht_err = np.zeros(len(senkrecht))
parallel_err = np.zeros(len(parallel))
dunkel_err = np.zeros(len(dunkel))
alpha_rad = alpha * (2 * np.pi) / (360)
I_e_parallel = ufloat(1000, 50)
I_e_senkrecht = ufloat(1800, 50)

# print("senkrecht")
for index, intensitaet in enumerate(senkrecht):
    if intensitaet < 10:
        senkrecht_err[index] = 0.1
        continue
    if intensitaet < 100:
        senkrecht_err[index] = 0.5
        continue
    senkrecht_err[index] = 5


# for index, intensitaet in enumerate(senkrecht):
# print(rf"{intensitaet} \pm {senkrecht_err[index]} ")


# print("parallel")
for index, intensitaet in enumerate(parallel):
    if intensitaet < 10:
        parallel_err[index] = 0.1
        continue
    if intensitaet < 100:
        parallel_err[index] = 0.5
        continue
    parallel_err[index] = 5

# for index, intensitaet in enumerate(parallel):
#     print(rf"{alpha[index]}°:{intensitaet} \pm {parallel_err[index]} ")


# print("dunkel")
for index, intensitaet in enumerate(dunkel):
    if intensitaet < 10:
        dunkel_err[index] = 0.1
        continue
    if intensitaet < 100:
        dunkel_err[index] = 0.5
        continue
    dunkel_err[index] = 5

# for index, intensitaet in enumerate(dunkel):
# print(rf"{intensitaet} \pm {dunkel_err[index]} ")

parallel = unp.uarray(parallel, parallel_err)
senkrecht = unp.uarray(senkrecht, senkrecht_err)
dunkel = unp.uarray(dunkel, dunkel_err)
# alpha = 90-alpha -> ist wirklich quatsch
# Intensitäten ->


parallel_korrigiert = parallel - dunkel
senkrecht_korrigiert = senkrecht - dunkel
plot_parallel = unp.sqrt(parallel_korrigiert / I_e_parallel)
plot_senkrecht = unp.sqrt(senkrecht_korrigiert / I_e_senkrecht)

darstellung(alpha, dunkel, "dunkel")
darstellung(alpha, senkrecht, "senkrecht")
darstellung(alpha, parallel, "parallel")
darstellung(alpha, senkrecht_korrigiert, "senkrecht_korrigiert")
darstellung(alpha, parallel_korrigiert, "parallel_korrigiert")
darstellung(alpha, plot_parallel, "plot_parallel")
# darstellung(alpha,plot_senkrecht,"plot_senkrecht")
darstellung(alpha, unp.sqrt(parallel), "E_r_parallel")


def n_senkrecht(I_r_senkrecht, I_e_senkrecht, alpha_rad):
    c = unp.sqrt(I_r_senkrecht)
    b = unp.sqrt(I_e_senkrecht)
    return unp.sqrt(-2 * b * c * (unp.cos(alpha_rad)) ** 2 + b**2 + c**2) / (
        unp.sqrt(b**2 - 2 * b * c + c**2)
    )


# Wolfram alpha output:
# -Divide[sqrt\(40)Power[b,2] + Power[c,2] + 2 b c cos\(40)2 a\(41)\(41),sqrt\(40)Power[b,2] - 2 b c + Power[c,2]\(41)]


n_senkrecht_values = n_senkrecht(senkrecht_korrigiert, I_e_senkrecht, alpha_rad)
darstellung(alpha, n_senkrecht_values, "n_senkrecht")

# Für n_parallel:
# solve Divide[b,c] =  Divide[Power[x,2]cos\(40)a\(41) -sqrt\(40)Power[x,2]- Power[sin\(40)a\(41),2]\(41) ,Power[x,2] cos\(40)a\(41) + sqrt\(40)Power[x,2]- Power[sin\(40)a\(41),2]\(41)]
# in wolfram alpha eingeben

# print("n_parallel")
def n_parallel(I_r_parallel, I_e_parallel, alpha_rad):
    E_r = unp.sqrt(I_r_parallel)
    E_e = unp.sqrt(I_e_parallel)
    frac = (E_r + E_e) / (E_e - E_r)
    return unp.sqrt(
        0.5 * (frac * 1 / unp.cos(alpha)) ** 2
        + unp.sqrt(
            0.25 * (frac * 1 / unp.cos(alpha)) ** 4 - (frac * unp.tan(alpha)) ** 2
        )
    )


n_parallel_values = n_parallel(
    unp.sqrt(plot_parallel), unp.sqrt(I_e_parallel), alpha_rad
)

darstellung(alpha, n_parallel_values, "n_parallel")


alpha_senkrecht = alpha
n_senkrecht_red = n_senkrecht_values
counter = 0
for index, n in enumerate(n_senkrecht_red):
    if n > 10:
        alpha_senkrecht = np.delete(alpha_senkrecht, index - counter)
        n_senkrecht_red = np.delete(n_senkrecht_red, index - counter)
        counter += 1

alpha_parallel = alpha
n_parallel_red = n_parallel_values
counter = 0
for index, n in enumerate(n_parallel_red):
    if n > 8:
        alpha_parallel = np.delete(alpha_parallel, index - counter)
        n_parallel_red = np.delete(n_parallel_red, index - counter)
        counter += 1


n_parallel_mean = sum(n_parallel_red) / len(n_parallel_red)
n_senkrecht_mean = sum(n_senkrecht_red) / len(n_senkrecht_red)
n_very_mean = (n_parallel_mean + n_senkrecht_mean) / 2

print("n_parallel mean ", n_parallel_mean)
print("n_senkrecht mean", n_senkrecht_mean)
print("n_very_mean", n_very_mean)


Brewster_Winkel = ufloat(76, 0.5)

n_Brewster = unp.tan(Brewster_Winkel * 2 * np.pi / 360)
print("n_Brewster:", n_Brewster)


def intensitaet_parallel(alpha, I_e_senkrecht, n):
    alpha_rad = alpha * 2 * np.pi / (360)
    return (
        np.sqrt(I_e_senkrecht)
        * (n**2 * np.cos(alpha_rad) - np.sqrt(n**2 - np.sin(alpha_rad) ** 2))
        / (n**2 * np.cos(alpha_rad) + np.sqrt(n**2 - np.sin(alpha_rad) ** 2))
    ) ** 2


def intensitaet_senkrecht(alpha, I_e_parallel, n):
    alpha_rad = alpha * 2 * np.pi / (360)
    return (
        -np.sqrt(I_e_parallel)
        * (np.sqrt(n**2 - np.sin(alpha_rad) ** 2) - np.cos(alpha_rad)) ** 2
        / (n**2 - 1)
    ) ** 2


plt.figure(constrained_layout=True)
xplot = np.linspace(0, 89)
plt.plot(
    xplot,
    np.sqrt(intensitaet_senkrecht(xplot, I_e_senkrecht.n, n_senkrecht_mean.n) / I_e_senkrecht.n),
    label=r"$I_{\perp,\text{theo}} \text{basierend auf } \overline{n_\perp}$",
)
plt.plot(
    xplot,
    np.sqrt(intensitaet_parallel(xplot, I_e_parallel.n, n_senkrecht_mean.n) / I_e_parallel.n),
    label=r"$I_{\parallel,\text{theo}} \text{basierend auf } \overline{n_\perp}$",
)

plt.plot(
    xplot,
    np.sqrt(intensitaet_senkrecht(xplot, I_e_senkrecht.n, n_parallel_mean.n) / I_e_senkrecht.n),
    label=r"$I_{\perp,\text{theo}} \text{basierend auf } \overline{n_\parallel}$",
)
plt.plot(
    xplot,
    np.sqrt(intensitaet_parallel(xplot, I_e_parallel.n, n_parallel_mean.n) / I_e_parallel.n),
    label=r"$I_{\parallel,\text{theo}} \text{basierend auf } \overline{n_\parallel}$",
)

print(nom(n_Brewster))
print(I_e_senkrecht.n)
plt.plot(
    xplot,
    np.sqrt(intensitaet_senkrecht(xplot, I_e_senkrecht.n, nom(n_Brewster)) / I_e_senkrecht.n),
    label=r"$I_{\perp,\text{theo}} \text{basierend auf } n_\text{b}$",
)
plt.plot(
    xplot,
    np.sqrt(intensitaet_parallel(xplot, I_e_parallel.n, nom(n_Brewster)) / I_e_parallel.n),
    label=r"$I_{\parallel,\text{theo}} \text{basierend auf } n_\text{b}$",
)

plt.errorbar(
    alpha,
    nom(plot_parallel),
    yerr=std(plot_parallel),
    fmt="x",
    label=r"Parallel Polarisiertes Licht",
)
plt.errorbar(
    alpha,
    nom(plot_senkrecht),
    yerr=std(plot_senkrecht),
    fmt="x",
    label=r"Senkrecht Polarisiertes Licht",
)
# plt.plot(alpha, parallel,"x", label=r"Parallel Polarisiertes Licht ohne Korrektur")
# plt.plot(alpha, senkrecht, "x", label=r"Senkrecht Polarisiertes Licht ohne Korrektur")

plt.xlabel(r"$\alpha /\unit{\degree}$")
plt.ylabel(r"$\sqrt{I(\alpha)/I_e} $")
plt.grid()
plt.legend(loc='upper left')
plt.savefig("build/03_plot.pdf")


plt.clf()

plt.errorbar(
    alpha,
    nom(plot_parallel),
    yerr=std(plot_parallel),
    fmt="x",
    label=r"Parallel Polarisiertes Licht",
)
plt.errorbar(
    alpha,
    nom(plot_senkrecht),
    yerr=std(plot_senkrecht),
    fmt="x",
    label=r"Senkrecht Polarisiertes Licht",
)

plt.xlabel(r"$\alpha /\unit{\degree}$")
plt.ylabel(r"$\sqrt{I(\alpha)/I_e} $")
plt.grid()
plt.legend(loc='upper left')
plt.savefig("build/02_plot")

plt.figure(constrained_layout=True)




plt.clf()

plt.figure(constrained_layout=True)

plt.errorbar(
    alpha,
    nom(n_parallel_values),
    yerr=std(n_parallel_values),
    fmt="x",
    label=r"$n_\parallel$",
)

plt.errorbar(
    alpha,
    nom(n_senkrecht_values),
    yerr=std(n_senkrecht_values),
    fmt="x",
    label=r"$n_\perp$",
)
plt.plot(alpha, 10 * np.ones(len(alpha)), label="Filtergrenze")

plt.xlabel(r"$\alpha /\unit{\degree}$")
plt.ylabel(r"$n$")
plt.grid()
plt.legend()

plt.savefig("build/01_plot.pdf")
