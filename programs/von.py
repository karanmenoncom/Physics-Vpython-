from vpython import *
import random as random
N = 100 # points to plot the function
graph = canvas( width=1600, height =900, title= 'vonNeumann Rejection Int' )
xsinx = curve( x=list(range(0,N)) , color=color.yellow , radius =0.5)
pts = label(pos=vec(-60, -60,0),text= 'points=', box=0) 
pts2 = label( pos=vec(-30, -60,0) , box=0)
inside = label( pos=vec(30 , -60,0) , text= 'accepted=' , box=0)
inside2 = label( pos=vec(60 , -60,0) , box=0)
arealbl = label( pos=vec( -65,60,0) , text= 'area=' , box=0)
arealbl2 = label(pos=vec( -35 ,60,0) , box=0)
areanal = label( pos=vec(30 ,60,0) , text= 'analytical=' , box=0)
zero = label( pos=vec(-85,-48,0) , text= '0' , box=0)
five = label( pos=vec( -85,50,0),text='5' , box=0)
twopi = label( pos=vec(90 , -48,0) , text= '2pi' , box=0)
def fx (x) : 
    return x*sin(x)*sin(x)
def plotfunc():
    incr = 2.0*pi/N
    for i in range (0,N) :
        xx = i*incr
        xsinx.x[i] = ((80.0/pi)*xx -80)
        #xsinx.y[i] = 20*fx(xx)-50
    #box = curve(pos=[(-80,-50),(-80,50),(80 ,50),(80,-50),(-80,-50)] ,color=color.white )

plotfunc()
j = 0
Npts=3001
analyt=( pi )**2
areanal.text = 'analytical ='
genpts = points()
for i in range (1,Npts):
    rate (500)
    x = 2.0*pi*random.random()
    y=5*random.random()
    xp = x*80.0/pi -80
    yp = 20.0*y-50
    pts2.text = '%4s'
    if y <= fx(x) :
        j += 1
        genpts.append( pos=vec(xp ,yp,0),color=color.cyan )
        inside2.text= '%4s'
    else: 
        genpts.append(pos=vec(xp,yp,0),color=color.green)
boxarea=2.0*pi*5.0
area = boxarea*j/(Npts-1)
arealbl2.text = '%8.5 f'
