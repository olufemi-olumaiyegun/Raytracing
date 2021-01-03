from functions import color,vector,image,sphere,point,ray,scene,Engine_Render,material,light,chessboard



WIDTH = 2560
HEIGHT = 1600

RENDERED_IMG = "balls.ppm"
CAMERA = vector(0,0.35,-1)



OBJECTS = [sphere(point(0,10000.5,1), 10000.0, chessboard(Color_1=color.from_hex("#b11226"), Color_2=color.from_hex("#b0a99f"), ambience=0.2, reflection=0.2),), sphere(point(-0.4, -0.1, 2.6), 0.6, material(color.from_hex("#32CD32")))]
LIGHTS = [light(point(-20,5,10), color.from_hex("#FFFFFF")), light(point(-5,-10.5,0), color.from_hex("#ffffff")),]



