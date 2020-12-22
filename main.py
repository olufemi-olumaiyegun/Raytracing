from functions import color,vector,image,sphere,point,ray,scene,Engine_Render,material,light

def main():
    WIDTH = 320
    HEIGHT = 200
    camera = vector(0,0,-1)
    objects = [sphere(point(0,0,0),0.5, material(color.from_hex("#800080")))]
    lights = [light(point(14.5,-4.5,-10.0),color.from_hex("#FFFFFF"))]

    the_scene = scene(camera, objects,lights, WIDTH, HEIGHT)
    rendering_engine= Engine_Render()
    Image = rendering_engine.renderNow(the_scene)

    with open("image.ppm","w") as myfile:
        Image.create_file_ppm(myfile)
    myfile.close()



if __name__ == "__main__":
    main()