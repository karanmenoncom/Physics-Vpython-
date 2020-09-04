from vpython import *
graph=canvas(width=1600,height=800)
ode=curve(color=color.green)
t0 = 0.0
dt = 0.01
t_final = 1000
T = arange(t0, t_final, dt)
alpha, beta = 10.82, 14.286
a, b, c, d = 1.3, .11, 7, 0
ode=curve(pos=(1,1,0),color=color.green)
x=1;y=1;z=0
for t in T:
    h = -b*sin(pi*x/(2*a)+d)
    new_x = x + alpha*(y-h) * dt
    new_y = y + (x - y + z) * dt
    new_z = z - beta*y*dt
    v=(new_x,new_y,new_z)
    ode.append(pos=v)
    rate(300)
    x, y, z = new_x, new_y, new_z

