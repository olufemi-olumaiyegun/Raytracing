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
        return self / self.magnitude()

    def __add__(self, other): ##add two vectors together and create another vector
        return vector(self.x + other.x,self.y + other.y, self.z + other.z)
     
    def __sub__(self, other):# sub two vectors together and create another vector
        return vector(self.x - other.x,self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        assert not isinstance(other,vector) #make sure that other is not a vector before multiplication
        return vector (self.x * other, self.y*other, self.z*other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __truediv__(self,other):
        assert not isinstance(other,vector)
        return vector (self.x / other, self.y/other, self.z/other)

class color(vector):
    """Stores color as RGB triplets. An alias for Vector"""

    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        return cls(x, y, z)

class point(vector):
    """Stores 3D coordinates of a vector and also serves as an alias for vector"""
    pass

 


class sphere:
    """This is a 3d shape in a 2d space"""

    def __init__(self,center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersection(self, Ray):
        """Check if a ray intersects a sphere"""
        a = 1
        RayHitSphere = Ray.origin - self.center
        b = 2 * Ray.direction.dot_product(RayHitSphere)
        c = RayHitSphere.dot_product(RayHitSphere) - self.radius * self.radius
        descrim = b*b - 4*c

        if descrim >= 0:
            distance = (-b- sqrt(descrim))/2
            if distance > 0:
                return distance
        return None

class scene:
    """A container of the sphere, rays and actions taking place"""
    def __init__(self,camera,objects,width,height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height


class ray:
    """A ray is a radius with an origin and a direction which has been normlaized"""
    def __init__(self,origin,direction):
        self.origin = origin
        self.direction = direction.normalize()



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


class Engine_Render:
    def renderNow(self,Scene):
        width = Scene.width
        height = Scene.height
        aspectRatio = float(width)/height
        x = -1.0
        x1 = +1.0
        stepx = (x1-x)/(width - 1)
        y = -1.0 / aspectRatio
        y1 = +1.0 / aspectRatio
        stepy = (y1 - y)/(height - 1)

        camera = Scene.camera
        pixels = image(width,height)


        ##scane through each pixel and crate raysls

        for step in range(height):
            y0 = y + step * stepy
            for swim in range(width):
                x0 = x + swim * stepx
                Ray = ray(camera,point(x0,y0)-camera)

                pixels.set_pixel(swim, step, self.trace(Ray,Scene))

        return pixels
    def trace(self, Ray, Scene):
        Color = color(0,0,0)
        distance_hit, object_hit = self.nearest(Ray,Scene)
        if object_hit is None:
            return Color
        hit_position = Ray.origin + Ray.direction * distance_hit
        Color+=self.color_at(object_hit, hit_position, Scene) 
        return Color
    def nearest(self,Ray,Scene):
        distance_minimu = None
        object_hit = None

        for obj in Scene.objects:
            distance = obj.intersection(Ray)
            if distance is not None and (object_hit is None or distance < distance_minimu):
                distance_minimu = distance
                object_hit = obj

        return distance_minimu,object_hit



    def color_at(self, object_hit, hit_position, Scene):
            return object_hit.material





