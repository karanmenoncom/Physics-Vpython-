from numpy import *
x,y =mgrid[-3:3:100j,-3:3:100j]
z= sin(x**2+y**2)
from mayavi import mlab
mlab.surf(x,y,z)

