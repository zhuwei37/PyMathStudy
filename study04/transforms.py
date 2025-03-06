from vectors import *
from random import randint
################################################################
# Vector transformation functions we'll introduce in Chapter 4 #
# (also used to render the teapot)                             #
################################################################

# def compose(f1,f2):
#     def new_function(input):
#         return f1(f2(input))
#     return new_function

# def compose(f1,f2):
#     return lambda x: f1(f2(x))

def compose(*args):
    def new_function(input):
        result = input
        for f in reversed(args):
            result = f(result)
        return result
    return new_function

def curry2(f):
    def g(x):
        def new_function(y):
            return f(x,y)
        return new_function
    return g

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function

def translate_by(translation):
    def new_function(v):
        return add(translation,v)
    return new_function

def rotate_z(angle, vector):
    x,y,z = vector
    new_x, new_y = rotate2d(angle, (x,y))
    return new_x, new_y, z

def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle,v)
    return new_function

def rotate_x(angle, vector):
    x,y,z = vector
    new_y, new_z = rotate2d(angle, (y,z))
    return x, new_y, new_z

def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle,v)
    return new_function

def rotate_y(angle,vector):
    x,y,z = vector
    new_x, new_z = rotate2d(angle, (x,z))
    return new_x, y, new_z

def rotate_y_by(angle):
    def new_function(v):
        return rotate_y(angle,v)
    return new_function

B = (
    (0,2,1),
    (0,1,0),
    (1,0,-1)
)

v = (1,-2,-2)

def transform_standard_basis(transform):
    return transform((1,0,0)), transform((0,1,0)), transform((0,0,1))


def multiply_matrix_vector(matrix,vector):
    return  linear_combination(vector,*zip(*matrix))
def multiply_matrix_vector2(matrix,vector):
    return tuple(
          sum([ row[i]*vector[i] for i in range(0,len(vector))])  for row in matrix
    )
def matrix_multiply(a,b):
    return tuple(
        tuple(dot(row,col) for col in zip(*b)) for row in a
    )
def inter_matrix(n,transformation):
    def standard_basis_vecotr(i):
        return tuple(1 if i==j else 0 for j in range(1,n+1))
    standard_basis=[standard_basis_vecotr(i) for i in range(1,n+1)]
    cols=[transformation(v) for v in standard_basis]
    return tuple(zip(*cols))
def random_matrix(rows,cols,min=-2,max=2):
    return tuple(
        tuple(
            randint(min,max) for j in range(0,cols)
            for i in range(0,rows)
        )
    )
def matrix_power(power,matrix):
    result=matrix
    for i in range(1,power):
        result=matrix_multiply(result,matrix)
    return result
def transpose(matrix):
    return tuple(zip(*matrix))