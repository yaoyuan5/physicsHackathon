import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation

import calculation as calc

N=50
dt=0.00001
dx=0.01
speed = 80
x=arange(-8,8,dx)
hbar=1.
m=1.
DATA = []


def init():
    line.set_data([], [])
    step_text.set_text('')
    return line, step_text

def animate(i):
    y = DATA[i]
    line.set_data(x, y)
    step_text.set_text("steps: " + str(i))
    return line, step_text



    

if __name__ == "__main__":

    #
    # initialize all variables
    #
    runtime = time.time()
    V = map(calc.V,x)

    #
    # Do the steps to solve Schroedingers equation
    #
    psi0 = exp(-x**2)
    DATA.append(abs(psi0)**2)

    for k in range(N):
        psi1 = calc.nlStep(psi0,x,V,dt)
        psi2 = calc.fStep(psi1,x,dt)
        DATA.append(abs(psi2)**2)
            
    #
    # plot the result
    #
    fig = figure()
    ax = axes(xlim=(-8, 8), ylim=(-1, 10))
    line, = plot([], [], lw=2)
    step_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=N, interval=speed, blit=True)
    plot(x, V)
    print "\n\n" + "program done in " + str(time.time() -runtime) + "\n\n"
    show()
