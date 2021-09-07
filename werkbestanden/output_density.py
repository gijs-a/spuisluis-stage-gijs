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
#H_S = -15 # [mNAP] locatie van as van opening
Dh = H_m - H_z # [m] verval over de spuisluis
mu = 1 # afvoercoefficient (0.6 - 1; bij kleine openingen vaak mu=1)
b = 120 # [m] breedte
D_values = np.array([0.01, 0.1, 0.25, 0.5, 1, 1.5, 2])

ii = 0
for D in D_values:
    A = b*D # [m^2] open oppervlak beschikbaar voor lekkage

    Q = mu*A*np.sqrt(2*g*Dh) # [m^3 s^-1] debiet
    q = Q/b # [m^2 s^-1] debiet per eenheid breedte

    H_S = np.linspace(H_B,H_m,1000)

    def rho_0(type):
        if type=='slot':
            K = 1.7
            # rho_0 [kg m^-3] dichtheid onttrokken water:
            rho_0 = rho_1 - (rho_1-rho_2)/2 * (1 - gp**(1/3)*(H_S-H_G)/(K*q**(2/3)))
            rho_0[H_S > H_G + K*q**(2/3)/gp**(1/3)] = rho_1
            rho_0[H_S < H_G - K*q**(2/3)/gp**(1/3)] = rho_2
        elif type=='orifice':
            K = 0.6
            # rho_0 [kg m^-3] dichtheid onttrokken water:
            rho_0 = rho_1 - (rho_1-rho_2)/2 * (1 - gp**(1/5)*(H_S-H_G)/(K*Q**(2/5)))
            rho_0[H_S > H_G + K*Q**(2/5)/gp**(1/5)] = rho_1
            rho_0[H_S < H_G - K*Q**(2/5)/gp**(1/5)] = rho_2
        return rho_0

    plt.clf()
    plt.figure(figsize=(5,5))
    plt.gca().axhline(H_G, color='black', linestyle='--')
    plt.text(rho_1-2.5, H_G, '$H_G$')
    plt.axis([rho_1-1,rho_2+1,H_B,H_m])
    plt.grid()
    plt.xlabel('output concentration [kg/m3]')
    plt.ylabel('$H_S$ [mNAP]')
    plt.title('output density ($D = {}$m)'.format(D))

    plt.plot(rho_0('slot'), H_S, '-', label='slot')
    plt.plot(rho_0('orifice'), H_S, '-', label='orifice')
    plt.legend()

    plt.savefig('figures/output_density{}.png'.format(ii))

    ii+=1
    