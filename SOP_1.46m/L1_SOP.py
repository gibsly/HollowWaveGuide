# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:25:28 2018

@author: physicsstudent
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:28:08 2018

@author: sshep
"""

import numpy as np
import pylab as py
from matplotlib.pyplot import figure, show

py.close('all')

before = np.loadtxt('L1_sop_bf.txt', skiprows=1) 
after  = np.loadtxt('L1_sop_af.txt', skiprows=1) 
c_before = np.loadtxt('L1_sop_circ_bf.txt', skiprows=1) 
c_after  = np.loadtxt('L1_sop_circ_af.txt', skiprows=1) 

pin = 20.12
pout = [10.66/pin, 10.42/pin,11.83/pin]
c_pin_bf, c_pin_af  = 16.92, 7.763

b_angle = before[:,0]*np.pi/180
a_angle = after[:,0]*np.pi/180
t_bf    = after[:,1]
t_af    = after[:,1]

c_b_angle = c_before[:,0]*np.pi/180
c_a_angle = c_after[:,0]*np.pi/180
c_t_bf    = c_before[:,1]/c_pin_bf
c_t_af    = c_after[:,1]/c_pin_bf

'''
#Power Comparison
fig = py.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],
                  projection='polar')
py.title('State of Polarization c_before & c_after Fiber')
ax.plot(c_b_angle, c_before[:,1], 'or', label='Power c_before Fiber [mW]')
ax.plot(c_a_angle, c_after[:,1], 'ob', label='Power c_after Fiber [mW]')
ax.legend()
py.show()
py.savefig('L1_SOP_power.png')
'''
x = 4.5
#Transmission Comparison
fig = py.figure(figsize=(x,x))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],
                  projection='polar')
py.title('State of Polarization Before & After Fiber')
ax.plot(c_b_angle, c_t_bf, 'or', label='Incident Power')
ax.plot(c_a_angle, c_t_af, 'ob', label='Transmitted Power')
ax.legend(bbox_to_anchor=(.43,0.045))
py.show()
py.savefig('L1_SOP_circ_trans.png')
'''
#Power Comparison
fig = py.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],
                  projection='polar')
py.title('State of Polarization Before & After Fiber')
ax.plot(b_angle, before[:,1], 'or', label='Incident Power')
ax.plot(a_angle, after[:,1], 'ob', label='Transmitted Power')
ax.legend()
py.show()
py.savefig('L1_SOP_power.png')
'''
#Transmission Comparison
fig = py.figure(figsize=(x, x))
ax = fig.add_axes([0.1, 0.09, 0.8, 0.8],
                  projection='polar')
py.title('State of Polarization Before & After Fiber')
ax.plot(b_angle, before[:,1]/max(before[:,1]), 'or', label='Incident Power')
ax.plot(a_angle, after[:,1]/max(before[:,1]), 'ob', label='Transmitted Power')
ax.legend(bbox_to_anchor=(.43,0.045))
py.show()
py.savefig('L1_SOP_trans.png')





