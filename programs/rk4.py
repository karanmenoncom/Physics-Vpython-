# rk4 . py 4th order Runge Kutta
import numpy as np
from pylab import *
A=np.array([])
B=np.array([])
C=np.array([])
D=np.array([])
# Initialization
a = 0.
b = 10.
n = 100
ydumb = np.zeros((2),float) ; y = np.zeros((2) , float )
fReturn = np.zeros((2) , float ) ; k1 = np.zeros(( 2 ) , float )
k2 = np.zeros( ( 2 ) , float ) ; k3 = np.zeros( ( 2 ) , float )
k4 = np.zeros( ( 2 ) , float )
y[0] = 3.0; y[1] = -5.
t = a; h =(b-a)/n;
def f( t , y):# Force function
    fReturn[0] = y[1]
    fReturn[1] = -100.0*y[0] -2.0*y[1] + 10.0*sin(3.0*t )
    return fReturn

def rk4( t,h,n):
    k1 = [ 0 ]*(n)
    k2 = [ 0 ]*(n)
    k3 = [ 0 ]*(n)
    k4 = [ 0 ]*(n)
    fR = [0 ]*(n)
    ydumb = [ 0 ]*(n)
    fR = f(t,y ) # Returns RHS ’ s
    for i in range(0 , n) :
        k1[ i ] = h*fR[ i ]
    for i in range(0 , n) :
        ydumb[ i ] = y[ i ] + k1[i ]/ 2.0
    k2 = h*f( t+h/2.0 , ydumb)
    for i in range(0,n) :
        ydumb[ i ] = y[ i ] + k2[ i ]/2.0
    k3 = h*f( t+h/2.0 , ydumb )
    for i in range(0 , n) :
        ydumb[ i ] = y[ i ] + k3[ i ]
        k4 = h*f( t+h , ydumb )
        for i in range(0 , 2) :
            y[i] = y[i] + ( k1[i] + 2.0*( k2[ i ] + k3[ i ] ) + k4[ i ] )/6.0
    return y
while ( t < b) :# Time loop
    if(( t + h) > b) :
        h=b-t # Last step
        y = rk4(t,h,2 )
        t= t+h
        rate(30)
        A=np.append(A,t)
        B=np.append(B,y[0])
        C=np.append(C,y[1])
        
plot(A,B)
show()
            