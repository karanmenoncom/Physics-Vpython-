from vpython import *
from vpython import graph
import random




graph1 = graph(title='Monte Carlo Circle', xtitle= 'x', ytitle = 'y')



Nbox=0
Ncirc=0
for i in range(10**4):
    
    x=random.choice([2*random.random(),0*random.random()])
    y=random.choice([2*random.random(),0*random.random()])
    if y-x*sin(x)*sin(x)<=0:
        yes=(x,y,0)
        points(pos=yes)
        rate(100)
        #rate(30)
        #X=append(X,x)
        #Y=append(Y,y)
        Ncirc+=1
    else:
        no=(x,y,0)
        points(pos=no,color=color.green)
        Nbox+=1

result=4*(Ncirc)/(Nbox+Ncirc)
print(result)
        

 
