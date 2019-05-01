'''
Calculate attenuation constant using derived equation
from Bell labs paper.
Additionally, several convient functions are defined for
practical use.

Steven Sheppard
Hollow Waveguide Research
CSU Chico, Physics
'''

import numpy as np
from numpy import pi, sqrt, cos, real
import scipy.special as bs

'''
Define constants, many are found in Bell Labs paper
'''
wl = 1.064*10**-6  # Wavelength (m)
a = 0.000375  # Fiber radius (m)
k = (2 * pi) / wl  # freespace propogation constant (1/m)
n, m = 1, 1  # Transverse Mode Order
theta = 0  # angle of polarization w/respect to bending plane

'''
Define Functions:
    a ~ dB from Power Ratio
    b ~ Power Ratio from dB
    c ~ Special solutions dependent on modes
    d ~ Delta function dependent on "n"
    e ~ Function V() from Bell labs bend attenuation
    f ~ Final attenuation constant, straight + bend
Reference pg. 35 of lab book for attenuation calculations
'''


def db_perc(ratio):
    return -10*np.log10(ratio)


def perc_db(db):
    return 10**(-db/10)


def dB_m(ratio, L):
    return db_perc(ratio)/L


def f(v):
    if TE0m == 1:
        return(1/sqrt(v**2-1))
    if TM0m == 1:
        return(v**2/sqrt(v**2-1))
    if EHnm == 1:
        return(0.5*(v**2+1)/sqrt(v**2-1))


def V(v, n, theta):
    if n == 1 or n == -1:
        delta_n = 1
    else:
        delta_n = 0
    a = f(v) * (4/3) * (2*pi/unm)**2
    b = 1 - n * (n-2)/unm**2 + (3/4) * ((v**2-1)/(v**2+1))*cos(2*theta)*delta_n
    return a * b


def Attenuation(a, n, v, wl, unm, R):
    straight_loss = (unm/(2*pi))**2 * (wl**2 / a**3) * real(f(v))
    bend_loss = (a**3 / (wl**2 * R**2)) * real(V(v, n, theta))
    return (straight_loss + bend_loss)


'''
Calculations for transmission, curvature and the attunuation constant
are done based on input parameters.
'''

# Turn calculation on and off by True/False
calc_transmission = False
calc_curvature = False
calc_attenuation_const = False

# Turn mode style on and off and set n & m:
TE0m = False
TM0m = False
EHnm = True
n,m  = 1,1

# Input the complex refractive index [v]:
v = 1.5

# The zeroth order root to the bessel function
unm  = bs.jn_zeros(n-1,m)[-1]

# Polarization angle with respect to plane of curvature. 
# Max attenuation theta = 0
theta = 0 #p.pi/2

# Calculations for quick Reference & use in other applications

if calc_transmission is True:
    p_in = float(input('Power in:'))
    p_out = float(input('Power out:'))
    print('efficiency:', p_out/p_in)

if calc_curvature is True:
    da = float(input('End Displacement:'))  # 1mm
    L = float(input('Fibre length:'))  # m
    R = da/2 + L**2/(8*da)  # m
    print(R, 'm')

if calc_attenuation_const is True:
    attenuation = Attenuation(a, n, v, wl, unm, R)
    print(attenuation, 'dB/m')

'''
Check with given solutions from Bell Labs paper:
    For given initial conditions the ratio of V() theta=max
    to V() theta = min
''' 

ratio_V = V(1.5,1,0) / V(1.5,1,pi/2)
ka = (pi*2*a)/wl
v_u = v*unm
ratio_ka = ka/v_u
