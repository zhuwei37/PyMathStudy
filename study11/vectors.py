from math import sqrt, sin, cos, acos, atan2
from abc import ABCMeta,abstractclassmethod
# def add(v1,v2):
#     return (v1[0] + v2[0], v1[1] + v2[1])



# def add(*vectors):
#     by_coordinate = zip(*vectors)
#     coordinate_sums = [sum(coords) for coords in by_coordinate]
#     return tuple(coordinate_sums)

def add(*vectors):
    return tuple(map(sum,zip(*vectors)))

def subtract(v1,v2):
    return tuple(v1-v2 for (v1,v2) in zip(v1,v2))

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))

def dot(u,v):
    return sum([coord1 * coord2 for coord1,coord2 in zip(u,v)])

def distance(v1,v2):
    return length(subtract(v1,v2))

def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                    for i in range(0,len(vectors))]
    return sum(distances)

def scale(scalar,v):
    return tuple(scalar * coord for coord in v)

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def rotate2d(angle, vector):
    l,a = to_polar(vector)
    return to_cartesian((l, a+angle))

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y,x)
    return (length(vector), angle)

def angle_between(v1,v2):
    return acos(
                dot(v1,v2) /
                (length(v1) * length(v2))
            )



def cross(u, v):
    ux,uy,uz = u
    vx,vy,vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

def component(v,direction):
    return (dot(v,direction) / length(direction))

def unit(v):
    return scale(1./length(v), v)

def linear_combination(scalars,*vectors):
    scaled = [scale(s,v) for s,v in zip(scalars,vectors)]
    return add(*scaled)



class Vector( metaclass=ABCMeta):
    @abstractclassmethod
    def scale(self,scaler):
        pass
    @abstractclassmethod
    def add(self,other):
        pass
    def zero(self):
        pass
    def __neg__(self):
        return  self.scale(-1)
    def __mul__(self,scaler):
        return self.scale(scaler)
    def __rmul__(self,scaler):
        return self.scale(scaler)
    def __add__(self,other):
        return self.add(other)
    def subtract(self,other):
        return self.add(-1*other)
    def __sub__(self,other):
        return self,subtract(other)
    def __truediv__(self,scaler):
        return self.scale(1/scaler)

class Vec2(Vector):
    def zero():
        return Vec2(0,0)
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self, other):
        assert self.__class__==other.__class__
        return Vec2(self.x+other.x,self.y+other.y)
    def scale(self, scaler):
        return Vec2(scaler*self.x,scaler*self.y)
   
    def __eq__(self,other):
        assert self.__class__==other.__class__
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return "Vec2 ({} ,{})".format(self.x,self.y)
    
class Vec3(Vector):
   
    def zero():
        return Vec3(0,0,0)
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def add(self,other):
        return Vec3(self.x+other.x,self.y+other.y,self.z+other.z)
    def scale(self,scaler):
        return Vec3(self.x*scaler,self.y*scaler,self.z*scaler)
    def __eq__(self, other):
        assert self.__class__==other.__class__
        return (self.x==other.x and self.y==other.y and self.z==other.y)
    
    def __repr__(self):
        return "Vec3 ({},{},{})".format(self.x,self.y,self.z)
class CoordinateVecotr(Vector):
    def zero(self):
        return tuple(0 for i in range(0,self.dimension()))
    def dimension(self):
        pass
    def __init__(self,*vector):
        self.coordinates=tuple(x for x in vector)
    def add(self,other):
        return self.__class__(*add(self.coordinates,other.coordinates))
    def scale(self,scaler):
        return self.__class__(*scale(scaler,self.coordinates))
    def __repr__(self):
        return "{}{}".format(self.__class__.__qualname__,self.coordinates)
class Vec6(CoordinateVecotr):
    def dimension(self):
        return 6

class LinearFunction(Vec2):
    def __call__(self,input):
        return self.x*input+self.y