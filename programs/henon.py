from vpython import *
graph1=canvas(width=1600,height=800)
#t0 = 0.0
#dt = 0.01
#t_final = 1000
#T = arange(t0, t_final, dt)
T=arange(0,1000,0.01)
a=1.4;b=0.3
x,y=0.1,0.1
ode=points(pos=(x,y,0),color=color.yellow)
for t in T:
    new_x = 1-a*x*x+y
    new_y = b*x

    v=(new_x,new_y,0)
    ode.append(pos=v)
    rate(100)
    x, y = new_x, new_y

