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

c_before = np.loadtxt('L1_sop_circ_bf.txt', skiprows=1) 
c_after  = np.loadtxt('L1_sop_circ_af.txt', skiprows=1) 

c_pin_bf, c_pin_af  = 16.92, 7.763

c_b_angle = c_before[:,0]*np.pi/180
c_a_angle = c_after[:,0]*np.pi/180
c_t_bf    = c_before[:,1]/c_pin_bf
c_t_af    = c_after[:,1]/c_pin_af
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
#Transmission Comparison
fig = py.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],
                  projection='polar')
py.title('State of Polarization c_before & c_after Fiber')
ax.plot(c_b_angle, c_t_bf, 'or', label='Power c_before Fiber')
ax.plot(c_a_angle, c_t_af, 'ob', label='Power c_after Fiber')
ax.legend()
py.show()
py.savefig('L1_SOP_trans.png')
