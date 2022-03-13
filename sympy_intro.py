import numpy
import sympy

from sympy import init_printing
init_printing(use_latex=True)

x, nu, t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
       sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))
phi

phiprime = phi.diff(x)
phiprime



from sympy.utilities.lambdify import lambdify

u = -2 * nu * (phiprime / phi) + 5



ufunc = lambdify((t, x, nu), u)

from matplotlib import pyplot

###variable declarations
nx = 101
nt = 101
dx = 2 * numpy.pi / (nx - 1)
nu = 0.1
dt = dx * nu

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t = 0

u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])

pyplot.plot(x, u, marker='x', lw=1)

for n in range(nt):
    un = u.copy()
    for i in range(1,nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *\
                (un[i+1] - 2 * un[i] + un[i-1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
                (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]
        
u_analytical = numpy.asarray([ufunc(nt * dt, xi, nu) for xi in x])

pyplot.show()
pyplot.plot(x,u, marker='', lw=1, label='Computational')
pyplot.plot(x, u_analytical, label='Analytical')
pyplot.legend();
