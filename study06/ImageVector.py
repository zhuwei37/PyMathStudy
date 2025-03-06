from PIL import Image
from vectors import *
class ImageVector(Vector):
    size=(300,300)
    def __init__(self,input):
        try:
            img=Image.open(input).resize(ImageVector.size)
            print("11"+input)
            self.pixels=img.getdata()           
        except:
            self.pixels=input
    def image(self):
        img=Image.new('RGB',ImageVector.size)
        img.putdata( [(int(r),int(g),int(b)) for (r,g,b) in self.pixels] )
        return img
    def add(self,img2):
        return ImageVector([(r1+r2,g1+g2,b1+b2) 
                            for ((r1,g1,b1),(r2,g2,b2))
                            in zip(self.pixels,img2.pixels)])
    def scale(self,scaler):
        return ImageVector([(scaler*r,scaler*g,scaler*b) for (r,g,b) in self.pixels])
    def zero(cls):
        total_pixels=cls.size[0]*cls.size[1]
        return ImageVector([(0,0,0) for _ in range(0,total_pixels)])
    def _repr_png_(self):
        return self.image()._repr_png_()
    def show(self):
        self.image().show()
    def soild_color(r,g,b):
        return ImageVector([(r,g,b) for _ in range(0,300*300)])
    
