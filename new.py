import sys
import time

import sys
import time
from numpy import *
from pylab import *
N=200
dt=0.01
dx=0.001
x=arange(-10,10,dx)
hbar=1.
m=1.
def V(x):
    if abs(x)>100.:
        return 0
    else:
        return x**2



def nonlinearStep( data_init,x, V_array, dt):
    data1=data_init+V_array*data_init*dt/(1.j*hbar)
    
    return data1
def fourierStep(data_init,x,dt):
    data1=fft(data_init)
    data2=fftshift(data1)
    h=fftfreq(len(x), (x[3]-x[2]))
    h1=fftshift(h)
    data3= -4*pi**2*h**2*data1*dt*1.j*hbar/(2.*m) +data1
    
    data4=ifftshift(data3)
    data5=ifft(data1)
    return data5
    

DATA=[]

V_array=[]
for j in arange(0,len(x)):
    V_array.append(V(x[j]))
V_array=array(V_array)
    
f_ini=exp(-x**2)
for k in range(N):
    a=nonlinearStep(f_ini,x,V_array,dt)
    f_nl=a
    b=fourierStep(a,x,dt)
    f_l=b
        
    f_ini=b
    DATA.append(f_ini)
        
