#from vpython import *
#from vpython import graph
import random




#graph1 = graph(title='Monte Carlo Circle', xtitle= 'x', ytitle = 'y')



Nbox=0
Ncirc=0
for i in range(10**9):
    
    x=random.choice([random.random(),-1*random.random()])
    y=random.choice([random.random(),-1*random.random()])
    if x*x +y*y<=1:
        #yes=(x,y,0)
        #points(pos=yes)
        #rate(30)
        #X=append(X,x)
        #Y=append(Y,y)
        Ncirc+=1
    else:
        Nbox+=1

result=4*(Ncirc)/(Nbox+Ncirc)
print(result)
