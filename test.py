from numpy import *
from pylab import *
import time


N=80
dt=0.01
x=arange(-100,100,0.1)
hbar=1.
m=1.
def V(x):
    return x



def nonlinearStep( data_init,x, dt):
    data1=data_init+V(x)*data_init*dt/(1.j*hbar)
    return data1
def fourierStep(data_init,x,dt):
    data1=fft(data_init)
    data2=fftshift(data1)
    h=fftfreq(len(x), x[3]-x[2])
    h1=fftshift(h)
    data3= -h1**2*data2*dt*1.j*hbar/(2.*m) +data2
    
    data4=ifftshift(data3)
    data5=ifft(data4)
    return data5
    


if __name__ == "__main__":
    DATA=[]
    
    
    runtime = time.time()
    
    V_array= V(x)
    f_ini=exp(-x**2)
    for j in range(N):
        
        f_nl=nonlinearStep(f_ini,x,dt)
        f_l=fourierStep(f_nl,x,dt)
        
        f_ini=f_l
        DATA.append(f_ini)
        
        

    
    


    print "program done in " + str(time.time() -runtime)




