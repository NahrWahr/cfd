from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot, cm

x,y=4,4

u = numpy.ones((x,y))

for i in range(0,x):
    for j in range(0,y):
        
        u[i,j]=(i+1)*(j+1)

print(u[1,:])

"""fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
print(X,Y)

ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)

pyplot.show()"""
