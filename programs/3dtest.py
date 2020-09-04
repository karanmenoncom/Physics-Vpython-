from vpython import *
graph1 = display( width=500,height=500,title='VPython 3D Shapes',range =10)
sphere(pos=vector(0,0,0),radius=1,color=color.green)
sphere(pos=vector(0,1,-3) ,radius=1.5 ,color=color.red )
arrow(pos=vector(3,2,2),axis =vector(3,1,1) ,color=color.cyan)
cylinder(pos=vector(-3,-2,3),axis=vector(6 ,-1,5), color=color.yellow)
cone(pos=vector(-6,-6,0),axis =vector(-2,1,-0.5) , radius =2, color=color.magenta)
helix(pos=vector(-5,5,-2),axis=vector(5,0,0) ,radius=2,thickness=0.4,color=color.orange )
ring ( pos=vector( -6 ,1 ,0),axis =vector(1,1,1),radius=2, thickness =0.3,color =vector(0.3 ,0.4 ,0.6))
box(pos =vector(5 , -2 ,2),length=5,width=5,height=0.4,color=vector(0.4,0.8,0.2))
pyramid(pos=vector(2,5,2),size=vector(4,3,2),color=vector(0.7,0.7,0.2))
ellipsoid(pos=vector(-1,-7,1),axis=vector(2,1,3),length =4,height=2,width=5,color=vector(0.1,0.9,0.8))

