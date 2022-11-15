import numpy as np
import matplotlib.pyplot as plt

(Delta_x, F) = np.genfromtxt('Hook_Daten.txt',unpack=True)

x = np.linspace(0,54)
sum = 0
mxf = 0
xsqrd = 0

for index in range(len(Delta_x)):
    print('{:.4f}'.format(F[index] / Delta_x[index]))
    sum += F[index] / Delta_x[index]
    mxf += F[index] * Delta_x[index]
    xsqrd += Delta_x[index]**2
print('Summe D: ', '{:.4f}'.format(sum))
print('Mittelwert D: ', '{:.4f}'.format(sum/10))

mx=np.sum(Delta_x)/len(Delta_x)
mf=np.sum(F)/len(F)
print('Mittelwert x: ', '{:.4f}'.format(mx))
print('Mittelwert F:', '{:.4f}'.format(mf))
print('Mittelwert xF:', '{:.4f}'.format(mxf/10))
print('Mittelwert xsqrd:', '{:.4f}'.format(xsqrd/10))

a = (mxf/10) - (mx * mf)
b = (xsqrd/10) - mx**2
c = a/b
d = sum/10
print('linreg für D: ', '{:.4f}'.format(c))




plt.plot(Delta_x, F, 'x', label = 'Messwerte')
plt.plot(x, d*x, 'k-', label = 'Mittelwert')
plt.plot(x, c*x, '-', label = 'Ausgleichsgerade')
plt.xlabel('$ \Delta x \\, [\\unit{{\\cm}}] $')
plt.ylabel('$ F \\, [\\unit{{\\newton}}] $')
plt.legend()


plt.savefig('build/plot.pdf')