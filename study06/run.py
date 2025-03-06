

from vectors import *
from ImageVector import *

#image1=0.5*ImageVector("./melba_face.jpg")+0.5*ImageVector("./melba5.JPG")
image_size=(300,300)
total_pixels=image_size[0]*image_size[1]
square_count=30
square_width=10

def ij(n):
    return (n//image_size[0],n%image_size[1])
def to_lowres_grayscale(img):
    matrix=[
        [0 for i in range(0,square_count)]
        for j in range(0,square_count)
    ]
    for (n,p) in enumerate(img.pixels):
        i,j = ij(n)
        weight=1.0/(3*square_width*square_width)
        matrix[i//square_width][j//square_width]+=(sum(p)*weight)
    return matrix
def from_lowers_grayscale(matrix):
    def lowres(pixels,ij):
        i,j=ij
        return pixels[i//square_width][j//square_width]
    def make_highres(limg):
        pixels=list(matrix)
        triple=lambda x:(x,x,x)
        return ImageVector([triple(lowres(matrix,ij(n))) for n in range(0,total_pixels) ])
    return make_highres(matrix)
from_lowers_grayscale(to_lowres_grayscale(ImageVector("melba2.jpg"))).show()