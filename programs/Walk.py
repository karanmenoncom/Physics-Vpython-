from vpython import *
from numpy import *
from vpython  import graph
import random

jmax = 20
x=0.0; y = 0.0 
graph1 = graph( width=500, height =500, title = 'Random Walk', xtitle= 'x',ytitle= 'y' )
pts = gcurve( color = color.yellow )
for i in range (0,jmax+1):
    pts.plot(pos=(x,y)) 
    x+=( random.random()-0.5)*2 
    y+= ( random.random()- 0.5)*2
    pts.plot(pos=(x,y ))
