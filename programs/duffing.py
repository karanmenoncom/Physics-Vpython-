from vpython import *
graph1=graph(width=1600,height=800)
t0 = 0.0
dt = 0.01
t_final = 1000
T = arange(t0, t_final, dt)
alpha, beta = -1,1
delta,gamma,omega=0.3,0.38,1.2
x,y=1,0
ode=gcurve(pos=(x,y),color=color.red)
for t in T:
    new_x = x + y*dt
    new_y = y + (gamma*cos(omega*t)-delta*y-alpha*x-beta*x**(3))*dt

    ode.plot(new_x,new_y)
    #rate(100)
    x, y = new_x, new_y
