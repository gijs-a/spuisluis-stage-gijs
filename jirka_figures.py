#! usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

g = 9.81

H = 20 # [m]
h_r = np.linspace(0.01,H,100) # [m]
B = 2 # [m]

rho_1 = 1000
rho_2 = 1022
Drho = rho_2-rho_1
gp = 2*g*Drho / (rho_2+rho_1)

F_rmax = (H/h_r)**(5/2)*(1+np.sqrt(H/h_r - 1))**(-2)
F_rc = (2/3)**(3/2)

#F_r = np.ones(h_r.size)*(2/3)**(3/2)
#cond = h_r < 3*B/2
#F_r[cond] = np.sqrt(2*(B/h_r[cond])**3*(h_r[cond]/B - 1))

plt.figure(figsize=(10,10))
plt.axis([0,8,0,1])
plt.xlabel('Fr')
plt.ylabel('hr/H')
plt.title('selective withdrawal effectiveness diagram')

plt.plot(F_rmax, h_r/H, '--')
plt.gca().axvline(F_rc, color='black')

#plt.plot(F_r, h_r/H, '.r')

plt.savefig('figures/jirka_fig4.png', bbox_inches='tight')