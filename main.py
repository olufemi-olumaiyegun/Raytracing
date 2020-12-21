from functions import Color,vector,image

def main():
    WIDTH = 3
    HEIGHT = 2
    Image = image(WIDTH,HEIGHT)
    red = Color(x=1,y=0,z=0)
    green = Color(x=0,y=1,z=0)
    blue = Color(x=0,y=0,z=1)
    Image.set_pixel(0,0,red)
    Image.set_pixel(1,0,green)
    Image.set_pixel(2,0,blue)

    Image.set_pixel(0,1,red+blue)
    Image.set_pixel(1,1,red+blue+green)
    Image.set_pixel(2, 1, red * 0.001)

    myfile = open("image.ppm","w+")
    Image.create_file_ppm(myfile)



if __name__ == "__main__":
    main()