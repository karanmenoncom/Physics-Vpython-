from vpython import *
graph1=canvas(width=1600,height=800)
dt = 0.01
t0 = 0.0
dt = 0.01
t_final = 10000
T = arange(t0, t_final, dt)
alpha, beta = -1,1
delta,gamma,omega=0.3,0.54,pi/4
x,y,=1,0
ode=points(pos=(x,y,0),color=color.red)
count=0
for t in T:

    new_x = x + y*dt
    new_y = y+(gamma*cos(omega*t)-delta*y-alpha*x-beta*x**(3))*dt
    v=(new_x,new_y,0)
    count+=1
    if count%8==0:
        rate(100)
        ode.append(pos=v)
        x, y = new_x, new_y
    else:    
        
        x, y = new_x, new_y
