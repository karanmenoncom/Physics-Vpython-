from vpython import *
graph=canvas(width=1600,height=800)
ode=curve(color=color.yellow)
t0 = 0.0
dt = 0.01
t_final = 1000
T = arange(t0, t_final, dt)
a=0.1;b=0.1;c=14
x,y,z=1,1,0
ode=curve(pos=(x,y,z),color=color.yellow)
for t in T:
    new_x = x+ (-y-z)*dt
    new_y =y+(x+a*y)*dt
    new_z = z+(b+z*(x-c))*dt
    v=(new_x,new_y,new_z)
    ode.append(pos=v)
    rate(300)
    x, y, z = new_x, new_y, new_z
