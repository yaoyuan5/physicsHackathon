import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation

N=200
dt=0.01
dx=0.001
x=arange(-8,8,dx)
hbar=1.
m=1.
DATA = []


def init():
    line.set_data([], [])
    return line,

def animate(i):
    y = DATA[i]
    line.set_data(x, y)
    return line,

def V(x):
    if x**2 > 100.:
        return 100
    else:
        return x**2


def nonlinearStep( data_init,x, V_array, dt):
    data1 = data_init+V_array*data_init*dt/(1.j*hbar)
    return data1


def fourierStep(data_init,x,dt):
    data1 = fft(data_init)
    data2 = fftshift(data1)
    h = fftfreq(len(x), (x[3]-x[2]))
    h1 = fftshift(h)
    data3 = -4*pi**2*h**2*data1*dt*1.j*hbar/(2.*m) +data1
    
    data4 = ifftshift(data3)
    data5 = ifft(data1)
    return data5
    

if __name__ == "__main__":
    runtime = time.time()

    V_array = map(V,x)


    f_ini = exp(-x**2)

    for k in range(N):
        a = nonlinearStep(f_ini,x,V_array,dt)
        f_nl = a
        b = fourierStep(a,x,dt)
        f_l = b
            
        f_ini = b
        DATA.append(f_ini)
            
    print "\n\n" + "program done in " + str(time.time() -runtime) + "\n\n"
    fig = figure()
    ax = axes(xlim=(-8, 8), ylim=(-1, 2))
    line, = plot([], [], lw=2)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
    show()
