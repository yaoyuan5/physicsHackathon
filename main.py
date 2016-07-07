
import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation

N=50
dt=0.00005
dx=0.01
speed = 80
x=arange(-8,8,dx)
hbar=1.
m=1.
DATA = []


def init():
    line.set_data([], [])
    time_text.set_text('')
    energy_text.set_text('')
    return line, time_text, energy_text

def animate(i):
    y = DATA[i]
    line.set_data(x, y)
    time_text.set_text(str(i))
    energy_text.set_text(str(i))
    return line, time_text, energy_text

def V(x):
        return 0
    #elif x < 0:
        #return 0


def nonlinearStep( data_init,x, V_array, dt):
    data1 = data_init+V_array*data_init*dt/(1.j*hbar)
    return data1


def fourierStep(data_init,x,dt):
    data1 = fft(data_init)
    
    h = fftfreq(len(x), (x[3]-x[2]))
    
    data3 = data1*exp(-1j*hbar*h**2*4*pi**2*dt/(2.*m))
    
    data5 = fft(data3)
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
        DATA.append(abs(f_ini)**2)
            
    fig = figure()
    ax = axes(xlim=(-8, 8), ylim=(-1, 10))
    line, = plot([], [], lw=2)
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=N, interval=speed, blit=True)
    plot(x, V_array)
    print "\n\n" + "program done in " + str(time.time() -runtime) + "\n\n"
show()
