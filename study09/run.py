from draw2d import *
from draw3d import *
from vectors import add,scale
from math import *

def function(s,v,a,dt,steps):
    arrary=[]
    total=0
    for _ in range(0,steps):
        total+=dt
        x,y=s(total)
        vx,vy=v(x,y)
        ax,ay=a(vx,vy) 
        arrary.append((x,y))
    return arrary



#print(cos(20)*30,sin(20)*30)

t=0
angle=70
s=(0,0,0)
v=(1,2,0)
a=(0,-1,1)
dt=10/1000

steps=1000
position=[s]
for _ in range(0,steps):
    t+=dt
   
    s=add(s,scale(dt,v))

    v=add(v,scale(dt,a))
    
    position.append(s)
print(*position)
draw3d(Points3D(*position))