from vpython import *
graph=canvas(width=1600,height=800)
ode=curve(color=color.yellow)
t0 = 0.0
dt = 0.01
t_final = 100
T = arange(t0, t_final, dt)
alpha, beta = 10.82, 14.286
s=10;r=28;b=8/3
ode=curve(pos=(1,1,0),color=color.yellow)
x=1;y=1;z=0
for t in T:
    new_x = x+ s*(y-x)*dt
    new_y =y+(r*x-y-x*z)*dt
    new_z = z+(x*y-b*z)*dt
    v=(new_x,new_y,new_z)
    ode.append(pos=v)
    rate(300)
    x, y, z = new_x, new_y, new_z

