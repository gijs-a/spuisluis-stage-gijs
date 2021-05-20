#! usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

opening_type = 'slot' # type opening ('orifice' of 'slot')

H_z = 6 # [mNAP] waterniveau zeezijde
H_m = 10 # [mNAP] waterniveau meerzijde
#H_G = 3.96 # [mNAP] locatie van dichtheidsinterface
H_S = -10 # [mNAP] locatie van as van opening
Dh = H_m - H_z # [m] verval over de spuisluis

mu = 1 # afvoercoefficient (0.6 - 1; bij kleine openingen vaak mu=1)
b = 20 # [m] breedte
A = b*0.1 # [m^2] open oppervlak beschikbaar voor lekkage
g = 9.81 # [m s^-2] gravitatieversnelling
rho_1 = 1000 # [kg m^-3] dichtheid zoet water
rho_2 = 1022 # [kg m^-3] dichtheid zout water
Drho = rho_2 - rho_1 # [kg m^-3] dichtheidsverschil
gp = 2*g*Drho / (rho_2+rho_1)

Q = mu*A*np.sqrt(2*g*Dh) # [m^3 s^-1] debiet
q = Q/b # [m^2 s^-1] debiet per eenheid breedte
# rho_0 [kg m^-3] dichtheid onttrokken water

def output_density(H_G, opening_type='slot'):
    if opening_type == 'orifice':
        K = 0.7
        #print(H_S - K*Q**(2/5)/(gp**(1/5)), '--', H_S + K*Q**(2/5)/(gp**(1/5)) )
        if H_G < H_S - K*Q**(2/5)/(gp**(1/5)):
            rho_0 = rho_1
        elif H_G > H_S + K*Q**(2/5)/(gp**(1/5)):
            rho_0 = rho_2
        else:
            rho_0 = rho_1 - 0.5*(rho_1 - rho_2) * (1 - gp**(1/5)*(H_S-H_G)/(K*Q**(2/5))) 
    elif opening_type == 'slot':
        K = 1.6
        #print(H_S - K*q**(2/3)/(gp**(1/3)), '--', H_S + K*q**(2/3)/(gp**(1/3)) )
        if H_G < H_S - K*q**(2/3)/(gp**(1/3)):
            rho_0 = rho_1
        elif H_G > H_S + K*q**(2/3)/(gp**(1/3)):
            rho_0 = rho_2
        else:
            rho_0 = rho_1 - 0.5*(rho_1 - rho_2) * (1 - gp**(1/3)*(H_S-H_G)/(K*q**(2/3)))
        
    return rho_0

rho_0 = output_density(H_G=0, opening_type=opening_type)
print('opening:', opening_type)
print('Q =', Q)
print('rho_0 =', rho_0)

#######################################################################
H_G_arr = np.linspace(-15,10,101)
rho_0_arr = np.zeros(H_G_arr.size)
for i in range(H_G_arr.size):
    H_G = H_G_arr[i]
    rho_0_arr[i] = output_density(H_G=H_G, opening_type=opening_type)

plt.figure(figsize=(10,10))
plt.plot(rho_0_arr, H_G_arr, 'o')
plt.xlim([1000,1022])
plt.xlabel('density [kg/m3]')
plt.ylabel('H_G [m]')
plt.title(opening_type)
plt.savefig('output_density_{}.png'.format(opening_type), bbox_inches='tight')