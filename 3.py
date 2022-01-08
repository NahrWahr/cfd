import numpy                 #loading our favorite library
import sympy
from matplotlib import pyplot    #and the useful plotting library

from sympy import init_printing
init_printing(use_latex=False)
from sympy.utilities.lambdify import lambdify
pyplot.ion()

nx = 50
dx = 2 / (nx - 1)
nt = 100    #the number of timesteps we want to calculate
nu = 0.01   #the value of viscosity
sigma = 0.1 #sigma is a parameter, we'll learn more about it later
dt = sigma * dx**2 / nu #dt is defined using sigma ... more later!

u = numpy.ones(nx)
u[1:2] = 2
un = numpy.ones(nx) #our placeholder array, un, to advance the solution in time

x,nu,t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) + sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))
phiprime=phi.diff(x)


u = -2 * nu * (phiprime / phi) + 4

ufunc = lambdify((t,x,nu),u)

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t = 0

#u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])


#pyplot.plot(numpy.linspace(0, 2, nx), u);

        

