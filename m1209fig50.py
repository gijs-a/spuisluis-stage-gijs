#! usr/bin/env python3

#### Noordland M1209 fig 50

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
D = 1
rho1 = 1000
rho2 = 1020

plt.figure(figsize=(5,5))
plt.xlabel('Fri')
plt.ylabel('h_r/D')
Drho = rho2 - rho1
gp = g*Drho/rho2

h_r = np.linspace(1,4,1000)
F = np.zeros(h_r.size)
F[h_r/D < 3/2] = np.sqrt(2* abs(h_r[h_r/D < 3/2]/D - 1))
F[h_r/D >= 3/2] = 2/3 * h_r[h_r/D >= 3/2]/D *np.sqrt(2/3 * h_r[h_r/D >= 3/2]/D)

F_meng = np.zeros(h_r.size)
F_meng[h_r/D < 3/2] = np.sqrt(2* abs(h_r[h_r/D < 3/2]/D - 1))
F_meng[h_r/D >= 3/2] = np.sqrt(0.2*(h_r[h_r/D >= 3/2]/D)**3)

plt.plot(F, h_r/D, '-', label='zonder menglaag')
plt.plot(F_meng, h_r/D, '-', label='met menglaag')
plt.legend()
plt.title('Noordland M1209 fig.50')

plt.savefig('figures/M1209_fig50.png')