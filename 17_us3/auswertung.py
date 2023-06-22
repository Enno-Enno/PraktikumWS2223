import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from uncertainties.unumpy import nominal_values as nom
from uncertainties.unumpy import std_devs as std
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy import odr
import numpy.polynomial as npp

# Daten
theta = np.array([15, 30, 60])
alpha_deg = np.array([80, 71, 55])
alpha = alpha_deg * 2 * np.pi / 360

c_l = 1800  # Schall in der Flüssigkeit
c_p = 2700  # Schall im Prisma

strömung = np.array([1.5, 2, 3, 4, 5])

f_max_1_5_l = np.array([-104, 163, -280])
f_mean_1_5_l = np.array([-67, 98, -171])

f_max_2_0_l = np.array([-140, 232, -410])
f_mean_2_0_l = np.array([-85, 134, -232])

f_max_3_0_l = np.array([-255, 430, -732])
f_mean_3_0_l = np.array([-134, 256, -439])

f_max_4_0_l = np.array([-400, 723, -1234])
f_mean_4_0_l = np.array([-220, 403, -708])

f_max_5_0_l = np.array([-507, 1048, -1740])
f_mean_5_0_l = np.array([-269, 562, -1050])

f_mean_matrix = np.array(
    [f_mean_1_5_l, f_mean_2_0_l, f_mean_3_0_l, f_mean_4_0_l, f_mean_5_0_l]
)
f_max_matrix = np.array(
    [f_max_1_5_l, f_max_2_0_l, f_max_3_0_l, f_max_4_0_l, f_max_5_0_l]
)
alpha_matrix = np.array([alpha, alpha, alpha, alpha, alpha])
# print(alpha_matrix[:, 0])


depth_mseconds = np.array(
    [
        12.5,
        13.0,
        13.5,
        14.0,
        14.5,
        15.0,
        15.5,
        16.0,
        16.5,
        17.0,
        17.5,
        18.0,
        18.5,
        19.0,
        19.5,
    ]
)
signal_5 = np.array([20, 29, 55, 57, 70, 70, 77, 80, 85, 70, 50, 135, 300, 300, 230])
speed_5 = np.array([0, 70, 90, 100, 110, 115, 108, 100, 82, 80, 80, 90, 98, 98, 90])


signal_3 = np.array([20, 34, 40, 50, 52, 60, 56, 61, 61, 56, 55, 105, 80, 100, 60])
speed_3 = np.array([0, 33, 37, 42, 45, 48, 48, 42, 37, 34, 34, 39, 35, 40, 38])


# rechnungen

print(f_mean_matrix)


strömung_long = np.concatenate((strömung, strömung, strömung))
f_mean_long = np.concatenate(
    (
        np.abs(f_mean_matrix[:, 0]) / (np.cos(alpha[0])),
        np.abs(f_mean_matrix[:, 1]) / (np.cos(alpha[1])),
        np.abs(f_mean_matrix[:, 2]) / (np.cos(alpha[2])),
    )
)
f_max_long = np.concatenate(
    (
        np.abs(f_max_matrix[:, 0]) / (np.cos(alpha[0])),
        np.abs(f_max_matrix[:, 1]) / (np.cos(alpha[1])),
        np.abs(f_max_matrix[:, 2]) / (np.cos(alpha[2])),
    )
)


def dopplergeschwindigkeit(delta_f, alpha):
    c = c_l
    f_0 = 2000000
    return delta_f * c / (2 * f_0 * np.cos(alpha))


# print(dopplergeschwindigkeit(f_mean_matrix, alpha_matrix))
speed_mean_matrix = dopplergeschwindigkeit(f_mean_matrix, alpha_matrix)
speed_max_matrix = dopplergeschwindigkeit(f_max_matrix, alpha_matrix)
speed_long = np.concatenate(
    (
        np.abs(speed_mean_matrix[:, 0]),
        np.abs(speed_mean_matrix[:, 1]),
        np.abs(speed_mean_matrix[:, 2]),
    )
)

params_mean, covariance_matrix = np.polyfit(strömung_long, f_mean_long, 1, cov=True)
errors_mean = np.sqrt(np.diag(covariance_matrix))

# for name, value, error in zip("ab", params_mean, errors_mean):
#     print(f"{name} = {value:.0f} +- {error:.0f}")

params_max, covariance_matrix = np.polyfit(strömung_long, f_max_long, 1, cov=True)
errors_max = np.sqrt(np.diag(covariance_matrix))

# for name, value, error in zip("ab", params_max, errors_max):
#     print(f"{name} = {value:.0f} +- {error:.0f}")


def p1(x, a, b):
    return a * x + b


 

# print(r" {\theta}  {$\alpha$} {f_max_1_5_l} & {f_mean_1_5_l} & {f_max_2_0_l} & {f_mean_2_0_l} & {f_max_3_0_l} & {f_mean_3_0_l} & {f_max_4_0_l} & {f_mean_4_0_l} & {f_max_5_0_l} & {f_mean_5_0_l} \\")
# for index, _ in enumerate(f_max_1_5_l):
# print(rf"{theta[index]}& {alpha[index]} & {f_max_1_5_l[index]} & {f_mean_1_5_l[index]} & {f_max_2_0_l[index]} & {f_mean_2_0_l[index]} & {f_max_3_0_l[index]} & {f_mean_3_0_l[index]} & {f_max_4_0_l[index]} & {f_mean_4_0_l[index]} & {f_max_5_0_l[index]} & {f_mean_5_0_l[index]}\\")


def depth_in_mm(micro_seconds):
    if micro_seconds < 4*3.07:
        return micro_seconds * 10/4
    return 4*3.07 *10/4 + (micro_seconds - 4*3.07)* 3/2 


depth_mm = np.zeros(len(depth_mseconds))
# for index,_ in enumerate(depth_mseconds):
#     print(f"{depth_mseconds[index]} & {depth_in_mm(depth_mseconds[index])} & {signal_3[index]}  \t& {speed_3[index]} & {signal_5[index]} & {speed_5[index]} \\\\")
#     depth_mm[index] = depth_in_mm(depth_mseconds[index])





# print("H:", 10/np.sin(np.deg2rad(80)))
# print(30.7 + 10.15)





xplot = np.linspace(1.5, 5)
plt.figure(constrained_layout=True)
plt.plot(xplot, p1(xplot, *params_mean), label=r"Linearer Fit $f_\text{mean}$")
plt.plot(xplot, p1(xplot, *params_max), label=r"Linearer Fit $f_\text{max}$")

# plt.plot(strömung_long, f_max_long, "x", label=r"$f_\text{max}$")
# plt.plot(strömung_long, f_mean_long, "x", label=r"$f_\text{mean}$")

plt.plot(
    np.abs(strömung) ,
    np.abs(f_mean_matrix[:, 0]) / (np.cos(alpha[0])),
    "x",
    label=r"$f_\text{mean, \qty{15}{\degree}}  $  ",
)

plt.plot(
    np.abs(strömung) ,
    np.abs(f_mean_matrix[:, 1]) / (np.cos(alpha[1])),
    "x",
    label=r"$f_\text{mean, \qty{30}{\degree}}  $",
)

plt.plot(
    np.abs(strömung) ,
    np.abs(f_mean_matrix[:, 2]) / (np.cos(alpha[2])),
    "x",
    label=r"$f_\text{mean, \qty{60}{\degree}}  $",
)

plt.plot(
    np.abs(strömung) ,
    np.abs(f_max_matrix[:, 0]) / (np.cos(alpha[0])),
    "x",
    label=r"$f_\text{max, \qty{15}{\degree}}  $  ",
)

plt.plot(
    np.abs(strömung) ,
    np.abs(f_max_matrix[:, 1]) / (np.cos(alpha[1])),
    "x",
    label=r"$f_\text{max, \qty{30}{\degree}}  $",
)

plt.plot(
    np.abs(strömung) ,
    np.abs(f_max_matrix[:, 2]) / (np.cos(alpha[2])),
    "x",
    label=r"$f_\text{max, \qty{60}{\degree}}  $",
)



plt.legend()

plt.xlabel(r"$W/ \unit{\liter\per\minute}$")
plt.ylabel(
    r"$\frac{\left|\Delta f\right|}{\cos{\alpha}}/\unit{1\per\second} $"
)
plt.savefig("build/01_plot.pdf")
plt.clf


plt.figure(constrained_layout=True)
plt.subplot(2,1,1)
plt.plot(depth_mm, speed_3, "x", label=r"$v$ \qty{3}{\liter\per\minute} ")
plt.plot(depth_mm, speed_5, "x", label=r"$v$ \qty{5}{\liter\per\minute} ")
plt.ylabel(r"$v / \unit{\cm\per\second} $ ")

plt.subplot(2,1,2)
plt.plot(depth_mm, signal_3, "x", label=r"Signal \qty{3}{\liter\per\minute}")
plt.plot(depth_mm, signal_5, "x", label=r"Signal \qty{5}{\liter\per\minute}")
plt.ylabel(r"signal $/ \unit{\volt\squared\per\second} $ ")
# plt.xlabel()

plt.legend()
plt.grid()

plt.savefig("build/02_plot.pdf")
# plt.clf

