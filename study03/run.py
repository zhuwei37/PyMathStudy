import draw3d
import draw2d
import vectors
import matplotlib.pyplot as plt
from math import sin,cos,pi
import colors
from teapot import load_triangles
from draw_model import draw_model
import transforms as trans
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])
octahedron=[
    [(1,0,0),(0,1,0),(0,0,1)],
    [(1,0,0),(0,0,-1),(0,1,0)],
    [(1,0,0),(0,0,1),(0,-1,0)],
    [(1,0,0),(0,-1,0),(0,0,-1)],
    [(-1,0,0),(0,0,1),(0,1,0)],
    [(-1,0,0),(0,1,0),(0,0,-1)],
    [(-1,0,0),(0,-1,0),(0,0,1)],
    [(-1,0,0),(0,0,-1),(0,-1,0)],
]
def stretch_x(scalar,vecotr):
    return (scalar*vecotr[0],vecotr[1],vecotr[2])
def stretch_x_by():
    def f1(scalar):
        def f2(vector):
           return stretch_x(scalar,vector)
        return f2
    return f1 
def curry2(f):
    def new_function1(x):
        def new_function2(y):
            f(x,y)
        return new_function2
    return new_function1
def translate_by(translate):
    def new_function(v):
        return vectors.add(translate,v)
    return new_function
def vectrices(faces):
    return list(set([vertex for face in faces for vertex in face]))
def translatelleft(v):
    return vectors.add((-1,0,0),v)
def scale2_then_translatelleft(v):
    return translatelleft(scale2(v))
def render(faces,light=(1,2,3),color_map=plt.get_cmap('Blues'),lines=None):
    polygons=[]
    for face in faces:
        unit_normal=vectors.unit(vectors.normal(face))
        if unit_normal[2]>0:
            c=color_map(1-vectors.dot(vectors.unit(vectors.normal(face)),vectors.unit(light)))
            p=draw2d.Polygon2D(*vectors.face_to_2d(face),fill=c,color=lines)
            polygons.append(p)
    draw2d.draw2d(*polygons,axes=False,origin=False,grid=None)
def scale2(v):
    return vectors.scale(2.0,v)
vs=[(sin(pi*t/6),cos(pi*t/6),1.0/3) for t in range(0,24)]
#render(octahedron,color_map=plt.get_cmap('Blues'),lines=colors.black)
#print(vectors.add(*vs))
#arrows=[]
#before=vs[0]
#for index,v in enumerate(vs,1):
  #  start=before
 ##   end=vectors.add(*[v,before])
  #  before=end
    #print( end)
 #   arrows.append(draw3d.Arrow3D(end,start))
#print(arrows)
#print(vectors.cross((0,0,1),(-6,12,-6)),vectors.cross((0,0,1),(-6,12,-8)))
#draw3d.draw3d(*[draw3d.Arrow3D((1,-2,1)),draw3d.Arrow3D((-6,12,-6))])
original_triangles=load_triangles()
scaled_trigangles=trans.polygon_map(trans.scale_by(-0.5),original_triangles)
draw_model(scaled_trigangles)