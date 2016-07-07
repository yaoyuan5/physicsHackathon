"""
    module for all the claculations
"""
from numpy import *
from pylab import *

# constants
hbar=1.
m=1.


# The potential for the Schroedinger equation
def V(x):
    if abs(x) < 5:
        return 0
    else:
        return 5


# A nonlinear step
def nlStep( data_init,x, V_array, dt):
    data1 = data_init+V_array*data_init*dt/(1.j*hbar)
    return data1


# A step in the k-space
def fStep(data_init,x,dt):
    data1 = fft(data_init)
    
    h = fftfreq(len(x), (x[3]-x[2]))
    
    data3 = data1*exp(-1j*hbar*h**2*4*pi**2*dt/(2.*m))
    
    data5 = fft(data3)
    return data5
