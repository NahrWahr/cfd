import numpy
from matplotlib import pyplot
import time, sys

pyplot.ion()

nx = 50
dx = 0.5
nt = 50
dt = .05
c = 2

u = numpy.ones(nx)
u[int(.5/dx) : int(1/dx+1)] = 2
#u[0 : 1] = 2
#print(.5/dx,1/dx+1,dx)

un = numpy.ones(nx)

pyplot.plot(numpy.linspace(0, 2, nx), u)


for n in range(nt):
    un = u.copy()
    pyplot.draw()
    #pyplot.flush_events()
    for i in range(1,nx):
        u[i] = un[i] - un[i]*dt/dx*(un[i] - un[i-1])
        #u[i] = un[i] - c*dt/dx*(un[i] - un[i-1])
        
pyplot.plot(numpy.linspace(0, 2, nx), u);
