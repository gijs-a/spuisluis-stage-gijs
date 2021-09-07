#! usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # [m s^-2] gravitatieversnelling
rho_1 = 1000 # [kg m^-3] dichtheid zoet water
rho_2 = 1020 # [kg m^-3] dichtheid zout water
Drho = rho_2 - rho_1 # [kg m^-3] dichtheidsverschil
gp = 2*g*Drho / (rho_2+rho_1)

H = 20 # m
D = 3 # m
lambdas = np.array([0,0.1,0.2,0.3,0.5])

plt.figure(figsize=(8,5))
plt.axis([0,8,0,5])
plt.grid()
plt.xlabel('$F_i$')
plt.ylabel('$h_r/D$')
plt.title('Noordland M1204 fig. 14')

for lam in lambdas:
    h_r = np.linspace(0, 15, 1000)

    F_i = np.zeros(h_r.size)
    F_i[D<=2/3*h_r*(1/(1-lam))] = 1/(1-lam)*2/3*h_r[D<=2/3*h_r*(1/(1-lam))]/D*np.sqrt(2/3*h_r[D<=2/3*h_r*(1/(1-lam))]/D)
    F_i[D>2/3*h_r*(1/(1-lam))] = np.sqrt(h_r[D>2/3*h_r*(1/(1-lam))]/D - (1-lam))

    plt.plot(F_i, h_r/D, label='{:.0%}'.format(lam))
    plt.legend()

plt.savefig('figures/noordland.png')