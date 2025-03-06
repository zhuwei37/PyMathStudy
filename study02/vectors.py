import math
def add(v1,v2):
    return (v1[0]+v2[0]+v1[1]+v2[1])
def add(*vectors):
    by_coordinate=zip(*vectors)
    coordinate_sums=[sum(coords) for coords in by_coordinate ]
    return tuple(coordinate_sums)
def length(v):
    return math.sqrt(sum([coord**2 for coord in v]))
def translate(translates ,vectors):
    return [(translates[0]+v[0],translates[1]+v[1]) for v in vectors]
def scale(scalar,vector):
    return tuple([scalar*v for v  in vector])
def subtract(u,v):
    return [u1-v1 for u1 ,v1 in zip(u,v)]
def distance(v1,v2):
    return length(subtract(v1,v2))
def perimeter(vectors):
    return sum([distance(vectors[i],vectors[(i+1)%len(vectors) ]) for i in range(0,len(vectors))] )
def to_cartesian(polar_vector):
    length,angle=polar_vector[0],polar_vector[1]
    return (length*math.cos(angle),length*math.sin(angle))
def to_polar(vector):
    x,y=vector[0],vector[1]
    angle=math.atan2(y,x)
    return (length(vector),angle)
def roatate(angle,vectors):
    polars=[to_polar(v) for v in vectors]
    return [to_cartesian((l,a+angle)) for l,a in polars]
def regular_polygon(n):
    if (n<3):
       return [] 
    rad=math.pi*2/n
    return [(math.cos(inc*rad),math.sin(inc*rad))  for inc in range(0,n)]

def dot(u,v):
    res=[u1*v1 for u1 ,v1 in zip(u,v)]
    return sum(res)
def  angle_between(v1,v2):
    return math.acos(
        dot(v1,v2)/(length(v1)*length(v2))
    )
def cross(u,v):
    ux,uy,uz=u
    vx,vy,vz=v
    return (uy*vz-uz*vy,uz*vx-ux*vz,ux*vy-uy*vx)
def component(v,direction):
    return (dot(v,direction)/length(direction))
def vector_to_2d(v):
    return (component(v,(1,0,0)),component(v,(0,1,0)))
def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]
def unit(v):
    return scale(1.0/length(v),v)
def normal(face):
    return (cross(subtract(face[1],face[0]),
                  subtract(face[2],face[0])
                  ))