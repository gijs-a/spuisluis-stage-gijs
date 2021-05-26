#! usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # [m s^-2] gravitatieversnelling
rho_1 = 1000 # [kg m^-3] dichtheid zoet water
rho_2 = 1022 # [kg m^-3] dichtheid zout water
Drho = rho_2 - rho_1 # [kg m^-3] dichtheidsverschil
gp = 2*g*Drho / (rho_2+rho_1)

H_B = -20 # [mNAP] niveau bodem
H_z = 2 # [mNAP] waterniveau zeezijde
H_m = 3 # [mNAP] waterniveau meerzijde
H_G = -8 # [mNAP] locatie van dichtheidsinterface
H_S = -15 # [mNAP] locatie van as van opening
Dh = H_m - H_z # [m] verval over de spuisluis
mu = 1 # afvoercoefficient (0.6 - 1; bij kleine openingen vaak mu=1)
b = 120 # [m] breedte
#D_values = np.array([0.01, 0.1, 0.25, 0.5, 1, 1.5, 2])
D = 0.25 # [m] spleethoogte
A = b*D # [m^2] open oppervlak beschikbaar voor lekkage
K = 1.7 # slot

Q = mu*A*np.sqrt(2*g*Dh) # [m^3 s^-1] debiet
q = Q/b # [m^2 s^-1] debiet per eenheid breedte

H = H_m - H_B # [m]
h_r = H_G - H_B

F_rc = (2/3)**(3/2)

if H_G < H_S - K*q**(2/3)/gp**(1/3):
    h_c = H_S - K*q**(2/3)/gp**(1/3) - H_B
else:
    h_c = H_S + K*q**(2/3)/gp**(1/3) - H_B

h_r = np.linspace(0.01,H,100)
lam = 0.5
F_r = (H/h_r)**(3/2) * (1+lam/(1-lam)) * ( (lam/(1-lam))**2/(1-h_c/H)**3 + 1/(h_c/H)**3 )**(-1/2)
F_rmax = (H/h_r)**(5/2)*(1+np.sqrt(H/h_r - 1))**(-2)

## Figure 4
plt.figure(figsize=(8,5))
plt.axis([0,8,0,1])
plt.xlabel('$F_r$')
plt.ylabel('$h_r/H$')
plt.title('Jirka figure 4')
plt.gca().axvline(F_rc, color='black')
plt.plot(F_rmax, h_r/H, '--', label='$F_rmax')
plt.plot(F_r, h_r/H, '--r')




g = 9.81 # [m s^-2] gravitatieversnelling
rho_1 = 1000 # [kg m^-3] dichtheid zoet water
rho_2 = 1022 # [kg m^-3] dichtheid zout water
Drho = rho_2 - rho_1 # [kg m^-3] dichtheidsverschil
gp = 2*g*Drho / (rho_2+rho_1)

H = 23
h_r = 0.5*H
for q in np.linspace(0,5,6):
    Fr = q/np.sqrt(gp*h_r**3)
    plt.plot(Fr, h_r/H, 'r.')

plt.savefig('figures/jirka_fig4.png', bbox_inches='tight')