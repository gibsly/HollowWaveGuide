# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:28:08 2018

@author: sshep
"""

import numpy as np
import pylab as py
from matplotlib.pyplot import figure, show

py.close('all')

w_array = np.loadtxt('Caustic_350.txt', skiprows=1) #0-Distance 1-x 2-y
py.figure()
py.plot(w_array[:,0], w_array[:,1]/1000, 'ob', label='x-width', linewidth=3)
py.plot(w_array[:,0], w_array[:,2]/1000, 'or', label='y-width', linewidth=3)
py.plot(np.full(2,30.5), np.linspace(0.55,0.75,2), 'r', label='Median Focus', linewidth=3)
py.title('Beam Diameter Near the Waist', fontsize = 18)
py.xlabel('Distance [cm]', fontsize = 15)
py.ylabel('Diameter [mm]', fontsize = 15)
py.legend(fontsize=15)

p_array = np.loadtxt('Polarization.txt')
angles = p_array[:,0]*np.pi/180
tranafter = p_array[:,2]
transbefo = p_array[:,4]
# force square figure and square axes looks better for polar, IMO
fig = figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1,.8, .8], projection='polar')
ax.plot(angles, transbefo, 'ob', lw=3, label='Before Fiber')
ax.plot(angles, tranafter, 'or', lw=3, label='After Fiber')
ax.legend(fontsize = 20)


show()
