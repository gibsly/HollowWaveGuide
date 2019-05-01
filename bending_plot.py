#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:21:28 2019

@author: steven
"""
import pylab as py
from scipy.optimize import curve_fit 
import scipy.special as bs
py.close('all')

a = 750*10**-6
wl = 1.064*10**-6
L = 1.46

def db_perc(ratio):
    return -10*py.log10(ratio)

def Test(R, A):
    return (4/3) * A * ((2*py.pi *a)/(wl))**4 * (a/R)**2

#import data
data = py.loadtxt('bend_data.txt', skiprows=1) 
radius = data[:,2]
trans = data[:,7]
alpha = db_perc(trans)/L
py.figure('Bending Loss')
py.plot(radius, alpha,'ro')

#Curve Fit
rad = py.linspace(0.1,max(radius),100)
fit = py.zeros(len(rad))
opt, cov = curve_fit(Test, radius,alpha)
yerr = data[:,8]
xerr = 0.1
perr = py.sqrt(py.diag(cov))
for i in range(len(rad)):
    fit[i] = Test(rad[i],opt[0])

    
#Plot the data and fit:
py.figure(figsize=(5.5,3.5), dpi=120)
py.title(r'Bend Losses $\alpha(R)$',fontsize=14)
py.xlabel('Radius of Curvature $[m]$',fontsize=12)
py.ylabel(r'$\alpha(R)$',fontsize=12) 
py.errorbar(radius,alpha, xerr=xerr, yerr=yerr, fmt='r.', label=r'$\alpha(R)$')
py.plot(rad,fit, 'b', label='Curve fit')
py.xlim(1,6.8)
py.ylim(0,4)
py.legend(fontsize=12)