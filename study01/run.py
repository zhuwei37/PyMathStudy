import vector_drawing as Painter
import vectors as vector
import math
dino_vectors=[(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),
(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),
(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1)]
res=vector.add(*dino_vectors)
res=vector.translate((1,1),dino_vectors)
res=max(dino_vectors,key=vector.length)
#print(" valie is",res)

#polar_list=[(math.cos(5*x*math.pi/500.0),2*math.pi*x/1000.0) for x in range(0,1000)]
#Painter.draw(Painter.Polygon(*[vector.to_cartesian(polar) for polar in polar_list]) )
Painter.draw(Painter.Polygon( *vector.translate((8,8),vector.roatate(5*math.pi/3,dino_vectors))) )