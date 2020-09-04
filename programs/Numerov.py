# QuantumNumerov : Quantum BS v i a Numerov ODE s o lv e r + se a rch
#from vpython import*
from pylab import *
from numpy import *
#psigr = canvas( x=0, y=0, width=600, height =300, title= 'R & L Wave Funcs ' )
#psi = curve( x= list( range(0 ,1000) ) , display=psigr , color=color . yellow )
#psi2gr = canvas( x=0,y=300,width=600, height =200, title= 'Wave func ^2 ' )
#psio = curve ( x= list( range(0 ,1000 ) ) , color=color . magenta , display=psi2gr )
#energr = canvas( x=0, y=500, width=600, height =200, title= 'Potential & E' )
#poten = curve( x= list( range(0 ,1000) ) , color=color . cyan , display=energr )
#autoen = curve( x= list( range(0 ,1000) ) , display=energr )


dl = 1e-6 # very small interval to stop bisection
ul= zeros([1501] , float )
ur = zeros([1501] , float )
k2l= zeros([1501] , float ) # k**2 le f t wavefunc
k2r= zeros([1501] , float )
n = 1501
m =5 # plot every 5 points
imax = 100
xl0 = -1000; xr0 = 1000 # leftmost , rightmost x
h = 1.0*( xr0-xl0 )/(n-1.)
amin = -0.001; amax = -0.00085 # root limits
e = amin # In i t ia l E guess
de = 0.01
ul[0] = 0.0; ul[1] = 0.00001; ur[0] = 0.0; ur[1] = 0.00001
im = 500 # match point
nl = im+2; nr = n-im+1 # l e f t , r i gh t wv
istep = 0
def V( x ) :# Square well
    if ( abs ( x ) <=500) : 
        v = -0.001
    else : v=0
    return v
def setk2 () : # k2
    for i in range(0 ,n) :
        xl = xl0+i*h
        xr = xr0-i*h
        k2l[ i ] = e-V( xl )
        k2r[ i ] = e-V( xr )
def numerov( n , h , k2 , u ) : # Numerov a lgor ithm
    b=(h**2)/12.0
    for i in range(1 , n-1) :
        u[ i +1] = (2*u[ i ]*( 1 -5*b*k2 [ i ] ) -(1.+b*k2 [ i -1])*u[i -1])/(1+b*k2 [ i +1])
setk2 ()
numerov( nl , h , k2l, ul) # Left psi
numerov( nr , h , k2r, ur ) # Right psi
fact= ur[ nr -2 ]/ul[ im ] # Scale
for i in range(0 , nl ) : 
    ul[ i ] = fact*ul[ i ]
    f0 = ( ur[ nr-1]+ ul[ nl -1]-ur[ nr-3]-ul[ nl -3])/(2*h*ur[ nr -2]) # Log de r iv
def normalize ( ) :
    potenX=([]);potenY=([])
    autoenX=([]);autoenY=([])
    asum = 0
    for i in range( 0,n) :
        if i > im :
            ul[ i ] = ur[n-i -1]
    #elabel = label ( pos=vec(700 , 500,0) , text= ' e=' , box=0, display=psigr )
    #elabel.text = ' e=%10.8 f ' %e
    #ilabel = label( pos=vec(700 ,400,0) , text= ' istep=' , box=0, display=psigr )
    #ilabel.text = ' i s t e p=%4s ' %istep
    #poten.append = [vec( -1500 ,200,0) ,vec( -1000 ,200,0) ,vec( -1000 , -200,0) ,vec(0, -200,0) ,vec(0 ,200,0) ,vec(1000 ,200,0) ]
    potenX=append(potenX,(-1500,-1000,-1000,0,0,1000))
    potenY=append(potenX,(200,200,-200,-200,200,200))
    #autoen.append = [vec( -1000,e*400000.0+200,0) ,vec(0 , e*400000.0+200,0) ]
    autoenX=append(autoenX,(-1000,0))
    autoenY=append(autoenY,(e*400000.0+200,e*400000.0+200))
    #label( pos=vec(-1150,-240,0) , text= '0.001 ' , box=0, display=energr )
    #label( pos=vec( -1000,300,0) , text= '0' , box=0, display=energr )
    #label( pos=vec( -900,180,0) , text= ' -500 ' , box=0, display=energr )
    #label( pos=vec( -100,180,0) , text= '500 ' , box=0, display=energr )
    #label( pos=vec( -500,180,0) , text= '0' , box=0, display=energr )
    #label( pos=vec(900 ,120,0) , text= 'r' , box=0, display=energr )
    j =0
    lineX=([])
    lineY=([])
    psiX=([])
    psiY=([])
    psioX=([])
    psioY=([])
    for i in range( 1 , n ,m) :
        xl = xl0 + i*h
        ul[ i ] = ul[ i ]/asum # wave function normalized

        #psi.append(pos = vec(xl - 500,10000.0*ul[ i ],0)) # ve r t ic a l l ine for match of wvfs
        psiX=append(psiX,(xl - 500))
        psiY=append(psiX,(10000.0*ul[ i ]))
    
        #line = curve( pos=[vec( -830,-500,0) ,vec( -830 ,500,0) ] ,color=color.red , display=psigr )
        lineX=append(lineX,(-830,-830))
        lineY=append(lineY,(-500,500))
        #psio.modify[ j ] = (xl -500,0,0) # plot psi
        #psio.append( pos = vec(xl -500,1.0e5*ul[ i ]**2,0))
        psioX=append(psioX,xl -500)
        psioY=append(psioY,1.0e5*ul[ i ]**2)
        j +=1
while abs ( de ) > dl and istep < imax : # bisection algorithm
    #rate (2) # Slow animation
    e1 = e
    e = ( amin+amax )/2
    for i in range(0 ,n) :
        k2l[ i ] = k2l[ i ] + e-e1
        k2r[ i ] = k2r[ i ] + e-e1
    im = 500;
    nl = im+2
    nr = n-im+1;
    numerov( nl , h , k2l, ul) # New wavefunt ions
    numerov( nr , h , k2r , ur )
    fact = ur[ nr -2 ]/ul[im ]
    for i in range(0 , nl ) : 
        ul[ i ] = fact*ul[ i ]
    f1 = ( ur [ nr-1]+ ul[ nl -1]-ur [ nr-3]-ul[ nl -3]) /(2*h*ur [ nr -2]) # Log de r iv
    #rate (2)
    if f0*f1 < 0: # Bisection loca lize root
        amax = e
        de = amax - amin
    else :
        amin = e
        de = amax - amin
        f0 = f1
    normalize()
    istep = istep + 1
plot(psiX,psiY)
plot(psioX,psioY)
plot(lineX,lineY)
plot(potenX,potenY)
plot(autoenX,autoenY)