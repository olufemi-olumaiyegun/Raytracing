from math import *
class vector:


    """A three element vector used in 3D graphics"""
##create constructor for the class and set default x,y,z
    def __init__(self, x=0.0,y =0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    ##set string representation of the class incase printing is neeeded
    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)

    def dot_product(self, other): #to calculate dot product of one or two vectors
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self): #calculate magnitude of a vector 
        return sqrt(self.dot_product(self))

    def normalize(self):
        return self/self.magnitude

    def __add__(self, other): ##add two vectors together and create another vector
        return vector(self.x + other.x,self.y + other.y, self.z + other.z)
     
    def __sub__(self, other):# sub two vectors together and create another vector
        return vector(self.x - other.x,self.y - other.y, self.z - other.z)
    
    def __multiply__(self, other):
        assert not isinstance(other,vector) #make sure that other is not a vector before multiplication
        return vector (self.x * other.x, self.y*other.y, self.x*other.z)

    def __rmul__(self,other):
        return self.__multiply__(other)

    def __division__(self,other):
        assert not isinstance(other,vector)
        return vector (self.x / other.x, self.y/other.y, self.x/other.z)

class Color(vector):
    pass

class image:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self,x,y,color):
        self.pixels[y][x] = color
    def create_file_ppm(self,img_file):
        def to_bytes(c):
            return round(max(min(c * 255, 255),0))
        img_file.write("P3 {} {}\n255\n".format(self.width,self.height))
        for row in self.pixels:
            for color in row:
                img_file.write("{} {} {} ".format(to_bytes(color.x),to_bytes(color.y),to_bytes(color.z)))
                img_file.write("\n")
