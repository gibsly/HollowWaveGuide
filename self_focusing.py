#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:45:00 2018

@author: steven
"""

import numpy as np
'''
Define Variables:
    n  = 1.3,1.4,1.5,1.6 (m**2/W)
    d  = non-linear depth
    P  = Power (mW)
    w  = Beam Radius (mm)
    wl = Wavelength (m)
'''
n, d, P, w, wl = 1.5, 1, 35, 0.520*0.5, 1064*10**-9
#Set the non-linear index of refraction (m**2/W):
if n == 1.6:
    n2 = 2.8e-22
if n == 1.5: #GLASS
    n2 = 2.9e-16 #cm**2/W
if n == 1.4:
    n2 = 3.2e-22
if n == 1.3:
    n2 = 3.45e-22
'''
Activate various calculations:
    a ~ Diotric Power
    b ~ Critical Power
    c ~ Plot index of refraction vs Power
'''
a = 0
b = 1
c = 0 #1~air, #2~glass
'''
Section contains the calculations:
'''
if a == 1:
    Diotric_Power = (4*n2*d)/(np.pi*w**4)*P
if b == 1:
    P_crit = (0.148*wl**2) / (n*n2)
if c == 1:
    n2_air = 1
    step_size= 0.1
    min_p, max_p = 0, 50
    P = np.arange(min_p,max_p,step_size)     
    n = 1 + n2_air * ((2*P)/(np.pi*w**2))
if c == 2:
    step_size= 0.1
    min_p, max_p = 0, 50
    P = np.arange(min_p,max_p,step_size)     
    n = 1 + n2 * ((2*P)/(np.pi*w**2))    

