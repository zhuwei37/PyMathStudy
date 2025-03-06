import draw3d
import draw2d
import vectors
import matplotlib.pyplot as plt
from math import sin,cos,pi
import colors
from teapot import load_triangles
from draw_model import draw_model
from transforms import * 
import sys
import camera
A=(
    (1,1,0),
    (1,0,1),
    (1,-1,1)
)
B=(
    (0,2,1),
    (0,1,0),
    (1,0,-1)
)
#print( [col for col in A])
def transform_a(v):
     return multiply_matrix_vector(A,v)

def transform_b(v):
     return multiply_matrix_vector(B,v)
print(multiply_matrix_vector( matrix_multiply(A,B),(1,2,3)))
#print(transform_a(transform_b((1,0,0))))
v=(0,1,0)
#print( multiply_matrix_vector(A ,multiply_matrix_vector(B,v)))
#print(inter_matrix(3,compose(transform_a,transform_b)))