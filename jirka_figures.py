#! usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
H = 20 # [m]
h_c = 0.9*H
h_r = np.linspace(0.01,H,100) # [m]
B = 2 # [m]
rho_1 = 1000
rho_2 = 1022
Drho = rho_2-rho_1
gp = 2*g*Drho / (rho_2+rho_1)

lam = 0.1

F_rmax = (H/h_r)**(5/2)*(1+np.sqrt(H/h_r - 1))**(-2)
F_rc = (2/3)**(3/2)
#F_r = (H/h_r)**(3/2) * ((lam/(1-lam))**2/(1-h_c/H)**3 + 1/(h_c/H)**3)**(-1/2) * (1+lam/(1-lam))


## Figure 4
plt.figure(figsize=(5,5))
plt.axis([0,8,0,1])
plt.xlabel('Fr')
plt.ylabel('hr/H')
plt.title('selective withdrawal effectiveness diagram')
plt.plot(F_rmax, h_r/H, '--')
plt.gca().axvline(F_rc, color='black')
plt.plot(F_r, h_r/H, '-r')

plt.savefig('figures/jirka_fig4.png', bbox_inches='tight')


lam = np.linspace(0,0.7,100)
F_r = F_rc/(1-lam)

## Figure 3
plt.figure(figsize=(10,10))
plt.axis([0,2,0,0.7])
plt.xlabel('Fr')
plt.ylabel('hr/H')
plt.title('Jirka figure 3')
plt.plot(F_r, lam, '.r')
plt.savefig('figures/jirka_fig3.png', bbox_inches='tight')


