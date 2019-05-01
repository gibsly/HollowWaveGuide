# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pylab as p
p.close('all')
data = p.loadtxt('caustic_18.11.04_L2.1.txt', skiprows=1)
x    = data[:,0]/100
u    = data[:,1]/1000
v    = data[:,2]/1000
el   = data[:,3]


p.figure(figsize=(8, 4.5))
p.plot(x,u,'r.', label='u-radius')
p.plot(x,v,'b.', label='v-radius')
p.title('Beam Profile at Fiber Tip', fontsize=18)
p.xlabel('Distance From Center of Iris2 [m]', fontsize=14)
p.ylabel('Beam Diameter [mm]', fontsize=14 )
p.legend(fontsize=14)


p.figure()
p.plot(x, el, 'b.')