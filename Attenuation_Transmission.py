'''
Project: Hollow Core Fiber
Purpose: Calculate the Attenuation & Theoretical Transmission
author: Steven Sheppard

                Units of length must be in METERS
                LB = Lab Book
'''
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
'''
Program Outline:
    1 - Turn Functions on and off (True/False)
    2 - Constants
    3 - Definitions
    4 - Calculations
    5 - Plotting Routines
Functions:
    1 ~ Attenuation:
        Losses [db/m]
        Transmission [%]
Plotting:
    1 ~
'''
Attenuation = False
Plotting1 = True
Plotting2 = True
Plotting3 = True

# Constants:
wl = 1.064*10**-6  # Wavelength [m]
a = 375* 10**-6  # Fiber radius [m]
L = 1.90  # Fiber length [m]
v = 1.5  # Index of Refraction of fiber
r = 375*10**-6  # Coupling Beam Radius [m]
n, m = 1, 1  # Mode Numbers
mode  = 0  # Mode Character: 0-EH, 1-TE, 2-TM
unm   = sp.jn_zeros(n-1, m)[-1]  # mth root of J_n-1(unm)=0
theta = 0  # Angle of Polorization with respect to Bend Plane (Max=0, Min=pi/2)
wla  = wl**2 / a**3  # Proportional to attenuation constant
R     = 50  # Radius of Curvature [m]
da    = 2.0*10**-3  # Displacement from straight, (LB pg.39)

'''
Definitions:
    1 ~ Unm : mth root of J_n-1(unm)=0.
    2 ~ Radius of Curvature given displacement of ends (LB pg.39)
    3 ~ Mode: Returns TE, TM, EH specific solution for atteunation caluclation.
    4 ~ Delta: Dependent on (n), affects whether theta matters.
    5 ~ V: V(v) as defined in Bell Labs equation 45.
    6 ~ Straight: Attenuation constant for straight losses, Bell Labs equation 22
    7 ~ Bend: Attenuation constant for bending losses, Bell Labs equation 44
'''


def Unm(n, m):
    return sp.jn_zeros(n-1, m)[-1]


def Radius(ds, L):
    return (ds/2) + L**2 / (8*ds)


def Mode(v):
    if mode == 0: #EH
        return 0.5 * (v**2 + 1) / (np.sqrt(v**2 -1))
    if mode == 1: #TE
        return 1 / (np.sqrt(v**2 -1))
    if mode == 2: #TM
        return v**2 / (np.sqrt(v**2 -1))


def Delta(n):
    if n == 1 or n == -1:
        return 1
    else:
        return 0


def V(v):
    a = 4/3 * (2*np.pi / unm)**2 * Mode(v)
    b = 1 - (n**2-2*n) / unm**2 + (0.75) * Delta(n) * (v**2 - 1) / (v**2 + 1) * np.cos(2*theta)
    return a * b


def Straight():
    return (unm / (2*np.pi)**2) * wla * Mode(v)


def Bend():
    return wla**-1 * R**-2 * np.real(V(v))


''' 
Calculations:
'''
if Attenuation == True:
    Losses       = 8.6858 * (Straight() + Bend()) #[dB/m]
    Transmission = 10**(-Losses*L/10) #[%]
    Bend_Radius = (da/2) + L**2/(8*da) #[m]
    Displacement = R - np.sqrt(R**2 - L**2/4)#[m]

'''
Plotting:
    1 - Straight Transmission: 1.9m fiber, 1064nm, a=0.375mm,v=1.5
        Vary the modes: EH11, EH22, EH33, EH44
    2 - Straight + Bend Attenuation: 1.9m fiber, 1064nm, a=0.375mm,v=1.5, da=2mm
        Vary the modes: EH11, EH22, EH33, EH44
    3 - Straight + Bend Attenuation: 1.9m fiber, 1064nm, a=0.375mm,v=1.5
        Vary the Bend Radius & Modes
'''

if Plotting1 == True:
    start, stop, num = 1, 1000, 10000
    bend_range = np.linspace(start, stop, num)
    transmission = np.zeros([num, 4])
    for mod in range(4):
        for r in range(num):
            n,m = mod+1, mod+1
            unm = Unm(n, m)
            R   = bend_range[r]
            Losses = 8.6858 * (Straight() + Bend()) #[dB/m]
            Transm = 10**(-Losses*L/10) #[%]
            transmission[r,mod] = Transm
    plt.figure()
    plt.plot(bend_range, transmission[:,0], label = 'EH11')
    plt.plot(bend_range, transmission[:,1], label = 'EH22')
    plt.plot(bend_range, transmission[:,2], label = 'EH33')
    plt.plot(bend_range, transmission[:,3], label = 'EH44')
    plt.title('Transmission Curves For Multiple Modes')
    plt.xlabel('Radius of Curvature [m]')
    plt.ylabel('Transmission [%]')
    plt.xscale('log')
    plt.legend()
    


        
 


