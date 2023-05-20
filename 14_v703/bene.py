import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
import uncertainties as unc
import uncertainties.unumpy as unp

U, N, I=np.genfromtxt('data1.txt', unpack=True)
Nf=np.sqrt(N)/120
N=N/120
#Nf=unp.uarray(N,Nf)

def f1(x,a,b):
    return a*x+b

def f2(x,c):
    return (x+c)-x

par, cov=curve_fit(f1,U, N,sigma=Nf)
par = unc.correlated_values(par, cov)
a = float(unp.nominal_values(par[0]))
b = float(unp.nominal_values(par[1]))
a_f = float(unp.std_devs(par[0]))
b_f = float(unp.std_devs(par[1]))


par, cov=curve_fit(f2,U[4:16], N[4:16],sigma=Nf[4:16])
par = unc.correlated_values(par, cov)
c = float(unp.nominal_values(par[0]))
c_f = float(unp.std_devs(par[0]))

x=np.linspace(300,710)
x2=np.linspace(410,620)

plt.plot(x,f1(x,a,b),"g-",label="Ausgleichsgerade")
plt.plot(x2,f2(x2,c),"r--",label="Plateau")
plt.errorbar(U,N,yerr=Nf,fmt="o",label="Messwerte")
plt.xlabel(r"Spannung $U \, [\mathrm{V}]$")
plt.ylabel(r"$N \, [\mathrm{\frac{1}{s}}]$")
plt.xlim(300,710)
plt.legend()
plt.savefig("build/plot1.pdf")
plt.show()

a=unp.uarray(a,a_f)
b=unp.uarray(b,b_f)
print(a)
print(b)
print(c)

#--------------------------------------------------------------------------------------------------------------------
#Anzahl Ladungsträger
e=1.6022 #*10**(-19)

If=0.05
Q=I*12/e  #*10**(-6)/e
Qf=If*12/e#*10**(-6)/e
print(Q)

par, cov=curve_fit(f1,U, Q)
par = unc.correlated_values(par, cov)
aq = float(unp.nominal_values(par[0]))
bq = float(unp.nominal_values(par[1]))
aq_f = float(unp.std_devs(par[0]))
bq_f = float(unp.std_devs(par[1]))

xq=np.linspace(300,710)

plt.plot(xq,f1(xq,aq,bq),"g-",label="Ausgleichsgerade")
plt.errorbar(U,Q,yerr=Qf,fmt="o",label="Messwerte")
plt.xlabel(r"Spannung $U \, [\mathrm{V}]$")
plt.ylabel(r"Anzahl Ladungsträger N $\,[10^{15}]$ ")
plt.xlim(300,710)
plt.legend()
plt.savefig("build/plot2.pdf")
plt.show()

aq=unp.uarray(aq,aq_f)
bq=unp.uarray(bq,bq_f)
print(aq*e)
print(bq)


#--------------------------------------------------------------------------------------------------------------------
#Totzeit

N1=29144+67200
N2=60860+2*67200
N12=51561+3*67200
N1=unc.ufloat(N1,np.sqrt(N1))/120
N2=unc.ufloat(N2,np.sqrt(N2))/120
N12=unc.ufloat(N12,np.sqrt(N12))/120

T=(N1+N2-N12)/(N12**2-N1**2-N2**2)
print(T)