import importlib
from functions import scene, Engine_Render
import os




def main():
   
    mod = importlib.import_module("balls")

    render = Engine_Render()
    the_scene = scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)

    Image = render.renderNow(the_scene)


    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open("2balls.jpg","w") as myfile:
        Image.create_file_ppm(myfile)
    myfile.close()



if __name__ == "__main__":
    main()
    