import math
def add(v1,v2):
    return (v1[0]+v2[0]+v1[1]+v2[1])
def add(*vector):
    return  (sum([v[0] for v in vector]),sum([v[1] for v in vector]))
def length(v):
    return math.sqrt(v[0]**2+v[1]**2)
def translate(translates ,vectors):
    return [(translates[0]+v[0],translates[1]+v[1]) for v in vectors]
def scale(s,v):
    return (s*v[0],s*v[1])
def subtract(v1,v2):
    return (v1[0]-v2[0],v1[1]-v2[1])
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