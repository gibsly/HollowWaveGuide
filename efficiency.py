"""
Steven Sheppard
Plotting and curve fit for attentuation constant \alpha
"""
import pylab as py
from scipy.optimize import curve_fit


def db_perc(ratio):
    return -10*py.log10(ratio)


def Alpha(L, alpha):
    Trans = py.exp(-alpha * L)
    return Trans


# Insert data for efficiency measurements:
trans = [0.8, 0.6, 0.55, 0.4, 0.3]  # ratio
length = [0.2, 0.5, 0.75, 1.0, 1.5]  # m

# Curve Fit for alpha:
Length = py.linspace(0, 2, 100)
fit = py.zeros(len(Length))
opt, cov = curve_fit(Alpha, length, trans)
yerr = 0
xerr = 0
perr = py.sqrt(py.diag(cov))

for i in range(len(Length)):
    fit[i] = Alpha(Length[i], opt[0])

py.figure(1)
py.title('Attenuation Constant $\alpha$')
py.xlabel('')
py.ylabel('')
py.plot()
py.legend()
py.show()