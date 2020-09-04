from vpython import *
display=canvas(height=800,width=1800)
x,y,z,vx,vy=0.55,0,0,0.0,1.63
track=curve(pos=vec(x,y,z),color=color.yellow)
planet=sphere(pos=vec(x,y,z),color=color.blue,radius=0.01)
Sun =sphere(pos=vec(0,0,0),color=color.yellow,radius=0.1)
T=arange(0,1000,0.1)
G=1 ;M=1
dt=0.01
def fx():
    return vx
def fy():
    return vy
def fvx():
    return -G*M*x/((x*x+y*y)**(3/2))
def fvy():
    return -G*M*y/((x*x+y*y)**(3/2))
for t in T:
    rate(30)
    x=x+dt*(fx())
    y=y+dt*(fy())
    vx+=dt*(fvx())
    vy+=dt*(fvy())
    v=vec(x,y,0)
    track.append(pos=v)
    planet.pos=v