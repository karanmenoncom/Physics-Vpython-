from vpython import *
import numpy as np

graph=canvas(width=1600,height=800)
ball1=sphere(pos=vec(-100,0,0),radius=3,color=color.red)
ball2=sphere(pos=vec(100,0,0),radius=3,color=color.green)

for x in range(0,97):
    rate(20)
    ball1.pos= ball1.pos+vec(1,0,0)
    ball2.pos=ball2.pos+vec(-1,0,0)
    if ball1.pos==vec(-3,0,0) and ball2.pos==vec(3,0,0):
        for y in range(0,97):
            rate(20)
            ball1.pos=ball1.pos+vec(-1,0,0)
            ball2.pos=ball2.pos+vec(1,0,0)