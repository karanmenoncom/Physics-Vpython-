from vpython import*
import random as random
graph1=canvas(width=1600,height=800)
walk=curve(pos=(0,0,0),color=color.cyan)
N=1000
x,y,z=0,0,0
for i in range(0,N):
    (dx,dy,dz)=random.choice([(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)])
    x+=dx
    y+=dy
    z+=dz
    v=(x,y,z)
    walk.append(pos=v)
    rate(30)
