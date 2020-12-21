class image:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x,y,color):
        self.pixels[y][x] = color
    def to_bytes(c):
        return round(max(min(c * 255, 255),0))
    def create_file_ppm(self,img_file):
     
        img_file.write("P3 {} {}\n255\n".format(self.width,self.height))
        for row in self.pixels:
            for color in row:
                img_file.write("{} {} {} ".format(to_bytes(color.x),to_bytes(color.y),to_bytes(color.z)))
                img_file.write("\n")